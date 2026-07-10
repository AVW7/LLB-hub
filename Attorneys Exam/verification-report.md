# Verification Report — Attorneys Exam + LSSA & Miscellaneous

**Date:** 10 July 2026  
**Scope:** Live filesystem check of `Attorneys Exam/` and `LSSA & Miscellaneous /` against folder READMEs and hub index types.  
**Source exams modified?** No. Report only.

---

## Verdict

| Area | Verdict | Expected count | Live count | Notes |
|------|---------|----------------|------------|-------|
| **Attorneys Exam** | **PASS** | 10 PDFs | **10 PDFs** | 5 Q + 5 A pairs; classification consistent with filenames |
| **LSSA & Miscellaneous** | **PASS** (catalogue count) | 3 logical reference items | **3** folders with root `markdown.md` | Extracted legislation/constitution; not exam Q/A |

**Overall:** **PASS** — both folders match expected primary file counts (10 and 3). No wrong memo/question classifications found from filenames.

---

## 1. Attorneys Exam

### Paths
- Folder: `/Users/ajadvanwyk/Desktop/LLB hub/Attorneys Exam/`
- README: `/Users/ajadvanwyk/Desktop/LLB hub/Attorneys Exam/README.md`

### README claims (confirmed)
- Module: Attorneys Admission Examination (Board Exam)
- **Total files: 10**
- Years: 2016–2017
- Exam question papers: **5**
- Marking memoranda: **5**

### Live inventory (10 PDFs)

| File | Filename role | README / index type | Pair date |
|------|---------------|---------------------|-----------|
| `AttExam9Feb2016Q.pdf` | **Q** = exam_question | exam_question / role question | 09 Feb 2016 |
| `AttExam9Feb2016A.pdf` | **A** = marking_memo | marking_memo / role answer | 09 Feb 2016 |
| `AttExam16Aug2016Q.pdf` | **Q** | exam_question | 16 Aug 2016 |
| `AttExam16Aug2016A.pdf` | **A** | marking_memo | 16 Aug 2016 |
| `AttExam17Aug2016Q.pdf` | **Q** | exam_question | 17 Aug 2016 |
| `AttExam17Aug2016A.pdf` | **A** | marking_memo | 17 Aug 2016 |
| `AttExam14Feb2017Q.pdf` | **Q** | exam_question | 14 Feb 2017 |
| `AttExam14Feb2017A.pdf` | **A** | marking_memo | 14 Feb 2017 |
| `AttExam15Feb2017Q.pdf` | **Q** | exam_question | 15 Feb 2017 |
| `AttExam15Feb2017A.pdf` | **A** | marking_memo | 15 Feb 2017 |

**Classification check:**  
Filename convention is consistent: suffix **`Q`** → question paper; suffix **`A`** → marking memo/answers. Every sitting has both a Q and an A.  
**No swapped or mislabelled Q/A pairs detected from filenames.**  
Also non-source metadata files only: `README.md` (plus this report). Source exam PDFs were not modified.

### PDF quality / OCR (source limitation)

All 10 board exam PDFs are **scanned image PDFs** with a **quality gap** for text extraction:

| Heuristic | Result |
|-----------|--------|
| `pdftotext` extractable characters | **0** on all 10 files |
| Embedded `/Font` objects | **0** on all 10 |
| Embedded `/Image` / `/XObject` | Present on all 10 (scan-only pattern) |
| `index.json` gaps | Every Attorneys Exam entry: `"scanned/no extractable text (OCR needed)"` |
| `quality_score` in index | 1.0 listed, but gap flag is authoritative for text usability |

**Conclusion:** Treat all Attorneys Exam PDFs as **OCR / image-scan sources**. Do not invent question or memo content from missing text layers. Re-OCR or human read of scans is required for full-text study/index improvement.

### Attorneys Exam count confirmation
- **Expected: 10**  
- **Live PDFs: 10**  
- **Q: 5 · A: 5 · Complete pairs: 5**  
→ **MATCH**

---

## 2. LSSA & Miscellaneous

### Paths
- Folder name has a **trailing space**: `LSSA & Miscellaneous `  
- Full path: `/Users/ajadvanwyk/Desktop/LLB hub/LSSA & Miscellaneous /`  
- README: `/Users/ajadvanwyk/Desktop/LLB hub/LSSA & Miscellaneous /README.md`

### README claims (confirmed)
- Module: LSSA Reference Materials and Miscellaneous
- **Total files: 3** (logical catalogue items, not recursive page dumps)
- Type: **reference** (not exam questions/memos)
- Exam question papers: **0**
- Marking memoranda: **0**

### Live logical items (3)

These are **folder names styled as `*.pdf`**, each holding extracted markdown (not raw PDF binaries at top level):

| Logical item | Root extraction | Type | Index path |
|--------------|-----------------|------|------------|
| `Constitution of RSA.pdf/` | `markdown.md` (~310 KB; Constitution text present) | reference | `./LSSA & Miscellaneous /Constitution of RSA.pdf/markdown.md` |
| `Legal Practice Act 28 of 2014.pdf/` | `markdown.md` (~443 KB) | reference | `./LSSA & Miscellaneous /Legal Practice Act 28 of 2014.pdf/markdown.md` |
| `Legal Practice Act Rules.pdf/` | `markdown.md` (~323 KB) | reference | `./LSSA & Miscellaneous /Legal Practice Act Rules.pdf/markdown.md` |

Each folder also contains per-page extraction under `pages/` (hundreds of page-level `markdown.md` + occasional JPEGs) plus a mini `README.md`. That page machinery supports extraction depth; **catalogue count of 3** refers to the three root documents, consistent with the folder README.

### Classification check
- All three correctly tagged **reference** (legislation / constitution), not exam Q or A.  
- **No memo/question misclassification** over LSSA (none of the items claim to be board exams).

### Quality / OCR note for LSSA
- **Not the same issue as Attorneys Exam scans.** LSSA root `markdown.md` files contain substantial extracted legislation text (Constitution sample begins correctly with “The Constitution OF THE REPUBLIC OF SOUTH AFRICA, 1996”).
- Caveat: `index.json` currently marks these three as gaps **`empty or near-empty`** with `quality_score: 0.5`. That **appears to be an indexer false positive** relative to live file sizes and content (root markdowns are large and non-empty). Flag as index quality-metadata mismatch, not empty sources.
- Page-level assets include scanned layout images in places (e.g. Rules); use root `markdown.md` as the primary text source; treat residual OCR/layout weirdness as source limitation if quote-level precision is critical.

### LSSA count confirmation
- **Expected catalogue: 3**  
- **Live top-level reference units: 3**  
→ **MATCH**

---

## 3. Cross-check summary

| Check | Result |
|-------|--------|
| Attorneys Exam PDF count = 10 | **Yes** |
| LSSA logical reference count = 3 | **Yes** |
| Q/A pairing complete (5 sittings) | **Yes** |
| Filenames vs type (Q→question, A→memo) wrong? | **No** |
| All Attorneys Exam PDFs image-scanned / need OCR | **Yes** (source limitation) |
| LSSA items are extracted reference markdown under `*.pdf` folder names | **Yes** |
| Source exam PDFs modified this run | **No** |

---

## 4. Report path

**This report:**  
`/Users/ajadvanwyk/Desktop/LLB hub/Attorneys Exam/verification-report.md`

### Final verdict line
**PASS — Attorneys Exam 10/10 PDFs (5Q+5A classifications OK; all OCR/scan gaps); LSSA 3/3 reference extracts (folder trailing space noted; no Q/A misclass).**
