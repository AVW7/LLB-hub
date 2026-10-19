---
type: dashboard
subject: ICP
tags:
  - icp/dashboard
---

# ICP — Introduction to Conveyancing Practice · Study Dashboard

Module 3.2 of the LLB hub. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
ICP/
├── ICP Dashboard.md          ← this note
├── ICP.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                 14 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                     9 exam-paper notes — real questions + real memo answers
│       └── ...
└── (13 original source files — .doc question papers and marking memoranda)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per legal topic, each with the rule, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal). Where the original question paper did not survive in the archive, the memo answers are still reproduced in full, flagged with a warning callout.
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[ICP.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `ICP.base` to see what's left.

## Progress board

![[ICP.base]]

## Topics (14)

**Every paper / high frequency**
- [[Exclusive Use Areas]]
- [[Mortgage Bonds — Registration and Cancellation]]
- [[Sectional Title Schemes]]
- [[Transfer of Land — Role Players and Process]]
- [[Deeds Registration Process]]
- [[Body Corporate — Management and Conduct Rules]]
- [[Types of Property Ownership]]

**Medium frequency**
- [[Real Rights vs Personal Rights]]
- [[FICA Compliance in Conveyancing]]
- [[Marital Property Regimes and Conveyancing]]
- [[Minors and Trusts in Conveyancing Transactions]]
- [[Trust Account, Guarantees and Undertakings]]

**Lower frequency, still examinable**
- [[Cooling-Off Right for Purchasers]]
- [[Zero-Rated VAT Transactions]]

## Past papers (9 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 15 Dec 2010 (Special Supp) | [[ICP 2010-12-15 Supp]] | 50 |
| 5 May 2012 | [[ICP 2012-05-05]] | 50 |
| 16 May 2012 (Supp) | [[ICP 2012-05-16 Supp]] | 50 |
| 28 Jun 2012 (Special Supp) | [[ICP 2012-06-28 Supp]] | 50 |
| 24 Oct 2015 | [[ICP 2015-10-24]] | 50 — ⚠️ no question paper on file |
| 3 Dec 2015 (Special Supp) | [[ICP 2015-12-03 Supp]] | 50 — ⚠️ no question paper on file |
| 7 May 2016 | [[ICP 2016-05-07]] | 50 — ⚠️ no question paper on file |
| 19 May 2016 (Supp) | [[ICP 2016-05-19 Supp]] | 50 — ⚠️ no question paper on file (same memo as 2015-12-03) |
| 29 Jun 2016 (Special Supp) | [[ICP 2016-06-29 Supp]] | 50 — ⚠️ no question paper on file (recycled 2012-05-16 paper — question text reconstructed from that sitting) |

## Source material

All 13 original `.doc` files (4 question papers + 9 marking memoranda) converted cleanly to text and were read in full — nothing in this module needed OCR, and nothing was unusable.

Five of the nine sittings only have a marking memorandum on file, with no matching question paper (2015-10-24, 2015-12-03 Supp, 2016-05-07, 2016-05-19 Supp, 2016-06-29 Supp). For two of those (2016-05-19 Supp and 2016-06-29 Supp), the underlying paper is confirmed recycled from an earlier sitting that *does* have a surviving question paper (2015-12-03 Supp and 2012-05-16 Supp respectively), so real question wording could be reconstructed with confidence for 2016-06-29 Supp. For the other three orphan memos, question headings in the Q&A notes are paraphrased from the memo's own structure and flagged accordingly — never presented as verbatim exam wording.

## Recurring fact patterns and traps worth knowing by name

- **The true/false block on Q1 of the 16 May 2012 Supp paper** (deeds registration basics, sectional title, mortgage bonds, FICA) is recycled almost verbatim as Q1 of the 29 June 2016 Special Supp paper — same 15 answers.
- **The FICA/coordination/certificate/VAT/definitions/cooling-off paper** (3 Dec 2015 Special Supp) is recycled word-for-word as the 19 May 2016 Supp paper.
- **"On prep"** — consistently defined as: deed passed by the examiners, notes attended to, finances in order, sitting after examination and before execution/registration. Watch the minor wording inconsistency between the 2012 and 2016 memos of the same recycled paper.
- **Exclusive Use Areas** — some form of EUA question (s27 vs s27A, definition, mortgageability, cession, undisclosed real right of extension) appears in almost every single sitting.
- **The "T / BC / BC / B" lodgement sequence** for a linked transfer-plus-bond-cancellation-plus-new-bond transaction appears as a stand-alone sequencing question.

## Next steps

This module follows the same structure as the CCP pilot (see `CCP Dashboard.md` in the CCP folder): `notes/topics/`, `notes/qa/`, module `Dashboard.md`, module `.base`.
