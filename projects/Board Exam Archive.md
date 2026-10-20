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
- [x] Save this work as linked Obsidian notes and update the dashboards and daily log.
- [ ] Complete manual proofreading of bilingual text and financial tables against original PDF pages.

## Recent Activity

- 2026-10-19: [[Logs/2026-10-19 - Board Exam Archive]] records recovery, OCR improvements and the Obsidian update.

## Sources

- Local verification: `.ocr-audit.json`, `.ocr-audit.md`, `.ocr_harness.py` and `.ocr-backups/20261019T204155/manifest.json` at the vault root.
- [[notes/Board Exam OCR Audit]] preserves the official source URLs for the corrected papers.

## Matching model answers - 2026-10-19

- As of 2026-10-19, 50 matching official model-answer memos for the 66 newly added question papers are saved with searchable text and original PDFs.
- [[notes/Board Exam Memo Coverage]] links every question/memo pair and lists the 16 unlocated official memos for 2022-2023.
- Full proofreading remains open; flagged extracted memo text is identified in the coverage note.

## Memo follow-up - 2026-10-19

- Corrected 24 flagged characters in ten official memo extracts against 14 original PDF pages.
- [[notes/Board Exam Memo Search - 2026-10-19]] records the follow-up source checks and partial or unofficial leads.
- As of 2026-10-19, 50 official memos are saved and 16 official 2022-2023 memos remain unlocated; full proofreading is still open.

## Mistral OCR exports - 2026-10-19

- [[notes/Board Exam Mistral OCR - 2026-10-19]] links 50 searchable alternative memo extracts covering 332 pages and the downloaded ZIP exports.
- Originals and existing corrected extracts are preserved; Mistral financial tables and full transcription still need source review. Official coverage remains 50 memos with 16 recent gaps.

## Mistral local search complete - 2026-10-19

- Local retrieval now includes the 50 Mistral memo extracts and their review report. Three scoped public exam queries returned the intended memos at ranks 1, 3 and 1 among these 50 extracts.
- See [[notes/Board Exam Mistral OCR - 2026-10-19]] for source completeness checks and remaining transcription-review limits. Official memo coverage remains 50 saved, with 16 recent official memos unlocated.

## Candidate model answers for 2022-2023 (pending verification) - 2026-10-19

- Generated 16 complete 100-mark candidate model memoranda (`official: false`, `verification-status: pending-multi-agent-review`) in [[Attorneys Exam/Candidate Model Answers 2022-2023/README]] for the 16 2022–2023 papers lacking public official LSSA LEAD PDFs, grounded in the 2015–2021 official memoranda, public YouTube walkthrough transcripts, and verified snippets.
