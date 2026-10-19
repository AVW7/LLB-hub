# Handoff: LLB Hub local second brain

Snapshot: **2026-10-19 14:40 Africa/Johannesburg**. Recheck live state before continuing.

## User intent

Implement a second brain in the existing **`/Users/ajad/Desktop/LLB hub`** folder,
using Obsidian. “LLB hub” is the attached legal-study archive, not an LLM provider.
The user now requested this handoff for other agents.

Preferences already established:

- Dedicated Obsidian interface; this Mac mini first.
- Private notes, embeddings, and answering stay local.
- Explicit knowledge saves; no automatic conversation capture or scheduled memory jobs.
- Firecrawl and Tavily can research public material separately.
- Reuse and improve an existing open-source plugin where useful.
- The user explicitly approved enabling the LLB plugin in Obsidian after the
  Restricted-mode prompt. That approval has already been used; the plugin is enabled.

## Current outcome

**Implemented and running:**

- Obsidian 1.14.4 has LLB Hub registered and open.
- `brain.md` is the new short navigation map, linked to the existing dashboards.
- New `notes/`, `people/`, `projects/`, `Templates/`, `Logs/`, `MEMORY.md`,
  `LEARNINGS.md`, `decisions.md`, `_CLAUDE.md`, and `CLAUDE.md` provide the
  explicit-save workflow. Existing study notes remain in their subject folders.
- 47 command skills plus their shared engine are installed **inside this vault**
  at `.agents/skills/`. Their default vault and shared-engine paths point here.
- A local fork of Local LLM Helper is installed and enabled as **LLB Second Brain**.
- Ollama 0.40.6 is installed, running on `127.0.0.1:11434`, and cloud features are disabled.
- `embeddinggemma-2:270m` is installed and has built a real local retrieval index.
- Obsidian's Notes chat is open, showing **541 indexed files / entire vault**.

**Still pending:**

- The answering model `gemma4:e2b-it-q4_K_M` is downloading.
- The ongoing setup process is meant to create the `llb-brain` model after the pull.
- Consequently, do not claim local answering is ready until both models appear in
  `ollama list`. Do not switch to a cloud fallback.

The model pull's last printed progress was 20% of its current large blob, not 20%
of the whole installation. There is no reliable ETA.

## Paths

| Item | Path |
|---|---|
| Active vault | `/Users/ajad/Desktop/LLB hub` |
| Navigation map | `/Users/ajad/Desktop/LLB hub/brain.md` |
| Existing archive instructions | `/Users/ajad/Desktop/LLB hub/AGENTS.md` |
| Additional operating guide | `/Users/ajad/Desktop/LLB hub/.brain/operating-guide.md` |
| Setup state | `/Users/ajad/Desktop/LLB hub/.brain/setup-status.json` |
| Local plugin install | `/Users/ajad/Desktop/LLB hub/.obsidian/plugins/llb-second-brain/` |
| Retrieval index | same directory, `embeddings.json` |
| Plugin source | `/Users/ajad/Documents/ChatGPT/local_voice/llb-local-llm-helper` |
| Local model definition | `/Users/ajad/Documents/ChatGPT/local_voice/LLBBrain.Modelfile` |
| Runtime agent | `/Users/ajad/Library/LaunchAgents/com.ajad.llb-ollama.plist` |
| Runtime log | `/Users/ajad/Library/Logs/LLBBrain/ollama.log` |
| Ollama configuration | `/Users/ajad/.ollama/server.json` |
| Original-file hashes | `/Users/ajad/Desktop/LLB hub/.brain/baseline.json` |
| Pre-setup metadata backups | `/Users/ajad/Desktop/LLB hub/.brain/backups/20261019-142732/` |
| Reindexer output | `/Users/ajad/Desktop/LLB hub/.brain/reindex.log` |

The earlier generic vault `/Users/ajad/Documents/Second Brain` still exists.
Global skill settings still point there: they were intentionally preserved.
Use the **LLB Hub workspace-scoped skills**, or specify this vault explicitly.

## Retrieval facts already observed

These are actual installed-index counts, not an evaluation benchmark:

- 541 sources: **334 Markdown, 202 Word documents, 5 text PDFs**.
- 7,378 chunks, 768-dimensional embeddings; about 77.5 MB of stored index JSON.
- Embedding profile: `llb-prefixes-and-code-v1`.
- The folder contained 906 Markdown files before setup, including 554 page
  extraction artifacts. Those artifacts are intentionally excluded from retrieval.
- Three image-only/scanned PDFs have no indexed text. OCR is not enabled.
- The existing `.reindex.py` successfully refreshed the archive catalogue to
  562 entries. Its catalogue and the retrieval index have different inclusion rules.
- All **1,125 protected original files** still matched their saved hashes after setup.

## Plugin implementation

Source branch: `codex/llb-second-brain`.
Upstream: `manimohans/obsidian-local-llm-helper`, tag 2.6.2, commit
`4758fefa3041aaa0d1a226942a4f392b1f0aff06`. MIT attribution is retained.
This is a local fork; no GitHub fork, PR, push, or commit was created.

