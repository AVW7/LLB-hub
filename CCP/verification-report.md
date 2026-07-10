# Verification Report — CCP + CLP

**Hub:** `/Users/ajadvanwyk/Desktop/LLB hub`  
**Verified:** 2026-07-10  
**Method:** On-disk listing vs module READMEs; filename Q/A stem pairing; `textutil` subject-label sampling.  
**Note:** READMEs were **not** edited.

---

## CCP — Criminal Court Practice

### File-count claim

| Claim (README) | On-disk | Status |
|----------------|---------|--------|
| **Total files: 21** | 21 content files (+ `README.md`) | **MATCH** |

Content files (basename):

1. `CCP2012(2)SuppA.doc`
2. `CCP2019AssQ.doc`
3. `CCP25Jul2015A.doc` / `CCP25Jul2015Q.doc`
4. `CCP26Jan2013A.doc` / `CCP26Jan2013Q.doc`
5. `CCP26Jul2014A.doc` / `CCP26Jul2014Q.doc`
6. `CCP26Jun2012A.doc` / `CCP26Jun2012Q.doc`
7. `CCP28Jan2012A.doc` / `CCP28Jan2012Q.doc`
8. `CCP30Jan2010A.doc` / `CCP30Jan2010Q.doc`
9. `CCPDec2010A.doc` / `CCPDec2010Q.doc`
10. `CCPExampleAppLeaveToAppeal.doc`
11. `CCPHighCourtAppLeavetoAppeal.pdf`
12. `CCPModule1A.doc` / `CCPModule1Q.doc`
13. `CCPWebinar2019Slides.pdf`

### Year claims

| Claim (README) | On-disk | Status |
|----------------|---------|--------|
| Years covered: **2010 – 2015** | Exam/dated set spans 2010, 2012–2015 | **MATCH** (operational span) |
| Missing years: **2011** | No 2011-named files | **MATCH** |
| Year breakdown counts | 2015:2, 2014:2, 2013:2, 2012:5, 2010:4 | **MATCH** |
| Undated / special: 6 files | `AssQ`, Example/HighCourt templates, Module1 Q/A, Webinar | **MATCH** |

**Caveat (non-blocking):** Filenames also contain **2019** (`CCP2019AssQ.doc`, `CCPWebinar2019Slides.pdf`). README correctly buckets these under undated/special rather than extending the exam year span to 2019.

### README Q/memo tallies

| Claim | Counted on disk | Status |
|-------|-----------------|--------|
| Exam question papers: **8** | 7 dated `*Q` + `CCPModule1Q.doc` (excludes `CCP2019AssQ` as assignment) | **MATCH** |
| Marking memoranda: **9** | 7 dated pair `*A` + `CCP2012(2)SuppA.doc` + `CCPModule1A.doc` | **MATCH** |

### Q/A pair orphans (filename stems)

Pairing rule: same stem with trailing `Q` vs `A` (`AssQ`/`AssA` → shared `Ass` stem). Non-QA materials excluded.

| Status | Stem / file | Notes |
|--------|-------------|-------|
| **Paired (8)** | `CCP25Jul2015`, `CCP26Jan2013`, `CCP26Jul2014`, `CCP26Jun2012`, `CCP28Jan2012`, `CCP30Jan2010`, `CCPDec2010`, `CCPModule1` | Q ↔ A present |
| **Orphan Q (1)** | `CCP2019AssQ.doc` | Assignment Q; no `CCP2019AssA` |
| **Orphan A (1)** | `CCP2012(2)SuppA.doc` | Supp memo; no matching `…SuppQ` |
| **Non-QA** | `CCPExampleAppLeaveToAppeal.doc`, `CCPHighCourtAppLeavetoAppeal.pdf`, `CCPWebinar2019Slides.pdf` | templates / slides |

### Source-quality flags

| File | Flag |
|------|------|
| `CCPHighCourtAppLeavetoAppeal.pdf` | **Known scanned PDF** — source quality limited; may need OCR |
| `CCPWebinar2019Slides.pdf` | **Known scanned PDF** — source quality limited; may need OCR |

### Subject-label sample (`textutil`)

| Sample | File | Extracted header | Folder match |
|--------|------|------------------|--------------|
| CCP Q | `CCP25Jul2015Q.doc` | `SCHOOL FOR LEGAL PRACTICE` / **MODULE 1** / **CRIMINAL COURT PRACTICE** / `25 JULY 2015` | **YES** — matches CCP folder |

---

## CLP — Constitutional Practice

### File-count claim

| Claim (README) | On-disk | Status |
|----------------|---------|--------|
| **Total files: 17** | 17 content files (+ `README.md`) | **MATCH** |

Content files (basename):

