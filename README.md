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
