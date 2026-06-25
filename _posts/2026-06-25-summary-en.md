---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 38 items, 19 important content pieces were selected

---

1. [OpenAI unveils Jalapeno, its first custom AI chip with Broadcom](#item-1) ⭐️ 10.0/10
2. [Anthropic Alleges Alibaba Illicitly Extracted Claude AI Capabilities](#item-2) ⭐️ 8.0/10
3. [Qualcomm to Acquire AI Startup Modular for $4 Billion](#item-3) ⭐️ 8.0/10
4. [NVIDIA's 45°C Liquid Cooling Slashes Data Center Water Use](#item-4) ⭐️ 8.0/10
5. [Superhuman Generals.io Agent via Self-Play RL and Vision Transformer](#item-5) ⭐️ 8.0/10
6. [DeepSWE: A Contamination-Free Benchmark for AI Code Generation](#item-6) ⭐️ 8.0/10
7. [LuaJIT 3.0 Proposal Introduces C-Style Syntax Extensions](#item-7) ⭐️ 7.0/10
8. [RubyLLM: A Ruby framework for all major AI providers](#item-8) ⭐️ 7.0/10
9. [Google Launches Computer Use in Gemini 3.5 Flash](#item-9) ⭐️ 7.0/10
10. [Fund Launched to End Respiratory Infections](#item-10) ⭐️ 7.0/10
11. [Simon Willison Converts MDN Browser Compatibility Data into a CORS-Enabled SQLite Database](#item-11) ⭐️ 7.0/10
12. [LLM-Generated Job Applications Erase Personal Identity, Tom MacWright Warns](#item-12) ⭐️ 7.0/10
13. [LLM Inference Pricing Across 7 Providers Reveals Surprising Cache Savings](#item-13) ⭐️ 7.0/10
14. [Blogging Can Just Be Stating the Obvious](#item-14) ⭐️ 6.0/10
15. [PR Spam Now Mirrors Early 2000s Email Spam](#item-15) ⭐️ 6.0/10
16. [Datasette 1.0a35 adds table creation and alteration interfaces](#item-16) ⭐️ 6.0/10
17. [Papers with Code Aggregates Top Open-Source OCR Models Including New Baidu and Mistral Releases](#item-17) ⭐️ 6.0/10
18. [MuJoFil: A GPU-Native Simulator Combining Newton Physics and Filament for High-Fidelity Vision RL](#item-18) ⭐️ 6.0/10
19. [HDD-RoPE: High-Dimensional Dynamic Rotary Positional Embedding Emerges](#item-19) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI unveils Jalapeno, its first custom AI chip with Broadcom](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 10.0/10

OpenAI announced its first custom AI inference chip, named Jalapeno, developed in collaboration with Broadcom and manufactured by TSMC, going from design to production in just nine months with AI-assisted optimization. This marks a strategic shift for OpenAI toward vertical hardware integration, reducing reliance on third-party GPUs and potentially lowering inference costs and latency for its AI services. The chip was designed from start to production in only nine months, with OpenAI's models used to accelerate parts of the design and optimization process. It is manufactured by TSMC and specifically targets AI inference workloads.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference chips are specialized processors optimized for running trained models to make predictions on new data, offering better performance per watt than general-purpose GPUs. OpenAI has historically depended on Nvidia GPUs, but custom chips can be tailored to specific model architectures for lower cost. Google has been developing its own inference-optimized TPUs for years, and companies like Groq have pioneered dedicated inference hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://naddod.medium.com/inference-chip-guide-the-foundation-of-scalable-ai-applications-d18f2c22b36c">Inference Chip Guide: The Foundation of Scalable AI Applications | by NADDOD | Medium</a></li>
<li><a href="https://groq.com/">Groq is fast, low cost inference.</a></li>

</ul>
</details>

**Discussion**: Commenters were skeptical about the AI-accelerated design claim, seeing it as potential marketing fluff. Some discussed the idea of hardcoding model weights into silicon for extreme throughput, citing companies like Taalas. The move was generally viewed as significant, with comparisons to Google's long-standing TPU strategy.

**Tags**: `#AI`, `#hardware`, `#OpenAI`, `#Broadcom`, `#chips`

---

<a id="item-2"></a>
## [Anthropic Alleges Alibaba Illicitly Extracted Claude AI Capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 8.0/10

Anthropic claims that Alibaba used fraudulent accounts to generate over 28.8 million exchanges with Claude between April and June 2026, and then distilled the model's capabilities, violating terms of service. This dispute highlights the growing tension over intellectual property in AI, as distillation is a common technique but using fraudulently obtained data crosses ethical and legal lines, potentially affecting international AI regulation and competition. The campaign involved nearly 25,000 fraudulent accounts, and the extracted data was likely used for targeted distillation (RLAIF) rather than simple black-box imitation. The reseller ecosystem, where Chinese intermediaries sell Claude tokens at steep discounts in exchange for user logs, further complicates the issue.

hackernews · htrp · Jun 24, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48664814)

**Background**: Knowledge distillation is a machine learning technique where a smaller 'student' model learns to mimic a larger 'teacher' model's behavior, often by training on the teacher's outputs. It is widely used for model compression and efficiency. However, using outputs from a proprietary model without authorization, especially via fraudulent means, may violate terms of service and intellectual property rights. The technique itself is not inherently illegal, but the method of obtaining training data is the key issue here.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Distillation_(machine_learning)">Distillation (machine learning)</a></li>
<li><a href="https://www.ibm.com/think/topics/knowledge-distillation">What is Knowledge distillation? | IBM</a></li>

</ul>
</details>

**Discussion**: Community discussion highlights several viewpoints: some argue that distillation is a legitimate practice, while others note the fraudulent account creation and reseller schemes that subsidize access to harvest data. The Xerox analogy is raised, suggesting that Anthropic itself trained on internet data without consent, and thus the accusation may be hypocritical. The technical distinction between black-box distillation and RLAIF is also discussed.

**Tags**: `#AI`, `#security`, `#distillation`, `#ethics`, `#geopolitics`

---

<a id="item-3"></a>
## [Qualcomm to Acquire AI Startup Modular for $4 Billion](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

Qualcomm announced the acquisition of Modular, the AI startup behind the Mojo programming language and MAX platform, in a deal reportedly valued at $4 billion, aiming to enhance its AI inference capabilities and offer an alternative to Nvidia's CUDA stack. This acquisition could disrupt the AI hardware landscape by enabling a cross-platform AI software stack that runs efficiently on Qualcomm's ARM-based chips, challenging Nvidia's dominance in AI inference, and signals Qualcomm's strategic expansion into AI infrastructure beyond mobile. The deal is reportedly valued at $4 billion; Mojo is built on MLIR to target heterogeneous hardware, and the MAX platform abstracts hardware complexity to accelerate GenAI deployment without code changes.

hackernews · timmyd · Jun 24, 13:49 · [Discussion](https://news.ycombinator.com/item?id=48659798)

**Background**: Mojo is a programming language developed by Modular that aims to combine Python's ease of use with the performance of C++, leveraging MLIR to target CPUs, GPUs, and ASICs. Nvidia's CUDA is the dominant parallel computing platform but is proprietary to Nvidia GPUs. Qualcomm, a leading ARM-based chip designer, has been seeking to strengthen its AI offerings for data centers and edge devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://github.com/modular/modular">GitHub - modular/modular: The Modular Platform (includes MAX ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is mixed: some see Mojo as another cross-platform language that may fail to become truly universal, while others view the acquisition as a strategic move by Qualcomm to build an ARM-based AI inference stack, potentially challenging Nvidia's dominance. Some note the $4 billion valuation and Qualcomm's broader portfolio moves toward RISC-V and AI infrastructure.

**Tags**: `#AI`, `#acquisition`, `#Qualcomm`, `#Modular`, `#Mojo`

---

<a id="item-4"></a>
## [NVIDIA's 45°C Liquid Cooling Slashes Data Center Water Use](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA has introduced a direct-to-chip liquid cooling design that operates at 45°C (113°F), far warmer than traditional cooling systems, enabling data centers to run with near-zero water consumption and eliminating the need for evaporative cooling. This breakthrough addresses the soaring water and energy demands of AI data centers, potentially saving millions of liters of water per facility annually and making waste heat recovery for district heating more feasible, which could turn data centers into community assets. The design is part of NVIDIA's Rubin-generation reference architecture, using higher coolant temperatures to reduce chiller energy and avoid water consumption. Its effectiveness depends on external climate conditions, and the 45°C outlet temperature is still within safe limits for modern server components.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Traditional data centers often use air conditioning or water-thirsty evaporative cooling, which can consume millions of gallons of water per year. Liquid cooling is far more efficient but typically requires coolant temperatures below 30°C. Raising the operating temperature to 45°C reduces the energy needed for chilling and makes the waste heat easier to reuse, for example in district heating networks that distribute heat to nearby buildings. Data center heat reuse is already being pioneered in Europe, where projects channel excess heat into residential and commercial systems.

<details><summary>References</summary>
<ul>
<li><a href="https://fortune.com/2026/06/22/nvidia-new-data-center-design-ai-water-problem-cooling/">Nvidia says its new data center design will fix AI’s water problem | Fortune</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers">NVIDIA Unveils 45°C Liquid Cooling Design for AI Data Centers</a></li>
<li><a href="https://www.weforum.org/stories/2025/06/sustainable-data-centre-heating/">These companies are using data centres to heat cities | World Economic Forum</a></li>

</ul>
</details>

**Discussion**: Commenters point out a strong synergy with district heating, though summer heat dissipation remains a challenge. Some question the novelty, citing NASA's existing high-temperature liquid cooled facility, while others note practical limitations like pump temperature ratings. The overall sentiment is optimistic but recognizes that climate conditions and local infrastructure heavily influence feasibility.

**Tags**: `#data center`, `#liquid cooling`, `#sustainability`, `#NVIDIA`, `#HPC`

---

<a id="item-5"></a>
## [Superhuman Generals.io Agent via Self-Play RL and Vision Transformer](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

A self-play reinforcement learning agent using a Vision Transformer and reimplemented entirely in JAX reached #1 on the Generals.io 1v1 leaderboard, achieving superhuman performance. The project provides an open-source JAX-based simulator and a detailed technical guide. It demonstrates that scaling with transformer architectures and efficient simulators can outperform domain-specific heuristics, offering a blueprint for building superhuman agents in imperfect-information RTS games. The open-source code and simulator are valuable resources for the RL community. The agent replaced a CNN with a Vision Transformer and reimplemented the pipeline from NumPy/PyTorch to JAX, focusing on scaling over human priors. It was originally developed from behavior cloning and RL fine-tuning for a master's thesis, and the JAX simulator handles imperfect-information real-time strategy environments.

reddit · r/MachineLearning · /u/shrekofspeed · Jun 24, 16:18

**Background**: Generals.io is a fast-paced multiplayer strategy game where players expand territory, battle enemies, and try to capture the opponent's general under fog of war. A Vision Transformer (ViT) splits an image into patches and processes them as tokens, offering high capacity and scalability compared to CNNs. The project leverages JAX, a high-performance numerical computing library, to build an efficient simulator and training pipeline.

<details><summary>References</summary>
<ul>
<li><a href="https://www.indiedb.com/games/generalsio">Generals . io Windows, Mac, iOS, Android game - IndieDB</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#self-play`, `#game-ai`, `#jax`, `#vision-transformer`

---

<a id="item-6"></a>
## [DeepSWE: A Contamination-Free Benchmark for AI Code Generation](https://www.reddit.com/r/MachineLearning/comments/1ue0hlp/deepswe_new_benchmark_looking_at_how_well_todays/) ⭐️ 8.0/10

DeepSWE is a new benchmark that evaluates coding agents' software engineering capabilities using contamination-free tasks created from scratch across 91 repositories in 5 languages, with shorter prompts but requiring 5.5x more code and 2x more output tokens than SWE-bench Pro, and hand-written verifiers that test actual software behavior. This benchmark tackles the problem of data contamination and unrealistic simplicity in existing coding benchmarks, offering a more reliable and challenging measure of AI coding agents' real-world software engineering skills, which is essential for advancing the field and comparing frontier models like GPT-5 and Claude Opus. The benchmark is open-source, with verifiers that check software behavior, and tasks are diverse, covering 91 repositories. The prompt length is halved compared to SWE-bench Pro, yet solutions require 5.5x more code and 2x more output tokens, indicating higher real-world complexity.

reddit · r/MachineLearning · /u/we_are_mammals · Jun 24, 02:03

**Background**: SWE-bench Pro is a recent benchmark that aimed to improve upon SWE-bench by introducing more realistic, enterprise-level tasks, but even the best models like GPT-5 score only around 23%. Data contamination, where test content appears in training data, is a recognized problem in AI evaluation, inflating model scores. DeepSWE builds on these efforts by creating tasks from scratch to avoid contamination entirely.

<details><summary>References</summary>
<ul>
<li><a href="https://labs.scale.com/leaderboard/swe_bench_pro_public">SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset ...</a></li>
<li><a href="https://arxiv.org/html/2602.16763v1">When AI Benchmarks Plateau: A Systematic Study of Benchmark Saturation</a></li>

</ul>
</details>

**Tags**: `#benchmarks`, `#code-generation`, `#software-engineering`, `#large-language-models`, `#evaluation`

---

<a id="item-7"></a>
## [LuaJIT 3.0 Proposal Introduces C-Style Syntax Extensions](https://github.com/LuaJIT/LuaJIT/issues/1475) ⭐️ 7.0/10

The LuaJIT 3.0 proposal suggests adding C-style ternary operators (? :), logical operators (&&, ||), and compound assignments (e.g., +=, -=) to the Lua language, aiming to make syntax more familiar to developers from C-like languages. This change could lower the barrier for developers switching from C-like languages, but it risks fragmenting Lua's language identity and breaking existing tooling and educational materials that rely on Lua's unique syntax. The proposal is still under discussion on GitHub issue #1475; it includes both new infix operators and compound assignments. The community has raised concerns about readability, backward compatibility, and potential confusion from having two ways to express the same operation.

hackernews · phreddypharkus · Jun 25, 00:41 · [Discussion](https://news.ycombinator.com/item?id=48667336)

**Background**: LuaJIT is a high-performance just-in-time compiler for Lua, widely used in games, embedded systems, and server-side applications. Lua is known for its minimalistic syntax, with keywords like 'and', 'or', and 'not'. The proposed C-style syntax aims to provide an alternative for developers accustomed to languages like C, JavaScript, and Java, but it deviates from Lua's traditional design philosophy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LuaJIT">LuaJIT - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Reactions are mixed: some commenters argue that C-style ternary and logical operators are unnecessary and hurt Lua's readability, suggesting if-then-else expressions instead. Others worry about added complexity and maintenance burden, while a few see potential quality-of-life improvements. The debate highlights deep concerns about preserving Lua's simplicity.

**Tags**: `#LuaJIT`, `#Lua`, `#programming-languages`, `#syntax`, `#language-design`

---

<a id="item-8"></a>
## [RubyLLM: A Ruby framework for all major AI providers](https://rubyllm.com/) ⭐️ 7.0/10

RubyLLM 1.0 was released in March 2025, providing a unified interface for Ruby developers to interact with AI models from OpenAI, Anthropic, Google, and others. The gem has been praised for its ease of use and developer-friendly API design. It simplifies AI integration for Ruby applications, lowering the barrier for the Ruby community to adopt AI features and keeping Ruby competitive in the rapidly evolving AI landscape. This fills a gap similar to Vercel's AI SDK for JavaScript. Notable limitations include unreliable caching for some providers like xAI, challenges with maintainer responsiveness on pull requests, and a retry pattern that clears model history, complicating trace observability. The responses API is now natively supported in recent versions.

hackernews · doener · Jun 24, 14:41 · [Discussion](https://news.ycombinator.com/item?id=48660711)

**Background**: Ruby is a popular dynamic programming language widely used for web development, especially with the Ruby on Rails framework. Large language models (LLMs) from providers like OpenAI, Anthropic, and Google expose distinct APIs with different conventions. RubyLLM abstracts these differences, offering a single, consistent way for Ruby developers to work with multiple AI models, similar to the Vercel AI SDK for JavaScript.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@raviskit2012/rubyllm-the-ruby-gem-that-makes-ai-feel-right-at-home-a34a1d18def4">💎 RubyLLM: The Ruby Gem That Makes AI Feel Right at Home | by Ravi Prakash | Medium</a></li>
<li><a href="https://dev.to/crmne/introducing-rubyllm-10-a-beautiful-way-to-work-with-ai-5p0">Introducing RubyLLM 1.0: A Beautiful Way to Work with AI - DEV Community</a></li>

</ul>
</details>

**Discussion**: The community generally finds RubyLLM easy to use and useful, comparing it favorably to Vercel's AI framework. However, users report pain points such as unreliable caching for xAI, difficulty getting maintainer engagement on pull requests, and a retry mechanism that erases model history, complicating observability. The maintainer's tendency to merge 'vibe coded' PRs and rewrite submitted contributions has raised concerns about code quality.

**Tags**: `#ruby`, `#ai`, `#llm`, `#framework`, `#open-source`

---

<a id="item-9"></a>
## [Google Launches Computer Use in Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 7.0/10

Google has introduced computer use capabilities in Gemini 3.5 Flash, enabling the model to directly interact with graphical user interfaces, such as clicking buttons and typing. This move positions Google alongside competitors like OpenAI and Anthropic in the race to develop AI agents that can autonomously operate computers, potentially streamlining workflows for developers and users. However, early reliability issues and missing features like MCP support could hinder its real-world utility. The feature is based on the lightweight Gemini 3.5 Flash model. Early user tests reveal frequent errors, such as failing to extract a table from a PDF and accidentally running destructive commands like `git reset --hard`, and it lacks support for the Model Context Protocol (MCP).

hackernews · swolpers · Jun 24, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48662999)

**Background**: Computer use agents are AI models designed to autonomously operate a computer through its GUI, mimicking human actions like clicking and typing. OpenAI's Computer-Using Agent (CUA) and Anthropic's Claude have previously introduced similar capabilities. The Model Context Protocol (MCP) is an open standard for connecting AI models to external data sources and tools, which enables more integrated and extensive task execution. Gemini 3.5 Flash is a lightweight version of Google's Gemini model family, optimized for speed and efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent | OpenAI</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Community feedback is largely critical, with users reporting that Gemini 3.5 Flash frequently fails at simple tasks, lacks MCP integration, and falls short of competitors like Claude and GPT in both benchmarks and real-world coding assistance. Many question why Google hasn't provided a capable coding agent akin to Codex or Claude Code.

**Tags**: `#AI`, `#Google`, `#Gemini`, `#computer-use`, `#LLM`

---

<a id="item-10"></a>
## [Fund Launched to End Respiratory Infections](https://blog.interceptfund.com/p/ending-respiratory-infections) ⭐️ 7.0/10

A philanthropic fund, the Intercept Fund, has been announced with the goal of ending respiratory infections by investing in air cleaning technologies and new preventatives. Respiratory infections like influenza, COVID-19, and common colds cause widespread illness, disability, and economic loss. This initiative could accelerate the development of better preventatives, potentially reducing suffering and deaths, especially for immunocompromised populations. The fund has an initial budget of $500 million. It focuses on air cleaning technologies and new preventatives, though some observers note that far larger investments are needed to tackle the problem.

hackernews · EthanFantl · Jun 25, 01:14 · [Discussion](https://news.ycombinator.com/item?id=48667588)

**Background**: Respiratory infections are among the leading causes of illness and death worldwide, with the COVID-19 pandemic highlighting the need for better prevention. Healthy adults spend roughly 15-25 days per year sick with such infections, representing about 5% of their lives. Public funding for prevention has historically been limited compared to treatment, and philanthropic efforts like this fund aim to address that gap.

**Discussion**: Community reactions are mixed: some express hope and personal relevance, such as a user whose girlfriend died from a respiratory virus, and others who are disabled by long COVID. Others criticize the reliance on philanthropy, noting that $500 million is far less than space exploration budgets, and question the cited statistic of 15-25 sick days per year. Many support the fund's focus on air cleaning and masking.

**Tags**: `#public-health`, `#philanthropy`, `#respiratory-infections`, `#community-discussion`, `#prevention`

---

<a id="item-11"></a>
## [Simon Willison Converts MDN Browser Compatibility Data into a CORS-Enabled SQLite Database](https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything) ⭐️ 7.0/10

Simon Willison has released a new open-source project (simonw/browser-compat-db) that converts Mozilla's MDN browser compatibility data into a portable ~66MB SQLite database. He used AI-assisted tools (Claude Code and Codex Desktop) to generate the conversion script and a GitHub Actions workflow that force-pushes the database to an orphan branch, enabling CORS-enabled CDN access. This makes the extensive browser compatibility data from MDN easily queryable offline and accessible cross-origin, benefiting web applications, developer tools, and AI assistants. It lowers the barrier for integrating compatibility checks into workflows and showcases AI-assisted development for practical data engineering tasks. The 66MB database is built from the mdn/browser-compat-data JSON files using the sqlite-utils library. It is hosted on GitHub's CDN with open CORS headers, allowing direct exploration via Datasette Lite. The build script was generated by Claude Code (Opus 4.8) and the workflow by Codex Desktop (GPT-5.5).

rss · Simon Willison · Jun 24, 23:59

**Background**: MDN browser compatibility data is an open-source JSON dataset from Mozilla documenting web API support across browsers. SQLite is a lightweight, embeddable database engine, and sqlite-utils is a Python library for creating and manipulating SQLite databases. CORS (Cross-Origin Resource Sharing) headers, such as Access-Control-Allow-Origin, allow web applications to fetch resources from a different origin; GitHub's CDN provides these headers for files in regular repositories, enabling cross-origin access.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library for manipulating SQLite databases · GitHub</a></li>
<li><a href="https://bunny.net/academy/http/what-are-cross-origin-resource-sharing-cors-headers/">How do Cross Origin Resource Sharing ( CORS ) Headers work?</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#browser-compatibility`, `#open-data`, `#ai-assisted-development`, `#developer-tools`

---

<a id="item-12"></a>
## [LLM-Generated Job Applications Erase Personal Identity, Tom MacWright Warns](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 7.0/10

Tom MacWright has observed that job applications are now being fully generated by LLMs, including resumes, portfolio sites, and GitHub projects, leaving candidates anonymous and indistinguishable. This trend erodes the authenticity of hiring, making it difficult for employers to assess genuine human qualities, and may prompt a shift toward valuing personal interaction over polished AI-generated materials. MacWright notes that the entire application chain is synthetic: LLM-generated portfolio sites link to LLM-generated GitHub projects with LLM-generated commit messages, creating what he calls 'accidental anonymity'.

rss · Simon Willison · Jun 24, 18:13

**Tags**: `#ai`, `#careers`, `#llm`, `#hiring`, `#authenticity`

---

<a id="item-13"></a>
## [LLM Inference Pricing Across 7 Providers Reveals Surprising Cache Savings](https://www.reddit.com/r/MachineLearning/comments/1ueavxn/i_compiled_llm_inference_pricing_across_7/) ⭐️ 7.0/10

A Reddit user compiled LLM inference pricing from seven providers, including OpenRouter, DeepSeek, and Together AI, into a spreadsheet, highlighting that cached input costs can vary over tenfold and are often dramatically cheaper than non-cached requests. This compilation is significant for developers building agents, RAG pipelines, and multi-turn conversations, where caching policies can drastically reduce costs, shifting the focus from raw token price to effective caching strategies. The spreadsheet includes input/output token pricing, context windows, supported models, and provider-specific differences, but does not cover latency, throughput, cold-start times, or hardware precision (e.g., FP16 vs FP8).

reddit · r/MachineLearning · /u/Technomadlyf · Jun 24, 11:28

**Background**: LLM inference caching reuses previously computed results for repeated prompt prefixes, reducing redundant computation. This is particularly beneficial for RAG (Retrieval-Augmented Generation) where external documents are retrieved and used as context, and for multi-turn conversations where the conversation history is reused. Providers like DeepSeek and Together AI offer different caching mechanisms, with varying documentation and cost structures.

<details><summary>References</summary>
<ul>
<li><a href="https://machinelearningmastery.com/the-complete-guide-to-inference-caching-in-llms/">The Complete Guide to Inference Caching in LLMs</a></li>
<li><a href="https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/">Optimize LLM response costs and latency with effective caching</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#pricing`, `#caching`, `#API providers`, `#cost optimization`

---

<a id="item-14"></a>
## [Blogging Can Just Be Stating the Obvious](https://blog.jim-nielsen.com/2026/blogging-stating-the-obvious/) ⭐️ 6.0/10

Jim Nielsen's blog post argues that sharing seemingly obvious insights is a valid and valuable form of blogging, because new audiences are always discovering information for the first time, and the accompanying discussion explores the curse of knowledge and the power of repetition. This perspective challenges the pressure on bloggers to constantly produce novel ideas, instead encouraging more people to share their knowledge without fear of redundancy, and it highlights how the curse of knowledge can inhibit communication and learning. The post, linked from a 2026-dated URL, is a concise argument without external references; the Hacker News discussion adds rich context, including a PhD mathematician's personal evolution and a direct link to the Wikipedia article on the Curse of Knowledge.

hackernews · Curiositry · Jun 24, 23:46 · [Discussion](https://news.ycombinator.com/item?id=48666927)

**Background**: The 'curse of knowledge' is a cognitive bias where an expert unknowingly assumes others share their background knowledge, making it hard to explain fundamentals. In blogging, writers often fear being unoriginal, but many successful blogs simply repackage known concepts for new learners. This post contributes to a broader conversation about the value of repetition in education and the role of 'new cohorts' in knowledge dissemination.

**Discussion**: The community overwhelmingly agrees, sharing personal stories that reinforce the premise. They emphasize the curse of knowledge, the constant arrival of new learners, and the value of imperfect, rough posts. Some note that criticism of 'not new' content often comes from outside the intended audience, while upvotes prove the content resonated with its target readers.

**Tags**: `#blogging`, `#writing`, `#knowledge-sharing`, `#curse-of-knowledge`, `#communication`

---

<a id="item-15"></a>
## [PR Spam Now Mirrors Early 2000s Email Spam](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 6.0/10

A recent blog post draws a parallel between the surge of spam pull requests on open source repositories and the early 2000s email spam epidemic, sparking discussion about reputation systems and community moderation. GitHub has also recently introduced configurable PR limits for maintainers to help combat this issue. The comparison highlights how spam can erode trust and productivity in open source, just as it did for email, and underscores the need for robust reputation mechanisms to filter out bad actors as AI-generated spam increases. The blog post, published by AI code review tool Greptile, was noted by some commenters as a promotional piece. GitHub's new configurable PR limits for maintainers allow restricting new contributors, but unlike email spam, which relied on IP and domain reputation, PR spam is tied to individual user accounts, making reputation harder to establish.

hackernews · dakshgupta · Jun 24, 14:32 · [Discussion](https://news.ycombinator.com/item?id=48660579)

**Background**: Email spam was a major problem in the early 2000s, leading to filters based on IP reputation and content analysis. Today, open source projects on GitHub are experiencing a wave of spam pull requests, where users submit irrelevant or low-quality contributions, sometimes triggered by tutorials or to promote tools. The Express.js project was hit by such spam in 2024 after a viral YouTube tutorial. The comparison to email spam suggests that similar reputation systems might be needed for GitHub accounts.

<details><summary>References</summary>
<ul>
<li><a href="https://socket.dev/blog/express-js-spam-prs-commoditization-of-open-source">Express.js Spam PRs Incident Highlights the Commoditization ...</a></li>
<li><a href="https://github.com/orgs/community/discussions/53233">What should I do about spam issues or pull requests ... - GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters appreciated GitHub's new PR limits but highlighted the key difference: email spam filters used IP reputation, not individual user identity, making it harder to apply directly to GitHub. Some users felt the blog post was a disguised ad for an AI tool. The community expressed interest in building reputation systems for GitHub, with one suggestion of 'unsubscribe lists' akin to uBlock Origin.

**Tags**: `#open-source`, `#spam`, `#pull-requests`, `#reputation`, `#github`

---

<a id="item-16"></a>
## [Datasette 1.0a35 adds table creation and alteration interfaces](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 6.0/10

Datasette 1.0a35 introduces a new "Create table" interface and a corresponding JSON API, along with an "Alter table" action that allows users to add, rename, reorder, drop columns, and modify constraints, defaults, and foreign keys directly from the UI or API. This release significantly expands Datasette's schema management capabilities beyond read-only exploration, allowing users to build and modify database structures interactively, which is crucial for data wrangling, prototyping, and self-service data management workflows. The create table interface supports defining columns, primary keys, custom column types, NOT NULL constraints, literal and expression defaults, and single-column foreign keys, while the alter table feature covers renaming tables, changing column types, defaults, and constraints, and includes a drop table button. The new template context documentation now provides a stable API for custom templates, with auto-generated docs validated against actual view contexts.

rss · Simon Willison · Jun 23, 21:34

**Background**: Datasette is an open-source tool for exploring and publishing data, built on top of SQLite. It provides a web interface and a JSON API for interacting with databases, and is widely used by data journalists, developers, and researchers for quick data exploration and sharing. The 1.0a35 release is a pre-release version moving toward a stable 1.0.

<details><summary>References</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and publishing data</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#release`, `#sqlite`, `#database-tools`, `#web-api`

---

<a id="item-17"></a>
## [Papers with Code Aggregates Top Open-Source OCR Models Including New Baidu and Mistral Releases](https://www.reddit.com/r/MachineLearning/comments/1ueiam6/find_the_best_opensource_ocr_models_in_one_place/) ⭐️ 6.0/10

A revived Papers with Code page now curates top open-source OCR models and benchmarks, highlighting this week's releases: Baidu's Unlimited OCR (3B parameters, with Reference Sliding Window Attention) and Mistral's OCR 4, available via API. By curating OCR benchmarks and models, this page helps developers quickly choose the best open-source solution for tasks like agentic RAG, which powers internal and external chatbots, streamlining the digitization of company data. Baidu's Unlimited OCR introduces Reference Sliding Window Attention (R-SWA), a variant that reduces attention complexity, and builds on the open-weight DeepSeek OCR. Top recommended benchmarks are OlmOCRBench (Ai2) and OmniDocBench (Shanghai AI Lab), and the leading open model is Chandra OCR 2, which can be self-hosted.

reddit · r/MachineLearning · /u/NielsRogge · Jun 24, 16:26

**Background**: Optical Character Recognition (OCR) converts scanned documents or PDFs into machine-readable text, often in Markdown. Retrieval-Augmented Generation (RAG) enhances LLMs by fetching external knowledge, and agentic RAG uses AI agents to make this pipeline more adaptive. Sliding Window Attention is a transformer technique that restricts each token's attention to a fixed nearby window, reducing computational cost; Baidu's Reference Sliding Window Attention is a novel variant building on this concept.

<details><summary>References</summary>
<ul>
<li><a href="https://klu.ai/glossary/sliding-window-attention">What is Sliding Window Attention? — Klu</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-rag">What is Agentic RAG? | IBM</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#open-source`, `#benchmarks`, `#RAG`, `#machine-learning`

---

<a id="item-18"></a>
## [MuJoFil: A GPU-Native Simulator Combining Newton Physics and Filament for High-Fidelity Vision RL](https://www.reddit.com/r/MachineLearning/comments/1uemrch/mujoco_derived_simulator_for_high_fidelity_vision/) ⭐️ 6.0/10

A new in-development simulator, MuJoFil, combines Nvidia's GPU-native Newton physics engine and Google's Filament renderer to enable highly parallelized, high-fidelity vision-based RL training, with PBR textures and support for external 3D environments like GLB and OpenUSD. It offers both CPU and GPU (CUDA) variants. MuJoFil fills a gap for GPU-native simulators with high-fidelity vision, offering an open-source alternative to licensed tools like NVIDIA Isaac and enabling faster, more scalable training of visuomotor policies for robotics. The simulator is still in early development with significant bugs; the GPU variant is built on NVIDIA Warp (currently named mujofil-warp, planned to be renamed mujofil-cuda), and the CPU variant is available as mujofil. It modifies Filament to render multiple simulations in parallel on the GPU and supports importing environments in GLB, OpenUSD, and other formats from online sources.

reddit · r/MachineLearning · /u/MT1699 · Jun 24, 19:07

**Background**: MuJoCo is a popular physics engine for robotics, but its CPU-based version limits parallelization. MJX, its GPU-accelerated variant, focuses on physics and lacks built-in high-fidelity vision rendering. NVIDIA's Newton engine is an open-source, GPU-native physics engine built on MuJoCo, developed collaboratively with Google DeepMind and Disney Research. Google's Filament is a real-time PBR renderer that can produce realistic visuals. MuJoFil integrates these two to create a simulator optimized for vision-based reinforcement learning.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/newton-physics">Newton Physics Engine | NVIDIA Developer</a></li>
<li><a href="https://github.com/google/filament">GitHub - google/filament: Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, macOS, and WebGL2 · GitHub</a></li>
<li><a href="https://mujoco.readthedocs.io/en/stable/mjx.html">MuJoCo XLA (MJX) - MuJoCo Documentation</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#simulation`, `#GPU`, `#vision`, `#open-source`

---

<a id="item-19"></a>
## [HDD-RoPE: High-Dimensional Dynamic Rotary Positional Embedding Emerges](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 6.0/10

A new positional embedding method called HDD-RoPE has been introduced, which generalizes standard Rotary Position Embedding (RoPE) by using cumulative matrix products to dynamically rotate embeddings in higher-dimensional spaces, with data-dependent rotation rates. Preliminary experiments on the TinyStories dataset show faster convergence compared to the xPos method. This approach could improve the representational capacity of transformer models by allowing them to learn multi-dimensional positional structures (e.g., paragraph or sentence boundaries) instead of just linear sequence positions. Faster convergence may also reduce training costs and benefit scenarios where positional relationships are complex. HDD-RoPE breaks query/key vectors into chunks of arbitrary size (e.g., 4 dimensions) corresponding to multiple rotation axes (e.g., 6 axes for 4D). The rotation amounts are data-dependent, computed from the current layer's activations. The test used a GPT-2-like model with 33M parameters on the TinyStories dataset, but validation is limited to this small, synthetic corpus and no peer review has been conducted.

reddit · r/MachineLearning · /u/mikayahlevi · Jun 24, 18:16

**Background**: RoPE is a relative position encoding that rotates query and key vectors at fixed frequencies, enabling transformers to capture relative distances. xPos extends RoPE by adding a decay mechanism to improve length extrapolation. The TinyStories dataset consists of short, simple stories generated by GPT-3.5/4 with a restricted vocabulary, used for fast experimentation on small language models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2104.09864">[2104.09864] RoFormer: Enhanced Transformer with Rotary Position Embedding</a></li>
<li><a href="https://arxiv.org/abs/2212.10554">[2212.10554] A Length-Extrapolatable Transformer - arXiv.org GitHub - lucidrains/rotary-embedding-torch: Implementation of ... Comparison of RoPE and xPos positional embeddings used in LLMs A Length-Extrapolatable Transformer - arXiv.org XPos Length Extrapolation | lucidrains/rotary-embedding-torch ... A Length-Extrapolatable Transformer - ACL Anthology</a></li>
<li><a href="https://arxiv.org/abs/2305.07759">[2305.07759] TinyStories: How Small Can Language Models Be ... TinyStories · Datasets GitHub - xingvu/TinyStories: Creating a mini GPT-2 model from ... noanabeshima/TinyStoriesV2 · Datasets at Hugging Face GitHub - sri9s/tinystories-language-models: Exploring the ... raymond-van/gpt-tinystories | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#positional embeddings`, `#transformers`, `#RoPE`, `#deep learning`, `#LLMs`

---