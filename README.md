# AI Native Social Media Agent Team

A Claude Code project that automatically runs the complete social media of a company: one orchestrator, eight departments,
eight interrupt playbooks, a shared Brand OS, and one owner who only approves.

Built by OneGTMLab.

## Open it

```bash
cd ai-native-social-media-agent-team
open board/index.html      # the full system: live view, how it runs, this project
claude                     # start Claude Code in this project
```

Inside Claude Code:

- `/agents` lists the orchestrator and the eight department agents.
- `/search-demand-spikes "glass skin routine +340%"` runs one interrupt playbook.
- Ask "run the orchestrator on today's signals" to walk the pipeline: Collects → Scores → Briefs → Drafts → Schedules → Approves.

## What you fill in

| Part | Status |
|---|---|
| Orchestrator rules (`CLAUDE.md`), agents, slash commands, Brand OS tree | Ready |
| File contents in `brand-os/` and `owner/` | Templates. Write them for your brand |
| Tool connections (Semrush, Brand24, Metricool, HubSpot and the rest) | Not configured. See `TOOLS.md` |

## Choose the LLM backend: Anthropic API or Ollama

The scripted parts of the team (the `llm/` provider layer) can run on either backend:

| Backend | Needs | Set it with |
|---|---|---|
| `anthropic` (default) | `ANTHROPIC_API_KEY` | `"provider": "anthropic"` in `config/llm.json`, or `LLM_PROVIDER=anthropic` |
| `ollama` (local) | `ollama serve` running and a pulled model, e.g. `ollama pull llama3.1` | `"provider": "ollama"`, or `LLM_PROVIDER=ollama` |

Setup:

```bash
cp .env.example .env          # then fill in the values you need
python3 scripts/llm_check.py  # ping the configured backend
python3 scripts/llm_check.py --provider ollama
```

Precedence, first hit wins: the `--provider` flag, then `LLM_PROVIDER`, then `config/llm.json`, then `anthropic`.
Model and host come from `ANTHROPIC_MODEL`, `OLLAMA_MODEL` and `OLLAMA_HOST`, falling back to `config/llm.json`.

Python code uses it like this:

```python
from llm import complete
print(complete("Write one hook for a skincare reel.", system="Follow owner/brand-voice.md"))
```

Note: Claude Code itself (the `claude` CLI and the agents in `.claude/`) always runs on Anthropic. The Ollama option covers the Python layer and any script you add on top of it.
