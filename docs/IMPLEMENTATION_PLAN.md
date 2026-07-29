# Horizon MCP · Implementation Plan

> Companion to [`COMMERCIAL_SPEC.md`](./COMMERCIAL_SPEC.md). Breaks the 14-day sprint into ~80 sub-tasks of 15-90 minutes each, with file paths, acceptance gates, and dependencies.
> Mirrored in Obsidian: `side-hustles/Project-G-Horizon情报引擎/05 - MCP 商业化实现 plan.md`.
> Use this as your daily working document — check off boxes as you go.

**Sprint length**: 14 days · **Total est. effort**: ~55 hours · **Owner**: Defang

---

## Conventions

| Field | Meaning |
|---|---|
| **ID** | `D{day}-{seq}` e.g. `D1-3`. Stable across rewrites. |
| **Min** | Estimated minutes (calendar time, not focus time) |
| **Files** | Repo-relative paths, `(new)` = create, `(mod)` = modify |
| **Gate** | Acceptance criterion before marking done |
| **Dep** | Blocking prereqs (sub-task IDs) |

Status icons in section headers: 🟢 done · 🟡 in progress · ⚪️ pending · 🔴 blocked.

---

## Day 0 — Pre-sprint Prep ⚪️

Block ~1 hour before Day 1 to reduce friction during the sprint.

| ID | Min | Task | Files | Gate |
|---|---|---|---|---|
| D0-1 | 5 | Create branch `feat/commercial-sprint` | git | `git status` clean on new branch |
| D0-2 | 15 | Verify dev env: `uv sync`, `uv run python scripts/check_mcp.py` | — | smoke check passes |
| D0-3 | 10 | Baseline test pass `uv run pytest` | — | all existing tests green |
| D0-4 | 20 | Re-read COMMERCIAL_SPEC.md end-to-end, note any deltas | docs/COMMERCIAL_SPEC.md | mental model fresh |
| D0-5 | 10 | Set up daily journal in Obsidian: `side-hustles/Project-G-Horizon情报引擎/sprint-log.md` | Obsidian | journal seeded with Day 1 heading |
| D0-6 | 5 | Block calendar slots for the 14 days | calendar | sessions scheduled |

---

## Day 1 — `hz_get_briefing` MVP ⚪️

**Goal**: Ship a working one-call briefing tool that wraps existing pipeline. No cache yet, no topic_keywords yet (those land in Day 2 and Day 4).

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D1-1 | 15 | Re-read `service.run_pipeline` and `service.filter_items` line by line | src/mcp/service.py | understand current params + return shape | — |
| D1-2 | 20 | Add `get_briefing` method **stub** (signature + docstring + `raise NotImplementedError`) | src/mcp/service.py (mod) | mypy/ruff clean | D1-1 |
| D1-3 | 45 | Implement body: build context, call `fetch → score → filter → enrich → summarize`, return top-N by score | src/mcp/service.py (mod) | returns valid dict for one topic | D1-2 |
| D1-4 | 20 | Add `_topic_to_keywords(topic: str) -> list[str]` helper (simple lowercase split + stopword filter for now) | src/mcp/service.py (mod) | unit-testable pure function | D1-3 |
| D1-5 | 20 | Register `@mcp.tool() async def hz_get_briefing(...)` in server.py | src/mcp/server.py (mod) | tool appears in `hz_get_metrics` after one call | D1-3 |
| D1-6 | 45 | Write 3 unit tests: happy path, validation error (bad language), small min_score returns more items | tests/mcp/test_get_briefing.py (new) | tests green | D1-5 |
| D1-7 | 15 | Run smoke + new tests | scripts/check_mcp.py | all green | D1-6 |
| D1-8 | 30 | Manual test from Claude Desktop: ask "give me today's AI inference briefing" | — | Claude returns 5 ranked items with summaries | D1-7 |

**Day 1 Gate**: `hz_get_briefing(topic="LLM inference", hours=24, count=5)` returns 5 valid items end-to-end from Claude Desktop.

