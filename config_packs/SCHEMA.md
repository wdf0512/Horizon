# Config Pack Schema

Config packs are turnkey JSON bundles that extend the base `data/config.json` schema with vertical-specific defaults.

Each pack must contain:

| Field | Type | Required | Notes |
|---|---|:---:|---|
| `name` | string | ✅ | Human-readable name. Shown in UI |
| `description` | string | ✅ | One-line description |
| `topic_keywords` | string[] | ✅ | Default keyword bundle for `hz_get_briefing` |
| `sources` | object | ✅ | Same shape as `data/config.json` sources |
| `filtering.ai_score_threshold` | number | ❌ | Override; default 7.0 |
| `scoring_prompt_addendum` | string | ❌ | Extra instructions appended to `CONTENT_ANALYSIS_USER`. 🚧 Field is reserved; not yet consumed in Phase 1 (only `topic_keywords` and `filtering.ai_score_threshold` are wired). |

Pack file name must match `^[a-z0-9][a-z0-9\-_]*$` (no path separators, no uppercase). Place under `config_packs/<name>.json` with a sibling `<name>.README.md`.
