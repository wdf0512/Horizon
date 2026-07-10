---
layout: default
title: "Horizon Summary: 2026-07-10 (EN)"
date: 2026-07-10
lang: en
---

> From 30 items, 17 important content pieces were selected

---

1. [EU Parliament Extends Chat Control 1.0, Warrantless Mass Scanning of Private Messages](#item-1) ⭐️ 10.0/10
2. [OpenAI's GPT-5.6 Sets New SOTA on ARC-AGI-3 and Enhances Intent Understanding](#item-2) ⭐️ 9.0/10
3. [Bun Rewritten from Zig to Rust with Agentic Engineering](#item-3) ⭐️ 9.0/10
4. [Colibri: Run GLM 5.2 on a 32GB Laptop with Int4 Quantization and Expert Streaming](#item-4) ⭐️ 8.0/10
5. [Mitchell Hashimoto on Ghostty, Zig, and pragmatic language choices](#item-5) ⭐️ 8.0/10
6. [Meta Launches Muse Spark 1.1 with API and Agentic Tool Calling](#item-6) ⭐️ 8.0/10
7. [OpenAI’s GPT‑Live Upgrades Voice Mode with Background GPT-5.5 Delegation](#item-7) ⭐️ 8.0/10
8. [LingBot-Video: 13B Sparse-MoE Video Diffusion World Model Released](#item-8) ⭐️ 8.0/10
9. [Tool-call attacks bypass SOTA LLM guardrails over 50% of the time](#item-9) ⭐️ 8.0/10
10. [Tencent's Hy3 Model Sparks Interest with Free Access and Strong Performance](#item-10) ⭐️ 7.0/10
11. [Experimental Rust rewrite of Postgres passes all regression tests](#item-11) ⭐️ 7.0/10
12. [No leap second will be introduced at the end of December 2026](#item-12) ⭐️ 7.0/10
13. [Why Lisp: A Personal Blog Post Sparks Hacker News Debate](#item-13) ⭐️ 7.0/10
14. [IMGNet: Face Verification Using Sign Patterns Instead of Cosine Similarity](#item-14) ⭐️ 7.0/10
15. [New Word Game '18 Words' Challenges Players with Timed Letter Puzzles](#item-15) ⭐️ 6.0/10
16. [Damn Interesting, Early Internet Gem, Seeks Community Support for Survival](#item-16) ⭐️ 6.0/10
17. [Kenton Varda Bans AI-Generated Change Descriptions](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [EU Parliament Extends Chat Control 1.0, Warrantless Mass Scanning of Private Messages](https://www.patrick-breyer.de/en/eu-parliament-greenlights-chat-control-1-0-breyer-our-children-lose-out/) ⭐️ 10.0/10

Despite a majority of voting MEPs (314 against, 276 in favor, 17 abstentions) opposing the regulation, the EU Parliament failed to reject Chat Control 1.0 because the motion needed an absolute majority of 361 votes, which was not reached. This allows US tech companies to resume warrantless scanning of private messages on platforms like Instagram, Discord, Snapchat, and email services. This decision undermines end-to-end encryption and privacy rights, setting a dangerous precedent for mass surveillance in the EU. It affects millions of users who rely on secure communications, and the controversial procedural tactics raise serious concerns about democratic legitimacy. The extension revives the temporary 2021 regulation that allows voluntary scanning of private communications for child sexual abuse material, but critics argue it effectively mandates scanning. The vote was held under urgency procedure on the last parliamentary session before the summer break, with 113 MEPs absent, ensuring that the required absolute majority to reject could not be met.

hackernews · rapnie · Jul 9, 11:03 · [Discussion](https://news.ycombinator.com/item?id=48843923)

**Background**: Chat Control 1.0 is a temporary EU regulation originally enacted in 2021, enabling digital platforms to scan private messages, emails, and files for child sexual abuse material without a warrant. It was set to expire, but this vote extends its provisions. A permanent version, Chat Control 2.0, is still under negotiation. The scanning is often implemented via client-side scanning, which analyzes content on the user's device before encryption, thereby undermining end-to-end encryption protections.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control_1.0">Chat Control 1.0</a></li>
<li><a href="https://fightchatcontrol.eu/chat-control-overview">Chat Control 1.0 vs 2.0 - Fight Chat Control</a></li>
<li><a href="https://samsungmagazine.eu/en/2026/07/09/chat-control/">The end of privacy on the internet. Chat Control passed the ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is overwhelmingly negative, condemning the procedural manipulation (holding the vote before summer break, requiring an absolute majority of all members to reject) as a democratic deficit. Users note that a majority of voting MEPs opposed the measure, yet it passed, and warn of the EU becoming a totalitarian surveillance state. Many highlight the hypocrisy and the erosion of privacy rights.

**Tags**: `#privacy`, `#encryption`, `#eu-regulation`, `#chat-control`, `#mass-surveillance`

---

<a id="item-2"></a>
## [OpenAI's GPT-5.6 Sets New SOTA on ARC-AGI-3 and Enhances Intent Understanding](https://openai.com/index/gpt-5-6/) ⭐️ 9.0/10

OpenAI has released GPT-5.6, its latest frontier model, in three sizes—Luna, Terra, and Sol—with Sol achieving a new state-of-the-art score of 7.8% on the interactive ARC-AGI-3 benchmark, the first frontier model to ever beat a game in it. The release also introduces improved intent understanding, allowing the model to infer user goals better, and preserves original image dimensions when handling images. This achievement marks a significant step toward agentic AI that can reason and interact in novel environments, moving beyond static knowledge tests. The tiered pricing and improved intent understanding could make AI more accessible and autonomous for developers and businesses, while directly challenging competitors like Anthropic's Claude. The model family is priced at $1/$6 (Luna), $2.50/$15 (Terra), and $5/$30 (Sol) per million input/output tokens; for comparison, Claude Opus is $5/$25 and Fable 5 is $10/$50. Developers are advised to still state important constraints, approval boundaries, and success criteria explicitly, as the model's intent inference works best when given clear guardrails.

hackernews · logickkk1 · Jul 9, 17:04 · [Discussion](https://news.ycombinator.com/item?id=48849066)

**Background**: ARC-AGI-3 is a new interactive reasoning benchmark introduced in 2026, designed to measure human-like intelligence by requiring agents to explore novel environments, infer goals, and plan actions without prior training. GPT-5.6 is OpenAI's latest large language model, building on the GPT series, and this release follows the industry trend of offering multiple model sizes for different performance and cost requirements. The model's enhanced intent understanding means it can better interpret the user's underlying goal from a prompt, reducing the need for step-by-step instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">[2603.24621] ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence</a></li>

</ul>
</details>

**Discussion**: Comments reflect a mix of excitement and competitive scrutiny: some users note Google's Gemini seems absent from the conversation, while others highlight the model's ARC-AGI-3 breakthrough and share developer tips on intent understanding. There is also discussion about coding tools (Claude Code vs. Codex) and one comment points out that Anthropic's Fable 5 was excluded from benchmarks because it refused to answer many questions.

**Tags**: `#AI`, `#GPT-5.6`, `#OpenAI`, `#Large Language Models`, `#ARC-AGI`

---

<a id="item-3"></a>
## [Bun Rewritten from Zig to Rust with Agentic Engineering](https://simonwillison.net/2026/Jul/8/rewriting-bun-in-rust/#atom-everything) ⭐️ 9.0/10

Bun’s founder Jarred Sumner published a detailed post describing the rewrite of the JavaScript runtime from Zig to Rust, using coordinated AI agents, dynamic workflows, and adversarial review. The Rust port is already live in Claude Code, achieving 10% faster startup on Linux. This rewrite demonstrates that frontier AI models can enable safe, large-scale language migrations previously considered too risky, solving long-standing memory-safety bugs in Bun and potentially setting a precedent for other projects. The agent-generated PR consisted of over 1 million lines of code, and the process used 5.9 billion uncached input tokens, costing an estimated $165,000 at API pricing. A TypeScript test suite served as a conformance suite, enabling the agent harness to automate the port and verify correctness.

rss · Simon Willison · Jul 8, 23:57

**Background**: Bun is a fast JavaScript runtime originally implemented in Zig, a systems language with manual memory management that led to frequent memory bugs like use-after-free and double-free. Rust, a systems language with compiler-enforced memory safety, was chosen for the rewrite. The rewrite leveraged agentic engineering, where AI agents orchestrate coding tasks, and adversarial review, where multiple agents challenge each other’s code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>
<li><a href="https://simonwillison.net/guides/agentic-engineering-patterns/what-is-agentic-engineering/">What is agentic engineering? - Agentic Engineering Patterns - Simon Willison's Weblog</a></li>
<li><a href="https://github.com/ng/adversarial-review">GitHub - ng/adversarial-review: Claude Code plugin ...</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Bun`, `#Zig`, `#agentic-engineering`, `#systems-programming`

---

<a id="item-4"></a>
## [Colibri: Run GLM 5.2 on a 32GB Laptop with Int4 Quantization and Expert Streaming](https://github.com/JustVugg/colibri) ⭐️ 8.0/10

A developer created Colibri, a single C file engine that runs the 744B MoE model GLM 5.2 on a 32GB RAM laptop by quantizing the dense part to int4 and streaming routed experts from disk, achieving ~0.1 tok/s while keeping the model functional. It demonstrates that massive MoE language models can be run on consumer hardware without GPUs, potentially democratizing access to state-of-the-art AI and inspiring further optimization for local deployment. The model activates only ~40B parameters per token, with the dense part (~17B params) resident in RAM at 9.9 GB and 21,504 routed experts (370 GB total) streamed from disk via LRU cache and OS page cache; the engine uses MTP for speculative decoding and DSA for long context, written in ~1,300 lines of C with no BLAS or Python dependencies.

hackernews · vforno · Jul 9, 08:05 · [Discussion](https://news.ycombinator.com/item?id=48842459)

**Background**: GLM 5.2 is a recently released 744B Mixture-of-Experts (MoE) large language model with a 1M-token context window, known for strong coding and long-horizon task performance. MoE models activate only a fraction of parameters per input, making them memory-efficient if the inactive experts are offloaded. Int4 quantization reduces model weight precision to 4-bit integers, drastically cutting memory usage. Multi-Token Prediction (MTP) speeds up inference by predicting multiple future tokens at once, and Dynamic Sparse Attention (DSA) handles long contexts without quadratic memory growth.

<details><summary>References</summary>
<ul>
<li><a href="https://openlm.ai/glm-5.2/">GLM-5.2 - openlm.ai</a></li>
<li><a href="https://github.com/zai-org/GLM-5">GitHub - zai-org/GLM-5: GLM-5: From Vibe Coding to Agentic ...</a></li>
<li><a href="https://apxml.com/courses/quantized-llm-deployment/chapter-1-advanced-llm-quantization-fundamentals/low-bit-quantization-techniques">Low-Bit LLM Quantization (INT4, NF4, FP4) - apxml.com</a></li>

</ul>
</details>

**Discussion**: Community reactions are largely positive, praising the clever concept and technical achievement. Some question the practicality of 0.1 tok/s, suggesting it could still be useful for overnight batch tasks. Others share parallel efforts—like an Apple Silicon version and modifications to llama.cpp—and note that GLM 5.2 itself is impressive even on high-end hardware.

**Tags**: `#LLM`, `#quantization`, `#inference-optimization`, `#local-models`, `#open-source`

---

<a id="item-5"></a>
## [Mitchell Hashimoto on Ghostty, Zig, and pragmatic language choices](https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/) ⭐️ 8.0/10

A new interview with Mitchell Hashimoto details his journey building Ghostty, a GPU-accelerated terminal emulator, and his choice of Zig over Rust, citing pragmatic trade-offs and negative views on Rust culture. The interview by a high-profile developer like Hashimoto, known for creating foundational infrastructure tools, lends credibility to Zig for serious systems projects and intensifies the debate on language culture and practical trade-offs between Rust and Zig. Hashimoto emphasized Zig's simplicity, better C interoperability, and his dislike of Rust's community culture, though he acknowledged Rust's technical merits. He also discussed the challenges of maintaining software forks and the burden of cross-platform support.

hackernews · veqq · Jul 9, 17:17 · [Discussion](https://news.ycombinator.com/item?id=48849292)

**Background**: Ghostty is a terminal emulator by Mitchell Hashimoto, released in late 2024, featuring GPU acceleration and native UI on Linux, macOS, and Windows. Hashimoto is the co-founder of HashiCorp and creator of infrastructure tools like Terraform and Vagrant. Zig is a systems programming language focused on simplicity, explicit control flow, and easy cross-compilation, often seen as an alternative to C and Rust. The interview explores why he chose Zig for this project.

<details><summary>References</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**Discussion**: Community reactions were mixed: some readers found Hashimoto's pragmatic reasoning inspiring for their own work, while others criticized his remarks about Rust culture as petty and unproductive. The discussion also touched on the maintenance burden of software forks and the broader friction between Rust and Zig communities.

**Tags**: `#zig`, `#rust`, `#terminal`, `#programming-languages`, `#software-engineering`

---

<a id="item-6"></a>
## [Meta Launches Muse Spark 1.1 with API and Agentic Tool Calling](https://simonwillison.net/2026/Jul/9/muse-spark-1-1/#atom-everything) ⭐️ 8.0/10

Meta has released Muse Spark 1.1, the first Spark model with API access, featuring improved agentic tool calling and computer use. The release includes a detailed evaluation report and a new plugin, llm-meta-ai, by Simon Willison for easy CLI access. This marks a significant step in Meta's agentic AI capabilities, enabling developers to integrate advanced tool calling and computer use via a public API. The plugin from a respected developer lowers the barrier to entry, making it highly relevant for AI practitioners building autonomous agents. The evaluation report reveals 'Attractor States in Self-Conversation,' where model self-talk produces existential statements. The model can generate SVGs, though the pelican on a bicycle example was 'a little blocky but recognizable.' The plugin is designed for the LLM command-line tool and installable via uv.

rss · Simon Willison · Jul 9, 16:24

**Background**: Tool calling (function calling) enables large language models to interact with external APIs, code, and systems, extending their capabilities beyond text generation. Agentic AI refers to autonomous systems that plan and execute complex tasks using such tools. The evaluation report's study of attractor states explores how LLM conversations can converge to stable, repetitive patterns when models talk to each other, a known phenomenon in AI discourse.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/tool-calling">What is tool calling? - IBM</a></li>
<li><a href="https://arxiv.org/abs/2606.30571v1">[2606.30571v1] Attractor States Emerge in Multi-Turn LLM Conversations</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#meta`, `#api`, `#tool use`, `#ai agents`

---

<a id="item-7"></a>
## [OpenAI’s GPT‑Live Upgrades Voice Mode with Background GPT-5.5 Delegation](https://simonwillison.net/2026/Jul/8/introducing-gptlive/#atom-everything) ⭐️ 8.0/10

OpenAI has launched GPT‑Live, a new model for ChatGPT voice mode that can delegate complex tasks to GPT‑5.5 in the background while keeping the conversation flowing seamlessly. This upgrade addresses the weak, outdated model behind the previous voice mode, making voice interactions far more capable for serious brainstorming and complex queries, and could revive user engagement with voice AI. The new model runs on iPhone (as previewed), delegates tasks like web search and deep reasoning to GPT‑5.5, and will be updated with future frontier models. A bug where the model laughed inappropriately was reported and tweaked.

rss · Simon Willison · Jul 8, 23:20

**Background**: GPT‑5.5 is OpenAI's latest frontier model, released in April 2026 and codenamed 'Spud', designed for complex tasks like coding, research, and data analysis. Frontier models are the most advanced general-purpose AI systems. The previous ChatGPT voice mode was based on a GPT‑4o era model with a knowledge cut-off in 2024, limiting its usefulness.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT‑5.5 - OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#voice-mode`, `#GPT-5.5`, `#AI`

---

<a id="item-8"></a>
## [LingBot-Video: 13B Sparse-MoE Video Diffusion World Model Released](https://www.reddit.com/r/MachineLearning/comments/1ur0bxq/lingbotvideo_sparsemoe_video_diffusion/) ⭐️ 8.0/10

LingBot-Video is an open-source 13B video diffusion transformer that uses a sparse mixture-of-experts (128 experts, top-8 routing, 1.4B active) and is post-trained with reinforcement learning, including a physical plausibility reward, for action-conditioned video generation in robotics. It blurs the line between video generation and world models, achieving top scores on RBench while raising open questions about VLM-based physics evaluation and the definition of a true world model, which could influence future training and benchmarking. The model uses a DeepSeek-V3-style sparse MoE, six-reward RL post-training (including a VLM-graded reward with real-video negatives to mitigate hacking), and an action-to-video mode; it is open-source with Diffusers/SGLang, but lacks closed-loop robot experiments and relies on VLM for physics judgment.

reddit · r/MachineLearning · /u/Savings-Display5123 · Jul 8, 17:58

**Background**: Sparse mixture-of-experts (MoE) activates only a subset of expert networks per input for efficiency. Video diffusion transformers extend diffusion models to generate temporally consistent videos. Action-conditioned world models predict future video frames from robot actions and are used for planning. LingBot-Video combines these with a large-scale, open-source release.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sparse_mixture-of-experts">Sparse mixture-of-experts</a></li>
<li><a href="https://arxiv.org/abs/2305.13311">[2305.13311] VDT: General-purpose Video Diffusion Transformers via Mask Modeling</a></li>
<li><a href="https://arxiv.org/abs/2606.04463">OSCAR: Omni-Embodiment Action-Conditioned World Model for ...</a></li>

</ul>
</details>

**Tags**: `#world-model`, `#video-diffusion`, `#sparse-moe`, `#robotics`, `#reinforcement-learning`

---

<a id="item-9"></a>
## [Tool-call attacks bypass SOTA LLM guardrails over 50% of the time](https://www.reddit.com/r/MachineLearning/comments/1ur1fnz/agentic_safety_triggers_arent_textual_safety/) ⭐️ 8.0/10

Researchers demonstrated that LLM agents using Model Context Protocol (MCP) for tool access can be exploited by embedding attacks in tool-call sequences rather than prompt text, causing state-of-the-art safety guardrails to fail more than half the time. Even after safety fine-tuning with SafeDPO, refusal rates only reached 48%, while a training-free method achieved roughly 3x the baseline refusal rate. This reveals a critical gap in AI safety for agentic systems, as textual guardrails are insufficient against tool-call manipulation. With LLM agents increasingly deployed with tool access, such attacks could lead to real-world harm, demanding fundamentally new safety alignment approaches. The attack exploits known CVEs and rewrites them as ordinary-sounding requests, so the malicious intent is hidden in the tool-call sequence. Base models (1B–14B parameters) refused ≤35% of attacks; SafeDPO only pushed that to 48%; the training-free method raised refusal to roughly 3x baseline. Code and dataset are provided.

reddit · r/MachineLearning · /u/mlsandwich · Jul 8, 18:36

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in 2024 that allows AI models to connect to external tools like file systems and databases. Direct Preference Optimization (DPO) is a method for aligning LLMs with human preferences directly from preference data, avoiding reinforcement learning. SafeDPO is a safety-constrained variant of DPO that balances helpfulness and safety. The study targets LLM agents using MCP and shows that textual safety guardrails are ineffective against tool-call attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://arxiv.org/abs/2305.18290">[2305.18290] Direct Preference Optimization: Your Language Model is Secretly a Reward Model</a></li>
<li><a href="https://arxiv.org/html/2505.20065v2">SafeDPO: A Simple Approach to Direct Preference Optimization ...</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#LLM Agents`, `#Model Context Protocol`, `#Adversarial Attacks`, `#Security`

---

<a id="item-10"></a>
## [Tencent's Hy3 Model Sparks Interest with Free Access and Strong Performance](https://hy.tencent.com/research/hy3) ⭐️ 7.0/10

Tencent has officially released Hy3, a 295B-parameter Mixture-of-Experts model with 21B active parameters, which outperforms similar-size models and rivals larger ones. It is available for free on OpenRouter until July 21, 2026, sparking community debate. Hy3's strong performance at a relatively small active parameter count demonstrates that efficient model architectures can rival much larger models, potentially reducing inference costs and enabling local deployment. The free access on OpenRouter encourages widespread experimentation and could influence future model development. Hy3 uses a Mixture-of-Experts architecture with 295B total parameters and 21B active parameters, plus 3.8B multi-token prediction layer parameters. The free tier on OpenRouter, provided by Novita, expires on July 21, 2026. Community members note that the effective input price is now similar to DeepSeek-hosted DeepSeek Flash V4.

hackernews · andai · Jul 9, 15:27 · [Discussion](https://news.ycombinator.com/item?id=48847552)

**Background**: Mixture-of-Experts (MoE) models activate only a fraction of their total parameters per input, reducing computational cost. OpenRouter is a platform that aggregates access to various large language models, offering unified billing and inference. The model's free tier was provided by Novita, an AI infrastructure provider.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent-Hunyuan/Hy3">GitHub - Tencent-Hunyuan/Hy3: Hy3 (295B A21B), a leading ...</a></li>
<li><a href="https://hunyuan.tencent.com/research/hy3">Introducing Hy3 - Tencent Hy</a></li>
<li><a href="https://grokipedia.com/page/openrouter">OpenRouter</a></li>

</ul>
</details>

**Discussion**: The community is impressed by Hy3's performance relative to its size, with some comparing it favorably to DeepSeek V4 Flash. However, there is debate about its long-term competitiveness, as its OpenRouter ranking has fallen and pricing is now on par with DeepSeek's own hosted model. Enthusiasm remains for potential local use and quantization.

**Tags**: `#AI`, `#LLM`, `#Tencent`, `#OpenRouter`, `#model comparison`

---

<a id="item-11"></a>
## [Experimental Rust rewrite of Postgres passes all regression tests](https://github.com/malisper/pgrust) ⭐️ 7.0/10

The pgrust project, an experimental Rust rewrite of PostgreSQL heavily assisted by LLMs, has passed 100% of the original PostgreSQL regression tests. This demonstrates that the rewritten database can correctly handle standard SQL operations and extended features tested by the official suite. This achievement shows that LLMs can help generate a functionally correct rewrite of a complex, production-grade system, raising questions about code quality, licensing, and the viability of modernizing legacy software. It could accelerate exploration of alternative database architectures and safer languages like Rust. The project is experimental and not production-ready; the author used LLM assistance to generate over 7,000 commits in less than a month. The license was changed from PostgreSQL's permissive license to AGPL, leading to compatibility concerns. The test suite covers standard SQL and extended features, but performance and real-world workload handling remain untested.

hackernews · SweetSoftPillow · Jul 9, 06:18 · [Discussion](https://news.ycombinator.com/item?id=48841676)

**Background**: PostgreSQL is a 30-year-old open-source relational database written in C. Its regression test suite is a comprehensive set of tests for SQL implementation and extended capabilities. Rust is a systems programming language that emphasizes memory safety and concurrency, making it attractive for rewriting performance-critical software. LLM-assisted code generation uses large language models to produce source code from natural language descriptions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/regress.html">PostgreSQL: Documentation: 18: Chapter 31. Regression Tests</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3747588">A Survey on Large Language Models for Code Generation | ACM Transactions on Software Engineering and Methodology</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is a mix of excitement and skepticism. Users discussed testing methods like mirroring production queries to compare outputs, raised concerns about the feasibility of reviewing LLM-generated code with 7,000+ commits, and debated the license change from PostgreSQL's permissive license to AGPL, questioning compatibility. Some expressed doubt about the value of such rewrites.

**Tags**: `#postgres`, `#rust`, `#llm`, `#database-rewrite`, `#code-generation`

---

<a id="item-12"></a>
## [No leap second will be introduced at the end of December 2026](https://datacenter.iers.org/data/latestVersion/bulletinC.txt) ⭐️ 7.0/10

The International Earth Rotation and Reference Systems Service (IERS) has announced that no leap second will be added to Coordinated Universal Time (UTC) at the end of December 2026. This decision avoids potential timing disruptions in digital systems, networks, and satellites that often struggle with leap second insertions, and it reflects the current unpredictability of Earth's rotation, which has recently been speeding up, making a positive leap second unnecessary for now. The UTC-TAI offset remains at -37 seconds, and the UTC-GPS offset stays at -18 seconds. The announcement follows the IERS's regular six-month bulletin cycle, meaning the next possible leap second could be at the end of June 2027 at the earliest.

hackernews · ChrisArchitect · Jul 9, 14:16 · [Discussion](https://news.ycombinator.com/item?id=48846281)

**Background**: Leap seconds are occasional adjustments to UTC that keep atomic time aligned with the Earth's variable rotation. Since 1972, 27 positive leap seconds have been added, but none since 2016. The IERS monitors Earth's rotation and announces leap seconds about six months in advance. Recently, Earth's rotation has been slightly faster than average, reducing the need for a positive leap second and raising the possibility of a future negative leap second.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Leap_second">Leap second - Wikipedia</a></li>
<li><a href="https://www.nist.gov/pml/time-and-frequency-division/leap-seconds-faqs">Leap Seconds FAQs | NIST</a></li>

</ul>
</details>

**Discussion**: Overall, commenters expressed curiosity about the causes of Earth's rotational unpredictability, technical concerns about UNIX timestamp handling in unmaintained systems, and lighthearted humor. One commenter noted the constant offsets between UTC, TAI, and GPS.

**Tags**: `#leap-second`, `#timekeeping`, `#UTC`, `#systems`, `#IERS`

---

<a id="item-13"></a>
## [Why Lisp: A Personal Blog Post Sparks Hacker News Debate](https://scotto.me/blog/2026-07-09-why-lisp/) ⭐️ 7.0/10

A personal blog post titled 'A road to Lisp: Why Lisp' was published on July 9, 2026, exploring the appeal of Lisp, and it sparked a lively discussion on Hacker News with 107 points and 105 comments. The discussion underscores the enduring fascination with Lisp's powerful features, such as macros and REPL-driven development, while also revealing a growing demand for more balanced critiques of its role in the modern programming ecosystem. The blog post itself is a personal reflection, not a technical breakthrough. Community comments note that REPLs and hot-reloading are now common in many languages, and some argue that articles should offer more critical perspectives on Lisp beyond its traditional praise. A syntax highlighting bug on the original website was also reported.

hackernews · silcoon · Jul 9, 13:06 · [Discussion](https://news.ycombinator.com/item?id=48845209)

**Background**: Lisp is a family of programming languages first specified in 1958, known for its unique code-as-data philosophy, powerful macros that allow code transformation, and the interactive REPL (read-eval-print loop) development environment. Macros in Lisp enable programmers to extend the language itself, while REPL provides a way to execute code piecewise. Paul Graham, a prominent programmer and essayist, has long been a vocal advocate for Lisp, influencing many developers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/REPL">REPL</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lisp_macros">Lisp macros</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was diverse and thoughtful. Commenters debated the 'Light Side' (safety and constraints) versus 'Dark Side' (power and flexibility) of programming paradigms, with some noting that Lisp's REPL and hot-reloading are no longer unique. A recurring sentiment was the desire for more critical, balanced articles on Lisp, rather than purely promotional pieces. A technical issue with syntax highlighting on the blog was also pointed out.

**Tags**: `#Lisp`, `#programming languages`, `#REPL`, `#macros`, `#Hacker News discussion`

---

<a id="item-14"></a>
## [IMGNet: Face Verification Using Sign Patterns Instead of Cosine Similarity](https://www.reddit.com/r/MachineLearning/comments/1urxvxh/i_built_imgnet_a_face_verification_model_that/) ⭐️ 7.0/10

An independent researcher built IMGNet, a face verification model that replaces cosine similarity with sliding window sign pattern matching, using a novel SW Block and IMG Sign MSE Loss. It achieves 96.27% accuracy on LFW and 99.58% when combined with ArcFace embeddings, only 0.24% below ArcFace's native cosine similarity. It challenges the dominance of cosine similarity in face verification, demonstrating that sign pattern agreement can be a competitive alternative. This opens the door to co-designing similarity metrics with training objectives, potentially improving robustness and interpretability. The SW Block computes 240 per-pixel differences across prime window sizes {3,5,7}, and the IMG Sign MSE loss is amplitude-independent and more stable than amplitude-based variants. The model uses a voting system across three metrics and achieves 99.58% on LFW with ArcFace without retraining, suggesting sign pattern consistency is a fundamental property of well-trained embeddings. An occlusion study also hints at implicit spatial organization.

reddit · r/MachineLearning · /u/img-_- · Jul 9, 18:00

**Background**: ArcFace is a widely used face recognition model that employs an additive angular margin loss to generate discriminative embeddings. Typically, face verification compares two embeddings using cosine similarity, which measures the angular distance between vectors. The new approach instead examines sign patterns (positive/negative) across overlapping windows of the embedding, inspired by the idea that identity can be preserved through relational structure rather than absolute values.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1801.07698">[1801.07698] ArcFace: Additive Angular Margin Loss for Deep Face Recognition</a></li>

</ul>
</details>

**Tags**: `#face verification`, `#metric learning`, `#embedding similarity`, `#sign pattern`, `#deep learning`

---

<a id="item-15"></a>
## [New Word Game '18 Words' Challenges Players with Timed Letter Puzzles](https://18words.com/) ⭐️ 6.0/10

A new word game called '18 Words' was posted on Hacker News's Show HN, where players must form words from a set of scrambled letters within a time limit. The launch sparked immediate community feedback, with users requesting timer-free modes, a scramble button, and bug fixes. The game underscores the timeless appeal of simple, well-designed word puzzles and shows how direct user feedback can quickly shape feature development, such as adding a relax mode or a scramble button. It also demonstrates how small web-based games can engage a community and drive iterative improvements. The game currently enforces a timer that ends the game after a few missed words; a bug was reported where the word 'LATER' was incorrectly rejected while 'ALERT' was accepted, indicating a dictionary or validation issue. Users also requested a 'scramble' button to reorder the letters and a relax mode without time pressure.

hackernews · pompomsheep · Jul 9, 12:48 · [Discussion](https://news.ycombinator.com/item?id=48845049)

**Background**: Show HN is a section on Hacker News where users share their personal projects for community feedback. Word games that involve forming words from a set of letters have been popular for decades, from classic board games like Scrabble and Boggle to many digital adaptations. '18 Words' joins this genre with a simple web-based implementation.

**Discussion**: The community feedback was largely constructive. Many users praised the design but criticized the timer, suggesting a 'Relax Mode' with infinite time and an asterisk on the score. A scramble button was requested to help when stuck. A bug was reported where 'LATER' was marked wrong but 'ALERT' was correct, and some suggested a scoring system that allows players to continue after missing a word.

**Tags**: `#game`, `#word-game`, `#show-hn`, `#web`, `#puzzle`

---

<a id="item-16"></a>
## [Damn Interesting, Early Internet Gem, Seeks Community Support for Survival](https://www.damninteresting.com/a-possible-future/) ⭐️ 6.0/10

The long-running independent publication Damn Interesting has publicly appealed to its readers for financial support to secure its future, triggering a wave of nostalgic donations and heartfelt comments from its community. This moment highlights the precarious existence of ad-free, deeply researched content on the modern web, and demonstrates that a loyal community can rally to sustain a niche cultural institution, even as corporate platforms dominate. The site, known for its meticulously researched articles and podcast, has been operating since 2005 and is considered a precursor to shows like 99% Invisible. The author noted the traffic spike was unsolicited and expressed surprise at the Hacker News attention.

hackernews · mzur · Jul 9, 15:25 · [Discussion](https://news.ycombinator.com/item?id=48847511)

**Background**: Damn Interesting is a pioneering independent website that curates obscure, fascinating true stories across science, history, and culture. Launched in 2005, it predated the narrative podcast boom and influenced an entire genre of 'interesting stuff' content. The site is ad-free and relies on reader donations and a small podcast network to survive.

**Discussion**: HN commenters shared a flood of nostalgic memories, recalling how the site shaped their early internet experiences and influenced modern podcasting. The sentiment was overwhelmingly supportive, with many donating immediately and expressing a desire to preserve the 'old internet' spirit.

**Tags**: `#independent publishing`, `#community`, `#nostalgia`, `#podcasts`, `#online content`

---

<a id="item-17"></a>
## [Kenton Varda Bans AI-Generated Change Descriptions](https://simonwillison.net/2026/Jul/8/kenton-varda/#atom-everything) ⭐️ 6.0/10

Kenton Varda, creator of Cap'n Proto and Cloudflare Workers, has banned his team from using AI to write change descriptions such as PR and commit messages. He found that AI-generated descriptions focus on trivial code details that are already visible in the code, while missing the high-level context necessary to understand the purpose of the change. This highlights a common limitation of current AI coding assistants: they can describe what the code does, but not why it was changed or the broader architectural intent. This matters for code review efficiency and software quality, as poor change descriptions can lead to misunderstandings and slower reviews. The ban applies to all AI-generated change descriptions, including PRs, commit messages, and issues/tickets. Varda specifically noted that such descriptions were 'worse than useless' because they omitted the high-level framing.

rss · Simon Willison · Jul 8, 20:03

**Background**: Kenton Varda is a well-known software engineer, the creator of the Cap'n Proto serialization protocol and a key contributor to Cloudflare Workers. The practice of using AI to generate commit messages and PR descriptions has become common in development workflows, but it often produces superficial summaries. This news reflects a growing pushback against uncritical adoption of AI in software engineering.

**Tags**: `#ai-assisted-programming`, `#generative-ai`, `#llms`, `#code-review`, `#commit-messages`

---