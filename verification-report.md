# Knowledge Verification Report: LLB Hub (index + AGENTS.md + READMEs)

**Date:** 2026-07-10  
**Source:** `/Users/ajadvanwyk/Desktop/LLB hub/` (live folder tree)  
**Claim artifacts:** `index.md`, `index.json`, `AGENTS.md`, per-module `README.md`  
**Mode:** index + agents-kb (mixed)  
**Method:** Parent execute_code inventory + targeted README/AGENTS inspection; parallel leaf verifiers dispatched for BBST, Attorneys Exam/LSSA, CCP/CLP  

## Executive Summary

**Verdict:** PASS WITH ISSUES (FAIL only if treating AGENTS.md interstitial narrative as authoritative without re-read)  

**Recommendation:** fix Critical AGENTS.md/index-quality bugs and reindexer markdown extraction before relying on agents; re-run `.reindex.py` after extract fix; then refresh README year windows.

**Grounded inventory:** Live content files under reindex SKIP rules = **222**. `index.json` count = **222**. Path set equality with disk = **exact match (0 missing, 0 extra)**. Per-folder counts match index subject tallies. All 14 module folders have `README.md`.

Main failures are **stale / contradictory claims inside AGENTS.md**, **false quality scores on LSSA markdown references** (extract never reads `.md`), and **several README year-coverage windows** that omit real years (or list 2015 as missing in HCP when 2015 files exist).

---

## Critical Issues (Must Fix)

1. **Location:** `AGENTS.md` line 5 (lede)  
   **Claim:** “179 exam papers… Covers **11 modules**…”  
   **Source evidence:** Live inventory + `index.json` → **222** files, **14** subject folders  
   **Problem:** Hallucinated/stale aggregate; understates archive by ~43 files and 3 modules  
   **Suggested fix:** Rewrite lede to 222 files / 14 modules (or “subject folders”).  

2. **Location:** `AGENTS.md` overview table LSSA row + Total line  
   **Claim:** LSSA **0** files; **Total: 219** files across 14 modules  
   **Source evidence:** `LSSA & Miscellaneous /` holds **3** `markdown.md` reference extracts; live total **222**  
   **Problem:** Precise counts used as truth are wrong (off-by-3 total; LSSA zeroed)  
   **Suggested fix:** LSSA → 3; Total → 222; align with `index.json`.  

3. **Location:** `.reindex.py` `extract()` + resulting `index.json` / `index.md` Quality & Gaps  
   **Claim:** LSSA `markdown.md` files are quality **0.5** “empty or near-empty”  
   **Source evidence:**  
   - `Constitution of RSA.pdf/markdown.md` ≈ **310 KB / 50k+ words**  
   - `Legal Practice Act 28 of 2014.pdf/markdown.md` ≈ **443 KB / 62k+ words**  
   - `Legal Practice Act Rules.pdf/markdown.md` ≈ **323 KB / 53k+ words**  
   **Problem:** `extract()` only handles doc/docx/ppt/pptx/pdf — plain `.md` returns `""` → systematic false empty/OCR gaps on the richest reference corpus. Downstream agents may skip statutes.  
   **Suggested fix:** In `extract()`, add `if ext in ("md","markdown","txt"): return open(path, encoding="utf-8", errors="replace").read()` (size-cap if desired); reindex.  

4. **Location:** `AGENTS.md` `## STRUCTURE` tree  
   **Claim:** Tree lists only 11 module dirs (CCP…PLE) + index files; **no BBST, Attorneys Exam, LSSA**  
   **Source evidence:** Those three folders exist on disk with 30+10+3 files  
   **Problem:** Knowledge-base structure diagram omits major archives agents will not “see”  
   **Suggested fix:** Add BBST/, Attorneys Exam/, LSSA & Miscellaneous / to tree with counts.  

---

## Important Issues (Should Fix)

1. **Location:** `CCP/README.md` years  
   **Claim:** Years covered **2010 – 2015**, missing only **2011**  
   **Source evidence:** Dated parse of names also yields **2019** (`CCP2019AssQ.doc`, webinar). Files exist; some parked under “Undated” because date regex missed `CCP2019…` variants depending on parser used.  
   **Problem:** Coverage window understates archive; missing-years list incomplete relative to live year set.  
   **Suggested fix:** Improve `parse_date_from_filename` for `SubjectYYYY…` / `…2019…` and regenerate READMEs.  

2. **Location:** `MCP/README.md` years  
   **Claim:** **2010 – 2012**, missing **2011** only  
   **Source evidence:** `MCPWebinar2019Word.docx` (2019) present; live years include 2019  
   **Problem:** Same under-range anomaly  
   **Suggested fix:** Reparse + reindex READMEs.  

