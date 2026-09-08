---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 33 items, 22 important content pieces were selected

---

1. [LG Smart TVs Caught Logging Audio and Snooping on Local Devices](#item-1) ⭐️ 9.0/10
2. [Researcher factors 512-bit RSA key of 1990s CA in two days on consumer GPU](#item-2) ⭐️ 8.0/10
3. [TALA Diagram Layout Engine Open-Sourced](#item-3) ⭐️ 8.0/10
4. [Jellyfin 12.0 Released with Smooth Migration and Performance Boosts](#item-4) ⭐️ 8.0/10
5. [Broadcom Pulls VDDK Downloads, Hindering VMware Exit](#item-5) ⭐️ 8.0/10
6. [AI Crawlers Overwhelm Linux Kernel Git Server, Using 14 CPU Cores for HTML Rendering](#item-6) ⭐️ 8.0/10
7. [DNS Abuse: 10-20% of New gTLD Domains Are Scams](#item-7) ⭐️ 8.0/10
8. [LLM-guided evolution improves 10 best-known circle-packing solutions](#item-8) ⭐️ 8.0/10
9. [KV Cache as an Agent Runtime: Yandex&\#x27;s Interactive LLM Approach](#item-9) ⭐️ 8.0/10
10. [Study Uses 31,352 Repeated Measurements to Track LLM Performance Drift](#item-10) ⭐️ 8.0/10
11. [OpenAI Researchers Embrace Coding Agents and Recursive Self-Improvement](#item-11) ⭐️ 7.0/10
12. [There&\#x27;s No Limit to How Bad Code Can Get](#item-12) ⭐️ 7.0/10
13. [Software Can Always Get Worse, Unlike Buildings](#item-13) ⭐️ 7.0/10
14. [Tiny Recurrent System Generates Full Bad Apple Video from Single Initial State](#item-14) ⭐️ 7.0/10
15. [Reproducibility in ML Research Declining Due to Hardware Barriers and Corporate Secrecy](#item-15) ⭐️ 7.0/10
16. [Researcher Claims 95% Token Reduction in Image Processing for Multimodal LLMs](#item-16) ⭐️ 7.0/10
17. [PINNStudio: A Free, Open-Source No-Code GUI for PINNs](#item-17) ⭐️ 7.0/10
18. [OpenAI Chief Scientist Advocates Powerful AI for Defense, Warns Against Recklessness](#item-18) ⭐️ 6.0/10
19. [Browser-Based Video Compressor Built with Claude Code and FFmpeg WebAssembly](#item-19) ⭐️ 6.0/10
20. [Zero-Downtime Embedding Model Migration via Reranking](#item-20) ⭐️ 6.0/10
21. [Rustuna: High-Performance Rust Implementation of Optuna Released](#item-21) ⭐️ 6.0/10
22. [Proposal: Stockfish-like Decision Quality Engine for Rocket League via Offline RL](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [LG Smart TVs Caught Logging Audio and Snooping on Local Devices](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 9.0/10

An investigation reveals that LG smart TVs are secretly recording audio and scanning other devices on the local network even when the screen is off, affecting up to 216 million units. This exposes a severe privacy violation, as users have no expectation that a turned-off TV is eavesdropping on their conversations and monitoring their home network, potentially breaching wiretapping laws and undermining trust in smart home devices. The TV&\#x27;s Automatic Content Recognition \(ACR\) and data collection features run even when the device appears powered off, actively capturing audio snippets and probing local network devices. LG&\#x27;s terms of service also require users to obtain consent from all household members and guests whose voices may be captured, a condition that is both impractical and legally questionable.

hackernews · treve · Sep 7, 00:22 · [Discussion](https://news.ycombinator.com/item?id=49592375)

**Background**: Smart TVs routinely use Automatic Content Recognition \(ACR\) to capture screenshots and track viewing habits, but this typically occurs only when the TV is actively in use. LG&\#x27;s behavior is more invasive because data collection persists even when the screen is off. Previous scandals, such as Samsung&\#x27;s ACR lawsuit, have shown that TV manufacturers collect vast amounts of viewing data without clear consent. The LG terms of service, highlighted by commenters, grant the company broad rights to process audio, requiring users to notify everyone within range, which exemplifies the aggressive nature of these privacy policies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.consumerreports.org/electronics/privacy/how-to-turn-off-smart-tv-snooping-features-a4840102036/">How to Turn Off Smart TV Snooping Features - Consumer Reports</a></li>
<li><a href="https://stateofsurveillance.org/guides/basic/disable-smart-tv-acr-surveillance-2026/">How to Disable Smart TV ACR Surveillance (2026 Guide)</a></li>

</ul>
</details>

**Discussion**: Community reaction is overwhelmingly negative, with users expressing outrage at the invasive data collection. One commenter highlights LG&\#x27;s absurd contractual requirement to notify all nearby individuals, while others share personal stories of proactively disabling network features and feeling vindicated. Some raise concerns about legality under wiretapping laws and point out the irony of ad-supported sites reporting on privacy violations.

**Tags**: `#privacy`, `#smart-tv`, `#LG`, `#security`, `#IoT`

---

<a id="item-2"></a>
## [Researcher factors 512-bit RSA key of 1990s CA in two days on consumer GPU](https://mcpherrin.ca/2026/09/07/rsa.html) ⭐️ 8.0/10

A researcher successfully factored a 512-bit RSA key from a Certificate Authority that operated in the 1990s, completing the computation in just two days using a consumer-grade GPU. This practical demonstration shows how easily historical encryption can be broken with modern hardware. This breakthrough highlights that any encrypted traffic recorded from that era, which largely lacked forward secrecy, could now be decrypted by anyone with modest computational resources. It underscores the urgent need to abandon weak legacy cryptography and protect past communications from retroactive decryption. The 512-bit RSA key was factored in approximately 48 hours on a consumer GPU, and the researcher had to implement a custom TLS stack because Go&\#x27;s standard library dropped SSLv3 support. The target was a CA key from the 1990s, a period when such key sizes were considered secure but are now trivially breakable.

hackernews · ahlCVA · Sep 8, 01:16 · [Discussion](https://news.ycombinator.com/item?id=49604637)

**Background**: RSA encryption security relies on the difficulty of factoring large numbers. In the 1990s, 512-bit RSA keys were common, but advances in computing have made them easily breakable. A Certificate Authority \(CA\) is a trusted entity that issues digital certificates; compromising a CA&\#x27;s private key allows impersonation of any website. The lack of forward secrecy in many old protocols means that recorded encrypted traffic can be decrypted if the key is later compromised.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29">RSA (cryptosystem) - Wikipedia</a></li>
<li><a href="https://arstechnica.com/security/2024/08/home-energy-system-gives-researcher-control-of-virtual-power-plant/">512 - bit RSA key in home energy system gives control... - Ars Technica</a></li>
<li><a href="https://en.wikipedia.org/wiki/Certificate_authority">Certificate authority - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that much traffic from the 90s lacked ephemeral keys, raising concerns about governments storing encrypted data for future decryption. Some criticized the researcher&\#x27;s reliance on LLM output for analyzing the custom TLS implementation, while others found the achievement impressive and the SSL grading report humorous.

**Tags**: `#cryptography`, `#RSA`, `#factoring`, `#historical security`, `#TLS/SSL`

---

<a id="item-3"></a>
## [TALA Diagram Layout Engine Open-Sourced](https://d2lang.com/blog/tala-is-open-source/) ⭐️ 8.0/10

TALA, Terrastruct&\#x27;s proprietary layout engine for D2 diagrams, has been open-sourced, making its advanced autolayout algorithms freely available to the community. This open-sourcing removes a cost barrier, enabling developers to create cleaner, more professional architecture diagrams with D2, and potentially integrating TALA into other diagramming tools and workflows. TALA is a general orthogonal layout engine, not limited to hierarchical structures, and was built from scratch with zero dependencies. The open-source release enables integration into other tools like Graphviz, as mentioned in community discussions.

hackernews · alixanderwang · Sep 7, 23:37 · [Discussion](https://news.ycombinator.com/item?id=49604150)

**Background**: D2 is a modern diagram scripting language that converts text descriptions into diagrams. TALA \(Terrastruct AutoLayout Approach\) is a layout engine that automatically arranges diagram elements, previously sold as a paid add-on for D2. It specializes in producing tidy, orthogonal layouts for cloud and software architecture diagrams, which are often complex and non-hierarchical.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/terrastruct/TALA">GitHub - terrastruct/ TALA : A diagram layout engine designed...</a></li>
<li><a href="https://terrastruct.com/tala/">Information about TALA , Terrastruct&#x27;s proprietary layout engine for D2</a></li>
<li><a href="https://d2lang.com/tour/tala/">TALA | D2 Documentation</a></li>

</ul>
</details>

**Discussion**: The community reacted positively, with many noting TALA produces cleaner layouts than D2&\#x27;s default engine or ELK. However, some pointed out that it can make certain diagrams, like a Go queue flow, appear more complicated. The high cost was a barrier for hobbyists, so open-sourcing is welcomed. There is interest in integrating TALA into Graphviz and Daedalus.

**Tags**: `#open-source`, `#diagramming`, `#layout-engine`, `#D2`, `#developer-tools`

---

<a id="item-4"></a>
## [Jellyfin 12.0 Released with Smooth Migration and Performance Boosts](https://jellyfin.org/posts/jellyfin-release-12.0/) ⭐️ 8.0/10

Jellyfin 12.0, a major update of the open-source media server, has been released, delivering performance improvements and a seamless migration experience. Users upgrading from older versions like 10.10.7 report quick and painless transitions. This release strengthens Jellyfin&\#x27;s role as a strong self-hosted alternative to Plex, offering a viable exit path for users avoiding vendor lock-in. Improved performance and easier upgrades lower the adoption barrier, potentially drawing more users from proprietary platforms. A user with a 40TB library upgraded from 10.10.7 to 12.0 in minutes, with only temporary title disappearance fixed by a rescan. Persistent subtitle issues remain, especially on the Android client with Chromecast, where display and manual addition often fail.

hackernews · 0xC0ncord · Sep 8, 01:56 · [Discussion](https://news.ycombinator.com/item?id=49604861)

**Background**: Jellyfin is a free, open-source media server that lets users host and stream their own media collections to any device. Built by volunteers, it is a popular alternative to proprietary solutions like Plex, providing full control without licensing fees. Often paired with the \*arr stack \(Sonarr, Radarr, etc.\) for automated media management, Jellyfin releases major version increments to deliver significant improvements and new features.

<details><summary>References</summary>
<ul>
<li><a href="https://jellyfin.org/">The Free Software Media System | Jellyfin</a></li>
<li><a href="https://github.com/jellyfin/jellyfin">GitHub - jellyfin / jellyfin : The Free Software Media System - Server ...</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is positive, with Plex users welcoming Jellyfin&\#x27;s progress as a safety net. Upgrade experiences were praised for speed and ease, though some users still face persistent subtitle issues, particularly on Android TV, and one user had to revert from a previous version due to performance problems.

**Tags**: `#Jellyfin`, `#media-server`, `#open-source`, `#release`, `#self-hosted`

---

<a id="item-5"></a>
## [Broadcom Pulls VDDK Downloads, Hindering VMware Exit](https://www.virtualizationhowto.com/2026/09/leaving-vmware-just-got-harder-after-broadcom-pulled-vddk-downloads/) ⭐️ 8.0/10

Broadcom has removed public access to VMware&\#x27;s Virtual Disk Development Kit \(VDDK\) downloads, a critical library for reading and converting VMware virtual disks during migrations. This disrupts tools that rely on VDDK to move workloads to other platforms. This strengthens vendor lock-in at a time when many enterprises are exploring alternatives due to Broadcom&\#x27;s licensing changes and cost hikes. By raising the technical barrier to exit, Broadcom may force customers to delay migrations and calls into question the ecosystem&\#x27;s openness. VDDK is a set of C/C++ libraries and utilities that enable programmatic access to VMDK files. Migration tools like virt-v2v and StarWind V2V Converter now require a valid VMware support contract to obtain VDDK legally, complicating transitions for organizations without active entitlements.

hackernews · josephcsible · Sep 7, 20:32 · [Discussion](https://news.ycombinator.com/item?id=49602699)

**Background**: VMware was the dominant virtualization platform for decades, but Broadcom&\#x27;s 2023 acquisition led to product bundling, per-core licensing, and price increases that pushed customers to consider Proxmox, Hyper-V, and KVM. VDDK was previously a free download for legitimate customers, enabling third-party backup and migration software to interoperate with VMware&\#x27;s disk format. The removal is seen as part of a broader strategy to monetize previously free components and retain customers.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/ptp2308/how-to-vm-migrate-from-vmware-to-kvm-key-tips-and-pitfalls-522c">How to vm migrate from vmware to kvm — key tips... - DEV Community</a></li>
<li><a href="http://appquantify.com/p39719-vmware-virtual-disk-development-kit.aspx">VMware Virtual Disk Development Kit - appQuantify</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely negative, with former VMware engineers and IT pros lamenting the platform&\#x27;s decline. Many shared migration experiences, noting that Proxmox migrations remain unaffected and surprisingly painless, while others advocate moving to KVM and investing in internal skills. There is nostalgia for VMware&\#x27;s past engineering excellence, contrasted with Broadcom&\#x27;s extraction-focused approach.

**Tags**: `#virtualization`, `#VMware`, `#Broadcom`, `#migration`, `#lock-in`

---

<a id="item-6"></a>
## [AI Crawlers Overwhelm Linux Kernel Git Server, Using 14 CPU Cores for HTML Rendering](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 8.0/10

Konstantin Ryabitsev reported that abusive web crawlers are overwhelming git.kernel.org, consuming more CPU time than all legitimate traffic. Across five geo-distributed nodes, 14 CPU cores are constantly rendering git commits as HTML for scrapers. This incident underscores the severe infrastructure burden that AI crawlers impose on critical open-source projects, raising concerns about the sustainability of free services that underpin modern software development. It also serves as a warning for other web services with many crawlable pages, like Datasette, which could face similar resource drains. The git.kernel.org infrastructure spans 5 nodes with a total of about 90 CPU cores; 14–16 of those cores are permanently occupied by rendering commits for crawlers, reducing capacity for legitimate operations like cloning. These crawlers ignore rate limits and robots.txt, creating a constant, non-bursty load.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org is the official Git repository for the Linux kernel, one of the most critical open-source projects. To make commits browsable, the server dynamically renders each commit into an HTML page, a CPU-intensive process. AI crawlers from various companies scrape these pages to train language models or build search indexes, often doing so aggressively without respecting rate limits, causing significant server strain. Cloudflare reports that training traffic accounts for nearly 80% of AI crawling, with no clear cyclical pattern.

<details><summary>References</summary>
<ul>
<li><a href="https://securityonline.info/ai-crawlers-git-kernel/">AI Crawlers Strain git .kernel.org Servers</a></li>
<li><a href="https://blog.cloudflare.com/ai-crawler-traffic-by-purpose-and-industry/">A deeper look at AI crawlers: breaking down traffic by purpose and industry | Cloudflare Blog</a></li>

</ul>
</details>

**Tags**: `#crawling`, `#web scraping`, `#infrastructure`, `#git`, `#AI crawlers`

---

<a id="item-7"></a>
## [DNS Abuse: 10-20% of New gTLD Domains Are Scams](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 8.0/10

An Interisle report reveals that in 2025, 85 million new gTLD registrations were made, 8.5 million were already blocklisted by May 2025, and the actual abuse rate is likely between 10% and 20%, meaning one in five new domains is a scam. This staggering abuse rate points to a systemic failure in internet governance and domain registration oversight, undermining trust in the DNS and enabling large-scale cybercrime that affects millions worldwide. ICANN, the organization coordinating the DNS, has been discussing this problem for years with little progress. The report focuses on new gTLDs, where cheap, easily registered domains are exploited by scammers.

rss · Simon Willison · Sep 6, 14:40

**Background**: gTLDs \(generic top-level domains\) are domain extensions not tied to a specific country, such as .com, .org, and newer ones like .shop or .online. ICANN \(Internet Corporation for Assigned Names and Numbers\) is the global body that coordinates the domain name system and IP addresses. The expansion of new gTLDs in the 2010s dramatically increased the number of available domains, often at very low cost, which scammers have exploited.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ovhcloud.com/en/learn/what-is-gtld/">What is a gTLD (Generic Top Level-Domain)? | OVHcloud Worldwide</a></li>
<li><a href="https://www.icann.org/resources/pages/what-2012-02-25-en">What Does ICANN Do? - ICANN</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#cybersecurity`, `#scams`, `#domain abuse`, `#internet infrastructure`

---

<a id="item-8"></a>
## [LLM-guided evolution improves 10 best-known circle-packing solutions](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

An LLM guided the iterative evolution of an optimization algorithm for circle packing. This improved the best-known solutions for 10 instances \(N=101–114\) on the Packomania csqv benchmark by 2.4–5.4%, at a total LLM cost of $27.72. It demonstrates that LLM-guided program evolution can achieve state-of-the-art results on a classic optimization benchmark with minimal cost, opening a new avenue for automated algorithm discovery. Starting from a simple seed solver, the LLM proposed algorithmic changes over 15 iterations guided by a scoreboard of results and history. The author flags the plateau-detection stopping rule as a weak point and invites critique; the improved solutions were independently verified by Packomania.

reddit · r/MachineLearning · /u/SIGH\_I\_CALL · Sep 7, 16:54

**Background**: Circle packing seeks to maximize the sum of radii of equal circles inside a container, a classic NP-hard optimization problem. Packomania is a long-standing benchmark tracking the best-known solutions. LLM-guided program evolution is a technique where a large language model iteratively mutates and refines source code, akin to genetic programming but leveraging language model capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://packomania.com/">Packomania (52C17)</a></li>
<li><a href="https://arxiv.org/html/2609.05093">LLM - Guided Program Evolution for Circle Packing:Breaking 10...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Packing_problems">Packing problems - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM-guided evolution`, `#optimization`, `#circle packing`, `#program synthesis`, `#machine learning`

---

<a id="item-9"></a>
## [KV Cache as an Agent Runtime: Yandex&\#x27;s Interactive LLM Approach](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

Yandex researchers propose using KV-cache modifications as an agent runtime, enabling more interactive and responsive LLM systems. They preview a Qwen3.8-27B agent playing DOOM interactively. This approach explores an underexplored design axis—the inference runtime—between the model and the agent harness, potentially offering lower latency and more responsive agents without costly model retraining. The work builds on previous papers Hogwild\! Inference and AsyncReasoning, and uses Qwen3.8-27B. The technique modifies the KV cache state directly during inference, rather than relying on traditional prompt-based interaction.

reddit · r/MachineLearning · /u/\_puhsu · Sep 7, 09:03

**Background**: KV cache \(Key-Value cache\) is an optimization in transformer models that stores intermediate key and value vectors from previous tokens during autoregressive inference, avoiding recomputation. Typically, the KV cache is a passive memory; Yandex&\#x27;s approach treats it as an active state that can be manipulated to simulate agent actions.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>

</ul>
</details>

**Tags**: `#KV-cache`, `#LLM agents`, `#interactive AI`, `#inference optimization`, `#agent runtime`

---

<a id="item-10"></a>
## [Study Uses 31,352 Repeated Measurements to Track LLM Performance Drift](https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/) ⭐️ 8.0/10

A study reframes LLM evaluation as a longitudinal measurement problem, using 31,352 repeated observations across 49 models to detect performance drift. It found between-day score variability \(SD 8.43\) was three times larger than within-day variability \(SD 2.80\), highlighting significant temporal changes. This approach addresses a critical blind spot in snapshot-based evaluation by revealing that API-served models can exhibit significant performance drift over time. It enables practitioners to detect behavioral changes early, ensuring more reliable LLM deployments. Based on 31,352 observations, the within-day score standard deviation was 2.80, while the between-day daily median standard deviation was 8.43, a roughly 3:1 ratio. The methodology versions benchmarks, uses execution-based evaluation, tracks metadata, and applies change-point detection to time series.

reddit · r/MachineLearning · /u/ionutvi · Sep 7, 07:44

**Background**: LLM benchmarks are typically one-time snapshots that assume static model performance. However, API-served models can change silently due to provider updates, infrastructure shifts, or version transitions, leading to performance drift. Longitudinal measurement, commonly used in clinical studies, involves repeated observations over time to detect changes. This study applies that paradigm to LLM evaluation, also addressing benchmark contamination where public test sets can skew results.

<details><summary>References</summary>
<ul>
<li><a href="https://toloka.ai/blog/llm-observability/">LLM observability</a></li>
<li><a href="https://www.logicmonitor.com/blog/llms-dont-stand-still-how-to-monitor-and-trust-the-models-powering-your-ai">How to Monitor and Trust the LLMs Powering Your AI | LogicMonitor</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#benchmarks`, `#performance drift`, `#longitudinal measurement`, `#machine learning`

---

<a id="item-11"></a>
## [OpenAI Researchers Embrace Coding Agents and Recursive Self-Improvement](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 7.0/10

OpenAI reveals that its researchers are increasingly using coding agents, with daily spending per researcher rising from near zero to about $600 by late August 2026. The company also introduces Recursive Self-Improvement \(RSI\) as a new paradigm for AGI, discussed in both a blog post and an essay by the Chief Scientist. This signals that AI-powered coding agents are becoming integral to cutting-edge AI research, potentially accelerating the development of more advanced AI systems. The emergence of RSI as an AGI paradigm suggests a shift toward self-improving AI, which could dramatically speed up progress but also raises safety concerns. The chart shows a plateau around $150–165 per researcher per day from June to July, then a steep climb to $600 in late August, possibly coinciding with internal access to the model later released as GPT-6 Astra. The post does not expand the acronym RSI, indicating it&\#x27;s already a familiar concept within OpenAI.

rss · Simon Willison · Sep 6, 23:57

**Background**: Recursive self-improvement \(RSI\) is the idea of AI systems rewriting their own code to enhance their capabilities, potentially leading to an intelligence explosion. Agentic engineering is a disciplined approach to software development where autonomous AI agents handle coding tasks under human oversight, distinct from the more free-form &\#x27;vibe coding.&\#x27; The steep increase in agent usage at OpenAI may reflect the arrival of a more powerful model like GPT-6 Astra.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is Agentic Engineering? | IBM</a></li>

</ul>
</details>

**Tags**: `#recursive self-improvement`, `#OpenAI`, `#coding agents`, `#agentic engineering`, `#AI research`

---

<a id="item-12"></a>
## [There&\#x27;s No Limit to How Bad Code Can Get](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 7.0/10

Simon Willison, in a Lobste.rs comment, argued that rewriting legacy software from scratch is rarely successful because the old system remains a moving target, developers lose incentive to maintain quality, and the new team often doesn&\#x27;t fully understand the scope, leading to two systems in production. This insight challenges the common impulse to &\#x27;burn it down and start over&\#x27; when facing technical debt, offering a practical, high-stakes lesson for software engineering teams—especially those in startups and large enterprises—who risk wasting time and resources on doomed rewrites. Willison emphasizes that the original system&\#x27;s lack of documentation and tests is precisely why it needs rewriting, yet this makes fully understanding it impossible. He recommends shoring up the old system with automated testing and targeted refactors, citing Will Larson&\#x27;s article &\#x27;Migrations: the sole scalable fix to tech debt&\#x27; as a responsible approach.

rss · Simon Willison · Sep 6, 09:08

**Background**: Technical debt refers to the implied cost of future rework caused by choosing an easy but limited solution today. Legacy code is old code that is difficult to maintain, often lacking tests and documentation. A &\#x27;greenfield&\#x27; project is one developed from scratch, without constraints of a prior system. Rewriting from scratch is often seen as a solution, but the &\#x27;Strangler Fig&\#x27; pattern \(gradual replacement\) is an alternative. The article discusses why the full rewrite strategy often fails because the old system must continue evolving, and the new team struggles to replicate its behavior.

**Tags**: `#software engineering`, `#technical debt`, `#rewrite vs refactor`, `#legacy code`, `#Simon Willison`

---

<a id="item-13"></a>
## [Software Can Always Get Worse, Unlike Buildings](https://simonwillison.net/2026/Sep/6/zach-kehs/) ⭐️ 7.0/10

Zach Kehs published a blog post arguing that software, unlike physical buildings, can perpetually degrade in quality without collapsing because there is no natural limit to adding new layers of indirection or reducing performance. This metaphor highlights the unbounded nature of technical debt, reminding developers that without deliberate maintenance, code quality can decline indefinitely, leading to spiraling complexity and maintenance costs. The quote specifically references the &\#x27;fundamental theorem of software engineering&\#x27;—that all problems can be solved by another level of indirection—but notes that software has no physical limit, so indirection and performance regressions can accumulate endlessly.

rss · Simon Willison · Sep 6, 08:42

**Background**: Technical debt is the future cost of choosing quick, suboptimal solutions today. The &\#x27;fundamental theorem of software engineering&\#x27; states that any problem can be solved by adding a level of indirection, but excessive indirection creates its own complexity. Unlike physical buildings, which have structural limits and will collapse if overloaded, software has no inherent limit to how complex or slow it can become.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indirection">Indirection - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fundamental_theorem_of_software_engineering">Fundamental theorem of software engineering - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Technical_debt">Technical debt</a></li>

</ul>
</details>

**Tags**: `#technical-debt`, `#software-engineering`, `#code-quality`, `#complexity`, `#insight`

---

<a id="item-14"></a>
## [Tiny Recurrent System Generates Full Bad Apple Video from Single Initial State](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/) ⭐️ 7.0/10

A compact recurrent dynamical system with only 417k parameters learns to generate the entire ~6,500-frame Bad Apple video autonomously from a single initial latent state, without any timestamp inputs. It shows that a tiny RNN can capture a long, complex temporal sequence from a single starting point, suggesting efficient paradigms for video generation, animation, and real-time control on resource-constrained hardware. The 64-dim latent state uses an LSTM-style recurrence \(16,640 params\) and a depthwise-separable frame decoder \(400,361 params\). Training leveraged teacher tables, a rollout horizon curriculum \(2→512\), state perturbation noise, and second-difference acceleration regularization, yet the model generalized to the full 6.5k rollout at inference.

reddit · r/MachineLearning · /u/SEBADA321 · Sep 8, 00:05

**Background**: Bad Apple is a monochrome shadow-art music video often used as a stress test for animation and compression. SIREN \(Sinusoidal Representation Networks\) are implicit neural representations that map coordinates to pixel values using periodic activations; this project instead uses a recurrent dynamical system that evolves a latent state to generate frames sequentially, without needing external time signals.

**Tags**: `#recurrent-neural-networks`, `#dynamical-systems`, `#generative-modeling`, `#machine-learning`, `#creative-coding`

---

<a id="item-15"></a>
## [Reproducibility in ML Research Declining Due to Hardware Barriers and Corporate Secrecy](https://www.reddit.com/r/MachineLearning/comments/1w92eis/reproducibility_seems_to_be_headed_towards/) ⭐️ 7.0/10

A Reddit post argues that ML reproducibility is being eroded by three forces: the prohibitive hardware costs of physical AI experiments, unverifiable performance claims from big AI companies, and vague, subjective problem definitions. This erosion threatens the scientific integrity of ML research, as unchecked results could lead to wasted resources, misdirected progress, and diminished trust, especially as AI systems are deployed in critical real-world applications. The post notes that physical AI often requires expensive hardware like high-speed cameras, corporate tools are promoted with unverified accuracy figures, and demos are cherry-picked to hide failures. It contrasts this with historical projects that had high internal reproducibility through mathematical rigor, which modern ML lacks.

reddit · r/MachineLearning · /u/NeighborhoodFatCat · Sep 6, 17:29

**Background**: Physical AI refers to AI systems integrated with robots, sensors, and actuators, requiring real-world testing that is often expensive and difficult to replicate. Reproducibility in ML has long been a challenge, but the rise of large-scale models and corporate secrecy has made it harder to verify results. The post highlights a broader concern that the field&\#x27;s incentive structures reward novelty over reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Physical_AI">Physical AI</a></li>

</ul>
</details>

**Tags**: `#reproducibility`, `#machine learning`, `#research ethics`, `#hardware`, `#corporate transparency`

---

<a id="item-16"></a>
## [Researcher Claims 95% Token Reduction in Image Processing for Multimodal LLMs](https://www.reddit.com/r/MachineLearning/comments/1wab7ui/i_reduced_imageprocessing_token_usage_by_95/) ⭐️ 7.0/10

A researcher reports a new method that reduces token consumption by approximately 95% for image-based LLM inference compared to GPT-4o direct vision, while maintaining roughly the same accuracy on the MOMA Graph benchmark. If validated, this could dramatically lower the cost and latency of multimodal AI applications, making them more feasible for large-scale deployment. It represents a potential breakthrough in inference efficiency for vision-language models. The method is still under development and no implementation details have been shared. The evaluation used 1,315 questions from the MOMA Graph benchmark, and the researcher is seeking community feedback on the strength of the result.

reddit · r/MachineLearning · /u/angelinusbread · Sep 8, 01:57

**Background**: GPT-4o is a multimodal model that processes images directly by converting them into a large number of tokens, which leads to high token usage and cost. Vision-language models \(VLMs\) typically use vision encoders to compress images into tokens; token count directly affects inference speed and expense. The MOMA Graph benchmark is a test suite for evaluating multimodal reasoning capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.ecitis.org/vision-language-models/">Vision Language Models: Architecture, Inference , and Practical...</a></li>

</ul>
</details>

**Tags**: `#multimodal AI`, `#token efficiency`, `#VLM inference`, `#cost optimization`, `#GPT-4o`

---

<a id="item-17"></a>
## [PINNStudio: A Free, Open-Source No-Code GUI for PINNs](https://www.reddit.com/r/MachineLearning/comments/1w9a2i7/pinnstudio_a_free_opensource_nocode_gui_for/) ⭐️ 7.0/10

PINNStudio, a free and open-source no-code GUI, has been released to simplify the setup, training, and visualization of physics-informed neural networks \(PINNs\) by automatically generating DeepXDE code and providing live loss curves and solution plots. By eliminating repetitive coding, PINNStudio lowers the barrier to entry for scientific machine learning, allowing researchers to focus on physics rather than implementation, and potentially speeding up experimentation and discovery. PINNStudio is built on top of DeepXDE, supports 1D and 2D domains with custom PDEs, boundary conditions, network architectures, and training schedules; it includes templates for classic equations like Heat, Allen-Cahn, and Cahn-Hilliard, and can be installed via pip.

reddit · r/MachineLearning · /u/Impossible-Jello2749 · Sep 6, 22:19

**Background**: Physics-informed neural networks \(PINNs\) are deep learning models that incorporate physical laws, typically expressed as partial differential equations \(PDEs\), into the loss function during training. This allows them to solve forward and inverse problems involving differential equations without needing large labeled datasets. DeepXDE is a popular library for implementing PINNs.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@tauqeerahmad899/physics-informed-neural-networks-pinns-8fb137024b62">Physics - Informed Neural Networks ( PINNs ) | by Tauqeer... | Medium</a></li>

</ul>
</details>

**Tags**: `#PINNs`, `#scientific machine learning`, `#no-code`, `#GUI`, `#open-source`

---

<a id="item-18"></a>
## [OpenAI Chief Scientist Advocates Powerful AI for Defense, Warns Against Recklessness](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 6.0/10

OpenAI&\#x27;s Chief Scientist Jakub Pachocki published a statement arguing that rapidly building more powerful AI models is necessary to defend against dangers from other AI systems, while cautioning that this urgency must not lead to recklessness. This statement provides a high-profile rationale for the continued acceleration of AI development, framing it as a defensive necessity that could shape public policy and industry debate on AI safety and alignment. The statement, from OpenAI&\#x27;s blog post &\#x27;An Alien Mind&\#x27;, emphasizes the need for &\#x27;powerful, aligned AI&\#x27; to secure infrastructure, protect against rogue agents in real time, and invent new protective measures.

rss · Simon Willison · Sep 7, 22:26

**Background**: AI alignment is the field of ensuring AI systems pursue goals that match human values and intentions. Rogue AI agents are autonomous systems that can cause unintended harm, such as unauthorized data deletion or strategic deception. Both concepts underpin Pachocki&\#x27;s argument that advanced AI is needed to counter threats from misaligned or malicious AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://grokipedia.com/page/AI_Agents_Gone_Rogue">AI Agents Gone Rogue</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#ai-safety`, `#openai`, `#alignment`, `#artificial-intelligence`

---

<a id="item-19"></a>
## [Browser-Based Video Compressor Built with Claude Code and FFmpeg WebAssembly](https://simonwillison.net/2026/Sep/7/video-compressor/) ⭐️ 6.0/10

Simon Willison built a browser-based video compressor using Claude Code \(Claude Fable 5.1\) and the WebAssembly port of FFmpeg, enabling users to generate multiple optimized video versions with presets and customizable settings without any server-side processing. This demonstrates the combination of AI-assisted coding and WebAssembly to bring powerful native multimedia processing to the web, lowering the barrier for content creators to compress videos without installing software or uploading to cloud services, and highlights the rapid prototyping potential of Claude Code. The tool uses presets with CRF values from 22 to 28, audio bitrates from 128 to 64 kbps, output resolutions like 854×370, and options for encoder speed, H.264 profile, 30 fps limit, metadata stripping, and encoding only the first 10 seconds. It generated 5 versions in 11.8 seconds using ffmpeg.wasm, a pure WebAssembly/JavaScript port of FFmpeg.

rss · Simon Willison · Sep 7, 18:29

**Background**: Claude Code is an agentic coding tool by Anthropic that understands codebases, edits files, and runs commands. FFmpeg is a widely used open-source multimedia framework. WebAssembly enables high-performance execution of C/C++ in browsers. The ffmpeg.wasm project compiles FFmpeg with Emscripten to run entirely in the browser, eliminating server-side processing. Claude Fable is a version of Claude with enhanced safeguards, released in 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://ffmpegwasm.netlify.app/docs/overview/">Overview | ffmpeg .wasm</a></li>

</ul>
</details>

**Tags**: `#webassembly`, `#ffmpeg`, `#video-compression`, `#ai-tools`, `#web-development`

---

<a id="item-20"></a>
## [Zero-Downtime Embedding Model Migration via Reranking](https://www.reddit.com/r/MachineLearning/comments/1wabmm7/my_lab_found_a_way_to_migrate_between_embedding/) ⭐️ 6.0/10

A research lab has introduced embedflow, a method that migrates between embedding models by retrieving top-K documents from the old index and reranking them with the new model, eliminating the need to re-embed the entire document collection. This approach can dramatically reduce the time and cost of upgrading embedding models in large-scale RAG systems, enabling continuous service without downtime and making it practical to adopt better models more frequently. The method requires selecting an appropriate K value; for a qwen4b to qwen8b migration, K=50 achieved retrieval quality equal to native use of the target model. It currently supports Qdrant and is available via pip, but the optimal K may vary across model pairs and the approach has not been validated on billion-scale datasets.

reddit · r/MachineLearning · /u/Potential\_Low\_1183 · Sep 8, 02:16

**Background**: Embedding models convert text into dense vectors for semantic search and are essential in Retrieval-Augmented Generation \(RAG\). Upgrading to a better model normally requires re-embedding all documents, which for large databases can take weeks or months. Reranking is a technique where a more accurate model re-scores a small set of candidate documents to improve retrieval precision. Embedflow combines initial retrieval from the old index with reranking by the new model, effectively simulating the new model&\#x27;s embeddings without a full backfill.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pinecone.io/learn/series/rag/embedding-models-rundown/">Choosing an Embedding Model | Pinecone</a></li>
<li><a href="https://grokipedia.com/page/LLM-Based_Reranking">LLM-Based Reranking</a></li>
<li><a href="https://www.ibm.com/think/topics/vector-search">What is vector search? | IBM</a></li>

</ul>
</details>

**Tags**: `#embedding-models`, `#vector-search`, `#rag`, `#reranking`, `#migration`

---

<a id="item-21"></a>
## [Rustuna: High-Performance Rust Implementation of Optuna Released](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 6.0/10

Rustuna, a new Rust implementation of the Optuna hyperparameter optimization framework, has been released with zero Python dependencies and improved memory efficiency. By eliminating Python dependencies, Rustuna reduces the risk of software supply chain attacks and offers a lower memory footprint, making hyperparameter optimization safer and more efficient for production environments. Rustuna maintains Optuna-compatible API design, enabling easy migration, and leverages Rust&\#x27;s memory management for optimized performance. It is available on GitHub under the optuna organization.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is a popular open-source hyperparameter optimization framework for machine learning, written in Python. Hyperparameter optimization is the process of automatically searching for the best model configuration to minimize a loss function. Rust is a systems programming language known for performance and memory safety.

<details><summary>References</summary>
<ul>
<li><a href="https://optuna.readthedocs.io/en/stable/index.html">Optuna : A hyperparameter optimization framework — Optuna ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperparameter_optimization">Hyperparameter optimization - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#rust`, `#hyperparameter-optimization`, `#machine-learning`, `#optuna`, `#performance`

---

<a id="item-22"></a>
## [Proposal: Stockfish-like Decision Quality Engine for Rocket League via Offline RL](https://www.reddit.com/r/MachineLearning/comments/1wadyz7/what_if_competitive_games_such_as_rocket_league/) ⭐️ 6.0/10

A Reddit user proposed a system to evaluate the quality of player decisions in Rocket League using offline reinforcement learning, trajectory transformers, and implicit Q-learning, similar to how Stockfish evaluates chess moves. Such a system could offer players objective, AI-driven feedback on their in-game decisions, potentially revolutionizing training and analysis in esports. The proposal is conceptual, from a first-year student, and outlines using pro player datasets, modeling as a sequential POMDP, and anti-cheat via FFT and kinematic limits. No implementation exists.

reddit · r/MachineLearning · /u/Ligras · Sep 8, 04:11

**Background**: Trajectory transformers treat reinforcement learning as a sequence modeling problem, encoding states, actions, and rewards. Offline RL learns policies from fixed datasets without online interaction. Implicit Q-learning \(IQL\) is an offline RL algorithm that estimates action values without querying out-of-distribution actions, making it suitable for learning from demonstrations. A sequential POMDP models decision-making under partial observability over time.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/docs/transformers/v4.21.2/model_doc/trajectory_transformer">Trajectory Transformer</a></li>
<li><a href="https://arxiv.org/abs/2110.06169">[2110.06169] Offline Reinforcement Learning with Implicit Q-Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#game AI`, `#decision quality`, `#trajectory transformers`, `#competitive gaming`

---