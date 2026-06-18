---
layout: default
title: "Horizon Summary: 2026-06-18 (EN)"
date: 2026-06-18
lang: en
---

> From 40 items, 14 important content pieces were selected

---

1. [Lore: A New Open-Source Version Control System Designed to Challenge Perforce for Game Development](#item-1) ⭐️ 9.0/10
2. [RFC 10008 introduces the new HTTP QUERY method](#item-2) ⭐️ 9.0/10
3. [GLM-5.2 open weights released as leading 753B MoE text-only LLM](#item-3) ⭐️ 9.0/10
4. [Adam Launches CADAM: Open-Source Text-to-CAD Platform](#item-4) ⭐️ 8.0/10
5. [Georgi Gerganov Endorses Qwen3.6-27B for Daily Local Coding Tasks](#item-5) ⭐️ 8.0/10
6. [Midjourney Unveils Medical Imaging Initiative Lacking Prototype](#item-6) ⭐️ 7.0/10
7. [US postpones blacklisting DeepSeek as over 100 firms flagged for security risks](#item-7) ⭐️ 7.0/10
8. [Launching browsers in under 1s using Firecracker microVMs on EC2](#item-8) ⭐️ 7.0/10
9. [AI makes code generation free and instant, turning code into a disposable commodity](#item-9) ⭐️ 7.0/10
10. [Datasette 1.0a34 Adds Native Row Insert, Edit, and Delete](#item-10) ⭐️ 7.0/10
11. [Next-Latent Prediction Transformers: Learning Compact World Models for Faster Inference](#item-11) ⭐️ 7.0/10
12. [Using Contrastive Targeted SFT to Build Causal Dependency Graphs for Mechanistic Interpretability](#item-12) ⭐️ 7.0/10
13. [Researcher Asks How to Evaluate Relative Probe Strength in Transformer Models](#item-13) ⭐️ 6.0/10
14. [I deployed a GAN on a Raspberry Pi 4 and built a physical NFT minting device](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Lore: A New Open-Source Version Control System Designed to Challenge Perforce for Game Development](https://lore.org/) ⭐️ 9.0/10

Lore, a new open-source version control system, has been announced with a design specifically targeting the scalability challenges game developers face with large binary files, positioning itself as a direct alternative to Perforce. This addresses a major, long-standing gap in game development tooling, as Git struggles with large binary assets. An open-source competitor to Perforce could significantly lower costs and improve workflows for studios of all sizes. Lore is designed to support features critical for game development, such as exclusive file locking for artists and efficient handling of large files like textures and 3D models. It is not intended as a general-purpose competitor to Git for text-based code.

hackernews · regnerba · Jun 17, 14:30 · [Discussion](https://news.ycombinator.com/item?id=48571081)

**Background**: Game development involves large, non-text binary files (textures, 3D models, audio) that Git handles inefficiently. The industry standard, Perforce, excels with these large files and offers exclusive file locking, preventing merge conflicts on assets that cannot be merged. However, Perforce is proprietary and can be complex and costly, creating a demand for a scalable, open-source alternative.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Perforce">Perforce - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community discussion is highly engaged and largely optimistic. Commenters highlight a strong need for a Perforce challenger, particularly for Unreal Engine development, and critique Git's poor user interface and handling of binary files. Some note that while programmers may prefer Git, non-technical creative staff often dictate the choice of Perforce, making an improved, user-friendly alternative highly welcome.

**Tags**: `#version-control`, `#game-development`, `#open-source`, `#devtools`, `#scalability`

---

<a id="item-2"></a>
## [RFC 10008 introduces the new HTTP QUERY method](https://www.rfc-editor.org/info/rfc10008/) ⭐️ 9.0/10

RFC 10008 defines the new HTTP QUERY method, a safe, idempotent, and cacheable request that uses a request body to perform complex data queries, solving the long-standing problem of sending a body with GET requests. This foundational shift in web protocols finally provides a standard way to send complex queries (like large JSON filters or image inputs) to APIs without the side effects of POST or the interoperability issues of GET with a body, making web services more reliable and cacheable. The IETF working group expressly rejected standardizing GET-with-body in favor of QUERY due to historical compatibility issues and strict HTTP architectural semantics; QUERY must not cause any state change on the server, and its request body forms part of the cache key.

hackernews · schappim · Jun 17, 10:51 · [Discussion](https://news.ycombinator.com/item?id=48568502)

**Background**: For decades, developers resorted to using a GET request with a body for complex queries, but this practice was undefined and often caused failures with proxies and caches because HTTP specifications advised against it. An idempotent method, like GET or PUT, means making the same request multiple times has the same effect as making it once, which is crucial for automatic retries without data corruption.

<details><summary>References</summary>
<ul>
<li><a href="https://httpwg.org/http-extensions/draft-ietf-httpbis-safe-method-w-body.html">The HTTP QUERY Method</a></li>
<li><a href="https://www.baeldung.com/cs/http-get-with-body">Why an HTTP Get Request Shouldn’t Have a Body | Baeldung on Computer Science</a></li>

</ul>
</details>

**Discussion**: Commenters noted that QUERY could prevent browser re-submission warnings for refreshable form data and questioned practical caching strategies for unbounded request bodies. Some highlighted they have been using GET-with-body for years out of necessity, while others reflected on the historic milestone of reaching 5-digit RFC numbers.

**Tags**: `#http`, `#ietf`, `#rfc`, `#web-standards`, `#api-design`

---

<a id="item-3"></a>
## [GLM-5.2 open weights released as leading 753B MoE text-only LLM](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Chinese AI lab Z.ai released the full open weights of GLM-5.2 under an MIT license on June 16, 2026. The model is a 753B-parameter Mixture of Experts architecture with 40 active parameters and a 1 million token context window. This release represents a major advance in accessible AI, providing the most powerful text-only open-weights model available, which could accelerate innovation across the industry. Its MIT license allows unrestricted use and commercialization, sharply contrasting with closed-source models like GPT-5.5 and Claude Opus. GLM-5.2 tops the Artificial Analysis Intelligence Index v4.1 with a score of 51, and ranks 2nd on the Code Arena WebDev leaderboard behind Claude Fable 5. It is notably token-hungry, using 43k output tokens per task on average, and is priced at $1.40/million input and $4.40/million output tokens via OpenRouter.

rss · Simon Willison · Jun 17, 23:58

**Tags**: `#LLM`, `#open-weights`, `#GLM-5.2`, `#Mixture of Experts`, `#AI release`

---

<a id="item-4"></a>
## [Adam Launches CADAM: Open-Source Text-to-CAD Platform](https://github.com/Adam-CAD/CADAM) ⭐️ 8.0/10

YC-backed startup Adam released CADAM, an open-source React app that generates parametric 3D mechanical models from natural language prompts, using code as an intermediate representation. This approach lowers the barrier to mechanical design by allowing anyone to describe a part in plain English and get an editable 3D model, potentially accelerating prototyping and broadening access to CAD tools. CADAM uses OpenSCAD compiled to WebAssembly for in-browser rendering, supports model-agnostic LLM backends via Vercel AI SDK, and surprisingly found Gemini 3.1 Pro to be the top performer in its evaluations. Parameters are extracted as interactive sliders, and exports include STL, SCAD, OBJ, GLB, and DXF.

hackernews · zachdive · Jun 17, 16:14 · [Discussion](https://news.ycombinator.com/item?id=48572553)

**Background**: OpenSCAD is a script-based CAD tool where models are defined by code rather than mouse interactions. Text-to-CAD systems like CADAM use large language models to translate natural language into such code, enabling parametric adjustments and deterministic edits. The platform is built with TanStack Start, a full-stack React framework, and Supabase for backend services.

<details><summary>References</summary>
<ul>
<li><a href="https://tanstack.com/start/latest">TanStack Start</a></li>
<li><a href="https://supabase.com/">Supabase | The Postgres Development Platform.</a></li>

</ul>
</details>

**Discussion**: Discussion on Hacker News was mixed: some engineers expressed skepticism about time savings for real-world parts, while others shared successful examples like a grommet seal generated in seconds. There was also interest in supporting photo inputs and a self-promotion of a similar project.

**Tags**: `#AI`, `#CAD`, `#open-source`, `#YC`, `#generative-design`

---

<a id="item-5"></a>
## [Georgi Gerganov Endorses Qwen3.6-27B for Daily Local Coding Tasks](https://simonwillison.net/2026/Jun/16/georgi-gerganov/#atom-everything) ⭐️ 8.0/10

Georgi Gerganov, the creator of llama.cpp, has publicly attested that he has been using the Qwen3.6-27B model almost daily for over a month for small coding tasks at his ggml-org repository. He uses a lightweight setup with the 'pi' agent in offline mode and a custom system prompt to align the model with his coding style. This is a significant practical endorsement from a highly respected figure in local AI development. It validates that consumer-grade hardware like an M2 Ultra or RTX 5090 can run a 27B model effectively for real-world coding assistance, signaling that local coding models have reached a level of genuine utility for professional developers. Gerganov runs the model on an M2 Ultra or an RTX 5090 box, and uses a stripped-down version of the 'pi' agent with the command 'pi -nc --offline'. He links directly to a public system prompt he uses and the commits in ggml-org that were assisted by the model.

rss · Simon Willison · Jun 16, 16:04

**Background**: Georgi Gerganov is the creator of llama.cpp, a foundational open-source library that enables large language models to run efficiently on consumer devices. Qwen3.6-27B is an open-weight, 27-billion-parameter dense model from Alibaba's Qwen team, launched in April 2026, which reportedly outperforms much larger models on coding benchmarks. The 'pi' agent is an AI coding assistant that can interface with local models via llama.cpp.

<details><summary>References</summary>
<ul>
<li><a href="https://qwen.ai/blog?id=qwen3.6-27b">Qwen3.6-27B: Flagship-Level Coding in a 27B Dense Model</a></li>
<li><a href="https://huggingface.co/docs/hub/agents-local">Local Agents with llama.cpp · Hugging Face</a></li>
<li><a href="https://github.com/gsanhueza/pi-llama-cpp">GitHub - gsanhueza/pi-llama-cpp: Pi extension for llama.cpp ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#coding`, `#local-models`, `#Qwen`, `#llama.cpp`

---

<a id="item-6"></a>
## [Midjourney Unveils Medical Imaging Initiative Lacking Prototype](https://www.midjourney.com/medical/blogpost) ⭐️ 7.0/10

Midjourney announced a medical imaging initiative that aims to reduce radiation exposure and healthcare costs, but the company has not yet demonstrated a working prototype, only a video render. If realized, the technology could make CT-class imaging more accessible and safer, enabling earlier detection of aneurysms, cancers, and other conditions. However, the lack of concrete evidence fuels skepticism about overpromising. The promotional video highlights nanometer deflection sensitivity, which is only for signal amplification and does not directly determine image resolution. The initiative also raises data privacy concerns, as it would involve collecting a vast library of personal health data.

hackernews · ricochet11 · Jun 18, 01:59 · [Discussion](https://news.ycombinator.com/item?id=48579650)

**Background**: Midjourney is an AI company known for its text-to-image generation tool. CT scans use ionizing radiation that can increase cancer risk, while MRI is expensive and slow. The initiative proposes using AI to enhance low-dose imaging, but requires breakthroughs in hardware and software that have not yet been shown.

**Discussion**: Community discussion is largely skeptical, criticizing the lack of a working prototype and calling it overpromising. Some see potential in reducing radiation, but many raise data privacy risks and question feasibility. A technical comment clarifies that the nanometer sensitivity only relates to signal amplification, not image resolution.

**Tags**: `#AI`, `#medical-imaging`, `#healthcare`, `#hype`, `#startup`

---

<a id="item-7"></a>
## [US postpones blacklisting DeepSeek as over 100 firms flagged for security risks](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 7.0/10

The US government has decided to hold off on adding Chinese AI company DeepSeek to its trade blacklist, while simultaneously designating more than 100 other firms as security risks. This decision signals a nuanced approach to US-China tech restrictions, avoiding immediate escalation with a prominent open-source AI lab while maintaining broad pressure. It directly affects developers and businesses globally who rely on DeepSeek's affordable models for coding and other tasks. Being on the 'Entity List' does not ban all trade, but generally prohibits US companies from selling goods and services to listed firms; Chinese AI companies largely depend on US goods only for already-restricted NVIDIA GPUs, so the practical impact may be limited.

hackernews · giuliomagnifico · Jun 17, 03:55 · [Discussion](https://news.ycombinator.com/item?id=48565498)

**Background**: DeepSeek is a Chinese AI company known for developing large language models (LLMs) like the DeepSeek V4 and R1 series, which are popular among developers as affordable alternatives to models from OpenAI and Anthropic. The 'Entity List' is a US trade restriction tool that limits exports to certain foreign companies for national security reasons. Another Chinese AI firm, Z.ai, has been on this list since January 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://deepseek.ai/">DeepSeek AI: R1 Reasoning, API & Local Deployment 2026</a></li>

</ul>
</details>

**Discussion**: Commenters debate the feasibility and implications of US tech restrictions, with some questioning enforcement methods and accusing the US of mimicking China's internet censorship. Others counter that cheap Chinese AI models are a strategic tool to foster Western dependence on Chinese servers, sparking a discussion on national security versus practical utility.

**Tags**: `#AI regulation`, `#DeepSeek`, `#US-China relations`, `#trade restrictions`, `#security`

---

<a id="item-8"></a>
## [Launching browsers in under 1s using Firecracker microVMs on EC2](https://browser-use.com/posts/firecracker-browser-infra) ⭐️ 7.0/10

browser-use.com published a technical deep-dive on how they run Firecracker microVMs inside Amazon EC2 instances using nested virtualization to launch browsers in under one second. This approach addresses the growing challenge of bot detection, as their setup achieves an 81% block-evasion rate compared to only 2% for plain headless Chromium, offering a new infrastructure blueprint for AI agents and web automation tools. The system leverages the recently released AWS nested virtualization support on standard EC2 instances (since February 2026), eliminating the previous requirement for expensive bare-metal instances, though the approach still faces ethical scrutiny from the community.

hackernews · gregpr07 · Jun 16, 15:15 · [Discussion](https://news.ycombinator.com/item?id=48556561)

**Background**: Firecracker is an open-source technology from AWS that creates lightweight virtual machines (microVMs), combining strong isolation with container-like speed. Running these microVMs inside EC2 requires nested virtualization, a feature that was only available on expensive bare-metal instances until AWS added support for regular EC2 instances in early 2026. Web automation often faces anti-bot systems that detect and block headless browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker-microvm/firecracker: Secure and fast ...</a></li>

</ul>
</details>

**Discussion**: The community is divided: some view the high bot-evasion success rate as unethical, arguing it undermines the purpose of anti-bot measures, while others find it technically impressive and discuss alternatives like using Lightpanda or Kasmweb containers for better density.

**Tags**: `#Firecracker`, `#browser-automation`, `#AWS`, `#virtualization`, `#anti-bot`

---

<a id="item-9"></a>
## [AI makes code generation free and instant, turning code into a disposable commodity](https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything) ⭐️ 7.0/10

Charity Majors, CTO of Honeycomb.io, observed that in 2025, the economics of code production were turned upside down as AI made generating code effectively free and instant, transforming it from a carefully curated asset into a disposable commodity. This shift fundamentally changes how software engineers value and manage code, prioritizing rapid regeneration over long-term curation, and could lead to a "fast fashion" era of software where speed trumps maintainability. The insight comes from Majors' article "AI demands more engineering discipline. Not less," arguing that the newfound disposability of code actually requires more rigorous engineering practices to manage the resulting complexity and risk.

rss · Simon Willison · Jun 17, 17:12

**Background**: Charity Majors is a respected figure in site reliability engineering, having previously led production engineering at Facebook. Her company, Honeycomb.io, specializes in observability for complex software systems, giving her a unique vantage point on how AI-generated code impacts production environments and operational discipline.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Charity_Majors">Charity Majors</a></li>
<li><a href="https://www.linkedin.com/pulse/rise-disposable-code-how-ai-changing-way-we-prakhar-thakur-rpllc">The Rise of Disposable Code: How AI is Changing the Way We Code</a></li>
<li><a href="https://www.linkedin.com/pulse/ai-makes-writing-code-cheap-does-make-owning-software-sandip-s-palve-nhwlf">AI Makes Writing Code Cheap. It Does Not Make Owning Software...</a></li>

</ul>
</details>

**Tags**: `#ai-assisted-programming`, `#generative-ai`, `#software-engineering`, `#economics-of-code`, `#charity-majors`

---

<a id="item-10"></a>
## [Datasette 1.0a34 Adds Native Row Insert, Edit, and Delete](https://simonwillison.net/2026/Jun/16/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a34 alpha release introduces native tools to insert, edit, and delete rows directly from the web interface, available on table pages and row pages. This feature fills a long-standing gap in Datasette, transforming it from a read-only exploration tool into a full data management interface, and was inspired by the write capabilities of Datasette Agent. Edit and delete actions are also available as action items on the row page, and the feature was prompted by the developer's realization that the chat interface via Datasette Agent already allowed writes. It remains an alpha release, so it may have limitations.

rss · Simon Willison · Jun 16, 21:31

**Background**: Datasette is an open-source tool by Simon Willison that provides a web interface for exploring and publishing SQLite databases. It has traditionally been read-only, focusing on searching, filtering, and visualizing data. Datasette Agent is a newer companion that integrates large language models to enable conversational data exploration and operations, including the recent addition of write capabilities. The developer found it ironic that the AI chat interface could already write to the database while the main Datasette UI could not, motivating this update.

**Tags**: `#datasette`, `#sqlite`, `#data-management`, `#web-interface`, `#release`

---

<a id="item-11"></a>
## [Next-Latent Prediction Transformers: Learning Compact World Models for Faster Inference](https://www.reddit.com/r/MachineLearning/comments/1u84mio/nextlatent_prediction_transformers_r/) ⭐️ 7.0/10

Microsoft Research proposes NextLat, a self-supervised pre-training objective where transformers predict their own next latent states, moving beyond next-token prediction. This enables the model to learn compact belief states, improving representation learning, data efficiency, and achieving up to 3.3x faster inference via self-speculative decoding. This work addresses the myopic nature of next-token prediction, encouraging transformers to build internal world models for better reasoning and planning. It could significantly speed up LLM inference without extra models, benefiting deployment of large-scale language models. NextLat adds a latent prediction head on top of standard next-token training, requiring the model to predict its next latent state given the current latent and next token. The method provides denser supervision in latent space and enables recursive multi-step lookahead for self-speculative decoding.

reddit · r/MachineLearning · /u/jayden_teoh_ · Jun 17, 08:44

**Background**: Traditional transformer language models are trained with next-token prediction, which only optimizes for immediate token accuracy, often failing to capture long-horizon dependencies. Self-speculative decoding is a technique that uses the model's own early layers to generate draft tokens, which are then verified by deeper layers, enabling faster inference without a separate draft model. NextLat extends this by training the model to predict its own latent states, creating a compact representation that enables both faster decoding and better generalization.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.05963">Next-Latent Prediction Transformers Learn Compact World Models</a></li>
<li><a href="https://huggingface.co/blog/layerskip">Faster Text Generation with Self-Speculative Decoding</a></li>
<li><a href="https://github.com/JaydenTeoh/NextLat">GitHub - JaydenTeoh/NextLat: Codebase for "Next-Latent Prediction ...</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#transformers`, `#self-supervised-learning`, `#representation-learning`, `#inference-optimization`

---

<a id="item-12"></a>
## [Using Contrastive Targeted SFT to Build Causal Dependency Graphs for Mechanistic Interpretability](https://www.reddit.com/r/MachineLearning/comments/1u8if6l/contrastive_targeted_sft_as_a_mechinterp_method/) ⭐️ 7.0/10

A Reddit user is experimenting with contrastive targeted supervised fine-tuning on a 31B model to isolate a capability dimension's circuit, then ablating it to measure how other dimensions degrade, aiming to build a causal dependency graph that could guide iterative training rounds. This approach could significantly advance mechanistic interpretability by enabling systematic mapping of causal relationships between capabilities in LLMs, potentially leading to more efficient and targeted fine-tuning strategies for better model control. The experiment involved 40 domains and 6 quality dimensions; one dimension consistently underperformed. The user plans to distinguish direct from indirect causal effects by ablating at multiple layers and using activation steering as a diagnostic for composition failures.

reddit · r/MachineLearning · /u/Substantial_Diver469 · Jun 17, 18:31

**Background**: Mechanistic interpretability is a subfield of explainable AI that seeks to understand the internal computations of neural networks, akin to reverse-engineering. Ablation is a technique where parts of a model are removed or modified to test hypotheses about their function. Contrastive learning and supervised fine-tuning are both methods for tuning models; contrastive approaches use pairs of positive and negative examples to highlight differences.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://arxiv.org/abs/2510.14824">Supervised Fine-Tuning or Contrastive Learning? Towards Better ...</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#fine-tuning`, `#causal inference`, `#language models`, `#ablation`

---

<a id="item-13"></a>
## [Researcher Asks How to Evaluate Relative Probe Strength in Transformer Models](https://www.reddit.com/r/MachineLearning/comments/1u8lo60/how_do_you_analyze_the_relative_strength_of/) ⭐️ 6.0/10

A researcher posted a question on the Machine Learning subreddit requesting theoretical frameworks and practical methods for analyzing the relative strength of probes in transformer models, particularly in the context of factuality guarantees and circuit analysis. Probing is a cornerstone of mechanistic interpretability, and a principled way to measure probe reliability is essential for trusting model explanations and building factuality guarantees into language models. The post highlights the tension between probe capacity and the underlying network’s capacity, raises concerns about overfitting and the need for sampling-theoretic guarantees akin to Nyquist limits, and questions whether examples should be labeled by difficulty. The researcher cites a concrete failure case where a Google Gemini model incorrectly answered a letter-counting task despite spelling out the word, undermining a simple position-probing claim.

reddit · r/MachineLearning · /u/RepresentativeBee600 · Jun 17, 20:29

**Background**: In mechanistic interpretability, linear probes are lightweight classifiers trained on a model’s internal activations to detect what information is encoded. Circuit analysis seeks to decompose neural networks into interpretable computational subgraphs. Recent work on conformal prediction, such as 'Language Models with Conformal Factuality Guarantees', provides statistical guarantees for LM outputs, addressing the type of factuality concerns raised in the post.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.arena.education/chapter1_transformer_interp/11_probing/intro/?curius=1051">Chapter 1: Transformer Interpretability - ARENA</a></li>
<li><a href="https://arxiv.org/abs/2402.10978">[2402.10978] Language Models with Conformal Factuality Guarantees</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#interpretability`, `#probing`, `#transformers`, `#circuit analysis`

---

<a id="item-14"></a>
## [I deployed a GAN on a Raspberry Pi 4 and built a physical NFT minting device](https://www.reddit.com/r/MachineLearning/comments/1u8cqan/i_deployed_a_gan_on_a_raspberry_pi_4_and_built_a/) ⭐️ 6.0/10

A user trained a 128×128 DCGAN on a MacBook and exported the model to ONNX. They then deployed it on a Raspberry Pi 4 connected to an ESP32 display, creating a physical device that generates and displays hybrid face images at the press of a button. This project demonstrates that generative AI models can be deployed on low-cost edge devices like the Raspberry Pi for interactive art, highlighting the accessibility of AI tools for creative expression and the potential for ONNX to bridge training and inference on constrained hardware. It may inspire similar edge AI art installations and showcases the playful intersection of AI, NFTs, and physical computing. The DCGAN generator is a 6-block architecture, trained for 800 epochs on 2480 images (11 subjects, one dominant anchor class of 2000 images) on an Apple Silicon MacBook, exported as a 53 MB float32 ONNX model. Inference on the Raspberry Pi 4 takes 3 seconds per image, and the output is sent to an ESP32 display with a randomly generated title.

reddit · r/MachineLearning · /u/Numerous-Dentist-882 · Jun 17, 15:05

**Background**: DCGAN (Deep Convolutional Generative Adversarial Network) is a type of GAN that uses deep convolutional layers to generate realistic images. ONNX (Open Neural Network Exchange) is an open format for representing machine learning models, enabling deployment across different frameworks. The ESP32 is a low-cost, low-power microcontroller with Wi-Fi and Bluetooth, popular in embedded electronics. The Raspberry Pi is a small single-board computer widely used for edge computing and DIY projects.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/why-gans-unstable-deep-dive-dcgan-its-limits-mostak-mahmud-chowdhury-mdsuc">Why GANs Are Unstable: A Deep Dive into DCGAN and Its Limits</a></li>
<li><a href="https://medium.com/@shivprataprai11/understanding-onnx-an-open-standard-for-deep-learning-models-350a72714660">Understanding ONNX : An Open Standard for Deep Learning Model ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/ESP32">ESP32</a></li>

</ul>
</details>

**Tags**: `#GAN`, `#Edge Computing`, `#Raspberry Pi`, `#Art`, `#ONNX`

---