# Upstream Sync Analysis — 2026-07-28

Investigation of what `upstream/main` (Thysrael/Horizon) has added since the fork's last
sync point, whether it's safe/valuable to pull in, and where it collides with the fork's
own divergence. Read-only investigation: no merge/checkout/reset was run against the
working tree. Conflict claims below are not guesses — they come from
`git merge-tree --write-tree main upstream/main` (git 2.45, non-mutating plumbing that
computes a hypothetical merge without touching HEAD, the index, or the working tree) and
from reading the actual diffs (`git show <sha>`), not commit subject lines.

- Last sync point: fork's `main` contains upstream history up to `7e0ffbb` ("feat: add
  balanced digest filtering (#95)").
- Upstream has since advanced 32 commits to `1e2fdc7` (`git log --oneline 7e0ffbb..upstream/main`).
- Fork's `main` is 52 commits ahead of `upstream/main` with its own feature work
  (`git log --oneline upstream/main..main`).
- `git merge-tree --write-tree main upstream/main` (hypothetical merge, computed
  2026-07-28) exits 1 (conflicts) and reports **real conflicts in exactly 8 files**, all
  captured and resolved-in-analysis below:
  `.github/workflows/daily-summary.yml`, `data/config.github.json`, `src/mcp/service.py`,
  `src/models.py`, `src/orchestrator.py`, `src/scrapers/github.py`,
  `src/scrapers/telegram.py`, `src/storage/manager.py`. Every other touched file
  (`src/ai/analyzer.py`, `src/ai/client.py`, `src/mcp/horizon_adapter.py`,
  `src/mcp/run_store.py`, `src/scrapers/rss.py`, `pyproject.toml`, `uv.lock`, and all
  files upstream touched that the fork never touched) auto-merges cleanly.

## 1. New upstream commits (`7e0ffbb..upstream/main`)

### 1.1 Summary table

| SHA | Commit | What it actually does | Why it matters here | Conflict risk | Verdict |
|---|---|---|---|---|---|
| `18b80c4` | docs: add Japanese README (#100) | New `README_ja.md` only | None | None | Pull (no-op for us) |
| `4b8d635` | fix(webhook): skip platform-specific error code check for generic webhook (#111) | `_check_body_error_code` now only checks the Feishu/DingTalk/Slack error-code pattern matching `self.config.platform`; previously it checked all three patterns regardless of platform, causing false-positive "error" logs when a generic webhook's JSON body happened to contain a field like `code` or `ok` | Fork's own Telegram webhook is configured with `"platform": "generic"` (`data/config.json` webhook block) — this exact false-positive is live risk today | None (fork never touched `src/services/webhook.py`) | **Pull** — direct, applicable bug fix |
| `ac6611c` | feat(ollama): custom base url | Adds `_BASE_URL_ENVS`/`_resolve_base_url`/`_normalize_ollama_base_url` to `OpenAIClient`; wizard now sources provider defaults from `AI_PROVIDER_DEFAULTS` centrally and handles Ollama specially (optional API key) | Fork's active AI provider is `ali`/`deepseek-v4-pro` (`data/config.json`), not Ollama — no immediate use, but zero cost | None (fork's `src/ai/client.py` diff since 7e0ffbb is a single blank line; `src/setup/wizard.py` untouched by fork) | Pull (low priority, free) |
| `91d9dd9` | feat(scrapper): use old reddit | `RedditScraper` now tries `old.reddit.com` HTML scraping first (subreddit listing + comment threads), falling back to the JSON API only if HTML returns nothing | Reddit's JSON API is increasingly rate-limited for unauthenticated scraping; old-Reddit HTML is a meaningfully more reliable path for a source the fork actively uses | None (fork never touched `src/scrapers/reddit.py`) | **Pull** — real reliability win |
| `817971c` | chore(scrapper): seq fetch | Mislabeled "chore" — actually changes `RedditScraper.fetch()` from concurrent (`asyncio.gather`) to sequential per-subreddit/user fetching with per-item try/except | Trades fetch speed for lower risk of Reddit rate-limit blocks; pairs with `91d9dd9` | None | Pull along with `91d9dd9` |
| `2144627` + CI chores (`050426e`,`f80e488`,`e13b4bb`,`16d54c9`,`18598aa`,`04e0843`,`3410b27`,`0735f9d`) | feat(ci)/chore(ci): enable/tune upstream's own CI | Upstream's own GitHub Actions schedule/secrets/timezone tuning for **their** deployment | Fork already fully diverged its own `.github/workflows/daily-summary.yml` and `data/config.github.json` (own cron, own secret names, own AI provider/model, own webhook target) | **Yes — real, see below** | Skip; keep fork's own CI config |
| `ac6611c`…`ed2148e`/`b76d864`/`32d668c`/`f84ec5c`/`838ec68`/`1ffd7be`/`c822780` | chore(doc): badges/logo/blank-line/title-rendering | Cosmetic README changes | None | Low (README likely already customized) | Skip / cherry-pick only if wanted cosmetically |
| `f4fe156` | feat(scrapers): add GDELT and Google News RSS sources (#118) | New key-less `GDELTScraper` (GDELT 2.0 DOC API) and `GoogleNewsScraper` (Google News RSS search), wired opt-in (`enabled: false` by default) into `SourceType`, `SourcesConfig`, `fetch_all_sources`, `_sub_source_label` | Two free, no-API-key news sources directly relevant to a "business/tech opportunity digest" — pure upside, disabled by default so zero behavior change until opted in | Touches `src/orchestrator.py` (`fetch_all_sources`, `_sub_source_label`) and `src/models.py` (new enum members + config classes) — **verified non-overlapping with fork's edits** (fork only touches `run()`/`__init__`, not `fetch_all_sources`) | **Pull** |
| `0414f12` | fix(scrapper): distinguish the reply news comment on telegram | `_parse_message` selector narrowed from `div.tgme_widget_message_text` to `div.tgme_widget_message_text.js-message_text`, so a quoted reply-preview block is no longer captured as the message body | Fork's current `src/scrapers/telegram.py` still uses the old broad selector — confirmed live bug: reply-quoted text gets prepended into scraped Telegram content today | None on its own line, but see `b016dc7` below — same file, needs combined resolution | **Pull** (part of telegram.py resolution) |
| `077c0d2` | fix(scrappers): add new domain alternatives for telegram | `t.me/s` → try `telegram.me/s`, `telegram.dog/s`, `t.me/s` in order; raises instead of silently returning `[]` if all channels fail | Improves resilience against `t.me` blocking/DNS issues for a source the fork relies on | Same file as above, see combined resolution | **Pull** (part of telegram.py resolution) |
| `b016dc7` | fix(scrapers): add missing category field to all source configs (#129) | Adds `category: Optional[str] = None` to `GitHubSourceConfig`, `HackerNewsConfig`, `RedditSubredditConfig`, `RedditUserConfig`, `TelegramChannelConfig`, `TwitterConfig`, `OSSInsightConfig`, and wires it into each scraper's metadata; refactors `github.py`/`telegram.py` internals to pass the whole config object instead of loose params | **Real, confirmed conflict** — fork independently added `category` to `GitHubSourceConfig` and `TelegramChannelConfig` (same field, same position — merges cleanly) but ALSO independently threaded category through `github.py`/`telegram.py` via an added trailing parameter, while upstream threads it by passing the whole `source`/`cfg` object. Both approaches reach the same runtime behavior, but the **code paths conflict line-for-line** | **HIGH — src/scrapers/github.py (7 conflict hunks), src/scrapers/telegram.py (3 conflict hunks)** | **Pull, manual resolution required** — adopt upstream's cleaner object-passing signatures (superset of what fork needed) |
| `3e21c04` | fix(ai): support max_completion_tokens for GPT-5 and o-series models (#126) | `OpenAIClient` detects `o1`/`o3`/`o4`/`gpt-5` model prefixes and switches `max_tokens` → `max_completion_tokens`; also retries on the specific "max_tokens unsupported" error string | Fork uses `ali`/`deepseek-v4-pro`, not GPT-5/o-series — no immediate use | None (fork's `client.py` untouched here) | Pull (free, future-proofing) |
| `9f83af4` | feat(rss): add opt-in full article extraction via pluggable extractors (#130) | New `src/extractors/` package: `BaseExtractor` ABC, `TrafilaturaExtractor` (optional `trafilatura` dep), `ExtractorRegistry`. `RSSSourceConfig.content_extractor` opt-in field; `RSSScraper` falls back to feed content on extraction failure | Genuinely useful for a digest pipeline: RSS feeds that only publish summaries could get full-article text before AI scoring/summarizing — directly improves digest quality. Opt-in, `enabled` nowhere by default, zero behavior change unless configured | Touches `src/models.py` (`RSSSourceConfig`) at the **same line** fork added its own `max_items` field — **1 confirmed conflict**, trivial (adjacent unrelated fields in same model) | **Pull** |
| `c507b7c` | feat(ALL): enhance security | See §1.2 — large multi-file SSRF/redaction/atomic-write/path-traversal hardening pass | Directly relevant: fork's MCP server exposes `get_effective_config` (secret redaction matters), its webhook/extractor code makes outbound requests to source-provided URLs (SSRF matters), and its own file writes benefit from atomicity | Touches `src/models.py`, `src/orchestrator.py`, `src/mcp/service.py`, `src/storage/manager.py`, `src/mcp/horizon_adapter.py` — see conflict detail below | **Pull, mostly clean — see §1.2** |
| `14d2b95` | chore(ALL): refine the code | **Mislabeled — NOT a trivial chore.** See §1.3 — introduces `FetchReport`/`SourceFetchOutcome` (raises if ALL sources fail in one run instead of silently continuing), a shared `orchestrator.filter_items()` pipeline stage (threshold + topic-dedup + balance in one call), tracking-parameter-aware URL dedup keys, `src/_file_utils.py` (dedupes the atomic-write helper introduced by `c507b7c`), and an `AI_PROVIDER_DEFAULTS`-driven fix to `ChainedAIClient` provider-chain base-URL leakage | Two genuinely valuable reliability features for an unattended daily cron pipeline: (1) fail loudly instead of silently producing an empty digest when every source is down, (2) the chained-AI-client base-URL bug fix matters if the fork ever configures `provider_chain` fallback across providers with different base URLs | **Real conflict** — upstream's new `filter_items()` step replaces the exact block the fork customized to exclude `compliance-*` category items from the main digest; also two independent new top-level functions/`__init__` fields landing at the same anchor point in `orchestrator.py`/`mcp/service.py` | **Pull, manual resolution required — highest-value, highest-effort item** |
| `d5e9dcf` | feat(ai): add MiniMax M3 compatible endpoint support (#134) | Updates `MiniMax` default model to `MiniMax-M3`, adds an Anthropic-compatible-endpoint code path (`AnthropicClient` selected when `base_url` ends in `/anthropic`) | Fork doesn't use MiniMax — no immediate use | None (fork's `client.py`/`models.py` diffs don't touch these lines) | Pull (free) |

*(Skipped as pure noise, verified non-interesting: all remaining `chore(ci): change time`,
badge/logo/blank-line doc chores, and `chore(ci)` timezone/secret/version bumps. These
were skimmed via `git show --stat` to confirm no source-code payload.)*

### 1.2 `c507b7c feat(ALL): enhance security` — detail

Real, substantial commit (26 files, +1198/-298). Key changes:

- **New `src/url_security.py`**: `validate_http_url` (rejects non-http(s), embedded
  credentials, localhost), `validate_public_http_url` (resolves the hostname and rejects
  private/loopback/link-local/reserved IPs — SSRF guard), `safe_request` (validates each
  redirect hop, not just the initial URL). Wired into `src/services/webhook.py` (outbound
  webhook POST/GET) and `src/extractors/trafilatura.py` (full-article fetch introduced by
  `9f83af4`).
- **`src/mcp/service.py`**: `_redact_config()` — strips API keys/tokens/passwords/cookies
  (by key-name pattern and by scanning header-like strings and URL query
  params/userinfo) from the JSON blob `get_effective_config` returns. **This directly
  matters to the fork**, which built an extensive MCP tool surface
  (`hz_get_briefing`, `get_effective_config`, etc.) that could otherwise leak
  `DASHSCOPE_API_KEY`/webhook URLs/tokens to any MCP client.
- **`src/storage/manager.py` + `src/mcp/run_store.py`**: atomic writes (`tempfile` +
  `os.replace`) for `config.json`, daily summaries, `subscribers.json`, run artifacts —
  avoids truncated/corrupt files on crash mid-write.
- **`src/orchestrator.py`**: `safe_output_path()` guards the Jekyll blog-post filename
  from path traversal.
- **`src/ai/analyzer.py`**: AI JSON response now validated through a Pydantic
  `AnalysisResult` model (score clamped 0–10, no NaN/Inf, typed fields) instead of blind
  `.get()` calls.
- **`src/ai/summarizer.py`**: escapes Markdown/HTML special characters in
  AI-and-source-derived text (titles, summaries, tags) before embedding in the digest —
  prevents a malicious/malformed source item from breaking Markdown rendering or
  injecting links.
- **`src/mcp/horizon_adapter.py`**: `VALID_SOURCES` becomes `frozenset(SOURCE_REGISTRY)`
  (data-driven from a new `SOURCE_REGISTRY` dict in `models.py`) instead of a hardcoded
  set; `apply_source_filter`/`get_enabled_sources` iterate the registry instead of
  per-source `if` blocks. **Verified via merge-tree: auto-merges cleanly** with the
  fork's own addition of `_CONFIG_PACKS_DIR`/`_CONFIG_PACK_NAME_RE`/`load_config_pack` in
  the same file — git correctly interleaves both without help.
- **`src/search.py` deleted** (unused HN-Algolia/Reddit search helper). Verified: no
  references anywhere in `src/`, `tests/`, or `scripts/` in the fork. Safe.
- **Docker hardening**: non-root user in `Dockerfile`, `.dockerignore` now excludes all of
  `data/` except examples (prevents leaking `data/config.json`/generated summaries into
  build context), `docker-compose.yml` restart policy `unless-stopped` → `"no"`.

Conflict-relevant: this commit's changes to `src/models.py` (new `SOURCE_REGISTRY`,
`AIConfig.validate_languages`), `src/mcp/service.py` (`_redact_config`, `generate_summary`
empty-guard, `run_pipeline` enrich guard, `send_webhook` return-type change to
`WebhookDeliveryResult`), and `src/storage/manager.py` (`safe_output_path` in
`save_daily_summary`) do **not** textually overlap with the fork's own edits to those
methods — confirmed via merge-tree and manual line-range comparison. The one real
conflict in `src/storage/manager.py` (`save_daily_summary`) comes from combining this
commit's `safe_output_path()` call with the fork's own `variant` parameter (used for the
compliance-digest filename `horizon-{date}-compliance-{lang}.md`) — see §4 resolution.

The `WebhookNotifier.notify()` return-type change (`None` → `WebhookDeliveryResult`) is
backward compatible: fork's only two call sites (`src/services/webhook.py`'s own
`send_daily_summary`, `src/mcp/service.py`'s `send_webhook`) both already discard/reuse
the return value in a way that tolerates the richer object.

### 1.3 `14d2b95 chore(ALL): refine the code` — detail

Despite the "chore" label this is the single most consequential commit in the batch for
merge planning (14 files, +962/-202, new file, new tests for cross-source dedup and fetch
reporting):

- **`FetchReport`/`SourceFetchOutcome`** (`src/orchestrator.py`): `fetch_all_sources` no
  longer swallows per-source exceptions via `asyncio.gather(..., return_exceptions=True)`
  and silently continues. Each scraper's outcome (`success`/`empty`/`failure`) is
  recorded; if **every** configured source failed, `run()` now raises
  `RuntimeError(self.last_fetch_report.failure_message())` instead of printing
  "No new content found" and exiting 0. `src/mcp/service.py` gained `_get_fetch_report()`
  to surface this in `fetch_items()`'s response/meta. This is a meaningful reliability
  improvement for an unattended daily GitHub Actions run — today a total outage (e.g. all
  scrapers broken) is indistinguishable from "quiet news day."
- **`orchestrator.filter_items()`**: consolidates score-threshold filtering, optional
  `merge_topic_duplicates`, and `apply_balanced_digest` into one reusable pipeline stage,
  returning a `FilteringPipelineResult`. `src/mcp/service.py`'s own `filter_items` MCP
  method is refactored to delegate to it instead of duplicating the logic inline.
  **This replaces the exact `run()` step-5 block the fork customized** (see conflict
  below).
- **Cross-source URL dedup improved** (`_deduplication_url_key`): strips tracking query
  parameters (`utm_*`, `gclid`, `fbclid`, `msclkid`, `ttclid`, `mc_cid`, etc.) and
  normalizes scheme/default-port/credentials before comparing URLs, and now deep-copies
  items before merging (previously could mutate shared list items). Directly improves
  digest quality (fewer near-duplicate items slipping through with different tracking
  params).
- **`src/_file_utils.py`** (new): the `_atomic_write_text` helper `c507b7c` had just
  duplicated into both `storage/manager.py` and `mcp/run_store.py` is consolidated into
  one shared module. Pure DRY cleanup, no behavior change.
- **`AI_PROVIDER_DEFAULTS`-driven `ChainedAIClient` fix** (`src/ai/client.py`): fixes a
  real bug where `_create_chained_client` copied the *primary* provider's `base_url` to
  *every* provider in a `provider_chain` fallback list, and dropped
  `throttle_sec`/`analysis_concurrency`/`enrichment_concurrency`/Azure fields for chained
  configs. Now each chained provider gets its own correct default `base_url` unless it is
  the primary configured provider.

**Real, confirmed conflicts** (from merge-tree):
1. `src/orchestrator.py` `__init__`: fork's `self.extra_notifiers = [...]` (extra-webhook
   list for the compliance channel) vs. upstream's `self.last_fetch_report: Optional[FetchReport] = None`
   — two independent new `__init__` fields inserted at the same point. Trivial: keep both.
2. `src/orchestrator.py` `run()` step 5: fork's inline filter
   (`important_items = [item for item in analyzed_items if item.ai_score and item.ai_score >= threshold and not (item.metadata.get("category") or "").startswith("compliance-")]`)
   vs. upstream's `filtering_result = await self.filter_items(analyzed_items, apply_balance=False)`.
   **This is the one place a pure "take theirs" resolution silently drops fork behavior**:
   upstream's `filter_items()` has no concept of excluding `compliance-*` items from the
   main digest (those are routed to the fork's own compliance channel/digest in
   steps 7.5/7.6/8 later in the same method). Resolution needs to exclude
   `compliance-*`-category items from the list **before** calling the new
   `filter_items()`, e.g.:
   ```python
   non_compliance_items = [
       item for item in analyzed_items
       if not (item.metadata.get("category") or "").startswith("compliance-")
   ]
   filtering_result = await self.filter_items(non_compliance_items, apply_balance=False)
   important_items = filtering_result.items
   ```
3. `src/mcp/service.py`: fork's new `_topic_to_keywords()` helper vs. upstream's new
   `_get_fetch_report()` helper — both inserted immediately after `_default_runs_root()`.
   Trivial: keep both functions.
4. `src/models.py`: fork's `RSSSourceConfig.max_items` vs. upstream's
   `RSSSourceConfig.content_extractor` (from `9f83af4`) — both added at the same line.
   Trivial: keep both fields.

## 2. Branch notes

- **`upstream/copilot/fix-deploy-github-actions-job`** — confirmed safe to ignore. It
  branches from `7e0ffbb` (the *old* sync point, i.e. it predates most of the 32 commits
  above) and adds exactly one commit, `c0ac1a3 "Initial plan"`, which is an empty
  GitHub-Copilot-coding-agent bootstrap commit with **zero file changes**
  (`git show c0ac1a3 --stat` returns nothing). This is an abandoned/never-started Copilot
  agent task, not a real feature branch. No action needed.
- **`upstream/gh-pages`** (`0c27d38..2c53c0e`) — the generated Jekyll site: daily
  `_posts/YYYY-MM-DD-summary-{en,zh}.md` auto-published digests plus mirrored doc pages
  (`configuration.md`, `extractors.md`, `scrapers.md`). Pure build output, not source.
  Confirmed low priority / informational only — no merge action applicable (this fork
  publishes its own blog via a different mechanism per §3).

## 3. Fork's own divergence (context)

`git log --oneline upstream/main..main` — 52 commits. For context only (already
well-understood by the team, not re-litigated here):

- Full MCP server layer (`src/mcp/*`): `hz_get_briefing`, `hz_subscribe_topic`,
  `hz_list_subscriptions`, `hz_delete_subscription`, `hz_search_history`,
  `BriefingCache` (LRU+TTL), `SubscriptionStore`, `config_packs/*`
  (`ai-developers`, `livestream-compliance`, `overseas-policy`), `topic_keywords`
  threaded through `ContentAnalyzer`/`score_items`/`run_pipeline`.
- Compliance monitoring + dependency-risk/ecosystem-signal scoring tracks
  (`src/ai/prompts.py` category-specific prompt sets, `src/orchestrator.py` steps
  7.5/7.6/8 building a separate compliance digest and firing extra category-filtered
  webhooks via `Config.webhooks`/`WebhookConfig.category_filter`).
- Distribution integrations: Obsidian vault sync (`scripts/to_obsidian_vault.py`), Notion
  push (`scripts/to_notion.py`), personal blog auto-publish
  (`scripts/to_blog_post.py`), bilingual zh+en digest.
- Own scraper: `src/scrapers/jinritemai.py` (not present upstream at all, zero overlap).
- Separate local branch `feat/daily-brief-cover` (7 commits, not on `main`): "daily ink
  cover" image generation (`generate_daily_cover.py`, palette/seed logic, `pillow`
  dependency, CI step to checkout the blog repo + copy fonts, backfill script).
- Own AI provider/model choice (`ali`/`deepseek-v4-pro` per `data/config.json`) and own
  CI/secrets layout in `.github/workflows/daily-summary.yml` +
  `data/config.github.json`.

## 4. Recommendation

**Do not run a blind `git merge upstream/main`.** It will stop on 8 conflicted files,
2 of which (`src/orchestrator.py` step-5 filtering, and the `github.py`/`telegram.py`
category-threading refactor) need actual judgment, not just "accept theirs." But nothing
found is a reason to skip the sync — every conflict has a clean, understood resolution,
and the payload is worth it (Reddit reliability, telegram reliability/bugfix, SSRF/secret-redaction
hardening for the fork's own MCP surface, fail-loud fetch reporting, free GDELT/Google
News sources, free extractor pluggability).

**Recommended approach: real merge, not cherry-pick.** The conflicts are concentrated and
already mapped; cherry-picking 16 non-trivial commits individually would hit the same
conflicts repeatedly (e.g. `b016dc7`/`0414f12`/`077c0d2` all touch
`src/scrapers/telegram.py`) with less context than doing it once. Steps:

1. `git merge --no-commit --no-ff upstream/main` (or an equivalent worktree) to stage the
   hypothetical merge without auto-committing.
2. Resolve the 8 conflicted files in this order (lowest to highest effort):
   - `src/models.py` — keep both sides (`max_items` + `content_extractor` on
     `RSSSourceConfig`; everything else auto-merges).
   - `src/mcp/service.py` — keep both new functions (`_topic_to_keywords` +
     `_get_fetch_report`) side by side after `_default_runs_root()`.
   - `src/storage/manager.py` — combine: keep the fork's `variant` parameter on
     `save_daily_summary`, wrap the final path in upstream's `safe_output_path()`.
   - `src/scrapers/github.py` and `src/scrapers/telegram.py` — adopt upstream's
     object-passing signatures (`source: GitHubSourceConfig`, `cfg: TelegramChannelConfig`)
     wholesale; they already expose `.category` and are a strict superset of what the
     fork's parallel-parameter approach achieved. This also pulls in `91d9dd9`/`817971c`
     (reddit — no conflict there) and `077c0d2`/`0414f12` (telegram domain
     fallback/reply-fix) for free once the signatures reconcile.
   - `src/orchestrator.py` — keep both new `__init__` fields
     (`self.extra_notifiers` + `self.last_fetch_report`); rewrite step 5 to exclude
     `compliance-*` items *before* calling the new `filter_items()` (see §1.3 snippet).
     Read through steps 7.5/7.6/8 afterward to confirm they still reference
     `analyzed_items` (unfiltered) rather than the now-restructured `important_items`, so
     the compliance digest is unaffected.
   - `.github/workflows/daily-summary.yml`, `data/config.github.json` — keep the fork's
     versions outright (`git checkout --ours <file>` semantics); these are CI reference
     configs, upstream's values are their own deployment's, not a source-of-truth to
     reconcile against. Optionally hand-copy over any *new* section shapes (e.g. `gdelt`/
     `google_news` stanzas) if choosing to enable those sources later.
3. Run the test suite (`uv run pytest`) after resolution — the incoming commits bring
   ~30 new/changed test files (`test_url_security.py`, `test_fetch_reporting.py`,
   `test_cross_source_duplicates.py`, `test_category_wiring.py`, `test_extractors_*`,
   `test_minimax_client.py`, etc.) that will directly validate the merged
   `github.py`/`telegram.py`/`orchestrator.py`/`storage/manager.py` resolutions.
4. Manually smoke-test the compliance-digest path (`run()` steps 7.5–8) and one MCP call
   (`get_effective_config`, to confirm secret redaction didn't regress) since these are
   the two areas where automatic tests won't catch a wrong hand-merge as directly as the
   scraper-signature conflicts will.
5. Skip pulling: all `chore(ci)`/badge/logo/blank-line commits, and the two CI-config
   files' upstream sides (already covered in step 2).
6. No action needed on `upstream/copilot/fix-deploy-github-actions-job` (abandoned,
   empty) or `upstream/gh-pages` (generated site).

**Two highest-risk spots to double-check personally after any AI-assisted merge**:
`src/orchestrator.py` step 5 (compliance-item exclusion must survive the `filter_items()`
refactor — a silent regression here would leak compliance items into the main digest with
no test failure, since the fork's own compliance tests likely test the compliance-digest
build in steps 7.5/7.6, not step 5's exclusion), and the `github.py`/`telegram.py`
signature reconciliation (must confirm every call site was updated consistently — a
partial hand-merge could leave a stale `self._parse_message(msg, cfg.channel, since, cfg.category)`
call site next to a signature expecting `cfg`).