---

## Day 2 — Briefing Cache Layer ⚪️

**Goal**: Add in-memory LRU cache so duplicate calls within TTL return instantly. Sets up for Day 9 Postgres migration.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D2-1 | 10 | Define cache key shape: `(tenant_id, topic_normalized, language, hours_bucket, min_score, config_pack)` | docs/cache-design.md (new) | written rationale | — |
| D2-2 | 40 | Implement `BriefingCache` (LRU 256 entries, configurable TTL default 3600s) | src/mcp/cache.py (new) | unit-tested in isolation | D2-1 |
| D2-3 | 25 | Wire cache into `service.get_briefing`: lookup before pipeline, store after | src/mcp/service.py (mod) | second identical call returns `cached=true` | D2-2 |
| D2-4 | 15 | Add `force_refresh: bool = False` param + `cached: bool`, `cached_until: str` in response | src/mcp/service.py, server.py (mod) | param respected | D2-3 |
| D2-5 | 40 | Tests: cache hit, miss, force_refresh bypass, TTL expiry (with frozen time) | tests/mcp/test_cache.py (new) | 4 tests green | D2-2 |
| D2-6 | 15 | Update src/mcp/README.md tool table to mention caching behavior | src/mcp/README.md (mod) | doc updated | D2-3 |

**Day 2 Gate**: Two identical calls in <1h → second has `cached=true` and returns in <50ms.

---

## Day 3 — `hz_search_history` MVP ⚪️

**Goal**: Let users search past runs by keyword + date range. File-based for now; rewrites cleanly to Postgres on Day 9.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D3-1 | 15 | Survey `RunStore.list_runs` and `get_run_stage` APIs | src/mcp/run_store.py | know how to iterate items | — |
| D3-2 | 45 | Implement `service.search_history(query, days, top_k, min_score)`: iterate stage='enriched' items in window, ILIKE-match title/summary, sort by score desc, return top_k | src/mcp/service.py (mod) | function works on local fixture | D3-1 |
| D3-3 | 20 | Register `hz_search_history` tool | src/mcp/server.py (mod) | callable from Claude Desktop | D3-2 |
| D3-4 | 40 | Tests: seed 3 days of fake runs in fixture, search "claude" returns expected items | tests/mcp/test_search_history.py (new) | tests green | D3-3 |
| D3-5 | 10 | Doc update | src/mcp/README.md (mod) | — | D3-3 |

**Day 3 Gate**: With at least 3 days of accumulated history, `hz_search_history(query="claude", days=7)` returns relevant items.

---

## Day 4 — `topic_keywords` Integration ⚪️

**Goal**: Generalize topic awareness so the existing pipeline (and `hz_run_pipeline`) accepts `topic_keywords`. Add a `<topic_relevance>` axis to scoring prompts when supplied.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D4-1 | 30 | Trace scoring prompt construction; find injection point | src/ai/ (probably src/ai/scoring.py or similar) | know exact file + function | — |
| D4-2 | 45 | Add `topic_relevance` dimension to prompt template — **only injected when `topic_keywords` is non-empty** | src/ai/scoring.py (mod) | unit test verifies prompt content | D4-1 |
| D4-3 | 30 | Add `topic_keywords: list[str] \| None = None` to `service.filter_items` and `service.run_pipeline` | src/mcp/service.py (mod) | mypy clean | D4-1 |
| D4-4 | 20 | Forward param through `hz_run_pipeline` tool | src/mcp/server.py (mod) | — | D4-3 |
| D4-5 | 30 | Backwards-compat test: omit `topic_keywords`, behavior identical to before | tests/mcp/test_backcompat.py (mod or new) | green | D4-3 |
| D4-6 | 30 | A/B smoke: same source set with vs without `topic_keywords=["llm","inference"]`, eyeball that top items shift | manual | top-5 contains ≥3 LLM-topic items vs baseline | D4-2 |
| D4-7 | 15 | Refactor `get_briefing` to use the new `topic_keywords` path instead of post-hoc filter | src/mcp/service.py (mod) | Day 1 tests still green | D4-3 |