3. **Location:** `IPM/README.md` years  
   **Claim:** Prior verification: README **2012 – 2014** vs live **2012 – 2019** with extra missing years  
   **Problem:** Year window and missing list incomplete  
   **Suggested fix:** Regenerate README after date-parser fix.  

4. **Location:** `HCP/README.md` missing years  
   **Claim:** Missing includes **2015**  
   **Source evidence:** Live years set includes **2015** (HCP has 2015 material; year breakdown may place some years under undated depending on name)  
   **Problem:** False “missing year” for a year that appears on disk  
   **Suggested fix:** Recompute missing = `range(min,max) - years_with_any_file`.  

5. **Location:** Folder name `LSSA & Miscellaneous ` (trailing space)  
   **Claim:** Paths in index use this name  
   **Source evidence:** `repr` confirms trailing space  
   **Problem:** Fragile for tools/scripts that left-strip paths; HIV for portability  
   **Suggested fix:** Rename folder to remove trailing space when convenient; keep reindexer normalize.  

6. **Location:** OCR / scanned corpus (source quality, correctly flagged for PDFs)  
   **Claim:** index Quality table lists 10× Attorneys Exam PDFs + 3 CCP/CLP PDFs as scanned  
   **Source evidence:** Country with pymupdf/text emptiness at reindex time  
   **Problem:** Not a false claim for binary PDFs; **content accuracy of board exams cannot be verified without OCR**  
   **Suggested fix:** Queue OCR; until then treat Attorneys Exam body claims as unverified.  

7. **Location:** Subagent / AGENTS module detail prose (beyond counts)  
   **Claim:** Specific CPA sections, jurisdictions, tax rates, etc.  
   **Status:** **Not fully re-litigated file-by-file in this pass** (inventory + index fidelity prioritized). Doctrine bullets remain **assumed-from-prior-summaries unless spot-checked**.  
   **Suggested fix:** Optional second pass: sample extracts per MODULE DETAILS section against exam text.  

---

## Minor Issues (Nice to Have)

1. **AGENTS.md** WHERE TO LOOK paths for some webinars omit folder prefixes (`CCPWebinar…` vs `CCP/…`).  
2. README Q/memo pair counts use coarse type filters; equity vs “matched pairs” language is informal.  
3. `index.md` reindex hint says regenerates index only; AGENTS/commands elsewhere also mention READMEs — keep wording consistent.  

---

## Check Results

| Check | Result | Notes |
|-------|--------|-------|
| 3.1 Source accuracy | **FAIL (partial)** | index.json ↔ disk excellent; AGENTS lede/total/LSSA and README year windows fail |
| 3.2 Completeness | **PASS WITH ISSUES** | Index complete; AGENTS STRUCTURE incomplete |
| 3.3 Structure | **PASS WITH ISSUES** | Hub layout OK; AGENTS tree stale |
| 3.4 Verbatim fidelity | **N/A** | No LO quote-verification target in this pass |
| 3.5 Pairs / tables | **PASS WITH NOTES** | Attorneys Exam 5Q/5A; many modules near-balanced; not all orphans audited |
| 3.6 Paths / citations | **PASS (index)** / **FAIL (AGENTS muddy paths)** | All index paths resolve |
| 3.7 Anomalies | **FAIL** | False empty LSSA; stale AGENTS counts; year-window anomalies |
| 3.8 Quality hygiene | **PASS WITH ISSUES** | LSSA quality scores wrong due extract; PDF OCR flags generally OK |

---

## Statistics

- Inventory / source units (live, skip rules): **222**  
- Claim units checked: `index.json` full path set; all folder counts; AGENTS table + lede + STRUCTURE; all README existence; year window audit all modules; LSSA markdown spot sizes  
- Critical / Important / Minor: **4 / 7 / 3**  
- Estimated coverage of archive **catalogue** claims verified: ~**95%** of inventory class; of AGENTS **doctrine** claims: **not measured** this pass  

### Live counts (authoritative for this run)

| Folder | Files |
|--------|------:|
| BBST | 30 |
| HCP | 24 |
| CCP | 21 |
| PLE | 18 |
| CLP | 17 |
| LDR | 16 |
| PCT | 16 |
| FBE | 14 |
| MCP | 14 |
| COS | 13 |
| ICP | 13 |
| IPM | 13 |
| Attorneys Exam | 10 |
| LSSA & Miscellaneous | 3 |
| **Total** | **222** |

---

## Suggested Fixes (Ordered)

