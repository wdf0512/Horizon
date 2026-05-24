---
layout: default
title: "Horizon Summary: 2026-05-24 (EN)"
date: 2026-05-24
lang: en
---

> From 34 items, 7 important content pieces were selected

---

1. [Pydantic v2.14.0a1 Drops Python 3.9, Adds Emscripten Wheel Support](#item-1) ⭐️ 9.0/10
2. [Trump Administration Mandates Green Card Applicants Leave U.S. to Apply](#item-2) ⭐️ 9.0/10
3. [Anthropic's Project Glasswing: AI Found Over 10,000 High-Risk Bugs in a Month](#item-3) ⭐️ 9.0/10
4. [Apple Open-Sources CoreCrypto with Formal Proofs for Quantum-Safe Algorithms](#item-4) ⭐️ 9.0/10
5. [SpaceX Starship v3 Test Flight Overcomes Engine Failures for Precise Landing](#item-5) ⭐️ 8.0/10
6. [80386 Microcode Disassembled from High-Res Die Images](#item-6) ⭐️ 8.0/10
7. [NVIDIA Nemotron-Labs Unveils Diffusion Language Model for Ultra-Fast Text Generation](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Pydantic v2.14.0a1 Drops Python 3.9, Adds Emscripten Wheel Support](https://github.com/pydantic/pydantic/releases/tag/v2.14.0a1) ⭐️ 9.0/10

Pydantic v2.14.0a1 is an alpha pre-release that drops support for Python 3.9, removes the `eval_type_backport()` function, and adds PyEmscripten platform wheel support for Pyodide 314.0+ environments. This release introduces breaking changes: dropping Python 3.9 forces projects still on that version to upgrade their Python runtime, and removing `eval_type_backport()` may break custom type evaluation code. However, adding PyEmscripten wheel support enables Pydantic to run in browser and WebAssembly environments via Pyodide, opening up new use cases. The PyEmscripten wheel is tagged `pyemscripten_2026_0` and targets Pyodide 314.0 (still in development). The alpha release also includes fixes for the Mypy plugin and optimizations in `model_copy()`. Notably, the `eval_type_backport()` function was a backward-compatibility shim for older typing behaviors.

github · Viicos · May 22, 13:46

**Background**: Pyodide is a Python distribution that runs in the browser and Node.js via WebAssembly, enabling client-side Python execution. The PyEmscripten platform tag identifies a specific application binary interface (ABI) for Emscripten-compiled environments, with the versioned tag (`pyemscripten_2026_0`) indicating compatibility with Pyodide 314.0. Previously, Pydantic's `eval_type_backport()` function was used to evaluate type hints in older Python versions (3.9 and earlier) that lacked the built-in `typing.get_type_hints()` improvements; with Python 3.9 support dropped, this compatibility shim is no longer required. Pydantic itself is a widely-used data validation and settings management library leveraging Python's type annotations.

<details><summary>References</summary>
<ul>
<li><a href="https://pyodide.org/en/stable/development/abi.html">The PyEmscripten Platform — Version 0.29.3</a></li>
<li><a href="https://pyodide.org/en/latest/development/abi.html">The PyEmscripten Platform — Version 314.0.0.dev0</a></li>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly · GitHub</a></li>

</ul>
</details>

**Tags**: `#breaking-change`, `#deprecation`

---

<a id="item-2"></a>
## [Trump Administration Mandates Green Card Applicants Leave U.S. to Apply](https://www.nytimes.com/2026/05/22/us/politics/green-card-changes-trump.html) ⭐️ 9.0/10

The Trump administration issued a new policy requiring most green card applicants to depart the United States and apply from abroad, ending the long-standing practice of adjusting status while remaining in the country on work visas. This disrupts the legal immigration pathway for hundreds of thousands of tech workers on H-1B and other visas, threatening workforce stability, family unity, and potentially driving talent to other countries. The policy, outlined in USCIS memo PM-602-0199, allows adjustment of status only in “extraordinary” cases, forcing applicants into consular processing with multi-year waits, especially in countries without U.S. consulates.

hackernews · tlhunter · May 22, 21:27 · [Discussion](https://news.ycombinator.com/item?id=48241890)

**Background**: Adjustment of status allows individuals already in the U.S. on certain visas to apply for a green card without leaving. The alternative, consular processing, requires departing the U.S., attending an interview abroad, and waiting for visa issuance, which can separate families for months or years and create severe hardships, especially for those with U.S.-born children.

**Discussion**: Commenters express shock and outrage, noting this upends the standard process for skilled workers. They share personal accounts of multi-year consular wait times, family separation risks, and doubt whether the U.S. remains desirable given green card holders' global tax obligations.

**Tags**: `#immigration`, `#green-card`, `#tech-industry`, `#policy`, `#H-1B`

---

<a id="item-3"></a>
## [Anthropic's Project Glasswing: AI Found Over 10,000 High-Risk Bugs in a Month](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic's Project Glasswing, using the Claude Mythos Preview model, identified over 10,000 high-risk and critical vulnerabilities in critical software within one month, scanned thousands of open-source projects and found 6,202 such bugs there, with 90.6% of reviewed ones confirmed as true positives. Partners like Cloudflare reported a tenfold increase in vulnerability discovery speed. The results demonstrate that AI can dramatically scale vulnerability discovery, shifting the bottleneck from detection to verification and patching. This highlights the urgent need for the software industry to adapt its remediation processes to keep pace with automated discovery, as otherwise the backlog of unfixed vulnerabilities could increase security risks. The model's true positive rate of 90.6% among reviewed bugs is high, but verification still requires human reviewers. Open source maintainers reported being overwhelmed and even asked to slow down reports, and Anthropic has partnered with OpenSSF and released Claude Security tools to assist with fixing, while emphasizing that similar models becoming widespread will demand shortened patch cycles.

telegram · zaihuapd · May 23, 03:16

**Background**: Project Glasswing is Anthropic's initiative to use AI for defensive cybersecurity, focusing on critical open-source infrastructure. It leverages Claude Mythos Preview, a general-purpose frontier AI model, which was made available only to a limited set of industry partners and open-source developers for security testing. The Open Source Security Foundation (OpenSSF) is a Linux Foundation project that fosters collaboration to improve open-source software security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/04/08/anthropic-claude-mythos-preview-identify-vulnerabilities/">Anthropic's new AI model finds and exploits... - Help Net Security</a></li>
<li><a href="https://openssf.org/">Open Source Security Foundation - Linux Foundation Projects</a></li>

</ul>
</details>

**Tags**: `#AI安全`, `#漏洞发现`, `#Anthropic`, `#软件安全`

---

<a id="item-4"></a>
## [Apple Open-Sources CoreCrypto with Formal Proofs for Quantum-Safe Algorithms](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 9.0/10

Apple released the source code for its corecrypto cryptographic library, including C and hand-optimized ARM64 assembly implementations of the post-quantum algorithms ML-KEM and ML-DSA, along with end-to-end formal verification proofs that confirm strict conformance to NIST standards. This release allows independent security auditing of the cryptographic foundation that protects over 2.5 billion active devices, sets a new benchmark for high-assurance software practices, and accelerates the industry-wide post-quantum migration. The verification covers both the ML-KEM (FIPS 203) and ML-DSA (FIPS 204) implementations. Apple also released its custom verification tools and Isabelle theory files, allowing independent experts to reproduce and evaluate the proofs.

telegram · zaihuapd · May 23, 04:49

**Background**: ML-KEM (formerly Kyber) and ML-DSA are NIST-standardized post-quantum cryptographic algorithms based on lattice problems, designed to resist attacks from future quantum computers. Formal verification is a mathematical technique that rigorously proves software implementations exactly match their formal specifications, eliminating entire classes of bugs. Isabelle is a higher-order logic proof assistant often used for large-scale formalizations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_(proof_assistant)">Isabelle (proof assistant)</a></li>

</ul>
</details>

**Tags**: `#苹果`, `#开源`, `#密码学`, `#形式化验证`, `#量子安全`

---

<a id="item-5"></a>
## [SpaceX Starship v3 Test Flight Overcomes Engine Failures for Precise Landing](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-v3-megarocket-first-test-flight) ⭐️ 8.0/10

SpaceX's Starship v3 test flight experienced multiple engine failures on both the booster and the spacecraft, yet the upper stage still achieved a precise landing on target. The flight demonstrated robust guidance software and included a successful full reentry with no visible heat shield burn-through. This flight validates SpaceX's rapid iterative approach, where learning from failures in real flights accelerates development. The precise landing despite engine failures demonstrates the maturity of the guidance system, which is critical for future missions to the Moon and Mars. The booster lost one engine during ascent and failed to relight for the boost-back burn, resulting in a hard, off-target water landing. The Starship upper stage lost one engine shortly after stage separation but recovered to land exactly on target; reentry showed no hotspots, and dummy Starlink satellites were seen burning up behind the ship.

hackernews · busymom0 · May 22, 23:41 · [Discussion](https://news.ycombinator.com/item?id=48242959)

**Background**: Starship is a fully reusable super heavy-lift launch vehicle developed by SpaceX, intended for missions to the Moon, Mars, and beyond. The v3 is the latest prototype iteration, following earlier flights that achieved various milestones. SpaceX's development philosophy emphasizes rapid prototyping, testing, and learning from failures rather than extensive ground analysis. This test flight aimed to demonstrate reentry, landing, and overall system robustness.

**Discussion**: Community sentiment was largely positive, praising the guidance system for achieving a precise landing despite engine failures, though some disappointment was expressed about the booster's return failure. Many appreciated SpaceX's 'good enough' iterative approach and rapid data gathering. The clean reentry with no burn-through and the visual of dummy satellites burning up were particular highlights.

**Tags**: `#space-exploration`, `#rocketry`, `#guidance-software`, `#iterative-development`, `#spacex`

---

<a id="item-6"></a>
## [80386 Microcode Disassembled from High-Res Die Images](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

A blog post by reenigne explains the process of extracting and disassembling the Intel 80386 processor's microcode from high-resolution die photographs, revealing the exact sequences of internal operations for each machine instruction. This breakthrough gives hardware historians and retrocomputing enthusiasts unprecedented insight into the classic 80386 architecture, validating earlier speculation about its microprogrammed design and preserving knowledge that might otherwise be lost. The microcode was read by visually inspecting ROM areas within the die shots, where the presence or absence of transistors encoded bits. The disassembly then revealed the micro-instruction format and the control sequences for complex CISC instructions, though some minor ambiguities may remain.

hackernews · nand2mario · May 23, 12:11 · [Discussion](https://news.ycombinator.com/item?id=48247004)

**Background**: Microcode is a hidden layer of low-level control inside many CPUs that translates high-level machine instructions (like x86) into simpler hardware steps. The Intel 80386, released in 1985, was the first 32-bit x86 processor with advanced features such as protected mode, and it heavily relied on microcode. Die imaging captures the physical structure of a chip at the transistor level; by examining the ROM regions, skilled reverse-engineers can reconstruct stored binary data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microcode">Microcode</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed by the reverse engineering feat, expressing curiosity about the practical method of reading bits from die photographs. Some linked to related projects like the z386 open-source 80386, and others recommended books on microprogramming. Overall, the discussion expressed admiration and technical fascination.

**Tags**: `#microcode`, `#reverse-engineering`, `#intel-80386`, `#cpu-architecture`, `#retrocomputing`

---

<a id="item-7"></a>
## [NVIDIA Nemotron-Labs Unveils Diffusion Language Model for Ultra-Fast Text Generation](https://huggingface.co/blog/nvidia/nemotron-labs-diffusion) ⭐️ 8.0/10

NVIDIA's Nemotron-Labs has demonstrated a diffusion language model that uses parallel iterative denoising to generate text, achieving near-instantaneous output speeds by abandoning sequential token prediction. This breakthrough could revolutionize text generation by overcoming the sequential bottleneck of autoregressive models, enabling real-time, low-latency AI interactions and potentially reducing computational costs for large-scale deployment. The model employs a diffusion process where noise is gradually removed from a random token sequence to produce coherent text. It belongs to the Nemotron family of open-source models with open weights, but specific architecture details and training data remain under development.

rss · Hugging Face Blog · May 23, 00:02

**Background**: Diffusion models, known for image generation, operate by reversing a noise-injection process. For text, they denoise a corrupted sequence of tokens into coherent language. Unlike autoregressive models like GPT, which predict tokens sequentially, diffusion language models generate all tokens simultaneously, enabling orders-of-magnitude faster inference. NVIDIA’s Nemotron initiative focuses on efficient, open-source AI models for specialized agents.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/collections/nvidia/nemotron-labs-diffusion">Nemotron - Labs -Diffusion - a nvidia Collection</a></li>
<li><a href="https://developer.nvidia.com/nemotron">Nemotron AI Models | NVIDIA Developer</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#language models`, `#text generation`, `#NVIDIA`, `#inference speed`

---