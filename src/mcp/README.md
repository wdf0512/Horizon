# Horizon MCP

Horizon includes a built-in MCP server that exposes the native Horizon pipeline as staged tools and read-only resources.

The MCP layer does not reimplement Horizon business logic. It reuses the existing fetch, score, filter, enrich, and summarize modules from the main codebase.

## Tools

| Tool | Description |
| --- | --- |
| `hz_validate_config` | Validate Horizon config and required environment variables |
| `hz_fetch_items` | Fetch and deduplicate content into the `raw` stage |
| `hz_score_items` | Score items from a stage into `scored` |
| `hz_filter_items` | Filter scored items into `filtered` |
| `hz_enrich_items` | Enrich filtered items into `enriched` |
| `hz_generate_summary` | Generate markdown from a stage |
| `hz_run_pipeline` | Run fetch -> score -> filter -> enrich -> summarize |
| `hz_list_runs` | List recent run artifacts |
| `hz_get_run_meta` | Read metadata for a run |
| `hz_get_run_stage` | Read items from a run stage |
| `hz_get_run_summary` | Read a generated summary |
| `hz_get_metrics` | Read in-memory server metrics |
| `hz_get_briefing` | Top-N curated items on a topic with cache |
| `hz_search_history` | Keyword + date-range search over enriched history |
| `hz_subscribe_topic` | Create or update a topic subscription |
| `hz_list_subscriptions` | List active subscriptions |
| `hz_delete_subscription` | Delete a subscription by id |

## Topic-aware params

`hz_run_pipeline` and `hz_score_items` now accept an optional `topic_keywords: list[str]` parameter. When supplied, scoring prompts include a `Topic relevance` dimension so high-score items skew toward the topic.

## Config packs

Three turnkey vertical bundles ship in `config_packs/`:
- `ai-developers` — LLM/inference engineers
- `livestream-compliance` — 中国直播电商合规
- `overseas-policy` — TikTok/Stripe/FTC cross-border policy

Pass `config_pack="<name>"` to `hz_get_briefing` or `hz_subscribe_topic` to apply.

## Resources

- `horizon://server/info`
- `horizon://metrics`
- `horizon://runs`
- `horizon://runs/{run_id}/meta`
- `horizon://runs/{run_id}/items/{stage}`
- `horizon://runs/{run_id}/summary/{language}`
- `horizon://config/effective`

## Install and Start

```bash
uv sync
uv run horizon-mcp
```

The server runs over stdio and is intended to be launched by an MCP client.

## Run Artifacts

Each run writes artifacts under `data/mcp-runs/<run_id>/`:

- `meta.json`
- `raw_items.json`
- `scored_items.json`
- `filtered_items.json`
- `enriched_items.json`
- `summary-<lang>.md`

## Design Principles

1. Keep Horizon as the single source of business logic.
2. Preserve staged re-entry so a run can continue from intermediate artifacts.
3. Default to no extra side effects unless explicitly requested.

## Client Setup

See [integration.md](integration.md).
