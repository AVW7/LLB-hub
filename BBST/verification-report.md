# Knowledge Verification Report: BBST/README.md

**Date:** 2026-07-10  
**Source:** `/Users/ajadvanwyk/Desktop/LLB hub/BBST/` (live folder inventory + `textutil` samples)  
**Claim artifact:** `/Users/ajadvanwyk/Desktop/LLB hub/BBST/README.md`  
**Mode:** index  
**Method:** inline leaf verification (knowledge-verifier 6-step protocol)  
**ALLOW_FIXES:** no (report only)

## Executive Summary

**Verdict:** PASS WITH ISSUES  
**Recommendation:** ready for inventory/count use; fix Important catalogue framing (undated vs 2017, type labels) before agents rely on per-file types or “undated” metadata

Live inventory (after SKIP rules: `~$…`, `README.md`, `.DS_Store`) is **exact**: 30 content files, all names listed in the README present on disk, no extra non-SKIP content. Span **2010–2018** with **2011** missing is correct. Claimed **exam_question = 5** and **marking_memo = 9** match the README’s own type tags on the listed files. Sampled binary `.doc` bodies are Broad Based Skills Test / School for Legal Practice skills-test materials.

Main risks: (1) two 2017-named files are parked under **Undated / Special** while the 2017 year bucket lists only 1 file; (2) some `assignment` vs `exam_question` tags conflict with document self-identification.

## Critical Issues (Must Fix)

None.

## Important Issues (Should Fix)

1. **Location:** README §“### 2017 (1 files)” + §“## Undated / Special Files”  
   **Claim:** 2017 has 1 file; two further files are undated/special: `BBST2017 Guideline writing BBST.docx`, `BBST2017Final Statement of Facts.doc`.  
   **Source evidence:** Year-token inventory on disk:
   - 2017 (3): `BBST2017 Guideline writing BBST.docx`, `BBST2017Final Statement of Facts.doc`, `BBST28Sep2017 Statement of Facts.docx`
   - No content file lacks a `20xx` year token (truly undated count = **0**).  
   **Problem:** Misleading catalogue structure. Total still reconciles (year sections 28 + undated 2 = 30), but “Undated” is wrong for year-bearing names, and 2017 coverage is understated in the year table.  
   **Suggested fix:** Move both 2017-named specials into **### 2017 (3 files)** (optionally keep a “Special / non-exam” flag in the line annotation), set undated = none or only files without year tokens.  
   **Severity:** Important  

2. **Location:** Year breakdown type tags for several `*Q.doc` entries (e.g. `BBST2013(1)Q.doc` → assignment; `BBST2016(1)Q.doc` → exam_question)  
   **Claim:** `BBST2013(1)Q.doc` — assignment; similar assignment tags for other formal Q packs (2013–2014 Final/Supp Q).  
   **Source evidence:** `textutil -convert txt -stdout BBST2013(1)Q.doc` header:  
   > “BROAD BASED SKILLS TEST OF THE SCHOOL FOR LEGAL PRACTICE … 2013(1) … Time: 4 Hours 30 Minutes … Marks: 100 … this examinations …”  
   Contrasts with README labeling that paper as **assignment**.  
   **Problem:** Type taxonomy is inconsistent with document self-description; agents matching Q/memo pairs by type may misroute “assignment” packs that are full BBST exam papers.  
   **Suggested fix:** Re-tag formal timed BBST papers as `exam_question` (or introduce an explicit `integrated_exam` type) and reserve `assignment` only for true formative tasks if any exist.  
   **Severity:** Important  

## Minor Issues (Nice to Have)

1. **Location:** Most line annotations use “(01 Jun)” as date  
   **Claim:** e.g. BBST2013/2014/2015/2016 files dated 01 Jun; contrast dated exceptions (09 Jun, 20 Apr, 28 Sep, 15 Dec).  
   **Source evidence:** Filenames mostly lack day/month; default Jun 1 is not independently verified from content for the bulk set.  
   **Problem:** Placeholder calendar dates presented as concrete metadata.  
   **Suggested fix:** Prefer “year / sitting (1)/(2) only” when day is unknown, or extract real dates from headers where present.  
   **Severity:** Minor  

2. **Location:** Live folder hygiene (not claimed in README counts)  
   **Claim:** N/A (README total 30 correctly excludes non-content).  
   **Source evidence:** Two Word lock stubs present: `~$ST2014(1)FinalQ&A.doc`, `~$ST2014(2)Q&A.doc`.  
   **Problem:** Clutter; correct SKIP from content counts but can confuse manual listing.  
   **Suggested fix:** Delete lock files when Word is closed; optional note in README hygiene.  
   **Severity:** Minor  

3. **Location:** §“## Question/Memo Pairs”  
   **Claim:** Exam question papers: 5; Marking memoranda: 9 only.  
   **Source evidence:** README self-tags also imply **6 assignment** + **10 general** lines; live pair completeness is not claimed as full matched sets.  
   **Problem:** Incomplete headline (omits assignment/general tallies) — accurate but thin for agents.  
   **Suggested fix:** Add assignment/general counts and note unpaired Q or SOF-only years.  
   **Severity:** Minor  

## Check Results

