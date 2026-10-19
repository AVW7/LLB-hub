---
type: dashboard
subject: LDR
tags:
  - ldr/dashboard
---

# LDR — Labour Dispute Resolution · Study Dashboard

Replicates the [[CCP Dashboard|CCP pilot]] structure. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
LDR/
├── LDR Dashboard.md          ← this note
├── LDR.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                12 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                    8 exam-paper notes — real questions + real memo answers
│       └── ...
└── (16 original source files — .doc question papers and marking memoranda)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per labour-law topic, each with the rule as stated in the actual memos, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[LDR.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `LDR.base` to see what's left.

## Progress board

![[LDR.base]]

## Topics (12)

**Every paper / high frequency**
- [[Rescission of CCMA Arbitration Awards]]

**Frequently tested**
- [[Incapacity Dismissal Due to Ill Health]]
- [[Incapacity Dismissal for Poor Work Performance and Probation]]
- [[Protected and Unprotected Strikes]]
- [[Legal Representation at Hearings and the CCMA]]
- [[Retrenchment and Operational Requirements]]
- [[Discrimination Disputes]]
- [[Organisational Rights and Collective Bargaining]]

**Medium frequency**
- [[Employee vs Independent Contractor Status]]
- [[Disciplinary Hearing Procedure]]

**Lower frequency, still examinable**
- [[Automatically Unfair Dismissal on Pregnancy]]
- [[Onus of Proof in Unfair Dismissal]]

## Past papers (8 sittings)

Unlike CCP, every LDR paper in this archive is worth exactly **25 marks** — a consistent format across all eight sittings from 2009 to 2012.

| Sitting | Note | Marks |
|---|---|---|
| 3 Dec 2009 (Special Supp) | [[LDR 2009-12-03]] | 25 |
| 22 May 2010 | [[LDR 2010-05-22]] | 25 |
| 3 Jun 2010 (Supp) | [[LDR 2010-06-03 Supp]] | 25 |
| 16 Nov 2010 (Supp) | [[LDR 2010-11-16 Supp]] | 25 |
| Dec 2010 (Special Supp) | [[LDR 2010-12-15 Special Supp]] | 25 — near-identical to 3 Jun 2010 |
| 5 May 2012 | [[LDR 2012-05-05]] | 25 |
| 16 May 2012 (Supp) | [[LDR 2012-05-16 Supp]] | 25 — richest paper, 15-mark retrenchment letter |
| 28 Jun 2012 (Final Paper / Special Supp) | [[LDR 2012-06-28 Special Supp]] | 25 |

All 16 source `.doc` files converted cleanly to text via LibreOffice — none were scanned or required OCR, and all 8 question papers have a matching marking memorandum (no orphans in this module, unlike CCP's 2019 assignment).

## Source material not yet converted into notes

None — all 16 source files (8 question papers + 8 marking memoranda) are fully represented across the topic and Q&A notes above.

## Recurring fact patterns worth knowing by name

- **"Burger Plumbers / Mtembu"** and its twins ("Mark Pienaar," "ABC Electronics/Sonja Wilson") — the small-business-never-received-CCMA-notices rescission scenario. Appears in [[LDR 2010-05-22]] Q4, [[LDR 2010-06-03 Supp]] Q1 & Q4, [[LDR 2010-12-15 Special Supp]] Q1 & Q4 (word-for-word identical to 3 Jun 2010), and [[LDR 2012-05-05]] Q4 — always tests [[Rescission of CCMA Arbitration Awards]].
- **"Mike / X Computer Company"** — the chronic-absenteeism ill-health incapacity question, near-verbatim in [[LDR 2009-12-03]] Q1, [[LDR 2010-06-03 Supp]] Q3, [[LDR 2010-12-15 Special Supp]] Q3 — and reused with a probation twist (poor work performance, not ill health) in [[LDR 2012-05-16 Supp]] Q3 and [[LDR 2012-06-28 Special Supp]] Q4.
- **"Spar Supermarket"** protected-strike question — identical in [[LDR 2009-12-03]] Q3 and [[LDR 2010-11-16 Supp]] Q3.
- **"John / Brookes Hill"** sexual-orientation medical-scheme discrimination question — identical in [[LDR 2009-12-03]] Q2 and [[LDR 2010-11-16 Supp]] Q4.
- **3 June 2010 and December 2010 are near-duplicate papers** — same four questions, same fact patterns, same marks, word-for-word memo answers. Useful for spaced repetition without re-reading a new scenario.

## Next steps once this module is approved

Continue replicating this structure (`notes/topics/`, `notes/qa/`, module `Dashboard.md`, module `.base`) into the remaining subject folders, then build a top-level `LLB hub.base` that rolls up every module's progress into one master board.