**Day 4 Gate**: A/B test confirms topic relevance steers the ranking.

---

## Day 5 — `hz_subscribe_topic` MVP ⚪️

**Goal**: Users can register topic subscriptions with a cron schedule and target channels. File-based storage; Day 10 moves to Postgres; scheduler worker is stubbed until Day 8 deployment.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D5-1 | 15 | Define `Subscription` schema (id, topic, schedule, channels, config_pack, active, last_run_at, created_at) | src/mcp/models.py (mod, or new file) | dataclass / pydantic model | — |
| D5-2 | 40 | Implement file-based store at `data/subscriptions.json` (CRUD: create, list, update, delete) | src/mcp/subscriptions_store.py (new) | unit tests for CRUD | D5-1 |
| D5-3 | 25 | Implement `service.subscribe_topic` + `service.list_subscriptions` + `service.delete_subscription` | src/mcp/service.py (mod) | — | D5-2 |
| D5-4 | 30 | Register 3 tools: `hz_subscribe_topic`, `hz_list_subscriptions`, `hz_delete_subscription` | src/mcp/server.py (mod) | callable from Claude Desktop | D5-3 |
| D5-5 | 30 | Tests: create (idempotent by topic), list, update schedule, delete | tests/mcp/test_subscriptions.py (new) | green | D5-2 |
| D5-6 | 15 | Sample `data/subscriptions.json.example` + doc | docs (mod) | — | D5-3 |

**Day 5 Gate**: Round-trip subscribe → list → delete works via MCP tool.

---

## Day 6 — Three Vertical Config Packs ⚪️

**Goal**: Ship 3 turnkey config packs (the "configuration knowledge" Project G-03 calls out as a hidden asset).

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D6-1 | 30 | Create `config_packs/` directory + write `config_packs/SCHEMA.md` (extends data/config.json + adds name, description, topic_keywords, scoring_prompt_addendum) | config_packs/SCHEMA.md (new) | schema documented | — |
| D6-2 | 45 | Build `ai-developers.json` + README: sources = HN, karpathy GitHub, vLLM/sglang releases, r/LocalLLaMA, Simon Willison, Anthropic blog | config_packs/ai-developers.{json,README.md} (new) | runs cleanly | D6-1 |
| D6-3 | 60 | Build `livestream-compliance.json` + README: sources from Project F (抖音学习中心 RSS, SAMR, 监管 Telegram channels) | config_packs/livestream-compliance.{json,README.md} (new) | runs cleanly | D6-1 |
| D6-4 | 45 | Build `overseas-policy.json` + README: TikTok blog, FTC, Shopify, Stripe policy RSS | config_packs/overseas-policy.{json,README.md} (new) | runs cleanly | D6-1 |
| D6-5 | 30 | Implement `horizon_adapter.load_config_pack(name)` + merge into existing config | src/mcp/horizon_adapter.py (mod) | unit-tested merge | D6-1 |
| D6-6 | 25 | Wire `config_pack` param in `hz_get_briefing` + `hz_subscribe_topic` | src/mcp/server.py (mod) | smoke test all 3 packs | D6-5 |
| D6-7 | 20 | Smoke test: `hz_get_briefing(topic="default", config_pack="ai-developers")` → ≥3 quality items | manual | passes | D6-6 |

**Day 6 Gate**: All 3 packs produce ≥3 high-score items in a real run.

---

## Day 7 — Week 1 Closeout & Public Update ⚪️

