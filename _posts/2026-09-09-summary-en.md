---
layout: default
title: "Horizon Summary: 2026-09-09 (EN)"
date: 2026-09-09
lang: en
---

> From 33 items, 23 important content pieces were selected

---

1. [OpenAI Claims Proof of Navier-Stokes Millennium Problem](#item-1) ⭐️ 10.0/10
2. [AlphaGenome Atlas: a high-resolution map of human DNA](#item-2) ⭐️ 9.0/10
3. [NeurIPS desk-rejected 178 papers for being AI-generated, detector flagged chairs&\#x27; own papers](#item-3) ⭐️ 9.0/10
4. [Meta Launches Muse, Personal AI Agent with Prompt Injection Defenses](#item-4) ⭐️ 8.0/10
5. [Kimi K3 \(2.8T\) runs at 1 token/s on a MacBook Pro using four SSDs](#item-5) ⭐️ 8.0/10
6. [Terence Tao Warns AI Is Rapidly Depleting Open Math Problems](#item-6) ⭐️ 8.0/10
7. [Interactive Tool Visualizes LLM Attention Mechanisms](#item-7) ⭐️ 8.0/10
8. [Terence Tao Warns AI Could Reverse Open Science Tradition](#item-8) ⭐️ 8.0/10
9. [Rustuna: Official High-Performance Rust Port of Optuna Hyperparameter Optimization Library](#item-9) ⭐️ 8.0/10
10. [KV Cache as an Agent Runtime: A New Approach to Interactive LLMs](#item-10) ⭐️ 8.0/10
11. [Qwen3.8 27B Quantization: 4-bit Holds Strong, 1-bit Collapses](#item-11) ⭐️ 7.0/10
12. [GitHub skill &\#x27;I-have-ADHD&\#x27; tackles Claude&\#x27;s verbosity in coding agents](#item-12) ⭐️ 7.0/10
13. [Mercury 2.5: Diffusion-Based LLM Hits 1100 Tokens/Sec for Low-Latency Inference](#item-13) ⭐️ 7.0/10
14. [OpenAI releases ChatGPT Images 2.5 with improved instruction-following](#item-14) ⭐️ 7.0/10
15. [Abusive Crawlers Consume More CPU on git.kernel.org Than Legitimate Use](#item-15) ⭐️ 7.0/10
16. [OpenAI Chief Scientist: Build Powerful AI for Defense, but Avoid Recklessness](#item-16) ⭐️ 7.0/10
17. [Generating Bad Apple from a Single Initial State with a 417k-Parameter Recurrent System](#item-17) ⭐️ 7.0/10
18. [LLM-Guided Program Evolution Breaks 10 Packomania Records](#item-18) ⭐️ 7.0/10
19. [DIY Printer Uses E-Ink Display Instead of Paper](#item-19) ⭐️ 6.0/10
20. [DaVinci Resolve 21.1 Release Sparks Discussion on Free Upgrades and Linux Codec Issues](#item-20) ⭐️ 6.0/10
21. [Simon Willison Builds Browser-Based Video Compressor Using Claude Fable 5.1](#item-21) ⭐️ 6.0/10
22. [Reddit User Seeks Debugging Strategies for Silent ML Pipeline Failures](#item-22) ⭐️ 6.0/10
23. [Practical Radar Object Classification with Histogram MLP: Ablation Studies and Insights](#item-23) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Claims Proof of Navier-Stokes Millennium Problem](https://www.reddit.com/r/MachineLearning/comments/1wavdi7/openal_says_it_has_cracked_one_of_maths/) ⭐️ 10.0/10

OpenAI announced that its internal AI system has produced a proof for the Navier-Stokes existence and smoothness problem, demonstrating that solutions can develop a singularity in finite time, and shared a formalization in the Lean proof assistant. This is one of the seven unsolved Millennium Prize Problems. If verified, it would be only the second ever solved and the first achieved with substantial AI assistance, marking a paradigm shift in mathematical research and the role of AI in scientific discovery. The proof has not been externally verified by mathematicians or the Clay Mathematics Institute. OpenAI stated it would decline the $1 million prize. A priority dispute involves Levent Alpöge \(Anthropic\) and Tristan Buckmaster, who derived related results on the Euler equations. The method built upon Cordoba and Zoroa&\#x27;s 2023 blowup proof for related fluid equations. The internal model was reportedly trained for under two weeks and is claimed to be more than twice as capable in mathematics as Astra.

reddit · r/MachineLearning · /u/Shizuka\_Kuze · Sep 8, 17:42

**Background**: The Navier-Stokes equations describe fluid motion and are central to understanding turbulence. The Clay Mathematics Institute listed the existence and smoothness problem among its seven Millennium Prize Problems in 2000, offering a $1 million prize. The challenge is to prove that smooth solutions always exist in three dimensions, or find a counterexample. Only the Poincaré conjecture has been officially solved so far. Lean is a proof assistant used to formally verify mathematical arguments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**Discussion**: Fields Medalist Terence Tao warned that AI could “flatten” research prematurely, discouraging early sharing of ideas. Comments also raised the priority dispute and speculation about whether the proof built on unpublished work. Some praised the stunning speed of model improvement \(doubling Astra’s capability in two weeks\) but wished such breakthroughs were pursued under public control rather than by a private company.

**Tags**: `#ai`, `#mathematics`, `#navier-stokes`, `#millennium-problems`, `#openai`

---

<a id="item-2"></a>
## [AlphaGenome Atlas: a high-resolution map of human DNA](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/) ⭐️ 9.0/10

DeepMind released AlphaGenome Atlas, a comprehensive database predicting the molecular effects of all 9 billion possible single-nucleotide variants in the human genome. This resource enables researchers to rapidly assess the functional impact of any DNA change, accelerating the discovery of disease-causing mutations and the development of targeted therapies. The atlas covers both coding and non-coding regions, including promoter sequences, and provides variant effect scores based on a deep learning model trained on functional genomics data.

hackernews · utiiiD · Sep 8, 14:55 · [Discussion](https://news.ycombinator.com/item?id=49611251)

**Background**: The human genome consists of 3 billion base pairs. A single-nucleotide variant \(SNV\) is a change in a single DNA letter. While coding variants can alter protein sequences, most disease-associated variants lie in non-coding regions that regulate gene expression. Deep learning models like AlphaGenome learn to predict functional effects from DNA sequence data, building on DeepMind&\#x27;s earlier AlphaFold breakthroughs in protein structure prediction.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/">AlphaGenome Atlas: Molecular predictions for 9 Billion human DNA ...</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/">Introducing AlphaGenome Atlas - The Keyword</a></li>

</ul>
</details>

**Discussion**: Community members inquired about promoter sequence coverage, practical use with direct-to-consumer genetic data, and the model&\#x27;s impact compared to other tools. Some expressed cautious optimism, noting that not all DeepMind biology models have had lasting impact, while others praised the open access.

**Tags**: `#genomics`, `#deepmind`, `#AI`, `#bioinformatics`, `#DNA`

---

<a id="item-3"></a>
## [NeurIPS desk-rejected 178 papers for being AI-generated, detector flagged chairs&\#x27; own papers](https://www.reddit.com/r/MachineLearning/comments/1wakf62/neurips_deskrejected_178_papers_for_being/) ⭐️ 9.0/10

NeurIPS used the proprietary Pangram AI detector to desk-reject 178 position papers without any human review or appeal, and independent tests showed the same detector flagged the track chairs&\#x27; own papers at 24% to 69% AI-generated probability. This controversy exposes the unreliability of AI detection tools in academic gatekeeping, disproportionately affects non-native English speakers, and damages trust in the fairness of top-tier conference review processes. The detector initially flagged 42.7% of all submissions as 90–100% AI before the team narrowed text windows to reduce the rate to 12.7%; 22 papers were rejected solely because authors denied AI use despite a score above 0.5, and a Stanford study showed 61% of human-written TOEFL essays by non-native speakers are falsely flagged as AI.

reddit · r/MachineLearning · /u/tughanbulut · Sep 8, 10:19

**Background**: NeurIPS is a top machine learning conference; its position paper track accepts novel viewpoints rather than full empirical results. AI detectors like Pangram use statistical patterns to guess text authorship, but they are known for high false positive rates, especially on formal, non-native English writing. The term &\#x27;circularity trap&\#x27; refers to the detector&\#x27;s score being used as proof that an author lied about AI use, creating a self-reinforcing cycle.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pangram_%28AI_detector%29">Pangram (AI detector)</a></li>
<li><a href="https://timrequarth.substack.com/p/why-you-shouldnt-trust-ai-detector">The Problem with AI Detector Companies - by Tim Requarth</a></li>

</ul>
</details>

**Discussion**: The Reddit thread garnered over 500 upvotes and extensive discussion, with overwhelming outrage. Many commenters pointed out that the detector&\#x27;s lack of transparency and the absence of appeal are unacceptable, and the fact that chairs&\#x27; own papers were flagged invalidates the entire process. Some highlighted the irony of using AI to police AI, and ESL researchers shared fears of being unfairly targeted.

**Tags**: `#machine learning`, `#AI detection`, `#academic integrity`, `#NeurIPS`, `#conference ethics`

---

<a id="item-4"></a>
## [Meta Launches Muse, Personal AI Agent with Prompt Injection Defenses](https://ai.meta.com/muse/) ⭐️ 8.0/10

Meta has launched Muse, a personal AI agent integrated into its ecosystem of apps. The launch emphasized security measures against prompt injection, with a layered defense strategy described by engineering lead David Singleton. With Meta&\#x27;s vast user base, Muse could become a mainstream AI interface, raising significant privacy and data harvesting concerns. The focus on prompt injection defenses highlights the industry&\#x27;s growing security challenges as AI agents gain more access to personal data. David Singleton detailed a layered defense: the model is trained to resist injection, the harness marks untrusted sources, deterministic code checks outputs, and an ensemble of classifiers runs in an inaccessible environment. This shows a multi-pronged approach to mitigate prompt injection risks.

hackernews · yks · Sep 8, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49615537)

**Background**: Prompt injection is a cybersecurity exploit where adversarial prompts manipulate large language models to bypass safeguards and execute unintended actions. With web browsing and file upload capabilities, AI agents are vulnerable to indirect prompt injection, where malicious content is embedded in websites or documents. Meta&\#x27;s layered defenses aim to address this threat by combining model training, input validation, and output verification.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://grokipedia.com/page/prompt-injection">Prompt injection</a></li>

</ul>
</details>

**Discussion**: The community is divided: some see Meta targeting casual users who are less aware of AI nuances, while others praise the technical depth of prompt injection defenses. Many express distrust of Meta&\#x27;s privacy practices, with some planning to build their own agents to avoid data harvesting. Creative use cases like scraping Facebook groups were also noted.

**Tags**: `#AI`, `#Meta`, `#personal-agent`, `#prompt-injection`, `#user-experience`

---

<a id="item-5"></a>
## [Kimi K3 \(2.8T\) runs at 1 token/s on a MacBook Pro using four SSDs](https://github.com/argonautlabsai/deltafin) ⭐️ 8.0/10

A developer demonstrated running the 2.8 trillion-parameter Kimi K3 language model on a MacBook Pro by streaming its weights from four external SSDs, achieving a speed of 1 token per second. This hack shows that even the largest open-weight models can be run on consumer-grade hardware with sufficient storage bandwidth, pushing the boundaries of local inference and potentially democratizing access to frontier AI for experimentation. The setup streams model weights from four SSDs \(likely via Thunderbolt\) to the MacBook&\#x27;s unified memory, yielding 1 token/s inference—far too slow for interactive use, but proving the viability of SSD-based weight streaming for enormous models.

hackernews · Argonautlabs · Sep 8, 20:07 · [Discussion](https://news.ycombinator.com/item?id=49616257)

**Background**: Kimi K3 is a 2.8 trillion-parameter open-weight large language model from Moonshot AI, released in July 2026, and is the largest open model ever. Running such a model typically requires a cluster of datacenter GPUs with hundreds of gigabytes of VRAM. SSD offloading for LLM inference is a technique where model weights are kept on fast SSDs and streamed into compute memory on demand, enabling inference on hardware with limited RAM. This demonstration takes that concept to an extreme by using consumer SSDs and a laptop.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://www.kimi.ai/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://www.lynxdigital.com/kb/ai/ollm">oLLM: SSD Offloading for Large-Context Inference</a></li>

</ul>
</details>

**Discussion**: The community reacted with humor and admiration, comparing the slow inference to the fictional Deep Thought computer and joking that a medium prompt would take 11 days; some also noted that Apple&\#x27;s soldered RAM makes SSD offloading necessary, and a few asked for technical details on the SSD connection method.

**Tags**: `#LLM`, `#local-inference`, `#MacBook`, `#SSD`, `#model-streaming`

---

<a id="item-6"></a>
## [Terence Tao Warns AI Is Rapidly Depleting Open Math Problems](https://mathstodon.xyz/@tao/117237320796901560) ⭐️ 8.0/10

Terence Tao posted on Mathstodon that AI models are solving open math problems at an unprecedented pace, turning the discovery of promising new problems into the scarce resource. His warning follows multiple AI-generated results on the Navier-Stokes equations within 24 hours. This insight shifts the focus in mathematical research from solving problems to creatively identifying them, potentially transforming the role of human mathematicians. It raises concerns that short-term solution extraction by AI could undermine the long-term health of the mathematical ecosystem. The warning was prompted by a flurry of AI results on Navier-Stokes within a single day, demonstrating that AI can now tackle problems once reserved for human insight. Tao cautions that indiscriminate use of such tools may achieve immediate goals but erode the foundation for future progress.

hackernews · \_alternator\_ · Sep 8, 21:00 · [Discussion](https://news.ycombinator.com/item?id=49616968)

**Background**: Terence Tao is a Fields Medal-winning mathematician renowned for his work in harmonic analysis, partial differential equations, and other areas. Open mathematical problems are unsolved questions that have resisted solution for years or decades, such as the Navier-Stokes existence and smoothness problem, one of the seven Millennium Prize Problems. Recent advances in AI, including large language models and formal proof assistants, have begun to produce verifiable solutions to some of these problems.

**Discussion**: Commenters debated whether AI solutions without human insight are valuable; some argued that the finite nature of open problems is overstated, while others suggested that the next frontier is asking novel questions. Concerns were raised about short-term extraction harming the research ecosystem, echoing Tao&\#x27;s own warning.

**Tags**: `#mathematics`, `#AI`, `#research`, `#automation`, `#Terence Tao`

---

<a id="item-7"></a>
## [Interactive Tool Visualizes LLM Attention Mechanisms](https://ishamf.dev/p/llm-attention-visualizer/) ⭐️ 8.0/10

A new interactive web-based tool has been released that allows users to see how attention layers in large language models combine information from multiple phrases, making the attention mechanism intuitively understandable. This tool demystifies a core component of LLMs, making it easier for students, educators, and practitioners to grasp how attention works, which is essential for interpreting model behavior and advancing AI literacy. The visualization uses vector magnitudes to represent influence, though one commenter noted that this assumption may be overly simplistic. The tool is client-side, easy to share, and has been praised for its clarity, but some concern was raised about later-layer attention being potentially obscured by contributions from earlier layers.

hackernews · ifz · Sep 8, 16:59 · [Discussion](https://news.ycombinator.com/item?id=49613068)

**Background**: The attention mechanism is a technique in deep learning that allows models to dynamically focus on the most relevant parts of an input sequence. It is the foundation of the Transformer architecture and powers models like GPT-4. By visualizing how attention weights are distributed across phrases, users can gain insight into how LLMs process and integrate information from different parts of a prompt.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Attention_%28machine_learning%29">Attention (machine learning) - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/attention-mechanism">What is an attention mechanism? | IBM</a></li>

</ul>
</details>

**Discussion**: Overall sentiment was very positive, with a teacher exclaiming it was perfect timing for a Friday class and another user calling it the clearest example they had seen. However, a critical view questioned the simplistic use of vector magnitude as a proxy for influence, and another commenter wondered if later-layer attention gets drowned out by earlier layers. The discussion balanced appreciation with constructive methodological scrutiny.

**Tags**: `#LLM`, `#attention-mechanism`, `#visualization`, `#machine-learning`, `#education`

---

<a id="item-8"></a>
## [Terence Tao Warns AI Could Reverse Open Science Tradition](https://simonwillison.net/2026/Sep/9/terence-tao/) ⭐️ 8.0/10

Terence Tao, a Fields Medalist mathematician, warned that AI systems capable of rapidly solving open problems upon hearing rumors of human interest could discourage researchers from sharing promising research directions, threatening centuries of open science tradition. This warning underscores a potential chilling effect on scientific collaboration: if AI can preemptively solve problems, researchers may become secretive, reversing the open sharing that has been fundamental to progress in mathematics and other fields. Tao noted that the pool of good open problems is being mined non-renewably, and even rumors of a researcher working on a problem can trigger massive AI-powered efforts to solve it before the original project reaches its full potential.

rss · Simon Willison · Sep 9, 00:20

**Background**: Terence Tao is a renowned mathematician and Fields Medalist known for contributions to harmonic analysis, partial differential equations, and other areas. Open problems are unsolved mathematical questions that researchers share publicly to stimulate collaboration and progress. Open science is the movement to make scientific research accessible to all, which has been central to how mathematics has advanced for centuries.

**Tags**: `#ai-ethics`, `#mathematics`, `#open-science`, `#ai-impact`, `#research-culture`

---

<a id="item-9"></a>
## [Rustuna: Official High-Performance Rust Port of Optuna Hyperparameter Optimization Library](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 8.0/10

The Optuna team has released Rustuna, an official Rust reimplementation of the widely used Optuna hyperparameter optimization framework. It delivers faster execution, lower memory footprint, and zero Python dependencies for improved security. This official port provides a memory-safe, high-performance alternative for ML practitioners who need fast hyperparameter tuning without the overhead or supply chain risks of Python dependencies. Long-term support from the Optuna team ensures it will become a trusted tool in the Rust ML ecosystem. Rustuna maintains API compatibility with Optuna, allowing users to leverage existing knowledge. Its zero Python dependency design eliminates the risk of supply chain attacks, and native Rust memory management reduces resource usage. The source code is available on GitHub, with details in a Medium blog post.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is an open-source Python library for automatic hyperparameter tuning, created by Preferred Networks in 2018. It allows machine learning engineers to efficiently search for the best model configurations. Rust is a systems programming language known for its memory safety and high performance, making it an attractive choice for optimization workloads. Rustuna brings together Optuna&\#x27;s proven tuning algorithms with Rust&\#x27;s speed and security, catering to production environments where Python&\#x27;s footprint may be undesirable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optuna">Optuna</a></li>
<li><a href="https://optuna.org/">Optuna - A hyperparameter optimization framework</a></li>

</ul>
</details>

**Tags**: `#hyperparameter-optimization`, `#Rust`, `#machine-learning`, `#Optuna`, `#performance`

---

<a id="item-10"></a>
## [KV Cache as an Agent Runtime: A New Approach to Interactive LLMs](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

A Yandex research team has published a blog post presenting their work on modifying the KV cache — the inference state of LLMs — to act as an agent runtime, enabling interactive systems. The post references prior papers Hogwild\! Inference and AsyncReasoning, and includes a preview of a Qwen3.8-27B model playing DOOM using this technique. This approach highlights an underexplored axis of agent capabilities: inference runtime design. By treating the KV cache as a mutable runtime, it could enable more responsive and efficient AI agents without expensive model retrofits, potentially changing how interactive AI systems are built. The technique leverages parallel LLM inference methods like Hogwild\! Inference, which uses concurrent attention with shared KV cache and Rotary Position Embeddings \(RoPE\) to avoid recomputation. The future work preview shows a Qwen3.8-27B agent playing DOOM interactively, demonstrating real-time control.

reddit · r/MachineLearning · /u/\_puhsu · Sep 7, 09:03

**Background**: The KV cache is a standard optimization in transformer models that stores key and value vectors from previous tokens during autoregressive generation, avoiding recomputation and speeding up inference. In agent systems, the &\#x27;harness&\#x27; is the external framework that manages the model&\#x27;s actions and environment; changing the model is often too costly. The newly proposed idea treats the KV cache as a dynamic runtime state, allowing the agent&\#x27;s behavior to be modified without altering the model weights. Hogwild\! Inference, a prior work, enables multiple workers to share the attention cache for parallel generation, demonstrating the flexibility of the KV cache.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>
<li><a href="https://eqimp.github.io/hogwild_llm/">Hogwild ! Inference</a></li>
<li><a href="https://arxiv.org/abs/2504.06261">Hogwild ! Inference : Parallel LLM Generation via Concurrent Attention</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#LLM`, `#agents`, `#KV cache`, `#inference optimization`

---

<a id="item-11"></a>
## [Qwen3.8 27B Quantization: 4-bit Holds Strong, 1-bit Collapses](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) ⭐️ 7.0/10

A new benchmark of the Qwen3.8 27B language model shows that 4-bit quantization nearly retains full performance, but 2-bit quantization causes a noticeable decline and 1-bit quantization leads to a complete collapse in accuracy. This finding confirms that aggressive 4-bit quantization makes a 27-billion-parameter model viable on consumer hardware with minimal quality loss, guiding practitioners on safe quantization levels for real-world deployment. The benchmark used Wilson 95% confidence intervals, which represent statistical uncertainty but not run-to-run variability, as commented by a user. The test also revealed a performance gap at 3-bit quantization, a critical breakpoint for sub-16GB GPUs like the RTX 5080 and 5070 Ti.

hackernews · stared · Sep 8, 14:49 · [Discussion](https://news.ycombinator.com/item?id=49611128)

**Background**: Quantization is a model compression technique that reduces memory footprint by using lower-precision numbers for weights \(e.g., 4-bit integers instead of 16-bit floats\), enabling large language models to run on consumer GPUs with limited VRAM. Qwen3.8 27B is an open-weight 27-billion-parameter model from Alibaba, popular for coding and reasoning tasks. The benchmark assessed how different quantization levels \(8-bit down to 1-bit\) affect reasoning performance.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/ Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**Discussion**: The community welcomed the benchmark, with users noting that 4-bit quantization is practical for local deployment. One commenter clarified that the reported confidence intervals do not reflect run-to-run variation. Others highlighted interest in KV cache quantization and the importance of Q3 performance for 16GB GPUs. Some users discussed the model&\#x27;s ability to &\#x27;think more&\#x27; to compensate for quantization loss, and a newcomer asked about safe local execution.

**Tags**: `#quantization`, `#LLM`, `#benchmark`, `#Qwen`, `#model-compression`

---

<a id="item-12"></a>
## [GitHub skill &\#x27;I-have-ADHD&\#x27; tackles Claude&\#x27;s verbosity in coding agents](https://github.com/ayghri/i-have-adhd) ⭐️ 7.0/10

A new GitHub repository offers a skill called &\#x27;i-have-adhd&\#x27; that instructs coding agents like Claude to be concise, preventing them from burying answers in unnecessary verbosity. The project gained attention on Hacker News, where users discussed Claude&\#x27;s verbose writing flaws in 242 comments. This addresses a widespread pain point with LLM coding assistants, especially Claude, whose verbosity wastes time and hampers productivity. The lightweight, open-source prompt engineering solution empowers developers to get straight to the point, potentially influencing tooling and model behavior. The skill is a simple CLAUDE.md or AGENTS.md instruction that tells the agent it has ADHD and must be concise. Users report that the effect often fades after a few turns, requiring repeated reminders or hooks, and the repository provides installation instructions for various coding agent platforms.

hackernews · domhudson · Sep 8, 14:13 · [Discussion](https://news.ycombinator.com/item?id=49610631)

**Background**: LLM-based coding agents like Claude Code and Cursor have become popular for software development, but Claude&\#x27;s responses are often criticized for being overly verbose, using unnecessary phrases like &\#x27;I did not edit...&\#x27; and burying key information. The community has developed various prompt engineering &\#x27;skills&\#x27; stored in configuration files to guide the model, though newer model versions sometimes override these instructions. The &\#x27;i-have-adhd&\#x27; skill is a humorous but effective attempt to enforce brevity by simulating a condition that demands concise communication.

**Discussion**: The Hacker News discussion reveals widespread frustration with Claude&\#x27;s verbosity, with users noting it insists on describing what it didn&\#x27;t do and uses convoluted sentence structures. Some find the ADHD skill only temporarily effective, as the model soon reverts to long-windedness. Others caution about the security risks of installing third-party skills from GitHub, recalling the danger of piping curl to shell.

**Tags**: `#LLM`, `#coding-agents`, `#Claude`, `#verbosity`, `#prompt-engineering`

---

<a id="item-13"></a>
## [Mercury 2.5: Diffusion-Based LLM Hits 1100 Tokens/Sec for Low-Latency Inference](https://www.inceptionlabs.ai/blog/introducing-mercury-2-5) ⭐️ 7.0/10

Inception Labs has released Mercury 2.5, a diffusion-based large language model that achieves inference speeds of 1100 tokens per second, optimized for low-latency applications. Its high throughput makes it particularly suitable for roles like arbiter in LLM consortium systems, where additional latency from a judge model is a key drawback; it also excels in real-time voice applications. The model is available via API, not open weights; users can opt out of data collection. It is not at the frontier but is comparable to some last-generation open-weight models, making it usable as a general chatbot.

hackernews · Topfi · Sep 8, 20:14 · [Discussion](https://news.ycombinator.com/item?id=49616354)

**Background**: Diffusion-based LLMs are an alternative to traditional autoregressive generation, where the model iteratively denoises a sequence, potentially enabling parallel token generation and faster inference. Inception Labs is a &\#x27;neolab&\#x27; exploring this architecture primarily for low-latency voice. The LLM consortium concept involves multiple models generating responses, with an arbiter model synthesizing them; fast arbiter inference reduces overall system latency.

<details><summary>References</summary>
<ul>
<li><a href="https://aipapersacademy.com/large-language-diffusion-models/">Large Language Diffusion Models: The Era Of Diffusion LLMs?</a></li>
<li><a href="https://github.com/irthomasthomas/llm-consortium">GitHub - irthomasthomas/llm-consortium: Parallel Reasoning: llm-consortium orchestrates mulitple LLMs, iteratively refines &amp; achieves consensus. · GitHub</a></li>

</ul>
</details>

**Discussion**: Community members expressed disappointment that the model is not open-weight, but praised its speed, especially for use as an arbiter in LLM consortium systems. Some noted that it is usable as a general chatbot and comparable to last-gen models, and appreciated the opt-out option for data collection.

**Tags**: `#LLM`, `#inference`, `#diffusion-models`, `#NLP`, `#low-latency`

---

<a id="item-14"></a>
## [OpenAI releases ChatGPT Images 2.5 with improved instruction-following](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 7.0/10

OpenAI has released ChatGPT Images 2.5, an update to its image generation models that improves instruction-following across multiple turns, responds faster, and better preserves reference photo subjects. The release includes two new API models: gpt-image-2.5-sunburst \(for precision editing\) and gpt-image-2.5-flare \(for fast, everyday generation\). The update addresses key user needs for precise, iterative image editing and faster generation, making it more practical for developers integrating image generation into workflows. With over 3 billion images generated, these improvements directly impact a large user base. The two new models differentiate by use case: Sunburst prioritizes editing precision, while Flare offers speed for everyday tasks. The API now supports passing reference images for inpainting tasks, as demonstrated by Simon Willison&\#x27;s CLI tool update.

rss · Simon Willison · Sep 8, 22:46

**Background**: OpenAI&\#x27;s ChatGPT Images is a feature that generates images from natural language descriptions, powered by AI models. The GPT-Image models are the underlying technology also available via OpenAI&\#x27;s API, which allows developers to programmatically create and edit images. The release of version 2.5 follows previous iterations, and the API model names &\#x27;sunburst&\#x27; and &\#x27;flare&\#x27; likely indicate different performance tiers.

**Tags**: `#openai`, `#image-generation`, `#api`, `#chatgpt`, `#ai`

---

<a id="item-15"></a>
## [Abusive Crawlers Consume More CPU on git.kernel.org Than Legitimate Use](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev revealed that abusive crawlers on git.kernel.org, the official Linux kernel Git repository, spend more CPU cycles rendering commits as HTML than all legitimate access combined, with 14 CPU cores across 5 nodes constantly doing nothing but rendering for scrapers. This highlights the severe resource drain that unchecked web scraping imposes on open-source infrastructure, potentially degrading performance for legitimate users and increasing operational costs, a concern relevant to many public web services. The abusive crawlers are not just fetching static pages but triggering expensive dynamic rendering of commit pages via cgit; the issue is not limited to git.kernel.org, as Simon Willison notes similar concerns for his Datasette project that serves crawlable pages.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org uses cgit, a fast web interface for Git repositories, to display commits as HTML pages. Rendering each commit into a web page requires server-side computation, which becomes costly when thousands of crawlers request many pages per second. Datasette is an open-source tool for exploring and publishing data, which also generates many crawlable HTML pages.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.archlinux.org/title/Cgit">cgit - ArchWiki</a></li>

</ul>
</details>

**Tags**: `#crawling`, `#git`, `#infrastructure`, `#web scraping`, `#performance`

---

<a id="item-16"></a>
## [OpenAI Chief Scientist: Build Powerful AI for Defense, but Avoid Recklessness](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 7.0/10

Jakub Pachocki, OpenAI&\#x27;s Chief Scientist, argued that continuing to train much smarter models quickly is necessary to build defensive systems against AI dangers, but he cautioned that this should not become an excuse for recklessness. This statement from a leading AI company&\#x27;s Chief Scientist highlights the strategic dilemma of advancing AI for defense while emphasizing responsible development, influencing the ongoing AI safety and alignment debate. Pachocki specifically referenced defending against rogue AI agents, securing infrastructure, and inventing entirely new protective measures, indicating that OpenAI will prioritize these defensive applications in its deployment efforts.

rss · Simon Willison · Sep 7, 22:26

**Background**: AI alignment is a subfield of AI safety focusing on ensuring AI systems pursue human-intended goals. Concerns about rogue AI agents, where autonomous AI systems act in harmful ways, have grown in recent years. OpenAI&\#x27;s statement reflects a dual approach: aggressively developing AI for defense while mitigating risks of reckless advancement.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://grokipedia.com/page/AI_Agents_Gone_Rogue">AI Agents Gone Rogue</a></li>

</ul>
</details>

**Tags**: `#ai-safety`, `#openai`, `#alignment`, `#ai-ethics`, `#defense`

---

<a id="item-17"></a>
## [Generating Bad Apple from a Single Initial State with a 417k-Parameter Recurrent System](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/) ⭐️ 7.0/10

A recurrent dynamical system with only 417k parameters generates the entire 6,500-frame Bad Apple video autonomously from a single initial state, without any time input. This demonstrates that a tiny recurrent model can learn a long, complex temporal sequence and remain stable over thousands of steps, challenging the need for larger models or explicit time embeddings for video generation. The model uses a 64-D latent state, LSTM-style recurrence, and bilinear upsampling decoder; training involved a curriculum of rollout horizons \(2 to 512 frames\), teacher tables, state noise, and second-difference acceleration regularization.

reddit · r/MachineLearning · /u/SEBADA321 · Sep 8, 00:05

**Background**: SIREN \(Sinusoidal Representation Networks\) is an implicit neural representation that uses sine activations to map coordinates to pixel values, enabling memorization of signals like images or videos. The previous approach for Bad Apple used a SIREN MLP with time as input. This work explores a recurrent dynamical system, a type of neural network that evolves its internal state over time without external time signals, similar to how a physical system moves according to its own dynamics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2006.09661">Implicit Neural Representations with Periodic</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S089360800580125X">Approximation of dynamical systems by continuous time recurrent neural networks - ScienceDirect</a></li>

</ul>
</details>

**Tags**: `#recurrent-neural-networks`, `#dynamical-systems`, `#generative-models`, `#computer-vision`, `#machine-learning`

---

<a id="item-18"></a>
## [LLM-Guided Program Evolution Breaks 10 Packomania Records](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 7.0/10

A researcher used an LLM to iteratively evolve a circle-packing solver, improving the best-known solutions for 10 problem instances \(N=101-114\) on the Packomania csqv benchmark by 2.4-5.4% in 15 iterations, at a total LLM API cost of $27.72. The improved results were independently verified and accepted by the Packomania maintainer. This demonstrates that LLMs can be used to evolve optimization algorithms themselves, not just solve problem instances directly. The approach is cost-effective and could be applied to other hard combinatorial optimization benchmarks, potentially leading to new state-of-the-art results with minimal human engineering effort. The LLM proposed algorithmic improvements, not direct packing solutions, and each candidate was evaluated by an independent verifier to ensure correctness. The author specifically seeks critique on the plateau-detection stopping rule used to terminate the evolution process.

reddit · r/MachineLearning · /u/SIGH\_I\_CALL · Sep 7, 16:54

**Background**: Circle packing is a classic combinatorial optimization problem that involves arranging circles within a container without overlap. The Packomania website tracks the best-known solutions for various packing variants, including the csqv benchmark where the goal is to maximize the sum of radii of N variable-radius circles packed into a unit square. Improving upon these long-standing records is considered a significant achievement, as the problem is computationally hard and requires sophisticated heuristics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.05093">[2609.05093] LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28</a></li>
<li><a href="https://en.wikipedia.org/wiki/Circle_packing">Circle packing - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#program-evolution`, `#optimization`, `#circle-packing`, `#machine-learning`

---

<a id="item-19"></a>
## [DIY Printer Uses E-Ink Display Instead of Paper](https://nishantjosh.dev/blogs/how-to-build-a-fking-printer/) ⭐️ 6.0/10

A blog post describes a creative hack that treats an e-ink display as a printer, allowing documents to be &\#x27;printed&\#x27; directly onto the electronic paper screen. The project highlights an unconventional use of e-ink technology, sparking conversation about paperless alternatives and the potential for repurposing e-readers as low-power, reusable displays. Commenters noted that the device might simply render the PDF directly without the need for a &\#x27;print&\#x27; function, suggesting the hack may be a demonstration of concept rather than a practical necessity.

hackernews · cat-whisperer · Sep 8, 21:22 · [Discussion](https://news.ycombinator.com/item?id=49617255)

**Background**: E Ink is a type of electronic paper display technology that mimics ink on paper, using tiny microcapsules to create a low-power, bistable screen that retains an image without continuous power. This project uses such a display as a printer output, effectively turning an e-reader or similar device into a reusable paper substitute.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/E_Ink">E Ink - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community reaction was mixed: some praised the idea as amazing and intuitive, while others were confused about its purpose, questioning why not simply view the PDF on the device. A few users expressed interest in adopting the approach.

**Tags**: `#e-ink`, `#printer`, `#DIY`, `#hack`, `#hardware`

---

<a id="item-20"></a>
## [DaVinci Resolve 21.1 Release Sparks Discussion on Free Upgrades and Linux Codec Issues](https://www.blackmagicdesign.com/media/release/20260908-03) ⭐️ 6.0/10

DaVinci Resolve 21.1 introduces integration with AI assistants like Claude and ChatGPT Codex, allowing users to control projects via natural language. It continues Blackmagic Design&\#x27;s free upgrade policy for Studio users, sparking renewed discussion over Linux platform limitations. This update aligns with the growing integration of AI in creative software, potentially simplifying complex tasks for editors. The sustained community focus on Linux codec limitations highlights the persistent gap in professional video editing tools for Linux, affecting a vocal subset of users. The AI feature works via external assistants, not a built-in model. On Linux, the free version cannot decode H.264/H.265, requiring the Studio version; additionally, VST3 plugins, JACK audio, and MIDI control in Fairlight are unsupported.

hackernews · tosh · Sep 8, 13:36 · [Discussion](https://news.ycombinator.com/item?id=49610181)

**Background**: DaVinci Resolve is a comprehensive video editing, color grading, and audio post-production suite. Blackmagic Design offers a free version with many features and a paid Studio version with advanced capabilities, and has historically provided free Studio upgrades. However, the Linux version has long-standing codec limitations: the free version lacks support for H.264 and H.265 decoding, forcing users to transcode footage. Audio support on Linux is also limited, missing VST3 plugins, JACK audio, and MIDI control surface functionality, which are available on Windows and macOS.

<details><summary>References</summary>
<ul>
<li><a href="https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_18_Supported_Codec_List.pdf?_v=1705996810000">DaVinci Resolve January 2024 Supported Formats and Codecs</a></li>
<li><a href="https://forum.blackmagicdesign.com/viewtopic.php?f=21&amp;t=192600">Blackmagic Forum • View topic - Codecs supported in Ubuntu Linux?</a></li>
<li><a href="https://github.com/drsnxt/davinci-kit/blob/main/docs/DAVINCI-RESOLVE-LINUX-GUIDE.md">davinci-kit/docs/DAVINCI-RESOLVE-LINUX-GUIDE.md at main · drsnxt/davinci-kit</a></li>

</ul>
</details>

**Discussion**: The community praised the software&\#x27;s stability and free upgrades, but many Linux users expressed frustration over the lack of H.264/AAC decoding and missing audio features like VST3 and JACK. Some viewed the AI agent integration as a gimmick, while others noted the need to rely on separate audio tools like Reaper.

**Tags**: `#video-editing`, `#davinci-resolve`, `#linux`, `#software-update`, `#community-discussion`

---

<a id="item-21"></a>
## [Simon Willison Builds Browser-Based Video Compressor Using Claude Fable 5.1](https://simonwillison.net/2026/Sep/7/video-compressor/) ⭐️ 6.0/10

Simon Willison built a pure client-side video compression tool using the ffmpeg.wasm WebAssembly port of FFmpeg, assisted by Claude Fable 5.1. The tool offers preset quality levels \(Largest to Smallest\) with CRF values from 22 to 28, and can generate multiple optimized versions in seconds directly in the browser. This demonstrates how powerful AI coding assistants like Claude Fable 5.1 can accelerate the creation of privacy-focused utilities. It also highlights the maturity of WebAssembly for running complex media processing like FFmpeg entirely in the browser, eliminating the need for server-side video handling. The tool provides five presets with resolutions from 854×370 to 640×276, CRF 22-28, and audio bitrates 128-64 kbps, plus options for encoder speed, H.264 profile, 30 fps cap, metadata stripping, audio removal, and encoding only the first 10 seconds. All processing is done client-side via ffmpeg.wasm, and the generated ffmpeg commands are displayed for transparency.

rss · Simon Willison · Sep 7, 18:29

**Background**: ffmpeg.wasm is a WebAssembly port of the popular FFmpeg multimedia framework, enabling video and audio processing directly in the browser without server-side infrastructure. CRF \(Constant Rate Factor\) is a quality control method used by H.264 encoders; lower values \(e.g., 18\) produce near-lossless quality, while higher values \(e.g., 28\) reduce file size at the cost of visual fidelity. Claude Fable 5.1 is a &\#x27;Mythos-class&\#x27; large language model released by Anthropic in September 2026, known for strong coding and reasoning abilities, and was used here to generate the tool&\#x27;s code.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ffmpegwasm/ffmpeg.wasm">ffmpegwasm/ffmpeg.wasm</a></li>
<li><a href="https://slhck.info/video/2017/02/24/crf-guide.html">CRF Guide (Constant Rate Factor in x264, x265 and libvpx)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>

</ul>
</details>

**Tags**: `#webassembly`, `#ffmpeg`, `#video-compression`, `#ai-assisted-coding`, `#tool`

---

<a id="item-22"></a>
## [Reddit User Seeks Debugging Strategies for Silent ML Pipeline Failures](https://www.reddit.com/r/MachineLearning/comments/1waewc3/when_a_run_is_wrong_but_nothing_actually_failed/) ⭐️ 6.0/10

A Reddit user on r/MachineLearning asked for practical debugging strategies when an ML pipeline run completes without errors or exceptions but produces incorrect results. The post lists several possible starting points, such as working backward from the output, comparing against a known good run, and inspecting tool call behavior, and invites community input on real-world production approaches. This highlights a common and frustrating challenge in ML engineering—silent failures where the system reports success but the output is flawed. Gathering community approaches can help standardize debugging practices and improve the reliability of ML pipelines in production. The user specifically mentions checking retrieval/tool behavior, model inputs, replaying the run, and examining business state outside the trace, indicating the pipeline likely involves LLM agents with external tool calls. The post emphasizes the need for practical, not idealized, debugging techniques.

reddit · r/MachineLearning · /u/Sensitive-Parsnip-12 · Sep 8, 05:01

**Background**: ML pipelines often combine multiple steps, including data retrieval, LLM reasoning, and tool calling—where an LLM invokes external functions or APIs. Silent failures can occur when each step appears to succeed but the overall outcome is incorrect. Replay debugging is a technique that preserves the full execution context \(states, messages, tool responses\) so developers can rerun the pipeline from any step to reproduce and diagnose issues. Tool calling is a core capability for LLM agents, but incorrect tool selection or parameter errors can silently corrupt results.

<details><summary>References</summary>
<ul>
<li><a href="https://composio.dev/content/ai-agent-tool-calling-guide">Tool Calling Explained: The Core of AI Agents (2026 Guide) | Composio</a></li>
<li><a href="https://mdsanwarhossain.me/blog-agentic-ai-debugging.html">Debugging Broken Agentic AI Pipelines in Production : Loops...</a></li>

</ul>
</details>

**Tags**: `#debugging`, `#MLOps`, `#production`, `#troubleshooting`, `#machine learning`

---

<a id="item-23"></a>
## [Practical Radar Object Classification with Histogram MLP: Ablation Studies and Insights](https://www.reddit.com/r/MachineLearning/comments/1w9m26u/automotive_radar_object_classification_p/) ⭐️ 6.0/10

A radar signal processing engineer implemented a 3-layer MLP classifier using per-scan histograms on the RadarScenes dataset, and conducted ablation studies revealing that the number of radar detections per instance is a critical factor, with macro F1 rising from 0.381 to 0.764 as detection count increases from 1 to 5, and that changes in architecture or encoding had less impact than data split variation. The work highlights practical challenges in real-world radar perception, such as class imbalance, sequence bias, and the critical role of detection density. It demonstrates that simple models can be effective, but data quality and split consistency are paramount, and underscores the limitations of single-scan classification without temporal context for autonomous driving. The model uses class-weighted cross-entropy loss. Aggregated classes \(e.g., two-wheeler mixing bicycles and motorized variants, large\_vehicle combining trucks, buses, trains\) cause confusion. Sequence bias from long tracks of slow-moving objects leads to high F1 variance across folds. The most important feature is radial velocity \(vr\_compensated\), causing two-wheelers to be misclassified as pedestrians when stationary. Wide or high-RCS cars are sometimes misclassified as large vehicles due to multipath effects.

reddit · r/MachineLearning · /u/bruno\_pinto90 · Sep 7, 08:10

**Background**: Radar point clouds provide sparse, low-resolution spatial information but are robust in adverse weather and offer direct Doppler velocity measurements. The 2023 paper &quot;Histogram-based Deep Learning for Automotive Radar&quot; proposed computing per-feature histograms of radar point clouds and feeding them to an MLP, achieving competitive results with minimal complexity. The RadarScenes dataset is a public real-world automotive radar point cloud dataset with labeled instances. MLP is a basic neural network architecture. Class imbalance and sequence bias are common in sequential sensor data, where contiguous objects can skew training/validation splits if not carefully handled.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2303.02975">[2303.02975] Histogram-based Deep Learning for Automotive Radar</a></li>
<li><a href="https://arxiv.org/html/2104.02493v2">RadarScenes: A Real-World Radar Point Cloud Data Set for Automotive Applications</a></li>

</ul>
</details>

**Tags**: `#automotive radar`, `#object classification`, `#point cloud`, `#MLP`, `#histogram features`

---