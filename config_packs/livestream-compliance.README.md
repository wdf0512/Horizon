# 直播电商合规 Config Pack

为中国直播电商商家与服务商跟踪监管/平台合规动态。

## Sources
- RSS: SAMR 市场监管总局
- Telegram: `@ecom_compliance_cn`（社区维护）

> **维护说明**：直播平台官方公告大多不提供稳定 RSS。如需抖音/快手学习中心 RSS，请在 `data/config.json` 中补充自建抓取脚本，再 merge 进本 pack。

## Default Topic Keywords
合规、处罚、封号、类目、结算、退款、直播、抖音、快手、samr、市监、电商法

## Usage
```python
hz_get_briefing(topic="抖音处罚", config_pack="livestream-compliance", language="zh", hours=48)
```
