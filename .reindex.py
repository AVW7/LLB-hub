#!/usr/bin/env python3
"""
LLB hub re-indexer.
Scans the folder, extracts text (textutil for .doc/.docx/.ppt, pymupdf for PDF if available),
classifies each file, and regenerates index.md + index.json.

Usage:
    python3 .reindex.py
Re-run any time files are added/removed/changed. Non-destructive to source files.

Requires: macOS `textutil` (built in). PDF text extraction is optional; if pymupdf is
missing or a PDF is image-only/scanned, it is flagged as "scanned/no extractable text".
"""
import os, re, json, subprocess, datetime, hashlib
from collections import defaultdict

HUB = os.path.dirname(os.path.abspath(__file__))
SUBJECTS = {
    "CCP": "Criminal Court Practice (Module 1)",
    "CLP": "Constitutional Practice (Module 1)",
    "COS": "Legal Costs (Module 2.1)",
    "FBE": "Forms of Business Enterprise (Module 3.x)",
    "HCP": "High Court Practice (Module 2.1)",
    "MCP": "Magistrate's Court Practice (Module 2.1)",
    "PCT": "Professional Conduct (Module 1)",
    "PLE": "Professional Legal Ethics (Module 4)",
    "LDR": "Labour Dispute Resolution (Module 3.2)",
    "IPM": "Introduction to Practice Management (Module 4)",
    "ICP": "Introduction to Conveyancing Practice (Module 3.2)",
    "BBST": "Broad Based Skills Test (Integrated Practical Exam)",
    "Attorneys Exam": "Attorneys Admission Examination (Board Exam)",
    "LSSA": "LSSA Reference Materials and Miscellaneous",
}
SKIP = {".DS_Store", "index.md", "index.json", "AGENTS.md", "README.md", ".reindex.py", "verification-report.md"}
# markdown.md files inside PDF extraction folders ARE indexed (LSSA reference materials)

# optional pdf extractor
_PDF_PY = None
for cand in ("/tmp/pdfvenv/bin/python",):
    if os.path.exists(cand):
        _PDF_PY = cand
        break


def extract(path):
    ext = path.lower().rsplit(".", 1)[-1]
    try:
        if ext in ("doc", "docx", "ppt", "pptx"):
            r = subprocess.run(["textutil", "-convert", "txt", "-stdout", path],
                               capture_output=True, text=True, timeout=90)
            return r.stdout or ""
        if ext == "pdf" and _PDF_PY:
            code = ("import sys,fitz;d=fitz.open(sys.argv[1]);"
                    "print(' '.join((''.join(p.get_text() for p in d)).split()))")
            r = subprocess.run([_PDF_PY, "-c", code, path],
                               capture_output=True, text=True, timeout=120)
            return r.stdout or ""
        if ext in ("md", "markdown", "txt"):
            return open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return ""
    return ""


