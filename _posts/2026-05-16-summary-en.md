---
layout: default
title: "Horizon Summary: 2026-05-16 (EN)"
date: 2026-05-16
lang: en
---

> From 45 items, 17 important content pieces were selected

---

1. [vLLM v0.21.0 introduces breaking changes: transformers v5 required and C++20 compiler enforced](#item-1) ⭐️ 9.0/10
2. [LiteLLM v1.84.0 released with undocumented breaking changes](#item-2) ⭐️ 9.0/10
3. [Google Project Zero discloses 0-click exploit chain for Pixel 10](#item-3) ⭐️ 9.0/10
4. [Zulip Core Team Transfers Company to New Nonprofit Foundation](#item-4) ⭐️ 9.0/10
5. [ASCII by Jason Scott: A landmark digital preservation initiative](#item-5) ⭐️ 9.0/10
6. [IBM and Hugging Face release Granite Embedding Multilingual R2](#item-6) ⭐️ 9.0/10
7. [Calif and Mythos Preview build first public M5 kernel memory corruption exploit in 5 days](#item-7) ⭐️ 9.0/10
8. [arXiv Imposes 1-Year Submission Ban for Unchecked LLM-Generated Content](#item-8) ⭐️ 9.0/10
9. [Mitchell Hashimoto coins 'AI psychosis' to describe organizational overreliance on AI](#item-9) ⭐️ 8.0/10
10. [California bill mandates patches or refunds when online games shut down](#item-10) ⭐️ 8.0/10
11. [The Sigmoid Curve Fallacy in AI Forecasting](#item-11) ⭐️ 8.0/10
12. [npm’s supply chain vulnerabilities demand systemic fixes like release cooldowns](#item-12) ⭐️ 8.0/10
13. [ABC News removes all FiveThirtyEight articles from the web](#item-13) ⭐️ 8.0/10
14. [Waymo issues software update to 3,800 robotaxis after standing water incident](#item-14) ⭐️ 8.0/10
15. [Radicle launches sovereign, Git-native peer-to-peer code forge](#item-15) ⭐️ 8.0/10
16. [Anima: Open-source 2-billion-parameter anime-style text-to-image model](#item-16) ⭐️ 8.0/10
17. [OpenAI previews personal finance features for US ChatGPT Pro users](#item-17) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.21.0 introduces breaking changes: transformers v5 required and C++20 compiler enforced](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 9.0/10

vLLM v0.21.0, released on GitHub, formally deprecates transformers v4 support and mandates a C++20-compatible compiler for building from source; it also integrates KV offloading with the Hybrid Memory Allocator (HMA), adds thinking-budget-aware speculative decoding, and introduces the TOKENSPEED_MLA attention backend for Blackwell GPUs. These breaking changes significantly impact production deployments: users must upgrade transformers to v5 and update their build toolchain, risking CI/CD pipeline failures and requiring thorough validation; meanwhile, HMA+KV offloading and TOKENSPEED_MLA enable higher throughput and lower memory pressure for large multimodal and reasoning models on modern hardware. The C++20 requirement stems from PyTorch compatibility updates (#40380), and transformers v4 deprecation is unconditional (#40389); HMA enables per-layer memory allocation with unified page sizing, while TOKENSPEED_MLA targets DeepSeek-R1/Kimi-K25 prefill/decode on Blackwell GPUs using NVIDIA's MLA architecture.

github · khluu · May 15, 08:44

**Background**: vLLM is an open-source high-throughput LLM inference engine optimized for GPU serving. KV cache offloading moves key-value tensors from GPU VRAM to CPU RAM or disk to serve larger context windows. The Hybrid Memory Allocator (HMA) unifies memory management across different attention layer types using fixed-size blocks. TOKENSPEED_MLA is a hardware-accelerated attention backend designed for NVIDIA's Multimodal Language Architecture (MLA) on Blackwell GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/hybrid_kv_cache_manager/">Hybrid KV Cache Manager - vLLM</a></li>
<li><a href="https://blog.vllm.ai/2026/01/08/kv-offloading-connector.html">Inside vLLM’s New KV Offloading Connector: Smarter Memory Transfer for Maximizing Inference Throughput | vLLM Blog</a></li>
<li><a href="https://docs.vllm.ai/projects/production-stack/en/vllm-stack-0.1.2/tutorials/kv_cache.html">KV Cache Offloading — production-stack - vLLM</a></li>

</ul>
</details>

**Tags**: `#breaking-change`, `#deprecation`

---

<a id="item-2"></a>
## [LiteLLM v1.84.0 released with undocumented breaking changes](https://github.com/BerriAI/litellm/releases/tag/v1.84.0) ⭐️ 9.0/10

BerriAI released LiteLLM v1.84.0, explicitly warning that it contains breaking changes—but the release notes and changelog omit specific details about which APIs, interfaces, or behaviors were altered. This forces all production users to conduct thorough compatibility testing before upgrading, as silent breaking changes risk runtime failures, incorrect logging, misconfigured caching, or proxy healthcheck regressions—especially in automated CI/CD or Kubernetes deployments relying on stable interfaces. The release includes Docker image signing via cosign using a pinned, cryptographically immutable commit hash (0112e53) for verification; however, no breaking change is explicitly named in the 'What's Changed' section—only generic PR titles like 'merge main' and low-level fixes are listed.

github · github-actions[bot] · May 14, 06:12

**Background**: LiteLLM is an open-source LLM abstraction and routing layer that standardizes calls across 100+ LLM providers (e.g., OpenAI, Anthropic, Vertex AI). It is widely used in production as a lightweight proxy or SDK wrapper. Breaking changes in such a library can cascade across downstream applications, especially when they affect request/response schemas, caching logic, or proxy configuration semantics.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore/cosign: Code signing and transparency for containers and binaries · GitHub</a></li>
<li><a href="https://docs.sigstore.dev/cosign/">Cosign - Sigstore</a></li>
<li><a href="https://docs.sigstore.dev/quickstart/quickstart-cosign/">Sigstore Quickstart with Cosign - Sigstore</a></li>

</ul>
</details>

**Tags**: `#breaking-change`

---

<a id="item-3"></a>
## [Google Project Zero discloses 0-click exploit chain for Pixel 10](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero disclosed a remote, zero-click exploit chain targeting the Google Pixel 10 that achieves root access without user interaction, leveraging vulnerabilities in AI-powered message processing and Android kernel drivers; the exploit was patched by Google in under 90 days from initial vendor notification. This highlights a critical tension between AI-enhanced mobile features and security: automated, pre-opening media decoding expands the attack surface for zero-click exploits, posing serious privacy and integrity risks to billions of Android users. It also sets a rare benchmark for rapid Android driver patching, underscoring both progress and fragmentation across the broader Android ecosystem. The exploit chain involves CVE-2025-54957 (previously seen in Pixel 9 research) and a newly discovered Android kernel driver vulnerability in the VPU (Video Processing Unit) subsystem; it bypasses standard sandboxing by exploiting mediacodec context escalation and improper memory mapping in vpu_mmap().

hackernews · happyhardcore · May 15, 13:39 · [Discussion](https://news.ycombinator.com/item?id=48148460)

**Background**: Zero-click exploits require no user interaction—such as clicking a link or opening a file—and are among the most severe classes of remote attacks, often used by state-sponsored actors. Project Zero is Google’s elite security team dedicated to discovering and responsibly disclosing zero-day vulnerabilities. Modern Android devices increasingly use on-device AI models to analyze SMS, calls, and media in real time—functions that necessitate early, privileged decoding of untrusted content, thereby expanding the kernel and HAL attack surface.

<details><summary>References</summary>
<ul>
<li><a href="https://projectzero.google/2026/01/pixel-0-click-part-1.html">A 0 - click exploit chain for the Pixel 9 Part 1: Decoding... - Project Zero</a></li>
<li><a href="https://logicity.in/en/blog/google-project-zero-finds-0-click-root-exploit-in-pixel-10">Google Project Zero Finds 0 - Click Root Exploit in Pixel 10 | Logicity</a></li>
<li><a href="https://developer.android.com/privacy-and-security/risks/ai-risks/prompt-injection">Mitigate prompt injection attacks | AI Risks | Android Developers</a></li>

</ul>
</details>

**Discussion**: Commenters express concern over AI-driven expansion of zero-click surfaces, praise Google’s unusually fast <90-day driver patch but worry about the wider Android ecosystem’s slower response, and question whether rising exploit disclosures reflect genuine growth in vulnerabilities or increased media attention due to AI hype. One user also raises prompt injection and LLM safety considerations in related contexts.

**Tags**: `#mobile-security`, `#zero-click-exploit`, `#android`, `#project-zero`, `#ai-security-risk`

---

<a id="item-4"></a>
## [Zulip Core Team Transfers Company to New Nonprofit Foundation](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 9.0/10

On May 15, 2026, Zulip’s core team—including co-founder Tim Abbott—announced the donation of Zulip, Inc. to the newly established independent nonprofit Zulip Foundation, effective immediately. This transition ensures long-term public-interest stewardship of Zulip, strengthens user trust amid growing concerns about corporate data practices, and sets a precedent for sustainable governance in mission-driven open-source projects. The Zulip Foundation is legally independent, governed by a board with fiduciary duty to the public good—not shareholders—and explicitly prioritizes serving public-interest organizations and communities; the transfer includes full ownership of the Zulip trademark, codebase, and infrastructure.

hackernews · boramalper · May 15, 18:37 · [Discussion](https://news.ycombinator.com/item?id=48152168)

**Background**: Zulip is an open-source team chat platform launched in 2012 by Jeff Arnold, Waseem Daher, Jessica McKellar, and Tim Abbott. It differentiates itself from tools like Slack and Discord through threaded conversations, strong self-hosting support, and a focus on asynchronous, organized collaboration. As a 100% open-source project, it supports both cloud-hosted and fully sovereign self-hosted deployments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zulip">Zulip - Wikipedia</a></li>
<li><a href="https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/">Announcing the Zulip Foundation</a></li>
<li><a href="https://zulip.com/">Zulip is an organized team chat app for distributed teams of all sizes.</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong emotional attachment to Zulip and appreciation for the transparency and public-good framing, though some noted bittersweet feelings about the core team’s departure and questioned the Friday timing amid concurrent Bun/Rust news cycles; others emphasized how this model counters commercial drift and improves trust communication.

**Tags**: `#open-source`, `#nonprofit`, `#software-governance`, `#privacy`, `#community-driven-development`

---

<a id="item-5"></a>
## [ASCII by Jason Scott: A landmark digital preservation initiative](https://ascii.textfiles.com/) ⭐️ 9.0/10

Jason Scott’s ongoing 'ASCII' project—hosted at ascii.textfiles.com and mirrored on the Internet Archive—has preserved over 13,000 technical manuals, digitized more than 1,300 magnetic tapes, and archived early web artifacts, BBS text files, ANSI art, and audio recordings from the 1980s–1990s. This effort safeguards irreplaceable computing and subcultural history that would otherwise be lost to media decay and obsolescence, ensuring open, free, and permanent public access to foundational digital artifacts for researchers, educators, and retrocomputing enthusiasts worldwide. The project includes sub-archives like artscene.textfiles.com (ANSI/ASCII art), audio.textfiles.com (prank calls, hacker radio), and web.textfiles.com (post-1995 web artifacts); all materials are freely downloadable, with no paywalls or DRM, and much of the digitization is performed live on Twitch.

hackernews · bookofjoe · May 15, 14:02 · [Discussion](https://news.ycombinator.com/item?id=48148726)

**Background**: textfiles.com, launched by Jason Scott in 1998, is a pioneering digital archive focused on preserving ASCII-based text files from the bulletin board system (BBS) era. It collects documents ranging from computer tutorials and game walkthroughs to hacker guides and countercultural manifestos—reflecting how communities communicated and created within strict technical constraints. The site’s ethos emphasizes completeness, open access, and long-term stewardship rather than curation or gatekeeping.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Textfiles.com">Textfiles.com</a></li>
<li><a href="https://grokipedia.com/page/textfilescom">textfiles.com</a></li>
<li><a href="https://utladal.com/wiki/textfilescom">textfiles.com</a></li>

</ul>
</details>

**Discussion**: Commenters widely praise Jason Scott’s prolific output, dedication, and personal warmth—highlighting his digitization of 1,300+ tapes and 13,000 manuals over a decade, calling him 'one of the good guys' and noting his live Twitch streams. Some users also correct outdated archive links and express deep personal connections to textfiles.com as an early internet touchstone.

**Tags**: `#digital-preservation`, `#internet-archive`, `#retrocomputing`, `#open-access`, `#web-history`

---

<a id="item-6"></a>
## [IBM and Hugging Face release Granite Embedding Multilingual R2](https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2) ⭐️ 9.0/10

IBM and Hugging Face jointly released Granite Embedding Multilingual R2, an open-source Apache 2.0 licensed multilingual embedding model supporting over 100 languages, with a 32K context length and state-of-the-art retrieval quality among sub-100M parameter models. This release significantly advances open, cost-efficient, and production-ready multilingual RAG systems—enabling high-quality cross-lingual search, localization for global LLM applications, and accessible alternatives to proprietary or larger embedding models. The model comes in two variants: a 97M-parameter version (granite-embedding-97m-multilingual-r2) and a 311M-parameter version (granite-embedding-311m-multilingual-r2), the latter built on a ModernBERT-base architecture with 22 layers and 768-dimensional embeddings; both support 32K context and outperform prior open multilingual models on MRL, long-document, and conversational retrieval benchmarks.

rss · Hugging Face Blog · May 14, 18:55

**Background**: Embedding models convert text into fixed-length numerical vectors to enable semantic similarity search and retrieval—core components of RAG (Retrieval-Augmented Generation) systems. Multilingual embeddings must generalize across diverse linguistic structures and scripts while maintaining alignment across languages. Prior open multilingual models often sacrificed performance, context length, or licensing flexibility—especially under 100M parameters.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2">ibm- granite / granite - embedding -97m- multilingual - r 2 · Hugging Face</a></li>
<li><a href="https://arxiv.org/pdf/2605.13521">Granite Embedding Multilingual R 2 Models</a></li>
<li><a href="https://www.ibm.com/granite/docs/models/embedding">Granite Embedding - IBM Granite</a></li>

</ul>
</details>

**Tags**: `#embeddings`, `#multilingual`, `#RAG`, `#open-source`, `#HuggingFace`

---

<a id="item-7"></a>
## [Calif and Mythos Preview build first public M5 kernel memory corruption exploit in 5 days](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Calif, collaborating with Anthropic’s Mythos Preview AI system, developed the first publicly disclosed local kernel privilege escalation exploit chain for macOS 26.4.1 running on Apple M5 hardware between April 25 and May 1, 2026—bypassing Apple’s Memory Integrity Enforcement (MIE) hardware protection using two vulnerabilities and multiple exploitation techniques. This marks the first real-world bypass of Apple’s MIE—a five-year hardware-software security initiative designed to eliminate memory corruption attacks—and demonstrates that AI-human collaboration can rapidly overcome cutting-edge hardware-enforced memory safety, reshaping expectations for vulnerability research timelines and defense-in-depth strategies across OS vendors. The exploit is local, user-initiated via standard system calls (no physical access or special privileges required), achieves root shell from an unprivileged account, and relies on a multi-stage chain—not a single vulnerability—validated against macOS 26.4.1 on M5 silicon; a full 55-page technical report will be released after Apple patches the issue.

telegram · zaihuapd · May 15, 02:15

**Background**: Apple's Memory Integrity Enforcement (MIE) is a hardware-software co-designed security feature introduced in 2026 across iPhone 17, iPhone Air, and M5 Macs. It combines Enhanced Memory Tagging Extension (EMTE) with secure allocators like gigacaging to prevent memory corruption exploits by enforcing strict memory type separation and runtime tag validation. MIE is intended to make traditional kernel heap spraying, use-after-free, and type-confusion attacks infeasible without hardware-level compromise.

<details><summary>References</summary>
<ul>
<li><a href="https://security.apple.com/blog/memory-integrity-enforcement/">Memory Integrity Enforcement: A complete vision for memory safety in Apple devices - Apple Security Research</a></li>
<li><a href="https://innovation.consumerreports.org/apples-new-iphone-memory-protections-safeguards-devices-against-sophisticated-attacks/">Apple’s New iPhone Memory Protections Safeguard Devices Against Sophisticated Attacks - Innovation at Consumer Reports</a></li>
<li><a href="https://www.corellium.com/blog/apples-mie-framework-makes-jailbreak-testing-obsolete">End of Jailbreaks? Apple MIE on iPhone 17 Explained</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>
<li><a href="https://www.bain.com/insights/claude-mythos-and-ai-cybersecurity-wake-up-call/">Claude Mythos and the AI Cybersecurity Wake-Up Call | Bain & Company</a></li>
<li><a href="https://www.armorcode.com/blog/anthropics-claude-mythos-and-what-it-means-for-security">Anthropic’s Claude Mythos and What it Means for Security</a></li>

</ul>
</details>

**Tags**: `#macOS安全`, `#AI辅助漏洞挖掘`, `#硬件内存保护绕过`

---

<a id="item-8"></a>
## [arXiv Imposes 1-Year Submission Ban for Unchecked LLM-Generated Content](https://x.com/tdietterich/status/2055000956144935055) ⭐️ 9.0/10

arXiv has formally announced a strict enforcement policy: authors who submit papers containing incontrovertible evidence of unchecked LLM output—such as hallucinated citations, residual meta-comments, or placeholder text—will face a one-year ban from submitting to arXiv. After the ban, re-entry requires prior acceptance by a reputable peer-reviewed venue. This is arXiv’s first explicit, enforceable penalty targeting LLM misuse in scholarly communication, directly shaping how AI-assisted researchers verify outputs and uphold academic integrity—especially in fast-moving fields like AI/ML where preprints are foundational. The policy applies only when evidence of negligence is 'incontrovertible'—e.g., fabricated citations with non-existent DOIs, LLM artifacts like '[Note: This table is illustrative]', or instructions left in final text. It does not ban LLM use itself, but mandates full author responsibility for all content under arXiv's existing authorship policy.

telegram · zaihuapd · May 15, 04:30

**Background**: arXiv is a widely used open-access preprint server for physics, mathematics, computer science, and related fields, where submissions undergo moderation—not formal peer review—before posting. LLM hallucinations, especially in citations, are well-documented: studies show hallucination rates up to 94.93% across leading models, posing serious risks to scholarly accuracy. arXiv’s policy reinforces that preprint authors retain full accountability despite using AI tools.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/science/2026/05/preprint-server-arxiv-will-ban-submitters-of-ai-generated-hallucinations/">Send the arXiv AI-generated slop, get a yearlong vacation from ...</a></li>
<li><a href="https://letsdatascience.com/news/arxiv-imposes-one-year-ban-for-unchecked-llm-output-be07fdf4">arXiv imposes one-year ban for unchecked LLM output</a></li>
<li><a href="https://dev.to/olivier-coreprose/why-llms-invent-academic-citations-and-how-to-stop-ghost-references-158p">Why LLMs Invent Academic Citations —and How to... - DEV Community</a></li>

</ul>
</details>

**Tags**: `#学术规范`, `#LLM合规`, `#arXiv政策`

---

<a id="item-9"></a>
## [Mitchell Hashimoto coins 'AI psychosis' to describe organizational overreliance on AI](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

Software engineer Mitchell Hashimoto coined the term 'AI psychosis' in a May 2024 social media post to describe organizations that outsource critical thinking, reasoning, and decision-making to large language models without human oversight, understanding, or accountability. This framing elevates discourse around responsible AI adoption by highlighting a systemic risk—not of AI malfunction, but of human abdication—threatening software reliability, engineering integrity, and organizational cognition across industries. AI psychosis is not about using AI as a tool (e.g., for code generation), but about treating AI outputs as authoritative reasoning without verification, testing, or domain expertise—akin to mistaking stochastic parroting for genuine understanding.

hackernews · reasonableklout · May 15, 20:26 · [Discussion](https://news.ycombinator.com/item?id=48153379)

**Background**: 'AI psychosis' draws an analogy to clinical psychosis—where perception detaches from reality—but applies it metaphorically to organizations whose decision processes become uncoupled from empirical grounding and human judgment. It reflects growing concerns about LLM limitations, including hallucination, lack of causal reasoning, and inability to self-correct without human intervention. The term emerged amid rising adoption of LLMs in production software workflows without corresponding investment in validation infrastructure or cognitive safeguards.

**Discussion**: Commenters broadly agree that the core issue is abdication—not tool use—and draw parallels to past infrastructure failures (e.g., MTBF/MTTR trade-offs), warn of emergent instability in AI-only systems, and anticipate new consulting roles for 'AI rescue' amid growing complexity and diminishing human comprehension.

**Tags**: `#AI ethics`, `#software engineering`, `#AI adoption`, `#organizational behavior`, `#LLM limitations`

---

<a id="item-10"></a>
## [California bill mandates patches or refunds when online games shut down](https://arstechnica.com/gaming/2026/05/bill-to-keep-online-games-playable-clears-key-hurdle-in-california/) ⭐️ 8.0/10

California Assembly Bill 2428, which passed a key legislative hurdle in May 2026, would require publishers to either release client- and server-side patches enabling continued local or community-run play—or offer full refunds—when permanently shutting down online game services. This bill represents one of the first U.S. state-level legal efforts to enforce digital service continuity and consumer rights for online games, potentially setting a precedent for game preservation, platform accountability, and developer liability across the industry. The bill applies only to online-only games whose functionality depends on publisher-operated servers; it exempts subscription-only titles and does not mandate open-sourcing, though community-run servers enabled by patches are permitted. Refunds must be offered within 60 days of announced shutdown.

hackernews · Lihh27 · May 15, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48152994)

**Background**: Online games face unique preservation challenges because their functionality relies on proprietary, often undocumented server infrastructure that is rarely released to the public. U.S. copyright law—including DMCA exemptions since 2018—permits limited preservation of server-dependent games by libraries and museums, but commercial shutdowns remain largely unregulated. Consumer refund obligations for digital services are typically governed by platform policies (e.g., Steam) or regional laws (e.g., EU’s 14-day right to refund), not federal statutes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Video_game_preservation">Video game preservation - Wikipedia</a></li>
<li><a href="https://www.washingtonpost.com/video-games/2022/01/12/video-game-preservation-emulation/">Video game preservation is complicated, both legally and technically - The Washington Post</a></li>
<li><a href="https://jscholarship.library.jhu.edu/bitstreams/49d19d02-a439-4a7d-8243-a685429cbcac/download">A Practical Guide for Video Game Preservation, Exhibition, and</a></li>

</ul>
</details>

**Discussion**: Commenters express divided views: some advocate open-sourcing server code as the fairest path to sustainability, while others warn the bill could disincentivize online game development due to heightened operational and legal risk. A developer shutting down a live game notes high moderation and infrastructure costs, and several users highlight loopholes—like subscription-only exemptions—that may undermine the bill’s intent.

**Tags**: `#game-preservation`, `#consumer-rights`, `#software-policy`, `#online-games`, `#open-source`

---

<a id="item-11"></a>
## [The Sigmoid Curve Fallacy in AI Forecasting](https://www.astralcodexten.com/p/the-sigmoids-wont-save-you) ⭐️ 8.0/10

The article argues that AI progress is unlikely to follow a smooth, saturating sigmoid (S-curve) trajectory; instead, it often stalls at fundamental physical or theoretical limits before being replaced by qualitatively new paradigms—such as the historical shift from propellers to turbojets to ramjets in aviation. This challenges widely used extrapolative forecasting methods in AI policy, investment, and safety planning, highlighting that overreliance on sigmoid models risks severe underestimation of discontinuities, paradigm shifts, or hard ceilings—potentially leading to misallocated resources or unpreparedness for abrupt technological change. The article emphasizes epistemic humility: without understanding underlying constraints, forecasts are speculative. It contrasts sigmoid assumptions with Lindy’s Law—which treats technological longevity as proportional to current age—and notes that Lindy applies best to robust, non-perishable ideas, not transient engineering trends.

hackernews · Tomte · May 15, 10:51 · [Discussion](https://news.ycombinator.com/item?id=48147021)

**Background**: Sigmoid curves model growth that starts slowly, accelerates, then asymptotically saturates—commonly assumed in AI scaling arguments. Lindy’s Law, rooted in survival statistics, posits that for non-perishable entities (e.g., technologies or ideas), expected remaining lifespan is proportional to current age. The 'S-curve fallacy' refers to misapplying sigmoid logic to domains where progress is constrained by fundamental limits and disrupted by paradigm shifts rather than gradual optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lindy_effect">Lindy effect - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2206.09511">[2206.09511] The Fallacy of AI Functionality</a></li>
<li><a href="https://arxiv.org/abs/2405.00020">[2405.00020] Technosignatures longevity and Lindy's law</a></li>

</ul>
</details>

**Discussion**: Commenters engage critically with forecasting epistemology: noosphr draws a detailed historical analogy to propulsion tech; stego-tech stresses radical uncertainty and the impossibility of provable predictions; btilly offers a statistical framing of Lindy’s Law with concrete confidence intervals; and dreambuffer notes the author’s personal stake in Lindy-based AGI timelines, raising questions about motivated reasoning.

**Tags**: `#AI forecasting`, `#technological limits`, `#Lindy's Law`, `#S-curve fallacy`, `#paradigm shifts`

---

<a id="item-12"></a>
## [npm’s supply chain vulnerabilities demand systemic fixes like release cooldowns](https://kevinpatel.xyz/posts/no-way-to-prevent-this/) ⭐️ 8.0/10

A widely discussed satirical yet technically grounded blog post argues that npm’s recurring supply chain compromises—such as the March 2026 axios incident and September 2025 chalk/debug attack—are preventable only through mandatory release cooldowns, not just developer vigilance. This matters because npm hosts over two billion weekly downloads across critical packages; repeated compromises erode trust in the entire JavaScript ecosystem and expose enterprises to severe financial and operational risk—making systemic safeguards like cooldowns a DevSecOps necessity, not an optional enhancement. Release cooldowns would require newly published packages to wait N days (e.g., 24–72 hours) before becoming installable by default, giving security teams time to detect malicious artifacts; this approach is already used internally by large enterprises via Artifactory/Nexus but remains absent from npm’s public registry policy.

hackernews · alligatorplum · May 16, 00:36 · [Discussion](https://news.ycombinator.com/item?id=48155690)

**Background**: npm is the default package manager for Node.js and the world’s largest software registry, hosting over 4.8 million packages. Unlike Rust’s crates.io or Go’s module proxy—which enforce stricter publishing controls and immutability guarantees—npm allows rapid, unreviewed package publication and version re-publication, creating fertile ground for typosquatting, account takeovers, and self-replicating attacks like 'Shai-Hulud'. Recent incidents include the September 2025 compromise of chalk and debug (affecting billions of downloads) and the February 2026 'Shai-Hulud' self-replicating attack.

<details><summary>References</summary>
<ul>
<li><a href="https://www.endorlabs.com/learn/major-supply-chain-attack-compromises-popular-npm-packages-including-chalk-and-debug">Major Supply Chain Attack Compromises Popular npm Packages Including chalk and debug | Blog | Endor Labs</a></li>
<li><a href="https://checkmarx.com/zero-post/npm-hit-by-shai-hulud-the-self-replicating-supply-chain-attack/">NPM Hit By Shai-Hulud, The Self-Replicating Supply Chain Attack - Checkmarx</a></li>
<li><a href="https://www.csoonline.com/article/4053725/massive-npm-supply-chain-attack-hits-18-popular-packages-with-2b-weekly-downloads.html">Massive npm supply chain attack hits 18 popular packages with 2B weekly downloads | CSO Online</a></li>

</ul>
</details>

**Discussion**: Commenters broadly agree on the urgency of cooldowns, citing real-world adoption in enterprise tooling (Artifactory/Nexus); others debate whether npm’s attractiveness as a target—not technical design flaws—is the root cause, while some express growing distrust in third-party packages altogether and highlight persistent pain points like enforcing safe global npm configs across developer machines.

**Tags**: `#npm`, `#supply-chain-security`, `#package-managers`, `#software-ecosystems`, `#devsecops`

---

<a id="item-13"></a>
## [ABC News removes all FiveThirtyEight articles from the web](https://twitter.com/baseballot/status/2055309076209492208) ⭐️ 8.0/10

ABC News has taken down all FiveThirtyEight articles, interactive visualizations, and associated web content, effectively shuttering the site as a public-facing platform. The removal occurred without prior public announcement and includes both archived and recent reporting. FiveThirtyEight was a pioneering data journalism outlet whose open-source datasets, reproducible analyses, and award-winning visualizations served educators, journalists, data scientists, and policymakers worldwide; its disappearance represents a significant loss for digital literacy, media accountability, and long-term archival access to public-interest data storytelling. The shutdown includes removal of interactive explainers (e.g., gun deaths, p-hacking, gut microbiome), GitHub repositories, and podcast archives; Nate Silver confirmed ABC refused to sell the IP back—even at nominal cost—citing his public criticism of their management. Some repos remain accessible on GitHub but are at risk of deletion.

hackernews · cmsparks · May 15, 19:07 · [Discussion](https://news.ycombinator.com/item?id=48152553)

**Background**: FiveThirtyEight was founded by Nate Silver in 2008 as a polling and statistics blog, gained prominence during the 2008 and 2012 U.S. presidential elections, and was acquired by ESPN in 2013 and later by ABC News (Disney) in 2018. It became known for transparent methodology, open-source code sharing, and innovative data visualizations that made complex statistical concepts accessible to broad audiences.

<details><summary>References</summary>
<ul>
<li><a href="https://www.libhunt.com/topic/fivethirtyeight">fivethirtyeight Open - Source Projects</a></li>
<li><a href="https://gitplanet.com/label/fivethirtyeight">Top fivethirtyeight open source projects - GitPlanet</a></li>
<li><a href="https://www.academia.edu/40540414/Visualization_and_interactivity_in_data_journalism_projects">(PDF) Visualization and interactivity in data journalism projects</a></li>

</ul>
</details>

**Discussion**: Commenters express dismay over lost educational resources and digital preservation risks, praise FiveThirtyEight’s technical excellence and pedagogical value, and criticize ABC’s strategic short-sightedness—particularly its failure to sustain the brand beyond election cycles despite strong niche appeal among data-literate professionals.

**Tags**: `#data-journalism`, `#digital-preservation`, `#media-studies`, `#data-visualization`, `#corporate-strategy`

---

<a id="item-14"></a>
## [Waymo issues software update to 3,800 robotaxis after standing water incident](https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html) ⭐️ 8.0/10

Waymo deployed a targeted software update to its fleet of 3,800 autonomous vehicles after a perception glitch caused some to drive into standing water—a rare but safety-critical edge case. The update was rolled out remotely and did not require physical recalls or vehicle downtime. This incident highlights a persistent challenge in autonomous driving: robust detection of hydrological hazards like shallow vs. deep standing water, which sits at the intersection of sensor fusion, computer vision, and real-world safety assurance. It underscores how over-the-air updates enable rapid, fleet-wide safety improvements—accelerating the path toward safer-than-human autonomy. The issue involved misclassification of wet pavement versus hazardous standing water—not sensor failure per se, but a limitation in perception inference under ambiguous visual conditions. Waymo’s system uses lidar and camera data, but current models lacked sufficient training on subtle hydrological cues such as surface reflectivity, texture continuity, and depth-dependent motion response.

hackernews · drob518 · May 15, 18:00 · [Discussion](https://news.ycombinator.com/item?id=48151767)

**Background**: Standing water detection is a known edge case in autonomous driving—classified as part of the 'long tail' of rare but high-consequence scenarios. Unlike humans who use contextual cues (e.g., preceding vehicles’ behavior, road grade, weather history), AVs rely on real-time sensor fusion and machine learning models trained on limited hydrological diversity. Waymo’s perception stack includes mid-range lidar and multi-camera inputs, but detecting water depth without dedicated hardware remains an open research challenge.

<details><summary>References</summary>
<ul>
<li><a href="https://waymo.com/open/about/">About – Waymo Open Dataset</a></li>
<li><a href="https://www.kognic.com/articles/edge-cases-autonomous-driving">Edge Cases in Autonomous Driving: Detection and Handling Guide</a></li>
<li><a href="https://rodneybrooks.com/edge-cases-for-self-driving-cars/">Edge Cases For Self Driving Cars – Rodney Brooks</a></li>

</ul>
</details>

**Discussion**: Commenters debated sensor-based versus inference-based solutions: one DARPA Grand Challenge veteran advocated for physical water sensors, while others emphasized scalable inference using fleet-wide map data and motion analysis. Several noted that this incident exemplifies the iterative, data-driven safety improvement cycle unique to autonomous systems.

**Tags**: `#autonomous-vehicles`, `#computer-vision`, `#safety-critical-systems`, `#edge-cases`, `#robotics`

---

<a id="item-15"></a>
## [Radicle launches sovereign, Git-native peer-to-peer code forge](https://radicle.dev/) ⭐️ 8.0/10

Radicle has released a new version of its decentralized code collaboration stack, establishing a sovereign, peer-to-peer code forge built on Git that supports cryptographic identities, private repositories, and local-first workflows. This represents a meaningful alternative to centralized forges like GitHub, advancing censorship-resistant infrastructure for open source development and enabling new paradigms such as agentic workflows with cryptographically signed artifacts. Radicle nodes run locally on personal computers, synchronize repositories via a custom gossip protocol for metadata discovery and Git’s native protocol for data replication, and use public-key cryptography for identity and access control; private repositories hide new updates but retain public history by default.

hackernews · KolmogorovComp · May 15, 12:07 · [Discussion](https://news.ycombinator.com/item?id=48147603)

**Background**: A 'code forge' is a platform for collaborative software development—like GitHub or GitLab—that hosts repositories, manages pull requests (called 'patches' in Radicle), issues, and code reviews. Radicle replaces centralized servers with a peer-to-peer network where users run their own nodes, using Git as the underlying data format and cryptographic keys instead of usernames/passwords for identity. This design prioritizes user sovereignty, offline capability, and resistance to platform lock-in or takedowns.

<details><summary>References</summary>
<ul>
<li><a href="https://radicle.dev/guides/protocol">Radicle Protocol Guide</a></li>
<li><a href="https://docs.radicle.xyz/guides/protocol">Radicle Protocol Guide</a></li>
<li><a href="https://radicle.dev/">Radicle: the sovereign forge</a></li>

</ul>
</details>

**Discussion**: Developers praise Radicle's local-first architecture and agentic workflow support, but raise concerns about its licensing (non-AGPL, enabling SaaS reuse), repository deletion limitations, and privacy model evolution; some note related tools like Epiq, a distributed Git-based issue tracker.

**Tags**: `#distributed systems`, `#git`, `#decentralized infrastructure`, `#open source`, `#developer tools`

---

<a id="item-16"></a>
## [Anima: Open-source 2-billion-parameter anime-style text-to-image model](https://civitai.com/models/2458426/anima) ⭐️ 8.0/10

CircleStone Labs and Comfy Org jointly released Anima, a 2-billion-parameter open-weight text-to-image diffusion model trained exclusively on real-world anime and non-realistic art images (no synthetic data), available on Civitai and Hugging Face as of March 2026. Anima is one of the few high-parameter, fully open, and anime-specialized text-to-image models trained only on authentic human-created art—making it a valuable benchmark for stylized generation, LoRA fine-tuning, and commercial-adjacent creative workflows in the anime/AI-art community. The model supports native integration with ComfyUI and can be fine-tuned using sd-scripts with LoRA or full-parameter training; it uses a diffusion-single-file architecture and is licensed for non-commercial use only.

telegram · zaihuapd · May 15, 03:00

**Background**: Text-to-image diffusion models like Stable Diffusion rely on large-scale image-text datasets to learn visual concepts. While many general-purpose models (e.g., SDXL) include anime content, they are not optimized for it and often mix synthetic or low-quality data. Specialized models like Anima fill a gap by focusing exclusively on curated, high-fidelity anime and artistic styles without data augmentation or synthetic generation.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/circlestone-labs/Anima">circlestone-labs/Anima · Hugging Face</a></li>
<li><a href="https://huggingface.co/circlestone-labs/Anima/discussions/35">circlestone-labs/Anima · The training script for the Anima model has already been implemented for sd-scripts</a></li>
<li><a href="https://huggingface.co/circlestone-labs/Anima/blob/main/README.md">README.md · circlestone-labs/Anima at main</a></li>

</ul>
</details>

**Tags**: `#文生图`, `#动漫生成`, `#开源模型`

---

<a id="item-17"></a>
## [OpenAI previews personal finance features for US ChatGPT Pro users](https://openai.com/index/personal-finance-chatgpt/) ⭐️ 8.0/10

OpenAI launched a preview of personal finance capabilities for US-based ChatGPT Pro users on April 23, 2026, enabling Plaid-powered financial account linking, real-time dashboards (assets, spending, subscriptions, pending payments), and context-aware Q&A—powered by the newly named GPT-5.5 Thinking model. This marks OpenAI’s first production-grade integration of live financial data into ChatGPT, establishing a new benchmark for secure, compliant AI Agent design in regulated domains—and signals a strategic shift toward reasoning-heavy, context-aware models (GPT-5.5 Thinking) for sensitive vertical applications. Data access is strictly read-only via Plaid; synced financial data is automatically deleted from OpenAI systems within 30 days after disconnection; Intuit integration is forthcoming; GPT-5.5 Thinking is currently exclusive to Pro users and not available via API at launch.

telegram · zaihuapd · May 15, 16:50

**Background**: Plaid is a leading financial data network that enables secure, standardized access to bank transaction and account data across thousands of US financial institutions. GPT-5.5 Thinking is a newly released OpenAI model variant optimized for step-by-step reasoning and contextual analysis, distinct from faster 'instant' variants. This preview represents OpenAI’s first public deployment of a dedicated reasoning model in a real-world, regulated application domain.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Plaid_Inc.">Plaid Inc. - Wikipedia</a></li>
<li><a href="https://plaid.com/products/transactions/">Transactions API - Bank account history & credit card data | Plaid</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#金融API集成`, `#GPT-5.5`

---