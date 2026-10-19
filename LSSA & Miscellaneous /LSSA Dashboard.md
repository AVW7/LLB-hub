---
type: dashboard
subject: LSSA
tags:
  - lssa/dashboard
---

# LSSA & Miscellaneous — Reference Library

This folder is different from every other module in the LLB hub. The other modules (CCP, CLP, PCT, HCP, MCP, and so on) are built from past exam papers and marking memoranda, and their notes follow a Q&A / topic-note structure aimed at exam self-testing.

This folder contains no exam papers. It holds three full primary-source legal texts — the Constitution of the Republic of South Africa, the Legal Practice Act 28 of 2014, and the Legal Practice Act Rules — each already OCR'd into a `markdown.md` file inside its own subfolder. There is nothing to rehearse here in a Q&A sense; there is only law to look up.

## What this is built out of

```
LSSA & Miscellaneous/
├── LSSA Dashboard.md              ← this note
├── LSSA.base                      ← reference-document tracker (embedded below)
├── notes/
│   ├── Constitution of RSA.md               ← chapter TOC + frequently referenced provisions
│   ├── Legal Practice Act 28 of 2014.md     ← chapter/Part TOC + frequently referenced provisions
│   └── Legal Practice Act Rules.md          ← Part TOC + frequently referenced provisions
├── Constitution of RSA.pdf/markdown.md              ← full constitutional text (source)
├── Legal Practice Act 28 of 2014.pdf/markdown.md    ← full Act text (source)
└── Legal Practice Act Rules.pdf/markdown.md         ← full Rules text (source)
```

- The three **reference index notes** in `notes/` are a navigable layer on top of the real source texts — a chapter/section table of contents plus short quoted excerpts of the provisions most likely to be cited from other modules. They link out to the real `markdown.md` files rather than duplicating them.
- **[[LSSA.base]]** is a simple tracker over the three reference notes (there is no exam-paper/topic split and no marks here, unlike the other modules' bases).

## How to use it

You will not normally start studying *here*. You'll arrive here from another module — e.g. a CCP topic note on bail applications cites s35(1)(d) of the Constitution's 48-hour rule, or a PLE topic note discusses trust-account discipline under s86 of the Legal Practice Act — and you want to check the exact wording of the provision being cited.

1. Open the relevant reference note (`Constitution of RSA`, `Legal Practice Act 28 of 2014`, or `Legal Practice Act Rules`).
2. Use its chapter/Part table of contents to find roughly where the provision lives, or check the "Frequently referenced provisions" section for a quick quote if it's a commonly cited one.
3. Follow the "Full text" link at the top of the note to open the complete source document and read the provision in full context.
4. Mark `status:` as `in-progress` once you've actually read through a document, or `reviewed` once you're comfortable navigating it.

## Progress board

![[LSSA.base]]
