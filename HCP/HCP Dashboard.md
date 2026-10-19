---
type: dashboard
subject: HCP
tags:
  - hcp/dashboard
---

# HCP — High Court Practice · Study Dashboard

The largest standard module in the hub after BBST, replicating the [[CCP Dashboard|CCP pilot]] structure. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
HCP/
├── HCP Dashboard.md          ← this note
├── HCP.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                17 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                    12 exam-paper notes — real questions + real memo answers
│       └── ...
└── (24 original source files — .doc/.docx question papers, marking memoranda,
    a lecture slide deck, and two precedent/template documents)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per civil-procedure topic, each with the Uniform Rules of Court provisions as applied in the actual memos, drafting checklists lifted verbatim from model answers, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[HCP.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer (including drafting the document from scratch) before expanding the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `HCP.base` to see what's left.

## Progress board

![[HCP.base]]

## Topics (17)

**Every paper / high frequency**
- [[Particulars of Claim and Rule 18 Requirements]]
- [[Rule 32 Judgment Procedure]] *(Summary Judgment — Rule 32)*
- [[Notice of Intention to Defend]]
- [[Plea, Special Plea, Replication and Close of Pleadings]]

**Frequently tested**
- [[Application Procedure and Notice of Motion]]
- [[Parties, Citation and Legal Capacity to Litigate]]
- [[Jurisdiction of the High Court]]
- [[Exception, Irregular Proceedings and Striking Out]]
- [[Discovery]]
- [[Summons Types and the Essentialia]]

**Medium frequency**
- [[Interdicts]]
- [[Provisional Sentence Procedure]]
- [[Default Judgment and Rescission of Judgment]]
- [[Service of Process and Edictal Citation]]

**Lower frequency, still examinable**
- [[Appeal Procedure and Heads of Argument]]
- [[Review Procedure and Appeal vs Review]]
- [[Joinder, Third Party Procedure and Interpleader]]

> Note: the Rule 32 topic note is filed as `Rule 32 Judgment Procedure.md` (not `Summary Judgment.md`) — a vault-tooling quirk, not a substantive rename. The H1 heading inside the note is still "Summary Judgment — Rule 32".

## Past papers (12 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 19 Mar 2008 (Special Supp) | [[HCP 2008-03-19 Special Supp]] | 50 — ⚠️ no question paper on file |
| 6 Mar 2010 | [[HCP 2010-03-06]] | 50 |
| 18 Mar 2010 (Supp) | [[HCP 2010-03-18 Supp]] | 50 |
| 7 Sep 2010 (Supp) | [[HCP 2010-09-07 Supp]] | 50 |
| 5 Mar 2011 | [[HCP 2011-03-05]] | 50 |
| 20 Aug 2011 | [[HCP 2011-08-20]] | 50 |
| 3 Mar 2012 | [[HCP 2012-03-03]] | 50 — ⚠️ no question paper on file |
| 2012(1) Special Supp | [[HCP 2012-06-01 Special Supp]] | 50 |
| 30 Aug 2012 (Supp) | [[HCP 2012-08-30 Supp]] | 50 |
| 6 Sep 2013 (Supp) | [[HCP 2013-09-06 Supp]] | 50 |
| 1 Mar 2014 | [[HCP 2014-03-01]] | 50 |
| 2019 Assignment | [[HCP 2019-03-07 Assignment]] | 100 — ⚠️ no marking memo on file |

## Source material — all 24 files converted and read

Unlike some other modules, **nothing in HCP required OCR** — every `.doc`/`.docx` converted cleanly via LibreOffice, and both PDFs (`HCP2015Slides.pdf`, `HCP Example - Heads of argument.pdf`) had extractable text via `pdftotext`. Two items are referenced from topic notes rather than duplicated into their own notes:

- [[HCP2015Slides.pdf]] — a ~226-slide practice lecture deck (jurisdiction, pleadings, discovery, applications, interdicts, appeal/review, execution/sale in execution). Mined directly into the relevant topic notes ([[Jurisdiction of the High Court]], [[Application Procedure and Notice of Motion]], [[Discovery]], [[Appeal Procedure and Heads of Argument]], [[Default Judgment and Rescission of Judgment]] in particular) rather than made into a standalone note, since its content is procedural background rather than examined Q&A.
- [[HCP NoticeofAppeal.doc]] — a full worked precedent (Minister of Water Affairs v Exxaro Coal) — referenced from [[Appeal Procedure and Heads of Argument]] as the structural model for grounds of appeal.
- [[HCP Example - Heads of argument.pdf]] — a full worked precedent (S v Penxa, respondent's heads on leave to appeal + condonation) — referenced from [[Appeal Procedure and Heads of Argument]] as the structural model for heads of argument.

## Recurring fact patterns worth knowing by name

- **"John Brown v Paul Naidoo"** — the Notice of Intention to Defend drafting scenario, near word-for-word in [[HCP 2010-09-07 Supp]] and [[HCP 2012-08-30 Supp]].
- **"Mr Moon / Sunshine Daily Newspaper"** — the urgent interdict-against-publication scenario, near word-for-word in [[HCP 2010-09-07 Supp]] and [[HCP 2012-08-30 Supp]].
- **"Daniel Steyn / Minister for Safety and Security / John Brown Trust"** — the Rule 17 citation trio (minor, state functionary, trust), near word-for-word in [[HCP 2010-09-07 Supp]], [[HCP 2011-08-20]] and [[HCP 2012-08-30 Supp]].
- **"Shopkeeper slip-and-fall"** — Rule 36 expert/medical-examination/photograph notices, near word-for-word in [[HCP 2011-08-20]] and [[HCP 2012-06-01 Special Supp]].
- **"Peregrinus debtor in Berlin"** — the ex parte attachment-to-found-jurisdiction scenario, near word-for-word in [[HCP 2011-08-20]] and [[HCP 2012-06-01 Special Supp]].
- **Motor-collision special plea of prescription** — the same four-line special plea template, with only dates changed, in [[HCP 2010-09-07 Supp]], [[HCP 2011-03-05]], [[HCP 2012-08-30 Supp]] and [[HCP 2013-09-06 Supp]].
- **Palmer/farm-sale occupational-rental interdict** — action vs application choice + interim/final interdict requirements, near-identical in [[HCP 2013-09-06 Supp]] and [[HCP 2012-03-03]].

## Next steps once this module is approved

Continue replicating this structure (`notes/topics/`, `notes/qa/`, module `Dashboard.md`, module `.base`) into the remaining subject folders, then build a top-level `LLB hub.base` that rolls up every module's progress into one master board.
