---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 39 items, 21 important content pieces were selected

---

1. [Encrypted LLM Reasoning Traces Exposed by Cross-Model Replay Attack](#item-1) ⭐️ 9.0/10
2. [Compression is prediction](#item-2) ⭐️ 8.0/10
3. [Making Holograms with a Pen Plotter](#item-3) ⭐️ 8.0/10
4. [Meta Releases Muse Glimmer: 30B Open-Weight Agentic AI Model Under Apache 2.0](#item-4) ⭐️ 8.0/10
5. [Long Benign Context Causes Activation Drift That Neutralizes RLHF Alignment in Gemma-3-1b-it](#item-5) ⭐️ 8.0/10
6. [WorldClaw: LLM-Driven Agentic Generation of 3D Open Worlds](#item-6) ⭐️ 7.0/10
7. [Nvidia Releases Nemotron 3.5 Lightning MoE Model and NeMo Switchyard](#item-7) ⭐️ 7.0/10
8. [Mojo 1.0 Released as Python-Compatible Language for AI Workloads](#item-8) ⭐️ 7.0/10
9. [OpenAI’s Head of Ethics Resigns After Less Than a Year](#item-9) ⭐️ 7.0/10
10. [Grok Bot: Persistent AI Agents with Browser Credential Snatching Spark Debate](#item-10) ⭐️ 7.0/10
11. [Go is an ideal language for AI-assisted software engineering](#item-11) ⭐️ 7.0/10
12. [Decoupled Descent: Enforcing Exact Train-Test Error Tracking Via AMP Onsager Corrections](#item-12) ⭐️ 7.0/10
13. [HyperSAE: Decoupled Poincaré Geometry for Sparse Autoencoders](#item-13) ⭐️ 7.0/10
14. [Manual Weight Setting Achieves 100% Multiplication Accuracy in Transformer](#item-14) ⭐️ 7.0/10
15. [CVPR 2026 Paper Fails to Release Promised Dataset, Prompting Complaint](#item-15) ⭐️ 7.0/10
16. [fru: A Fast Rust-Based Random Forest Library with Python and R Bindings](#item-16) ⭐️ 7.0/10
17. [How We Used to Get Jobs: A Nostalgic Look at Pre-Internet Job Hunting](#item-17) ⭐️ 6.0/10
18. [England set to be one of the first countries to eliminate hepatitis C](#item-18) ⭐️ 6.0/10
19. [No Lossless Natural Language Transformations Exist; Engineers Must Take Full Responsibility](#item-19) ⭐️ 6.0/10
20. [Agentic World Cup: LLMs Compete in 1v1 Soccer to Close Embodiment Gap](#item-20) ⭐️ 6.0/10
21. [Synthetic Query Probing: A Simple Method to Compare Embedding Models](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Encrypted LLM Reasoning Traces Exposed by Cross-Model Replay Attack](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/#atom-everything) ⭐️ 9.0/10

A new paper demonstrates that encrypted chain-of-thought blocks from Anthropic, OpenAI, and Google APIs can be replayed into weaker sibling models, jailbroken, and then recovered in plaintext, exposing the hidden reasoning traces of frontier models. This attack reveals a critical vulnerability in how LLM providers protect proprietary reasoning, threatening intellectual property, AI safety, and user privacy, and showing that encryption alone is insufficient if cross-model compatibility is allowed. The attack exploits the fact that models in the same family share the same encryption key; it used a specific jailbreak prompt and pre-filled assistant response on Claude Haiku 4.5. The vulnerability has since been patched, and the paper extracted 315,320 reasoning blocks, revealing 367 PII artifacts and 182 credentials, as well as demonstrating anti-distillation bypass and invisible prompt injection.

rss · Simon Willison · Aug 11, 22:40

**Background**: Chain-of-thought \(CoT\) reasoning is the intermediate reasoning steps LLMs generate internally before answering. Providers recently began encrypting these traces to protect intellectual property and prevent extraction. The attack succeeds because the encrypted blocks are portable across models due to cross-model compatibility features, and weaker models can be jailbroken to dump the plaintext reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://stolen-thoughts.com/paper.pdf">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://www.explainx.ai/blog/stealing-reasoning-traces-encrypted-cot-vulnerability-august-2026">Stealing Reasoning Traces: The Encrypted Chain-of-Thought ...</a></li>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes Hidden Reasoning Traces</a></li>

</ul>
</details>

**Discussion**: Some commenters questioned the term &\#x27;stealing,&\#x27; arguing that users pay for tokens and that training on model outputs is common practice; others noted that disabling reasoning and using a &\#x27;deep\_think&\#x27; tool achieves similar results. Additional comments pointed out that the traces suggest training data contamination and that models may have an index of problems.

**Tags**: `#LLM security`, `#chain-of-thought`, `#model extraction`, `#AI safety`, `#API vulnerabilities`

---

<a id="item-2"></a>
## [Compression is prediction](https://ngrok.com/blog/compression-is-prediction) ⭐️ 8.0/10

The article explores the deep equivalence between data compression and prediction, illustrating how information theory and machine learning are fundamentally interconnected. This insight unifies two major fields, suggesting that advances in compression can directly improve predictive models, and vice versa, with implications for artificial intelligence, neuroscience, and physics. The equivalence is supported by concepts like prediction by partial matching, Kolmogorov complexity, and normalized compression distance. The article draws from the Cambridge course &\#x27;Information Theory, Inference, and Learning Algorithms&\#x27; and related works.

hackernews · nikolay · Aug 11, 19:49 · [Discussion](https://news.ycombinator.com/item?id=49263497)

**Background**: Information theory deals with the quantification and communication of information, while data compression reduces file sizes by exploiting patterns. Prediction involves forecasting future data. The equivalence stems from the fact that a predictor can encode only unexpected data, and a compressor can be turned into a predictor by estimating probabilities. This connection is rooted in the minimum description length principle and Kolmogorov complexity, which measures the shortest program that produces a given data string.

**Discussion**: Commenters largely endorse the connection, citing David MacKay&\#x27;s Cambridge course and Grant Sanderson&\#x27;s video series. Some argue that compression may not always imply prediction, as compressors can exploit global patterns without sequential prediction. Physics laws are praised as the ultimate compression, enabling prediction and the industrial revolution. The discussion also mentions technical depths like normalized compression distance and Kolmogorov complexity.

**Tags**: `#information theory`, `#machine learning`, `#data compression`, `#prediction`, `#intelligence`

---

<a id="item-3"></a>
## [Making Holograms with a Pen Plotter](https://blog.jordan.matelsky.com/Penplotter-holography/) ⭐️ 8.0/10

A blog post details a novel DIY technique for creating holograms using a pen plotter and simple materials like olive oil and a phone screen, demonstrating the underlying physics of scratch holography. This hack makes holography accessible to hobbyists without expensive equipment, sparking creativity and community-driven improvements that could lead to new artistic and educational applications. The method likely involves drawing precise arcs with the plotter to create scratch holograms; community members suggested using a needle instead of a pen for finer lines, and a piezoelectric disk for even higher precision.

hackernews · DemiGuru · Aug 11, 18:51 · [Discussion](https://news.ycombinator.com/item?id=49262811)

**Background**: A pen plotter is a machine that draws vector graphics using a pen or other tool. Scratch holography, or abrasion holography, creates holographic images by scratching arcs on a reflective surface; each arc acts like a mirror to reconstruct a 3D light field. The technique can be demonstrated with common materials like an oily fingerprint on a phone screen, which bends light similarly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pen_plotter">Pen plotter</a></li>

</ul>
</details>

**Discussion**: Commenters praised the &\#x27;old Internet&\#x27; fun style and noted related resources: abrasion holography with hand-drawn lines, a Steve Mould video explaining the physics, and suggestions to use a needle or piezoelectric scanner for finer details. Some joked about chocolate as a medium.

**Tags**: `#holography`, `#pen-plotter`, `#diy`, `#optics`, `#hardware-hacking`

---

<a id="item-4"></a>
## [Meta Releases Muse Glimmer: 30B Open-Weight Agentic AI Model Under Apache 2.0](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

Meta released Muse Glimmer, a new 30-billion-parameter open-weight model under the Apache 2.0 license, optimized for agentic task completion, reliable tool use, and multi-step reasoning. It is a vision model capable of describing images and handling complex tool-calling workflows. The permissive Apache 2.0 license and 30B size make it ideal for local deployment on consumer hardware, democratizing access to powerful agentic AI that can autonomously use tools and complete multi-step tasks. This addresses the growing demand for open-weight models that can reliably function as agents, potentially accelerating the development of local AI assistants. The model performs well on benchmarks like DeepSearch QA, MCP-Atlas, τ-Bench, and SWE-Bench, and Simon Willison demonstrated its tool-calling abilities with his llm-coding-agent plugin, though it struggled with precise image generation like a pelican SVG. It requires about 18GB of storage in quantized form, leaving headroom on 32GB systems for other applications.

rss · Simon Willison · Aug 10, 23:56

**Background**: Open-weight models are AI models whose trained parameters are publicly released, allowing anyone to run and modify them. Agentic AI refers to AI systems that can autonomously pursue goals, use tools, and take actions, as opposed to chatbots that simply answer questions. The Apache 2.0 license is a permissive open-source license that allows commercial use, modification, and distribution without requiring derivative works to be open-sourced. SWE-Bench is a benchmark for evaluating AI models on real-world software engineering tasks, while DeepSearchQA tests multi-step information retrieval and reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2601.20975">[2601.20975] DeepSearchQA: Bridging the Comprehensiveness Gap ... DeepSearchQA:Bridgingthe ComprehensivenessGapforDeepResearch ... Evals — Google DeepMind DeepSearchQA: Bridging the Comprehensiveness Gap for Deep ... DeepSearchQA Leaderboard DeepSearchQA Evaluation for AI-Q Deep Researcher</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#AI`, `#language-model`, `#agentic-ai`, `#meta`

---

<a id="item-5"></a>
## [Long Benign Context Causes Activation Drift That Neutralizes RLHF Alignment in Gemma-3-1b-it](https://www.reddit.com/r/MachineLearning/comments/1vm16hs/contextinduced_activation_drift_long_benign/) ⭐️ 8.0/10

Researchers found that feeding a long, benign, thematically coherent context \(100–3000 tokens\) to google/gemma-3-1b-it causes a massive passive shift in internal activations at deep layers, which decouples RLHF alignment and neutralizes refusal templates without any adversarial prompts. A shuffled-text ablation confirmed the drift is semantics-driven, not an artifact of sequence length. This reveals a previously unknown vulnerability in RLHF alignment: even non-adversarial, benign text can passively undermine safety mechanisms. It has significant implications for AI safety, as it suggests that aligned models may become unsafe when processing long documents or conversations, potentially affecting deployment in real-world applications. The drift was measured at approximately 85% network depth \(Layer 22\), with a KL divergence of ~22.87 nats and a 325x entropy surge for coherent contexts. The shuffled-text ablation showed consistently lower KL divergence \(~8 nats\) and different model responses, confirming that semantic coherence, not just length, triggers the drift.

reddit · r/MachineLearning · /u/PresentSituation8736 · Aug 12, 02:09

**Background**: RLHF \(Reinforcement Learning from Human Feedback\) is a technique to align language models with human preferences, training them to refuse harmful requests. Mechanistic interpretability aims to understand neural networks&\#x27; internal computations. Activation drift refers to gradual changes in neural activations that can alter model behavior. Gemma-3-1b-it is a small instruction-tuned model from Google.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/progressive-activation-drift">Progressive Activation Drift - emergentmind.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/RLHF">RLHF</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>

</ul>
</details>

**Tags**: `#RLHF`, `#alignment`, `#mechanistic interpretability`, `#activation drift`, `#AI safety`

---

<a id="item-6"></a>
## [WorldClaw: LLM-Driven Agentic Generation of 3D Open Worlds](https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/) ⭐️ 7.0/10

Tencent&\#x27;s WorldClaw introduces a novel approach to 3D open-world generation: an LLM-driven agentic pipeline uses image composition to create scene layouts, then extracts 3D objects via SAM3D for placement, enabling scalable procedural generation from text. The framework demonstrates a practical technique for scalable world generation, potentially lowering the barrier for indie developers to create expansive environments; however, it may not yet match the hand-crafted detail needed for narrative-driven open-world games. The system is not a single model but a pipeline of Python scripts that call external models; the code is not publicly available. The composition step uses an image model to generate scene layouts, and then tools like SAM3D extract objects into 3D. The generated worlds often exhibit artifacts like misplaced buildings and inconsistent water levels.

hackernews · EwanG · Aug 11, 21:56 · [Discussion](https://news.ycombinator.com/item?id=49265051)

**Background**: Procedural generation \(PCG\) has long been used in games to create large worlds algorithmically, but often lacks coherence. Large language models \(LLMs\) can reason about world structure, while image generation models excel at composition. WorldClaw combines these by using an LLM to plan the world, an image model to compose a scene, and a 3D object extraction method \(like SAM3D\) to place objects. This builds on recent advances in AI-driven 3D reconstruction and segmentation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.05248v1">WorldClaw Agentic 3D Open-World Generation at Scale</a></li>

</ul>
</details>

**Discussion**: Comments highlight both interest and skepticism. The composition-then-extraction technique is praised as novel, but users note that the generated worlds lack the hand-crafted detail of games like Skyrim, and artifacts like floating buildings are common. Some argue it&\#x27;s better suited for mass production of gacha games than for immersive open-world experiences. There&\#x27;s also concern about code being closed-source, limiting reproducibility.

**Tags**: `#3D generation`, `#procedural generation`, `#AI`, `#open-world`, `#LLM`

---

<a id="item-7"></a>
## [Nvidia Releases Nemotron 3.5 Lightning MoE Model and NeMo Switchyard](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) ⭐️ 7.0/10

Nvidia announced Nemotron 3.5 Lightning, a 30B-parameter Mixture-of-Experts \(MoE\) model with only 3B active parameters, optimized for fast agentic task execution, and NeMo Switchyard, an open-source library for intelligently routing agent requests to the most suitable model. This release accelerates the industry shift toward small, efficient models for always-on agentic AI, delivering up to 4x faster output speed and a routing framework that can reduce costs and improve quality by dynamically selecting the best model per task. Nemotron 3.5 Lightning uses speculative decoding to achieve its speed, and NeMo Switchyard routes requests based on model capabilities, cost, and infrastructure signals, supporting OpenAI and Anthropic API formats.

hackernews · droidjj · Aug 11, 19:35 · [Discussion](https://news.ycombinator.com/item?id=49263340)

**Background**: Mixture-of-Experts models divide an AI model into multiple specialized sub-networks, activating only a subset for each input, which reduces compute cost. Nvidia&\#x27;s NeMo platform is a framework for training and customizing AI models. The trend toward smaller, efficient models is driven by cost and deployment constraints, especially for agentic workflows that require continuous, low-latency operation.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/">NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver Faster, Smarter, More Efficient Agentic AI | NVIDIA Blog</a></li>
<li><a href="https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4">nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4 · Hugging Face</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>

</ul>
</details>

**Discussion**: Community comments reflect mixed sentiment: some users found MoE models like Nemotron 3.5 Lightning perform poorly on complex coding tasks compared to dense models, while others see the push toward small efficient models as a necessary evolution. Concerns were raised about how model routers handle prompt caching, and a call for more honest benchmarking against models like Qwen was made.

**Tags**: `#NVIDIA`, `#MoE`, `#AI model`, `#model routing`, `#small models`

---

<a id="item-8"></a>
## [Mojo 1.0 Released as Python-Compatible Language for AI Workloads](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 7.0/10

Modular Inc. has officially released Mojo 1.0, a systems programming language with Python-like syntax, optimized for high-performance AI and heterogeneous computing. The release marks a stable milestone for the language, which targets CPUs, GPUs, and other accelerators using the MLIR compiler framework. Mojo aims to combine Python&\#x27;s ease of use with the speed of compiled languages, enabling developers to write performance-critical code without leaving the Python ecosystem. Its ability to directly target diverse hardware makes it significant for AI infrastructure and edge computing. Mojo is built on MLIR, not LLVM, allowing higher-level compiler optimizations and direct hardware targeting. The compiler is currently closed-source, with a plan to open source in fall 2026; the original goal of being a full Python superset may not be fully realized.

hackernews · dayanruben · Aug 11, 16:56 · [Discussion](https://news.ycombinator.com/item?id=49261128)

**Background**: Mojo is developed by Modular Inc., a company founded by former Google engineers, aiming to solve the performance bottleneck of Python in AI and numerical computing. It leverages MLIR \(Multi-Level Intermediate Representation\), a modern compiler infrastructure that enables efficient code generation across diverse hardware like CPUs, GPUs, and NPUs. Unlike Python, Mojo provides static typing, ownership semantics, and direct hardware control, bridging the gap between ease of development and maximum performance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed, with many expressing skepticism about the closed-source compiler and questioning the value over Python with Rust-backed libraries. Some are disappointed that the goal of being a full Python superset may be abandoned, and the 2026 open-source timeline is not reassuring. However, a few remain hopeful for Mojo&\#x27;s potential.

**Tags**: `#mojo`, `#python`, `#programming-languages`, `#ai`, `#release`

---

<a id="item-9"></a>
## [OpenAI’s Head of Ethics Resigns After Less Than a Year](https://www.ft.com/content/e49dfb75-f841-4466-a577-f7aaff8779a0) ⭐️ 7.0/10

Chloe Bakalar, OpenAI&\#x27;s head of ethics, resigned less than a year after joining the company, having previously served as chief ethicist at Meta. Her departure occurred shortly after the HuggingFace hacking incident, fueling speculation about the company&\#x27;s commitment to AI safety. The resignation of a high-profile ethics leader at a top AI company raises questions about the genuine influence of ethics departments and whether they can meaningfully shape product development. It highlights broader industry concerns about AI safety and corporate governance. The article lacks specific reasons for her departure, but notes the timing after the HuggingFace incident. Community members point out that she spent six years at Meta, so she is likely aware of the limitations of ethics roles, suggesting other factors may be at play.

hackernews · ilamont · Aug 11, 12:23 · [Discussion](https://news.ycombinator.com/item?id=49257160)

**Background**: OpenAI is the leading AI research lab behind ChatGPT, and ethics teams are often created to guide responsible AI development. The industry frequently debates whether such roles have real authority or serve primarily as public relations. The HuggingFace hacking incident refers to a security breach at the machine learning platform Hugging Face, which may have raised concerns about model security and alignment.

**Discussion**: Comments range from cynicism that ethics teams are just PR stunts with no real power, to speculation that the departure might be due to other factors like the HuggingFace incident or internal dynamics. One commenter notes she was at Meta for 6 years, so she knew what she was getting into, implying the situation is not as simple as ethics being a mere PR move. Overall, sentiment is skeptical about the effectiveness of ethics roles in AI companies.

**Tags**: `#AI ethics`, `#OpenAI`, `#corporate governance`, `#technology industry`, `#AI safety`

---

<a id="item-10"></a>
## [Grok Bot: Persistent AI Agents with Browser Credential Snatching Spark Debate](https://x.ai/bot) ⭐️ 7.0/10

x.ai&\#x27;s Grok Bot introduces a new paradigm of persistent AI agents that can own routines, communicate with each other, and access browser data, including credentials. A demo video on the bot&\#x27;s page shows the agent snatching browser credentials, fueling intense debate over security and privacy. This marks a potential evolution from chatbots to persistent agents that autonomously handle tasks, but the credential-snatching capability raises serious security, privacy, and legal questions. It could accelerate adoption of AI agents while forcing a reckoning over bot access to personal data and the rules for automated interactions with websites. The agents are persistent, with each owning its own routines and context, and they can intercommunicate. The demo shows the bot directly extracting credentials from the browser, a technique similar to known credential-stealing attacks \(MITRE T1555.003\), which would allow it to take over user accounts, blurring the line between legitimate automation and malicious bot activity.

hackernews · rvz · Aug 11, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49261514)

**Background**: Persistent AI agents are always-on assistants that retain memory, permissions, and tool access across sessions, going beyond simple chatbots. Browser credential stealing is a common attack where adversaries extract saved passwords and cookies from web browsers to hijack accounts. The conflict between bots and anti-bot systems has been ongoing, with websites using CAPTCHAs and fingerprinting to block automated access, while bots evolve to mimic human behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tigerdata.com/learn/building-ai-agents-with-persistent-memory-a-unified-database-approach">Building AI Agents with Persistent Memory | Tiger Data</a></li>
<li><a href="https://fourcore.io/blogs/threat-hunting-browser-credential-stealing">Threat Hunting: Detecting Browser Credential Stealing [T1555.003]</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bot_prevention">Bot prevention - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed. Some users are impressed by the natural interaction model and the paradigm shift toward persistent, communicating agents, calling it an evolutionary step. However, many express deep concern about the security implications of a bot that can snatch browser credentials, fearing data leaks, account hijacking, and prompt injection attacks. The debate also touches on the legal and ethical aspects of automated credential access and the conflicting stance of companies that both deploy bots and fight against them.

**Tags**: `#AI agents`, `#automation`, `#security`, `#privacy`, `#Grok`

---

<a id="item-11"></a>
## [Go is an ideal language for AI-assisted software engineering](https://developers.googleblog.com/why-go-is-an-ideal-language-for-ai-assisted-software-engineering/) ⭐️ 7.0/10

Google&\#x27;s Go language creator published a blog post arguing that Go&\#x27;s simplicity and strong engineering practices make it ideal for AI-generated code, sparking significant debate. As AI-assisted coding tools become mainstream, the choice of programming language could influence code quality, developer productivity, and the adoption of AI in software engineering. The post highlights Go&\#x27;s readability, fast compilation, and standardized tooling as advantages for LLM-generated code, but community commenters point out Go&\#x27;s limited abstraction capabilities and challenges with concurrent code generation.

hackernews · 0xedb · Aug 11, 16:57 · [Discussion](https://news.ycombinator.com/item?id=49261133)

**Background**: Go is a statically-typed compiled language designed for simplicity and concurrency, while AI coding assistants like GitHub Copilot use large language models to generate code. Language features such as type safety, compilation speed, and idiomatic style conventions can affect how accurately LLMs produce correct code.

**Discussion**: Comments are polarized. Some practitioners report that AI writes better Go code, but many argue the post is biased from Go&\#x27;s creator. Critics suggest Rust is more suitable because its compiler catches more errors at compile time, which better suits LLM workflows. Others note that Go&\#x27;s weak abstractions and concurrency pitfalls may lead to more low-quality AI-generated code.

**Tags**: `#Go`, `#AI-assisted programming`, `#LLMs`, `#software engineering`, `#programming languages`

---

<a id="item-12"></a>
## [Decoupled Descent: Enforcing Exact Train-Test Error Tracking Via AMP Onsager Corrections](https://www.reddit.com/r/MachineLearning/comments/1vlu1se/decoupled_descent_enforcing_exact_traintest_error/) ⭐️ 7.0/10

The paper introduces Decoupled Descent, a novel training method that leverages AMP Onsager corrections to asymptotically guarantee equal training and test error at each iteration of full-batch gradient descent on Gaussian mixture models. This addresses the fundamental problem of train-test error discrepancy in deep learning, offering theoretical guarantees that could improve generalization, inform optimal stopping, and inspire extensions to stochastic gradient descent and larger models. The method is tested on a high-dimensional XOR problem with a two-layer network, comparing training and test error quantiles over 100 simulations; it currently only supports full-batch GD and is theoretical, with no PyTorch package yet.

reddit · r/MachineLearning · /u/mlovik1 · Aug 11, 21:06

**Background**: Approximate Message Passing \(AMP\) is an iterative algorithm for high-dimensional inference that uses an Onsager correction term to remove correlations between the current error and previous residuals, enabling accurate performance predictions via state evolution. The Onsager correction subtracts a weighted prior message based on the divergence of the denoiser, which is crucial for correcting the data reuse bias inherent in gradient descent. In the context of Gaussian mixture models, this bias causes the training error to diverge from the test error; the Decoupled Descent method uses AMP to correct it, asymptotically equalizing the two.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/approximate-message-passing-amp">AMP: Iterative Algorithms for High-Dimensional Inference</a></li>
<li><a href="https://www.emergentmind.com/topics/onsager-correction-in-goamp">Onsager Correction in GOAMP</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#optimization`, `#generalization`, `#approximate message passing`, `#train-test discrepancy`

---

<a id="item-13"></a>
## [HyperSAE: Decoupled Poincaré Geometry for Sparse Autoencoders](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/) ⭐️ 7.0/10

HyperSAE introduces a decoupled Poincaré hyperbolic geometry approach to sparse autoencoders, achieving a 9.8% reduction in reconstruction MSE and only 0.2% dead latents on Gemma-2-2B, while maintaining zero inference overhead. This addresses fundamental scalability issues in SAEs by aligning geometry with hierarchical concept structures, potentially improving mechanistic interpretability of larger language models and enabling more efficient feature disentanglement. The architecture projects dictionary weights onto the Poincaré ball during training using an entailment cone loss, while the forward pass remains Euclidean, preserving causal steering as a single vector addition. The TriPartite loss combines reconstruction, L1 sparsity, and entailment terms.

reddit · r/MachineLearning · /u/visha1v · Aug 11, 18:37 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/)

**Background**: Sparse autoencoders \(SAEs\) are used in mechanistic interpretability to decompose a language model&\#x27;s activations into a sparse set of interpretable features, or &\#x27;dictionary atoms&\#x27;. Typically, these atoms are embedded in Euclidean space, but the hierarchical nature of concepts in LLMs is better captured by hyperbolic geometry, where volume grows exponentially, like the Poincaré disk model. This geometric mismatch causes feature collisions and dead latents in standard SAEs. HyperSAE resolves this by using a decoupled hyperbolic geometry during training.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Poincar%C3%A9_disk_model">Poincaré disk model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sparse_Auto-Encoders">Sparse Auto-Encoders</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>

</ul>
</details>

**Tags**: `#Sparse Autoencoders`, `#Mechanistic Interpretability`, `#Hyperbolic Geometry`, `#Language Models`, `#Open Source`

---

<a id="item-14"></a>
## [Manual Weight Setting Achieves 100% Multiplication Accuracy in Transformer](https://www.reddit.com/r/MachineLearning/comments/1vkrnb5/transformers_are_famously_bad_at_arithmetic_so_i/) ⭐️ 7.0/10

A Reddit user directly compiled a grade-school multiplication algorithm into the weights of a Phi-3 transformer using the custom torchwright compiler, without any training, achieving 100% accuracy on up to 12-digit multiplication and releasing checkpoints. It shows that transformers can perform exact arithmetic if their weights are appropriately chosen, countering the common belief that they are inherently poor at arithmetic. This approach also opens new avenues for mechanistic interpretability and understanding transformer computational capabilities. The implementation uses the grade-school algorithm, and the author also built hardware-style, scratchpad, and brute-force memorization variants. The three-digit calculator handles all 3 million supported expressions perfectly. The torchwright compiler treats the transformer as a fixed computational substrate, setting weights directly without training.

reddit · r/MachineLearning · /u/notforrob · Aug 10, 17:37

**Background**: Transformers are a neural network architecture widely used in large language models, but they are notoriously bad at arithmetic reasoning unless specially trained. Mechanistic interpretability is a field that aims to reverse-engineer the internal computations of neural networks. The torchwright compiler, introduced by the same author, transforms computation graphs into transformer weights, enabling direct programming of the model.

<details><summary>References</summary>
<ul>
<li><a href="https://ood.dev/posts/torchwright-intro/">Introducing torchwright — Out of Distribution</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#arithmetic`, `#mechanistic-interpretability`, `#manual-weight-engineering`, `#compilation`

---

<a id="item-15"></a>
## [CVPR 2026 Paper Fails to Release Promised Dataset, Prompting Complaint](https://www.reddit.com/r/MachineLearning/comments/1vkn5x9/how_to_file_a_complaint_about_a_published_cvpr/) ⭐️ 7.0/10

A Reddit user is seeking guidance on how to file a complaint about a CVPR 2026 paper whose main contribution is a dataset that was never released, despite the paper pointing to an empty GitHub repository and the authors being unresponsive. The user notes that the dataset was not made available before, during, or after the conference, violating CVPR&\#x27;s explicit requirement. This incident exposes a critical lapse in enforcing reproducibility and dataset-release policies at a top-tier conference, undermining trust in academic integrity. It may affect the credibility of CVPR publications and the broader push for open science in machine learning. The paper&\#x27;s GitHub link is empty, and the authors have not responded to inquiries. The user claims the dataset was never released at any point, directly contradicting CVPR&\#x27;s requirement that datasets claimed as contributions must be made public by the camera-ready deadline or upon publication.

reddit · r/MachineLearning · /u/ElPelana · Aug 10, 14:56

**Background**: CVPR \(Conference on Computer Vision and Pattern Recognition\) is a premier annual conference for computer vision and AI research. Its author guidelines state that if a paper claims a new dataset as a major contribution, the dataset must be made publicly available no later than the camera-ready deadline. Reviewer guidelines also specify that there should be a reasonable expectation that the dataset will be available upon publication. Failure to comply can lead to a paper being rejected or investigated.

<details><summary>References</summary>
<ul>
<li><a href="https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines">CVPR 2026 Author Guidelines</a></li>
<li><a href="https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelines">CVPR 2026 Reviewer Guidelines</a></li>

</ul>
</details>

**Tags**: `#academic integrity`, `#reproducibility`, `#dataset`, `#CVPR`, `#machine learning`

---

<a id="item-16"></a>
## [fru: A Fast Rust-Based Random Forest Library with Python and R Bindings](https://www.reddit.com/r/MachineLearning/comments/1vkrvks/fru_fast_random_forest_implementation_p/) ⭐️ 7.0/10

A new Rust-based Random Forest library called fru has been published in Software X, featuring Python and R bindings and delivering orders-of-magnitude speedups over scikit-learn in Python and competitive performance improvements in R, along with a novel permutation importance implementation. This library offers substantial performance gains for random forest models, which are widely used in industry and research, enabling faster experimentation and deployment, and its seamless integration with popular data tools via Arrow PyCapsule lowers the barrier to adoption. The library is implemented in Rust for performance, and its Python bindings leverage the Arrow PyCapsule interface for efficient data interchange with pandas, polars, and pyarrow, avoiding unnecessary copies. The novel permutation importance method adds to its feature set.

reddit · r/MachineLearning · /u/kpiwonski · Aug 10, 17:45

**Background**: Random forests are a popular ensemble machine learning method for classification and regression. In Python, scikit-learn provides a widely used implementation, but it can be slow for large datasets. The ranger package in R is a fast alternative. Rust is a systems programming language that offers memory safety and high performance, making it attractive for building efficient ML backends. The Arrow PyCapsule interface is a Python-specific protocol that allows libraries to share Arrow columnar data efficiently, enabling zero-copy integration between tools like pandas, polars, and pyarrow.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Permutation_importance">Permutation importance</a></li>
<li><a href="https://arrow.apache.org/docs/format/CDataInterface/PyCapsuleInterface.html">The Arrow PyCapsule Interface — Apache Arrow v25.0.0</a></li>
<li><a href="https://cran.r-project.org/package=ranger">CRAN: Package ranger</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#random-forest`, `#rust`, `#performance`, `#python`

---

<a id="item-17"></a>
## [How We Used to Get Jobs: A Nostalgic Look at Pre-Internet Job Hunting](https://ironicsans.ghost.io/how-we-used-to-get-jobs/) ⭐️ 6.0/10

An article on Ironic Sans recounts pre-internet job hunting methods like newspaper classifieds, USENET postings, and hand-delivered resumes, sparking a rich community discussion with 93 comments and 118 points on Hacker News. It highlights how drastically job searching has changed, offering perspective on the impersonal nature of modern automated hiring systems and the loss of personal touch and serendipity in the process. The piece is a nostalgic reflection rather than a technical analysis, and the community anecdotes include specific practices like mailing resumes, using answering machines, finding tech jobs on USENET, and taking aptitude tests at IBM in the 1960s.

hackernews · speckx · Aug 11, 18:09 · [Discussion](https://news.ycombinator.com/item?id=49262211)

**Background**: Before the internet, job seekers relied heavily on newspaper classified ads, where employers listed openings. USENET, a distributed discussion system created in 1980, was an early online platform where tech jobs were sometimes advertised in newsgroups. Resumes were often mailed or hand-delivered, and communication was slower, involving phone calls and answering machines.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Usenet">Usenet</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal stories of finding jobs via USENET, hand-delivered resumes, and aptitude tests. Some argued that the older methods acted as a useful effort and presentation filter, reducing candidate overload and encouraging employers to invest more in employees, while others simply reminisced about the slower, more personal process.

**Tags**: `#job hunting`, `#tech history`, `#nostalgia`, `#career`, `#hiring`

---

<a id="item-18"></a>
## [England set to be one of the first countries to eliminate hepatitis C](https://www.bbc.com/news/articles/c75gk620r22o) ⭐️ 6.0/10

England is poised to become one of the first countries globally to eliminate hepatitis C as a public health threat, thanks to a comprehensive NHS screening and treatment program. This achievement would mark a major public health victory, preventing liver disease and cancer, reducing long-term healthcare costs, and providing a model for other nations to eliminate a viral disease without a vaccine. The NHS England program combined widespread testing with direct-acting antiviral drugs that cure over 95% of cases, and it appears to have already contributed to a downturn in liver cancer rates since 2019. Notably, the initiative is specific to England and not yet uniformly rolled out across Scotland, Wales, or Northern Ireland.

hackernews · stevekemp · Aug 11, 12:41 · [Discussion](https://news.ycombinator.com/item?id=49257377)

**Background**: Hepatitis C is a blood-borne virus that can cause chronic liver disease, cirrhosis, and liver cancer. Unlike eradication \(global extinction of a pathogen\), elimination means stopping endemic transmission within a defined region. The WHO set a 2030 target for eliminating viral hepatitis, and England&\#x27;s NHS launched a pioneering program to find and treat undiagnosed cases, securing affordable drug deals to make treatment accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Eradication_of_infectious_diseases">Eradication of infectious diseases - Wikipedia</a></li>
<li><a href="https://healthjournalism.org/glossary-terms/disease-elimination-vs-eradication/">Disease elimination vs. eradication | Association of Health Care Journalists</a></li>

</ul>
</details>

**Discussion**: Comments are largely positive, with individuals sharing personal stories of early diagnosis and successful treatment. Some express frustration that the US lacks comparable public health efforts, while others question why the program is limited to England and not the whole UK. There is also interest in the program&\#x27;s possible impact on liver cancer rates.

**Tags**: `#public health`, `#hepatitis C`, `#NHS`, `#elimination`, `#UK`

---

<a id="item-19"></a>
## [No Lossless Natural Language Transformations Exist; Engineers Must Take Full Responsibility](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/#atom-everything) ⭐️ 6.0/10

Simon Willison endorsed Sophie Alpert’s policy on AI writing, emphasizing that engineers must stand behind every idea and sentence in their documents. The policy highlights that AI rewrites are inherently lossy and can introduce unwanted changes in meaning. As AI writing tools become commonplace, this principle reinforces accountability and trust, ensuring that AI-assisted content remains a genuine reflection of the author’s intent and not a source of miscommunication. The core rule: “You must stand behind every idea and every sentence in your docs.” If a reviewer questions a line, blaming the AI is unacceptable. The “no lossless transformations” concept means that any rewrite changes the original meaning, and AI lacks the writer’s full mental model, so information is always lost.

rss · Simon Willison · Aug 11, 23:48

**Background**: The original post was by Sophie Alpert, a former Facebook engineering manager and React core team member, and was shared by well-known developer Simon Willison. The term “lossless transformation” comes from data compression, where it means preserving all original information. Applied to natural language, it asserts that paraphrasing or rewriting inevitably alters subtle nuances. This discussion is part of a broader push for human oversight in AI-generated content.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/">There are no lossless transformations of natural-language text</a></li>
<li><a href="https://sophiebits.com/2026/06/25/there-are-no-lossless-transformations-of-natural-language-text">There are no lossless transformations of natural-language ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#writing`, `#software engineering`, `#LLMs`, `#ethics`

---

<a id="item-20"></a>
## [Agentic World Cup: LLMs Compete in 1v1 Soccer to Close Embodiment Gap](https://www.reddit.com/r/MachineLearning/comments/1vllvmn/we_built_the_agentic_world_cup_llms_that_compete/) ⭐️ 6.0/10

A new platform, the Agentic World Cup, allows users to submit LLM agents that compete in 1v1 soccer matches, aiming to benchmark embodied intelligence. The platform addresses the &\#x27;embodiment gap&\#x27; by evaluating how well LLMs can think and act in a dynamic sports environment. This project highlights the challenge of applying LLMs to embodied tasks, moving beyond text-based domains to dynamic physical simulations. It could spur research into agents that combine reasoning with real-time physical decision-making, relevant to robotics and embodied AI. Agents are coached through prompting, and the platform runs automated matches with weekly rankings. The long-term vision is to provide a public testing ground for various AI techniques, including vision transformers, online reinforcement learning, and neuro-symbolic systems.

reddit · r/MachineLearning · /u/agenticworldcup · Aug 11, 16:12

**Background**: Embodied intelligence is the concept that cognition is deeply influenced by an organism&\#x27;s physical body and its interactions with the environment. In AI, the &\#x27;embodiment gap&\#x27; refers to the difficulty of transferring learning from data or simulations to physical robots with different bodies and control systems. The Agentic World Cup uses a 1v1 soccer simulation to test how well LLMs can bridge this gap by reasoning and acting in a dynamic sports setting.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Embodied_intelligence">Embodied intelligence</a></li>
<li><a href="https://arxiv.org/abs/2504.12609">[2504.12609] Crossing the Human-Robot Embodiment Gap with Sim ... Crossing the Human-Robot Embodiment Gap with Sim-to-Real RL ... The Embodiment Gap: Why Robots Struggle to Learn from Humans The Embodiment Gap in Robot Foundation Models (PDF) Bridging the Embodiment Gap: Embodied AI for Enhanced ... Embodiment Gap: Definition &amp; Challenges in Robotics</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#Embodied AI`, `#Multi-agent Systems`, `#Simulation`, `#Benchmarking`

---

<a id="item-21"></a>
## [Synthetic Query Probing: A Simple Method to Compare Embedding Models](https://www.reddit.com/r/MachineLearning/comments/1vkh1ul/comparing_embedding_models_with_synthetic_query/) ⭐️ 6.0/10

The paper introduces Synthetic Query Probing, a method that compares embedding models by analyzing the relationship between their similarity scores on synthetic query-chunk pairs, rather than directly comparing embedding spaces. It reveals, for example, that Titan models of different dimensions exhibit semilinear similarity score relationships, while Titan and ADA scores are nonlinearly related. This approach helps practitioners understand how similarity scores map between models, aiding in model selection and threshold setting for retrieval tasks. It also provides insights into the fundamental structure of embedding spaces. The study used synthetic queries to probe similarity spaces, showing that Titan models of different dimensionalities \(e.g., V2\) are semilinearly related in similarity scores, while the relationship between Titan and OpenAI&\#x27;s ADA model is nonlinear with different score ranges. The paper is to be presented at Discovery Science 2026.

reddit · r/MachineLearning · /u/pppeer · Aug 10, 10:27

**Background**: Embedding models like OpenAI&\#x27;s text-embedding-ada-002 and Amazon&\#x27;s Titan Text Embeddings convert text into numerical vectors for semantic search and retrieval. Since different models produce different embedding spaces, their raw similarity scores are not directly comparable. Synthetic Query Probing uses synthetic queries to generate paired similarity scores across models, enabling comparison of the similarity score distributions without needing to align the embedding spaces.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/models/text-embedding-ada-002">text-embedding-ada-002 Model | OpenAI API</a></li>
<li><a href="https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html">Amazon Titan Text Embeddings models - Amazon Bedrock</a></li>

</ul>
</details>

**Tags**: `#embedding models`, `#similarity search`, `#model comparison`, `#synthetic queries`, `#retrieval`

---