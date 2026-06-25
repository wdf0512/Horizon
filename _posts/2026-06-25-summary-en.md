---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 42 items, 24 important content pieces were selected

---

1. [OpenAI Unveils First Custom AI Inference Chip with Broadcom](#item-1) ⭐️ 9.0/10
2. [Krea 2: State-of-the-Art Open-Weights 12B Image Model](#item-2) ⭐️ 9.0/10
3. [Qualcomm to Acquire AI Startup Modular for $4 Billion](#item-3) ⭐️ 8.0/10
4. [Open-source PR spam resembles early 2000s email spam](#item-4) ⭐️ 8.0/10
5. [GLM-5.2: An Open-Weight Model Challenging Proprietary AI for Coding Agents](#item-5) ⭐️ 8.0/10
6. [Xteink X4: A Microcontroller-Powered, Open E-Ink Reader](#item-6) ⭐️ 8.0/10
7. [John Carmack Reflects on Early Management Mistakes at id Software](#item-7) ⭐️ 8.0/10
8. [Self-Play RL Agent Tops Generals.io Leaderboard with JAX and Vision Transformer](#item-8) ⭐️ 8.0/10
9. [DeepSWE: A Contamination-Free Benchmark for Evaluating Coding Agents](#item-9) ⭐️ 8.0/10
10. [RubyLLM: A Versatile Ruby Framework for Multi-Provider AI Integration](#item-10) ⭐️ 7.0/10
11. [Google Introduces Computer Use for Gemini 3.5 Flash](#item-11) ⭐️ 7.0/10
12. [NVIDIA's 45°C Liquid Cooling Design Cuts Data Center Water Use to Near Zero](#item-12) ⭐️ 7.0/10
13. [Nub: A Bun-like all-in-one toolkit for Node.js](#item-13) ⭐️ 7.0/10
14. [Simon Willison Converts MDN Browser Compatibility Data into SQLite Database](#item-14) ⭐️ 7.0/10
15. [Tom MacWright: AI-generated resumes create accidental anonymity](#item-15) ⭐️ 7.0/10
16. [Datasette 1.0a35 adds Create and Alter Table UI and API](#item-16) ⭐️ 7.0/10
17. [HDD-RoPE: High-Dimensional Dynamic Rotary Positional Embedding Boosts Convergence](#item-17) ⭐️ 7.0/10
18. [LLM Inference Pricing Comparison Shows Caching Cost Disparities Across 7 Providers](#item-18) ⭐️ 7.0/10
19. [Bunny.net Makes Bunny DNS Free with No Query Limits](#item-19) ⭐️ 6.0/10
20. [Elastic Lays Off 7% of Workforce in AI-Driven Reorganization](#item-20) ⭐️ 6.0/10
21. [Blog Post Argues Copying Designs Is a Skill, Sparks Ethical Debate](#item-21) ⭐️ 6.0/10
22. [Papers with Code Launches OCR Benchmark Overview with New Baidu and Mistral Models](#item-22) ⭐️ 6.0/10
23. [MuJoFil: A GPU-Native Simulator for Vision-Based RL with Newton Physics and Filament Rendering](#item-23) ⭐️ 6.0/10
24. [Production ML Models Often Skip Security Testing for Extraction and Poisoning](#item-24) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils First Custom AI Inference Chip with Broadcom](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI announced its first custom AI inference chip, codenamed Jalapeno, developed in partnership with Broadcom and manufactured by TSMC. The chip was designed specifically for AI inference workloads, marking OpenAI's strategic entry into custom hardware. This move reduces OpenAI's dependence on NVIDIA GPUs for inference, potentially lowering costs and improving efficiency. It also signals a broader trend of AI companies designing their own hardware, following Google's TPU example, which could reshape the AI hardware landscape. The chip was developed from design to production in about nine months, with OpenAI claiming its models accelerated parts of the design and optimization. It is fabricated by TSMC, not Intel, and key architectural details or performance benchmarks remain undisclosed.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference is the process where a trained model processes new data to generate outputs, and specialized inference chips are built to handle these computations with low latency and high throughput. Unlike general-purpose GPUs, inference chips are optimized for the repetitive, high-volume demands of serving AI models at scale. OpenAI's custom chip follows a path paved by Google's TPUs and other cloud providers aiming to reduce reliance on third-party hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://naddod.medium.com/inference-chip-guide-the-foundation-of-scalable-ai-applications-d18f2c22b36c">Inference Chip Guide: The Foundation of Scalable AI Applications | by NADDOD | Medium</a></li>
<li><a href="https://cloud.google.com/discover/what-is-ai-inference">What is AI inference? How it works and examples | Google Cloud</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the claim that OpenAI's models accelerated chip design, calling it potentially marketing fluff. Others noted TSMC is the manufacturer, and some discussed more radical ideas like baking model weights directly into silicon. Overall, the community views the move as significant but remains cautious about the limited technical details.

**Tags**: `#OpenAI`, `#custom chip`, `#AI inference`, `#Broadcom`, `#hardware`

---

<a id="item-2"></a>
## [Krea 2: State-of-the-Art Open-Weights 12B Image Model](https://www.krea.ai/blog/krea-2-technical-report) ⭐️ 9.0/10

Krea has released Krea 2, a 12-billion parameter open-weights text-to-image model, along with a fast distilled Turbo variant that generates images in just 8 steps. The release includes a detailed technical report covering training, data curation, and infrastructure. This model achieves state-of-the-art performance among locally hostable open-weights models, rivaling slower proprietary systems, and democratizes access to high-quality AI image generation. The Turbo model is both guidance- and timestep-distilled, enabling 8-step generation, and the full model outperforms many competing models while being significantly faster than Ideogram 4. The report details RL pipelines, prompt expansion, and style references.

hackernews · mattnewton · Jun 23, 15:31 · [Discussion](https://news.ycombinator.com/item?id=48646659)

**Background**: Open-weights models provide publicly accessible trained parameters, allowing anyone to run and fine-tune them locally. Model distillation transfers knowledge from a large teacher model to a smaller, faster student model, reducing inference time without sacrificing quality. Krea 2's 12 billion parameters place it in the larger category of image models, typically requiring high-end GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights : not quite what you’ve been told – Open Source Initiative</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>

</ul>
</details>

**Discussion**: The community praised the release of open weights and the comprehensive technical report, highlighting the Turbo model's efficiency and competitive performance. Some commenters noted that while the model excels in style diversity, it may be overshadowed by newer agentic composition models like Nano Banana 2, and it struggled with certain test prompts. Overall, the reception was very positive.

**Tags**: `#open-weights`, `#text-to-image`, `#generative-ai`, `#model-release`, `#deep-learning`

---

<a id="item-3"></a>
## [Qualcomm to Acquire AI Startup Modular for $4 Billion](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

Qualcomm announced on June 24, 2026, that it will acquire AI infrastructure startup Modular in an all-stock deal valued at nearly $4 billion, gaining access to Modular's AI engine and the Mojo programming language to enhance its software stack for edge and mobile devices. This acquisition strengthens Qualcomm's AI software capabilities, potentially reducing the industry's reliance on Nvidia's CUDA ecosystem and enabling more efficient AI inference on mobile and IoT devices. It signals a major push by Qualcomm into the AI software space, competing with established players. Modular is known for its Modular AI Engine, an inference engine that runs AI models across diverse hardware, and the Mojo programming language, a Python-based language designed for high-performance AI that compiles via MLIR. The deal is all-stock, and Mojo is expected to be open-sourced later in 2026.

hackernews · timmyd · Jun 24, 13:49 · [Discussion](https://news.ycombinator.com/item?id=48659798)

**Background**: Modular was founded by Chris Lattner, creator of LLVM and Swift, with the goal of simplifying AI development across CPUs, GPUs, and accelerators. The Mojo language aims to combine Python's ease of use with systems-level performance, making it attractive for AI workloads. Qualcomm, a dominant mobile chipmaker, has been expanding into AI and edge computing, previously acquiring startups like Tenstorrent and collaborating with Ventana and Alphawave. This acquisition aligns with its strategy to offer a comprehensive AI software-hardware solution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/">Qualcomm to buy startup Modular for $4 billion in AI software push</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/qualcomm-ai-chip-modular-software.html">Qualcomm inks deal for AI startup Modular to bolster software stack - CNBC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed. Some express surprise at the acquisition, questioning its strategic logic given Qualcomm's limited presence in the high-end training market. Others see it as part of a broader portfolio move, including RISC-V and AI, to compete beyond mobile. There is also irony noted that Modular, which criticized hardware companies' AI stacks, is now being acquired by one.

**Tags**: `#AI`, `#acquisition`, `#Qualcomm`, `#Modular`, `#edge computing`

---

<a id="item-4"></a>
## [Open-source PR spam resembles early 2000s email spam](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 8.0/10

Open-source repositories are experiencing a surge in spam pull requests that mirrors the email spam epidemic of the early 2000s, leading to active discussions about mitigation strategies and the growing burden on maintainers. The proliferation of PR spam drains maintainer resources and threatens the collaborative model of open source, potentially discouraging contributions and slowing down legitimate development. GitHub has introduced configurable PR limits for maintainers to curb spam, but the attack surface differs from email spam: GitHub spam relies on individual user accounts rather than IP or domain reputation, making mitigation more nuanced. Some projects have adopted non-textual verification requirements for new contributors.

hackernews · dakshgupta · Jun 24, 14:32 · [Discussion](https://news.ycombinator.com/item?id=48660579)

**Background**: Pull request spam refers to the submission of automated, low-quality, or irrelevant pull requests to open-source repositories on platforms like GitHub. Similar to the email spam wave of the early 2000s, these spam PRs are often designed to promote services, earn contributor badges, or inject malicious code. The influx creates significant triage work for maintainers, who until recently had limited built-in defenses. The comparison underscores the need for platform-level anti-spam measures and community-driven solutions.

<details><summary>References</summary>
<ul>
<li><a href="https://garvitasood.medium.com/github-clean-up-spam-babc5e5b5ab0">GitHub Clean-up Spam . by Garvita Sood, Anuj Bansal, Garima | Medium</a></li>
<li><a href="https://github.com/shitoberfest/spam-pullrequests">GitHub - shitoberfest/ spam - pullrequests : Show the world how many...</a></li>

</ul>
</details>

**Discussion**: Community members shared mitigation strategies: GitHub's new configurable PR limits, requiring non-textual verification for new contributors, and token-based donations for maintainers. A key insight was that unlike email, PR spam targets individual user accounts rather than server reputation, making it harder to block. Some also drew parallels to the anti-spam legal frameworks of the early 2000s.

**Tags**: `#open-source`, `#spam`, `#pull-requests`, `#maintainer-experience`, `#github`

---

<a id="item-5"></a>
## [GLM-5.2: An Open-Weight Model Challenging Proprietary AI for Coding Agents](https://www.interconnects.ai/p/glm-52-is-the-step-change-for-open) ⭐️ 8.0/10

Z.AI has released GLM-5.2, an open-weight large language model that achieves competitive benchmark scores on coding agent tasks like SWE-bench Pro (62.1%) and Terminal-Bench 2.1 (81.0%), rivaling some proprietary models. This model provides a low-cost, openly accessible alternative for building autonomous coding agents, potentially democratizing advanced AI coding tools for developers worldwide who cannot afford expensive subscriptions. GLM-5.2 uses multi-token prediction and shows strong performance on design and agentic benchmarks, but it lags behind Claude Opus 4.8 on SWE-bench and NL2Repo. Users report excessive token consumption—draining weekly quotas in hours—and restrictive service plans that limit practical usage.

hackernews · vantareed · Jun 23, 03:23 · [Discussion](https://news.ycombinator.com/item?id=48639840)

**Background**: Open-weight models make their trained parameters publicly available, enabling local deployment and customization. Coding agents are AI systems that can autonomously write, debug, and deploy software. GLM-5.2 is developed by the Chinese lab Z.AI and competes with frontier models like Claude Opus, GPT-5.5, and Gemini 3.1 Pro in the fast-growing field of AI-assisted coding.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reddit.com/r/technology/comments/1uc5hjh/what_is_glm52_another_opensource_chinese_ai_model/">r/technology on Reddit: What is GLM-5.2? Another open-source Chinese AI model has Silicon Valley's attention.</a></li>
<li><a href="https://docs.z.ai/guides/llm/glm-5.2">GLM-5.2 - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-glm-5-2-open-weight-model">What Is GLM 5.2? The Open-Weight Model Beating GPT 5.5 on Design Benchmarks | MindStudio</a></li>

</ul>
</details>

**Discussion**: Sentiment is mixed: some users praise GLM-5.2's performance and affordability, calling it a step change for those priced out of proprietary tools; others criticize the token consumption and service plan, describing it as a scam due to rapid quota depletion and frequent 429 errors.

**Tags**: `#AI`, `#open-weight models`, `#GLM-5.2`, `#coding agents`, `#LLM evaluation`

---

<a id="item-6"></a>
## [Xteink X4: A Microcontroller-Powered, Open E-Ink Reader](https://blog.omgmog.net/post/xteink-x4-e-ink-reader/) ⭐️ 8.0/10

The Xteink X4 is a new minimalist e-reader that uses a microcontroller instead of a full operating system, enabling an open, hackable platform with easy WiFi-based book transfers. It challenges the locked-down ecosystems of mainstream e-readers like Kindle, proving that a simple microcontroller can deliver a distraction-free reading experience and potentially inspire more open hardware designs. The X4 features a 4.3-inch E Ink screen, USB-C charging, magnetic attachment for phones, and a built-in HTTP server for drag-and-drop file transfers; it lacks a backlight and the small screen size may be a limitation for some users.

hackernews · felixdoerp · Jun 24, 16:35 · [Discussion](https://news.ycombinator.com/item?id=48662381)

**Background**: Traditional e-readers like Kindle or Kobo run on Linux or Android, offering full multitasking and app support but often at the cost of complexity and closed software. Microcontroller-based e-readers, by contrast, use lightweight chips that handle only essential tasks, enabling longer battery life, simpler interfaces, and easier hacking. The Xteink X4 is part of a growing movement toward open, single-purpose devices that prioritize a focused reading experience.

<details><summary>References</summary>
<ul>
<li><a href="https://www.xteink.com/products/xteink-x4">Xteink X 4 Pocket eReader</a></li>
<li><a href="https://hackaday.com/2025/08/03/open-source-flexible-e-reader/">Open-Source, Flexible E-Reader | Hackaday</a></li>
<li><a href="https://grokipedia.com/page/Xteink_X4">Xteink X4</a></li>

</ul>
</details>

**Discussion**: Users praise the X4 and X3 for their simplicity, openness, and the convenience of the WiFi HTTP server for book transfers, with some successfully modding the device with CrossPoint. Common wishes include a larger screen, a backlight, and stronger magnets, though many see it as a secondary, ultra-portable companion rather than a primary e-reader.

**Tags**: `#e-ink`, `#ereader`, `#microcontroller`, `#hardware`, `#open-source`

---

<a id="item-7"></a>
## [John Carmack Reflects on Early Management Mistakes at id Software](https://twitter.com/ID_AA_Carmack/status/2069799283369345247) ⭐️ 8.0/10

John Carmack publicly shared personal lessons about his management mistakes at id Software, admitting he pushed teams too hard, failed to adapt his style, and caused burnout, in a candid Twitter thread. Carmack's reflections provide rare, candid leadership lessons from a legendary figure, illustrating the trade-offs between creating groundbreaking products and maintaining a healthy, sustainable company culture. Carmack specifically admitted that the intense development of Quake 'gutted' id Software, and that he failed to realize growing companies need more slack than startups. Comments from Sandy Petersen and others provided contrasting viewpoints on the cost of that pressure.

hackernews · shadowtree · Jun 24, 15:56 · [Discussion](https://news.ycombinator.com/item?id=48661825)

**Background**: John Carmack is the co-founder of id Software and a legendary programmer known for pioneering 3D game engines behind iconic titles like Doom and Quake. id Software's early culture was defined by intense, crunch-heavy development that pushed technical boundaries. The company's transition from a small startup to a larger studio exposed tensions between Carmack's relentless drive for innovation and the need for sustainable management practices.

**Discussion**: The HN discussion was rich and nuanced: some comments praised Carmack's honesty, while others debated whether the creation of Quake justified the cost to the company. Sandy Petersen's firsthand accounts offered a counterpoint, and several users noted that id Software's post-Doom 2 decline was due to prioritizing technical feats over artistic design. Overall sentiment was respectful, with many acknowledging the complexity of leadership in high-pressure creative environments.

**Tags**: `#game development`, `#leadership`, `#management`, `#software engineering`, `#tech history`

---

<a id="item-8"></a>
## [Self-Play RL Agent Tops Generals.io Leaderboard with JAX and Vision Transformer](https://www.reddit.com/r/MachineLearning/comments/1uei2yg/i_made_a_superhuman_generalsio_agent_with/) ⭐️ 8.0/10

A developer trained a self-play reinforcement learning agent for the real-time strategy game Generals.io, achieving the #1 spot on the human 1v1 leaderboard. The breakthrough came from rewriting the entire pipeline in JAX and replacing the CNN with a Vision Transformer architecture. This demonstrates that modern ML infrastructure (JAX) and scalable architectures (Vision Transformers) can solve complex imperfect-information games without relying on hand-crafted domain knowledge. The open-source release and comprehensive guide provide a practical blueprint for RL practitioners building similar agents. The agent began as a master's thesis using behavior cloning and RL fine-tuning, but was consistently beaten by top players. The reimplementation adopted JAX’s high-performance array computation and a Vision Transformer, prioritizing scaling over human priors; the full pipeline, including a fast JAX simulator, is open source.

reddit · r/MachineLearning · /u/shrekofspeed · Jun 24, 16:18

**Background**: Generals.io is an online real-time strategy game with imperfect information (fog of war), where players command armies to capture territory. JAX is a Python library for high-performance numerical computing and machine learning, known for automatic differentiation and just-in-time compilation. A Vision Transformer (ViT) is a neural network architecture that divides images into patches and processes them with a transformer encoder, offering high capacity for visual tasks. Self-play reinforcement learning is a technique where an agent learns by playing against itself, famously used by AlphaGo.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/JAX_(software)">JAX (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer</a></li>

</ul>
</details>

**Tags**: `#reinforcement-learning`, `#self-play`, `#JAX`, `#vision-transformer`, `#game-ai`

---

<a id="item-9"></a>
## [DeepSWE: A Contamination-Free Benchmark for Evaluating Coding Agents](https://www.reddit.com/r/MachineLearning/comments/1ue0hlp/deepswe_new_benchmark_looking_at_how_well_todays/) ⭐️ 8.0/10

DeepSWE is a new benchmark that evaluates coding agents on software engineering tasks using hand-written verifiers, real-world complexity, and a contamination-free design. It spans 91 repositories in 5 languages and requires solutions with 5.5x more code than SWE-bench Pro. It addresses key weaknesses of existing benchmarks like SWE-bench by eliminating data contamination and focusing on realistic, multi-file engineering work. This gives a more accurate picture of how frontier AI coding agents perform in practice. Prompts are about half the length of SWE-bench Pro's, yet solutions require ~2x more output tokens. Verifiers test software behavior rather than implementation details, ensuring reliable evaluation even for creative solutions.

reddit · r/MachineLearning · /u/we_are_mammals · Jun 24, 02:03

**Background**: Existing software engineering benchmarks like SWE-bench use real GitHub issues and pull requests, which can lead to contamination if models have seen the solutions during training. Contamination-free benchmarks such as LiveBench create entirely new questions to avoid this problem. DeepSWE extends this approach by writing tasks from scratch and using behavior-based hand-written verifiers, ensuring a fair and realistic test of coding agents.

<details><summary>References</summary>
<ul>
<li><a href="https://www.swebench.com/">SWE - bench Leaderboards</a></li>
<li><a href="https://github.com/LiveBench/LiveBench">GitHub - LiveBench/LiveBench: LiveBench: A Challenging, Contamination-Free LLM Benchmark · GitHub</a></li>

</ul>
</details>

**Tags**: `#benchmarking`, `#code generation`, `#software engineering`, `#AI evaluation`, `#LLMs`

---

<a id="item-10"></a>
## [RubyLLM: A Versatile Ruby Framework for Multi-Provider AI Integration](https://rubyllm.com/) ⭐️ 7.0/10

RubyLLM has emerged as a popular open-source Ruby framework that simplifies working with multiple AI providers like OpenAI, Anthropic, and xAI, earning praise for its developer-friendly API. It fills a gap in the Ruby ecosystem for AI integration, enabling Ruby developers to easily switch between providers and potentially accelerating the development of Ruby-based AI applications. While praised for ease of use, the framework has limitations: caching doesn't work correctly for xAI due to completions API constraints, and the responses API was initially not natively supported, though a recent update may have added it. Retry logic can erase model history, complicating observability.

hackernews · doener · Jun 24, 14:41 · [Discussion](https://news.ycombinator.com/item?id=48660711)

**Background**: RubyLLM is a Ruby gem that provides a common interface for interacting with large language models from various providers. It aims to offer a simple, Rails-like developer experience, handling API nuances and allowing easy swapping of backends. The Ruby ecosystem has historically had fewer AI/ML libraries compared to Python, making RubyLLM a significant addition for Ruby developers building AI-powered applications.

**Discussion**: Community response is overwhelmingly positive, with many praising its ease of use and comparing it favorably to Vercel's AI framework. However, users highlight practical pain points: broken caching for xAI, missing native responses API support (possibly fixed), and retry logic that obscures observability. Some question whether it offers enough value over direct provider SDKs, while others eagerly await version 2.0.

**Tags**: `#ruby`, `#llm`, `#ai-framework`, `#developer-tools`, `#open-source`

---

<a id="item-11"></a>
## [Google Introduces Computer Use for Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) ⭐️ 7.0/10

Google announced that Gemini 3.5 Flash now supports computer use, allowing the AI model to interpret graphical user interfaces and perform actions like clicking and typing to automate tasks. This marks Google's entry into the AI agent computer-use race, competing with OpenAI's Operator and Anthropic's Claude Computer Use, but community feedback highlights significant reliability issues and missing features that may limit adoption. The feature is part of the Gemini 3.5 Flash model release. Google's blog claims performance gains, but community members note that the model gave up on simple data extraction tasks, lacks MCP support in the Gemini app, and has no coding agent equivalent to Codex or Claude Code.

hackernews · swolpers · Jun 24, 17:21 · [Discussion](https://news.ycombinator.com/item?id=48662999)

**Background**: Computer use in AI refers to the ability of a model to interpret screen content visually and simulate mouse and keyboard input to complete tasks across applications. OpenAI's Operator employs a Computer-Using Agent (CUA) model, and Anthropic's Claude offers similar capabilities. Gemini 3.5 Flash is a fast, cost-efficient model from Google DeepMind, part of the Gemini family of multimodal LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/">Gemini 3 . 5 : frontier intelligence with action</a></li>
<li><a href="https://openai.com/index/computer-using-agent/">Computer-Using Agent | OpenAI</a></li>

</ul>
</details>

**Discussion**: Community comments are overwhelmingly negative. Users report Gemini throwing errors and giving up on a simple table extraction task, lament the absence of MCP support and a coding agent tool, and criticize a benchmark graph that they claim misrepresents Gemini's performance. One commenter calls computer use a 'terrible idea'—slow, insecure, error-prone, and expensive.

**Tags**: `#gemini`, `#computer-use`, `#ai-agents`, `#google`, `#human-computer-interaction`

---

<a id="item-12"></a>
## [NVIDIA's 45°C Liquid Cooling Design Cuts Data Center Water Use to Near Zero](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 7.0/10

NVIDIA has introduced a liquid cooling architecture that operates at an inlet temperature of 45°C, enabling data centers to drastically reduce water consumption compared to traditional air-cooled or lower-temperature liquid-cooled systems. The design claims to eliminate water use entirely in favorable climates, sparking debate over its practical feasibility. This approach could significantly reduce the environmental impact of AI and HPC data centers, which are facing increasing scrutiny over water and energy usage. If proven, it may also enable waste heat integration with district heating networks, potentially turning data centers into net-positive community assets. The 45°C inlet temperature is warmer than typical liquid-cooled systems (often ~24°C) and allows the use of dry coolers instead of evaporative cooling towers, which consume water. However, the effectiveness depends on ambient climate, and the 'zero water' claim is contested because the recirculating coolant still requires initial fill and periodic makeup water, though at minimal levels.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Data centers traditionally use air conditioning or evaporative cooling to remove heat from servers, which can consume millions of gallons of water annually. Liquid cooling is more efficient because water transports heat better than air. Warm-water liquid cooling (e.g., up to 75°F/24°C) has been used in some HPC facilities to reduce energy, but NVIDIA's design raises the temperature further to 45°C (113°F), enabling heat rejection without water evaporation. District heating is a centralized system that distributes waste heat from industrial sources to buildings, and 45°C is a viable temperature for some low-temperature district heating loops.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/District_heating">District heating</a></li>
<li><a href="https://www.nrel.gov/computational-science/warm-water-liquid-cooling">High-Performance Computing Data Center Warm-Water Liquid Cooling | Computational Science | NLR</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the 'zero water consumption' claim, noting that recirculating water still comes from somewhere and requires makeup. Some highlighted the synergy with district heating, while others questioned the lack of technical details on performance in different climates, and pointed out that warm-water liquid cooling is not entirely new (e.g., NASA Ames facility).

**Tags**: `#liquid cooling`, `#data centers`, `#water conservation`, `#NVIDIA`, `#sustainability`

---

<a id="item-13"></a>
## [Nub: A Bun-like all-in-one toolkit for Node.js](https://github.com/nubjs/nub) ⭐️ 7.0/10

Nub, created by Colin McDonnell (creator of Zod), is a new toolkit that enhances Node.js with a fast transpiler based on oxc, module resolution hooks, and polyfills for APIs like Worker and Temporal, delivering a Bun-like developer experience while still using the stock Node.js runtime. Nub is significant because it allows Node.js developers to enjoy Bun-like speed and convenience—such as TypeScript transpilation and modern API polyfills—without abandoning the mature Node.js ecosystem, reducing migration risks and enabling incremental adoption. Nub uses a `--require` preload hook to inject its transpiler and hooks, which may have edge cases with ESM and top-level await; the transpiler is powered by oxc, a high-performance Rust-based tool, and is packaged as a Node-API add-on for speed. It injects polyfills for APIs like `Worker` and `Temporal` as needed, ensuring compatibility without replacing Node's standard library.

hackernews · colinmcd · Jun 24, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48660267)

**Background**: Bun is a fast, all-in-one JavaScript runtime that bundles a transpiler, package manager, and test runner, offering a streamlined developer experience. Node.js, the most widely used server-side JavaScript runtime, traditionally requires separate tools like ts-node for TypeScript. Nub bridges this gap by using a transpiler (powered by oxc, a high-performance Rust-based toolchain) and Node's module resolution hooks to add these capabilities directly to Node.js without changing the runtime.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>
<li><a href="https://nodejs.org/api/module.html">Modules : ` node : module ` API | Node . js v26.3.0 Documentation</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely positive, with many praising the idea and the credentials of creator Colin McDonnell (Zod). Some raised technical questions about the transpiler necessity given Node's native TypeScript support and the use of a `--require` hook, which may affect ESM and top-level await. One user reported successfully migrating a monorepo to Nub with zero issues, highlighting its speed and reliability.

**Tags**: `#Node.js`, `#TypeScript`, `#toolkit`, `#Bun`, `#oxc`

---

<a id="item-14"></a>
## [Simon Willison Converts MDN Browser Compatibility Data into SQLite Database](https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything) ⭐️ 7.0/10

Simon Willison built a new GitHub repo that transforms Mozilla's comprehensive browser-compat-data JSON dataset into a ~66MB SQLite database, using a script generated by Claude Code and the sqlite-utils library. The database is served via GitHub's raw content CDN with open CORS headers, enabling direct web-based querying through Datasette Lite. This provides developers with an offline-queryable, portable database of browser compatibility information, enabling easy integration into local tools, CI/CD pipelines, and web applications. The open CORS headers remove backend dependencies, allowing any web-based tool to query the data directly, which lowers the barrier for building browser-compat-aware features. The database is force-pushed to an orphan branch named 'db' to ensure CORS support on raw.githubusercontent.com; GitHub release assets lack these headers. The build workflow is automated via GitHub Actions, and the initial script was generated by Claude Code (Opus 4.8) while the workflow was built with Codex Desktop (GPT-5.5).

rss · Simon Willison · Jun 24, 23:59

**Background**: MDN's browser-compat-data is a community-maintained JSON dataset covering HTML, CSS, JavaScript, and Web API compatibility across browsers. sqlite-utils is a Python CLI tool by Simon Willison that simplifies importing JSON into SQLite. Claude Code is an AI-powered coding agent from Anthropic that can understand codebases and generate scripts. GitHub repositories support CORS for raw file access on the raw.githubusercontent.com domain, but release assets do not; this project uses an orphan branch to host the database file and make it queryable from the web.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/sqlite-utils">GitHub - simonw/sqlite-utils: Python CLI utility and library for manipulating SQLite databases · GitHub</a></li>
<li><a href="https://developer.mozilla.org/en-US/mcp">MDN MCP server</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#browser-compat`, `#sqlite`, `#web-development`, `#mdn`, `#open-data`

---

<a id="item-15"></a>
## [Tom MacWright: AI-generated resumes create accidental anonymity](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 7.0/10

Tom MacWright reports that he has seen job applications where the resume, portfolio, GitHub projects, and commit messages are all clearly generated by LLMs, resulting in candidates who appear anonymous and reveal nothing about their true personality. This trend could undermine the hiring process by making it hard for employers to evaluate candidates authentically, potentially leading to poor hiring decisions and eroding trust in application materials. The observation, published in June 2026, highlights that the 'perfected, generated, prompted' content strips away individuality, leaving candidates indistinguishable beyond their tool usage.

rss · Simon Willison · Jun 24, 18:13

**Background**: Large language models (LLMs) like GPT-4 can generate coherent text, code, and entire websites from prompts. In tech hiring, resumes and portfolios are meant to showcase unique skills and personality; automating them with AI raises concerns about authenticity. MacWright's term 'accidental anonymity' describes how AI tools can inadvertently erase the human element that employers rely on to assess candidates.

**Tags**: `#careers`, `#ai`, `#llm`, `#hiring`, `#ethics`

---

<a id="item-16"></a>
## [Datasette 1.0a35 adds Create and Alter Table UI and API](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a35, a major alpha release, introduces a new 'Create table' interface and JSON API for defining tables with columns, constraints, and foreign keys, as well as an 'Alter table' interface and API for modifying existing tables, including adding, renaming, and dropping columns and changing types. This update transforms Datasette from a read-only exploration tool into a more complete database management interface, enabling users to create and modify database schemas without leaving the tool. It is a significant step toward making SQLite more accessible for data management tasks and aligns with the trend of embedding admin features in developer-friendly tools. The new endpoints support custom column types, NOT NULL constraints, literal and expression defaults, primary keys, and foreign keys; the Alter table dialog also includes a 'Drop table' button. Additionally, the template context documentation is now a stable API for custom templates, generated from dataclass definitions and validated by tests.

rss · Simon Willison · Jun 23, 21:34

**Background**: Datasette is an open-source tool by Simon Willison that provides a web interface and JSON API for exploring and publishing SQLite databases. It is widely used for data journalism and rapid data exploration. Prior to this release, Datasette was primarily read-only, lacking built-in capabilities to create or modify tables, forcing users to rely on external tools like the sqlite3 command-line interface.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.datasette.io/en/stable/json_api.html">JSON API - Datasette documentation</a></li>
<li><a href="https://docs.datasette.cn/en/stable/json_api.html">JSON API - Datasette 文档</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#sqlite`, `#data-exploration`, `#open-source`, `#api`

---

<a id="item-17"></a>
## [HDD-RoPE: High-Dimensional Dynamic Rotary Positional Embedding Boosts Convergence](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 7.0/10

HDD-RoPE introduces a novel positional embedding that extends RoPE by grouping query/key vectors into larger chunks (e.g., size 4) and making rotations data-dependent, treating token position as multidimensional. On the TinyStories dataset, it shows faster convergence than the xPos baseline. This advancement could improve training efficiency and model performance for transformers, as positional embeddings are crucial for sequence modeling. By enabling multidimensional position learning, it may allow models to capture richer structural information like paragraphs or sentences, potentially leading to better language understanding. The method uses cumulative matrix products to handle rotations, and a chunk size of 4 corresponds to 6 rotational axes. The test architecture is a GPT-2-like model with 4 blocks and 768 hidden dimensions, trained on TinyStories, and the code and math are open-source.

reddit · r/MachineLearning · /u/mikayahlevi · Jun 24, 18:16

**Background**: Rotary Positional Embedding (RoPE) is a widely used method in transformers that encodes token positions by rotating query and key vectors in pairs, allowing the model to learn relative positions. xPos is an enhanced variant designed to improve length extrapolation. HDD-RoPE generalizes this by grouping features into larger chunks and making rotation amounts data-dependent, turning position into a multidimensional concept rather than a one-dimensional sequence index.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rotary_positional_embedding">Rotary positional embedding</a></li>
<li><a href="https://github.com/ggml-org/ggml/issues/441">Support for xPos positional embedding · Issue #441 · ggml-org/ggml</a></li>
<li><a href="https://github.com/jploski/RotaryEmbedding">GitHub - jploski/RotaryEmbedding: Comparison of RoPE and xPos positional embeddings used in LLMs</a></li>

</ul>
</details>

**Tags**: `#positional-embeddings`, `#transformers`, `#deep-learning`, `#NLP`, `#rotary-position-embedding`

---

<a id="item-18"></a>
## [LLM Inference Pricing Comparison Shows Caching Cost Disparities Across 7 Providers](https://www.reddit.com/r/MachineLearning/comments/1ueavxn/i_compiled_llm_inference_pricing_across_7/) ⭐️ 7.0/10

A Reddit user compiled public pricing data from 7 LLM inference providers, uncovering that cached input token costs can differ by tens of times between services. The comparison reveals that caching policy is often more important than base token pricing for cost-sensitive applications like agents and RAG pipelines, helping developers make more informed provider choices. The spreadsheet tracks input/output token pricing, context windows, cached input pricing, and supported models; the same model can cost several times more across providers, and caching documentation is often incomplete.

reddit · r/MachineLearning · /u/Technomadlyf · Jun 24, 11:28

**Background**: In LLM inference, caching stores intermediate computations (KV cache) from previous requests to avoid recomputing for repeated tokens, such as system prompts or conversation history. This significantly reduces latency and cost. Providers may offer different discounts for cached tokens, reflected in separate pricing tiers.

<details><summary>References</summary>
<ul>
<li><a href="https://machinelearningmastery.com/the-complete-guide-to-inference-caching-in-llms/">The Complete Guide to Inference Caching in LLMs - MachineLearningMastery.com</a></li>
<li><a href="https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/">Optimize LLM response costs and latency with effective caching | Amazon Web Services</a></li>

</ul>
</details>

**Tags**: `#LLM pricing`, `#inference`, `#caching`, `#cost comparison`, `#spreadsheet`

---

<a id="item-19"></a>
## [Bunny.net Makes Bunny DNS Free with No Query Limits](https://bunny.net/blog/were-making-bunny-dns-free/) ⭐️ 6.0/10

Bunny.net has eliminated all DNS query fees and now offers free DNS hosting for up to 500 domains per account, including smart records and health monitoring, with no query limits. This move positions Bunny as a competitive European alternative to Cloudflare's free DNS service, appealing to users seeking EU-based infrastructure amid geopolitical concerns. It also lowers the barrier for individuals and small teams to use a scriptable DNS platform with global anycast. The free tier includes smart records and health monitoring, but the community notes that the spending cap feature (e.g., block requests after a certain bill) is only available for Bunny CDN, not other products like Bunny DNS, raising concerns about unexpected costs from traffic spikes.

hackernews · dabinat · Jun 24, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48657030)

**Background**: Bunny.net is a European CDN and DNS provider, known for its scriptable DNS platform with global anycast network. It competes with larger providers like Cloudflare, which also offers free DNS services. The company received a small $6 million funding round in 2022 and operates organically without heavy loss-leader strategies. This announcement makes their DNS hosting free, similar to Cloudflare's model, but with a European base.

<details><summary>References</summary>
<ul>
<li><a href="https://bunny.net/dns/">Bunny DNS | The #1 Scriptable DNS Platform | bunny.net</a></li>

</ul>
</details>

**Discussion**: The HN community had mixed reactions. Some praised Bunny as a welcome EU-based alternative to Cloudflare, especially given geopolitical tensions. Others noted the company's organic growth model and lack of loss-leader features. Several commenters expressed concerns about the lack of spending caps on DNS services, fearing unexpected bills from automated traffic, and criticized the unclear messaging on the announcement page.

**Tags**: `#DNS`, `#free`, `#CDN`, `#infrastructure`, `#cloud`

---

<a id="item-20"></a>
## [Elastic Lays Off 7% of Workforce in AI-Driven Reorganization](https://www.elastic.co/blog/ceo-ash-kulkarni-announcement-to-elastic-employees) ⭐️ 6.0/10

Elastic announced a layoff of 7% of its employees, citing advances in AI and automation as the reason for restructuring its workforce. The company plans to simplify its structure and increase hiring in go-to-market roles. This reflects a growing trend where tech companies use AI to justify job cuts, raising concerns about employment stability and the normalization of layoffs. The discussion highlights the shifting norms in the tech industry, where layoffs are no longer seen as a sign of failure. The CEO's blog post emphasized future growth and hiring for go-to-market positions, but did not provide details on severance packages. The SEC filing also mentions headcount increases in go-to-market roles.

hackernews · dakrone · Jun 24, 21:57 · [Discussion](https://news.ycombinator.com/item?id=48666100)

**Background**: Elastic is a search software company best known for Elasticsearch, an open-source search and analytics engine. AI-driven reorganization refers to the company's strategy of leveraging automation and AI to streamline operations, a trend seen across the tech industry. This approach often involves reducing roles that can be automated while expanding customer-facing teams. Such layoffs are part of a broader pattern where tech firms adjust headcount to focus on AI and cloud services.

**Discussion**: Commenters expressed sadness over the normalization of layoffs, noting they were once a sign of failure. Some criticized the company's framing of AI-driven cuts while planning to hire in other areas, and debated AI's uneven impact on big vs. small firms.

**Tags**: `#layoffs`, `#tech-industry`, `#ai-impact`, `#business`, `#hackernews`

---

<a id="item-21"></a>
## [Blog Post Argues Copying Designs Is a Skill, Sparks Ethical Debate](https://ben-mini.com/2026/stealing-is-a-skill) ⭐️ 6.0/10

A blog post titled 'Stealing Is a Skill' claimed that methodically copying others' designs is a valuable creative learning process, sparking a lively debate among web designers and developers. The discussion highlights the tension between learning through imitation and the ethical boundaries of copying for commercial work, reflecting broader concerns about design originality and homogeneity in the web industry. Community reactions were mixed: some compared it to the copywork exercise in writing, while others criticized the ethics of copying without permission and lamented the blandness of modern web design. The post's argument is opinion-based rather than a technical breakthrough.

hackernews · bewal416 · Jun 24, 13:08 · [Discussion](https://news.ycombinator.com/item?id=48659165)

**Background**: Copywork is a traditional exercise in writing where students transcribe the works of great authors to internalize style and technique. In design, similar practices of recreating existing works for study are common, but the line between learning and plagiarism is often debated. The modern web has seen a trend toward minimalist, template-driven design, which some see as diluting creativity. The post reignites debates about originality and the 'blandness' of contemporary web aesthetics.

**Discussion**: Some likened the approach to 'copywork' used by writers, viewing it as a legitimate learning method. Others strongly disagreed, arguing that copying a finished design does not convey the creator's underlying process and that commercial copying without permission crosses an ethical line. The debate also touched on the broader perception of bland, template-driven web design.

**Tags**: `#web design`, `#copying`, `#creativity`, `#ethics`, `#front-end development`

---

<a id="item-22"></a>
## [Papers with Code Launches OCR Benchmark Overview with New Baidu and Mistral Models](https://www.reddit.com/r/MachineLearning/comments/1ueiam6/find_the_best_opensource_ocr_models_in_one_place/) ⭐️ 6.0/10

Papers with Code released a curated overview of top open-source OCR models and benchmarks, highlighting recent releases: Baidu’s Unlimited OCR (3B parameters, with Reference Sliding Window Attention) and Mistral OCR 4. This resource helps developers and enterprises quickly identify the best OCR model for converting documents into machine-readable formats, which is crucial for powering agentic RAG applications and AI agents. The page recommends OlmOCRBench and OmniDocBench as key benchmarks, and lists Chandra OCR 2 and Mistral OCR v4 as top performers; Baidu’s model innovates on DeepSeek OCR with R-SWA.

reddit · r/MachineLearning · /u/NielsRogge · Jun 24, 16:26

**Background**: OCR (Optical Character Recognition) is the task of digitizing text from images or PDFs. Agentic RAG (Retrieval-Augmented Generation) uses AI agents to retrieve and generate answers from unstructured data, often requiring documents in standardized formats like Markdown. Papers with Code is a platform that tracks machine learning benchmarks and code.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-rag">What is Agentic RAG? | IBM</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#benchmarks`, `#open-source`, `#document-ai`, `#paperswithcode`

---

<a id="item-23"></a>
## [MuJoFil: A GPU-Native Simulator for Vision-Based RL with Newton Physics and Filament Rendering](https://www.reddit.com/r/MachineLearning/comments/1uemrch/mujoco_derived_simulator_for_high_fidelity_vision/) ⭐️ 6.0/10

A developer has introduced MuJoFil, an open-source simulator that combines Nvidia's GPU-native Newton physics engine (derived from MuJoCo) with a modified Google Filament renderer to enable highly parallelized, high-fidelity vision-based reinforcement learning training directly on the GPU. Current GPU-accelerated MuJoCo variants like MJX lack robust support for vision-based RL pipelines, and alternatives like NVIDIA Isaac require expensive hardware and licenses. MuJoFil aims to fill this gap with an open-source, accessible solution that can leverage any online 3D environment, potentially democratizing vision-based robot learning. The simulator is available in two variants: a CPU-based version (pip install mujofil) and a CUDA-enabled GPU-native version (pip install mujofil-warp). It supports PBR textures, GLB, OpenUSD, and other environment formats, and the developer is actively seeking feedback before making the repository public.

reddit · r/MachineLearning · /u/MT1699 · Jun 24, 19:07

**Background**: MuJoCo is a widely used open-source physics engine for robotics and machine learning research. MJX is a GPU-accelerated version of MuJoCo but focuses on physics and lacks native vision rendering. Google Filament is a real-time physically based rendering engine, while Nvidia's Newton physics engine is a GPU-native derivative of MuJoCo's physics. MuJoFil merges Newton and a heavily modified Filament to render multiple simulations in parallel on the GPU, targeting vision-based policy training.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MuJoCo">MuJoCo - Wikipedia</a></li>
<li><a href="https://mujoco.readthedocs.io/en/stable/mjx.html">MuJoCo XLA (MJX) - MuJoCo Documentation</a></li>
<li><a href="https://github.com/google/filament">GitHub - google/filament: Filament is a real-time physically based rendering engine for Android, iOS, Windows, Linux, macOS, and WebGL2 · GitHub</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#simulation`, `#robotics`, `#GPU computing`, `#machine learning`

---

<a id="item-24"></a>
## [Production ML Models Often Skip Security Testing for Extraction and Poisoning](https://www.reddit.com/r/MachineLearning/comments/1uddtws/are_model_security_risks_extraction_poisoning/) ⭐️ 6.0/10

A Reddit user reports that many ML teams deploy models without any adversarial testing for model extraction and poisoning risks, and asks whether others are actually conducting such security reviews in production. This highlights a significant gap in MLOps security compared to traditional software security reviews, potentially leaving models vulnerable to intellectual property theft and data integrity attacks as ML becomes more deeply embedded in critical systems. The post specifically mentions model extraction (stealing model functionality via API queries) and model poisoning (injecting malicious data into training), and notes that adversarial testing—systematically evaluating models with malicious inputs—is often skipped entirely before deployment.

reddit · r/MachineLearning · /u/Xorphian · Jun 23, 10:52

**Background**: Model extraction attacks allow an adversary with query access to replicate a model's functionality by sending many inputs and using the outputs to train a clone. Model poisoning attacks corrupt a model's behavior by manipulating training data, either during initial training or retraining. Adversarial testing is a security practice that probes models with crafted adversarial inputs to uncover vulnerabilities, but it is not yet a standard part of MLOps pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://www.praetorian.com/blog/stealing-ai-models-through-the-api-a-practical-model-extraction-attack/">Stealing AI Models Through the API: A Practical Model Extraction Attack | Praetorian</a></li>
<li><a href="https://medium.com/@AT24/data-integrity-model-poisoning-tryhackme-12859f52f8ae">Data Integrity & Model Poisoning | Tryhackme | by Aaron | Medium</a></li>
<li><a href="https://developers.google.com/machine-learning/guides/adv-testing">Adversarial Testing for Generative AI | Machine Learning | Google for Developers</a></li>

</ul>
</details>

**Tags**: `#machine learning security`, `#adversarial testing`, `#model extraction`, `#model poisoning`, `#production ML`

---