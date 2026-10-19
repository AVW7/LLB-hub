---
type: dashboard
subject: PLE
tags:
  - ple/dashboard
---

# PLE — Professional Legal Ethics · Study Dashboard

Replicates the [[CCP Dashboard|CCP pilot]] structure for the PLE module: what the system is built out of, how to use it, and a live progress board.

## What this is built out of

```
PLE/
├── PLE Dashboard.md          ← this note
├── PLE.base                  ← live tracker (embedded below)
├── README.md                 ← original archive contents overview
├── notes/
│   ├── topics/                16 topic notes — the law, synthesised from every memo
│   │   └── ...
│   └── qa/                    9 exam-paper notes — real questions + real memo answers
│       └── ...
└── (18 original source files — .doc/.docx question papers, marking memoranda, one intro PDF)
```

- **Topic notes** (`notes/topics/`) are the revision layer — one per ethics topic, each with the rule, the exam pattern, and links to every past paper that tests it.
- **Q&A notes** (`notes/qa/`) are the self-test layer — one per exam sitting, every question reproduced with the real memo answer hidden behind a collapsible callout (click to reveal).
- Every note carries `status` in its frontmatter (`not-started` → `in-progress` → `reviewed` → `mastered`). Update that one field as you study and the dashboard board below updates itself — no separate tracker to maintain.
- **[[PLE.base]]** is the live database view over both note types. Open it directly in Obsidian for a sortable/filterable table, or use the embedded view below.

## How to use it

1. Open a **topic note** first to learn the rule and see which papers test it.
2. Work through the linked **Q&A notes** — read the question, attempt your own answer out loud or in writing, then expand the `> [!success]- Answer` callout to check yourself.
3. Update `status:` in that note's frontmatter as you go.
4. Come back here or open `PLE.base` to see what's left.

## Progress board

![[PLE.base]]

## Topics (16)

**Every paper / high frequency**
- [[Mandate Acceptance, Refusal and Withdrawal]]
- [[Defending a Guilty Client]]
- [[Trust Account Theft and the Attorneys Fidelity Fund]]
- [[Fee Assessment, Overreaching and Fee Sharing]]
- [[Admission as an Attorney and Fitness to Practise]]

**Frequently tested**
- [[Contingency Fee Agreements]]
- [[FICA Obligations on Attorneys]]
- [[Duty of Candour to the Court]]
- [[Recusal of a Judicial Officer]]
- [[Commissioner of Oaths Restrictions]]
- [[Borrowing From or Lending to Clients]]
- [[Trust Account Rules — Deposits and Fee Transfers]]
- [[Prescribed Claims — Ethical Duty and Negligence Liability]]
- [[Conflict of Interest]]

**Lower frequency, still examinable**
- [[Client Confidentiality and Privilege]]
- [[Interviewing an Opponent's Witness]]

## Past papers (9 sittings)

| Sitting | Note | Marks |
|---|---|---|
| 30 May 2015 | [[PLE 2015-05-30]] | 25 |
| 11 Jun 2015 (Supp) | [[PLE 2015-06-11 Supp]] | 25 |
| 14 Nov 2015 | [[PLE 2015-11-14]] | 25 |
| 26 Nov 2015 (Supp) | [[PLE 2015-11-26 Supp]] | 25 |
| 2 Dec 2015 (Special Supp) | [[PLE 2015-12-02 Special Supp]] | 25 — ⚠️ no marking memo on file |
| 28 May 2016 | [[PLE 2016-05-28]] | 25 |
| 15 Jun 2016 (Final Supp) | [[PLE 2016-06-15 Supp]] | 25 |
| 28 Jun 2016 (Special Supp) | [[PLE 2016-06-28 Special Supp]] | 25 |
| 2019 Assignment (Self-Assessment) | [[PLE 2019-02-03 Assignment]] | 100 — ⚠️ no marking memo on file (self-assessment by design) |

## Source material not yet converted into notes

- [[PLE2019Intro.pdf]] — "Introduction to Practice Management 2019" study guide. This is L.E.A.D's general practice-management reading material (value chain theory, business skills), not PLE exam content proper, and contains no exam questions to extract. Kept as background reading only — not linked from any topic or Q&A note.

## Recurring fact patterns worth knowing by name

- **The guilty-client dilemma** — client admits guilt in consultation but instructs a not-guilty plea. Tested with armed robbery ([[PLE 2015-05-30]]), rape ([[PLE 2016-05-28]]), and reckless/negligent driving with prior convictions ([[PLE 2019-02-03 Assignment]]) — same answer structure every time. See [[Defending a Guilty Client]].
- **Trust account theft by a bookkeeper/secretary** — appears in some form in six of the nine papers, always paired with a "some claims also prescribed" sub-question. See [[Trust Account Theft and the Attorneys Fidelity Fund]].
- **"Must you accept the first mandate, or are you free to choose?"** — the competing-mandates scenario appears near-verbatim in [[PLE 2015-11-14]] and [[PLE 2016-06-28 Special Supp]].
- **The magistrate's-son complainant** — the judicial recusal scenario appears in [[PLE 2015-11-14]] and [[PLE 2019-02-03 Assignment]] with an identical four-step escalation answer.
- **Deposit-for-costs mechanics** — the identical five-part deposit question appears word-for-word in [[PLE 2015-12-02 Special Supp]] (no memo) and [[PLE 2016-06-28 Special Supp]] (full memo) — use the latter to self-check the former.

## Next steps once this module is approved

Continue replicating this structure across the remaining subject folders, then build a top-level `LLB hub.base` that rolls up every module's progress into one master board.
