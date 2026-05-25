---
layout: default
title: "Horizon Summary: 2026-05-25 (EN)"
date: 2026-05-25
lang: en
---

> From 37 items, 5 important content pieces were selected

---

1. [Huawei's 'Tao's Law' replaces geometric scaling with time scaling to extend chip density](#item-1) ⭐️ 9.0/10
2. [Audiomass: Free, Open-Source Multitrack Audio Editor for the Web](#item-2) ⭐️ 8.0/10
3. [Memory Now Represents Nearly Two-Thirds of AI Chip Component Costs](#item-3) ⭐️ 8.0/10
4. [Study Reveals 'Constraint Decay' in LLM Coding Agents](#item-4) ⭐️ 8.0/10
5. [Vivado 2026.1 Free Tier Drops Linux Support, Angering FPGA Community](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Huawei's 'Tao's Law' replaces geometric scaling with time scaling to extend chip density](https://www.peopleapp.com/column/30052220655-500007509895) ⭐️ 9.0/10

Huawei announced 'Tao's Law' at ISCAS 2026, proposing to replace traditional geometric scaling (shrinking transistor size) with time scaling (reducing signal propagation delay via the time constant τ). The company has already designed and mass-produced 381 chips using this principle over six years, and will release a new Kirin phone chip this fall featuring 'logic folding' technology. This is China's first globally proposed guiding principle for the semiconductor industry, providing a practical path to continue performance scaling as Moore's Law hits physical limits. It can enable transistor density equivalent to a 1.4nm process without relying solely on advanced lithography, significantly impacting AI/ML hardware evolution and the global chip landscape. The law focuses on reducing the time constant τ (tau), which is the product of resistance and capacitance (RC) determining signal travel time, through multi-level optimization from device, circuit, chip, to system. The enabling technology is 'logic folding', set to debut in the 'Kirin 2026' phone chip, with a roadmap targeting 1.4nm-equivalent density by 2031. The detailed technical mechanism of logic folding has not been publicly disclosed.

telegram · zaihuapd · May 25, 01:35

**Background**: Moore's Law historically advanced by geometric scaling—shrinking transistor gate lengths to pack more into a chip. As dimensions approach atomic scales, further shrinking becomes extremely difficult and costly. 'Time scaling' addresses the same problem from signal propagation: the time constant τ = RC dictates how fast a signal can travel. By optimizing circuit topology and system architecture to shorten signal paths and reduce delay, Huawei effectively increases processing density without making transistors tinier. The Greek letter τ also corresponds to the Chinese character '韬,' which is part of the name of He Tingbo, Huawei's semiconductor head.

<details><summary>References</summary>
<ul>
<li><a href="https://www.21jingji.com/article/20260525/herald/1573642c437a5e4e76a15fc1c40f0a35.html">华为提出的"韬定律"是什么？跟摩尔定律有什么不同？ - 21经济网</a></li>
<li><a href="https://www.huxiu.com/article/4861142.html">华为发布"韬定律"半导体新理论 提出以时间缩微替代几何缩微</a></li>
<li><a href="https://www.ithome.com/0/954/677.htm">华为发表半导体韬定律：预计到 2031 年，基于该定律的高端芯片晶体管密度将达到 1.4 纳米制程的同等水平</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#芯片设计`, `#技术突破`, `#华为`

---

<a id="item-2"></a>
## [Audiomass: Free, Open-Source Multitrack Audio Editor for the Web](https://audiomass.co/?multitrack=1) ⭐️ 8.0/10

Audiomass, a free and open-source multitrack audio editor, has been released as a web application, enabling users to mix and edit audio tracks directly in the browser with native FLAC support and an intuitive interface. This tool democratizes audio editing by eliminating installation and platform barriers, making multitrack production accessible from any modern browser; it also opens up possibilities for real-time online collaboration, as suggested by the community. The editor features a classic vanilla JavaScript codebase reminiscent of pre‑framework development, native FLAC handling, and an interface praised for its similarity to early Cool Edit Pro; however, the project currently lacks a clear open‑source license, which may hinder adoption.

hackernews · pantelisk · May 24, 15:25 · [Discussion](https://news.ycombinator.com/item?id=48258015)

**Background**: FLAC (Free Lossless Audio Codec) is a lossless audio compression format that retains original audio quality, widely used by audiophiles. Multitrack audio editors like Audacity and professional DAWs allow users to layer and edit multiple audio tracks. Traditionally, such tools require desktop installation; Audiomass brings full‑featured editing to the browser, lowering the barrier to entry for casual creators.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FLAC">FLAC - Wikipedia</a></li>
<li><a href="https://www.audacityteam.org/">Audacity ® | Free Audio editor, recorder, music making and more!</a></li>

</ul>
</details>

**Discussion**: Commenters praised the editor’s intuitive UX reminiscent of early Cool Edit Pro, its nostalgic vanilla JavaScript style, and native FLAC support. Some raised concerns about the absence of a license file, while others dreamed of adding cloud collaboration features to enable remote jamming.

**Tags**: `#audio-editor`, `#open-source`, `#web-application`, `#show-hn`, `#multitrack`

---

<a id="item-3"></a>
## [Memory Now Represents Nearly Two-Thirds of AI Chip Component Costs](https://epoch.ai/data-insights/ai-chip-component-cost-shares) ⭐️ 8.0/10

A new analysis from Epoch AI reveals that memory components, primarily high-bandwidth memory (HBM), now account for nearly two-thirds of the total component cost of AI accelerator chips, highlighting the extreme supply-demand imbalance in the DRAM market. The dominance of memory costs suggests that AI hardware could become substantially cheaper once DRAM supply matches demand, potentially enabling wider AI adoption and reducing barriers for smaller players. It also underscores the critical dependency of AI progress on memory manufacturing capacity. The cost breakdown specifically points to high-bandwidth memory (HBM), a 3D-stacked DRAM technology that provides the massive throughput required by GPUs like NVIDIA's H100. The analysis implies that even if logic die costs remain constant, total chip cost is dominated by memory.

hackernews · intelkishan · May 24, 16:31 · [Discussion](https://news.ycombinator.com/item?id=48258684)

**Background**: AI accelerators like GPUs rely on high-bandwidth memory (HBM) to feed data to thousands of processing cores. HBM uses 3D stacking and through-silicon vias (TSVs) to achieve terabyte-per-second bandwidth, but it is expensive and supply-constrained. The AI boom, especially large language models, has caused a surge in HBM demand, leading to price increases and shortages as DRAM manufacturers struggle to scale production.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree that memory supply constraints are a major bottleneck, with one noting a potential 3x hardware cost reduction if supply meets demand. Others expressed frustration over doubled RAM prices and personal decisions to delay hardware upgrades until prices normalize, reflecting widespread concern over memory affordability.

**Tags**: `#ai hardware`, `#memory`, `#chip design`, `#cost analysis`, `#supply chain`

---

<a id="item-4"></a>
## [Study Reveals 'Constraint Decay' in LLM Coding Agents](https://arxiv.org/abs/2605.06445) ⭐️ 8.0/10

A new paper identifies that LLM-based coding agents suffer from 'constraint decay', with performance dropping by an average of 30 percentage points in assertion pass rates when forced to follow explicit architectural rules like database schemas and ORM patterns. This finding reveals a critical fragility in AI coding agents, confirming that while they excel at unconstrained prototyping, they are currently unreliable for production-grade backend development where strict architectural constraints are necessary. The paper reports that capable models lose an average of 30 points in assertion pass rates when structural constraints accumulate. The study primarily tested non-frontier models, so the performance of the latest frontier systems under constraints remains underexplored.

hackernews · wek · May 24, 12:55 · [Discussion](https://news.ycombinator.com/item?id=48256912)

**Background**: LLM agents are AI systems that use large language models to autonomously perform tasks like code generation, interacting with codebases and tools. Back-end development often requires strict adherence to architectural patterns, such as database schema design, Object-Relational Mapping (ORM) configurations, and API structure. Constraint decay refers to the observed decline in code quality and correctness when these explicit rules must be followed, as opposed to more free-form code generation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.06445v1">Constraint decay: The Fragility of LLM Agents in Backend Code ...</a></li>
<li><a href="https://news.ycombinator.com/item?id=48256912">Constraint Decay: The Fragility of LLM Agents in Back End ...</a></li>
<li><a href="https://byteiota.com/llm-agent-constraint-decay-backend-code/">LLM Agent Constraint Decay: Why Real Backends Break AI Code</a></li>

</ul>
</details>

**Discussion**: Practitioners confirm experiencing constraint decay in real projects, noting that agents struggle more with large-scale architectural rules. Some suggest that constraints should be introduced incrementally during the coding process rather than specified upfront. Concerns remain about whether this fragility holds for frontier models, and a related side-effect of 'calcification' was mentioned, where repeated patterns in code generation hinder adaptability.

**Tags**: `#LLM agents`, `#code generation`, `#constraint decay`, `#backend development`, `#AI reliability`

---

<a id="item-5"></a>
## [Vivado 2026.1 Free Tier Drops Linux Support, Angering FPGA Community](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US) ⭐️ 8.0/10

AMD announced that starting with version 2026.1, the Vivado Design Suite's free 'Basic' tier will no longer support the Linux operating system, while Windows support remains. This decision alienates a large portion of the FPGA development community—including students, hobbyists, and open-source developers—who predominantly use Linux, potentially hindering AMD's ecosystem growth and driving users to competing platforms like Lattice. The free Basic tier will remain device-limited and require annual renewal, but Linux support is removed; official statements have not provided a technical or business justification, focusing instead on the new tiered licensing structure.

hackernews · zdw · May 24, 04:14 · [Discussion](https://news.ycombinator.com/item?id=48254309)

**Background**: Xilinx Vivado is a comprehensive suite for FPGA design, synthesis, and implementation, widely used in hardware development and education. The free tier, previously available for both Windows and Linux, enabled hobbyists and students to learn and develop on AMD hardware without cost. Linux is favored by many developers for its flexibility and open-source tool integration. AMD acquired Xilinx in 2022.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vivado">Vivado - Wikipedia</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-licensing-options.html">AMD Vivado™ Licensing Options | Flexible Subscription & Perpetual Tiers</a></li>

</ul>
</details>

**Discussion**: The community reaction is overwhelmingly negative. Users criticize AMD for nickel-and-diming even loyal customers, creating licensing hassles for CI setups and interns, and worry that removing Linux support will deter students and shrink the hobbyist ecosystem. Several commenters suggest switching to Lattice FPGAs, citing better treatment of free-tier users and stronger documentation. Some long-time Xilinx users now consider moving to competitors.

**Tags**: `#FPGA`, `#AMD`, `#Vivado`, `#Linux`, `#licensing`

---