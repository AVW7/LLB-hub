---
type: dashboard
subject: COS
tags:
  - cos/dashboard
---

# COS — Legal Costs · Study Dashboard

Attorneys Act + court tariff scales; allocatur, taxation, party-and-party vs attorney-and-client costs, de bonis propriis, drawing/attendance fees, contingency fee agreements, VAT on fees. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
COS/
├── COS Dashboard.md          ← this note
├── COS.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                 9 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                     6 exam-paper notes — real questions + real memo answers
│       └── ...
└── (13 original source files — .doc/.docx question papers and marking memoranda)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per legal topic, each with the rule, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[COS.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer (including the full numerical workings for calculation questions) in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `COS.base` to see what's left.

## Progress board

![[COS.base]]

## Topics (9)

**Every paper / highest frequency**
- [[Allocatur Completion]]
- [[Costs Terminology]]
- [[Drawing Fee and Attendance Fee Scale]]
- [[VAT on Fees and Disbursements]]
- [[Statement of Account and Bill Preparation]]

**Frequently tested**
- [[Litigious vs Non-Litigious Matters]]

**Medium frequency**
- [[Taxation Procedure]]
- [[Contingency Fee Agreements]]

**Lower frequency, still examinable**
- [[Recovering Costs After Judgment]]

## Past papers (6 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 6 Mar 2010 | [[COS 2010-03-06]] | 25 |
| 18 Mar 2010 (Supp) | [[COS 2010-03-18 Supp]] | 25 |
| 7 Sep 2010 (Supp) | [[COS 2010-09-07 Supp]] | 25 |
| 2012(1) Special Supp (undated) | [[COS 2012 Special Supp]] | 25 |
| 30 Aug 2012 (Supp) | [[COS 2012-08-30 Supp]] | 25 |
| Module 2.1 Practice Paper (undated) | [[COS Module 2.1 Practice]] | 25 |

All 6 sittings have a matching marking memo — no orphan papers in this module.

## Source material not yet converted into notes

None — all 13 source files (`.doc`/`.docx`, 6 question papers + 7 memo files including one duplicate) converted and read in full. `COS30Aug2012A.docx` is a re-saved duplicate of `COS30Aug2012A.doc` with identical content — both are kept as source files but only one memo is cited from in the QA note.

## Recurring patterns worth knowing by name

- **The allocatur build-up sequence** (subtotal → less taxed off → drawing fee → disbursements → attendance fee (tiered) → VAT on each fee-type line → total) is identical across every calculation question — only the percentages and figures change. See [[Allocatur Completion]].
- **"Jay Zee / bigamy, District Court Durban"** statement-of-account fact pattern appears near-verbatim in [[COS 2010-09-07 Supp]] Q3 and [[COS 2012-08-30 Supp]] Q3, resolving to the identical figures (R23 250 → R26 505 → R21 505 due).
- **The six-step Law Society assessment procedure** for a non-litigious fee dispute is reproduced almost word-for-word in [[COS 2010-03-18 Supp]] Q3, [[COS 2010-09-07 Supp]] Q2, [[COS 2012-08-30 Supp]] Q2, and [[COS Module 2.1 Practice]] Q3 — memorise it once, apply it to any "client unhappy with a flat/lump-sum fee" scenario.
- **Textbook drawing-fee rate (6.25%/5%) vs worked-example rate (8.88% or 10.6%)** — two different memos ([[COS 2010-09-07 Supp]] Q4.4, [[COS 2012-08-30 Supp]] Q4.4) define the drawing fee at the lower textbook rate while their own Q1 allocatur calculations use a materially higher rate. See [[Drawing Fee and Attendance Fee Scale]] for how to handle this on the exam.
- **Two contingency-fee formulas, same underlying cap**: "double the normal fee or 25% of capital recovered, whichever is the lesser" ([[COS 2012 Special Supp]] Q4.4) vs the Contingency Fees Act phrasing of "up to 100% uplift, capped at 25% of the amount awarded" ([[COS Module 2.1 Practice]] Q5). See [[Contingency Fee Agreements]].

## Next steps

Part of the wider LLB hub rollout across all 14+ subject folders, feeding into a top-level master dashboard once every module is complete.
