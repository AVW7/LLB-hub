---
type: dashboard
subject: CLP
tags:
  - clp/dashboard
---

# CLP — Constitutional Practice · Study Dashboard

Third module built in the LLB hub study system, replicating the [[CCP Dashboard|CCP pilot]] structure (also see [[PCT Dashboard]]). This note is the front door: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
CLP/
├── CLP Dashboard.md          ← this note
├── CLP.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                14 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                    8 exam-paper notes — real questions + real memo answers
│       └── ...
└── (17 original source files — .doc/.docx question papers and marking memoranda,
     a lecture Q&A PDF, and a webinar slide deck)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per constitutional-practice topic, each with the rule as stated in the actual memos and real case law, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[CLP.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `CLP.base` to see what's left.

## Progress board

![[CLP.base]]

## Topics (14)

**Every paper / high frequency**
- [[Limitation of Rights]]

**Frequently tested**
- [[Locus Standi]]
- [[Amicus Curiae]]

**Medium frequency**
- [[Direct Access to the Constitutional Court]]
- [[Confirmation of Constitutional Invalidity]]
- [[Jurisdiction in Constitutional Matters]]
- [[Constitutional Remedies and Draft Orders]]

**Lower frequency, still examinable**
- [[Application of the Bill of Rights to Foreigners]]
- [[Equality and the Harksen Test]]
- [[Right to Privacy and the Prince Judgment]]
- [[Best Interests of the Child]]
- [[Forfeiture and the Right to Property]]
- [[Fit and Proper Person for Admission]]
- [[Leave to Appeal to the Constitutional Court]]

## Past papers (8 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 30 Jan 2010 | [[CLP 2010-01-30]] | 25 — *Nyathi* (State Liability Act s3) |
| 24 Jul 2010 | [[CLP 2010-07-24]] | 25 — Films and Publications Act s27 |
| Dec 2010 (Special Supp) | [[CLP 2010-12-15 Special Supp]] | 25 — ⚠️ no marking memo on file |
| 26 Jun 2012 (Special Supp) | [[CLP 2012-06-26 Special Supp]] | 25 — Vaal River mining/environmental rights |
| Jul 2012 Assignment | [[CLP 2012-07-15 Assignment]] | 100 — richest single paper, 11 sub-questions, POCA forfeiture |
| 21 Jul 2012 | [[CLP 2012-07-21]] | 25 — *Mohamed* extradition/death penalty |
| 2 Aug 2012 (Supp) | [[CLP 2012-08-02 Supp]] | 25 — fit and proper person, Rastafarian religion |
| 30 Jan 2019 Assignment | [[CLP 2019-01-30 Assignment]] | 25 — *Prince* (cannabis/privacy) |

## Source material not yet converted into notes

- [[CLPLecture2019Q&A.pdf]] — scanned, no extractable text layer (`pdftotext` returned only "Open Rubric"). OCR was attempted (`pdftoppm` + `tesseract`, 3 pages) but the output is too garbled to transcribe reliably as exam content — visible fragments suggest a fact pattern involving an arrest/detention of an activist (locus standi, NGOs, the Commission for Gender Equality) and a separate electoral-rights scenario (voting, party regalia at a polling station), but no confident quote can be sourced from it. Flagged as unusable rather than guessed at.
- [[CLPWebinar2019Slides.ppt]] — converted cleanly via LibreOffice → PDF → text (not scanned). Content is a structured summary of the standard CLP exam methodology (procedural: BOR application/s8, justiciability/standing/s38, jurisdiction/ss166-173; substantive: interpretation/s39, limitation/s36; remedy: ss38 and 172) plus a detailed SGBV/locus-standi fact pattern (Sesi Tlou/Tsakane/WEA) and an electoral-rights fact pattern (Mackenzie, party regalia at a polling station, a family member in prison). This slide deck maps closely onto the topics already built ([[Locus Standi]], [[Limitation of Rights]], [[Amicus Curiae]]) but was not turned into a standalone topic or Q&A note because it is lecture material without a marking memo — no graded model answers exist to transcribe.
- [[CLP 2012.2 SUPP ENG - only for appeal students.doc]] — despite its filename ("only for appeal students," filed as a "general" document in the hub index), this is in fact the real **2 August 2012** question paper — it pairs exactly with `CLP2Aug2012A.doc` (the Brown/Cape Law Society Rastafarian fact pattern). It has been used as the source question paper for [[CLP 2012-08-02 Supp]] rather than left unconverted.

## Recurring fact patterns worth knowing by name

- **"Brown"** appears in two unrelated fact patterns under the same surname — don't conflate them: the **child pornography/Films Act** Brown ([[CLP 2010-07-24]]) and the **Rastafarian dagga/Law Society articles** Brown ([[CLP 2012-08-02 Supp]]) are different clients in different years.
- **The s38/Rule 10 "standing + amicus" combo** — nearly every paper pairs a locus standi question with an amicus curiae question in the same fact pattern: [[CLP 2010-01-30]], [[CLP 2010-12-15 Special Supp]], [[CLP 2012-06-26 Special Supp]], [[CLP 2012-07-15 Assignment]], [[CLP 2012-07-21]] all do this — the amicus Rule 10 checklist is worth memorising cold since its wording barely changes between memos.
- **The "no immediate force" trap** — [[CLP 2010-01-30]] Q5 and [[CLP 2010-07-24]] Q1.3.2 both test the same point (s172(2)(a), Rule 16 confirmation) on different facts; the [[CLP 2012-08-02 Supp]] Q5 tests the sibling procedure (Rule 19 leave to appeal) that students often confuse with confirmation.
- **Real Constitutional Court judgments reproduced verbatim as "model answers"** — [[CLP 2010-01-30]] (*Nyathi*) and [[CLP 2019-01-30 Assignment]] (*Prince*) both build their memos directly around the text of the actual CC judgment rather than a paraphrase; know the paragraph-level detail, not just the headnote.

## Next steps once this module is approved

Continue replicating this structure (`notes/topics/`, `notes/qa/`, module `Dashboard.md`, module `.base`) into the remaining subject folders, then build a top-level `LLB hub.base` that rolls up every module's progress into one master board.
