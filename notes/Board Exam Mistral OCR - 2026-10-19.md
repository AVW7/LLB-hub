---
date: '2026-10-19'
type: research
tags:
- research
- board-exams
- ocr
ai-first: true
confidence: high for archive completeness; unreviewed for transcription accuracy
documents: 50
pages: 332
---

## For future agent

Mistral OCR export and import record for 50 public official board-exam memos (332 pages), saved on 2026-10-19. It links searchable alternative extracts while preserving the original PDFs and earlier reviewed text; financial-table proofreading remains incomplete.

# Board Exam Mistral OCR - 2026-10-19

## Verified scope

- As of 2026-10-19: 50 distinct official memos, 332 exported pages, 5 downloaded ZIP archives; every source page has nonempty machine text included in its combined extract.
- All ZIP CRC integrity checks pass. Unicode replacement characters found in these exports: 0.
- These are alternative extractions of existing memos, not newly recovered model answers. Collection coverage remains 50 official memos for 66 recovered papers; the 16 official 2022-2023 gaps in [[notes/Board Exam Memo Coverage]] remain open.
- Project: [[projects/Board Exam Archive]]. Search leads: [[notes/Board Exam Memo Search - 2026-10-19]]. Work record: [[Logs/2026-10-19 - Board Exam Archive]].
- Service used on 2026-10-19: https://console.mistral.ai/document-ai/ocr-playground ; model selected in the interface: mistral-ocr-latest.
- Public source URLs are retained in each extract. Source PDF hashes and per-document page counts are in the accompanying manifest.

## Review limits and decisions

- Original PDFs and existing sidecars are preserved, and the structured Mistral Markdown bodies have been synced into the canonical `Attorneys Exam/Official Memoranda 2015-2021/` sidecars.
- All pages passing completeness checks does not establish full line-by-line transcription accuracy.
- The flagged multi-column financial tables in `AttExam21Aug2019P2A` (page 1 asset values), `AttExam6Mar2019P2A` (page 1 asset values), `AttExam23Aug2017P4A` (page 1 bank reconciliation), `AttExam15Oct2018P2A` (pages 1–3 movable property & estate duty addendum rows), `AttExam9Feb2016P2A` (page 1 Erf 56 valuation of R2 000 000.00), `AttExam16Aug2016P2A` (page 1 movable row shift), `AttExam17Aug2016P4A` (page 1 supplementary trust cash book), and `AttExam19Feb2020P2A` (page 9 fiduciary asset distribution) have been reviewed against the original PDFs and aligned in both `Mistral OCR 2026-10-19/` and `Official Memoranda 2015-2021/`.
- The first-batch 2015 Paper 4 image reference was broken in Mistral's ZIP. Local image links are resolved to the matching nested page asset, without changing legal or numerical text.
- Whole-document visual proofreading is still pending. Existing OCR corrections are not treated as evidence that Mistral output is legally or arithmetically correct.

## Searchable alternative extracts

