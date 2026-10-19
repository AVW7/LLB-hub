---
date: '2026-10-19'
type: research
tags:
- research
- board-exams
- ocr
ai-first: true
confidence: high
related-projects:
- '[[projects/Board Exam Archive]]'
source: .ocr-audit.json
---

## For future agent

This audit records the attorneys exam OCR corrections verified on 2026-10-19 and links the corrected text to each original public PDF. It preserves the workflow and recovery evidence for future maintenance; full transcription accuracy remains unverified.

# Board Exam OCR Audit

## Verified result on 2026-10-19

- Scope: the 66 recovered official question-paper PDFs in `Attorneys Exam/Official Previous Papers 2015-2023` and their Markdown sidecars.
- 14 sidecars corrected; 43 Unicode replacement characters resolved; ten damaged bilingual headings restored.
- Source checks included Afrikaans diacritics, a missing five-mark allocation and the damaged R3 000 000.00 accrual passage.
- The post-update audit reported 66 `sidecar_ready` entries. Original PDF hashes matched after installation, and each corrected sidecar matched its staged hash and appeared in the archive index.
- The earlier 21 review flags included genuine corruption and legitimate answer blanks or decorative bullet symbols. A zero-flag result after the changes is a basic integrity check, not a full proofreading result.

## Extraction and review

- Original sidecars were extracted from the official public PDFs, primarily with Jina AI Reader; one paper used a Firecrawl fallback.
- Ten fresh OCR candidates were generated with OCRmyPDF force mode, Tesseract English/Afrikaans best models and deskewing. The candidates and rendered original pages supported targeted corrections rather than wholesale replacement of the existing extraction.
- The harness now defaults to `--mode auto`, choosing a fresh raster-based pass when it detects corrupt embedded text. A real automatic-mode check recovered text on every page of the five-page test paper.
- Remaining text retains the original extraction. Check exact wording, amounts and table structure against the original PDF when precision matters; these are historical examination materials.

## Workflow

Run from the LLB hub root:

```bash
python3 .ocr_harness.py audit
python3 .ocr_harness.py compare --files "Attorneys Exam/Official Previous Papers 2015-2023"
```

Inspect the printed candidate Markdown and searchable PDF before using `promote` with the exact comparison-report path and `--reviewed`. Promotion validates source and candidate hashes, saves the prior Markdown, replaces the sidecar and refreshes the archive index. The Python environment requires `pypdf`; local OCR requires OCRmyPDF, Tesseract and the selected language models.

## Corrected papers and official sources

Each entry links the corrected Markdown, the preserved source PDF and the original official download URL verified during recovery on 2026-10-19.

- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam10Feb2016P4Q|AttExam10Feb2016P4Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam10Feb2016P4Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/LegalPractitionersBookkeeping/2016_10-FEBRUARY_PART-4.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam11Feb2015P3Q|AttExam11Feb2015P3Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam11Feb2015P3Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/AttorneysPractice/2015_11-FEBRUARY_PART-3.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam11Feb2015P4Q|AttExam11Feb2015P4Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam11Feb2015P4Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/LegalPractitionersBookkeeping/2015_11-FEBRUARY_PART-4.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam15Feb2017P4Q|AttExam15Feb2017P4Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam15Feb2017P4Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/LegalPractitionersBookkeeping/2017_15-FEBRUARY_PART-4.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam16Oct2018P4Q|AttExam16Oct2018P4Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam16Oct2018P4Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/LegalPractitionersBookkeeping/2018_16-OCTOBER_PART-4.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam17Aug2016P4Q|AttExam17Aug2016P4Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam17Aug2016P4Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/LegalPractitionersBookkeeping/2016_17-AUGUST_PART-4.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam18Aug2015P1Q|AttExam18Aug2015P1Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam18Aug2015P1Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/CourtProcedures/2015_18-AUGUST_PART-1.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam18Aug2015P2Q|AttExam18Aug2015P2Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam18Aug2015P2Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/AdmissionEstate/2015_18-AUGUST_PART-2.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam19Aug2015P3Q|AttExam19Aug2015P3Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam19Aug2015P3Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/AttorneysPractice/2015_19-AUGUST_PART-3.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam19Aug2015P4Q|AttExam19Aug2015P4Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam19Aug2015P4Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/LegalPractitionersBookkeeping/2015_19-AUGUST_PART-4.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam23Aug2017P4Q|AttExam23Aug2017P4Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam23Aug2017P4Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/LegalPractitionersBookkeeping/2017_23-AUGUST_PART-4.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam6Feb2018P2Q|AttExam6Feb2018P2Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam6Feb2018P2Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/AdmissionEstate/2018_6-FEBRUARY_PART-2.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam7Feb2018P4Q|AttExam7Feb2018P4Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam7Feb2018P4Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/LegalPractitionersBookkeeping/2018_7-FEBRUARY_PART-4.pdf
- [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam9Feb2016P2Q|AttExam9Feb2016P2Q]] - [[Attorneys Exam/Official Previous Papers 2015-2023/AttExam9Feb2016P2Q.pdf|source PDF]] - https://www.lssalead.org.za/wp-content/uploads/courses/ProfessionalExamination/AdmissionEstate/2016_9-FEBRUARY_PART-2.pdf

## Evidence and recovery

- Local audit: `.ocr-audit.json`; original review summary: `.ocr-audit.md`.
- Recoverable baselines, exact before/after diff, manifest and reindex log: `.ocr-backups/20261019T204155/`.
- Source tooling references: https://github.com/ocrmypdf/OCRmyPDF and https://github.com/tesseract-ocr/tessdata_best . These URLs identify the tools and models used; no claim is made about their latest releases.
- Project: [[projects/Board Exam Archive]]. Work log: [[Logs/2026-10-19 - Board Exam Archive]]. Navigation: [[brain]].
