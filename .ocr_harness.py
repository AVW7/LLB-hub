#!/usr/bin/env python3
"""Quality-gated OCR workflow for the LLB Hub.

Commands:
  audit   Find PDFs with missing or noisy searchable text.
  compare Run local OCR into a review directory and compare candidate metrics.
  promote Install a manually reviewed candidate, preserve its baseline, reindex.

OCR candidates are never written over a paper automatically.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

HUB = Path(__file__).resolve().parent
DEFAULT_SCOPE = HUB / "Attorneys Exam" / "Official Previous Papers 2015-2023"
DEFAULT_REVIEW = Path("/private/tmp/llb-hub-ocr-review")
DEFAULT_LANGUAGES = "eng+afr"
WORD_RE = re.compile(r"(?u)\b[\w]+(?:[’'-][\w]+)*\b")
ARTIFACT_RE = re.compile(r"(?:\ufffd|(?:[^\W_]{1,3}_+){3,}|(?<=\w)[\u25a1\u25a0]+(?=\w))")
END_RE = re.compile(r"-\s*THE\s+END\s*-", re.IGNORECASE)


def inside(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_path(raw: str, fallback: Path | None = None) -> Path:
    p = Path(raw).expanduser()
    if not p.is_absolute():
        p = HUB / p
    p = p.resolve()
    if not p.exists() and fallback is not None:
        alt = (fallback / Path(raw).name).resolve()
        if alt.exists():
            return alt
    return p


def pdf_page_texts(path: Path) -> list[str]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise RuntimeError("pypdf is required. Install it for the Python interpreter running this harness.") from exc
    reader = PdfReader(str(path), strict=False)
    return [page.extract_text() or "" for page in reader.pages]


def find_sidecar(pdf: Path) -> Path | None:
    candidates = [
        pdf.with_suffix(".md"),
        pdf.parent / pdf.name / "markdown.md",
    ]
    return next((p for p in candidates if p.is_file()), None)


def visible_pdfs(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*") if p.is_file() and p.suffix.lower() == ".pdf"
                  and not any(part.startswith(".") for part in p.relative_to(root).parts))


def sidecar_body(text: str, pdf: Path) -> str:
    lines = text.splitlines()
    kept = []
    removed_title = False
    for line in lines:
        stripped = line.strip()
        if not removed_title and stripped == f"# {pdf.stem}":
            removed_title = True
            continue
        if re.match(r"^>\s*(Source|Source PDF|Extracted by|OCR engine|OCR review|Input PDF|Input SHA-256|Candidate created):", stripped, re.I):
            continue
        kept.append(line)
    return "\n".join(kept).strip()


def metrics(text: str, page_texts: list[str] | None = None) -> dict[str, Any]:
    words = WORD_RE.findall(text)
    artifact_runs = ARTIFACT_RE.findall(text)
    page_stats = None
    if page_texts is not None:
        per_page = [len(WORD_RE.findall(t)) for t in page_texts]
        page_stats = {
            "pages": len(page_texts),
            "empty_pages": sum(1 for n in per_page if n < 10),
            "page_words": per_page,
        }
    return {
        "words": len(words),
        "characters": len(text),
        "replacement_characters": text.count("\ufffd"),
        "artifact_runs": len(artifact_runs),
        "has_end_marker": bool(END_RE.search(text)),
        **(page_stats or {}),
    }


def flags_for(m: dict[str, Any], min_words: int) -> list[str]:
    flags: list[str] = []
    if m["words"] < min_words:
        flags.append("low_word_count")
    if m["replacement_characters"]:
        flags.append("replacement_characters")
    if m["artifact_runs"]:
        flags.append("visible_ocr_artifacts")
    if m.get("empty_pages", 0):
        flags.append("pages_with_little_or_no_text")
    return flags


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(HUB.resolve()).as_posix()
    except ValueError:
        return str(path)


def command_audit(args: argparse.Namespace) -> int:
    root = resolve_path(args.root)
    if not root.is_dir():
        raise RuntimeError(f"Audit root is not a directory: {root}")
    pdfs = visible_pdfs(root)
    items: list[dict[str, Any]] = []
    for pdf in pdfs:
        try:
            pages = pdf_page_texts(pdf)
            embedded = "\n".join(pages)
            sidecar = find_sidecar(pdf)
            if sidecar:
                body = sidecar_body(sidecar.read_text(encoding="utf-8", errors="replace"), pdf)
                m = metrics(body)
                flags = flags_for(m, args.min_words)
                status = "review" if flags else "sidecar_ready"
                items.append({
                    "pdf": rel(pdf),
                    "sidecar": rel(sidecar),
                    "status": status,
                    "flags": flags,
                    "sidecar_metrics": m,
                    "embedded_pdf_metrics": metrics(embedded, pages),
                })
            else:
                m = metrics(embedded, pages)
                if m["words"] >= args.min_words:
                    status = "native_text_no_sidecar"
                    flags = ["no_markdown_sidecar"]
                else:
                    status = "needs_ocr"
                    flags = ["no_markdown_sidecar", "little_or_no_embedded_text"]
                items.append({
                    "pdf": rel(pdf),
                    "sidecar": None,
                    "status": status,
                    "flags": flags,
                    "embedded_pdf_metrics": m,
                })
        except Exception as exc:
            items.append({
                "pdf": rel(pdf),
                "sidecar": None,
                "status": "error",
                "flags": ["pdf_read_error"],
                "error": str(exc),
            })

    counts: dict[str, int] = {}
    for item in items:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    selected = items if args.all else [x for x in items if x["status"] != "sidecar_ready"]
    print(json.dumps({
        "root": str(root),
        "pdf_count": len(pdfs),
        "status_counts": counts,
        "items": selected,
    }, ensure_ascii=False, indent=2))
    return 0


def find_binary(name: str, fallback: str) -> str:
    found = shutil.which(name)
    if found:
        return found
    if Path(fallback).is_file():
        return fallback
    raise RuntimeError(f"{name} was not found. Install the OCR tools or add them to PATH.")


def tool_versions(ocrmypdf: str, tesseract: str, env: dict[str, str]) -> dict[str, str]:
    ocr = subprocess.run([ocrmypdf, "--version"], capture_output=True, text=True, env=env, check=True)
    tess = subprocess.run([tesseract, "--version"], capture_output=True, text=True, env=env, check=True)
    return {
        "ocrmypdf": ocr.stdout.strip().splitlines()[0],
        "tesseract": tess.stdout.strip().splitlines()[0],
    }


def list_languages(tesseract: str, env: dict[str, str]) -> set[str]:
    p = subprocess.run([tesseract, "--list-langs"], capture_output=True, text=True, env=env, check=True)
    return {line.strip() for line in p.stdout.splitlines()[1:] if line.strip()}


def baseline_text(pdf: Path, sidecar: Path | None) -> tuple[str, str | None]:
    if sidecar:
        return sidecar_body(sidecar.read_text(encoding="utf-8", errors="replace"), pdf), sha256(sidecar)
    return "\n".join(pdf_page_texts(pdf)), None


def recommendation(old: dict[str, Any] | None, new: dict[str, Any]) -> str:
    if old is None or old["words"] < 20:
        return "new_text_candidate_review_required"
    enough_text = new["words"] >= max(20, int(old["words"] * 0.80))
    if not enough_text:
        return "candidate_has_much_less_text"
    if new["replacement_characters"] < old["replacement_characters"]:
        return "candidate_reduces_replacement_characters_review_required"
    if new["artifact_runs"] < old["artifact_runs"] and new["replacement_characters"] <= old["replacement_characters"]:
        return "candidate_reduces_artifact_runs_review_required"
    if (new["replacement_characters"] <= old["replacement_characters"]
            and new["artifact_runs"] <= old["artifact_runs"]):
        return "comparable_review_required"
    return "candidate_has_more_measured_noise"


def command_compare(args: argparse.Namespace) -> int:
    review_root = Path(args.output).expanduser().resolve()
    if inside(review_root, HUB.resolve()):
        raise RuntimeError("Review output must be outside the hub so candidates do not pollute its index.")
    if args.jobs < 1:
        raise RuntimeError("--jobs must be at least 1.")
    if args.deskew and args.mode == "redo":
        raise RuntimeError("--deskew cannot be combined with --mode redo.")
    review_root.mkdir(parents=True, exist_ok=True)
    ocrmypdf = find_binary("ocrmypdf", "/opt/homebrew/bin/ocrmypdf")
    tesseract = find_binary("tesseract", "/opt/homebrew/bin/tesseract")
    env = os.environ.copy()
    if args.tessdata_dir:
        data_dir = Path(args.tessdata_dir).expanduser().resolve()
        if not data_dir.is_dir():
            raise RuntimeError(f"Tesseract data directory not found: {data_dir}")
        if not (data_dir / "configs" / "hocr").is_file():
            raise RuntimeError("Custom tessdata directory must include configs/hocr; copy Tesseract configs into it.")
        env["TESSDATA_PREFIX"] = str(data_dir)
    versions = tool_versions(ocrmypdf, tesseract, env)
    available = list_languages(tesseract, env)
    languages = args.languages.split("+")
    missing_languages = [lang for lang in languages if lang not in available]
    if missing_languages:
        raise RuntimeError("Missing Tesseract language data: " + ", ".join(missing_languages))
    if args.rotate_pages and "osd" not in available:
        raise RuntimeError("Page rotation requires the Tesseract osd language data.")

    inputs: list[Path] = []
    for raw in args.files:
        path = resolve_path(raw, DEFAULT_SCOPE)
        if path.is_dir():
            inputs.extend(visible_pdfs(path))
        elif path.is_file() and path.suffix.lower() == ".pdf":
            inputs.append(path)
        else:
            raise RuntimeError(f"PDF not found: {raw}")
    inputs = sorted(set(p.resolve() for p in inputs))
    if not inputs:
        raise RuntimeError("No PDF files selected.")
    outside = [p for p in inputs if not inside(p, HUB.resolve())]
    if outside:
        raise RuntimeError("All inputs must be inside the LLB Hub: " + ", ".join(map(str, outside)))

    successes = 0
    failures = []
    for pdf in inputs:
        rel_slug = re.sub(r"[^A-Za-z0-9_-]+", "_", pdf.relative_to(HUB).with_suffix("").as_posix())
        item_dir = review_root / f"{rel_slug}-{datetime.now().strftime('%Y%m%dT%H%M%S%f')}"
        item_dir.mkdir(parents=True, exist_ok=False)
        sidecar = find_sidecar(pdf)
        old_text, old_hash = baseline_text(pdf, sidecar)
        old_metrics = metrics(old_text) if old_text.strip() else None
        processing_mode = args.mode
        mode_reason = "explicit selection"
        if processing_mode == "auto":
            embedded_metrics = metrics("\n".join(pdf_page_texts(pdf)))
            broken_text = embedded_metrics["replacement_characters"] or embedded_metrics["artifact_runs"]
            processing_mode = "force" if broken_text or args.deskew else "redo"
            mode_reason = "rasterize corrupt embedded text or deskew" if processing_mode == "force" else "refresh existing OCR"
        ocr_pdf = item_dir / "candidate-searchable.pdf"
        candidate_md = item_dir / "candidate.md"
        report_path = item_dir / "comparison.json"
        cmd = [ocrmypdf, "--jobs", str(args.jobs), "-l", args.languages]
        cmd.append({"redo": "--redo-ocr", "force": "--force-ocr", "skip": "--skip-text"}[processing_mode])
        if args.rotate_pages:
            cmd.append("--rotate-pages")
        if args.deskew:
            cmd.append("--deskew")
        cmd.extend([str(pdf), str(ocr_pdf)])
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
        (item_dir / "ocrmypdf.log").write_text(proc.stdout + "\n" + proc.stderr, encoding="utf-8")
        if proc.returncode:
            failures.append({"pdf": rel(pdf), "review_dir": str(item_dir), "error": proc.stderr[-2000:]})
            continue

        pages = pdf_page_texts(ocr_pdf)
        new_text = "\n\n".join(f"--- Page {i + 1} ---\n{page}" for i, page in enumerate(pages))
        new_metrics = metrics(new_text, pages)
        source_url = None
        if sidecar:
            match = re.search(r"^>\s*Source:\s*(\S+)", sidecar.read_text(encoding="utf-8", errors="replace"), re.M)
            source_url = match.group(1) if match else None
        provenance = [
            f"# {pdf.stem}",
            "",
            f"> Source PDF: {rel(pdf)}",
        ]
        if source_url:
            provenance.append(f"> Source: {source_url}")
        provenance.extend([
            f"> OCR engine: {versions['ocrmypdf']} / {versions['tesseract']}; languages {args.languages}; mode {processing_mode}.",
            f"> Candidate created: {datetime.now().astimezone().isoformat(timespec='seconds')}.",
            f"> Input SHA-256: {sha256(pdf)}",
            "",
            new_text.strip(),
            "",
        ])
        candidate_md.write_text("\n".join(provenance), encoding="utf-8")
        rec = recommendation(old_metrics, new_metrics)
        report = {
            "status": "candidate_ready_for_manual_review",
            "pdf": str(pdf),
            "pdf_relative": rel(pdf),
            "pdf_sha256": sha256(pdf),
            "sidecar": str(sidecar) if sidecar else None,
            "baseline_sha256": old_hash,
            "candidate_markdown": str(candidate_md),
            "candidate_markdown_sha256": sha256(candidate_md),
            "candidate_pdf": str(ocr_pdf),
            "candidate_pdf_sha256": sha256(ocr_pdf),
            "candidate_metrics": new_metrics,
            "baseline_metrics": old_metrics,
            "recommendation": rec,
            "versions": versions,
            "languages": args.languages,
            "mode": processing_mode,
            "requested_mode": args.mode,
            "mode_reason": mode_reason,
            "command": cmd,
        }
        report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        successes += 1
        print(json.dumps({
            "pdf": rel(pdf),
            "candidate": str(candidate_md),
            "report": str(report_path),
            "baseline_metrics": old_metrics,
            "candidate_metrics": new_metrics,
            "recommendation": rec,
        }, ensure_ascii=False))
    print(json.dumps({"completed": successes, "failed": failures}, ensure_ascii=False, indent=2))
    return 1 if failures else 0


def command_promote(args: argparse.Namespace) -> int:
    report_path = Path(args.report).expanduser().resolve()
    if not report_path.is_file() or report_path.name != "comparison.json":
        raise RuntimeError("Provide a comparison.json generated by the compare command.")
    if inside(report_path, HUB.resolve()):
        raise RuntimeError("Comparison reports must be outside the hub.")
    report = json.loads(report_path.read_text(encoding="utf-8"))
    pdf = Path(report["pdf"]).resolve()
    relative_pdf = Path(report["pdf_relative"])
    if relative_pdf.is_absolute() or ".." in relative_pdf.parts:
        raise RuntimeError("Comparison report contains an invalid relative PDF path.")
    if (HUB / relative_pdf).resolve() != pdf:
        raise RuntimeError("Comparison report PDF paths do not match; generate a fresh comparison.")
    candidate = Path(report["candidate_markdown"]).resolve()
    candidate_pdf = Path(report["candidate_pdf"]).resolve()
    if not inside(pdf, HUB.resolve()) or not pdf.is_file():
        raise RuntimeError("Report source PDF is missing or outside the hub.")
    if inside(candidate, HUB.resolve()) or candidate.parent != report_path.parent:
        raise RuntimeError("Candidate must be beside its comparison report and outside the hub.")
    if not candidate.is_file():
        raise RuntimeError(f"Candidate Markdown not found: {candidate}")
    if sha256(candidate) != report.get("candidate_markdown_sha256"):
        raise RuntimeError("Candidate Markdown changed after comparison; generate a fresh candidate.")
    if candidate_pdf.parent != report_path.parent or not candidate_pdf.is_file():
        raise RuntimeError("Candidate OCR PDF must be present beside its comparison report.")
    if sha256(candidate_pdf) != report.get("candidate_pdf_sha256"):
        raise RuntimeError("Candidate OCR PDF changed after comparison; generate a fresh candidate.")
    if sha256(pdf) != report["pdf_sha256"]:
        raise RuntimeError("Source PDF changed after comparison; generate a fresh candidate.")
    current_sidecar = find_sidecar(pdf)
    target = current_sidecar.resolve() if current_sidecar else pdf.with_suffix(".md").resolve()
    recorded_target = Path(report["sidecar"]).resolve() if report.get("sidecar") else pdf.with_suffix(".md").resolve()
    if recorded_target != target or not inside(target, HUB.resolve()):
        raise RuntimeError("Target sidecar changed or is outside the hub; generate a fresh comparison.")
    current_hash = sha256(target) if target.is_file() else None
    if current_hash != report.get("baseline_sha256"):
        raise RuntimeError("Existing sidecar changed after comparison; review the new baseline before promoting.")
    if report.get("status") != "candidate_ready_for_manual_review":
        raise RuntimeError("Comparison report is not promotable.")
    backup = None
    if target.exists():
        backup_dir = report_path.parent / "backups"
        backup_dir.mkdir(exist_ok=True)
        backup = backup_dir / f"{target.name}.{datetime.now().strftime('%Y%m%dT%H%M%S')}.bak"
        shutil.copy2(target, backup)
    with tempfile.NamedTemporaryFile(prefix=f".{target.name}.", suffix=".tmp", dir=target.parent, delete=False) as f:
        tmp = Path(f.name)
    try:
        shutil.copy2(candidate, tmp)
        os.replace(tmp, target)
    finally:
        if tmp.exists():
            tmp.unlink()
    print(f"Promoted reviewed candidate to {rel(target)}")
    if backup:
        print(f"Saved previous sidecar to {backup}")
    if not args.no_reindex:
        proc = subprocess.run([sys.executable, str(HUB / ".reindex.py")], cwd=HUB, text=True, capture_output=True)
        print(proc.stdout, end="")
        if proc.stderr:
            print(proc.stderr, file=sys.stderr, end="")
        if proc.returncode:
            raise RuntimeError(f"Sidecar promoted, but reindex failed with exit {proc.returncode}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit and review OCR for LLB Hub PDFs.")
    sub = parser.add_subparsers(dest="command", required=True)

    audit = sub.add_parser("audit", help="find PDFs with missing or noisy text")
    audit.add_argument("--root", default=str(DEFAULT_SCOPE), help="PDF folder to inspect; defaults to the official board-paper archive.")
    audit.add_argument("--min-words", type=int, default=250, help="text below this count is flagged for review.")
    audit.add_argument("--all", action="store_true", help="include sidecars that pass the basic checks.")
    audit.set_defaults(func=command_audit)

    compare = sub.add_parser("compare", help="generate OCR candidates outside the hub for review")
    compare.add_argument("--files", nargs="+", required=True, help="PDF paths or directories inside the hub.")
    compare.add_argument("--output", default=str(DEFAULT_REVIEW), help="review folder, outside the hub.")
    compare.add_argument("--languages", default=DEFAULT_LANGUAGES, help="Tesseract languages, for example eng+afr.")
    compare.add_argument("--jobs", type=int, default=2, help="OCRmyPDF worker count.")
    compare.add_argument("--mode", choices=("auto", "redo", "force", "skip"), default="auto", help="auto rasterizes corrupt embedded text; otherwise refreshes OCR.")
    compare.add_argument("--rotate-pages", action="store_true", help="detect and correct rotation; requires osd data.")
    compare.add_argument("--deskew", action="store_true", help="deskew pages; unavailable in redo mode.")
    compare.add_argument("--tessdata-dir", help="optional Tesseract data directory with requested models and configs/hocr.")
    compare.set_defaults(func=command_compare)

    promote = sub.add_parser("promote", help="install a manually reviewed candidate and refresh the index")
    promote.add_argument("report", help="comparison.json generated by the compare command.")
    promote.add_argument("--reviewed", action="store_true", help="confirm that candidate.md was manually checked.")
    promote.add_argument("--no-reindex", action="store_true", help="leave index regeneration for a later run.")
    promote.set_defaults(func=command_promote)

    args = parser.parse_args()
    if args.command == "promote" and not args.reviewed:
        parser.error("promote requires --reviewed after you have checked candidate.md.")
    try:
        return args.func(args)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
