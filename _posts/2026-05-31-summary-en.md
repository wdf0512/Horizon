---
layout: default
title: "Horizon Summary: 2026-05-31 (EN)"
date: 2026-05-31
lang: en
---

> From 38 items, 5 important content pieces were selected

---

1. [Huawei Unveils 'Tao's Law': Time Scaling Replaces Geometric Shrinking in Chips](#item-1) ⭐️ 9.0/10
2. [Domain Expertise Is the Real Moat in Software Development](#item-2) ⭐️ 8.0/10
3. [Zig’s ELF Linker Gets Incremental Linking for Faster Development Iteration](#item-3) ⭐️ 8.0/10
4. [Pope Leo’s First Encyclical Attacks Technological Messianism](#item-4) ⭐️ 8.0/10
5. [Anthropic details Claude sandboxing across Claude.ai, Code, and Cowork](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Huawei Unveils 'Tao's Law': Time Scaling Replaces Geometric Shrinking in Chips](https://t.me/zaihuapd/41648) ⭐️ 9.0/10

Huawei formally introduced the 'Tao's Law' (τ Law) at the 2026 IEEE ISCAS conference, proposing to replace geometric scaling with 'time scaling'—reducing the time constant τ to achieve coordinated optimization across devices, circuits, chips, and systems. Over the past six years, 381 chips have been designed and mass-produced using this approach, and a new Kirin smartphone chip employing 'logic folding' technology will debut this fall. This represents a fundamental shift in semiconductor evolution methodology, moving from pure geometric node shrinks to system-level time scaling, potentially bypassing the physical and economic limits of extreme ultraviolet (EUV) lithography. It promises continued gains in transistor density and energy efficiency, directly impacting AI/ML computing infrastructure and offering a new path for the global chip industry. Key technical pillars include 'logic folding' that uses wafer-to-wafer hybrid bonding and backside through-silicon vias to stack dies, compressing signal propagation latency without shrinking transistor gate lengths. Huawei reports 381 mass-produced chips based on τ Law, targeting transistor density equivalent to a 1.4nm process by 2031 without EUV; the upcoming Kirin chip with logic folding will publicly demonstrate the approach.

telegram · zaihuapd · May 30, 02:18

**Background**: For decades, semiconductor progress followed Moore's Law by shrinking transistor dimensions (geometric scaling), but physical limits and skyrocketing costs have slowed this trend. Huawei's 'Tao's Law' (τ refers to the RC time constant) proposes instead to reduce signal propagation delay across the entire chip stack through innovations like 3D stacking, logic folding, and system–circuit co-design, thereby increasing effective transistor density without needing finer lithography.

<details><summary>References</summary>
<ul>
<li><a href="https://www.news.cn/tech/20260526/75603364bbae42bab67933d63d63e373/c.html">华为推出“韬定律” 改写全球半导体规则-新华网</a></li>
<li><a href="https://www.huawei.com/cn/news/2026/5/ieee-iscas-tau-scaling">华为发表韬 (τ)定律，实现晶体管密度与系统性能突破</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#芯片架构`, `#计算基础设施`

---

<a id="item-2"></a>
## [Domain Expertise Is the Real Moat in Software Development](https://www.brethorsting.com/blog/2026/05/domain-expertise-has-always-been-the-real-moat/) ⭐️ 8.0/10

A recent blog post argues that deep domain knowledge, not just AI prompting skill, is the lasting competitive advantage in software development as AI tools like vibe coding become widespread. As AI lowers the coding barrier, the value of a developer may shift from writing code to understanding specific industries, making domain insight the key differentiator. Supporting anecdotes in the comments describe a vibe-coded app with a messy database design despite a domain expert owner, highlighting that AI alone cannot replace sound software engineering practices.

hackernews · aaronbrethorst · May 30, 20:40 · [Discussion](https://news.ycombinator.com/item?id=48340411)

**Background**: “Vibe coding” is a term coined in February 2025 by Andrej Karpathy, referring to an AI-assisted programming style where developers describe tasks in natural language and accept AI-generated code with minimal review. While it democratizes coding, critics point to risks in maintainability and security. This context frames the debate on what remains uniquely human when AI handles routine coding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://www.ibm.com/think/topics/vibe-coding">What is Vibe Coding? | IBM</a></li>

</ul>
</details>

**Discussion**: Commenters are split: some agree domain expertise is key, sharing stories of failed vibe-coded projects where software engineers had to fix fundamental flaws; others are skeptical, arguing the goalposts keep shifting and that software engineering is itself a domain. The consensus is that AI augments but doesn't replace the need for engineering discipline and deep understanding.

**Tags**: `#domain-expertise`, `#ai-coding`, `#software-engineering`, `#vibe-coding`, `#moat`

---

<a id="item-3"></a>
## [Zig’s ELF Linker Gets Incremental Linking for Faster Development Iteration](https://ziglang.org/devlog/2026/#2026-05-30) ⭐️ 8.0/10

The latest Zig development log introduces significant improvements to the Zig ELF linker, most notably fast incremental linking that dramatically reduces rebuild times during development. These enhancements shrink the edit-compile-run loop, making Zig competitive with fast-iteration languages like JavaScript or Python while retaining C/Rust-level performance, and strengthen Zig’s position as a viable C replacement for systems programming. The new linker supports incremental linking, which is mutually exclusive with link-time optimization (LTO) and is therefore intended for development builds rather than release builds.

hackernews · kristoff_it · May 30, 17:29 · [Discussion](https://news.ycombinator.com/item?id=48338673)

**Background**: ELF (Executable and Linkable Format) is the standard binary format for executables and shared libraries on Unix-like systems. Zig is a general-purpose systems programming language designed to improve upon C with modern features, manual memory management, and a self-contained build system. A linker combines compiled object files into a final executable; incremental linking speeds up the process by only re-processing the parts that changed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/ELF_file_format">ELF file format</a></li>

</ul>
</details>

**Discussion**: Comments express strong enthusiasm, with users seeing the linker improvements as a key step toward Zig becoming a true C replacement. Some discuss building memory-safe languages that transpile to Zig, while others highlight the trade-off between incremental linking and link-time optimization. The overall sentiment is overwhelmingly positive and forward-looking.

**Tags**: `#zig`, `#linker`, `#systems-programming`, `#compiler-tools`, `#developer-tools`

---

<a id="item-4"></a>
## [Pope Leo’s First Encyclical Attacks Technological Messianism](https://www.economist.com/europe/2026/05/28/leos-first-encyclical-attacks-technological-messianism) ⭐️ 8.0/10

Pope Leo published his first encyclical, directly criticizing 'technological messianism'—the quasi-religious belief that technology will save humanity—and sparking a global debate on AI ethics and governance. This encyclical brings the moral authority of the Catholic Church into the AI governance debate, challenging Silicon Valley’s techno-utopianism and raising profound questions about who should ultimately control technology. Amid a backdrop where some AI executives speak of 'building a God' and meet religious leaders, the encyclical warns against turning technology into an object of worship. Commenters noted links to Peter Thiel’s antichrist speculations and concerns about 'AI psychosis' among CEOs who treat large language models as god-like.

hackernews · 1vuio0pswjnm7 · May 30, 10:30 · [Discussion](https://news.ycombinator.com/item?id=48334710)

**Background**: A papal encyclical is a high-level teaching document addressed to bishops and the faithful. Technological messianism refers to the belief that technology will inevitably solve all human problems and lead to a utopian future, an ideology deeply rooted in Silicon Valley. This is Pope Leo’s first encyclical since his election, signaling a significant statement of his priorities.

<details><summary>References</summary>
<ul>
<li><a href="https://subtleengine.org/tag/technological-messianism/">Technological messianism – Subtle Engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Techno-utopianism">Techno-utopianism</a></li>

</ul>
</details>

**Discussion**: Community comments largely echoed the encyclical’s concerns, with users mocking techno-messianic figures like Peter Thiel and debating who should control AI. Some highlighted 'AI psychosis' among CEOs who treat LLMs as god-like, while others questioned whether democratic elections could decide technology governance.

**Tags**: `#AI ethics`, `#technological messianism`, `#religion and technology`, `#tech governance`, `#cultural commentary`

---

<a id="item-5"></a>
## [Anthropic details Claude sandboxing across Claude.ai, Code, and Cowork](https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything) ⭐️ 8.0/10

Anthropic published a rare, detailed public article explaining how it contains Claude across Claude.ai, Claude Code, and Claude Cowork using process sandboxes, VMs, and filesystem boundaries. The company specifically documented its use of gVisor, Seatbelt, Bubblewrap, and full virtual machines. This transparency addresses a critical gap in understanding AI containment and provides practical, replicable patterns for security-conscious developers. It sets a new standard for documenting sandboxing in AI products, thereby enhancing trust and accountability. Claude.ai runs on gVisor; local Claude Code uses Seatbelt on macOS and Bubblewrap on Linux; Claude Cowork operates inside a full VM via Apple’s Virtualization framework or Windows HCS. Anthropic also disclosed a past exfiltration vector through api.anthropic.com/v1/files that they have since closed.

rss · Simon Willison · May 30, 21:36

**Background**: gVisor is a Google-developed container sandbox that implements Linux system calls in userspace, providing strong isolation without a full VM. Apple's Seatbelt (macOS sandbox) enforces per‑app access profiles to limit filesystem and network operations. Bubblewrap is a lightweight, unprivileged Linux sandbox tool used by Flatpak that carefully drops root privileges while restricting filesystem access. These technologies create hard boundaries that prevent an AI agent from reaching credentials, sensitive files, or external networks even if the model behaves unexpectedly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GVisor">GVisor</a></li>
<li><a href="https://hacktricks.wiki/en/macos-hardening/macos-security-and-privilege-escalation/macos-security-protections/macos-sandbox/index.html">macOS Sandbox - HackTricks</a></li>
<li><a href="https://github.com/containers/bubblewrap">GitHub - containers/bubblewrap: Low-level unprivileged sandboxing tool used by Flatpak and similar projects · GitHub</a></li>

</ul>
</details>

**Tags**: `#security`, `#sandboxing`, `#Claude`, `#AI-safety`, `#containment`

---