Read `LLB-CHANGES.md` in the plugin source for the change list. Main changes:

1. Plugin ID `llb-second-brain`, version `2.6.2-llb.1`.
2. Model endpoints restricted to HTTP loopback; built-in web search and the
   automatic update check disabled.
3. EmbeddingGemma 2 query prefix `task: search result | query: ...` and document
   prefix `title: ... | text: ...`; batch size eight.
4. BM25 lexical ranking plus cosine similarity, combined by reciprocal-rank fusion.
5. Code blocks retained in Markdown; stored embedding profile prevents loading
   vectors built with older formatting.
6. `.doc`/`.docx`/`.rtf` extracted locally with `/usr/bin/textutil` using `execFile`,
   not shell interpolation. Citations use original document paths.
7. Hidden files, generated catalogues, templates, operation logs, and duplicate
   `pages/` artifacts excluded from retrieval.
8. Existing indexes refresh after saved edits, creation, renaming, or deletion.
9. A map-opening command and historical-archive grounding rules were added.

`pnpm run build` passed TypeScript checking and bundling. Automated tests and an
answer-quality evaluation were **not run**; the user did not request them.
The actual Obsidian indexing operation completed successfully.

## Local runtime

The LaunchAgent runs Ollama at login with:

```text
OLLAMA_HOST=127.0.0.1:11434
OLLAMA_NO_CLOUD=1
OLLAMA_CONTEXT_LENGTH=8192
OLLAMA_NUM_PARALLEL=1
OLLAMA_MAX_LOADED_MODELS=1
OLLAMA_FLASH_ATTENTION=1
OLLAMA_KV_CACHE_TYPE=q8_0
```

The runtime log explicitly confirmed `Ollama cloud disabled: true` and the loopback bind.
This is a model-serving daemon, not a scheduled memory-maintenance job.

Chat settings: `llb-brain`, temperature 0.2, max output 1,024 tokens, six retrieval
chunks. The Modelfile derives from `gemma4:e2b-it-q4_K_M` with an 8K context.
Radar, scheduled indexing, and automatic vault actions are disabled.

The in-progress pull runs in the originating chat's exec session **43137**.
It downloads both models sequentially and then runs `ollama create llb-brain`.
Another chat may not be able to poll that session; use the local service and logs.
Do not start duplicate pulls without checking the existing job.

## Continuation steps

1. Read this vault's existing `AGENTS.md` and `.brain/operating-guide.md`.
2. Check the runtime and installed models:

   ```sh
   /opt/homebrew/bin/ollama list
   /opt/homebrew/bin/ollama ps
   ```

   The execution sandbox requires escalation for localhost network access.
   A sandbox `URLError` alone does not establish that Ollama is down.

3. If the original pull is still active, let it finish. If it stopped before the
   base model became available, resume the existing download:

   ```sh
   /opt/homebrew/bin/ollama pull gemma4:e2b-it-q4_K_M
   /opt/homebrew/bin/ollama create llb-brain -f /Users/ajad/Documents/ChatGPT/local_voice/LLBBrain.Modelfile
   ```

4. Confirm the created model is named `llb-brain`; preserve the embedding model.
   The first retrieval index is already complete, so do not rebuild it unnecessarily.
5. Update `.brain/setup-status.json` when answering becomes available. The project
   setup note points to that status file.
6. Leave the navigation map and Notes chat visible in Obsidian. The command palette
   command is **LLB Second Brain: Chat: Notes (RAG)**.
7. Report the actual final state. Do not describe the pending model as installed
   or imply that answer accuracy was evaluated.

## Preservation, privacy, and approvals

- The archive already had substantial unrelated uncommitted changes. Preserve them.
  Do not reset, clean, or broadly stage the vault.
- Existing `AGENTS.md`, `.reindex.py`, and study dashboards were preserved byte for byte.
  Only the archive's own generated catalogue/README outputs were refreshed, after backup.
- Automatic approval review rejected the initial broader script that would have
  rewritten those guides, changed Git configuration, and edited global skills.
  A safer vault-scoped installation was approved and completed instead. Do not run
  the original broad proposal or silently expand its scope.
- `configure-llb-vault.py` is a one-time installer. **Do not rerun it** on the now
  configured vault; it exits when `.brain` exists.
- The user edited plugin settings during setup. `data.json` may contain credentials.
  **Never print it, copy its values into a handoff, overwrite it with defaults, or
  include it in Git.** The built-in web-search path remains disabled in this fork.
- `embeddings.json` contains source text and should also stay local. `.brain`
  contains backups. Neither belongs in an indiscriminate `git add .`.
- Do not read private note bodies into a hosted agent's context. Local extraction
  and indexing ran on the Mac; only counts and setup metadata were returned here.
- Archive sources are historical study materials. Do not treat their tax figures,
  monetary thresholds, or procedural rules as current law without current authority.
- No agents were messaged, spawned, or assigned a new chat for this handoff.

