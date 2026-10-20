---
date: '2026-10-19'
type: project
tags:
- project
- board-exams
- ocr
ai-first: true
confidence: high
status: active
source-root: Attorneys Exam/Official Previous Papers 2015-2023
---

## For future agent

This project maintains the recovered attorneys admission exam papers in the LLB hub Obsidian vault. This note records the archive and OCR work verified on 2026-10-19; the collection has not been certified complete against every historical exam sitting.

# Board Exam Archive

## State as of 2026-10-19

- 66 official question-paper PDFs in `Attorneys Exam/Official Previous Papers 2015-2023`, each with an extracted Markdown sidecar.
- 14 sidecars received targeted corrections checked against original PDF pages, resolving 43 replacement characters and restoring ten damaged bilingual headings.
- All 66 sidecars passed the basic text-integrity audit after the corrections. These checks do not establish perfect transcription accuracy.
- See [[notes/Board Exam OCR Audit]] for the corrected papers, official source URLs, workflow, verification and recovery evidence.
- Use [[index]] for the archive catalogue and [[Attorneys Exam/Attorneys Exam Dashboard]] for study navigation.

## Key decisions recorded 2026-10-19

- Preserve original PDFs and apply reviewed corrections to their derived Markdown text.
- Use the OCR harness automatic mode to rasterize corrupt embedded text before extraction; a redo pass can retain corrupt visible text.
- Treat answer blanks and standalone bullet symbols as legitimate layout rather than OCR errors.
- Keep note retrieval and embeddings on this Mac.

## Progress as of 2026-10-19

- [x] Save and index the 66 recovered official PDFs and their extracted Markdown.
- [x] Correct the 14 affected sidecars and retain recoverable baselines.
- [x] Save 50 matching official 2015–2021 marking memoranda (`Official Memoranda 2015-2021`) and 50 structured Mistral OCR extracts (`Mistral OCR 2026-10-19`), and sync structured tables into the canonical memo sidecars.
- [x] Review and align the flagged Estates (Paper 2) and Bookkeeping (Paper 4) financial tables (`AttExam21Aug2019P2A`, `AttExam6Mar2019P2A`, `AttExam15Oct2018P2A`, `AttExam23Aug2017P4A`, `AttExam9Feb2016P2A`, `AttExam16Aug2016P2A`, `AttExam17Aug2016P4A`, `AttExam19Feb2020P2A`) against the source PDFs.
- [x] Expand `Attorneys Exam` study layer with 6 new Paper 2 / Paper 4 topic notes and 7 new `notes/qa/` self-test packs (including [[AttExam 2022-2023 Orphan Papers]]).
- [x] Fix `.reindex.py` question/memo classification and deduplicate `.reindex.py` catalogue output.
- [ ] Complete manual line-by-line proofreading of remaining unflagged bilingual passages against original PDF pages.

## Summary of 2026-10-19 Archive & OCR Updates

- **Question Papers**: 66 official PDFs (2015–2023) with audited sidecars ([[notes/Board Exam OCR Audit]]).
- **Model-Answer Memoranda**: 50 official 2015–2021 memos paired in [[notes/Board Exam Memo Coverage]] and upgraded with structured tables from [[notes/Board Exam Mistral OCR - 2026-10-19]]; 16 official 2022–2023 memos remain unlocated after publisher catalogue searches ([[notes/Board Exam Memo Search - 2026-10-19]]).
- **Local RAG Search**: Local retrieval index verified across vault sources via `127.0.0.1:11434` (`embeddinggemma-2:270m`).
- **Work Log**: [[Logs/2026-10-19 - Board Exam Archive]] and [[Logs/2026-10-19]].

## Candidate model answers for 2022-2023 (pending verification) - 2026-10-19

- Generated 16 complete 100-mark candidate model memoranda (`official: false`, `verification-status: pending-multi-agent-review`) in [[Attorneys Exam/Candidate Model Answers 2022-2023/README]] for the 16 2022–2023 papers lacking public official LSSA LEAD PDFs, grounded in the 2015–2021 official memoranda, public YouTube walkthrough transcripts, and verified snippets.