**Goal**: Stabilize Week 1, publish first build-in-public update, tag a milestone. Don't skip the public post — it's the flywheel.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D7-1 | 30 | Run full `uv run pytest`, fix any lints (`ruff check`, `mypy`) | — | green | — |
| D7-2 | 30 | Update `src/mcp/README.md` tool table with all new tools (sorted) | src/mcp/README.md (mod) | doc reflects reality | D7-1 |
| D7-3 | 60 | Record a 1-minute demo (gif or mp4) of Claude Desktop calling `hz_get_briefing` with `ai-developers` pack | docs/assets/demo-briefing.gif (new) | playable | D7-2 |
| D7-4 | 40 | Draft Twitter long thread (8 tweets) + 小红书 carousel (5 cards): "Week 1 of building Horizon MCP" | drafts in Obsidian sprint-log.md | published | D7-3 |
| D7-5 | 20 | Tag `v0.1.0-mcp-week1` on GitHub (annotated tag with summary) | git | tag pushed | D7-1 |
| D7-6 | 15 | EOD: write retro in `sprint-log.md` — what worked, what slipped | Obsidian | journal entry | — |

**Day 7 Gate**: Public post live, demo gif viewable, all Week 1 tests green on `main`.

---

## Day 8 — HTTP Transport + Fly.io Deploy ⚪️

**Goal**: Move from stdio to streamable HTTP, get a public URL.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D8-1 | 30 | Read FastMCP streamable-http docs + minimal example | — | know transport API | — |
| D8-2 | 40 | Create `src/mcp/server_http.py` reusing `mcp` instance from `server.py` | src/mcp/server_http.py (new) | local run on :8080 responds | D8-1 |
| D8-3 | 20 | Add `[project.scripts] horizon-mcp-http = "src.mcp.server_http:main"` | pyproject.toml (mod) | `uv run horizon-mcp-http` works | D8-2 |
| D8-4 | 30 | Update `Dockerfile` to default to HTTP entry; expose 8080; add `/healthz` route | Dockerfile (mod), src/mcp/server_http.py (mod) | docker-compose up works | D8-3 |
| D8-5 | 30 | Local test: `curl localhost:8080/healthz` 200, then invoke a tool via MCP HTTP from Claude Desktop pointed at local URL | — | tool call works over HTTP | D8-4 |
| D8-6 | 45 | `fly launch` + first deploy. Use `fly.toml` from spec §5.2 | fly.toml (new) | app deployed | D8-4 |
| D8-7 | 15 | Configure Fly secrets: `fly secrets set QWEN_API_KEY=...` etc. | Fly dashboard | secrets set | D8-6 |
| D8-8 | 15 | External smoke test from another machine: `curl https://horizon-mcp.fly.dev/healthz` | — | 200 | D8-6 |

**Day 8 Gate**: Public URL responds, Claude Desktop can connect via HTTP.

---

## Day 9 — Postgres Migration ⚪️

**Goal**: Move state from filesystem to Supabase Postgres for multi-tenant + durability. Keep file backend as a fallback.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D9-1 | 45 | Create Supabase project, run SQL migrations from spec §6.1 (5 tables + indexes) | Supabase dashboard | tables visible | — |
| D9-2 | 60 | Create `src/storage/postgres.py` implementing same interface as `RunStore` (list_runs, get_run_meta, save_stage, get_run_stage, etc.) | src/storage/postgres.py (new) | unit tests on test DB green | D9-1 |
| D9-3 | 25 | Add `STORAGE_BACKEND` env switch (`file`|`postgres`) + factory in service init | src/mcp/service.py (mod), src/storage/__init__.py (new) | switch works | D9-2 |
| D9-4 | 45 | Migration script: `scripts/migrate_runs_to_postgres.py` — import `data/mcp-runs/*` into Postgres | scripts/migrate_runs_to_postgres.py (new) | dry-run + real run | D9-2 |
| D9-5 | 45 | E2E test on Fly with `STORAGE_BACKEND=postgres`: full pipeline run writes correctly | — | rows visible in Supabase | D9-3 |
| D9-6 | 30 | Migrate `BriefingCache` (Day 2) and `subscriptions_store` (Day 5) to Postgres tables | src/mcp/cache.py (mod), src/mcp/subscriptions_store.py (mod) | tests still green | D9-3 |
| D9-7 | 20 | Update `integration.md` with backend choice + secrets | src/mcp/integration.md (mod) | doc updated | D9-3 |