def parse_name(fname, rel_path=""):
    """Return (subject, role) from the naming convention."""
    stem = os.path.splitext(fname)[0]
    subj = None
    up = stem.upper()
    # Try exact matches first (CCP, CLP, etc.)
    for s in SUBJECTS:
        if up.startswith(s.upper()):
            subj = s
            break
    # Handle special cases for folder names with spaces
    if not subj:
        if up.startswith("ATTEXAM"):
            subj = "Attorneys Exam"
        elif up.startswith("ATTORNEY"):
            subj = "Attorneys Exam"
        elif up.startswith("LSSA"):
            subj = "LSSA"
        elif up.startswith("LEGAL PRACTICE") or up.startswith("CONSTITUTION"):
            subj = "LSSA"
    # Check parent folder for extracted PDF content (e.g., AttExam9Feb2016Q.pdf/markdown.md)
    pdf_parent = None
    if ".pdf/" in rel_path:
        pdf_parent = rel_path.split(".pdf/")[0].split("/")[-1]
        parent_up = pdf_parent.upper()
        if not subj:
            if parent_up.startswith("ATTEXAM"):
                subj = "Attorneys Exam"
            elif parent_up.startswith("ATTORNEY"):
                subj = "Attorneys Exam"
    # Check top-level module folder if still not matched
    if not subj and rel_path.startswith("./"):
        top_folder = rel_path[2:].split("/", 1)[0].rstrip()
        if top_folder in SUBJECTS:
            subj = top_folder
        elif top_folder.startswith("LSSA"):
            subj = "LSSA"
    # Use parent folder name for role detection when dealing with extracted PDF markdown files
    role_stem = pdf_parent if pdf_parent else stem
    role_up = role_stem.upper()
    role = "general"
    if role_up.endswith("Q") or "ASSQ" in role_up or "Q&A" in role_up.replace(" ", ""):
        role = "question"
    if role_up.endswith("A") or "ASSA" in role_up or role_up.endswith("SUPPA"):
        role = "answer"
    if "SLIDE" in role_up or "WEBINAR" in role_up:
        role = "slides"
    if "LECTURE" in role_up:
        role = "lecture"
    if "EXAMPLE" in role_up or "APPLEAVE" in role_up or "APPLEAVETOAPPEAL" in role_up:
        role = "template"
    return subj, role


def detect_type(text, role, fname):
    t = text.lower()
    # Handle markdown.md files based on role (PDF extractions from Attorneys Exam, etc.)
    if fname.lower() == "markdown.md":
        if role == "question":
            return "exam_question"
        if role == "answer":
            return "marking_memo"
        return "reference"
    if role == "slides":
        return "slides"
    if role == "template":
        return "template"
    if role == "question":
        if "assignment" in t and ("assq" in fname.lower() or "assignment" in fname.lower()):
            return "assignment"
        return "exam_question"
    if (("guideline to markers" in t or "memorandum" in t or "guide" in t) and role == "answer") or role == "answer":
        return "marking_memo"
    if role == "lecture":
        return "lecture_qa"
    return "general"


TOPIC_KEYWORDS = {
    "bail": "bail",
    "section 115": "s115-statement",
    "section 112": "s112-statement",
    "plea": "plea",
    "leave to appeal": "leave-to-appeal",
    "appeal": "appeal",
    "bill of costs": "bill-of-costs",
    "allocatur": "allocatur",
    "allocator": "allocatur",
    "vat": "vat",
    "taxing master": "taxation",
    "party and party": "party-and-party-costs",
    "de bonis propriis": "costs-de-bonis-propriis",
    "close corporation": "close-corporation",
    "partnership": "partnership",
    "sole proprietor": "sole-proprietorship",
    "pre-incorporation": "pre-incorporation-contract",
    "pre- incorporation": "pre-incorporation-contract",
    "trust": "trust",
    "judicial management": "judicial-management",
    "bill of rights": "bill-of-rights",
    "locus standi": "locus-standi",
    "constitution": "constitution",
    "criminal procedure act": "criminal-procedure-act",
    "private defence": "private-defence",
    "culpable homicide": "culpable-homicide",
    "docket": "police-docket",
}


def topics(text, subj):
    t = text.lower()
    found = []
    for k, v in TOPIC_KEYWORDS.items():
        if k in t and v not in found:
            found.append(v)
    base = {"CCP": "criminal-court-practice", "CLP": "constitutional-practice",
            "COS": "legal-costs", "FBE": "forms-of-business-enterprise"}.get(subj)
    if base and base not in found:
        found.insert(0, base)
    return found[:8]


def describe(subj, role, text):
    label = {"question": "exam question paper", "answer": "marking memorandum / model answers",
             "slides": "webinar/lecture slide deck", "lecture": "lecture Q&A",
             "template": "precedent/template document",
             "reference": "reference material (legislation/constitution)"}.get(role, "document")
    sub = SUBJECTS.get(subj, "").split(" (")[0] if subj else "LLB material"
    return f"{sub} — {label}"


