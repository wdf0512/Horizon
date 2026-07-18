---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 37 items, 15 important content pieces were selected

---

1. [The Zilog Z80 Microprocessor Celebrates Its 50th Anniversary](#item-1) ⭐️ 8.0/10
2. [JWST Finds Atmosphere on Rocky Exoplanet in Habitable Zone](#item-2) ⭐️ 8.0/10
3. [Julia Evans Shares Practical Tips for Running SQLite in Production](#item-3) ⭐️ 8.0/10
4. [Kimi K3: Moonshot AI's 2.8T-parameter model tested via pelican SVG benchmark](#item-4) ⭐️ 8.0/10
5. [Firefox in WebAssembly: Puter's Browser-in-Browser Demo](#item-5) ⭐️ 8.0/10
6. [Thinking Machines Lab Releases Inkling, a 975B-Parameter Open-Weight Multimodal Model](#item-6) ⭐️ 8.0/10
7. [Linus Torvalds Declares Linux Will Not Be Anti-AI, Calls AI a Useful Tool](#item-7) ⭐️ 8.0/10
8. [ExTernD: Expanded-Rank Ternary Decomposition for Near-Lossless LLM Quantization](#item-8) ⭐️ 8.0/10
9. [Kaiser Nurses Raise Concerns Over AI Surveillance and Workplace Metrics](#item-9) ⭐️ 7.0/10
10. [GPT-5.6 Codex Bug Causes Accidental File Deletion in Full Access Mode](#item-10) ⭐️ 7.0/10
11. [Spot Birds Not Golf: Offsetting Data Center Water Use with Parks](#item-11) ⭐️ 6.0/10
12. [Stereo2Spatial: Open-Source Binaural Music Converter Using Flow-Matching Diffusion](#item-12) ⭐️ 6.0/10
13. [EU AI Act Corpus Released with 933 Legal Chunks and BGE-M3 Embeddings](#item-13) ⭐️ 6.0/10
14. [New Recurrent Architecture DABSN Seeks Collaborators for Scaling and Evaluation](#item-14) ⭐️ 6.0/10
15. [ECCV Student Presenters Required to Pay Full Registration Fee](#item-15) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [The Zilog Z80 Microprocessor Celebrates Its 50th Anniversary](https://goliath32.com/blog/z80.html) ⭐️ 8.0/10

A nostalgic blog post marks the 50th anniversary of the Zilog Z80 microprocessor, sparking a wave of personal memories and technical reflections from the developer community. The Z80 powered countless early home computers, game consoles, and embedded systems, shaping a generation of programmers. Its anniversary highlights the enduring legacy of foundational hardware in today's computing landscape. The Z80 was introduced in July 1976 as an enhanced, binary-compatible successor to the Intel 8080, but community members note that the parity flag behavior differed, making it not fully compatible. Zilog discontinued the Z80 in April 2024 after 48 years of production.

hackernews · st_goliath · Jul 17, 19:41 · [Discussion](https://news.ycombinator.com/item?id=48951461)

**Background**: The Zilog Z80 is an 8-bit microprocessor designed by Federico Faggin and Masatoshi Shima, released in 1976. It became widely used in home computers like the ZX Spectrum, MSX, and the Sega Game Gear, as well as in embedded systems. Its simple architecture and rich instruction set made it popular for learning assembly language.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zilog">Zilog - Wikipedia</a></li>
<li><a href="https://www.computinghistory.org.uk/det/12157/Zilog-Z-80-Microcomputer-System/">Zilog Z - 80 Microcomputer System - Computer - Computing History</a></li>

</ul>
</details>

**Discussion**: The comments are overwhelmingly nostalgic, with many sharing personal stories of first programming experiences on Z80-based systems like the ZX-81 and Timex computers. One commenter pointed out a technical inaccuracy: the Z80 is not fully binary-compatible with the 8080 due to parity flag differences. Overall, the discussion is warm and appreciative of the chip's impact.

**Tags**: `#retrocomputing`, `#history`, `#microprocessors`, `#z80`, `#vintage-computing`

---

<a id="item-2"></a>
## [JWST Finds Atmosphere on Rocky Exoplanet in Habitable Zone](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

The James Webb Space Telescope has confirmed, via emission spectroscopy, the presence of an atmosphere on LHS 1140b, a rocky exoplanet orbiting within the habitable zone of a red dwarf star. This rules out the possibility that it is a mini-Neptune and marks the first such detection on a potentially habitable Earth-like planet. This discovery is significant because it demonstrates that rocky planets in the habitable zones of red dwarfs can retain atmospheres despite intense stellar activity, boosting the prospects for finding life beyond Earth. It also refines our understanding of planetary evolution and habitability conditions. The atmosphere was detected using JWST's emission spectroscopy as the planet passed behind its star, which measured the thermal glow and allowed scientists to rule out a thick hydrogen-helium envelope characteristic of mini-Neptunes. The planet is only 48 light-years away, making it a prime candidate for future atmospheric characterization.

hackernews · neversaydie · Jul 17, 14:06 · [Discussion](https://news.ycombinator.com/item?id=48947560)

**Background**: Red dwarfs are the most common type of star in the galaxy, but they are often active with flares and strong stellar winds that could strip away atmospheres from close-in planets. Emission spectroscopy involves analyzing the light emitted by a planet itself (as opposed to starlight passing through its atmosphere) to determine its composition. The habitable zone is the region around a star where temperatures may allow liquid water to exist on a planet's surface.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Emission_spectroscopy">Emission spectroscopy</a></li>

</ul>
</details>

**Discussion**: The community discussion highlighted initial skepticism about the planet's ability to retain an atmosphere, which was resolved by the JWST spectroscopy data. Some users called for building a solar gravitational lens telescope for future direct imaging, while others debated the Fermi paradox implications and the feasibility of interstellar probes within centuries.

**Tags**: `#astronomy`, `#exoplanets`, `#JWST`, `#habitability`, `#space-exploration`

---

<a id="item-3"></a>
## [Julia Evans Shares Practical Tips for Running SQLite in Production](https://jvns.ca/blog/2026/07/17/learning-about-running-sqlite/) ⭐️ 8.0/10

On July 17, 2026, Julia Evans published a blog post detailing practical techniques for operating SQLite in production, including using the `.expert` mode for query optimization and various backup strategies. These tips help developers avoid common pitfalls in SQLite production deployments, potentially improving performance and reliability for the vast number of applications that embed SQLite, from mobile apps to edge devices and web backends. The `.expert` mode in SQLite's CLI suggests indexes based on query analysis. Backup approaches include using `sqlite3 .dump` piped through `zstd` for compressed, rsync-friendly dumps, and tools like `s3-credentials` to generate scoped AWS credentials. For deletes, batching and preloading rowids can prevent blocking writers.

hackernews · surprisetalk · Jul 17, 17:45 · [Discussion](https://news.ycombinator.com/item?id=48950122)

**Background**: SQLite is a serverless, zero-configuration, self-contained SQL database engine that stores data in a single file. It is widely used in production, but its simplicity requires careful handling of concurrency, backups, and query performance. The `.expert` mode is a special CLI command that helps find missing indexes, while backup strategies often leverage WAL mode to avoid blocking writers.

<details><summary>References</summary>
<ul>
<li><a href="https://databaseschool.com/series/high-performance-sqlite/videos/41">Where to add indexes - High Performance SQLite - Database School</a></li>
<li><a href="https://oldmoe.blog/2024/04/30/backup-strategies-for-sqlite-in-production/">Backup strategies for SQLite in production – Oldmoe's blog</a></li>

</ul>
</details>

**Discussion**: Commenters valued the `.expert` mode for avoiding manual query plan reading. They shared production backup scripts using `sqlite3 .dump | zstd`, and a tool `s3-credentials` to simplify AWS permissions. Others noted that DELETE operations can be optimized by batching and preloading rowids with SELECT, and that WAL mode enables non-blocking backups.

**Tags**: `#SQLite`, `#database`, `#backup`, `#performance`, `#devops`

---

<a id="item-4"></a>
## [Kimi K3: Moonshot AI's 2.8T-parameter model tested via pelican SVG benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything) ⭐️ 8.0/10

Moonshot AI released Kimi K3, a 2.8 trillion-parameter flagship model, with an open-weight release promised by July 27, 2026; it claims benchmark dominance over Claude Opus 4.8 and GPT-5.5 High, and tops the Arena.ai Frontend Code arena. Simon Willison used his 'pelican riding a bicycle' SVG test to reveal hidden prompt engineering and evaluate cost/quality. This release marks the first open 3T-class model, intensifying competition with DeepSeek and Western labs; its high pricing signals a shift toward premium open-weight models. The pelican test demonstrates that even playful benchmarks can surface critical details about tokenization, hidden system prompts, and evaluation methodology. The model uses Kimi Delta Attention (KDA) hybrid linear attention, a 1M-token context window, and costs $3/$15 per million input/output tokens; the pelican test consumed 95 input tokens, 16,658 output tokens (13,241 reasoning), and cost 25 cents. A hidden 85-token system prompt was inferred from the token count, possibly for reasoning effort.

rss · Simon Willison · Jul 16, 20:19 · [Discussion](https://news.ycombinator.com/item?id=48947717)

**Background**: The 'pelican riding a bicycle' is a humorous benchmark started by Simon Willison in 2024, asking models to generate an SVG of a pelican on a bike, to compare visual creativity, code quality, and consistency. Moonshot AI is a Chinese AI startup, and Kimi K3 is a large language model with vision capabilities. The benchmark's popularity has led to concerns about training data contamination.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/pelican-bicycle">GitHub - simonw/pelican-bicycle: LLM benchmark: Generate an SVG of a pelican riding a bicycle · GitHub</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K 3 - Kimi API Platform</a></li>
<li><a href="https://www.bbc.com/news/articles/cy9w4q8pgp0o">China's Moonshot AI claims Kimi K 3 can rival OpenAI and Anthropic</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether the pelican benchmark is now contaminated (since it appears in many training corpora), noted tokenizer quirks revealing a hidden system prompt, suggested a more agentic variant (SWE-bench-adversarial-pelican-gen), and pointed out that single-run results may not be representative; overall, the discussion valued the test as a probe rather than a definitive ranking.

**Tags**: `#AI`, `#LLM`, `#Kimi K3`, `#model evaluation`, `#SVG generation`

---

<a id="item-5"></a>
## [Firefox in WebAssembly: Puter's Browser-in-Browser Demo](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 8.0/10

Puter compiled Firefox (Gecko) to WebAssembly, enabling the entire browser to run inside another browser, with network traffic proxied via WebSocket through their servers. The project used AI code generation from Claude Opus and Fable models. This demonstrates the extreme portability of WebAssembly and the potential for running complex, sandboxed applications in the browser, while highlighting how AI-assisted programming can drastically reduce the time and cost of such ambitious porting efforts. The demo relies on Gecko's single-process mode, uses a 233MB gecko.wasm file and 18MB of assets, and routes all HTTP traffic through Puter's server via the Wisp protocol over WebSocket, which the team had to scale up during the HN launch. An estimated $25,000 in AI tokens was consumed, but a subscription plan reduced actual expenses. A similar WebKitWasm project exists but lacks an online demo.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (WASM) is a low-level binary format that runs in browsers at near-native speed, allowing C/C++ codebases to be compiled for the web. The Wisp protocol is a lightweight method for proxying TCP/UDP sockets over a single WebSocket, used to bypass the browser's inability to open arbitrary network connections. Claude Opus is Anthropic's most capable LLM, while Claude Fable is a newer model with higher token pricing; both were used to assist in the complex compilation process.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus">Claude Opus</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#WebAssembly`, `#Firefox`, `#browser`, `#AI-assisted-development`, `#demo`

---

<a id="item-6"></a>
## [Thinking Machines Lab Releases Inkling, a 975B-Parameter Open-Weight Multimodal Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab has released Inkling, a 975 billion-parameter Mixture-of-Experts multimodal model under the Apache 2.0 license, with a smaller 276B variant promised later. This release provides a competitive open-weights multimodal model from a US lab, strengthening the ecosystem with a permissive license for fine-tuning, though the sparse documentation raises transparency concerns. Inkling has 975B total parameters with 41B active per token, trained on 45 trillion tokens of text, images, audio, and video. The model card and training data documentation are notably sparse, and the lab describes it as a strong base for fine-tuning via their Tinker platform, not a frontier model.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) is a transformer architecture that sparsely activates multiple expert sub-networks, enabling efficient training of very large models with fewer active parameters. Open-weights models make their trained parameters publicly available, allowing anyone to use, modify, and distribute them. A model card is a standard transparency document that describes a model's intended use, performance, limitations, and training data; thorough model cards are important for responsible AI deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.snowflake.com/en/artificial-intelligence/ai-governance/model-card/">What Is a Model Card ? Sections, Templates & Best... | Snowflake</a></li>

</ul>
</details>

**Tags**: `#open-weights`, `#LLM`, `#multimodal`, `#Mixture-of-Experts`, `#AI`

---

<a id="item-7"></a>
## [Linus Torvalds Declares Linux Will Not Be Anti-AI, Calls AI a Useful Tool](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the top-level maintainer of Linux, firmly stated on a mailing list that AI is a useful tool and Linux will not be an anti-AI project, inviting those who disagree to fork it. This definitive stance from a highly influential figure in open-source sets a precedent for other projects, potentially shaping the integration of AI tools in software development and calming the community debate about AI's role in open-source. Torvalds noted that just a year ago AI's usefulness was not as clear, but now it is no longer in question. He added that other questions about AI, such as its economic impact, remain, but the question of utility is settled.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linux is the world's most widely used open-source operating system kernel, maintained by thousands of developers and overseen by Linus Torvalds since its creation in 1991. The open-source community has been debating the use of AI, with concerns about copyright, licensing, and code quality. Some projects have adopted anti-AI policies, such as rejecting AI-generated contributions. Torvalds' statement directly addresses this debate, asserting that the Linux project will not take an anti-AI stance.

**Tags**: `#open-source`, `#AI`, `#Linus Torvalds`, `#Linux`, `#software development`

---

<a id="item-8"></a>
## [ExTernD: Expanded-Rank Ternary Decomposition for Near-Lossless LLM Quantization](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

The paper proposes ExTernD, a method that decomposes weight matrices into two ternary matrices and a diagonal scaling matrix, enabling arbitrary precision in ternary post-training quantization by allowing the inner rank to be arbitrarily large. This approach allows LLMs to be deployed with near-lossless accuracy using ternary operations that replace multiplications with simple additions, drastically reducing computational cost and enabling efficient inference on hardware. ExTernD incurs only a modest increase in VRAM compared to standard quantization, yet its expanded rank enables arbitrarily close approximation to original weights. The paper demonstrates that the accuracy can be made arbitrarily small, i.e., arbitrarily high fidelity.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Ternary quantization maps weights to {−1, 0, +1}, eliminating multiplications. Post-training quantization (PTQ) applies compression after training without retraining, but often suffers accuracy loss. Standard ternary PTQ with fixed matrix size limits representational power; ExTernD uses expanded-rank decomposition (similar to full-rank factorization) to overcome this.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2303.01505">Ternary Quantization : A Survey</a></li>
<li><a href="https://www.emergentmind.com/topics/ternary-quantization">Ternary Quantization in Neural Networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rank_factorization">Rank factorization - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#ternary quantization`, `#post-training quantization`, `#LLM compression`, `#model efficiency`, `#expanded rank decomposition`

---

<a id="item-9"></a>
## [Kaiser Nurses Raise Concerns Over AI Surveillance and Workplace Metrics](https://localnewsmatters.org/2026/07/15/kaiser-nurses-say-ai-workplace-surveillance-are-making-their-jobs-and-patient-care-worse/) ⭐️ 7.0/10

The article reports that Kaiser Permanente nurses are complaining that AI tools and workplace surveillance are degrading their jobs and patient care quality. However, community discussion reveals that many complaints target call center metrics and care rationing pressures rather than AI itself, and that a 2024 AI empathy evaluation pilot was discontinued. This highlights the tension between healthcare efficiency metrics and the human touch in caregiving, affecting both nurse well-being and patient outcomes. It also reflects broader concerns about AI transparency and oversight in high-stakes environments. The AI empathy tool was a 2024 pilot that has been discontinued, and some nurses find medical LLM tools valuable for live translation, note summarization, and quick answers. However, workplace surveillance and metrics that pressure staff to ration care remain contentious issues.

hackernews · gnabgib · Jul 17, 22:26 · [Discussion](https://news.ycombinator.com/item?id=48952880)

**Background**: Kaiser Permanente is a large US healthcare consortium. AI-powered tools like large language models (LLMs) are increasingly used in healthcare for tasks such as documentation, translation, and clinical decision support. Workplace surveillance can include monitoring call times, typing speed, or adherence to scripts, often using algorithms to evaluate performance.

**Discussion**: The community discussion brings nuance: some note that the real issue is metrics and care rationing, not AI, and point out that an AI empathy pilot was already discontinued. Others share positive experiences with AI note-taking reducing stress, while concerns about surveillance and power dynamics persist. The impact of AI is mixed, with both relief and anxiety among healthcare workers.

**Tags**: `#healthcare`, `#AI`, `#workplace surveillance`, `#ethics`, `#metrics`

---

<a id="item-10"></a>
## [GPT-5.6 Codex Bug Causes Accidental File Deletion in Full Access Mode](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 7.0/10

OpenAI has identified a bug in GPT-5.6 Codex where, when full access mode is enabled without sandboxing or auto review, the model may accidentally delete files by attempting to override the $HOME environment variable and then mistakenly deleting the user's home directory. This bug underscores the significant risks of granting AI coding agents unrestricted file system access, highlighting the importance of sandboxing, approval mechanisms, and auto review to prevent catastrophic unintended actions. The deletion occurs when the model mistakenly deletes $HOME after overriding it to set a temporary directory. It requires full access mode, the absence of sandboxing protections, and auto review disabled. Auto review, which automatically evaluates agent actions, can catch such mistakes.

rss · Simon Willison · Jul 16, 17:45

**Background**: Codex operates in different modes: Read Only, Default (Agent), and Full Access. Full Access mode grants the agent unrestricted capabilities, suitable only for trusted tasks. Sandboxing provides isolation, limiting access to the host system and protecting critical paths. Auto review is an automated mechanism that reviews agent actions, approving around 99% of actions and rejecting unsafe ones to prevent harmful outcomes.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/codex/llms-full.txt">developers.openai.com/ codex /llms- full .txt</a></li>
<li><a href="https://openai-codex.mintlify.app/concepts/sandboxing">Sandboxing - Codex CLI</a></li>
<li><a href="https://alignment.openai.com/auto-review">Auto - review of agent actions without synchronous human oversight</a></li>

</ul>
</details>

**Tags**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#software-bugs`

---

<a id="item-11"></a>
## [Spot Birds Not Golf: Offsetting Data Center Water Use with Parks](https://simonwillison.net/2026/Jul/17/spot-birds-not-golf/#atom-everything) ⭐️ 6.0/10

A blog post humorously suggests that hyperscalers like Google, which consumed 10.9 billion gallons of water in 2025, could offset their water usage by purchasing golf courses and converting them into public parks, with the math showing that buying 40 Coachella Valley golf courses would cover Google's daily water consumption. This witty comparison highlights the enormous water footprint of AI data centers, making the abstract consumption figures tangible and drawing attention to the sustainability challenges of growing AI infrastructure. Google's 30 million gallons per day is compared to a single golf course's 750,000 gallons per day; the proposed solution would require buying 40 courses, but the post is satirical rather than a serious policy proposal.

rss · Simon Willison · Jul 17, 02:58

**Background**: Hyperscalers are cloud providers operating massive data centers, which require substantial water for cooling. Google's 2026 environmental report disclosed 10.9 billion gallons of water use in 2025. Golf courses, especially in arid regions like Coachella Valley, are known for high water consumption, making the comparison a pointed commentary on resource allocation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hyperscaler">Hyperscaler</a></li>

</ul>
</details>

**Tags**: `#ai-energy-usage`, `#ai`, `#sustainability`, `#data-centers`, `#water-usage`

---

<a id="item-12"></a>
## [Stereo2Spatial: Open-Source Binaural Music Converter Using Flow-Matching Diffusion](https://www.reddit.com/r/MachineLearning/comments/1uzevbg/stereo2spatial_convert_stereo_music_tracks_to/) ⭐️ 6.0/10

The developer released Stereo2Spatial, an open-source model that converts stereo music to spatial binaural audio using a flow-matching diffusion model, featuring a novel memory token mechanism for long-context consistency and a waveform-based approach stabilized by amplitude lifting, trained on 7,669 tracks. This model allows users to convert any stereo track into a spatial binaural mix, expanding the availability of immersive audio content. Its technical innovations in waveform-based diffusion training and memory tokens could advance generative audio research. The waveform model was trained in two stages (10-34s and 122s clips) on 7,669 tracks with amplitude lifting clipping to ±12, stabilizing training. It currently outputs binaural audio, not full 7.1.4, but the codebase is designed for future multichannel conversion.

reddit · r/MachineLearning · /u/kittenkrazy · Jul 17, 22:55

**Background**: Flow matching is a generative modeling technique that learns a probability path between noise and data, closely related to diffusion models. EAR-VAE is a variational autoencoder for high-quality audio reconstruction in latent space. Spatial audio formats like 7.1.4 use multiple speakers for immersive sound, and binaural rendering recreates that spatial illusion over headphones.

<details><summary>References</summary>
<ul>
<li><a href="https://diffusionflow.github.io/">Diffusion Meets Flow Matching</a></li>
<li><a href="https://arxiv.org/html/2601.12950v1">ImmersiveFlow : Stereo - to -7.1.4 Spatial Audio Generation with Flow ...</a></li>
<li><a href="https://huggingface.co/earlab/EAR_VAE">earlab/ EAR _ VAE · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#spatial audio`, `#diffusion models`, `#generative models`, `#audio processing`, `#machine learning`

---

<a id="item-13"></a>
## [EU AI Act Corpus Released with 933 Legal Chunks and BGE-M3 Embeddings](https://www.reddit.com/r/MachineLearning/comments/1uytlac/eu_ai_act_openrag_933_legally_structured_chunks/) ⭐️ 6.0/10

A new dataset, EU AI Act OpenRAG, has been released, providing the full text of Regulation (EU) 2024/1689 as 933 chunks structured by legal paragraphs, each with a BGE-M3 embedding, and demonstrating improved retrieval over naive chunking. This dataset enables more accurate and reliable retrieval-augmented generation for legal AI applications, particularly for complying with the EU AI Act, and sets a standard for structuring legal corpora for NLP. The corpus chunks by legal structure (article paragraphs, recitals, definitions, annex points) rather than sliding windows, uses 1024-dim BGE-M3 embeddings, and improves retrieval: scenario article recall@20 rose from 0.449 to 0.541, QA hit@10 from 0.898 to 0.927; however, classification accuracy was slightly lower, suggesting generator dominance in that task.

reddit · r/MachineLearning · /u/Automatic-Forever-63 · Jul 17, 08:18

**Background**: The EU AI Act (Regulation 2024/1689) is a landmark law governing AI systems in the EU. BGE-M3 is a multilingual embedding model from BAAI that supports dense, sparse, and multi-vector retrieval, and can handle up to 8192 tokens. RAG (Retrieval-Augmented Generation) pipelines enhance language models by first retrieving relevant text chunks from a knowledge base. Legal texts are often chunked naively, but structure-aware chunking can improve retrieval precision.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/BAAI/bge-m3?ref=blog-ko.allganize.ai">BAAI/ bge - m 3 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#RAG`, `#legal NLP`, `#EU AI Act`, `#embeddings`, `#dataset`

---

<a id="item-14"></a>
## [New Recurrent Architecture DABSN Seeks Collaborators for Scaling and Evaluation](https://www.reddit.com/r/MachineLearning/comments/1uycffg/seeking_collaborators_for_scaling_and_independent/) ⭐️ 6.0/10

An independent researcher released a preprint and code for DABSN, a new recurrent architecture, and seeks collaborators for scaling and independent evaluation after training a 24M-parameter language model on 1B tokens. This open, reproducible approach could accelerate research into alternatives to Transformer-based models, potentially leading to more efficient architectures for long-context tasks. The architecture uses a Dynamic Adaptive Bias State Network cell, with implementations in PyTorch, C++, and Triton; the initial LM was small (24M params, 1B tokens), and scaling to larger models is needed.

reddit · r/MachineLearning · /u/BleedingXiko · Jul 16, 19:17

**Background**: Recurrent neural networks process sequences sequentially, offering potential efficiency for long contexts compared to Transformers. The MQAR (Multi-Query Associative Recall) benchmark tests a model's ability to perform multiple associative recall operations within a single sequence, commonly used to evaluate long-range memory. The project also includes other standard benchmarks such as Copy, Key-Value retrieval, and A5/60 for testing reasoning and memory.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/multi-query-associative-recall-mqar-99600239-c8a9-49da-a81b-9ce2f354c1aa">MQAR : Multi-Query Associative Recall</a></li>

</ul>
</details>

**Tags**: `#recurrent-neural-networks`, `#language-modeling`, `#architecture`, `#research-collaboration`, `#preprint`

---

<a id="item-15"></a>
## [ECCV Student Presenters Required to Pay Full Registration Fee](https://www.reddit.com/r/MachineLearning/comments/1uxyd6z/why_is_eccv_so_insanely_expensive_for_students/) ⭐️ 6.0/10

A student discovered that ECCV requires a full registration fee of $805 USD for paper presenters, even though the student early bird rate is $440, and their travel grant and registration waiver applications were rejected. This highlights the financial barriers for students at top-tier conferences, potentially limiting participation from researchers with limited funding and affecting the accessibility of academic exchange. The student early bird registration is $440, but any accepted paper must be covered by a full registration of $805; travel grants and fee waivers applied for were rejected.

reddit · r/MachineLearning · /u/NotGondor · Jul 16, 09:55

**Background**: ECCV (European Conference on Computer Vision) is a premier computer vision conference. Academic conferences typically require at least one author to register at the full rate to present a paper, in order to cover venue and publication costs. Student discounts are commonly available for attendees without a paper, but presenting authors are usually not eligible.

**Tags**: `#ECCV`, `#conference fees`, `#academia`, `#student issues`, `#machine learning`

---