| Memo | Pages | Words | Table rows | Alternative extract |
|---|---:|---:|---:|---|
| AttExam10Feb2015P1A.pdf | 10 | 3087 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam10Feb2015P1A]] |
| AttExam10Feb2015P2A.pdf | 10 | 1744 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam10Feb2015P2A]] |
| AttExam10Feb2016P3A.pdf | 5 | 1764 | 7 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam10Feb2016P3A]] |
| AttExam10Feb2016P4A.pdf | 5 | 1091 | 62 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam10Feb2016P4A]] |
| AttExam11Feb2015P3A.pdf | 5 | 1596 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam11Feb2015P3A]] |
| AttExam11Feb2015P4A.pdf | 4 | 1188 | 58 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam11Feb2015P4A]] |
| AttExam14Feb2017P2A.pdf | 7 | 1342 | 2 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam14Feb2017P2A]] |
| AttExam15Feb2017P4A.pdf | 5 | 1089 | 71 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam15Feb2017P4A]] |
| AttExam15Oct2018P1A.pdf | 7 | 2152 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam15Oct2018P1A]] |
| AttExam15Oct2018P2A.pdf | 6 | 1988 | 67 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam15Oct2018P2A]] |
| AttExam16Aug2016P2A.pdf | 8 | 1708 | 88 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam16Aug2016P2A]] |
| AttExam16Oct2018P4A.pdf | 6 | 1064 | 67 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam16Oct2018P4A]] |
| AttExam17Aug2016P4A.pdf | 7 | 1180 | 110 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam17Aug2016P4A]] |
| AttExam17Mar2021P1A.pdf | 7 | 2528 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam17Mar2021P1A]] |
| AttExam17Mar2021P2A.pdf | 7 | 1983 | 92 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam17Mar2021P2A]] |
| AttExam18Aug2015P1A.pdf | 7 | 2219 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam18Aug2015P1A]] |
| AttExam18Aug2015P2A.pdf | 9 | 1770 | 86 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam18Aug2015P2A]] |
| AttExam18Mar2021P3A.pdf | 6 | 1846 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam18Mar2021P3A]] |
| AttExam18Mar2021P4A.pdf | 12 | 1704 | 128 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam18Mar2021P4A]] |
| AttExam19Aug2015P3A.pdf | 4 | 1630 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam19Aug2015P3A]] |
| AttExam19Aug2015P4A.pdf | 6 | 1423 | 126 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam19Aug2015P4A]] |
| AttExam19Feb2020P1A.pdf | 9 | 3113 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam19Feb2020P1A]] |
| AttExam19Feb2020P2A.pdf | 11 | 2155 | 102 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam19Feb2020P2A]] |
| AttExam19Oct2021P1A.pdf | 8 | 2520 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam19Oct2021P1A]] |
| AttExam19Oct2021P2A.pdf | 6 | 1958 | 92 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam19Oct2021P2A]] |
| AttExam20Feb2020P3A.pdf | 5 | 1447 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam20Feb2020P3A]] |
| AttExam20Feb2020P4A.pdf | 6 | 1188 | 48 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam20Feb2020P4A]] |
| AttExam20Oct2021P3A.pdf | 5 | 1967 | 5 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam20Oct2021P3A]] |
| AttExam20Oct2021P4A.pdf | 6 | 1541 | 141 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam20Oct2021P4A]] |
| AttExam21Aug2019P1A.pdf | 7 | 2345 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam21Aug2019P1A]] |
| AttExam21Aug2019P2A.pdf | 7 | 1945 | 75 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam21Aug2019P2A]] |
| AttExam22Aug2017P1A.pdf | 8 | 2329 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam22Aug2017P1A]] |
| AttExam22Aug2017P2A.pdf | 8 | 2221 | 92 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam22Aug2017P2A]] |
| AttExam22Aug2019P3A.pdf | 6 | 2097 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam22Aug2019P3A]] |
| AttExam22Aug2019P4A.pdf | 7 | 1054 | 74 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam22Aug2019P4A]] |
| AttExam23Aug2017P3A.pdf | 4 | 1496 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam23Aug2017P3A]] |
| AttExam23Aug2017P4A.pdf | 7 | 1377 | 90 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam23Aug2017P4A]] |
| AttExam4Nov2020P1A.pdf | 6 | 1934 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam4Nov2020P1A]] |
| AttExam4Nov2020P2A.pdf | 6 | 1775 | 49 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam4Nov2020P2A]] |
| AttExam5Nov2020P3A.pdf | 6 | 1837 | 6 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam5Nov2020P3A]] |
| AttExam5Nov2020P4A.pdf | 6 | 1907 | 149 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam5Nov2020P4A]] |
| AttExam6Feb2018P1A.pdf | 6 | 2363 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam6Feb2018P1A]] |
| AttExam6Feb2018P2A.pdf | 6 | 1665 | 74 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam6Feb2018P2A]] |
| AttExam6Mar2019P1A.pdf | 7 | 2403 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam6Mar2019P1A]] |
| AttExam6Mar2019P2A.pdf | 7 | 1562 | 4 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam6Mar2019P2A]] |
| AttExam7Feb2018P3A.pdf | 6 | 1844 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam7Feb2018P3A]] |
| AttExam7Feb2018P4A.pdf | 6 | 1601 | 160 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam7Feb2018P4A]] |
| AttExam7Mar2019P3A.pdf | 5 | 1626 | 0 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam7Mar2019P3A]] |
| AttExam7Mar2019P4A.pdf | 6 | 1242 | 84 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam7Mar2019P4A]] |
| AttExam9Feb2016P2A.pdf | 6 | 1564 | 83 | [[Attorneys Exam/Mistral OCR 2026-10-19/AttExam9Feb2016P2A]] |

## Download archives

- [[Attorneys Exam/Mistral OCR 2026-10-19/exports/mistral-ocr-ten-memos.zip]]
- [[Attorneys Exam/Mistral OCR 2026-10-19/exports/mistral-ocr-batch-2.zip]]
- [[Attorneys Exam/Mistral OCR 2026-10-19/exports/mistral-ocr-batch-3.zip]]
- [[Attorneys Exam/Mistral OCR 2026-10-19/exports/mistral-ocr-batch-4.zip]]
- [[Attorneys Exam/Mistral OCR 2026-10-19/exports/mistral-ocr-batch-5.zip]]

## Local search verification - 2026-10-19

- As of 2026-10-19T20:51:47.787079+00:00, all 50 alternative memo extracts plus this report matched their current modification times in the local retrieval index (51/51); the index contained 828 sources.
- Three public exam queries were embedded locally through http://127.0.0.1:11434 using embeddinggemma-2:270m. No private note bodies or embeddings were transmitted to an external service.
- Among the 50 new Mistral memo extracts, the intended memos ranked 1, 3 and 1. This is a scoped retrieval check, not a claim about answer accuracy or retrieval across every vault source.
- Obsidian's earlier startup dialog prevented indexing until the app became responsive. The retry confirmed the vault window was open and indexing had completed; no permissions or application data were changed by this finalization.
- Metadata and query evidence are retained under `.brain/mistral-ocr-search-2026-10-19/`.
