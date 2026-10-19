---
type: master-dashboard
tags:
- llb-hub/dashboard
- master-dashboard
date: '2026-10-19'
ai-first: true
---

## For future agent

Study dashboard for the LLB hub archive. The dated board-exam update records the recovered papers and OCR improvements verified on 2026-10-19; other module coverage remains scoped to its own source notes.

# LLB Hub — Master Study Dashboard

Every module of the South African Attorneys' Admission Exam archive, rebuilt as a linked Obsidian study system: real past-paper questions with real memo answers behind self-test callouts, topic notes synthesised from those memos, and a `status` field on every note that drives the progress boards below. This note is the front door to the whole hub — each module also has its own dashboard for module-specific detail.

## What the whole hub is built out of

```
LLB hub/
├── LLB Hub Dashboard.md      ← this note
├── LLB Hub.base               ← master tracker, rolls up every module (embedded below)
├── AGENTS.md, index.md, index.json  ← original archive catalogue (unchanged)
├── CCP/    Criminal Court Practice        — CCP Dashboard.md · CCP.base
├── CLP/    Constitutional Practice        — CLP Dashboard.md · CLP.base
├── PCT/    Professional Conduct           — PCT Dashboard.md · PCT.base
├── BBST/   Broad Based Skills Test        — BBST Dashboard.md · BBST.base
├── COS/    Legal Costs                    — COS Dashboard.md · COS.base
├── HCP/    High Court Practice            — HCP Dashboard.md · HCP.base
├── MCP/    Magistrate's Court Practice    — MCP Dashboard.md · MCP.base
├── FBE/    Forms of Business Enterprise   — FBE Dashboard.md · FBE.base
├── LDR/    Labour Dispute Resolution      — LDR Dashboard.md · LDR.base
├── ICP/    Conveyancing Practice          — ICP Dashboard.md · ICP.base
├── PLE/    Professional Legal Ethics      — PLE Dashboard.md · PLE.base
├── IPM/    Practice Management            — IPM Dashboard.md · IPM.base
├── Attorneys Exam/   Board Exam           — Attorneys Exam Dashboard.md · Attorneys Exam.base
└── LSSA & Miscellaneous/   Reference legislation (not exam papers) — LSSA Dashboard.md · LSSA.base
```

Every module folder follows the same pattern (except LSSA, which is reference-only — see below):
- **`notes/topics/`** — one note per legal topic, the rule as stated in the real memos, plus links to every past paper that tests it.
- **`notes/qa/`** — one note per real exam sitting, every question with the real memo answer hidden behind a collapsible `> [!success]-` callout.
- **`<Module> Dashboard.md`** — the module's own front door and gap analysis.
- **`<Module>.base`** — the module's own live progress tracker.

## How to use it

1. Start at whichever module you're studying via the table below, or open that module's own Dashboard.
2. Work topic-by-topic: read the topic note, then work the linked past-paper questions, checking your answer against the real memo.
3. Update `status:` (`not-started` → `in-progress` → `reviewed` → `mastered`) in each note's frontmatter as you go — every board on this page and in every module dashboard reads from that one field.
4. Come back here for the cross-module view, or open a module's own dashboard for that module's detail (gaps, recurring fact patterns, orphan papers).

## Master progress board

![[LLB Hub.base]]

## Module overview

| Code | Module | Topic notes | Past-paper notes | Dashboard |
|---|---|---|---|---|
| CCP | Criminal Court Practice | 15 | 9 | [[CCP Dashboard]] |
| CLP | Constitutional Practice | 14 | 8 | [[CLP Dashboard]] |
| PCT | Professional Conduct | 15 | 9 | [[PCT Dashboard]] |
| BBST | Broad Based Skills Test | 20 | 14 | [[BBST Dashboard]] |
| COS | Legal Costs | 9 | 6 | [[COS Dashboard]] |
| HCP | High Court Practice | 18 | 12 | [[HCP Dashboard]] |
| MCP | Magistrate's Court Practice | 14 | 6 | [[MCP Dashboard]] |
| FBE | Forms of Business Enterprise | 9 | 7 | [[FBE Dashboard]] |
| LDR | Labour Dispute Resolution | 12 | 8 | [[LDR Dashboard]] |
| ICP | Conveyancing Practice | 14 | 9 | [[ICP Dashboard]] |
| PLE | Professional Legal Ethics | 16 | 9 | [[PLE Dashboard]] |
| IPM | Practice Management | 13 | 7 | [[IPM Dashboard]] |
| Attorneys Exam | Board Exam | 20 | 5 | [[Attorneys Exam Dashboard]] |
| LSSA | Reference legislation | 3 reference notes | — no exam papers | [[LSSA Dashboard]] |
| **Total** | | **189** | **109** | |

189 topic notes + 109 real past-paper notes (each with multiple questions) + 3 reference notes = the full hub, all cross-linked with wikilinks, all verified for valid frontmatter and resolvable links.

## Known gaps across the hub

- **Scanned/unreadable source files** (flagged in the relevant module dashboard rather than silently skipped): `CCP/CCPHighCourtAppLeavetoAppeal.pdf`, `CCP/CCPWebinar2019Slides.pdf`, `CLP/CLPLecture2019Q&A.pdf` — OCR was attempted and failed to produce reliable text.
- **Attorneys Exam** — all 10 source PDFs required OCR (pre-existing page-image extraction was reused); OCR succeeded cleanly for all 5 sittings, with one narrow gap flagged in-note where a memo answer's mark allocation didn't fully match its OCR'd text.
- **Orphan papers** (question with no memo, or memo with no question) exist in most modules — every one is flagged in its own note with a `> [!warning] No memo in the archive` callout and self-check pointers to topic notes, never a fabricated answer. See each module's Dashboard for the specific list.
- **LSSA & Miscellaneous** is deliberately reference-only: it holds the full text of the Constitution, the Legal Practice Act, and its Rules (already OCR'd), with three navigable index notes pointing into them — not past exam papers, so it has no `.base` topic/paper split.

## Next steps

The system is fully built across all 14 folders. From here it's pure study: work through topics module by module, update `status:` as you go, and use `LLB Hub.base`'s "Not Started Yet" view to see what's left at a glance.

## Board exam archive update - 2026-10-19

- [[projects/Board Exam Archive]] - recovered papers, current state and remaining proofreading.
- [[notes/Board Exam OCR Audit]] - verified corrections, original PDF links and recovery evidence.
- [[Logs/2026-10-19 - Board Exam Archive]] - dated work record.

As of 2026-10-19, the recovered collection contains 66 PDFs with Markdown sidecars; 14 sidecars were corrected and all 66 passed the basic text-integrity audit. Full proofreading remains open.

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
