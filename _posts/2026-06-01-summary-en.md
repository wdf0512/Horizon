---
layout: default
title: "Horizon Summary: 2026-06-01 (EN)"
date: 2026-06-01
lang: en
---

> From 44 items, 7 important content pieces were selected

---

1. [NVIDIA Cosmos 3: First Open Omni-Model for Physical AI Reasoning and Action](#item-1) ⭐️ 9.0/10
2. [MiniMax M3: Open-Source Model with 1M Context, Multimodality, and Top Coding Scores](#item-2) ⭐️ 9.0/10
3. [Cloudflare Turnstile Uses WebGL Fingerprinting, Raising Privacy Concerns](#item-3) ⭐️ 8.0/10
4. [OpenAI Blocks Apps Script Generation After Data Exfiltration Flaw in ChatGPT for Sheets](#item-4) ⭐️ 8.0/10
5. [Dav2d: Open-Source AV2 Decoder Released by VideoLAN](#item-5) ⭐️ 8.0/10
6. [Meta Launches Subscription Plans for Instagram, Facebook, and WhatsApp](#item-6) ⭐️ 8.0/10
7. [Restartable Sequences](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [NVIDIA Cosmos 3: First Open Omni-Model for Physical AI Reasoning and Action](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai) ⭐️ 9.0/10

NVIDIA has released Cosmos 3, the first open omni-model for physical AI, integrating reasoning and action capabilities into a unified system for embodied applications. This release marks a significant step toward democratizing physical AI, enabling researchers and developers to build autonomous systems like robots and self-driving cars with advanced perception and reasoning without relying on proprietary models. Cosmos 3 is released as an open omni-model, combining reasoning and action in a single framework; specific technical details, such as model architecture and training data, have yet to be fully disclosed.

rss · Hugging Face Blog · Jun 1, 04:44

**Background**: Physical AI refers to AI systems that interact with the real world, such as robots and autonomous vehicles, requiring perception, reasoning, and action capabilities. An omni-model is a single model that handles multiple modalities (e.g., text, images, video) and integrates reasoning across them, as exemplified by Google's Gemini Omni. NVIDIA's Cosmos 3 extends this omni-model approach to the physical domain, aiming to provide a unified solution for embodied AI tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>
<li><a href="https://deepmind.google/models/gemini-omni/">Gemini Omni — Google DeepMind</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Cosmos`, `#physical AI`, `#omni-model`, `#open-source`

---

<a id="item-2"></a>
## [MiniMax M3: Open-Source Model with 1M Context, Multimodality, and Top Coding Scores](https://www.minimaxi.com/blog/minimax-m3) ⭐️ 9.0/10

MiniMax launched M3, an open-source model with a 1 million token context window, native multimodal capabilities, and a 59% score on SWE-Bench Pro, surpassing GPT-5.5 and Gemini 3.1 Pro. The release includes the MiniMax Code agent and an affordable token subscription plan at 49 yuan per month for 600 million tokens. This is China's first open-source model to simultaneously offer ultra-long context, advanced coding, and native multimodal abilities, with a coding benchmark score far exceeding current top models (typically around 23%). The affordable token plan and agent product lower the barrier for developers to build complex AI applications. M3 uses Memory Sparse Attention (MSA), which internally retrieves only the most relevant key-value vectors for attention, enabling efficient long-context processing. The model weights and technical report will be released within 10 days, and the API is now open. The 49 yuan Plus plan offers 15 times the token capacity of comparable overseas subscriptions.

telegram · zaihuapd · Jun 1, 01:55

**Background**: The Memory Sparse Attention (MSA) architecture is an end-to-end trainable latent-memory framework that overcomes the quadratic cost of long sequences by selectively loading only the most pertinent key-value pairs, similar to an internal retrieval system. SWE-Bench Pro is a challenging software engineering benchmark where the best models previously scored around 23%, so M3's 59% represents a major breakthrough. MiniMax is a prominent Chinese AI company known for earlier models like M2.5.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.23516">[2603.23516] MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens</a></li>
<li><a href="https://labs.scale.com/leaderboard/swe_bench_pro_public">SWE-Bench Pro Leaderboard AI Coding Benchmark (Public Dataset) | Scale</a></li>
<li><a href="https://github.com/EverMind-AI/MSA">GitHub - EverMind-AI/MSA: Memory Sparse Attention - A scalable, end-to-end trainable latent-memory framework for 100M-token contexts. · GitHub</a></li>

</ul>
</details>

**Tags**: `#多模态大模型`, `#开源模型`, `#AI代理`, `#编程辅助`

---

<a id="item-3"></a>
## [Cloudflare Turnstile Uses WebGL Fingerprinting, Raising Privacy Concerns](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) ⭐️ 8.0/10

Cloudflare’s Turnstile CAPTCHA has been found to employ WebGL fingerprinting, silently collecting detailed GPU and graphics information to track visitors and identify bots even when users enable browser privacy protections like Firefox’s resistFingerprinting. This technique undermines key browser privacy defenses, potentially locking users who value anonymity out of a significant portion of the web. It fuels the cat-and-mouse race between anti-bot services and privacy-conscious users, threatening the open web. WebGL fingerprinting renders a hidden 3D scene and analyzes subtle GPU differences to create a unique identifier, requiring no user interaction. Spoofing this fingerprint often demands complex workarounds like CycleTLS for JA3/TLS fingerprint altering, and even strict privacy modes can be detected.

hackernews · HypnoticOcelot · May 31, 14:13 · [Discussion](https://news.ycombinator.com/item?id=48345840)

**Background**: WebGL is a JavaScript API that lets websites render 3D graphics using the device's GPU; because hardware and driver combinations vary, the rendering output can be used to create a unique 'fingerprint' that tracks users across sites. Cloudflare Turnstile is a CAPTCHA alternative meant to distinguish bots without showing puzzles, but its use of fingerprinting clashes with privacy expectations. Common defenses include Firefox's privacy.resistFingerprinting setting, which tries to standardize fingerprint values, though Turnstile's technique may bypass it.

<details><summary>References</summary>
<ul>
<li><a href="https://browserleaks.com/webgl">WebGL Browser Report - WebGL Fingerprinting - BrowserLeaks</a></li>
<li><a href="https://medium.com/@datajournal/what-is-webgl-fingerprinting-and-how-to-bypass-it-60893a9ca382">What is WebGL Fingerprinting? How It Works & Tips | Medium</a></li>
<li><a href="https://developers.cloudflare.com/turnstile/">Overview · Cloudflare Turnstile docs</a></li>

</ul>
</details>

**Discussion**: Commenters note that fingerprinting is a practical necessity for bot detection, with some already using JA3/TLS fingerprints. Others express frustration over breakage of privacy-respecting browsers, warn that escalating anti‑bot measures may turn the internet into a walled garden, and developers of minority browsers report user impacts, seeking mitigation help.

**Tags**: `#privacy`, `#web-fingerprinting`, `#cloudflare`, `#web-api`, `#anti-bot`

---

<a id="item-4"></a>
## [OpenAI Blocks Apps Script Generation After Data Exfiltration Flaw in ChatGPT for Sheets](https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration) ⭐️ 8.0/10

Security researchers discovered that ChatGPT for Google Sheets could be exploited to exfiltrate workbook data, and OpenAI responded by removing the model's ability to generate Google Apps Script code. The flaw demonstrates how AI integrations with productivity tools can inadvertently create data theft vectors, and the incident underscores the pressing need for secure disclosure processes and robust safeguards in LLM-powered applications. The attack tricked the model into generating malicious Apps Script code that could access and transfer sheet contents; OpenAI acknowledged a gap in its disclosure pipeline and quickly removed the code-generation capability to protect users.

hackernews · hackerBanana · May 31, 20:35 · [Discussion](https://news.ycombinator.com/item?id=48349487)

**Background**: Google Apps Script is a cloud-based JavaScript platform that allows automation and customization within Google Workspace apps like Sheets. Data exfiltration refers to unauthorized data transfer, often by malicious actors. The ChatGPT for Google Sheets extension enables users to interact with an AI model directly in their spreadsheets.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Apps_Script">Google Apps Script</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_exfiltration">Data exfiltration</a></li>

</ul>
</details>

**Discussion**: OpenAI's security team acknowledged the research and apologized for the disclosure delay, while removing Apps Script generation. Some commenters criticized the lack of response to the initial disclosure. Broader concerns were raised about the security of LLM tool integrations, with calls for local execution, containerization, and proper application-layer security before deploying AI agents that handle sensitive data.

**Tags**: `#security`, `#data-exfiltration`, `#LLM`, `#Google-Sheets`, `#vulnerability`

---

<a id="item-5"></a>
## [Dav2d: Open-Source AV2 Decoder Released by VideoLAN](https://jbkempf.com/blog/2026/dav2d/) ⭐️ 8.0/10

VideoLAN has announced dav2d, a new open-source, CPU-based AV2 decoder that builds on the highly optimized dav1d project, aiming to deliver fast and correct software decoding for the next-generation AV2 codec. AV2 promises around 30% better compression than AV1 but is roughly five times more complex to decode, making efficient software decoders like dav2d crucial for early adoption, hardware compatibility, and serving as a reference implementation that shapes the evolving specification. AV2 decoding is five times more computationally demanding than AV1, meaning real-time software playback will require aggressive, architecture-specific optimization; dav2d is still in early development and is not yet production-ready, as the AV2 specification was only finalized in May 2026.

hackernews · captain_bender · May 31, 11:44 · [Discussion](https://news.ycombinator.com/item?id=48344961)

**Background**: AV1 is an open, royalty-free video codec developed by the Alliance for Open Media, now widely adopted by streaming platforms. Its successor, AV2, was released on May 28, 2026, using a similar framework but with major innovations to improve compression. VideoLAN’s dav1d was a breakthrough software decoder that enabled real-time AV1 playback on many devices, and dav2d aims to replicate that success. The new codec’s extreme complexity, however, raises concerns about the viability of software-only decoding in the absence of dedicated hardware accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AV2_(video_coding_format)">AV2 (video coding format)</a></li>
<li><a href="https://www.phoronix.com/news/AV2-1.0-Specification-Released">AV 2 v1.0 Specification Released For Next-Gen Video Coding - Phoronix</a></li>
<li><a href="https://www-test.videolan.org/projects/dav2d/">dav2d - VideoLAN</a></li>

</ul>
</details>

**Discussion**: Hacker News comments reflected skepticism about whether AV2’s modest size reduction justifies obsoleting existing AV1 hardware decoders, with many voicing concerns over the steep decoding cost. Others highlighted that field decoders like dav2d are essential for maturing the specification—quoting the adage that a codec standard isn’t complete until a field implementation exists—while also suggesting that dav2d’s work should be left to proceed without undue criticism.

**Tags**: `#AV2`, `#video codec`, `#software decoding`, `#dav2d`, `#performance`

---

<a id="item-6"></a>
## [Meta Launches Subscription Plans for Instagram, Facebook, and WhatsApp](https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/) ⭐️ 8.0/10

On May 27, 2026, Meta officially launched subscription plans for Instagram, Facebook, and WhatsApp, offering users ad-free experiences and curated social feeds for a monthly fee, with AI-powered plans announced to follow. This signals a major shift from Meta's pure advertising business model, potentially reshaping the social media landscape by giving users a privacy-first, ad-free alternative and challenging the 'if it's free, you're the product' paradigm. Subscriptions start at $5 per month, with premium tiers up to $49.99 offering unlimited ad-free access and only friends' updates; Meta also plans to introduce AI-enhanced subscription tiers, though specifics remain undisclosed.

hackernews · tambourine_man · May 31, 17:02 · [Discussion](https://news.ycombinator.com/item?id=48347354)

**Background**: Historically, Meta's platforms have been free and revenue came from targeted advertising, raising privacy concerns. 'If you're not paying for the product, you are the product' became a common critique. Subscription models offer a direct payment path, aligning with user demands for control and privacy, as seen with other services moving to paid tiers.

**Discussion**: Community reactions are mixed. Some users welcome paying for an ad-free, friend-only feed, viewing it as a healthier alternative to dopamine-driven feeds. Others argue that simply leaving Meta platforms is better, or that a new privacy-first network could outperform. There's also concern that subscriptions might become a status signal.

**Tags**: `#Meta`, `#subscriptions`, `#social media`, `#business model`, `#privacy`

---

<a id="item-7"></a>
## [Restartable Sequences](https://justine.lol/rseq/) ⭐️ 8.0/10

A detailed article on justine.lol explains how Linux's restartable sequences (rseq) enable lock-free, atomic-free critical sections by having the kernel restart a short sequence of instructions if the thread is preempted, offering a more efficient alternative to mutexes and atomics. This technique drastically reduces synchronization overhead, allowing highly concurrent applications to scale better on multi-core systems without the complexity of traditional locking, potentially reshaping how per-CPU data is accessed in performance-critical software. Programs register a struct rseq with the kernel to define the critical region; the sequence must not make changes visible to other threads until the final instruction. The kernel restarts the sequence on preemption or signal delivery. Limitations include no nesting and no function calls that leave the region.

hackernews · grappler · May 31, 14:38 · [Discussion](https://news.ycombinator.com/item?id=48346019)

**Background**: Restartable sequences are an OS-assisted lock-free primitive. Traditional concurrency often relies on mutexes or atomic compare-and-swap, which can limit scalability. The concept of introspection windows dates back about 25 years in OS research. Linux added rseq support in kernel 4.18, enabling safe user-space access to per-CPU data structures without disabling preemption.

<details><summary>References</summary>
<ul>
<li><a href="https://justine.lol/rseq/">Restartable Sequences</a></li>
<li><a href="https://lwn.net/Articles/883104/">Restartable sequences in glibc [LWN.net]</a></li>
<li><a href="https://dynamorio.org/page_rseq.html">Restartable Sequences - DynamoRIO Restartable sequences in glibc [LWN.net] Restartable Sequences — The Linux Kernel documentation What are RSEQs (Restartable Sequences) and how to use them? What Are RSEQs (Restartable Sequences)? A Guide to Using the ... Restartable Sequences - CRIU</a></li>

</ul>
</details>

**Discussion**: Commenters generally praised the article's technical depth but some criticized its elitist opening tone. Several contributed valuable context, including a link to the librseq helper library, historical background on introspection windows, and discussion on using rseq to implement load-link/store-conditional primitives.

**Tags**: `#Linux`, `#concurrency`, `#synchronization`, `#rseq`, `#systems-programming`

---