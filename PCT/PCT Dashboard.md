---
type: dashboard
subject: PCT
tags:
  - pct/dashboard
---

# PCT — Professional Conduct · Study Dashboard

Second module built in the LLB hub study system, replicating the [[CCP Dashboard|CCP pilot]] structure. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
PCT/
├── PCT Dashboard.md          ← this note
├── PCT.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                15 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                    9 exam-paper notes — real questions + real memo answers
│       └── ...
└── (16 original source files — .doc question papers and marking memoranda)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per conduct-rule topic, each with the rule as stated in the actual memos, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[PCT.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `PCT.base` to see what's left.

## Progress board

![[PCT.base]]

## Topics (15)

**Every paper / high frequency**
- [[Trust Account Theft and the Attorneys Fidelity Fund]]

**Frequently tested**
- [[Prescribed Claims and the Attorneys Insurance Indemnity Fund]]
- [[Accepting, Refusing and Withdrawing from a Mandate]]
- [[Conflict of Interest]]
- [[Defending a Client Who Admits Guilt]]
- [[Duty to the Court and Opposing Counsel]]
- [[Confidentiality, Privilege and Protected Communications]]

**Medium frequency**
- [[Contingency Fee Agreements]]
- [[Borrowing Money From or Investing With a Client]]
- [[Commissioner of Oaths Conflicts]]
- [[Fit and Proper Person and Striking Off the Roll]]
- [[Fees, Trust Deposits and Billing Practice]]
- [[Declining Work Outside Your Competence]]

**Lower frequency, still examinable**
- [[Requirements for Admission as an Attorney]]
- [[Sources of the Rules of Professional Conduct]]

## Past papers (9 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 3 Dec 2009 (Special Supp) | [[PCT 2009-12-03 Special Supp]] | 25 — ⚠️ memo only, no question paper survives |
| 30 Jan 2010 | [[PCT 2010-01-30]] | 25 |
| 24 Jul 2010 | [[PCT 2010-07-24]] | 25 |
| Dec 2010 (Special Supp) | [[PCT 2010-12-15 Special Supp]] | 25 |
| 19 May 2012 | [[PCT 2012-05-19]] | 25 — single integrated scenario |
| 1 Jun 2012 (Supp) | [[PCT 2012-06-01 Supp]] | 25 |
| 27 Jun 2012 (Special Supp) | [[PCT 2012-06-27 Special Supp]] | 25 — ⚠️ no marking memo on file |
| 18 May 2013 | [[PCT 2013-05-18]] | 25 |
| 31 May 2014 (Final Paper) | [[PCT 2014-05-31]] | 25 — richest single paper, 11 questions |

## Source material not yet converted into notes

All 16 source files converted cleanly to text via LibreOffice — none were scanned or required OCR. Two quirks worth flagging:

- [[PCT3Dec2009Q.doc]] — filename suggests a question paper, but the actual content is a marking memorandum with brief answer statements; no question wording survives for this sitting. Handled in [[PCT 2009-12-03 Special Supp]] with an explicit warning and only the real memo text (no invented question wording).
- [[PCT27Jun2012Q.doc]] — genuine orphan question paper; no matching `PCT27Jun2012A.doc` exists in the archive. Handled in [[PCT 2012-06-27 Special Supp]] with self-check pointers to topic notes instead of a model answer.

## Recurring fact patterns worth knowing by name

- **The absconding/thieving bookkeeper** — a bookkeeper or secretary steals trust money and a personal injury or other claim is discovered to have prescribed at the same time. This near-identical fact pattern anchors [[PCT 2010-01-30]] Q2, [[PCT 2010-07-24]] Q2, [[PCT 2010-12-15 Special Supp]] Q4, [[PCT 2012-05-19]] (the whole paper), and [[PCT 2012-06-27 Special Supp]] Q4 — always tests [[Trust Account Theft and the Attorneys Fidelity Fund]] and [[Prescribed Claims and the Attorneys Insurance Indemnity Fund]] together.
- **The client who admits guilt but wants a not-guilty plea** — appears in [[PCT 2010-07-24]] Q1 (armed robbery) and twice in [[PCT 2010-12-15 Special Supp]] (Q2 and Q3.3, both murder) — the ethical-limits answer is consistent across all three: no false version to witnesses, no misleading the court, but full latitude to attack the State's case.
- **The adverse-authority-and-recusal double question** — [[PCT 2010-01-30]] Q3 and [[PCT 2013-05-18]] Q1 are near word-for-word the same question (new SCA authority against the client; magistrate is the complainant's relative), with identical memo answers.
- **The reluctant commissioner of oaths** — a partner is asked to commission an urgent affidavit for the firm's own client; appears in [[PCT 2013-05-18]] Q2 and (as an orphan question) [[PCT 2012-06-27 Special Supp]] Q3.

## Next steps once this module is approved

Continue replicating this structure (`notes/topics/`, `notes/qa/`, module `Dashboard.md`, module `.base`) into the remaining subject folders, then build a top-level `LLB hub.base` that rolls up every module's progress into one master board.