def quality(text, ext, role):
    words = len(text.split())
    gaps = []
    score = 3.0
    if ext == "pdf" and words < 20:
        gaps.append("scanned/no extractable text (OCR needed)")
        score = 1.0
    elif ext in ("ppt", "pptx") and words < 20:
        gaps.append("binary slides / limited extractable text")
        score = 1.5
    elif words < 10:
        gaps.append("empty or near-empty")
        score = 0.5
    else:
        # exam papers are terse by design; judge structure lightly
        if "question" not in text.lower() and role in ("question", "answer"):
            score -= 0.3
    return round(score, 1), gaps


def parse_date_from_filename(filename):
    """Extract date from filename like 'CCP30Jan2010Q.doc' or 'HCP2012(1)Q.doc'"""
    # Try: YYYY-MM-DD pattern first (AttExam 2016-02-09.md)
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', filename)
    if m:
        return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    # Try: DDMMMYYYY pattern (30Jan2010)
    m = re.search(r'(\d{1,2})(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\d{4})', filename, re.I)
    if m:
        day, mon, year = int(m.group(1)), m.group(2).capitalize(), int(m.group(3))
        mon_num = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}[mon]
        return datetime.date(year, mon_num, day)
    # Try: MMMYYYY (Jul2015)
    m = re.search(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\d{4})', filename, re.I)
    if m:
        mon, year = m.group(1).capitalize(), int(m.group(2))
        mon_num = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}[mon]
        return datetime.date(year, mon_num, 15)
    # Try: YYYY(N) pattern like 2012(1)
    m = re.search(r'(\d{4})\s*\(\s*\d+\s*\)', filename)
    if m:
        return datetime.date(int(m.group(1)), 6, 1)
    # Try: year only (Dec2010)
    m = re.search(r'Dec(\d{4})', filename, re.I)
    if m:
        return datetime.date(int(m.group(1)), 12, 1)
    # Try: bare YYYY after subject prefix (BBST2017, HCP2015)
    m = re.search(r'(?:BBST|HCP|CCP|CLP|MCP|PLE|PCT|COS|FBE|LDR|ICP|IPM|AttExam) *(\d{4})(?!\d)', filename, re.I)
    if m:
        return datetime.date(int(m.group(1)), 6, 1)
    return None


