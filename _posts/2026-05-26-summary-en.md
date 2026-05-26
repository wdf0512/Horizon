---
layout: default
title: "Horizon Summary: 2026-05-26 (EN)"
date: 2026-05-26
lang: en
---

> From 35 items, 4 important content pieces were selected

---

1. [Using AI to Write Better Code More Slowly](#item-1) ⭐️ 8.0/10
2. [Norway Trains Sovereign LLM with 2PB Huawei Flash Storage and HPE Cray](#item-2) ⭐️ 8.0/10
3. [Armin Ronacher slams AI-generated bug reports, demands return to human-written issues](#item-3) ⭐️ 8.0/10
4. [Huawei Proposes 'Tao's Law': Time Scaling Replaces Geometric Scaling for Chips](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Using AI to Write Better Code More Slowly](https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/) ⭐️ 8.0/10

The article introduces a deliberate multi-model AI workflow where developers use separate LLMs for design (e.g., Claude), implementation, and review (e.g., GPT-5.5), iterating to achieve higher code quality, rather than just speed. This approach challenges the perception that AI coding is only for quick, low‑quality output, showing how careful orchestration can turn LLMs into rigorous engineering partners, potentially improving software reliability and developer productivity in a more sustainable way. The workflow described uses Claude 4.7 Max for implementation, Codex GPT-5.5 xhigh fast for finding corner cases, and back-and-forth fixes. Review loops may sometimes take longer than manual coding, but the resulting quality is noticeably higher.

hackernews · signa11 · May 25, 23:16 · [Discussion](https://news.ycombinator.com/item?id=48272984)

**Background**: Large language models (LLMs) are increasingly applied to code review, detecting bugs and suggesting improvements. Iterative AI development is a paradigm where developers engage in repeated back-and-forth with AI assistants, refining output through multiple cycles. This multi-model technique leverages the different strengths of individual models to emulate a thorough human review process.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Large_Language_Models_for_Code_Review">Large Language Models for Code Review</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-032-09318-9_24">LLMs as Code Review Agents: A Rapid Review and Experimental ... - Springer</a></li>
<li><a href="https://www.linkedin.com/pulse/new-ai-iterative-development-paradigm-why-ia-darren-broemmer">The New AI Iterative Development Paradigm (and Why AI == IA)</a></li>

</ul>
</details>

**Discussion**: The community broadly validated the multi‑model approach. One commenter detailed using Claude for design/implementation and Codex for review, noting that Claude is better at writing fixes. Others argued that most developers don't aim for low quality and that AI can often produce high‑quality code. A few noted the approach sometimes takes longer than manual coding, but agreed the review loop yields better results. Some found multi‑model critique compelling and less prone to deskilling humans.

**Tags**: `#AI-assisted coding`, `#code quality`, `#software engineering`, `#LLM code review`, `#developer tools`

---

<a id="item-2"></a>
## [Norway Trains Sovereign LLM with 2PB Huawei Flash Storage and HPE Cray](https://www.blocksandfiles.com/flash/2026/05/22/norways-2-petabytes-of-huawei-flash-storage-and-llm-training/5244910) ⭐️ 8.0/10

Norway's national library is training a sovereign Norwegian LLM using 2 petabytes of Huawei flash storage and an HPE Cray supercomputer with 448 GPUs and 64,512 CPU cores, as discussed at Huawei’s ID Forum 2026 in Paris. The initiative highlights the global push for sovereign AI to ensure language and cultural representation, sparking debate on the necessity of training models from scratch versus fine-tuning, and raising geopolitical questions about reliance on Huawei hardware. The library's HPE Cray 'Olivia' supercomputer uses 448 GPUs and 64,512 CPU cores, which some experts view as insufficient for full LLM training, fueling skepticism about the project's feasibility; the library's IT head argued that no commercial provider was developing a Norwegian LLM, necessitating a sovereign effort.

hackernews · rbanffy · May 25, 19:37 · [Discussion](https://news.ycombinator.com/item?id=48270770)

**Background**: Sovereign AI initiatives aim to build national AI infrastructure to ensure data sovereignty and cultural inclusion, as seen in countries like the UK with its £500 million Sovereign AI Fund. Training a large language model from scratch demands massive parallel computation and fast storage; HPE Cray supercomputers like the Olivia system are designed for such workloads, while high-performance flash storage such as Huawei’s mitigates data bottlenecks. The Norwegian National Library, which holds a comprehensive digitized collection of Norwegian texts, is a key institution for language preservation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_AI_Fund">Sovereign AI Fund</a></li>
<li><a href="https://grokipedia.com/page/Sovereign_AI">Sovereign AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cray">Cray - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some praised the library's excellent text search interface and supported the need for a sovereign Norwegian LLM, while others questioned the project's feasibility given the modest 448-GPU setup and argued that fine-tuning existing models might be more cost-effective. The claim that global models lack local language knowledge was disputed, with some noting that major providers already train on multilingual data.

**Tags**: `#sovereign-ai`, `#llm-training`, `#storage-infrastructure`, `#national-library`, `#norwegian-language`

---

<a id="item-3"></a>
## [Armin Ronacher slams AI-generated bug reports, demands return to human-written issues](https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything) ⭐️ 8.0/10

Armin Ronacher, creator of Flask, criticized AI-generated issue reports for being verbose, inaccurate, and overconfident. He urged developers to submit concise, human-observed bug reports, providing a simple four-step format. This critique highlights a growing problem in open source: AI-generated 'slop' issues waste maintainers' time and erode trust. As a respected developer, Ronacher's call may influence community norms and tooling to encourage more meaningful human contributions. Ronacher detailed how AI rewordings produce inaccurate conclusions filled with confidence, including fake-minimal reproductions and wrong root-cause guesses. His proposed format: state the command run, expected vs. actual outcome, and the exact error or log.

rss · Simon Willison · May 24, 18:46

**Background**: Armin Ronacher is the creator of the Flask web framework and the Pi package installer, and a respected voice in open source. 'Clanker' is slang for AI, often derogatory, derived from Star Wars battle droids and used to criticize AI output. 'Slop' refers to low-quality, spam-like AI content.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Clanker">Clanker - Wikipedia</a></li>
<li><a href="https://www.euronews.com/next/2025/09/02/what-is-a-clanker-and-why-are-people-on-social-media-using-it-as-an-anti-ai-slang">What is a Clanker and why are people on social media using it as an anti-AI slang? | Euronews</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#software-development`, `#ai`, `#debugging`, `#bug-reports`

---

<a id="item-4"></a>
## [Huawei Proposes 'Tao's Law': Time Scaling Replaces Geometric Scaling for Chips](https://www.peopleapp.com/column/30052220655-500007509895) ⭐️ 8.0/10

At the 2026 ISCAS conference, Huawei's semiconductor head He Tingbo unveiled 'Tao's Law' (τ Law), proposing 'time scaling' to replace traditional geometric scaling by systematically reducing time constants across device, circuit, chip, and system levels. Huawei has already designed and mass-produced 381 chips based on this principle, and a new Kirin phone chip with 'logic folding' technology is set to launch this fall. This represents China's first homegrown guiding principle for semiconductor evolution, offering a new path as Moore's Law reaches its physical and economic limits. It signals Huawei's shift from chasing process nodes to system-level innovation, potentially influencing global chip design strategies and directly addressing the surging compute demands of AI and high-performance computing. The approach focuses on reducing signal propagation delay through techniques like logic folding, targeting transistor density equivalent to 1.4nm process node by 2031 via system-wide co-optimization. Specific technical implementations remain sparse, but the law aims to compress time constant (τ) and boost effective transistor density across all layers of electronic systems.

telegram · zaihuapd · May 25, 01:35

**Background**: Moore's Law has historically relied on geometric scaling—shrinking transistor features to pack more per chip. That approach is now facing fundamental physical limits and rising costs. Time scaling instead improves performance by reducing delays and increasing effective density through architectural and circuit innovations, without requiring ever-smaller process nodes. This becomes crucial as AI and large models drive exponential demand for compute, and as advanced semiconductor manufacturing encounters geopolitical and technical constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://www.guancha.cn/xinzhiguanchasuo/2026_05_25_818270.shtml">心智观察所| 芯片发展的中国方案：华为提出的“韬定律”到底是什么？</a></li>
<li><a href="https://www.huxiu.com/article/4861142.html">华为发布"韬定律"半导体新理论 提出以时间缩微替代几何缩微</a></li>
<li><a href="https://www.eetop.cn/semi/6965611.html">华为“韬(τ)定律”论文全文！ - 半导体/EDA - -EETOP-创芯网</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#芯片设计`, `#摩尔定律`

---