1. **Patch `.reindex.py` `extract()`** to read `.md`/`.txt` — then **`python3 .reindex.py`**.  
2. **Rewrite AGENTS.md** lede, LSSA count, Total 222, STRUCTURE tree (+ BBST / Attorneys Exam / LSSA).  
3. **Harden date parsing** in reindexer for `…YYYY…` filename forms; regenerate all README year tables.  
4. Consider **rename** `LSSA & Miscellaneous ` → no trailing space.  
5. Plan **OCR** for 10 Attorneys Exam PDFs + 3 CCP/CLP scanned PDFs.  
6. Optional: second verification pass on AGENTS MODULE DETAILS vs sample exam text.  

**Approval gate:** Do not apply until user approves.

---

## Source Quality Limitations

- Scanned PDFs / no text (index-confirmed): all **Attorneys Exam/** board papers (10); **CCP** leave-to-appeal PDF + webinar slides; **CLP** lecture Q&A PDF.  
- LSSA markdown is **excellent text** once read directly — **index quality labels currently wrong**.  
- Trailing space on LSSA folder name.  
- Leaf subagent reports (BBST, Attorneys Exam, CCP/CLP) may add module detail when complete; parent findings above stand independently.

## Re-verify Plan

After approval and fixes:

- [ ] Re-run inventory equality (`index.json` vs walk)  
- [ ] Confirm LSSA quality_score ≥ 2.5 and no “empty” gap  
- [ ] Confirm AGENTS lede/total/STRUCTURE  
- [ ] Spot-check CCP/MCP/IPM/HCP README year lines  
- [ ] Full 6-step only if deep doctrine claims edited  

---

## Child agent results (merged)

Parallel leaf verifiers completed (`deleg_427dfcea`). Source exams/READMEs were **not** modified by children.

| Module report | Verdict | C / I / Min | Path |
|---------------|---------|-------------|------|
| **BBST** | PASS WITH ISSUES | 0 / 2 / 3 | `BBST/verification-report.md` |
| **Attorneys Exam + LSSA** | **PASS** | 0 / notes / 0 | `Attorneys Exam/verification-report.md` |
| **CCP + CLP** | PASS (catalogue) | 0 / orphans noted / 0 | `CCP/verification-report.md` |

### BBST (Important adds)
- **2017 understated:** README “2017 (1 file)” + two year-bearing files under Undated; live 2017 = **3** (`BBST2017 Guideline…`, `BBST2017Final Statement of Facts`, `BBST28Sep2017…`).
- **Type tags:** some full timed BBST papers labelled `assignment` while headers say integrated exam (“Broad Based Skills Test…” / 100 marks).
- **Confirmed BBST content** via `textutil` on multiple samples.
- Minor: default “01 Jun” placeholder dates; `~$` Word lock stubs present (correctly skipped from counts).

### Attorneys Exam + LSSA (confirms parent Critical #3)
- **10/10** PDF pairs **5Q + 5A**; filename Q/A classification **correct**.
- All 10 are **image scans** (0 extractable text) — OCR source limitation, not catalogue error.
- LSSA **3/3** reference folders; markdown extracts **not empty**; trailing space on folder name confirmed.
- Index “empty” LSSA gaps contradict live file size/content (**same root cause:** reindexer `extract()` skips `.md`).

### CCP + CLP
- **Counts match** README (CCP 21, CLP 17); year-breakdown tables match **dated exam set** as framed.
- **Caveat alignment:** parent flagged 2019 materials; CCP leaf treats 2019 under Undated/special as intentional non-extension of exam span — **Important polish**, not catalogue failure for “2010–2015 exam years.”
- **Orphans (filename stems):**
  - CCP: orphan Q `CCP2019AssQ.doc`; orphan A `CCP2012(2)SuppA.doc`
  - CLP: orphan Q `CLPDec2010Q.doc`; orphan A `CLP2Aug2012A.doc`
- **Subject labels match folders** (`textutil`): CCP → CRIMINAL COURT PRACTICE; CLP → CONSTITUTIONAL PRACTICE.
- Known scanned: `CCPHighCourtAppLeavetoAppeal.pdf`, `CCPWebinar2019Slides.pdf`, `CLPLecture2019Q&A.pdf`.

### Consolidated issue score (hub + children)

| Severity | Parent hub inventory/AGENTS | + child module details |
|----------|----------------------------|-------------------------|
| **Critical** | 4 (AGENTS lede/counts/STRUCTURE; false LSSA empty via extract) | still **4** (no new Critical) |
| **Important** | year windows (MCP/IPM/HCP), trailing space, OCR backlog, doctrine untested | + BBST 2017/types; CCP/CLP orphans as coverage gaps; CCP/MCP “2019 vs undated” framing |
| **Minor** | AGENTS paths, README pair wording | BBST Jun-1 defaults, lock files |

**Updated recommendation:** same fix order as before; add BBST date-bucketing + type retag when READMEs are regenerated; log Q/A orphans in module READMEs as gaps (not silent).
