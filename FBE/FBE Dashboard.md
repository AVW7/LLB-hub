---
type: dashboard
subject: FBE
tags:
  - fbe/dashboard
---

# FBE — Forms of Business Enterprise · Study Dashboard

Module 3.x. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
FBE/
├── FBE Dashboard.md          ← this note
├── FBE.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                 9 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                     7 exam-paper notes — real questions + real memo answers
│       └── ...
└── (14 original source files — .doc question papers and marking memoranda)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per legal topic, each with the rule, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[FBE.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `FBE.base` to see what's left.

## Progress board

![[FBE.base]]

## Topics (9)

**Every paper / high frequency**
- [[Close Corporations]]
- [[Choosing a Business Entity]]
- [[Partnerships]]
- [[Private Companies]]
- [[Sole Proprietorships]]
- [[Tax Rates and VAT Registration]]
- [[Trusts]]

**Medium frequency**
- [[Pre-Incorporation Contracts]]

**Lower frequency, still examinable**
- [[Judicial Management]]

## Past papers (7 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 3 Dec 2009 (Special Supp, Module 3.1) | [[FBE 2009-12-03 Special Supp]] | 25 |
| 22 May 2010 (Module 3.2) | [[FBE 2010-05-22]] | 25 |
| 3 Jun 2010 (Supp) | [[FBE 2010-06-03 Supp]] | 25 |
| 16 Nov 2010 (Supp, Module 3.2) | [[FBE 2010-11-16 Supp]] | 25 |
| 5 May 2012 (Module 3.2) | [[FBE 2012-05-05]] | 25 |
| 16 May 2012 (Supp, Module 3.2) | [[FBE 2012-05-16 Supp]] | 25 |
| 28 Jun 2012 (Special Supp, Module 3.2) | [[FBE 2012-06-28 Special Supp]] | 25 |

## Source material not yet converted into notes

None — all 14 source files (7 question papers + 7 marking memoranda) converted cleanly to text and are fully represented in the Q&A notes above. No orphan papers (every question paper in this module has a matching marking memo on file).

## Recurring fact patterns worth knowing by name

- **"Recommend a form of business enterprise for a client who fears personal liability"** — the answer is almost always the **Close Corporation**, motivated with the same handful of points (separate legal personality, cheap/simple formalities, single-person formation, limited liability, no separate board). Appears near-verbatim in [[FBE 2010-05-22]] Q1, [[FBE 2010-11-16 Supp]] Q2, and [[FBE 2012-05-16 Supp]] Q1. See [[Choosing a Business Entity]].
- **"How is entity X cited in an agreement"** — Partnership / Trust / Close Corporation / Sole Proprietorship citation wording, tested as a discrete 4-mark question in [[FBE 2010-11-16 Supp]] Q3.
- **VAT registration threshold changed mid-archive** — R300,000 p.a. in the 2009–2010 papers, R1,000,000 p.a. in the 2012 papers. See [[Tax Rates and VAT Registration]] — know which figure applies to the year in front of you.
- **"A sole proprietor is taxed at the flat rate of 40%"** — a recurring false trap, appears in [[FBE 2012-05-16 Supp]] Q3.3 and [[FBE 2012-06-28 Special Supp]] Q6.
- **Pre-incorporation contract requirements** — near-identical 6-point list tested in [[FBE 2009-12-03 Special Supp]] Q2, [[FBE 2010-06-03 Supp]] Q2, and [[FBE 2012-05-05]] Q2.

## Next steps once this module is approved

Replicate this same structure into any remaining subject folders, then roll every module's progress into the top-level `LLB hub.base`.
