---
layout: default
title: "Horizon Summary: 2026-09-07 (EN)"
date: 2026-09-07
lang: en
---

> From 25 items, 16 important content pieces were selected

---

1. [OpenAI Pursues Automated AI Researcher for Recursive Self-Improvement and Alignment](#item-1) ⭐️ 9.0/10
2. [OpenAI Researcher Urges Voluntary AI Slowdown Over Unsolved Alignment](#item-2) ⭐️ 9.0/10
3. [Making a Python Interpreter in 1024 Bytes](#item-3) ⭐️ 8.0/10
4. [Anubis Adds WebAssembly Support After Year-Long Integration](#item-4) ⭐️ 8.0/10
5. [Report: 10-20% of New gTLD Domains Are Scams](#item-5) ⭐️ 8.0/10
6. [Hands-On: Astra vs. Fable 5.1 on Real ML Tasks Reveals Key Tradeoffs](#item-6) ⭐️ 8.0/10
7. [Runtime MoE Expert Expansion in llama.cpp with Layered Linear Decay](#item-7) ⭐️ 8.0/10
8. [Declarative Attention: LLMs Declare Context Regions to Cut KV Cache Scanning](#item-8) ⭐️ 8.0/10
9. [Nitter and XCancel Resume Service After Legal Advice](#item-9) ⭐️ 7.0/10
10. [Simon Willison on Why Rewriting Legacy Systems from Scratch Fails](#item-10) ⭐️ 7.0/10
11. [Software Code Can Always Get Worse, Unlike Buildings](#item-11) ⭐️ 7.0/10
12. [PINNStudio: An Open-Source No-Code GUI for Physics-Informed Neural Networks](#item-12) ⭐️ 7.0/10
13. [GPT-6 Jailbroken Within 24 Hours Using Extended Task-in-Prompt Attack](#item-13) ⭐️ 7.0/10
14. [Applying Sliding Window Attention to Pretrained LLMs at Inference](#item-14) ⭐️ 7.0/10
15. [Using Blender with Coding Agents on macOS to Generate 3D Scenes](#item-15) ⭐️ 6.0/10
16. [Is Reproducibility Becoming Irrelevant in Machine Learning Research?](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Pursues Automated AI Researcher for Recursive Self-Improvement and Alignment](https://openai.com/index/research-acceleration-view-inside-openai) ⭐️ 9.0/10

OpenAI publicly detailed its goal to build an automated AI researcher capable of performing research tasks under human supervision, aiming to accelerate progress in deep learning and alignment, effectively pursuing recursive self-improvement. This could dramatically speed up AI safety research, but it also raises profound concerns about recursive self-improvement leading to an intelligence explosion, potentially bypassing human control and exacerbating alignment risks if the researcher misbehaves. OpenAI envisions a system that can handle tasks taking a skilled researcher a few days, and they note their researchers already spend up to $8,000 per day on compute; they use the term RSI without defining it, indicating an internal assumption of familiarity.

hackernews · iamsyr · Sep 6, 15:08 · [Discussion](https://news.ycombinator.com/item?id=49587217)

**Background**: AI alignment is the field aiming to ensure AI systems pursue intended goals, not harmful unintended ones. Recursive self-improvement \(RSI\) is the hypothetical process where an AI system rewrites its own code, leading to an intelligence explosion. OpenAI&\#x27;s automated researcher would be a deliberate step toward RSI, raising safety concerns because a misaligned self-improving system could quickly become uncontrollable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about the self-serving narrative of &quot;AI to protect us from AI,&quot; noted the alignment with the &quot;AI 2027&quot; scenario, and questioned the oversight of potentially misaligned earlier generations. Some found the practical usage details interesting, but the overall sentiment is cautious and critical.

**Tags**: `#AI research`, `#recursive self-improvement`, `#alignment`, `#OpenAI`, `#automation`

---

<a id="item-2"></a>
## [OpenAI Researcher Urges Voluntary AI Slowdown Over Unsolved Alignment](https://openai.com/index/an-alien-mind/) ⭐️ 9.0/10

An OpenAI researcher published a blog post titled “An Alien Mind,” arguing that no lab has sufficiently solved AI alignment and monitoring to continue scaling AI responsibly, and explicitly calling for voluntary slowdowns and international coordination on safety standards. This public stance from a leading AI company directly challenges the prevailing “scale at all costs” mentality, and could catalyze industry-wide discussions on safety, regulation, and the geopolitical AI arms race, potentially reshaping the trajectory of AGI development. The post states that ‘no lab has solved alignment and monitoring to a sufficient degree,’ advocates for voluntary slowdowns until shared safety bars are established, and frames international coordination as a top priority. The piece sparked over 330 community comments with a mix of skepticism, satire, and debate.

hackernews · tosh · Sep 6, 16:27 · [Discussion](https://news.ycombinator.com/item?id=49588080)

**Background**: AI alignment is the field of ensuring AI systems pursue intended goals and values, avoiding unintended harm. Scaling laws describe how AI model performance predictably improves with more data, parameters, and compute. This post emerges from growing tension between rapid scaling and the difficulty of aligning increasingly capable models, especially as systems approach superintelligence, where misalignment could pose existential risks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-scaling-laws/">How Scaling Laws Drive Smarter, More Powerful AI | NVIDIA Blog</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a range of views: some mocked the call for slowdowns as pre-IPO posturing or as futile given humanity’s inability to stop the momentum; others highlighted the internal contradiction of OpenAI advocating restraint while racing ahead; and a few noted the realpolitik of an AI arms race that makes unilateral slowdowns dangerous.

**Tags**: `#AI alignment`, `#AI safety`, `#OpenAI`, `#superintelligence`, `#scaling laws`

---

<a id="item-3"></a>
## [Making a Python Interpreter in 1024 Bytes](https://austinhenley.com/blog/python1024.html) ⭐️ 8.0/10

Austin Henley created a Python interpreter in just 1024 bytes of C source code as a code golf exercise, using creative shortcuts and strict assumptions to execute a tiny subset of Python. This project showcases extreme code compression and clever interpretation hacks, inspiring both recreational programming and considerations for minimal language implementations in resource-constrained environments. The interpreter maps single characters to keywords \(e.g., &\#x27;f&\#x27; for &\#x27;for \[x\] in range\[y\]&\#x27;, &\#x27;w&\#x27; for &\#x27;while&\#x27;, &\#x27;i&\#x27; for &\#x27;if&\#x27;\), loops reparse source code each iteration, and the 1024-byte C source compiles to a much larger binary, with no error checking and an assumption of perfect input.

hackernews · azhenley · Sep 6, 23:14 · [Discussion](https://news.ycombinator.com/item?id=49591876)

**Background**: Code golf is a recreational programming competition where participants aim to write the shortest possible source code to solve a given problem. This project is a code golf attempt to create a minimal Python interpreter, exploiting every possible shortcut to fit within a strict byte limit.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Code_golf">Code golf</a></li>

</ul>
</details>

**Discussion**: Community reactions are largely positive, marveling at the creativity and humor. Commenters highlight the extreme shortcuts \(single-letter keywords, no error checking\), compare it to other tiny language projects like C4 and Sector C, and note its impracticality for production. Some share related projects such as Snek for embedded use, and the author&\#x27;s earlier tiny compiler.

**Tags**: `#code-golf`, `#python`, `#interpreters`, `#c`, `#obfuscation`

---

<a id="item-4"></a>
## [Anubis Adds WebAssembly Support After Year-Long Integration](https://anubis.techaro.lol/blog/2026/anubis-wasm/) ⭐️ 8.0/10

The Anubis proof-of-work captcha system has successfully integrated WebAssembly \(WASM\) after a year-long engineering effort, achieving improved performance and security while navigating complex browser compatibility issues, including support for Chrome 66. This integration makes the captcha more resistant to automated solvers and reduces the computational burden on the client, while the deep-dive into toolchain and backwards compatibility challenges provides valuable insights for web developers working on similar performance-critical features. The integration involved targeting Chrome 66 for backwards compatibility, and the author explored using Rust&\#x27;s \`wasm32v1-none\` target to generate baseline WASM without extensions, though the exact fallback mechanism for browsers without WASM is likely still in place.

hackernews · xena · Sep 6, 20:32 · [Discussion](https://news.ycombinator.com/item?id=49590611)

**Background**: Proof-of-work captchas require users&\#x27; devices to perform a computational puzzle to verify they are human, rather than asking them to identify images. WebAssembly \(WASM\) is a low-level binary format that runs in browsers at near-native speed, making it ideal for intensive tasks like solving proof-of-work challenges. Anubis is an open-source captcha system designed to protect small websites from AI scraping bots, and it was previously implemented purely in JavaScript.

<details><summary>References</summary>
<ul>
<li><a href="https://anubis.zehuti.com/docs/captcha">Anubis documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proof_of_work">Proof of work - Wikipedia</a></li>
<li><a href="https://directory.fsf.org/wiki/Anubis_captcha">Anubis captcha - Free Software Directory</a></li>

</ul>
</details>

**Discussion**: Commenters praised the author&\#x27;s handling of demanding users and the technical depth, but some worried about users who disable WebAssembly for privacy, requesting a fallback message. Others noted the importance of backwards compatibility with older browsers like Chrome 66, and one commenter suggested using period-correct toolchains for better compatibility.

**Tags**: `#webassembly`, `#open-source`, `#browser-compatibility`, `#proof-of-work`, `#developer-experience`

---

<a id="item-5"></a>
## [Report: 10-20% of New gTLD Domains Are Scams](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 8.0/10

An Interisle report reveals that of the 85 million new generic top-level domain \(gTLD\) registrations in 2025, 8.5 million were blocklisted by May 2025, and the true abuse rate is likely between 10% and 20%—meaning roughly one in five new gTLDs may be a scam. This staggering abuse rate erodes trust in DNS, a fundamental internet infrastructure, and fuels widespread phishing, fraud, and malware, threatening global users and businesses. The 10% figure is considered a floor, with the actual rate possibly closer to 20%; blocklisted domains represent only a lower bound, as many scams go undetected. ICANN has discussed the problem for years but has struggled to implement effective countermeasures.

rss · Simon Willison · Sep 6, 14:40

**Background**: Generic top-level domains \(gTLDs\) are the common domain endings like .com, .org, and newer ones such as .xyz, operated under ICANN&\#x27;s oversight. DNS abuse includes registering domains for phishing, fraud, malware, and spam. ICANN is the global coordinator of the DNS, but its multi-stakeholder governance model has been slow to respond to rapid abuse.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GTLD">GTLD</a></li>
<li><a href="https://en.wikipedia.org/wiki/ICANN">ICANN</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#cybersecurity`, `#domain abuse`, `#scams`, `#internet infrastructure`

---

<a id="item-6"></a>
## [Hands-On: Astra vs. Fable 5.1 on Real ML Tasks Reveals Key Tradeoffs](https://www.reddit.com/r/MachineLearning/comments/1w8g1gk/astra_vs_fable_51_on_real_ml_tasks_tradeoffs/) ⭐️ 8.0/10

A user compared Fable 5.1 and Astra on an ML text-processing and model-training workflow. Astra demonstrated stronger agentic coding, scientific rigor, and debugging, while Fable 5.1 produced better prose, more idiomatic code, and handled data encoding correctly. This comparison shows that neither model has fully mastered the ML workflow, highlighting the ongoing trade-offs in AI coding assistants. It provides practical insights for practitioners choosing between models for ML tasks, emphasizing the importance of human oversight. Astra fixed a gensim kernel bug by downgrading dependencies and produced a forensic audit trail, but it introduced a UTF-8 encoding defect. Fable 5.1 overlooked a tokenization bug, but its analysis report included an ablation study and insightful findings. Both models improved accuracy by 0.02–0.04 after human feedback.

reddit · r/MachineLearning · /u/returnity · Sep 5, 23:33

**Background**: Astra is OpenAI&\#x27;s latest GPT-6 model, known for its coding and reasoning capabilities but controversial for opaque recurrence. Fable 5.1 is Anthropic&\#x27;s Claude Fable model, recently updated to be cheaper and better at coding, with improved vision and document understanding. Both are leading large language models used for complex agentic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI models`, `#ML workflow`, `#model comparison`, `#language models`, `#benchmarking`

---

<a id="item-7"></a>
## [Runtime MoE Expert Expansion in llama.cpp with Layered Linear Decay](https://www.reddit.com/r/MachineLearning/comments/1w94dtn/proposed_architecture_for_inferencing_sparse_moe/) ⭐️ 8.0/10

A new runtime modification to llama.cpp enables MoE models to infer with more active experts than the native top-K, using an adaptive threshold and layered linear influence decay from 99% to 50%, without any retraining. This approach can enhance the capacity of existing MoE models at inference time without costly retraining, offering a practical way to improve performance on tasks like reasoning and coding. It makes advanced MoE models more accessible to the community. Implemented in llama.cpp with support for all backends, the method was tested on Qwen 3.6 35B A4B+. It allows specifying a layer range, and the linear decay reduces each additional expert&\#x27;s influence from 99% in early layers to 50% in later layers, ensuring a smooth transition.

reddit · r/MachineLearning · /u/Specific-Tax-6700 · Sep 6, 18:41

**Background**: Mixture of Experts \(MoE\) models use a gating network to route each token to a subset of &\#x27;expert&\#x27; sub-networks, typically via top-K routing where only the top K scoring experts are activated. This keeps computation manageable while scaling model parameters. However, the fixed top-K limits the number of active experts per token. Expanding the number of experts at runtime without retraining allows models to leverage more knowledge, potentially improving accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/learning/scaling-ai-models-with-mixture-of-experts-moe-design-principles-and-real-world-applications/intro-to-moe-architecture">Intro to MoE architecture - Scaling AI Models with Mixture of Experts ...</a></li>
<li><a href="https://mbrenndoerfer.com/writing/top-k-routing-mixture-of-experts-expert-selection">Top-K Routing: Expert Selection in Mixture of Experts Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer</a></li>
<li><a href="https://architecturediagram.ai/blog/mixture-of-experts-architecture">Mixture of Experts ( MoE ) Architecture ... - ArchitectureDiagram.ai</a></li>

</ul>
</details>

**Tags**: `#moE`, `#inference`, `#llama.cpp`, `#expert-expansion`, `#runtime-optimization`

---

<a id="item-8"></a>
## [Declarative Attention: LLMs Declare Context Regions to Cut KV Cache Scanning](https://www.reddit.com/r/MachineLearning/comments/1w7sgf3/language_models_can_control_their_own_attention_r/) ⭐️ 8.0/10

A new paper introduces Declarative Attention \(DA\), a zero-shot protocol that allows language models to declare which context segments \(global, focus, or local\) they need to attend to during generation, avoiding a full scan of the KV cache. This intrinsic approach reduces long-context inference cost dramatically—decoding attended tokens dropped by up to 52% on Gemma-4-31B with only a 1.27 percentage point accuracy loss—making large-scale LLM serving more efficient. The model partitions generation into &lt;global&gt;, &lt;focus&gt;, and &lt;local&gt; modes; the inference engine parses these declarations as tool calls and skips most of the KV cache read. Evaluated zero-shot on Gemma-4-31B and Qwen-3.6-27B across 15 long-context tasks, performance improves with model scale.

reddit · r/MachineLearning · /u/eigenlaplace · Sep 5, 06:07

**Background**: In autoregressive transformer inference, key and value vectors from all previous tokens are stored in a KV cache to avoid recomputation. The cache grows linearly with context length, making long-context decoding expensive. Sparse attention methods reduce cost by selecting token subsets, but often require external scoring. Chain-of-thought prompting, where the model generates intermediate reasoning steps, provides a natural way to elicit attention declarations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.02737">Language Models Can Control Their Own Attention</a></li>
<li><a href="https://www.youtube.com/watch?v=lRSAD-t1x20">Language Models Can Control Their Own Attention ... - YouTube</a></li>
<li><a href="https://academy.dair.ai/papers/language-models-can-control-their-own-attention-2609.02737">Language Models Can Control Their Own Attention | DAIR.AI Academy</a></li>

</ul>
</details>

**Tags**: `#Language Models`, `#Attention Mechanisms`, `#Efficient Inference`, `#Long-Context`, `#Machine Learning Research`

---

<a id="item-9"></a>
## [Nitter and XCancel Resume Service After Legal Advice](https://github.com/zedeus/nitter/commit/1428b4c2b4246f92a7e5b2673438e5fb39fcc4a3) ⭐️ 7.0/10

Alternative frontends Nitter and XCancel, which had shut down after receiving a cease-and-desist from X, have resumed operations following legal counsel, restoring privacy-focused access to content on the platform. The resumption preserves public access to information on a walled-garden platform, highlighting the tension between open access and corporate control, and the legal pressures faced by small open-source projects. Nitter and XCancel are privacy-centric frontends that allow browsing X without tracking, ads, or an account, but cannot be used for interaction. They were shut down by a cease-and-desist from X in August 2026, and the legal advice they received apparently indicated that the risk was manageable for resuming the service.

hackernews · zImPatrick · Sep 6, 17:49 · [Discussion](https://news.ycombinator.com/item?id=49588988)

**Background**: Nitter is a free and open-source alternative frontend for X \(formerly Twitter\) that provides access to public posts without tracking, ads, or login requirements. XCancel similarly redirects X links to a privacy-oriented interface. In August 2026, X issued a cease-and-desist letter to these projects, forcing them offline. The legal reassessment and subsequent return underscore the ongoing struggle between walled-garden platforms and the open web.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nitter">Nitter</a></li>
<li><a href="https://www.forbes.com/sites/siladityaray/2026/08/26/cease-and-desist-from-x-shuts-down-nitter-and-xcancel-sites-that-scraped-and-mirrored-tweets/">Cease-And-Desist From X Shuts Down Nitter And XCancel—Sites That Scraped And Mirrored Tweets</a></li>

</ul>
</details>

**Discussion**: Community members expressed relief at the return, noting the importance of alternative frontends for accessing public information. Several highlighted the legal asymmetry where large companies can intimidate small projects with legal threats, and others called for user migration to decentralized platforms to break the hold of tech giants.

**Tags**: `#alternative frontends`, `#Twitter`, `#privacy`, `#open-source`, `#censorship circumvention`

---

<a id="item-10"></a>
## [Simon Willison on Why Rewriting Legacy Systems from Scratch Fails](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 7.0/10

Simon Willison, in a Lobste.rs comment, argues that attempting to rewrite a legacy system from scratch is rarely successful because the old system continues to evolve, developers lose incentive to maintain it, and the new team&\#x27;s ambition often leads to delays and incomplete replacements. This insight highlights a common strategic mistake in software engineering, affecting companies that struggle with technical debt. Recognizing the pitfalls can save organizations from wasted resources and parallel system maintenance nightmares. Willison emphasizes that the old system remains a moving target, the new team often underestimates the complexity, and the result is two systems running in production. He recommends instead strengthening the old system with automated testing and targeted refactoring.

rss · Simon Willison · Sep 6, 09:08

**Background**: Technical debt refers to the implied cost of future rework caused by choosing expedient solutions over better design. Lobste.rs is a technology-focused discussion forum similar to Hacker News. The discussion was triggered by a comment about &\#x27;burning it down to start from scratch&\#x27; when technical debt becomes overwhelming.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_debt">Technical debt</a></li>
<li><a href="https://grokipedia.com/page/Lobsters">Lobste.rs</a></li>

</ul>
</details>

**Tags**: `#software engineering`, `#technical debt`, `#rewrite`, `#legacy code`, `#code quality`

---

<a id="item-11"></a>
## [Software Code Can Always Get Worse, Unlike Buildings](https://simonwillison.net/2026/Sep/6/zach-kehs/) ⭐️ 7.0/10

Zach Kehs observed that while adding floors to a building will eventually cause collapse, software code has no such constraint—it can always deteriorate further with new layers of indirection and performance degradation. This observation highlights the perpetual risk of technical debt in software engineering, where codebases can degrade indefinitely without natural limits, making active maintenance essential. It resonates with developers who face the challenge of escalating complexity. The quote references &quot;a new layer of indirection,&quot; a nod to the famous adage by David Wheeler that all problems in computer science can be solved by another level of indirection. It also notes that performance can always be reduced, implying no lower bound on efficiency.

rss · Simon Willison · Sep 6, 08:42

**Background**: The metaphor contrasts software with physical structures. In civil engineering, a building&\#x27;s weight creates stress that eventually exceeds material strength, causing collapse. Software, however, is abstract and can be layered arbitrarily without physical failure, but this leads to accumulation of technical debt—a term describing the consequences of poor design choices that compound over time. The concept is central to software maintenance discussions.

**Tags**: `#technical-debt`, `#software-engineering`, `#code-quality`, `#metaphor`

---

<a id="item-12"></a>
## [PINNStudio: An Open-Source No-Code GUI for Physics-Informed Neural Networks](https://www.reddit.com/r/MachineLearning/comments/1w9a2i7/pinnstudio_a_free_opensource_nocode_gui_for/) ⭐️ 7.0/10

PINNStudio is a newly released free, open-source tool that provides a no-code graphical interface for defining, training, and visualizing physics-informed neural networks, automatically generating the underlying code using DeepXDE. By eliminating the need to manually write boilerplate code for each new PINN problem, PINNStudio lowers the technical barrier for students and researchers, enabling faster experimentation and broader adoption of scientific machine learning methods. The tool is built on top of the DeepXDE library, supports both forward and inverse problems in 1D/2D domains, and includes built-in templates for classic PDEs like the Heat and Allen-Cahn equations. It can be installed via pip and is available on GitHub.

reddit · r/MachineLearning · /u/Impossible-Jello2749 · Sep 6, 22:19

**Background**: Physics-informed neural networks \(PINNs\) embed physical laws described by partial differential equations \(PDEs\) directly into the training of neural networks, allowing them to solve forward problems \(solving a known PDE\) and inverse problems \(estimating unknown parameters from data\). Setting up PINNs typically requires significant coding effort: defining the PDE, boundary conditions, network architecture, and training loop. DeepXDE is a popular library that simplifies this process, but still requires programming. PINNStudio builds on DeepXDE to provide a visual interface that generates the necessary code automatically.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Physics-informed_neural_networks">Physics-informed neural networks</a></li>
<li><a href="https://www.mathworks.com/discovery/physics-informed-neural-networks.html">What Are Physics-Informed Neural Networks (PINNs)? - MATLAB &amp; Simulink</a></li>
<li><a href="https://cvw.cac.cornell.edu/SciML/pinns/inverse-problems-with-pinns">Cornell Virtual Workshop &gt; Scientific Machine Learning ...</a></li>

</ul>
</details>

**Tags**: `#PINNs`, `#scientific-machine-learning`, `#no-code`, `#open-source`, `#GUI`

---

<a id="item-13"></a>
## [GPT-6 Jailbroken Within 24 Hours Using Extended Task-in-Prompt Attack](https://www.reddit.com/r/MachineLearning/comments/1w89m36/gpt6_reportedly_jailbroken_within_24_hours_using/) ⭐️ 7.0/10

A researcher reportedly jailbroke GPT-6 Astra within 24 hours of release by combining an extended Task-in-Prompt \(TIP\) attack from an ACL 2025 paper with four unnamed techniques, and privately disclosed the method to OpenAI. The rapid jailbreak of a frontier model underscores persistent AI safety challenges and shows that even advanced reasoning models remain vulnerable to adversarial attacks, highlighting the difficulty of building robust safeguards. The original minimal TIP attack was insufficient for GPT-6, requiring reworking; the attack exploits hidden harmful objectives within tasks like cipher decoding or code execution. The same researcher previously jailbroke GPT-5 within an hour of its release.

reddit · r/MachineLearning · /u/Asleep-Requirement13 · Sep 5, 19:11

**Background**: Task-in-Prompt \(TIP\) attacks are a recently discovered class of jailbreak techniques that trick LLMs by embedding harmful instructions within seemingly innocuous tasks like solving ciphers or executing Python code. The attack exploits the model&\#x27;s reasoning abilities to bypass safety filters. The method was presented in a paper at ACL 2025, demonstrating that even state-of-the-art models can be manipulated to produce disallowed outputs. For GPT-6, the original TIP attack was extended with additional techniques to overcome the model&\#x27;s improved safety measures.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2501.18626">[2501.18626] The TIP of the Iceberg: Revealing a Hidden Class of Task-in-Prompt Adversarial Attacks on LLMs</a></li>
<li><a href="https://aclanthology.org/2025.acl-long.334/">The TIP of the Iceberg: Revealing a Hidden Class of Task-in-Prompt Adversarial Attacks on LLMs - ACL Anthology</a></li>

</ul>
</details>

**Tags**: `#jailbreak`, `#AI safety`, `#GPT-6`, `#adversarial attacks`, `#Task-in-Prompt`

---

<a id="item-14"></a>
## [Applying Sliding Window Attention to Pretrained LLMs at Inference](https://www.reddit.com/r/MachineLearning/comments/1w8repz/applying_sliding_window_attention_to_pretrained/) ⭐️ 7.0/10

A reusable inference layer for pretrained Hugging Face causal LLMs applies sliding window attention with attention sinks, reducing KV cache memory from 923 MB to 3.5 MB at 16K context for Qwen2.5-7B and improving token generation speed. This enables memory-constrained long-context inference without expensive retraining, allowing deployment of large models on edge devices or with limited VRAM, and reducing latency in applications like chatbots. The implementation uses a circular buffer for KV cache, attention sinks to preserve initial tokens, and supports streaming prefill and chunked attention. The trade-off is potential quality degradation on tasks requiring information beyond the sliding window.

reddit · r/MachineLearning · /u/ahsaor8 · Sep 6, 09:23

**Background**: Sliding window attention restricts each token&\#x27;s attention to a local neighborhood of recent tokens, rather than all previous tokens, reducing memory and computation. Attention sinks are special tokens \(often at the beginning\) that absorb disproportionate attention, helping maintain stability. The KV cache stores key and value vectors from previous tokens to avoid recomputation during autoregressive generation, but its size grows linearly with context length, causing memory bottlenecks.

<details><summary>References</summary>
<ul>
<li><a href="https://sebastianraschka.com/faq/docs/sliding-window-attention.html">Sliding - window attention | Sebastian Raschka, PhD</a></li>
<li><a href="https://github.com/tomaarsen/attention_sinks">GitHub - tomaarsen/ attention _ sinks : Extend existing LLMs way...</a></li>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>

</ul>
</details>

**Tags**: `#sliding-window-attention`, `#inference-optimization`, `#kv-cache`, `#long-context`, `#memory-efficiency`

---

<a id="item-15"></a>
## [Using Blender with Coding Agents on macOS to Generate 3D Scenes](https://simonwillison.net/2026/Sep/5/blender-coding-agents-macos/) ⭐️ 6.0/10

Simon Willison demonstrated that coding agents like ChatGPT Codex can control Blender&\#x27;s Python API on macOS by simply prompting it to render a 3D scene \(e.g., a pelican riding a bicycle\), and shared the resulting image and script. This shows how AI coding agents can automate complex 3D software, lowering the barrier for non-experts to create sophisticated 3D content and pointing to a future of AI-assisted creative workflows. The process used ChatGPT Codex with the gpt-6-astra model, costing an estimated $4.24 at API prices. The final Python script is available on GitHub, and the method requires the Blender Mac application installed at /Applications/Blender.

rss · Simon Willison · Sep 5, 15:51

**Background**: Blender is a free, open-source 3D creation suite with a comprehensive Python API for scripting. Coding agents are AI tools that can write and execute code in a sandboxed environment, such as ChatGPT Codex. By combining them, users can instruct the agent to generate and run Blender Python scripts to create 3D renders without manual interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.blender.org/api/current/index.html">Blender Python API</a></li>
<li><a href="https://docs.blender.org/api/current/info_overview.html">API Overview - Blender Python API</a></li>

</ul>
</details>

**Tags**: `#Blender`, `#coding agents`, `#macOS`, `#AI`, `#Python`

---

<a id="item-16"></a>
## [Is Reproducibility Becoming Irrelevant in Machine Learning Research?](https://www.reddit.com/r/MachineLearning/comments/1w92eis/reproducibility_seems_to_be_headed_towards/) ⭐️ 6.0/10

A machine learning researcher argues that reproducibility is becoming a lost cause, citing three trends: the shift to expensive physical AI setups, unverifiable corporate claims, and selective demo cherry-picking. This threatens the scientific integrity of ML research, potentially slowing progress and eroding trust in AI systems deployed in safety-critical settings. The post highlights three specific threats: costly physical AI laboratories, unverifiable corporate performance metrics, and the incentive to only show successful demos, which may mask underlying system fragility.

reddit · r/MachineLearning · /u/NeighborhoodFatCat · Sep 6, 17:29

**Background**: Physical AI refers to AI systems that perceive and act in the physical world—like robots and autonomous vehicles—combining AI models with sensors, actuators, and real-world hardware. Reproducibility in such systems is inherently difficult because experiments require specialized equipment and controlled environments that are not easily shared or replicated.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Physical_AI">Physical AI</a></li>

</ul>
</details>

**Tags**: `#reproducibility`, `#machine learning`, `#research`, `#AI ethics`, `#physical AI`

---