1. `CLP 2012.2 SUPP ENG - only for appeal students.doc`
2. `CLP21Jul2012A.doc` / `CLP21Jul2012Q.doc`
3. `CLP24Jul2010A.doc` / `CLP24Jul2010Q.doc`
4. `CLP26Jun2012A.doc` / `CLP26Jun2012Q.doc`
5. `CLP2Aug2012A.doc`
6. `CLP30Jan2010A.doc` / `CLP30Jan2010Q.doc`
7. `CLP30Jan2019AssA.docx` / `CLP30Jan2019AssQ.docx`
8. `CLPDec2010Q.doc`
9. `CLPJul2012A.doc` / `CLPJul2012Q.doc`
10. `CLPLecture2019Q&A.pdf`
11. `CLPWebinar2019Slides.ppt`

### Year claims

| Claim (README) | On-disk | Status |
|----------------|---------|--------|
| Years covered: **2010 – 2019** | Materials named for 2010, 2012, 2019 | **MATCH** (span + assignment year) |
| Missing: **2011, 2013–2018** | No files for those years | **MATCH** |
| 2019 breakdown: **2** | Ass Q + Ass A only in year section | **MATCH** (Lecture/Webinar held as special despite “2019” in name) |
| 2012 breakdown: **7** | Jun, Jul, 21 Jul pairs + `CLP2Aug2012A` | **MATCH** |
| 2010 breakdown: **5** | Jan pair, Jul pair, Dec Q only | **MATCH** |
| Undated / special: **3** | 2012.2 SUPP, Lecture2019 Q&A, Webinar slides | **MATCH** |

**Caveat (non-blocking):** `CLP 2012.2 SUPP ENG…` and the 2019 lecture/webinar files contain year tokens but are intentionally listed as special, not folded into the year tallies above.

### README Q/memo tallies

| Claim | Counted on disk | Status |
|-------|-----------------|--------|
| Exam question papers: **5** | `CLP21Jul2012Q`, `CLP26Jun2012Q`, `CLP30Jan2010Q`, `CLP24Jul2010Q`, `CLPDec2010Q` (README treats `CLPJul2012Q` + AssQ as assignment, not exam) | **MATCH** |
| Marking memoranda: **7** | `CLP21Jul2012A`, `CLP26Jun2012A`, `CLPJul2012A`, `CLP2Aug2012A`, `CLP30Jan2010A`, `CLP24Jul2010A`, `CLP30Jan2019AssA` | **MATCH** |

### Q/A pair orphans (filename stems)

| Status | Stem / file | Notes |
|--------|-------------|-------|
| **Paired (6)** | `CLP21Jul2012`, `CLP24Jul2010`, `CLP26Jun2012`, `CLP30Jan2010`, `CLPJul2012`, `CLP30Jan2019Ass` | Q ↔ A present |
| **Orphan Q (1)** | `CLPDec2010Q.doc` | No `CLPDec2010A` |
| **Orphan A (1)** | `CLP2Aug2012A.doc` | No matching `CLP2Aug2012Q` |
| **Non-QA** | `CLP 2012.2 SUPP ENG - only for appeal students.doc`, `CLPLecture2019Q&A.pdf`, `CLPWebinar2019Slides.ppt` | supp / combined Q&A lecture / slides |

### Source-quality flags

| File | Flag |
|------|------|
| `CLPLecture2019Q&A.pdf` | **Known scanned PDF** — source quality limited; may need OCR |
| `CLPWebinar2019Slides.ppt` | Binary slides (PPT); not a scanned PDF but not plain-text `.doc` either |

### Subject-label sample (`textutil`)

| Sample | File | Extracted header | Folder match |
|--------|------|------------------|--------------|
| CLP Q | `CLP21Jul2012Q.doc` | `SCHOOL FOR LEGAL PRACTICE` / **CONSTITUTIONAL PRACTICE** / **MODULE 1** / `21 JULY 2012` | **YES** — matches CLP folder |

---

## Cross-cutting summary

| Check | CCP | CLP |
|-------|-----|-----|
| Total file count vs README | ✅ 21 = 21 | ✅ 17 = 17 |
| Year span / missing years | ✅ | ✅ |
| Per-year breakdown sums | ✅ | ✅ |
| Exam Q / memo counts | ✅ 8 / 9 | ✅ 5 / 7 |
| Q/A orphans | AssQ only; SuppA only | Dec2010Q only; 2Aug2012A only |
| Subject label in sample Q | ✅ Criminal Court Practice | ✅ Constitutional Practice |
| Scanned / low-quality sources | HighCourt leave PDF; Webinar PDF | Lecture 2019 Q&A PDF |

### Overall verdict

**Both CCP and CLP README year and file-count claims are accurate against on-disk contents.**  
Filename-based Q/A pairing shows small, documented-style orphans (one lonely Q and one lonely A in each module), consistent with supplementary and assignment materials rather than index corruption. Sample question papers open correctly via `textutil` and carry subject titles that match their folder labels.
