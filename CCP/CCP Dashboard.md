---
type: dashboard
subject: CCP
tags:
  - ccp/dashboard
---

# CCP — Criminal Court Practice · Study Dashboard

Pilot module for the LLB hub study system. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
CCP/
├── CCP Dashboard.md          ← this note
├── CCP.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── verification-report.md    ← archive audit (pre-existing)
├── notes/
│   ├── topics/                15 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                    9 exam-paper notes — real questions + real memo answers
│       └── ...
└── (21 original source files — .doc question papers, marking memoranda, templates, slides)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per legal topic, each with the rule, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[CCP.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `CCP.base` to see what's left.

## Progress board

![[CCP.base]]

## Topics (15)

**Every paper / high frequency**
- [[Bail Applications]]
- [[Plea Procedure]]
- [[Appeal vs Review]]
- [[Sentencing and Mitigation]]

**Frequently tested**
- [[Discharge and Close of State's Case]]
- [[Appeal Procedure]]
- [[Access to the Police Docket]]

**Medium frequency**
- [[Objection to a Charge]]
- [[Legal Representation of Multiple Accused]]
- [[Rights of Arrested and Accused Persons]]

**Lower frequency, still examinable**
- [[Competent and Compellable Witnesses]]
- [[Seizure of Articles]]
- [[Mental Capacity Enquiries]]
- [[Securing Attendance of the Accused]]
- [[Forms J88 and SAP13]]

## Past papers (9 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 30 Jan 2010 | [[CCP 2010-01-30]] | 74 (richest paper — 15 Qs) |
| Dec 2010 (Special Supp) | [[CCP 2010-12-15 Supp]] | 72 |
| 28 Jan 2012 | [[CCP 2012-01-28]] | 50 |
| 26 Jun 2012 (Special Supp) | [[CCP 2012-06-26 Supp]] | 50 |
| 2 Aug 2012 (Supp) | [[CCP 2012-08-02 Supp]] | 50 |
| 26 Jan 2013 | [[CCP 2013-01-26]] | 50 |
| 26 Jul 2014 | [[CCP 2014-07-26]] | 50 |
| 25 Jul 2015 | [[CCP 2015-07-25]] | 50 |
| 2019 Assignment | [[CCP 2019-03 Assignment]] | 100 — ⚠️ no marking memo on file |

## Source material not yet converted into notes

- [[CCPHighCourtAppLeavetoAppeal.pdf]] — scanned, no extractable text (would need OCR)
- [[CCPWebinar2019Slides.pdf]] — scanned, no extractable text (would need OCR)
- [[CCPExampleAppLeaveToAppeal.doc]] — precedent template, referenced from [[Appeal Procedure]] rather than duplicated into its own note

## Recurring fact patterns worth knowing by name

- **"Joe Bloggs / Flip van der Merwe"** culpable homicide (iron bar, private defence) — appears in [[CCP 2012-01-28]] and [[CCP 2015-07-25]] almost verbatim.
- **"Fast Fingers / John Doe"** housebreaking-via-open-door — the recurring [[Plea Procedure|s113 correction of plea]] scenario, appears in [[CCP 2012-01-28]], [[CCP 2013-01-26]], [[CCP 2015-07-25]].
- **s60(11B) disclosures** — nearly word-for-word the same question in six of the nine papers.

## Next steps once this pilot is approved

Replicate this same structure (`notes/topics/`, `notes/qa/`, module `Dashboard.md`, module `.base`) into the other 13 subject folders, then build a **top-level `LLB hub.base`** that rolls up every module's progress into one master board.