| Check | Result | Notes |
|-------|--------|-------|
| 3.1 Source accuracy | PASS WITH ISSUES | File names, totals, missing year, Q/memo headline counts match. Undated framing and some type tags disagree with live year tokens / document headers. |
| 3.2 Completeness | PASS | All 30 content files listed; no silent omitted content file; year sections + undated reconcile to 30. |
| 3.3 Structure | PASS WITH ISSUES | Consistent year-table layout; 2017 vs Undated split imperfect. |
| 3.4 Verbatim fidelity | N/A | No labeled statutory/LO quotes in README. |
| 3.5 Pairs / tables | PASS | Exam Q 5 + memos 9 match labeled rows; not a full matched-pair matrix claim. |
| 3.6 Paths / citations | PASS | Every README basename resolves under `BBST/`; zero missing / zero extra (after SKIP). |
| 3.7 Anomalies | PASS WITH ISSUES | No hallucinated files/years. False “undated” for 2017-named files. Placeholder (01 Jun). Lock files on disk. |
| 3.8 Quality hygiene | PASS WITH ISSUES | Counts clean; date placeholders + lock pollution minor. |

## Statistics

### Live inventory (skip `~$`, `.DS_Store`, `README.md`, this report)

| Metric | README claim | Live | Match |
|--------|--------------|------|-------|
| Total content files | 30 | 30 | Yes |
| Years covered | 2010 – 2018 | 2010, 2012–2018 | Yes (span) |
| Missing years | 2011 | 2011 only in 2010–2018 span | Yes |
| Truly undated (no year token) | 2 “Undated / Special” | **0** (both specials contain `2017`) | **No** (label) |
| Exam question papers (by README type tags) | 5 | 5 labeled | Yes |
| Marking memoranda (by README type tags) | 9 | 9 labeled | Yes |
| Assignments (README type tags, unclaimed tally) | — | 6 | N/A |
| General (README type tags, unclaimed tally) | — | 10 | N/A |

### Live year-token counts (content only)

| Year | Live n | README year-section n | Notes |
|------|--------|------------------------|-------|
| 2010 | 2 | 2 | Match |
| 2011 | 0 | missing | Match |
| 2012 | 2 | 2 | Match |
| 2013 | 10 | 10 | Match |
| 2014 | 9 | 9 | Match |
| 2015 | 1 | 1 | Match |
| 2016 | 2 | 2 | Match |
| 2017 | **3** | **1** (+ 2 under Undated) | Structural mismatch |
| 2018 | 1 | 1 | Match |

### Extensions (content)

- `.doc` 27 · `.docx` 2 · `.pdf` 1

### Content samples (subject authenticity)

| File | Extract method | Subject confirmation |
|------|----------------|----------------------|
| `BBST2016(1)Q.doc` | `textutil -convert txt -stdout` | Header: **“BROAD BASED SKILLS TEST OF THE SCHOOL FOR LEGAL PRACTICE”**, 2016(1), 100 marks → **BBST-related** |
| `BBST9Jun2012A.doc` | `textutil -convert txt -stdout` | “SCHOOL FOR LEGAL PRACTICE / MODULE 2.2 / SKILLS TEST / 9 JUNE 2012 / GUIDELINE TO MARKERS” → **memo for skills test / BBST lineage** |
| `BBST20Apr2010Q.doc` | `textutil -convert txt -stdout` | “SCHOOL FOR LEGAL PRACTICE / MODULE 2.2 / SKILLS TEST / 20 APRIL 2010” → **BBST-related** |
| `BBST2013(1)Q.doc` | `textutil -convert txt -stdout` | Explicit **Broad Based Skills Test** exam paper → supports subject; undercuts “assignment” type tag |
| `BBST2018(2) Statement of Facts.pdf` | `textutil` | Did not yield plain text (compressed PDF); filename + pack context still BBST SOF; treat as **OCR/extract gap**, not wrong module |

- Inventory / source units: 30 content + 2 SKIP locks + README  
- Claim units checked: total, year span, missing year, per-year buckets, undated set, Q/memo counts, full name listing, 4+ content subjects  
- Critical / Important / Minor: **0 / 2 / 3**  
- Estimated coverage of catalogue claims: ~95% accurate counts; ~100% file presence; weaker “undated”/type semantics  

## Suggested Fixes (Ordered)

1. Relocate `BBST2017 Guideline writing BBST.docx` and `BBST2017Final Statement of Facts.doc` under 2017; set 2017 count to 3; clear or redefine Undated.  
2. Align `exam_question` / `assignment` tags with document headers (especially 2013–2014 Q packs).  
3. Replace default “(01 Jun)” with “date unknown / sitting only” where filename and body lack day.  
4. Optionally remove `~$…` lock files; extend Question/Memo section with assignment/general tallies and unpaired-year notes.  

**Approval gate:** Do not apply until user approves.

## Source Quality Limitations

- Mostly legacy `.doc`; body verification requires macOS `textutil` (done for samples).  
- `BBST2018(2) Statement of Facts.pdf` did not extract as clean text via `textutil` in this pass — scanned/encoded PDF possible.  
- Office lock files present; correctly excluded from “30”.  
- Module historical naming shifted (“Module 2.2 Skills Test” vs “Broad Based Skills Test”); both are BBST family content in this archive.  
- Incomplete year coverage is archive reality (missing 2011; thin 2010/2012/2015/2018), not a catalogue error when stated.  

## Re-verify Plan

After approval and fixes:
- [ ] Re-check year buckets + undated = 0 (or document specials separately)  
- [ ] Re-count type tags vs any revised taxonomy  
- [ ] Full re-list if files added/removed after reindex  

---

**Module subject (claimed):** Broad Based Skills Test (Integrated Practical Exam) — **confirmed** from multiple primary headers.  
**Verdict returned to parent:** PASS WITH ISSUES · Critical **0** · Important **2** · Minor **3** · Report path: `/Users/ajadvanwyk/Desktop/LLB hub/BBST/verification-report.md`
