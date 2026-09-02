---
layout: default
title: "Horizon Summary: 2026-09-02 (EN)"
date: 2026-09-02
lang: en
---

> From 38 items, 19 important content pieces were selected

---

1. [Claude Fable 5.1 and Mythos 5.1 released with natural writing, lower cache pricing, and enhanced reasoning](#item-1) ⭐️ 9.0/10
2. [OpenAI Unveils Astra: Frontier Model Achieves Perfect Exploit Score, Sparking Safety Debate](#item-2) ⭐️ 9.0/10
3. [FBI Probes Service Selling 153M+ Drivers Licenses](#item-3) ⭐️ 8.0/10
4. [A Latent Reasoning Taxonomy: Mapping BDH-CQ, HRM/TRM, and Coconut](#item-4) ⭐️ 8.0/10
5. [TontaubeV1: A 2.9B-Parameter Character-Level TTS Model for Long-Form Speech](#item-5) ⭐️ 8.0/10
6. [Sliding-Window Attention with Sinks Beats Linear Attention on Long-Context Reasoning](#item-6) ⭐️ 8.0/10
7. [Ed Zitron&\#x27;s AI Skeptic Predictions: A Critical Analysis and Debate](#item-7) ⭐️ 7.0/10
8. [A Walkthrough for Setting Up Local LLMs on an M4 Pro Mac Mini](#item-8) ⭐️ 7.0/10
9. [Nori Robotics Launches $1,688 Bimanual Mobile Robot for Developers](#item-9) ⭐️ 7.0/10
10. [Creator of Jujutsu \(jj\) Joins ERSC](#item-10) ⭐️ 7.0/10
11. [Movie Scene Map Compiles 13,312 Filming Locations Across Media](#item-11) ⭐️ 7.0/10
12. [Wrapture: A new Python library for unified mocking, tracing, and monkeypatching](#item-12) ⭐️ 7.0/10
13. [EvoUndo: Safe Self-Evolution for LLM Agents via Recoverability Constraints](#item-13) ⭐️ 7.0/10
14. [Professor shares best practices for cold emailing PhD positions](#item-14) ⭐️ 7.0/10
15. [Firefox on iOS Gets Built-in Ad Blocker, but Not for Search or YouTube Ads](#item-15) ⭐️ 6.0/10
16. [OpenAI&\#x27;s Codex App Bundles Full LibreOffice, Python, and Node.js in Cache](#item-16) ⭐️ 6.0/10
17. [Ambient CSS v3 Brings Blender-Inspired 3D Lighting to CSS, Draws Criticism](#item-17) ⭐️ 6.0/10
18. [Simon Willison Builds GeoJSON Map Viewer with AI Assistance](#item-18) ⭐️ 6.0/10
19. [YOLO26-RGB: Depth-Trained Backbone Transfers to Image Deraining](#item-19) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Claude Fable 5.1 and Mythos 5.1 released with natural writing, lower cache pricing, and enhanced reasoning](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic has launched Claude Fable 5.1 and Mythos 5.1, featuring a more natural writing style, a significant reduction in cache read pricing from $1/M to $0.25/M, and adjustable reasoning effort levels that allow users to control the depth of the model&\#x27;s thinking. The release also includes a system card detailing safety and capabilities. The more natural writing style improves the usability of AI-generated text, while the cache pricing cut sets a potential ceiling for LLM API costs, benefitting developers and enterprises. The reasoning effort control makes the model more versatile for complex tasks, potentially raising the bar for competitive models. The cache read price drop makes Fable 5.1 half the cost of Opus, and the reasoning effort can be set from low to &\#x27;max&\#x27; \(max took 14 minutes in a demo\). However, community tests note that performance improvements outside a specific science benchmark are modest, and native thought traces are not visible, though summarized traces can be extracted with external tools.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**Background**: Claude Fable is Anthropic&\#x27;s high-end model for long-horizon reasoning and coding, introduced with Fable 5. Prompt caching allows repeated input prefixes to be stored and re-read at a fraction of the cost; the cache read price is the cost per token when the cache is hit. The system card is a transparency document covering safety evaluations and deployment decisions. Adjustable reasoning effort lets users trade off between speed and depth of analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/models/fable-5-1/overview">Claude Fable 5.1 - Claude Platform Docs</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/pricing">Pricing - Claude Platform Docs</a></li>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>

</ul>
</details>

**Discussion**: The community reaction is mixed: an Anthropic employee praises the writing style improvement, and demonstrations show impressive reasoning quality \(e.g., detailed pelican drawings\). However, some users criticize the model as &\#x27;nerfed&\#x27; and accuse the company of using Mythos marketing to compensate for modest gains, while the removal of visible thought traces is seen as a step backward. Others view the pricing change as evidence of weak initial demand, which may cap future LLM pricing.

**Tags**: `#AI`, `#Claude`, `#model release`, `#Anthropic`, `#LLM`

---

<a id="item-2"></a>
## [OpenAI Unveils Astra: Frontier Model Achieves Perfect Exploit Score, Sparking Safety Debate](https://openai.com/index/path-to-astra/) ⭐️ 9.0/10

OpenAI announced Astra, a frontier model that scored 100% on ExploitBench, a benchmark for developing exploits from known vulnerabilities, and outlined new safeguards and access policies. Astra&\#x27;s perfect exploit capability represents a major leap in automated cybersecurity, intensifying debate on how to govern frontier AI models that could be weaponized by malicious actors or restricted by governments. The model scored 100% on ExploitBench, which evaluates end-to-end vulnerability exploitation. OpenAI says it will use &\#x27;clear, objective criteria&\#x27; for access, but community members note that access is already restricted in certain countries, raising equity concerns.

hackernews · jithinraj · Sep 1, 20:20 · [Discussion](https://news.ycombinator.com/item?id=49527595)

**Background**: A frontier model is a cutting-edge, general-purpose AI system like GPT-4. ExploitBench is a cybersecurity benchmark that measures a model&\#x27;s ability to discover and exploit software vulnerabilities. Alignment refers to ensuring AI systems act in accordance with human values, a critical concern for models with dangerous capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>
<li><a href="https://llm-stats.com/benchmarks/exploitbench">ExploitBench Leaderboard | LLM Stats</a></li>
<li><a href="https://www.lesswrong.com/posts/aRiG8AqSM2tbNzbeg/alignment-is-not-one-problem-a-3d-map-of-ai-risk">Alignment Is Not One Problem: A 3D Map of AI Risk — LessWrong</a></li>

</ul>
</details>

**Discussion**: Comments reflect skepticism, concern, and intrigue. Users highlighted existing country-based access restrictions, questioned the novelty of the capabilities, feared alignment breakdowns \(citing a recent HuggingFace hack\), and debated whether the government could compel OpenAI to release unguarded model weights for national security. The overall sentiment is cautious, with calls to prioritize alignment over capability release.

**Tags**: `#openai`, `#ai-safety`, `#frontier-models`, `#cybersecurity`, `#alignment`

---

<a id="item-3"></a>
## [FBI Probes Service Selling 153M+ Drivers Licenses](https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/) ⭐️ 8.0/10

The FBI is investigating a service that was selling access to a database containing over 153 million driver&\#x27;s license records, revealing a massive breach of identity verification data. This breach highlights systemic flaws in identity verification and data retention, where companies hoard sensitive personal data indefinitely without adequate security or regulatory penalties, exposing millions to identity theft and fraud. The compromised data includes full front-and-back scans of driver&\#x27;s licenses, with many records linked to marijuana dispensary purchases, indicating that verification services retained the information long after it was needed.

hackernews · tatersolid · Sep 1, 23:17 · [Discussion](https://news.ycombinator.com/item?id=49529621)

**Background**: Identity verification services often require users to upload scans of government-issued IDs and a selfie for age or identity checks. Once verified, these companies may store the data indefinitely, creating large repositories of sensitive personal information that are attractive targets for hackers.

**Discussion**: Commenters criticized the unnecessary retention of data, arguing that strict liability and fixed compensation for breaches would force companies to minimize data collection. Some suspected the data could be misused for voter suppression or other malicious purposes.

**Tags**: `#cybersecurity`, `#data-breach`, `#privacy`, `#identity-verification`, `#regulatory-failure`

---

<a id="item-4"></a>
## [A Latent Reasoning Taxonomy: Mapping BDH-CQ, HRM/TRM, and Coconut](https://www.reddit.com/r/MachineLearning/comments/1w4evwo/latent_reasoning_landscape_in_2026_mapping_bdhcq/) ⭐️ 8.0/10

A Reddit analysis proposes a taxonomy of latent reasoning methods, grouping them into five distinct families that operate on continuous hidden states rather than token-level chains of thought, marking a shift away from superficial reasoning imitations. This taxonomy highlights a fundamental shift from chain-of-thought to latent reasoning, which could address the core limitation of superficial reasoning imitations and potentially offer a more efficient path toward AGI, while also raising critical questions about the future of interpretability and evaluation. The five families include: continuous thoughts \(Coconut, Soft Thinking\), compressed discrete tokens \(Abstract-CoT\), recurrent depth/looped models, task-trained recursive solvers \(HRM, TRM\), and in-context recurrent latent solvers \(BDH-CQ\). BDH-CQ achieves a new cost-accuracy Pareto frontier on ARC-AGI-1, while HRM/TRM use transductive optimization for unseen tasks.

reddit · r/MachineLearning · /u/Typical-Scene-5794 · Sep 1, 15:14

**Background**: Chain-of-thought \(CoT\) prompting makes large language models generate explicit reasoning steps, but studies have shown that these steps can be unreliable, often not reflecting the actual computation. Latent reasoning methods bypass token generation, instead using continuous hidden states to perform computation, which may enable more efficient and genuine reasoning. The ARC-AGI benchmark is a challenging test of abstraction and reasoning, often used to evaluate general intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.06769">[2412.06769] Training Large Language Models to Reason in a ... GitHub - facebookresearch/coconut: Training Large Language ... Training Large Language Models to Reason in a Continuous ... Coconut: A Framework for Latent Reasoning in LLMs Coconut LLM Coconut: Training Large Language Models to Reason in a ... Santosh Sawant - Training Large Language Models to Reason in ...</a></li>
<li><a href="https://arxiv.org/abs/2608.09888">[2608.09888] BDH-CQ: In-Context Learning with Recurrent Latent Reasoning</a></li>
<li><a href="https://medium.com/@m.mastrodonato/thinking-small-reasoning-deep-how-hrm-and-trm-redefine-the-architecture-of-intelligence-68d748a9ffe5">Thinking Small, Reasoning Deep: How HRM and TRM Redefine the Architecture of Intelligence | by Marco Mastrodonato | Medium</a></li>

</ul>
</details>

**Tags**: `#latent reasoning`, `#chain-of-thought`, `#machine learning`, `#AGI`, `#deep learning`

---

<a id="item-5"></a>
## [TontaubeV1: A 2.9B-Parameter Character-Level TTS Model for Long-Form Speech](https://www.reddit.com/r/MachineLearning/comments/1w4afjn/we_released_tontaubev1_a_characterlevel_tts_model/) ⭐️ 8.0/10

We released TontaubeV1, a 2.9B-parameter open-weight TTS model that uses character-level tokenization and the DualCodec multi-codebook discrete audio codec to enable expressive long-form narration and zero-shot voice cloning from up to one minute of reference audio. The open-weight release and novel character-level tokenization improve robustness for long-form synthesis and simplify the text-to-speech mapping, making high-quality, low-latency local inference accessible to the research community and pushing the state of the art in speech generation. The model is built on a Qwen3-1.7B checkpoint, trained on ~200k hours of audio across 7 languages \(primarily tested in English and German\), and uses a chunking scheme with separate logical position IDs for text and audio streams to maintain temporal alignment across long passages.

reddit · r/MachineLearning · /u/EAVDR · Sep 1, 12:23

**Background**: DualCodec is a low-frame-rate, semantically-enhanced neural audio codec that uses dual encoding streams \(SSL and waveform\) to produce discrete tokens for speech generation. Character-level tokenization treats each character as a separate token, which helps the model avoid out-of-distribution issues common with subword tokenizers when handling rare or complex character sequences, especially in long-form TTS tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.13000">[2505.13000] DualCodec: A Low-Frame-Rate, Semantically-Enhanced Neural Audio Codec for Speech Generation</a></li>
<li><a href="https://dualcodec.github.io/">DualCodec Demo Page</a></li>

</ul>
</details>

**Tags**: `#text-to-speech`, `#open-source`, `#deep-learning`, `#audio-generation`, `#zero-shot-voice-cloning`

---

<a id="item-6"></a>
## [Sliding-Window Attention with Sinks Beats Linear Attention on Long-Context Reasoning](https://www.reddit.com/r/MachineLearning/comments/1w3j1vw/slidingwindow_attention_beats_linear_on/) ⭐️ 8.0/10

A new preprint by Alexia Jolicoeur-Martineau et al. demonstrates that Sliding Window Attention \(SWA\) with sinks massively outperforms post-trained linear attention models on long-context reasoning tasks, such as Needle-in-a-Haystack and BABILong, achieving 2 to 10 times higher performance. The authors argue that simpler baselines have been overlooked and recommend switching to SWA instead of post-training linear models. This finding challenges the prevailing trend of using linear attention for long-context LLMs, potentially saving substantial post-training compute resources and redirecting research efforts toward simpler, more efficient baselines. It could significantly influence how labs design and train models for long-context tasks. The paper reports that SWA with sinks achieves 2 to 10 times higher performance on the Needle-in-a-Haystack and BABILong benchmarks. The authors note that linear attention models likely require training from scratch or extensive post-training to even match SWA, while SWA itself needs no post-training, runs fast, and maintains low memory usage.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Aug 31, 16:35

**Background**: Sliding Window Attention \(SWA\) is a technique that limits the attention computation to a fixed-size local window around each token, reducing the quadratic cost of standard self-attention to linear complexity with respect to sequence length. Linear attention models aim to achieve similar efficiency by approximating the softmax attention with linear operations, but they often require post-training or training from scratch to maintain performance. The attention sink phenomenon refers to the observation that some tokens \(e.g., punctuation\) attract disproportionately high attention weights, and incorporating sinks into SWA can stabilize and improve long-context modeling. The Needle-in-a-Haystack and BABILong benchmarks are common tests for evaluating a model&\#x27;s ability to retrieve and reason over information in long contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28444">[2608.28444] Sliding-window beats linear attention - arXiv.org</a></li>
<li><a href="https://www.ultralytics.com/glossary/linear-attention">What is Linear Attention ? O(N) Efficiency | Ultralytics</a></li>
<li><a href="https://github.com/gkamradt/needle-in-a-haystack">GitHub - gkamradt/needle-in-a-haystack: Doing simple ...</a></li>

</ul>
</details>

**Tags**: `#sliding-window attention`, `#linear attention`, `#long-context reasoning`, `#LLM efficiency`, `#attention mechanisms`

---

<a id="item-7"></a>
## [Ed Zitron&\#x27;s AI Skeptic Predictions: A Critical Analysis and Debate](https://danluu.com/zitron/) ⭐️ 7.0/10

Dan Luu&\#x27;s blog post critically examines the accuracy of AI skeptic Ed Zitron&\#x27;s predictions from 2024 and 2025, sparking a high-quality discussion on interpretation and media punditry. This analysis is significant because it scrutinizes the sensationalist nature of tech punditry, the ambiguity of terms like &\#x27;dying&\#x27; in the AI context, and provides a model for how the tech community can more rigorously evaluate AI trend predictions. The critique points out that Zitron&\#x27;s numerical evidence, such as a Facebook MAU decline, does not coherently support his arguments about Meta&\#x27;s AI missteps, and the community debate reveals that differing interpretations of &\#x27;dying&\#x27;—company failure versus product rot—significantly affect the accuracy assessment.

hackernews · jatins · Sep 1, 18:35 · [Discussion](https://news.ycombinator.com/item?id=49526069)

**Background**: Ed Zitron is a prominent tech commentator and AI skeptic known for his &\#x27;rot economy&\#x27; thesis, where companies remain profitable while their core products degrade. He frequently predicts the downfall of AI firms using user metrics. Dan Luu, a software engineer, is recognized for data-driven debunkings of tech claims. Their clash highlights the tension between narrative-driven punditry and empirical scrutiny.

**Discussion**: The community discussion reveals a nuanced debate: supporters argue the critique misinterprets &\#x27;dying&\#x27; as corporate death rather than product rot, while others note that pundits inevitably rely on vague numbers to maintain relevance. Some commenters highlight that Zitron&\#x27;s data does not support his arguments, and the overall sentiment underscores the inherent tension between engagement-driven punditry and rigorous accuracy.

**Tags**: `#AI`, `#skepticism`, `#predictions`, `#media-critique`, `#commentary`

---

<a id="item-8"></a>
## [A Walkthrough for Setting Up Local LLMs on an M4 Pro Mac Mini](https://lws.io/blog/my-local-model-setup/) ⭐️ 7.0/10

A blog post by lws.io provides a detailed, hands-on walkthrough of installing and running local large language models on an Apple M4 Pro Mac Mini, using tools like Ollama and sharing the author&\#x27;s personal configuration and experience. This guide offers a practical resource for practitioners who want to leverage the powerful yet affordable M4 Pro Mac Mini for private, offline AI inference, addressing the growing demand for data sovereignty and low-latency local AI. The setup uses Ollama for model management, and community comments highlight that while small models like Qwen 3.5 4B/9B are usable, performance issues such as prefill latency on high-RAM M4 Max systems persist, and building effective harnesses around small models is crucial.

hackernews · raybb · Sep 1, 22:30 · [Discussion](https://news.ycombinator.com/item?id=49529132)

**Background**: Ollama is an open-source tool for running LLMs locally, providing a command-line interface and REST API. The M4 Pro Mac Mini is a compact desktop computer with Apple&\#x27;s latest M4 Pro chip, featuring a 12-core CPU, 16-core GPU, and up to 24GB unified memory, introduced in October 2024. Running LLMs locally avoids sending data to cloud servers, enhancing privacy and reducing reliance on internet connectivity. The concept of privacy-preserving inference is also being explored to allow using cloud GPUs without exposing sensitive data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama</a></li>
<li><a href="https://en.wikipedia.org/wiki/M4_Pro_Mac_mini">M4 Pro Mac mini</a></li>
<li><a href="https://eprint.iacr.org/2026/105">Privacy-Preserving LLM Inference in Practice: A Comparative Survey of Techniques, Trade-Offs, and Deployability</a></li>

</ul>
</details>

**Discussion**: Overall, the community showed great interest but mixed opinions on performance. Some users questioned the lack of performance metrics, noting that loading models on low-RAM systems can be slow. Others discussed the potential of a privacy-protecting GPU cloud service as an alternative, and the need to build custom harnesses around small models for practical use. One user praised the guide but noted that prefill latency on an M4 Max with 128GB RAM was problematic, leading them to switch to DGX Sparks.

**Tags**: `#local-llm`, `#apple-silicon`, `#ollama`, `#setup-guide`, `#hardware`

---

<a id="item-9"></a>
## [Nori Robotics Launches $1,688 Bimanual Mobile Robot for Developers](https://www.norirobotics.com/) ⭐️ 7.0/10

Nori Robotics, a YC S26 startup, has launched a $1,688 bimanual mobile robot with 19 degrees of freedom, designed to lower hardware costs for robotics developers and researchers by using high-ratio servos instead of more expensive QDD motors. The robot comes with an open SDK and a browser-based simulator, and the first units have already shipped. By offering a full-featured robot at a fraction of the cost of typical research platforms, Nori could enable more labs and independent developers to experiment with physical AI, potentially accelerating the development of robotic manipulation and imitation learning. However, community skepticism about servo precision suggests that the robot&\#x27;s real-world utility for fine-grained tasks may be limited. The robot features 19 degrees of freedom, two 7+1 DOF arms with 1.5 kg payload each, a telescoping lift, a differential wheeled base, and a Raspberry Pi 5 for onboard SLAM and safety; computationally intensive models like ACT and VLAs must be run on an external computer or server. The use of high-ratio servos keeps costs low but results in jerky motion, limited precision, and no force feedback, as noted by the community.

hackernews · AntonioLi · Sep 1, 17:35 · [Discussion](https://news.ycombinator.com/item?id=49525153)

**Background**: ACT \(Action Chunking with Transformers\) is a robot learning policy that predicts a sequence of future joint actions from camera images and the current state, enabling smooth, reactive behavior. VLA \(Vision-Language-Action\) models extend this concept by incorporating language instructions, allowing robots to reason about tasks described in natural language. QDD \(Quasi-Direct Drive\) motors provide better torque control and backdrivability, used in more expensive research robots, but Nori chose high-ratio servos to hit the $1,688 price point.

<details><summary>References</summary>
<ul>
<li><a href="https://www.roboticscenter.ai/blog/act-policy-explained">ACT Policy Explained: Action Chunking with Transformers for Robot Learning | Robotics Center Blog</a></li>
<li><a href="https://medium.com/online-inference/vlm-models-explained-the-future-of-robotics-ai-fdff3346c679">VLM models explained: The future of robotics AI | by Dave... | Medium</a></li>

</ul>
</details>

**Discussion**: The community voiced significant concern about the use of RC-style servos, which cause jerky motion and lack force feedback, limiting precision. Several questioned whether the demonstrated tasks \(e.g., tidying up\) are staged and what the real-world success rate is. Others expressed interest in seeing the robot in person and inquired about its hackability, while some made lighthearted observations about the name collision with other &\#x27;nori&\#x27; brands.

**Tags**: `#robotics`, `#humanoid-robot`, `#hardware`, `#developer-tools`, `#hackernews-launch`

---

<a id="item-10"></a>
## [Creator of Jujutsu \(jj\) Joins ERSC](https://ersc.io/blog/martin-joins-ersc) ⭐️ 7.0/10

Martin, the creator of the Jujutsu \(jj\) version control system, has joined ERSC, a new code hosting platform that uses Jujutsu as its native model and aims to compete with GitHub. This hire deepens the integration between jj and ERSC, potentially accelerating the development of a modern, undo-friendly alternative to GitHub, and validates the growing interest in Jujutsu as a more user-friendly git-compatible tool. Jujutsu&\#x27;s standout feature is safe undo for all operations, including rebases and commit abandonment; ERSC builds on Jujutsu with first-class conflict handling, fine-grained ACLs, and backwards compatibility with Git.

hackernews · steveklabnik · Sep 1, 17:46 · [Discussion](https://news.ycombinator.com/item?id=49525297)

**Background**: Jujutsu \(jj\) is a version control system compatible with Git repositories but designed with a simpler, more expressive CLI and built-in safety like universal undo. ERSC \(East River Source Control\) is a new code hosting platform that uses Jujutsu as its native version control model, positioning itself as a competitor to GitHub. The creator of jj, Martin, is now joining the ERSC team, likely to work on platform development.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/jj-vcs/jj">jj-vcs/jj - Jujutsu—a version control system</a></li>
<li><a href="https://ersc.io/blog/ersc-availability">An update on ERSC availability</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some users praise jj&\#x27;s undo capabilities and better UX, while others question the need for a new tool when Git suffices for their workflow. Skepticism about ERSC&\#x27;s value proposition compared to GitHub also surfaces, with some feeling it doesn&\#x27;t address GitHub&\#x27;s core issues.

**Tags**: `#jujutsu`, `#version-control`, `#git`, `#devtools`, `#ersc`

---

<a id="item-11"></a>
## [Movie Scene Map Compiles 13,312 Filming Locations Across Media](https://moviescenemap.com/) ⭐️ 7.0/10

The site moviescenemap.com launched an interactive map that pinpoints real-world filming locations for over 13,000 movies, TV series, video games, anime, and manga. Users can explore scenes from productions like “Jericho” or “Star Wars” and suggest missing locations via a dedicated submission page. This map provides a fun, practical resource for film tourists and travelers, turning everyday trips into cinematic discoveries. It also demonstrates how a non-corporate internet project can aggregate scattered location data into a single, polished interface, highlighting the value of community-driven curation. The map UI is smooth and accurate for single scenes, but some users noted overlapping pins at certain zoom levels and missing well-known films. The site includes a “missing” page \(moviescenemap.com/missing/\) for user submissions, and the creator may consider partnering with larger databases or adding crowd-sourced verification.

hackernews · Flightmussy · Sep 1, 16:34 · [Discussion](https://news.ycombinator.com/item?id=49524320)

**Background**: Filming location maps have long been popular among fans and travelers, but they are often fragmented across forums or Wikipedia. This site consolidates over 13,000 entries from diverse media, including anime and video games, which are less commonly mapped. The project appears to be a one-person or small-team effort, relying on curated data and user contributions to fill gaps.

**Discussion**: Comments are overwhelmingly positive, praising the idea and smooth UX. Constructive feedback includes requests for easier access to media pages, fixing z-order pin overlap, and adding more content via partnerships or crowd-sourcing. Users noted missing famous films in their areas and offered to help, showing strong engagement and a desire to improve the resource.

**Tags**: `#data-visualization`, `#maps`, `#movies`, `#entertainment`, `#geospatial`

---

<a id="item-12"></a>
## [Wrapture: A new Python library for unified mocking, tracing, and monkeypatching](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

Graham Dumpleton has introduced Wrapture, a Python library that combines monkeypatching, mocking, and tracing into a single tool for testing and observability. It allows wrapping any function or method to trace all access or override return values, and includes OpenTelemetry support for instrumentation. This library simplifies the developer workflow by merging testing mocks with production tracing, making it easier to instrument and debug applications. Created by a respected Python developer, it offers a credible alternative to unittest.mock and integrates with the OpenTelemetry standard, potentially streamlining observability practices. Wrapture supports both a context-manager-based API for stubbing in tests and a declarative TOML-based configuration for adding tracing to existing projects. The entire codebase was generated by AI under Graham Dumpleton&\#x27;s careful direction, and the project is still in its early weeks.

rss · Simon Willison · Aug 31, 23:59

**Background**: Monkeypatching is the dynamic modification of code at runtime, often used to alter behavior without changing source code. Mocking is a testing technique that replaces real objects with simulated ones to isolate code under test. Tracing is the recording of program execution for debugging and performance monitoring. OpenTelemetry is an open standard for collecting telemetry data from applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Monkeypatching">Monkeypatching</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tracing_%28software%29">Tracing (software)</a></li>

</ul>
</details>

**Tags**: `#python`, `#testing`, `#tracing`, `#monkeypatching`, `#observability`

---

<a id="item-13"></a>
## [EvoUndo: Safe Self-Evolution for LLM Agents via Recoverability Constraints](https://www.reddit.com/r/MachineLearning/comments/1w4m0hq/evoundo_recoverabilityconstrained_selfevolution/) ⭐️ 7.0/10

Researchers introduced EvoUndo, a framework that constrains LLM agents&\#x27; self-modifications to ensure recoverability across counterfactual harness states. On 600 one-shot self-evolution tasks, 197 capability-improving mutations failed recoverability, but an extended recovery calculus boosted oracle recovery from 48/197 to 191/197. As LLM agents increasingly self-modify at runtime, ensuring safe rollback across diverse states is crucial for deployment in real-world autonomous systems. EvoUndo demonstrates that simple recovery strategies fail, and that reliable self-evolution requires co-designed verification, state grounding, and expressive recovery languages. Under the original recovery language, conventional repair strategies recovered 0 out of 197 failures; a deterministic oracle recovered 48/197, while the extended recovery calculus achieved 191/197. A 2×2 intervention revealed that exact state-address grounding and language expressivity are key, and a negative interaction observed on GPT-oss-120B was absent in Qwen3.8-27B, indicating model-dependence.

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · Sep 1, 19:17

**Background**: LLM agents are autonomous systems that can modify their own prompts, tools, or execution harnesses at runtime—a process known as self-evolution. While this can improve performance, a mutation that works in one state may become irreversible in a different \(counterfactual\) state, posing safety risks. Recoverability is the ability to safely undo these modifications, and the paper&\#x27;s recovery calculus provides a formal language to express and verify undo operations. EvoUndo extends this calculus to handle a wider range of failures.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.28363">EvoUndo: Recoverability-ConstrainedSelf-Evolution for LLM Agent Harnesses</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#self-evolution`, `#recoverability`, `#safety`, `#autonomous systems`

---

<a id="item-14"></a>
## [Professor shares best practices for cold emailing PhD positions](https://www.reddit.com/r/MachineLearning/comments/1w3bwci/cold_emailing_profs_about_phd_positions_read_this/) ⭐️ 7.0/10

A professor on Reddit posted detailed advice for cold emailing about PhD positions, emphasizing that emails should be brief, targeted to the supervisor&\#x27;s research, and free of common mistakes like mass emails, misrepresenting publications, and excessive AI use. This guidance is important because cold emailing is a standard part of PhD recruitment in many countries, and following these tips can significantly improve a candidate&\#x27;s chances of receiving a positive response, particularly in the competitive field of machine learning. The professor cautioned against dishonestly presenting workshop papers as conference papers, using LLMs to generate research ideas or summarize his work, and ignoring the specific contact instructions on his website, which can lead to emails being marked as spam.

reddit · r/MachineLearning · /u/tariban · Aug 31, 12:09

**Tags**: `#PhD applications`, `#academia`, `#career advice`, `#machine learning`, `#cold emailing`

---

<a id="item-15"></a>
## [Firefox on iOS Gets Built-in Ad Blocker, but Not for Search or YouTube Ads](https://blog.mozilla.org/en/firefox/ad-blocker-on-ios/) ⭐️ 6.0/10

Mozilla has introduced a built-in ad blocker in Firefox for iOS, rolling out gradually as an experimental feature, but it does not block ads on search engine results pages or YouTube. This brings Firefox on iOS closer to rival browsers in ad blocking, yet the exclusions—likely tied to Mozilla&\#x27;s reliance on Google revenue—may limit its appeal and reinforce concerns about the company&\#x27;s financial independence. The feature is part of a gradual rollout, requires users to opt into telemetry data collection, and explicitly excludes search engine ads and YouTube video ads. Some users have waited weeks without seeing the option appear.

hackernews · HieronymusBosch · Sep 1, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49521973)

**Background**: Ad blocking on iOS has historically been limited because Apple mandates all browsers use WebKit, restricting the type of content-blocking extensions possible. Firefox previously lacked a built-in ad blocker on iOS, while competitors like Brave and Orion offered one. Mozilla&\#x27;s search partnership with Google, which supplies the majority of its revenue, likely influences the decision to exclude search and YouTube ads.

**Discussion**: Users are frustrated by the slow rollout, the requirement to enable telemetry, and the lack of search/YouTube ad blocking. Many suspect the exclusions stem from Mozilla&\#x27;s dependence on Google revenue, while some argue that this dependency makes it even more important to support Mozilla&\#x27;s other monetization efforts. Overall, the feature is welcomed but seen as incomplete.

**Tags**: `#Firefox`, `#iOS`, `#ad-blocking`, `#privacy`, `#Mozilla`

---

<a id="item-16"></a>
## [OpenAI&\#x27;s Codex App Bundles Full LibreOffice, Python, and Node.js in Cache](https://simonwillison.net/2026/Sep/1/codex-libreoffice/) ⭐️ 6.0/10

Simon Willison discovered that the ChatGPT desktop app \(formerly Codex\) stores a 1.7GB &\#x27;codex-primary-runtime&\#x27; in its cache, containing a full Python installation, Node.js, and native binaries for LibreOffice, Poppler, and git, used for document processing. This reveals the app&\#x27;s heavy reliance on bundled third-party tools for file handling, raising questions about app design, bloat, and the future of desktop AI assistants that embed entire office suites. The runtime is located in ~/.cache/codex-runtimes/codex-primary-runtime/, with a &\#x27;plugins/documents&\#x27; folder containing skills that tell Codex how to use the bundled binaries; the libreoffice-headless binary alone takes 429.7 MB.

rss · Simon Willison · Sep 1, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49527396)

**Background**: Codex is the original name for OpenAI&\#x27;s ChatGPT desktop app, which can access local files. LibreOffice is a free and open-source office suite that can read and write Microsoft Office formats. Poppler is a PDF rendering library often used for document processing. OmniDiskSweeper is a macOS tool that Simon used to scan the cache folder.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Poppler_%28software%29">Poppler (software) - Wikipedia</a></li>
<li><a href="https://motionobj.com/articles/reducing-disk-usage-on-your-mac-with-omnidisksweeper/">How to Use OmniDiskSweeper to Find Large Files - MotionObj</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise at the bundled dependencies, with some noting they bundle LibreOffice for similar file compatibility reasons. Others criticized the app&\#x27;s design and suggested OpenAI donate to LibreOffice to improve Office format support. Some questioned whether the app downloads these on demand or bundles them upfront.

**Tags**: `#OpenAI`, `#ChatGPT`, `#software dependencies`, `#LibreOffice`, `#desktop app`

---

<a id="item-17"></a>
## [Ambient CSS v3 Brings Blender-Inspired 3D Lighting to CSS, Draws Criticism](https://ambientcss.vercel.app/) ⭐️ 6.0/10

Ambient CSS v3 is a new CSS library that attempts to simulate Blender-like 3D lighting effects by defining a lighting environment with direction, intensity, hue, and elevation, generating shadows and highlights dynamically. The Hacker News demo attracted significant attention but faced sharp criticism for broken implementation and poor design. The reaction reflects the web development community&\#x27;s evolving standards for both visual design and technical execution, highlighting the challenge of reviving skeuomorphic 3D effects in an era dominated by flat UI. It also underscores the importance of UX principles and performance when implementing complex visual effects. The library claims physics-based lighting, but the demo is reportedly buggy: light direction incorrectly affects the entire grid, stops outside arbitrary divs, and often fails. Color mappings like &\#x27;Brass&\#x27; turn into &\#x27;Olive&\#x27;, and some interactive knobs work inconsistently, with performance lag.

hackernews · kikkupico · Sep 1, 15:35 · [Discussion](https://news.ycombinator.com/item?id=49523387)

**Background**: CSS can create 3D-like effects using transforms, gradients, and box-shadows, but realistic lighting requires complex calculations typically done in 3D software like Blender. Earlier web eras used images and proprietary filters for similar effects; modern CSS has the potential to do it natively, but the trend toward flat design has diminished interest. Ambient CSS attempts to bring this back with a physics-based approach.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/kikkupico/ambientcss">kikkupico/ambientcss: A physics-based lighting system for CSS . Define...</a></li>
<li><a href="https://codepen.io/alexmwalker/pen/YXKLKw">3d Lighting Effects in CSS</a></li>

</ul>
</details>

**Discussion**: Commenters overwhelmingly criticized the library&\#x27;s design and UX, noting broken behavior, ugly textures, inconsistent controls, and a jarring mix of skeuomorphic elements with flat UI. Some pointed out the irony of attempting 3D effects when the industry has moved to flat design, and warned that AI-generated designs often lack proper UX principles. A few acknowledged the idea was neat but execution was poor.

**Tags**: `#CSS`, `#UI design`, `#3D effects`, `#frontend`, `#web development`

---

<a id="item-18"></a>
## [Simon Willison Builds GeoJSON Map Viewer with AI Assistance](https://simonwillison.net/2026/Sep/1/geojson/) ⭐️ 6.0/10

Simon Willison built a web-based GeoJSON Map Viewer tool with AI assistance, using GPT-5.6-Sol for initial suggestions and Claude Code with Fable 5.1 for iterations. He also discovered that ChatGPT Work can extract and combine government boundary data into GeoJSON files. This tool fills a gap for quick, client-side GeoJSON visualization and export, and illustrates the growing trend of AI-assisted development for niche tools. The ChatGPT boundary extraction technique could democratize access to government geospatial data. The tool is entirely client-side, using Leaflet and OpenStreetMap, with features like multiple shape layers, color/opacity controls, and PNG export at configurable resolution. The AI development pipeline involved GPT-5.6-Sol for ideation, Claude Code for web development, and Fable 5.1 for polishing.

rss · Simon Willison · Sep 1, 18:05

**Background**: GeoJSON is an open standard format for encoding geographic data structures like points, lines, and polygons, based on JSON. Simon Willison is a prolific developer known for creating simple, useful web tools and for exploring AI-assisted development. Claude Code is Anthropic&\#x27;s agentic coding tool that can understand codebases, edit files, and run commands; Fable is a version of Anthropic&\#x27;s Claude model with enhanced safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GeoJSON">GeoJSON</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#geojson`, `#tools`, `#ai-assisted-development`, `#mapping`, `#simon-willison`

---

<a id="item-19"></a>
## [YOLO26-RGB: Depth-Trained Backbone Transfers to Image Deraining](https://www.reddit.com/r/MachineLearning/comments/1w4fxln/yolo26rgb_repurposing_yolo26s_depthtrained/) ⭐️ 6.0/10

The experiment shows that initializing the backbone and neck of a deraining model with YOLO26&\#x27;s depth-estimation pretrained weights outperforms random initialization, achieving a +0.48 dB PSNR improvement across all 10 test sets, with a custom RGBHead decoder. This indicates that dense regression tasks like depth estimation can provide useful pretrained features for other low-level vision tasks, potentially reducing the need for large labeled datasets and training time in image restoration. The nano model \(5.25M\) achieved 27.94 dB PSNR vs 27.45 dB from scratch; the depth-trained initialization matched all 468 backbone+neck tensors, and the RGBHead uses residual output, LayerNorm, and skip connections to preserve fine details.

reddit · r/MachineLearning · /u/Naive-Explanation940 · Sep 1, 15:52

**Background**: Image deraining is the task of removing rain artifacts from images, important for outdoor autonomous systems. YOLO26 is a variant of the YOLO object detection family that includes a depth estimation model; its backbone is CSPDarknet, a convolutional network used in many YOLO versions, and its neck is a PAN-FPN structure for multi-scale feature fusion. Transfer learning in computer vision is common for high-level tasks like classification, but less explored for dense regression tasks such as deraining or depth estimation. PSNR and SSIM are standard metrics for image restoration quality.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2310.03535">[2310.03535] Towards Unified Deep Image Deraining: A Survey ... GitHub - nnUyi/DerainZoo: DerainZoo for collecting deraining ... Data-Driven single image deraining: A Comprehensive review ... UniRain: Unified Image Deraining with RAG-based Dataset ... Towards Unified Deep Image Deraining: A Survey and a New ... Single Image Deraining: From Model-Based to Data-Driven and ...</a></li>
<li><a href="https://deepwiki.com/bubbliiiing/yolov4-pytorch/2.1-cspdarknet53-backbone">CSPDarknet53 Backbone | bubbliiiing/yolov4-pytorch | DeepWiki</a></li>
<li><a href="https://deepwiki.com/motokimura/yolox-ti-lite_tflite/2.1-backbone-and-neck:-cspdarknet-and-yolopafpn">Backbone and Neck: CSPDarknet and YOLOPAFPN</a></li>

</ul>
</details>

**Tags**: `#transfer learning`, `#computer vision`, `#image restoration`, `#YOLO`, `#depth estimation`

---