**Day 9 Gate**: Cloud version runs entirely on Postgres; data persists across redeploys.

---

## Day 10 — Auth + Quota ⚪️

**Goal**: API-key gate, plan-based quota, basic user routes.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D10-1 | 20 | Create `src/mcp/middleware/__init__.py` + module structure | src/mcp/middleware/ (new) | importable | — |
| D10-2 | 45 | Implement `auth_middleware`: extract Bearer, look up `tenants` row by `api_key`, attach to request state | src/mcp/middleware/auth.py (new) | 401 paths work | D10-1, D9-1 |
| D10-3 | 45 | Implement `quota_middleware`: check `quota_used < quota_limit`, increment on success | src/mcp/middleware/quota.py (new) | 429 path works | D10-2 |
| D10-4 | 30 | Wire middlewares into `server_http.py` | src/mcp/server_http.py (mod) | unauthed request → 401 | D10-3 |
| D10-5 | 45 | `src/api/auth.py`: `POST /auth/register` with email → returns `sk_horizon_xxx` (random 32 hex + prefix) | src/api/auth.py (new) | registration works | D10-2 |
| D10-6 | 30 | `src/api/me.py`: `GET /me` returns plan + quota usage + reset date | src/api/me.py (new) | endpoint works with valid key | D10-2 |
| D10-7 | 30 | Tests: 401 no key, 401 bad key, 429 over quota, success path increments | tests/api/test_auth_quota.py (new) | 4 tests green | D10-3 |
| D10-8 | 20 | Deploy to Fly, smoke test from external client | — | works in production | D10-4 |

**Day 10 Gate**: External MCP client with valid `sk_horizon_xxx` works; invalid key → 401; over-quota → 429.

---

## Day 11 — Stripe + WeChat Pay ⚪️

**Goal**: Real money flowing for both USD and CNY users.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D11-1 | 30 | Stripe dashboard: create products `horizon-pro-monthly` ($19), `horizon-team-monthly` ($99) | Stripe dashboard | price IDs in hand | — |
| D11-2 | 45 | `src/api/billing/stripe.py`: Checkout session creation (`POST /billing/stripe/checkout`) | src/api/billing/stripe.py (new) | returns Stripe URL | D11-1 |
| D11-3 | 45 | Stripe webhook handler `/webhook/stripe`: handle `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted` → update tenant.plan + quota_limit | src/api/billing/stripe.py (mod) | test-mode event updates DB | D11-2 |
| D11-4 | 45 | WeChat Pay sandbox via pingxx or z-pay: account setup | external | sandbox keys obtained | — |
| D11-5 | 60 | `src/api/billing/wechatpay.py`: equivalent interface (checkout + webhook) | src/api/billing/wechatpay.py (new) | sandbox flow works | D11-4 |
| D11-6 | 30 | E2E: Stripe test card → tenant.plan = pro, quota_limit = 500 | — | Postgres row updated | D11-3 |
| D11-7 | 30 | E2E: WeChat sandbox → tenant.plan = pro | — | Postgres row updated | D11-5 |
| D11-8 | 15 | Set webhook secrets on Fly + lock down endpoints | Fly secrets | secured | D11-3 |

**Day 11 Gate**: Both rails: test transaction completes → tenant upgraded automatically.

---

## Day 12 — Landing Page ⚪️

