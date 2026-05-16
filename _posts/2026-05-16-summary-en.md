---
layout: default
title: "Horizon Summary: 2026-05-16 (EN)"
date: 2026-05-16
lang: en
---

> From 44 items, 16 important content pieces were selected

---

1. [vLLM v0.21.0 introduces breaking changes: transformers v4 deprecation and C++20 build requirement](#item-1) ⭐️ 9.0/10
2. [LiteLLM v1.84.0 released with breaking changes and signed Docker images](#item-2) ⭐️ 9.0/10
3. [Project Zero discloses 0-click exploit chain for Google Pixel 10](#item-3) ⭐️ 9.0/10
4. [O(x)Caml deployed in real satellite software with zero-GC performance](#item-4) ⭐️ 9.0/10
5. [IBM and Hugging Face release Granite Embedding Multilingual R2](#item-5) ⭐️ 9.0/10
6. [First public Apple M5 kernel exploit bypasses MIE using AI-human collaboration](#item-6) ⭐️ 9.0/10
7. [arXiv Imposes 1-Year Submission Ban for Unverified LLM-Generated Content](#item-7) ⭐️ 9.0/10
8. [Mitchell Hashimoto coins 'AI psychosis' to describe corporate overreliance on LLMs](#item-8) ⭐️ 8.0/10
9. [Zulip Foundation Launched to Ensure Public-Good Stewardship](#item-9) ⭐️ 8.0/10
10. [U.S. DOJ subpoenas Apple and Google to identify 100,000+ users of EZ Lynk car-tinkering app](#item-10) ⭐️ 8.0/10
11. [ABC News removes all FiveThirtyEight articles from the web](#item-11) ⭐️ 8.0/10
12. [Waymo issues OTA update to 3,800 robotaxis after water-depth misperception](#item-12) ⭐️ 8.0/10
13. [New IEEE Spectrum article examines Steve Jobs’s NeXT era and its impact on Apple](#item-13) ⭐️ 8.0/10
14. [Anima: Open-source 2B-parameter anime-style text-to-image model](#item-14) ⭐️ 8.0/10
15. [Surge Declines VLESS/XLS Support Due to Non-Standard TLS Design](#item-15) ⭐️ 8.0/10
16. [OpenAI previews personal finance feature for US ChatGPT Pro users](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [vLLM v0.21.0 introduces breaking changes: transformers v4 deprecation and C++20 build requirement](https://github.com/vllm-project/vllm/releases/tag/v0.21.0) ⭐️ 9.0/10

vLLM v0.21.0 formally deprecates support for Hugging Face transformers v4 and mandates a C++20-compatible compiler for building from source, effective immediately. It also integrates KV offloading with the Hybrid Memory Allocator (HMA), adds thinking-budget-aware speculative decoding, and introduces the TOKENSPEED_MLA attention backend for Blackwell GPUs. These breaking changes significantly impact production deployments: users must upgrade transformers to v5 and modernize their build toolchains, or risk compilation failure and runtime incompatibility. The HMA+KV offloading integration and Blackwell-optimized backends enable higher throughput and lower memory footprint for large-scale LLM serving on modern hardware. The C++20 requirement breaks compatibility with older GCC/Clang versions (e.g., GCC < 11, Clang < 14); transformers v4 users must migrate before upgrading vLLM. HMA enables per-layer memory allocation with unified page sizing, and TOKENSPEED_MLA is currently exclusive to DeepSeek-R1/Kimi-K25 on NVIDIA Blackwell GPUs.

github · khluu · May 15, 08:44

**Background**: vLLM is a high-throughput, open-source LLM inference engine known for PagedAttention and efficient memory management. Transformers is Hugging Face's foundational library for pretrained language models; v5 introduced major API and serialization changes. C++20 brings critical features like concepts and ranges that PyTorch and vLLM now rely on for type safety and performance. KV offloading moves key-value caches to CPU or NVMe to extend context length, while HMA unifies memory allocation across heterogeneous attention layers.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/hybrid_kv_cache_manager/">Hybrid KV Cache Manager - vLLM</a></li>
<li><a href="https://vllm-website-pzi7pzblm-inferact-inc.vercel.app/blog/kv-offloading-connector">Inside vLLM ’s New KV Offloading Connector: Smarter Memory...</a></li>
<li><a href="https://github.com/vllm-project/vllm/issues/11382">[RFC]: Hybrid Memory Allocator · Issue #11382 · vllm-project/vllm</a></li>

</ul>
</details>

**Tags**: `#breaking-change`, `#deprecation`

---

<a id="item-2"></a>
## [LiteLLM v1.84.0 released with breaking changes and signed Docker images](https://github.com/BerriAI/litellm/releases/tag/v1.84.0) ⭐️ 9.0/10

BerriAI released LiteLLM v1.84.0, a major version containing breaking changes requiring full compatibility testing before upgrade; all associated Docker images are cryptographically signed using Cosign and the Sigstore ecosystem. This release strengthens supply-chain security via mandatory image signing and introduces critical proxy, caching, and logging improvements—but breaking changes risk runtime failures for existing deployments if not rigorously tested. The release uses a pinned, immutable commit hash (0112e53) to fetch the Cosign public key—recommended for strongest verification—and includes fixes for Vertex AI, Redis caching, streaming cost logging, and GPT-5.5 Pro pricing, alongside new proxy healthcheck timeout and session cleanup features.

github · github-actions[bot] · May 14, 06:12

**Background**: LiteLLM is an open-source LLM abstraction and routing library that standardizes API calls across 100+ LLM providers. Cosign is a Sigstore project tool for signing and verifying software artifacts—including container images—using public-good infrastructure like Fulcio and Rekor. Docker image signing helps prevent supply-chain attacks by cryptographically proving image origin and integrity.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.sigstore.dev/quickstart/quickstart-cosign/">Sigstore Quickstart with Cosign - Sigstore</a></li>
<li><a href="https://github.com/sigstore/cosign">GitHub - sigstore / cosign : Code signing and transparency for...</a></li>
<li><a href="https://www.wiz.io/academy/container-security/container-image-signing">What Is Container Image Signing? | Wiz - Cool</a></li>

</ul>
</details>

**Tags**: `#breaking-change`

---

<a id="item-3"></a>
## [Project Zero discloses 0-click exploit chain for Google Pixel 10](https://projectzero.google/2026/05/pixel-10-exploit.html) ⭐️ 9.0/10

Google Project Zero disclosed a novel 0-click exploit chain targeting the newly released Pixel 10, beginning with CVE-2025-54957 — a critical flaw in the Dolby Unified Decoder (UDC) previously exploited against Pixel 9 — and achieving full root compromise without user interaction. This highlights how AI-powered message processing features—requiring real-time media decoding before user consent—significantly expand the 0-click attack surface on modern Android devices, raising urgent concerns about privacy-by-design tradeoffs and ecosystem-wide security fragmentation. The exploit chain leverages a driver-level vulnerability in the UDC component and bypasses multiple Android sandboxing layers; Google patched it within 90 days of disclosure—a notably fast response compared to historical Android vendor timelines.

hackernews · happyhardcore · May 15, 13:39 · [Discussion](https://news.ycombinator.com/item?id=48148460)

**Background**: Zero-click exploits require no user interaction—such as opening a message or clicking a link—and typically target always-on services like messaging or media decoders. The Pixel 10 includes new on-device AI features that automatically analyze SMS/MMS attachments (e.g., images, audio) using real-time decoding, increasing exposure to such vulnerabilities. This follows Project Zero’s earlier 0-click work on Pixel 9, which revealed similar risks from the same Dolby UDC component.

<details><summary>References</summary>
<ul>
<li><a href="https://projectzero.google/2026/05/pixel-10-exploit.html">A 0-click exploit chain for the Pixel 10: When a Door Closes, a Window Opens - Project Zero</a></li>
<li><a href="https://cyberpress.org/zero-click-exploit-chain-for-pixel-10/">Google Project Zero Reveals Zero-Click Exploit Chain for Pixel 10</a></li>
<li><a href="https://developer.android.com/privacy-and-security/risks/ai-risks/prompt-injection">Mitigate prompt injection attacks | AI Risks | Android Developers</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern over AI-driven automatic message analysis eroding user consent, praised Google’s unusually fast 90-day patch timeline but worried about broader Android fragmentation, questioned whether exploit reporting frequency reflects actual risk increase or just heightened AI-related media attention, and noted the apparent scarcity of recent iOS jailbreaks compared to Android exploits.

**Tags**: `#android-security`, `#zero-click-exploit`, `#project-zero`, `#mobile-security`, `#ai-security-risk`

---

<a id="item-4"></a>
## [O(x)Caml deployed in real satellite software with zero-GC performance](https://gazagnaire.org/blog/2026-05-14-borealis.html) ⭐️ 9.0/10

O(x)Caml — an extension of OCaml supporting compile-time stack allocation via exclave_ and stack_ annotations — has been deployed in the GHGSat-D satellite’s payload software since at least 2016, reducing p99.9 per-packet dispatch latency from 29 ns to 9 ns and eliminating all 394 minor GCs over 25 million packets on the CCSDS hot path. This marks one of the first verified deployments of a functional, garbage-collected language in space-grade embedded systems, demonstrating that memory-safe high-level languages can meet hard real-time and reliability constraints — potentially reshaping safety-critical systems engineering across aerospace, defense, and autonomous infrastructure. Stack allocation in O(x)Caml is enforced via locality annotations (e.g., @local, exclave_, stack_), and the compiler rejects escaping allocations instead of falling back to heap — ensuring deterministic memory behavior; this differs from standard OCaml, where such annotations are optional and heap fallback remains default.

hackernews · yminsky · May 15, 10:55 · [Discussion](https://news.ycombinator.com/item?id=48147058)

**Background**: OCaml is a statically typed, functional-first language known for strong type safety and predictable performance, but its garbage collector poses challenges for real-time and space-constrained systems. O(x)Caml extends OCaml with explicit memory locality control, enabling developers to annotate values as stack-allocated and have the compiler enforce that constraint — turning GC pressure into a compile-time error rather than a runtime risk. CCSDS (Consultative Committee for Space Data Links) is the international standard suite for space communications, specifying packet formats, telemetry, and encryption guidelines used by most operational satellites.

<details><summary>References</summary>
<ul>
<li><a href="https://oxcaml.org/documentation/stack-allocation/intro/">OxCaml | Stack allocation | Intro</a></li>
<li><a href="https://oxcaml.org/documentation/stack-allocation/reference/">OxCaml | Stack allocation | Reference</a></li>
<li><a href="https://gazagnaire.org/blog/2026-05-14-borealis.html">Thomas Gazagnaire :: O(x)Caml in Space</a></li>
<li><a href="https://www.eoportal.org/satellite-missions/ghgsat-d">GHGSat-D (Greenhouse Gas Satellite - Demonstrator) / Claire - eoPortal</a></li>

</ul>
</details>

**Discussion**: Experts debated tradeoffs between CCSDS-compliant custom stacks versus battle-tested protocols like TLS for satellite encryption; practitioners shared firsthand experience deploying OCaml on GHGSat-D; and system architects questioned how far GC-based languages can be bent toward deterministic behavior without sacrificing ergonomics or safety.

**Tags**: `#OCaml`, `#systems-programming`, `#space-software`, `#memory-safety`, `#real-time-systems`

---

<a id="item-5"></a>
## [IBM and Hugging Face release Granite Embedding Multilingual R2](https://huggingface.co/blog/ibm-granite/granite-embedding-multilingual-r2) ⭐️ 9.0/10

IBM and Hugging Face jointly released Granite Embedding Multilingual R2, an open-source Apache 2.0 licensed embedding model supporting over 100 languages, with a 32K context length and 97M parameters, achieving state-of-the-art retrieval quality among sub-100M models. This release significantly advances open, production-ready RAG systems by providing a high-quality, multilingual, long-context embedding model that lowers barriers to localized, cost-efficient, and enterprise-safe AI deployment. The model is built on a ModernBERT-base architecture (22 layers, 768-dim vectors, GeLU activation), and its 32K context support is achieved without additional training—leveraging recent techniques like positional interpolation or RoPE extension as implied by LongEmbed research.

rss · Hugging Face Blog · May 14, 18:55

**Background**: Text embedding models convert input text into fixed-length numerical vectors, enabling semantic search, retrieval, and similarity comparison. In Retrieval-Augmented Generation (RAG), embedding quality directly determines whether the LLM retrieves relevant, grounded context—or hallucinates. Long-context embeddings (e.g., 32K) are critical for processing documents, code files, or multi-turn conversations without truncation.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2">ibm- granite / granite - embedding -97m- multilingual - r 2 · Hugging Face</a></li>
<li><a href="https://arxiv.org/pdf/2605.13521">Granite Embedding Multilingual R 2 Models</a></li>
<li><a href="https://arxiv.org/html/2404.12096v1">LongEmbed: Extending Embedding Models for Long Context Retrieval</a></li>

</ul>
</details>

**Tags**: `#embeddings`, `#multilingual`, `#RAG`, `#open-source`, `#HuggingFace`

---

<a id="item-6"></a>
## [First public Apple M5 kernel exploit bypasses MIE using AI-human collaboration](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

Calif and Anthropic's Mythos Preview AI co-developed the first publicly disclosed local kernel memory corruption exploit for Apple M5 macOS 26.4.1 within five days (April 25–May 1, 2026), achieving root privilege escalation while fully bypassing Memory Integrity Enforcement (MIE). This demonstrates that even Apple’s most advanced hardware-enforced memory safety mechanism—designed over five years and touted as 'unparalleled'—can be defeated rapidly via AI-augmented reverse engineering, signaling a paradigm shift in offensive security and urgent implications for OS kernel hardening and AI security governance. The exploit chain targets a data-type vulnerability (not control-flow), requires only unprivileged system calls, and bypasses MIE by leveraging ARM's Enhanced Memory Tagging Extension (EMTE) in synchronous mode — though full technical details remain embargoed until Apple patches the issue.

telegram · zaihuapd · May 15, 02:15

**Background**: Apple introduced Memory Integrity Enforcement (MIE) with the M5 chip as its flagship hardware-software memory safety feature, built on ARM's Enhanced Memory Tagging Extension (EMTE) to prevent buffer overflows and use-after-free vulnerabilities. MIE is enabled by default on M5 Macs and A19 iPhones, representing Apple's strongest defense against kernel memory corruption exploits to date. It operates at the hardware level with synchronous tag checking, making traditional exploitation techniques significantly harder.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_M5">Apple M5 - Wikipedia</a></li>
<li><a href="https://www.computerworld.com/article/4124435/apple-touts-unparalleled-protection-for-m5-macs.html">Apple touts ‘unparalleled’ protection for M5 Macs</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>
<li><a href="https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities">Our evaluation of Claude Mythos Preview’s cyber capabilities | AISI Work</a></li>

</ul>
</details>

**Tags**: `#macOS安全`, `#内核漏洞利用`, `#AI辅助安全研究`

---

<a id="item-7"></a>
## [arXiv Imposes 1-Year Submission Ban for Unverified LLM-Generated Content](https://x.com/tdietterich/status/2055000956144935055) ⭐️ 9.0/10

arXiv announced a formal policy effective immediately: authors who submit papers containing unverified LLM-generated content—such as hallucinated citations, meta-comments (e.g., 'replace with real data'), or placeholder text—will face a 1-year ban from submitting to arXiv. After the ban, they must first have a paper accepted by a reputable peer-reviewed venue before being allowed to submit to arXiv again. This is arXiv’s first explicit, enforceable penalty targeting misuse of LLMs in scholarly communication, signaling a major shift toward accountability in AI-augmented research. It directly affects thousands of AI/ML researchers and engineers who rely on LLMs for drafting, citation generation, or figure/table creation—and compels adoption of rigorous human-in-the-loop verification workflows. The policy applies only when evidence shows the author failed to verify LLM output—e.g., verbatim LLM artifacts like 'This table is illustrative only' or fabricated DOIs. It reinforces arXiv’s long-standing principle that authorship implies full responsibility for all content, regardless of origin. The ban is per author, not per submission, and applies retroactively to violations detected during moderation.

telegram · zaihuapd · May 15, 04:30

**Background**: arXiv is a preprint server widely used in physics, mathematics, computer science, and related fields, operating on a moderation-based model rather than full peer review. Large language models (LLMs) are increasingly used for academic writing assistance but suffer from 'hallucinations'—fabricated facts, citations, or data—posing serious integrity risks. Several high-profile cases, such as the 2023 Mata v. Avianca lawsuit, have demonstrated real-world consequences of uncritically using LLM outputs in formal documents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2605.07723">LLM hallucinations in the wild</a></li>
<li><a href="https://www.lakera.ai/blog/guide-to-hallucinations-in-large-language-models">LLM Hallucinations in 2026: How to Understand and Tackle AI’s Most...</a></li>

</ul>
</details>

**Tags**: `#学术规范`, `#LLM伦理`, `#arXiv政策`

---

<a id="item-8"></a>
## [Mitchell Hashimoto coins 'AI psychosis' to describe corporate overreliance on LLMs](https://twitter.com/mitchellh/status/2055380239711457578) ⭐️ 8.0/10

Mitchell Hashimoto, creator of Vagrant and Terraform, coined the term 'AI psychosis' in a May 2024 social media post to describe companies that uncritically outsource reasoning, decision-making, and software development to AI without human oversight or domain understanding. This critique highlights a growing risk in the AI adoption wave: erosion of engineering rigor, accountability, and cognitive capacity within organizations, with implications for software reliability, security, and long-term technical debt. The term specifically targets abdication of judgment—not tool use—e.g., treating LLM outputs as authoritative reasoning rather than assistive drafts; it reflects concerns about 'vibe-coded' PRs, unreviewed AI-generated infrastructure changes, and production outages caused by unchecked AI suggestions.

hackernews · reasonableklout · May 15, 20:26 · [Discussion](https://news.ycombinator.com/item?id=48153379)

**Background**: 'AI psychosis' is a metaphorical, non-clinical term—not a medical diagnosis—but draws attention to pathological organizational behavior emerging from excessive trust in LLMs. It builds on longstanding software engineering principles like 'blameless postmortems', 'human-in-the-loop' design, and the 'principle of least authority'. The concept resonates amid rising adoption of LLMs in coding (e.g., GitHub Copilot), DevOps automation, and executive decision support tools.

**Discussion**: Commenters distinguish between responsible AI tooling and dangerous abdication of judgment, with some predicting an emerging 'AI rescue consulting' niche for stabilizing AI-overloaded systems; others cite observable declines in software quality and real-world outages tied to unvetted AI outputs.

**Tags**: `#AI ethics`, `#software engineering`, `#organizational behavior`, `#LLM adoption`, `#AI risk`

---

<a id="item-9"></a>
## [Zulip Foundation Launched to Ensure Public-Good Stewardship](https://blog.zulip.com/2026/05/15/announcing-zulip-foundation/) ⭐️ 8.0/10

On May 15, 2026, Zulip’s core team at Kandra Labs announced the donation of the Zulip company and intellectual property to a newly established independent nonprofit, the Zulip Foundation, to ensure long-term stewardship aligned with public interest and user trust. This governance shift strengthens trust in Zulip as an open-source messaging platform amid growing industry concerns about corporate monetization, data exploitation, and erosion of OSS values—placing it alongside Mozilla, Signal, and Wikipedia in mission-driven stewardship. The foundation adopts a governance model similar to Mozilla and Wikipedia, enabling charitable fundraising and formalizing commitments to privacy and independence; 12 remaining Kandra Labs engineers continue development under the foundation’s stewardship, and an interim president has been appointed.

hackernews · boramalper · May 15, 18:37 · [Discussion](https://news.ycombinator.com/item?id=48152168)

**Background**: Zulip is a widely respected open-source team chat platform known for its threaded message model, strong moderation tools, and emphasis on accessibility and information discoverability. It has long served academic, open-source, and public-interest communities—including Lean theorem prover and NixOS—where structured, searchable communication is critical. Until 2026, it was developed and maintained by Kandra Labs, a for-profit entity founded by Tim Abbott.

<details><summary>References</summary>
<ul>
<li><a href="https://app.daily.dev/posts/announcing-the-zulip-foundation-jbrmj2rls">Announcing the Zulip Foundation | daily.dev</a></li>
<li><a href="https://conzit.com/post/zulip-foundation-launches-as-kandra-labs-transitions-leadership">Zulip Foundation Launches as Kandra Labs Transitions Leaders</a></li>
<li><a href="https://discourse.nixos.org/t/zulip-for-governance-discussions/44684">Zulip for governance discussions - NixOS Discourse</a></li>

</ul>
</details>

**Discussion**: Commenters express deep personal and professional attachment to Zulip, praising the foundation as a trust-preserving response to corporate OSS risks—but also voice nuanced concerns about leadership transition optics, timing (Friday announcement), and comparisons to recent controversial acquisitions like Bun/Rust. Some highlight Zulip’s unique utility for serious technical discourse and community governance.

**Tags**: `#open-source`, `#nonprofit`, `#software-governance`, `#messaging-platform`, `#community-trust`

---

<a id="item-10"></a>
## [U.S. DOJ subpoenas Apple and Google to identify 100,000+ users of EZ Lynk car-tinkering app](https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/) ⭐️ 8.0/10

The U.S. Department of Justice has issued subpoenas to Apple and Google demanding they identify over 100,000 users of the EZ Lynk Auto Agent app, which pairs with an OBD dongle to modify diesel vehicle emissions control software. This sets a major legal precedent for government access to platform-held user data in regulatory enforcement—especially where apps enable technically sophisticated but legally contested modifications—and raises urgent questions about privacy, platform liability, and mission creep in surveillance authority. The subpoena targets users of EZ Lynk—a tool previously sued by the DOJ in 2021 for selling 'defeat devices' violating the Clean Air Act—and relies on a Doe subpoena mechanism to unmask anonymous users; Apple and Google are not accused of wrongdoing but are compelled as third-party custodians of account data.

hackernews · tencentshill · May 15, 17:28 · [Discussion](https://news.ycombinator.com/item?id=48151383)

**Background**: EZ Lynk Auto Agent is a car-tinkering app that works with an OBD-II hardware dongle to reprogram engine control units (ECUs), primarily on diesel trucks, allowing users to disable or alter factory emissions controls. The U.S. Environmental Protection Agency and DOJ classify such tools as illegal 'defeat devices' under the Clean Air Act if their primary purpose is circumventing emissions standards. Apple and Google host the app on their respective app stores, though it has since been removed from both platforms following regulatory pressure.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/05/15/doj-reportedly-demands-apple-and-google-identify-over-100000-users-of-car-app/">DOJ reportedly demands Apple and Google identify over 100,000 ... - 9to5Mac</a></li>
<li><a href="https://macdailynews.com/2026/05/15/u-s-doj-demands-apple-and-google-unmask-over-100000-users-of-popular-car-tinkering-app-in-emissions-crackdown/">U.S. DOJ demands Apple and Google unmask over 100,000 users of popular ...</a></li>
<li><a href="https://www.forbes.com/sites/thomasbrewster/2026/05/14/government-demands-apple-and-google-identify-over-100000-users-of-car-app/">The DOJ Is Demanding Apple And Google Identify Over 100,000 ... - Forbes</a></li>

</ul>
</details>

**Discussion**: Commenters express divergent views: some support enforcement against emissions tampering, others warn of slippery-slope surveillance expanding to legitimate modifications like disabling GPS tracking, and several highlight risks of centralized app distribution and advocate for decentralized alternatives like F-Droid.

**Tags**: `#privacy`, `#surveillance`, `#automotive-software`, `#platform-governance`, `#environmental-regulation`

---

<a id="item-11"></a>
## [ABC News removes all FiveThirtyEight articles from the web](https://twitter.com/baseballot/status/2055309076209492208) ⭐️ 8.0/10

ABC News has taken down all FiveThirtyEight articles and removed them from its website, effectively shuttering the data journalism site as a public-facing resource. The removal occurred without prior public announcement and includes all archived articles, interactives, and visualizations. FiveThirtyEight was a pioneering, widely cited data journalism outlet whose analyses shaped public understanding of elections, sports, economics, and science; its abrupt disappearance represents a significant loss for media literacy, digital scholarship, and open access to methodologically transparent journalism. As of June 13, 2023, FiveThirtyEight had already ceased updating sports predictions and forecasts; GitHub repositories containing its data and code remain publicly accessible but are no longer maintained. Nate Silver confirmed ABC refused to sell the IP, citing personal criticism as a reason.

hackernews · cmsparks · May 15, 19:07 · [Discussion](https://news.ycombinator.com/item?id=48152553)

**Background**: FiveThirtyEight was founded by Nate Silver in 2008 as an independent blog focused on statistical analysis of politics and elections, later acquired by ESPN in 2013 and then by ABC News (Disney) in 2018. It became renowned for transparent methodology, interactive data visualizations, and rigorous polling aggregation — setting standards for modern data journalism.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/fivethirtyeight/data">GitHub - fivethirtyeight / data : Data and code behind the articles and...</a></li>
<li><a href="https://www.archives.gov/preservation/digital-preservation">Digital Preservation - Home | National Archives</a></li>
<li><a href="https://www.newspapers.org/stories/protecting-the-record-tips-from-journalists-librarians-on-digital-preservation-in-evolving-tech,4164047">Tips from journalists, librarians on digital preservation in evolving ...</a></li>

</ul>
</details>

**Discussion**: Commenters express dismay over lost visualizations and educational resources, urge archiving GitHub repos, and criticize ABC’s decision as short-sighted brand mismanagement; some note FiveThirtyEight’s declining profitability outside election years, while others highlight its irreplaceable role for wonky professionals and educators.

**Tags**: `#data-journalism`, `#media-ethics`, `#digital-preservation`, `#data-visualization`, `#corporate-media`

---

<a id="item-12"></a>
## [Waymo issues OTA update to 3,800 robotaxis after water-depth misperception](https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html) ⭐️ 8.0/10

Waymo deployed an over-the-air software update to approximately 3,800 of its autonomous vehicles after a perception flaw caused some to drive into standing water, mistaking shallow puddles for safe road surfaces. This incident underscores a critical real-world limitation in autonomous vehicle perception: reliably estimating water depth using vision alone. It highlights both the safety-critical nature of perception robustness and the growing reliance on OTA updates to rapidly correct field-observed flaws across large fleets. The issue was not hardware failure but a software-level misclassification in computer vision — specifically, insufficient differentiation between wet pavement and hazardous deep water. No physical recalls or vehicle immobilizations occurred; the fix was delivered remotely via OTA without requiring service visits.

hackernews · drob518 · May 15, 18:00 · [Discussion](https://news.ycombinator.com/item?id=48151767)

**Background**: Autonomous vehicles rely heavily on visual perception systems — often deep learning-based — to detect and classify objects, road conditions, and hazards in real time. Robust perception under adverse conditions (e.g., rain, glare, reflective surfaces) remains an open challenge, as these systems can struggle with ambiguous visual cues like standing water. Perception robustness is widely recognized as foundational to safe autonomous operation, especially where sensor fusion or contextual inference is limited.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2602.00314">On the Assessment of Sensitivity of Autonomous Vehicle Perception</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10287869">Robust Perception Under Adverse Conditions for Autonomous Driving Based ...</a></li>
<li><a href="https://csrc.nist.gov/pubs/other/2026/01/30/on-the-assessment-of-sensitivity-of-autonomous-veh/final">On the Assessment of Sensitivity of Autonomous Vehicle Perception</a></li>

</ul>
</details>

**Discussion**: Commenters debated technical solutions (e.g., adding dedicated water sensors, as done in the 2005 DARPA Grand Challenge), questioned why this common scenario wasn’t addressed earlier, and highlighted the systemic advantage of OTA updates for rapid fleet-wide improvement — while also expressing healthy skepticism about overconfidence in current deployment readiness.

**Tags**: `#autonomous-vehicles`, `#computer-vision`, `#safety-critical-systems`, `#OTA-updates`, `#perception-robustness`

---

<a id="item-13"></a>
## [New IEEE Spectrum article examines Steve Jobs’s NeXT era and its impact on Apple](https://spectrum.ieee.org/steve-jobs-next-computer) ⭐️ 8.0/10

IEEE Spectrum published a detailed analysis of how Steve Jobs’s leadership and technological vision at NeXT Computer (1985–1997) directly shaped Apple’s modern software architecture, including macOS and iOS, following his return in 1997. This analysis clarifies a pivotal but often misunderstood chapter in tech history: NeXTSTEP’s object-oriented, Mach/BSD-based architecture became the foundational layer for all major Apple operating systems, influencing everything from developer tools to user interface philosophy—and remains relevant to current challenges like Vision Pro’s software limitations. NeXTSTEP was built on the Mach microkernel and BSD Unix, featured an advanced object-oriented development environment (including Interface Builder and Objective-C), and was acquired by Apple in 1996—its core technologies directly evolved into Rhapsody, then Mac OS X, and ultimately macOS, iOS, and iPadOS.

hackernews · rbanffy · May 15, 10:34 · [Discussion](https://news.ycombinator.com/item?id=48146908)

**Background**: After being ousted from Apple in 1985, Steve Jobs founded NeXT Inc. and developed the NeXT Computer and its proprietary NeXTSTEP operating system. Though commercially unsuccessful as hardware, NeXTSTEP gained acclaim among developers and academia for its innovative design, stability, and developer tools. When Apple acquired NeXT in 1996, it adopted NeXTSTEP as the foundation for its next-generation OS, marking a decisive pivot away from the aging Classic Mac OS.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NeXTSTEP">NeXTSTEP - Wikipedia</a></li>
<li><a href="https://www.howtogeek.com/698532/before-mac-os-x-what-was-nextstep-and-why-did-people-love-it/">Before Mac OS X: What Was NeXTSTEP , and Why Did People Love It?</a></li>

</ul>
</details>

**Discussion**: Readers highlight NeXT’s outsized influence on modern Apple ('modern Apple is largely Next'), correct historical oversights (e.g., praising Apple II’s success), express concern over Apple’s recent software stagnation (citing Vision Pro’s underwhelming OS), and note ongoing cultural interest in NeXT’s legacy—including Linux projects emulating its UI.

**Tags**: `#Apple`, `#NeXT`, `#Steve Jobs`, `#operating systems`, `#tech history`

---

<a id="item-14"></a>
## [Anima: Open-source 2B-parameter anime-style text-to-image model](https://civitai.com/models/2458426/anima) ⭐️ 8.0/10

CircleStone Labs and Comfy Org jointly released Anima, a 2-billion-parameter open-source text-to-image model trained exclusively on real-world anime and non-photorealistic art data (no synthetic data), available under a non-commercial license. Anima fills a notable gap in the open-source ecosystem by offering high-capacity, anime-specialized generation without reliance on synthetic or photorealistic data—enabling more authentic, lightweight, and controllable local deployment for creators, designers, and AIGC communities focused on anime and stylized art. The model is distributed via Civitai and Hugging Face, supports ComfyUI workflows natively, and is trained on ~millions of anime images plus ~800K non-anime non-photorealistic artworks; its non-commercial license restricts commercial fine-tuning or deployment.

telegram · zaihuapd · May 15, 03:00

**Background**: Text-to-image models convert natural language prompts into visual outputs; anime-style models specialize in generating illustrations resembling Japanese animation or manga. ComfyUI is a node-based, open-source interface widely used for customizing and orchestrating diffusion models. Unlike many large models trained on mixed or synthetic datasets (e.g., Stable Diffusion XL), Anima emphasizes authenticity by using only human-curated, real-world artistic data.

<details><summary>References</summary>
<ul>
<li><a href="https://civitai.com/models/2458426/anima-official">Anima - base-v1.0 | Anima Checkpoint | Civitai</a></li>
<li><a href="https://www.modelscope.cn/models/circlestone-labs/Anima">Anima · Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/ComfyUI">ComfyUI - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#文生图`, `#动漫生成`, `#开源模型`

---

<a id="item-15"></a>
## [Surge Declines VLESS/XLS Support Due to Non-Standard TLS Design](https://t.me/zaihuapd/41396) ⭐️ 8.0/10

Surge's official team confirmed it will not merge its experimental VLESS/XLS (including XTLS Vision) implementation into the stable release, citing risks from non-standard TLS layering and required deep modifications to OpenSSL/BoringSSL. This decision highlights a critical engineering trade-off between protocol innovation and long-term maintainability/security—especially relevant for developers building secure, standards-compliant network gateways or edge proxies for AI/ML services. Supporting VLESS/XLS requires custom patching of TLS libraries to break the strict separation between transport and application layers, hindering upstream security updates and increasing audit complexity; Surge retains experimental support only in development builds.

telegram · zaihuapd · May 15, 05:36

**Background**: VLESS is a lightweight, stateless proxy protocol developed by Project X (Xray), designed to evade deep packet inspection (DPI) through flexible transport options like WebSocket and Reality. XTLS Vision is an optimized variant that modifies TLS handshake behavior for performance, but does so by injecting application-layer logic into TLS record processing—a departure from RFC-compliant TLS usage. Surge is a popular macOS/iOS network debugging and proxy tool known for its strict adherence to standard protocols and upstream library compatibility.

<details><summary>References</summary>
<ul>
<li><a href="https://xtls.github.io/en/development/protocols/vless.html">VLESS Protocol | Project X - GitHub Pages</a></li>
<li><a href="https://habr.com/en/articles/990144/">The VLESS Protocol: How It Bypasses Censorship in Russia and Why ... - Habr</a></li>
<li><a href="https://aurax-services.online/en/learn/vless-vpn-protocol">What Is VLESS? VPN Protocol Explained — AuraX</a></li>

</ul>
</details>

**Tags**: `#网络协议`, `#TLS安全`, `#软件工程决策`

---

<a id="item-16"></a>
## [OpenAI previews personal finance feature for US ChatGPT Pro users](https://openai.com/index/personal-finance-chatgpt/) ⭐️ 8.0/10

OpenAI has launched a preview of a personal finance feature for US-based ChatGPT Pro users, enabling secure financial account linking via Plaid across 12,000+ institutions and introducing the newly named GPT-5.5 Thinking model for contextual financial analysis. This marks OpenAI’s first deep integration of real-time financial data into ChatGPT, setting a precedent for AI-powered financial assistance with strict privacy safeguards—and signals a major step toward production-grade, regulated-domain AI applications. The feature uses Plaid for read-only access to balances, transactions, investments, and liabilities; all synced data is automatically deleted from OpenAI systems within 30 days after disconnection, and Intuit support is forthcoming.

telegram · zaihuapd · May 15, 16:50

**Background**: Plaid is a leading financial data API platform that enables secure, standardized connectivity between fintech apps and banks—eliminating the need to integrate individually with thousands of financial institutions. Financial API integrations like Plaid’s are foundational for building compliant, scalable money management tools. OpenAI’s use of Plaid reflects industry-standard practices for secure open banking access in the US.

<details><summary>References</summary>
<ul>
<li><a href="https://plaid.com/resources/open-finance/financial-api-integration/">What is a financial API integration and how does it work? | Plaid</a></li>
<li><a href="https://medium.com/@sharrite/integrating-plaid-api-a-comprehensive-guide-for-financial-app-authentication-b1a7c0aab97e">Integrating Plaid API : A Comprehensive guide for financial ... | Medium</a></li>
<li><a href="https://itexus.com/how-to-use-plaid-api-integration-a-comprehensive-guide-for-fintech-startups/">Plaid API Integration Guide: Secure Bank Connectivity for Fintech Apps</a></li>

</ul>
</details>

**Tags**: `#AI应用落地`, `#金融API集成`, `#数据隐私设计`

---