# AI Developers Config Pack

For engineers using Claude / Cursor / Codex and shipping LLM-powered software.

## Sources
- GitHub: karpathy + simonw user activity; vllm / sglang / claude-code releases
- RSS: Anthropic news, Simon Willison's blog
- HackerNews (score ≥ 100), r/LocalLLaMA, r/ClaudeAI

## Default Topic Keywords
`llm`, `inference`, `claude`, `anthropic`, `openai`, `cursor`, `vllm`, `sglang`, `triton`, `cuda`, `rag`, `agent`

## Threshold
`ai_score_threshold = 7.5` (slightly stricter than default 7.0 — high-signal pack).

## Usage
```python
hz_get_briefing(topic="LLM inference", config_pack="ai-developers", hours=24, count=5)
```
