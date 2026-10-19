---
type: dashboard
subject: MCP
tags:
  - mcp/dashboard
---

# MCP — Magistrate's Court Practice · Study Dashboard

Replicates the [[CCP Dashboard|CCP pilot]] structure. This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
MCP/
├── MCP Dashboard.md          ← this note
├── MCP.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                14 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                    6 exam-paper notes — real questions + real memo answers
│       └── ...
└── (14 original source files — .doc question papers, marking memoranda, rules PDF, webinar notes)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per procedural topic, each with the rule as drilled in the actual memos, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[MCP.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer (draft it out — this module is drafting-heavy), then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `MCP.base` to see what's left.

## Progress board

![[MCP.base]]

## Topics (14)

**Every paper / high frequency**
- [[Jurisdiction of the Magistrate's Court]]
- [[Summons and Particulars of Claim Drafting]]

**Frequently tested**
- [[Rule 14 Judgment|Summary Judgment (Rule 14)]]
- [[Default Judgment]]
- [[Expert Witness Notices (Rule 24)]]

**Medium frequency**
- [[Security for Costs]]
- [[Provisional Sentence]]
- [[Rescission of Default Judgment]]
- [[Warrants of Execution]]
- [[Notice of Bar]]
- [[Special Pleas, Exceptions and Further Particulars]]
- [[Settlement Agreements (Deed of Settlement)]]

**Lower frequency, still examinable**
- [[Demand Prior to Litigation]]
- [[Parties and Locus Standi]]

## Past papers (6 sittings)

Every question paper in this archive has a matching marking memo — no orphan papers in MCP, unlike CCP/PCT.

| Sitting | Note | Marks |
|---|---|---|
| 6 Mar 2010 | [[MCP 2010-03-06]] | 50 |
| 18 Mar 2010 (Supp) | [[MCP 2010-03-18 Supp]] | 50 |
| 7 Sep 2010 (Supp) | [[MCP 2010-09-07 Supp]] | 50 |
| Dec 2010 (Special Supp) | [[MCP 2010-12-15 Special Supp]] | 50 — exact day not stated in source |
| 2012(1) (Special Supp) | [[MCP 2012 Special Supp]] | 50 — exact date not stated in source |
| 30 Aug 2012 (Supp) | [[MCP 2012-08-30 Supp]] | 50 |

## Source material not yet converted into notes

- [[MCPMagCourtRules.pdf]] — the full Magistrates' Courts Rules (75,000+ words, extracted cleanly via `pdftotext`). Used as a cross-check reference for rule numbers/time periods cited in the topic notes, but not itself converted into a note — it's the primary legislation, not exam content. The archive's own `README.md` mislabels it as a "marking_memo," which it isn't.
- [[MCPWebinar2019Word.docx]] — 2019 webinar discussion notes covering demand, prescription, jurisdiction, and parties/locus standi in outline form. Fully converted to text and mined directly into [[Jurisdiction of the Magistrate's Court]], [[Demand Prior to Litigation]], and [[Parties and Locus Standi]] — the last of these three topics is sourced entirely from this file, since none of the six past papers test it directly.

## Recurring fact patterns worth knowing by name

- **"A. Brown / Red Leather CC"** — an oral loan to a close corporation plus a same-day written Deed of Suretyship from the sole member. Appears near-verbatim (only the years roll forward) in [[MCP 2010-09-07 Supp]] Q1 and [[MCP 2012-08-30 Supp]] Q1.
- **"Li Na v Koos Smith"** — an MVA particulars-of-claim comprehension exercise (peregrinus plaintiff, three alternative jurisdiction bases, illiquid damages claim). Appears near-verbatim in [[MCP 2010-09-07 Supp]] Q2 and [[MCP 2012-08-30 Supp]] Q2, and the same "settle for R8,000, pay by instalment" deed-of-settlement question follows immediately after both.
- **Expert witness notice periods (Rule 24(9)/(9)(a)/(9)(b)) — 15 days then 10 days** — tested in five of the six papers, occasionally with the companion Rule 24(10) notice for documentary/photographic evidence (10 days, 5-day objection window).
- **Suretyship as "surety and co-principal debtor," annexed and pleaded jointly and severally, one paying the other absolved** — the standard prayer wording drilled in every full particulars-of-claim question in this archive.

## Next steps once this module is approved

Continue replicating this structure (`notes/topics/`, `notes/qa/`, module `Dashboard.md`, module `.base`) into the remaining subject folders, then build a top-level `LLB hub.base` that rolls up every module's progress into one master board.