**Goal**: Public marketing surface; Lighthouse perf ≥ 90; 3-click checkout from home.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D12-1 | 30 | Plan layout: hero / value prop / pricing / config packs / demo / FAQ / signup | docs/commercial/_layout.md (new) | wireframe sketched | — |
| D12-2 | 60 | Build hero + pricing table (USD + CNY toggle) | docs/commercial/index.md (new) | renders | D12-1 |
| D12-3 | 45 | Config pack showcase (3 cards with sample item) | docs/commercial/packs.md (new) | renders | D12-2 |
| D12-4 | 30 | Embed demo gif from Day 7 + signup CTA → Stripe/WeChat checkout | docs/commercial/index.md (mod) | CTA works | D11-2 |
| D12-5 | 30 | FAQ (8 questions: pricing, BYO key, data privacy, self-host, refund, etc.) | docs/commercial/faq.md (new) | renders | D12-1 |
| D12-6 | 30 | GitHub Pages config + custom domain (optional: `horizon-mcp.com` if available) | _config.yml (mod) | live URL | D12-5 |
| D12-7 | 15 | Lighthouse audit, fix low-hanging perf hits | — | Lighthouse Perf ≥ 90 | D12-6 |
| D12-8 | 15 | 3-click checkout smoke: home → pricing → Stripe Checkout | — | path works | D12-7 |

**Day 12 Gate**: Live URL, Lighthouse ≥ 90, paid checkout reachable in 3 clicks.

---

## Day 13 — Distribution Submissions ⚪️

**Goal**: Prepare all launch materials in one batch; do not post yet (Day 14).

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D13-1 | 45 | Draft PR description for `modelcontextprotocol/servers` (title + summary + screenshots) | drafts | reviewed | — |
| D13-2 | 30 | Open the PR (status: draft until Day 14 morning) | GitHub | PR link in hand | D13-1 |
| D13-3 | 45 | Smithery submission form: fill out, attach assets | Smithery | submission link | D13-2 |
| D13-4 | 30 | mcp.run submission form | mcp.run | submission link | D13-2 |
| D13-5 | 45 | Draft HN Show HN post (title + body) — keep in drafts | drafts | reviewed | D13-2 |
| D13-6 | 30 | Draft 小红书 5-card carousel (visuals + copy) | drafts | reviewed | D13-2 |
| D13-7 | 30 | Draft Twitter long thread (10-12 tweets) | drafts | reviewed | D13-2 |
| D13-8 | 45 | Draft 公众号 2000-char article — "我把 400 star 开源新闻雷达包装成付费 MCP" | drafts | reviewed | D13-2 |
| D13-9 | 30 | Draft 即刻 + Reddit posts (r/ClaudeAI, r/LocalLLaMA) | drafts | reviewed | D13-2 |

**Day 13 Gate**: All launch materials drafted and reviewed.

---

## Day 14 — Launch ⚪️

**Goal**: Coordinated multi-channel launch; first real signup.

| ID | Min | Task | Files | Gate | Dep |
|---|---|---|---|---|---|
| D14-1 | 15 | Pre-flight: production status check, Stripe live mode, all endpoints green, secrets verified | — | all green | — |
| D14-2 | 10 | Convert PR to ready-for-review on `modelcontextprotocol/servers` | GitHub | PR open | D14-1 |
| D14-3 | 15 | Post Twitter long thread (English) | Twitter | live | D14-1 |
| D14-4 | 15 | Post 小红书 carousel | 小红书 | live | D14-1 |
| D14-5 | 15 | Post 公众号 article | 公众号 | live | D14-1 |
| D14-6 | 15 | Post HN Show HN | HN | live | D14-1 |
| D14-7 | 15 | Post 即刻 + Reddit | 即刻, Reddit | live | D14-1 |
| D14-8 | 240 | Active monitoring (4-hour block): respond to comments, fix hotfix bugs, capture leads | — | continuous | D14-3..7 |
| D14-9 | 30 | EOD recap: first signup, top issues found, retro notes; close out Day 14 | sprint-log.md | journal entry | — |

**Day 14 Gate**: ≥1 real signup (friend OK); all channels posted; no production fires.

---

## Cross-Cutting Practices

### Testing Strategy
- Unit tests: every new service method gets at least 3 tests (happy / boundary / error)
- Integration tests: from Day 8 onward, run against live Fly instance in CI
- Manual smoke: each Day's Gate includes at least one manual verification

