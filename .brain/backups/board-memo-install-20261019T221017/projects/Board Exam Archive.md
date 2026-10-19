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
