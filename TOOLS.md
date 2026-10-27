# Tools

Each board tile, what it does in this team, and its connection status. Nothing is connected by default.

| Tile | Used by | What it does here | Status |
|---|---|---|---|
| Google Search Console | Search Visibility | query and page performance | Not configured |
| Semrush | Search Visibility, Market Radar | keyword demand, spikes, rank drops | Not configured |
| GA4 | Search Visibility, Results & ROI | traffic and conversions | Not configured |
| Ahrefs | Search Visibility | backlinks and site health | Not configured |
| Screaming Frog | Search Visibility | technical crawl | Not configured |
| Brand24 | Market Radar, Reviews & Reputation | mentions and competitor promos | Not configured |
| Similarweb | Market Radar | competitor traffic | Not configured |
| Google Alerts | Market Radar | news and topic watch | Not configured |
| Claude | Content Engine, Reviews & Reputation, Creative Studio | drafts and briefs | Ready |
| Surfer | Content Engine | SEO briefs and scoring | Not configured |
| Frase | Content Engine | research | Not configured |
| Grammarly | Content Engine | editing | Not configured |
| Airtable | Content Engine | content calendar | Not configured |
| Canva | Creative Studio | graphics and ad rebuilds | Not configured |
| Midjourney | Creative Studio | images | Not configured |
| Remotion | Creative Studio | programmatic video | Not configured |
| Figma | Creative Studio | layouts | Not configured |
| ElevenLabs | Creative Studio | voiceover | Not configured |
| Metricool | Publishing & Social | scheduling and ad rotation | Not configured |
| WordPress | Publishing & Social | blog publishing | Not configured |
| Google Business Profile | Publishing & Social, Reviews & Reputation | posts and review replies | Not configured |
| Facebook & Instagram | Publishing & Social | posting and Meta boosts | Not configured |
| LinkedIn | Publishing & Social | posting | Not configured |
| TikTok | Publishing & Social | posting and ads | Not configured |
| Podium | Reviews & Reputation | review requests | Not configured |
| NiceJob | Reviews & Reputation | review requests | Not configured |
| Messenger, Instagram, WhatsApp (chat tile) | Leads & Conversations | DMs and chats | Not configured |
| ManyChat | Leads & Conversations | auto-replies at night | Not configured |
| HubSpot | Leads & Conversations | leads and CRM | Not configured |
| Twilio | Leads & Conversations | SMS to the owner | Not configured |
| Calendly | Leads & Conversations | bookings | Not configured |
| Front | Leads & Conversations | shared inbox | Not configured |
| Looker | Results & ROI | dashboards | Not configured |
| BigQuery | Results & ROI | data warehouse | Not configured |
| Metabase | Results & ROI | ad-hoc queries | Not configured |
| Postgres + pgvector | all | long-term memory (planned) | Not configured |

## LLM backends

| Backend | Used for | Connection |
|---|---|---|
| Anthropic API (default) | drafts, briefs, reviews, orchestrator reasoning | `ANTHROPIC_API_KEY` in `.env` |
| Ollama (local) | same tasks, offline or cost-free drafting | `ollama serve` at `OLLAMA_HOST` (default `http://localhost:11434`) |
