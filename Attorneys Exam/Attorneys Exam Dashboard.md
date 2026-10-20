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

## Topics (26)

**Every paper (of their Part) / high frequency**
- [[Road Accident Fund Claims]] *(Part 1)*
- [[Bail Applications]] *(Part 1)*
- [[Statements and Pleas in Criminal Trials]] *(Part 1)*
- [[Particulars of Claim Drafting]] *(Part 1)*
- [[Liquidation and Distribution Accounts]] *(Part 2: Estates)*
- [[Estate Duty Calculations and Section 4A Rebate]] *(Part 2: Estates)*
- [[Intestate Succession and Representation]] *(Part 2: Estates)*
- [[Wills, Codicils, Massing and Section 2(3) Condonation]] *(Part 2: Estates)*
- [[Contract Drafting — Standard Clauses]] *(Part 3)*
- [[Prescription of Claims]] *(Part 3)*
- [[Professional Ethics and Conduct]] *(Part 3)*
- [[Trust and Business Accounting, Transfers and Reconciliations]] *(Part 4: Bookkeeping)*
- [[Correspondent Accounting, Conveyancing Statements and VAT]] *(Part 4: Bookkeeping)*

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

## Past papers (12 self-test notes + 66 archive sittings)

| Sitting | Part | Note | Marks |
|---|---|---|---|
| 9 Feb 2016 | Part 1: Court Procedures | [[AttExam 2016-02-09]] | 100 |
| 16 Aug 2016 | Part 1: Court Procedures | [[AttExam 2016-08-16]] | 100 |
| 17 Aug 2016 | Part 3: Attorney's Practice | [[AttExam 2016-08-17]] | 100 |
| 14 Feb 2017 | Part 1: Court Procedures | [[AttExam 2017-02-14]] | 100 |
| 15 Feb 2017 | Part 3: Attorney's Practice | [[AttExam 2017-02-15]] | 100 |
| 15 Feb 2017 | Part 4: Bookkeeping | [[AttExam 2017-02-15 P4]] | 100 |
| 23 Aug 2017 | Part 4: Bookkeeping | [[AttExam 2017-08-23 P4]] | 100 |
| 6 Feb 2018 | Part 2: Estates | [[AttExam 2018-02-06 P2]] | 100 |
| 15 Oct 2018 | Part 2: Estates | [[AttExam 2018-10-15 P2]] | 100 |
| 7 Mar 2019 | Part 4: Bookkeeping | [[AttExam 2019-03-07 P4]] | 100 |
| 21 Aug 2019 | Part 2: Estates | [[AttExam 2019-08-21 P2]] | 100 |
| 2022–2023 (16 papers) | Parts 1–4 (Orphan Question Papers) | [[AttExam 2022-2023 Orphan Papers]] | 100 ea |

## Recurring fact patterns worth knowing by name

- **"Plaintiff withdraws without tendering costs"** — tested near-verbatim in [[AttExam 2016-08-16]] Q4 and [[AttExam 2017-02-14]] Q15. See [[Costs, Tenders and Withdrawal of Action]].
- **Abandoned building/renovation contract, replacement contractor engaged at a different price** — the same structural fact pattern with different numbers in [[AttExam 2016-08-16]] Q9 (Improve-A-Home) and [[AttExam 2017-02-14]] Q12 (AB Builders CC). See [[Particulars of Claim Drafting]].
- **Bail affidavit immediately followed by a s112/s115 statement on the same accused** — the standard integrated criminal-procedure combo in [[AttExam 2016-02-09]] Q7.
- **Joint Estate Funeral Expense Add-Back (Paper 2)** — in a marriage in community of property, add funeral expenses back before splitting the net joint estate 50/50 for the surviving spouse, then deduct 100% of funeral expenses from the deceased's half-share ([[AttExam 2018-02-06 P2]] Q1).
- **Nasciturus + Murderer Child (s1(7)) + Renouncing Child (s1(6)) Combo (Paper 2)** — a murderer's descendants take by representation under s1(7), whereas a renouncing child's share vests in the surviving spouse under s1(6), and a minor cannot renounce ([[AttExam 2018-10-15 P2]] Q2).
- **Instructing vs Correspondent 1/3 Allowance + Property Transfer Statement (Paper 4)** — tested in every bookkeeping sitting ([[AttExam 2017-02-15 P4]], [[AttExam 2017-08-23 P4]], [[AttExam 2019-03-07 P4]]).

## Notes on overlap with other modules

Several topics here (bail, s60(11B) disclosures, s115 statements, docket access) mirror core CCP-module topics, since the Board exam re-tests foundational criminal procedure alongside the newer civil/practice material. Per the hub's convention, this module's notes stand alone — no cross-module wikilinks — but the parallel is flagged in prose within [[Bail Applications]] and [[Statements and Pleas in Criminal Trials]] for anyone studying both modules together.

## 2015–2023 Official Archive & OCR Status (2026-10-19)

- **Question Papers (2015–2023)**: All **66** official question papers in `Attorneys Exam/Official Previous Papers 2015-2023/` have searchable Markdown sidecars and pass the text-integrity audit ([[notes/Board Exam OCR Audit]]).
- **Official Marking Memoranda (2015–2021)**: **50** matching official LEAD marking memoranda in `Attorneys Exam/Official Memoranda 2015-2021/` are paired with their question papers in [[notes/Board Exam Memo Coverage]] and upgraded with structured table extractions from [[notes/Board Exam Mistral OCR - 2026-10-19]], with flagged Estates (Paper 2) and Bookkeeping (Paper 4) tables reviewed and aligned against the original PDFs.
- **Remaining 2022–2023 Gaps**: **16** recent question papers (2022–2023) have no public official memo located yet ([[notes/Board Exam Memo Search - 2026-10-19]]) and are tracked for self-test in [[AttExam 2022-2023 Orphan Papers]]. See [[projects/Board Exam Archive]] and [[Logs/2026-10-19 - Board Exam Archive]].

## Candidate model answers for 2022-2023 (pending verification) - 2026-10-19

- [[Attorneys Exam/Candidate Model Answers 2022-2023/README]] links 16 complete 100-mark candidate model memoranda (`official: false`, `verification-status: pending-multi-agent-review`) generated for the 16 2022–2023 papers lacking public official LSSA LEAD PDFs, grounded in the 2015–2021 official memoranda and public walkthrough transcripts.
