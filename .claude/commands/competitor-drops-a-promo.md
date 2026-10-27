---
description: Interrupt · Competitor Drops a Promo (Brand24, Claude, Canva)
argument-hint: <competitor and what the promo is>
---

Interrupt from "What Interrupts The Loop": **Competitor Drops a Promo**.

Event: $ARGUMENTS

Send this event to the orchestrator agent first. Nothing publishes on its own.

What the board's card says happens:
1. **Brand24**: flags the promo
2. **Claude**: re-briefs the plan
3. **Canva**: refreshes the creative

A reply to a competitor's promo always goes to `queue/needs-your-ok.md`. Run the voice and budget gates from CLAUDE.md first.