def generate_subdir_readmes(entries, subjects):
    """Generate README.md for each subdirectory with year coverage and gaps."""
    # Group files by folder
    by_folder = defaultdict(list)
    for e in entries:
        path = e["path"].lstrip("./")
        # Get first folder component only (handles nested paths like "LSSA/Constitution.pdf/markdown.md")
        parts = path.split("/")
        if len(parts) > 1:
            folder = parts[0]
        else:
            folder = os.path.dirname(path)
        if folder:
            # Normalize folder name for matching (strip trailing spaces)
            by_folder[folder.rstrip()].append(e)

    for folder, files in sorted(by_folder.items()):
        lines = []
        # Get subject name - handle folder names with spaces
        # Try exact match, then uppercase match, then strip spaces
        folder_clean = folder.rstrip()
        subject_name = subjects.get(folder_clean, subjects.get(folder_clean.upper(), subjects.get(folder_clean.split()[0], folder_clean)))

        lines.append(f"# {folder} — Contents Overview")
        lines.append("")
        lines.append(f"**Module:** {subject_name}")
        lines.append(f"**Total files:** {len(files)}")
        lines.append("")

        # Parse dates
        dated_files = []
        undated_files = []
        years = set()

        for e in files:
            fname = os.path.basename(e["path"])
            dt = parse_date_from_filename(fname)
            if dt:
                dated_files.append((dt, fname, e["type"], e["path"]))
                years.add(dt.year)
            else:
                undated_files.append((fname, e["type"], e["path"]))

        # Years covered
        if years:
            min_year, max_year = min(years), max(years)
            lines.append(f"**Years covered:** {min_year} – {max_year}")
            all_years = set(range(min_year, max_year + 1))
            missing = sorted(all_years - years)
            if missing:
                lines.append(f"**Missing years:** {', '.join(map(str, missing))}")
            lines.append("")

        # Year breakdown
        if years:
            lines.append("## Year Breakdown")
            lines.append("")
            by_year = defaultdict(list)
            for dt, fname, ftype, path in dated_files:
                by_year[dt.year].append((dt, fname, ftype, path))

            for year in sorted(by_year.keys(), reverse=True):
                items = sorted(by_year[year])
                lines.append(f"### {year} ({len(items)} files)")
                lines.append("")
                for dt, fname, ftype, path in items:
                    date_str = dt.strftime("%d %b")
                    # Show extracted PDF source folder for markdown files
                    display_name = fname
                    if fname == "markdown.md" and ".pdf/" in path:
                        pdf_name = path.split(".pdf/")[0].split("/")[-1] + ".pdf"
                        display_name = f"{pdf_name}/markdown.md"
                    lines.append(f"- **{display_name}** — {ftype} ({date_str})")
                lines.append("")

        # Undated files
        if undated_files:
            lines.append("## Undated / Special Files")
            lines.append("")
            for fname, ftype, path in sorted(undated_files):
                # For files in subfolders, show the parent folder name
                parent = os.path.basename(os.path.dirname(path))
                if parent and parent != folder:
                    lines.append(f"- **{parent}/{fname}** — {ftype}")
                else:
                    lines.append(f"- **{fname}** — {ftype}")
            lines.append("")

        # Q/A pair status
        q_files = [e for e in files if e["type"] == "exam_question"]
        a_files = [e for e in files if e["type"] == "marking_memo"]
        lines.append("## Question/Memo Pairs")
        lines.append("")
        lines.append(f"- Exam question papers: {len(q_files)}")
        lines.append(f"- Marking memoranda: {len(a_files)}")
        lines.append("")

        # Write file - find actual folder path (preserve trailing spaces)
        actual_folder_path = None
        for d in os.listdir(HUB):
            if os.path.isdir(os.path.join(HUB, d)) and not d.startswith('.'):
                if d.rstrip() == folder_clean:
                    actual_folder_path = d
                    break
        if actual_folder_path:
            readme_path = os.path.join(HUB, actual_folder_path, "README.md")
            with open(readme_path, "w") as fh:
                fh.write("\n".join(lines))

