---
type: dashboard
subject: IPM
tags:
  - ipm/dashboard
---

# IPM — Introduction to Practice Management · Study Dashboard

Replicates the [[CCP Dashboard|CCP pilot]] structure for Practice Management. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
IPM/
├── IPM Dashboard.md          ← this note
├── IPM.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                13 topic notes — the content, synthesised from every memo
│   │   └── ...
│   └── qa/                    7 exam-paper/assignment notes — real questions + real memo answers
│       └── ...
└── (13 original source files)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per practice-management topic, each with the content as stated in the actual memos, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam/assignment sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself.
- **[[IPM.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the content and see which papers test it.
2. Work through the linked **Q&A notes** — attempt your own answer, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `IPM.base` to see what's left.

## Progress board

![[IPM.base]]

## Topics (13)

**High frequency**
- [[Budgeting and Cash Flow]]
- [[Financial Reports in Practice]]
- [[The Business Plan]]
- [[The Management Process]]

**Medium frequency**
- [[Client Liaison and Complaint Handling]]
- [[Emotional Intelligence]]
- [[Filing Systems and Preventing Prescription]]
- [[Insurance for Practitioners]]
- [[Marketing Mix]]
- [[Office Administration and HR]]
- [[SWOT Analysis]]
- [[Statutory Requirements to Open a Practice]]

**Lower frequency, still examinable**
- [[FICA Reporting Obligations]]

## Past papers / assignments (7 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 19 May 2012 | [[IPM 2012-05-19]] | 25 |
| 1 Jun 2012 (Supp) | [[IPM 2012-06-01 Supp]] | 25 |
| 2012 Assignment | [[IPM 2012 Assignment]] | 25 |
| 27 Jun 2012 (Special Supp) | [[IPM 2012-06-27 Special Supp]] | 25 |
| Nov 2015 Assignment | [[IPM 2015-11 Assignment]] | 25 |
| 2016 Assignment | [[IPM 2016 Assignment]] | 25 |
| 2019-05 Self-Assessment Assignment | [[IPM 2019-05 Assignment]] | 55 — largest, no submission required |

## Next steps once this module is approved

Continue replicating this structure into the remaining subject folders, then build a top-level `LLB hub.base` that rolls up every module's progress into one master board.
