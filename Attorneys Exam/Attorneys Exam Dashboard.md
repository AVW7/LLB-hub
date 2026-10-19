---
type: dashboard
subject: AttExam
tags:
- attexam/dashboard
- dashboard
date: '2026-10-19'
ai-first: true
---

## For future agent

Study dashboard for the attorneys admission examination materials. The dated update links the 66 recovered official question papers and OCR corrections verified on 2026-10-19; passing the OCR audit does not certify every transcription.

# Attorneys Exam — Attorneys Admission Examination (Board Exam) · Study Dashboard

The integrated Board exam covering multiple subject areas in a single sitting — Part 1 (Court Procedures) mixes RAF/delict, civil procedure drafting, and criminal procedure in one paper; Part 3 (Attorney's Practice) mixes contract drafting, professional ethics, prescription, and company/insolvency/family law in one paper. Expect broad, mixed scenarios rather than single-subject depth.

## What this is built out of

```
Attorneys Exam/
├── Attorneys Exam Dashboard.md   ← this note
├── Attorneys Exam.base           ← live tracker (embedded below)
├── README.md                     ← original archive contents overview
├── verification-report.md        ← archive audit (pre-existing)
├── notes/
│   ├── topics/                    20 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                        5 exam-paper notes — real questions + real memo answers
│       └── ...
└── (10 original source files — scanned PDFs, each with a pre-rendered pages/ subfolder
     and a markdown.md OCR transcript at the PDF's own root)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per legal/procedural topic, each with the rule, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[Attorneys Exam.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `Attorneys Exam.base` to see what's left.

## OCR quality notes

All 10 source PDFs were flagged in the hub's index as scanned with **no extractable text layer**. Each PDF folder already had a `pages/` subfolder of pre-rendered page images **and** a pre-existing `markdown.md` OCR transcript at the PDF folder's own root (from an earlier processing pass) — this transcript was used directly rather than re-running OCR from scratch.

**Result: all 10 files (5 question papers + 5 marking memos) OCR'd cleanly.** No sitting had illegible or unusable passages. The papers are bilingual (Afrikaans/English side by side in the original layout); the English text was used throughout for the notes, cross-checked against the Afrikaans where a term was ambiguous. Minor OCR noise (stray characters, garbled diacritics in a handful of words) was corrected by judgment where the surrounding context made the intended word unambiguous; nothing was fabricated. One narrow gap is flagged explicitly in [[AttExam 2016-02-09]] Q11, where the memo's enumerated points fall short of the 4 marks allocated — likely additional averments were expected that the OCR transcript didn't capture from the original layout.

| Sitting | OCR quality |
|---|---|
| 9 Feb 2016 (Part 1) | Clean |
| 16 Aug 2016 (Part 1) | Clean |
| 17 Aug 2016 (Part 3) | Clean |
| 14 Feb 2017 (Part 1) | Clean |
| 15 Feb 2017 (Part 3) | Clean |

## Progress board

![[Attorneys Exam.base]]

## Topics (20)

**Every paper (of their Part) / high frequency**
- [[Road Accident Fund Claims]]
- [[Bail Applications]]
- [[Statements and Pleas in Criminal Trials]]
- [[Particulars of Claim Drafting]]
- [[Contract Drafting — Standard Clauses]]
- [[Prescription of Claims]]
- [[Professional Ethics and Conduct]]

**Medium frequency**
- [[Interlocutory Applications and Notices of Motion]]
- [[Civil Appeal and Review Procedure]]
- [[Execution of Judgments and Interpleader]]
- [[Trial Notices for Expert and Documentary Evidence]]
- [[Costs, Tenders and Withdrawal of Action]]
- [[Magistrates' Court Jurisdiction]]
- [[Matrimonial Property and Divorce Procedure]]

**Lower frequency, still examinable**
- [[Default Judgment and Provisional Sentence]]
- [[Sale of a Business and Restraint of Trade]]
- [[Company, Close Corporation and Partnership Law]]
- [[Insolvency Law]]
- [[Consumer Protection Act]]
- [[Discharge, Withdrawal and Stopping of Criminal Prosecution]]

## Past papers (5 sittings)

| Sitting | Part | Note | Marks |
|---|---|---|---|
| 9 Feb 2016 | Part 1: Court Procedures | [[AttExam 2016-02-09]] | 100 |
| 16 Aug 2016 | Part 1: Court Procedures | [[AttExam 2016-08-16]] | 100 |
| 17 Aug 2016 | Part 3: Attorney's Practice | [[AttExam 2016-08-17]] | 100 |
| 14 Feb 2017 | Part 1: Court Procedures | [[AttExam 2017-02-14]] | 100 |
| 15 Feb 2017 | Part 3: Attorney's Practice | [[AttExam 2017-02-15]] | 100 |

## Recurring fact patterns worth knowing by name

- **"Plaintiff withdraws without tendering costs"** — tested near-verbatim in [[AttExam 2016-08-16]] Q4 and [[AttExam 2017-02-14]] Q15. See [[Costs, Tenders and Withdrawal of Action]].
- **Abandoned building/renovation contract, replacement contractor engaged at a different price** — the same structural fact pattern with different numbers in [[AttExam 2016-08-16]] Q9 (Improve-A-Home) and [[AttExam 2017-02-14]] Q12 (AB Builders CC). See [[Particulars of Claim Drafting]].
- **Bail affidavit immediately followed by a s112/s115 statement on the same accused** — the standard integrated criminal-procedure combo in [[AttExam 2016-02-09]] Q7.

## Notes on overlap with other modules

Several topics here (bail, s60(11B) disclosures, s115 statements, docket access) mirror core CCP-module topics, since the Board exam re-tests foundational criminal procedure alongside the newer civil/practice material. Per the hub's convention, this module's notes stand alone — no cross-module wikilinks — but the parallel is flagged in prose within [[Bail Applications]] and [[Statements and Pleas in Criminal Trials]] for anyone studying both modules together.

## Next steps once this module is approved

Continue rolling the same structure out across the remaining subject folders, then build the top-level `LLB hub.base` that rolls up every module's progress into one master board.

## Board exam archive update - 2026-10-19

- [[projects/Board Exam Archive]] - recovered papers, current state and remaining proofreading.
- [[notes/Board Exam OCR Audit]] - verified corrections, original PDF links and recovery evidence.
- [[Logs/2026-10-19 - Board Exam Archive]] - dated work record.

- [x] As of 2026-10-19: 66 recovered official PDFs and their Markdown are saved and indexed.
- [x] As of 2026-10-19: 14 sidecars corrected; 43 replacement characters resolved.
- [ ] Proofread bilingual text and financial tables against the original PDFs.

Use [[index]] for the catalogue, including the `Official Previous Papers 2015-2023` folder.

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