def main():
    entries = []
    skip_dirs = {"pages", "Mistral OCR 2026-10-19", "exports", "assets", "Logs", "Templates", "people", "projects", "Attachments"}
    root_skip_files = {"CLAUDE.md", "_CLAUDE.md", "LEARNINGS.md", "MEMORY.md", "brain.md", "decisions.md", "LLB Hub Dashboard.md", "LLB Hub.base"}
    for root, dirs, files in os.walk(HUB):
        # Skip hidden dirs, PDF page extraction subdirectories, and alternate OCR / non-archive root dirs
        rel_root = os.path.relpath(root, HUB)
        dirs[:] = [
            d for d in dirs
            if not d.startswith(".")
            and d not in skip_dirs
            and not (rel_root == "." and d == "notes")
        ]
        for f in sorted(files):
            if f.startswith(".") or f.startswith("~$") or f in SKIP:
                continue
            if rel_root == "." and f in root_skip_files:
                continue
            ext = f.lower().rsplit(".", 1)[-1]
            if ext in ("zip", "json"):
                continue
            path = os.path.join(root, f)
            rel = "./" + os.path.relpath(path, HUB)
            # Skip if inside a pages/ subdirectory (PDF extraction artifacts)
            if "/pages/" in rel:
                continue
            subj, role = parse_name(f, rel)
            # Check folder path for subject assignment (handles LSSA & Miscellaneous / with trailing space)
            if not subj:
                if "LSSA & Miscellaneous" in rel or rel.startswith("./LSSA"):
                    subj = "LSSA"
            text = extract(path)
            typ = detect_type(text, role, f)
            tps = topics(text, subj)
            desc = describe(subj, role, text)
            q, gaps = quality(text, ext, role)
            entries.append({
                "path": rel,
                "subject": SUBJECTS.get(subj, "Uncategorised"),
                "role": role,
                "type": typ,
                "topics": tps,
                "description": desc,
                "size_bytes": os.path.getsize(path),
                "quality_score": q,
                "gaps": gaps,
            })

    entries.sort(key=lambda e: e["path"])
    now = datetime.date.today().isoformat()

    # index.json
    topic_index, type_index = {}, {}
    for e in entries:
        for tp in e["topics"]:
            topic_index.setdefault(tp, []).append(e["path"])
        type_index.setdefault(e["type"], []).append(e["path"])
    js = {"version": "1.0", "lastUpdated": now, "count": len(entries),
          "subjects": SUBJECTS, "entries": entries,
          "topicIndex": {k: sorted(v) for k, v in sorted(topic_index.items())},
          "typeIndex": {k: sorted(v) for k, v in sorted(type_index.items())}}
    with open(os.path.join(HUB, "index.json"), "w") as fh:
        json.dump(js, fh, indent=2, ensure_ascii=False)


    # index.md
    lines = []
    lines.append("# LLB Hub — Index")
    lines.append("")
    lines.append(f"**Scanned:** {len(entries)} files across {len(SUBJECTS)} subject folders  ")
    lines.append(f"**Last updated:** {now}  ")
    lines.append("**Source:** LSSA / School for Legal Practice past exam papers, memoranda, "
                 "assignments, webinar slides and precedents.")
    lines.append("")
    lines.append("> Re-index anytime after adding/removing files: `python3 \".reindex.py\"` "
                 "from this folder. Regenerates `index.md` + `index.json` (source files untouched).")
    lines.append("")
    lines.append("## Subjects")
    lines.append("")
    lines.append("| Code | Subject | Files |")
    lines.append("|------|---------|-------|")
    for s, name in SUBJECTS.items():
        n = sum(1 for e in entries if e["subject"] == name)
        lines.append(f"| {s} | {name} | {n} |")
    lines.append("")

    # gaps
    gapped = [e for e in entries if e["gaps"] or e["quality_score"] < 2.5]
    if gapped:
        lines.append("## Quality & Gaps")
        lines.append("")
        lines.append("| Path | Type | Quality | Gaps |")
        lines.append("|------|------|---------|------|")
        for e in gapped:
            lines.append(f"| {e['path']} | {e['type']} | {e['quality_score']} | "
                         f"{'; '.join(e['gaps']) or '—'} |")
        lines.append("")

    # files by subject
    for s, name in SUBJECTS.items():
        subset = [e for e in entries if e["subject"] == name]
        if not subset:
            continue
        lines.append(f"## {s}/ — {name}")
        lines.append("")
        for e in subset:
            tp = ", ".join(e["topics"][:5])
            # Show PDF source folder for extracted markdown files
            display_name = os.path.basename(e['path'])
            if display_name == "markdown.md" and ".pdf/" in e['path']:
                pdf_folder = e['path'].split(".pdf/")[0].rsplit("/", 1)[-1]
                display_name = f"{pdf_folder}/markdown.md"
            lines.append(f"- **[{display_name}]({e['path']})** "
                         f"*({e['type']}"
                         + (f", topics: {tp}" if tp else "") + ")* — "
                         + e["description"]
                         + (f"  ⚠️ {'; '.join(e['gaps'])}" if e["gaps"] else ""))
        lines.append("")

    with open(os.path.join(HUB, "index.md"), "w") as fh:
        fh.write("\n".join(lines) + "\n")

    # Generate README.md for each subdirectory
    generate_subdir_readmes(entries, SUBJECTS)

    print(f"Indexed {len(entries)} files. Wrote index.md, index.json, and README.md files.")
    for e in gapped:
        print("  GAP:", e["path"], e["gaps"])


if __name__ == "__main__":
    main()
