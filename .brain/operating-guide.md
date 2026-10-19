# LLB Hub second brain

This vault is the source of truth for its legal study archive and explicitly saved knowledge.

## Start here

1. Read `brain.md`, the small navigation map.
2. Use `index.json` for archive metadata and topic/type filters; use `index.md` for the full catalogue.
3. Read only relevant downstream notes. Existing subject folders and dashboards remain authoritative for archive organization.

## Knowledge and sources

- Existing subject folders hold source documents and derived study notes. Preserve their paths and original documents.
- New general knowledge belongs in `notes/`, contacts in `people/`, and active work in `projects/`.
- One subject per note. Search before creating a note; link the source path, source date, and related notes.
- `MEMORY.md` holds approved stable preferences; `LEARNINGS.md` holds explicitly saved corrections; `decisions.md` records accepted decisions.
- Append dated operation records under `Logs/`. Keep the navigation map small.
- Many archive materials are historical. Never present an old exam answer, rate, threshold, deadline, or procedural rule as current law without a dated current authority. Mark unavailable verification clearly.

## User preferences

- Save and change knowledge only on explicit request. Conversation and corrections are not automatic capture triggers.
- Private note bodies, embeddings, transcription, and answers stay on this Mac. Hosted agents may inspect setup/code and metadata; do not load private note bodies into hosted model context.
- Public web research may use Firecrawl/Tavily separately; never include private vault content in remote requests.
- No scheduled memory maintenance or automatic outbound actions.
- Time zone: Africa/Johannesburg.

## Local tools

- Obsidian plugin: LLB Second Brain (`llb-second-brain`). Open Notes chat for cited vault questions.
- Ollama endpoint: `http://127.0.0.1:11434`; cloud features disabled.
- Embeddings: `embeddinggemma-2:270m`, with retrieval query/document prefixes.
- Answer model: `llb-brain` (Gemma 4 E2B Q4, 8192-token context).
- Search combines lexical BM25 ranking and cosine similarity with reciprocal-rank fusion.
- Saving, renaming, and deleting notes refreshes an existing local retrieval index; this does not create new knowledge notes.
- Prefer the vault-scoped Codex command skills and engine under `.agents/skills/`. Global skill settings are unchanged.

## Maintenance

Run `python3 .reindex.py` from this vault after adding/removing archive material; it regenerates the catalogue and subject READMEs.
Use Obsidian's "Notes: Index notes for RAG" command to build/rebuild the local retrieval index.
The previous long archive guide and pre-installation catalogues are preserved under `.brain/backups/`.
