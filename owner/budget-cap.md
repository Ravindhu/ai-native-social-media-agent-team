# Budget cap (Template)

_Owner input. The orchestrator checks every paid action against this file._
OWNER INPUT · human-led · not counted as an agent.

| Channel | Monthly cap | Spent this month | Alert at |
|---|---|---|---|
| Meta ads | 0 | 0 | 80% |
| TikTok ads | 0 | 0 | 80% |
| Boosts (any channel) | 0 | 0 | 80% |

Rules:
- At 80% of a cap, the orchestrator notes it in `logs/results.md`.
- At 100%, the orchestrator holds all new spend and writes to `queue/needs-your-ok.md`.
- Changing a cap is always an owner decision.
