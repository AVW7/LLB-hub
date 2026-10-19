---
type: dashboard
subject: BBST
tags:
  - bbst/dashboard
---

# BBST — Broad Based Skills Test · Study Dashboard

BBST is the **integrated practical exam** — every sitting mixes scenario-based questions across the other modules (insolvency, matrimonial/divorce, RAF/delict, CC/company liability, wills/succession, attorneys' fees, defamation, urgent applications, lease/eviction, domestic violence) into single Statement-of-Facts papers with multiple unrelated "waiting-room client" clusters. Topics therefore span many legal areas — that is the nature of the module, not a filing error.

## What this is built out of

```
BBST/
├── BBST Dashboard.md         ← this note
├── BBST.base                 ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── verification-report.md    ← archive audit (pre-existing)
├── notes/
│   ├── topics/                 20 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                     14 exam-paper notes — real questions + real memo answers
│       └── ...
└── (28 original source files — .doc/.docx/.pdf statements of facts, question papers, marking memoranda)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per legal skill/subject area, each with the rule, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal). Sittings with no surviving memo carry a `bbst/no-memo` tag and use a "self-check pointers" callout linking to the relevant topic notes instead.
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[BBST.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself. Where no memo survives, use the `> [!note]- Self-check pointers` callout and the linked topic note instead.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `BBST.base` to see what's left.

## Progress board

![[BBST.base]]

## Topics (20)

**Every paper / high frequency**
- [[Compulsory Sequestration and Acts of Insolvency]] — tested in 10 of 14 sittings, the single most-tested BBST topic
- [[Road Accident Fund Claims]]
- [[Divorce Actions and Settlement Agreements]]
- [[Matrimonial Property Systems]]

**Frequently tested (medium)**
- [[Personal Liability of CC Members]]
- [[Attorneys Fees and Fee Agreements]]
- [[Rescission of Judgment]]
- [[Lease Agreements and Eviction]]
- [[Urgent Applications and Interdicts]]
- [[Defamation]]
- [[Delictual Claims and Vicarious Liability]]
- [[Wills and Disqualified Beneficiaries]]

**Lower frequency, still examinable**
- [[Rehabilitation of an Insolvent Estate]]
- [[Pre-Trial Procedure and Expedited Judgment]]
- [[Maintenance Claims]]
- [[Domestic Violence Protection Orders]]
- [[Contingency Fee Agreements]]
- [[Intestate Succession and Customary Marriages]]
- [[Suretyship and the Matrimonial Property Act]]
- [[Universal Partnership and Breach of Promise to Marry]]

## Past papers (14 sittings)

| Sitting | Note | Marks | Notes |
|---|---|---|---|
| 20 Apr 2010 | [[BBST 2010-04-20]] | not stated | ⚠️ no marking memo — pre-2013 format, facts embedded in each question |
| 15 Dec 2010 (Special Supp) | [[BBST 2010-12-15 Special Supp]] | not stated | ⚠️ no marking memo |
| 9 Jun 2012 | [[BBST 2012-06-09]] | 120 | full memo present |
| 2013(1) | [[BBST 2013(1)]] | 100 | full memo present |
| 2013(1) Supplementary | [[BBST 2013(1) Supp]] | 100 | full memo present |
| 2013(2) Final | [[BBST 2013(2) Final]] | 100 | full memo present |
| 2013(2) Supplementary | [[BBST 2013(2) Supp]] | 100 | full memo present |
| 2014(1) Final | [[BBST 2014(1) Final]] | 100 | full memo present |
| 2014(2) | [[BBST 2014(2)]] | 100 | full memo present |
| 2014(2) Supplementary Assessment | [[BBST 2014(2) Supp]] | 100 | 🔁 reuses the [[BBST 2013(1)]] paper word-for-word |
| 2015(1) | [[BBST 2015(1) Statement of Facts Only]] | ~100 (per mark scheme) | ⚠️ Statement of Facts only — no question paper or memo survives |
| 2016(1) | [[BBST 2016(1)]] | 100 | full memo present; Statement of Facts reconstructed from the archived 2018(2) PDF (identical client) |
| 2017(2) | [[BBST 2017(2) Statement of Facts Only]] | not stated | ⚠️ Statement of Facts only — no question paper or memo survives |
| 28 Sep 2017 (LSSA-UNISA Assignment) | [[BBST 2017-09-28 Assignment]] | 100 | ⚠️ no marking memo |

## Source material not yet converted into notes

- [[BBST2017 Guideline writing BBST.docx]] — a general drafting/writing-style guideline document, not a scenario paper; not converted into a topic or Q&A note since it contains no examinable question content of its own.
- `BBST2018(2) Statement of Facts.pdf` — not given its own Q&A note because its content (Tsepo Mavuso, Station FM) was folded directly into [[BBST 2016(1)]] as the reconstructed Statement of Facts for that sitting (the question paper cross-references a "2016(1) Statement of Facts" that itself no longer survives standalone).

## Recurring fact patterns worth knowing by name

- **"Biko" / J&S Motors CC** — CC personal liability + sequestration + timed divorce + s2B Wills Act — appears verbatim in both [[BBST 2013(1)]] and [[BBST 2014(2) Supp]] (the same paper recycled ~18 months later), and closely parallels the S&Y Coins CC facts in [[BBST 2017(2) Statement of Facts Only]].
- **"Sure Rentals" commercial lease arrears + eviction** — near-identical combined summons fact pattern in [[BBST 2015(1) Statement of Facts Only]] and [[BBST 2017(2) Statement of Facts Only]].
- **Abusive ex-partner with a violent skill/profession** (MMA fighter; threats to kill; break-ins) triggering a domestic violence protection order — appears in [[BBST 2015(1) Statement of Facts Only]] and [[BBST 2017-09-28 Assignment]].
- **RAF amendment-date distinction** (pre- vs post-2008 RAF Act amendment governing general damages) — tested near-identically in [[BBST 2010-12-15 Special Supp]] Q3 and [[BBST 2012-06-09]] Q5.
- **"Tembi Ndlebe" rehabilitation timelines** — the same rehabilitation-options question, with refreshed numbers, in both [[BBST 2013(1) Supp]] and [[BBST 2013(2) Supp]].
- **Divorce timed to defeat creditors** — a joint estate divorced away just ahead of (or during) sequestration/liquidation proceedings recurs across the Biko facts, the Kruger/Bernato facts in [[BBST 2017(2) Statement of Facts Only]], and is explicitly flagged in [[Compulsory Sequestration and Acts of Insolvency]] and [[Rescission of Judgment]].
- **"Mavuso"/Station FM defamation + fee agreement + urgent interdict + sequestration risk + rescission** cluster — five legal issues built around one client in [[BBST 2016(1)]], reconstructed from the 2018(2) source PDF.

## Next steps

Once every sitting's `status` reaches `reviewed`/`mastered` and all topic notes are studied, return to the top-level LLB hub master dashboard to roll BBST's progress into the whole-archive board.