### Documentation Discipline
- Every new tool → update `src/mcp/README.md` table same-day
- Every new env var → update `src/mcp/integration.md` same-day
- Sprint log: append daily entries to Obsidian `sprint-log.md`

### Daily Standup Template (5-min self-check)
```
Day N (date)
- [ ] Yesterday's Gate verified
- [ ] Today's focus: D{N}-1 .. D{N}-X
- [ ] Blockers: (none|...)
- [ ] If slipping >30%: cut scope, don't extend day
```

### Hotfix Policy
- If production breaks during Day 8-14, fix immediately (treat as P0)
- Document in `sprint-log.md` under day section
- After fix: write a 1-line postmortem

---

## At-a-glance Burndown

| Day | Hours | Cumulative | Theme |
|---:|---:|---:|---|
| 0 | 1.0 | 1.0 | prep |
| 1 | 3.5 | 4.5 | get_briefing |
| 2 | 2.5 | 7.0 | cache |
| 3 | 2.0 | 9.0 | search_history |
| 4 | 3.0 | 12.0 | topic_keywords |
| 5 | 2.5 | 14.5 | subscribe_topic |
| 6 | 4.5 | 19.0 | config packs |
| 7 | 3.0 | 22.0 | week 1 closeout |
| 8 | 3.5 | 25.5 | HTTP + Fly |
| 9 | 4.5 | 30.0 | Postgres |
| 10 | 4.5 | 34.5 | auth + quota |
| 11 | 5.0 | 39.5 | billing |
| 12 | 4.0 | 43.5 | landing page |
| 13 | 5.0 | 48.5 | distribution prep |
| 14 | 5.0 | 53.5 | launch |

**Total: ~54 hours.** Weekend-heavy: Days 6, 11, 13 are the longest. Schedule those on actual weekends if possible.

---

## If Slipping — Cut List (Priority Order)

Cut from bottom up. Do not cut Week 1 essentials.

| Cut # | Item | Impact |
|---|---|---|
| 1 | WeChat Pay (D11-4, D11-5, D11-7) | Domestic users wait 1 week; Stripe alone is enough for launch |
| 2 | Smithery + mcp.run (D13-3, D13-4) | Submit Day 16 instead |
| 3 | Landing page FAQ section (D12-5) | Add Day 16 |
| 4 | 公众号 article (D13-8, D14-5) | Skip; 小红书 covers 中文 |
| 5 | Postgres migration script (D9-4) | Start fresh on cloud, lose local history |

Do not cut:
- `hz_get_briefing` (Day 1) — core product
- Cache (Day 2) — needed for cost control
- HTTP transport (Day 8) — needed for remote
- Auth (Day 10) — needed to charge
- Stripe (Day 11 main path) — needed to charge

---

## Definition of Done (sprint-level)

The sprint is complete when **all** of these are true:

1. [ ] All 4 new tools (`hz_get_briefing`, `hz_search_history`, `hz_subscribe_topic`, + enhanced `hz_run_pipeline`) live in production
2. [ ] 3 config packs available with READMEs
3. [ ] Public HTTPS endpoint with API-key auth
4. [ ] Postgres backend for runs, briefings, tenants, subscriptions
5. [ ] Stripe live-mode checkout works end-to-end
6. [ ] Landing page live with Lighthouse ≥ 90
7. [ ] PR open on `modelcontextprotocol/servers`
8. [ ] Launch posts on Twitter + 小红书 + HN
9. [ ] ≥1 real user signup
10. [ ] Sprint log filled for all 14 days

---

## See Also

- `docs/COMMERCIAL_SPEC.md` — the source of truth for *what* to build
- This file (`IMPLEMENTATION_PLAN.md`) — *how* to build it, day by day
- Obsidian `sprint-log.md` — daily journal of *what actually happened*
- Obsidian `side-hustles/Project-G-Horizon情报引擎/05 - MCP 商业化实现 plan.md` — Obsidian mirror of this file
