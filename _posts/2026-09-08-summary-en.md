---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 28 items, 18 important content pieces were selected

---

1. [LG Smart TVs Found Logging Audio and Snooping on Local Devices](#item-1) ⭐️ 8.0/10
2. [Caltech Mathathon: First-ever AI Hackathon for Research Mathematics](#item-2) ⭐️ 8.0/10
3. [Abusive Crawlers Consume 14 CPU Cores Rendering Git Commits on kernel.org](#item-3) ⭐️ 8.0/10
4. [OpenAI Chief Scientist: Build Powerful AI for Defense, but Avoid Recklessness](#item-4) ⭐️ 8.0/10
5. [Rustuna: High-Performance Rust Implementation of Optuna Released](#item-5) ⭐️ 8.0/10
6. [LLM-Guided Program Evolution Breaks 10 Circle-Packing Records for $28](#item-6) ⭐️ 8.0/10
7. [KV Cache as an Agent Runtime for Interactive LLM Systems](#item-7) ⭐️ 8.0/10
8. [IEEE T-PAMI EIC Confirms Ghost Reviewer in Paper Rejection](#item-8) ⭐️ 8.0/10
9. [Interactive Map Charts LA Building Construction Dates from 1880 to 2026](#item-9) ⭐️ 7.0/10
10. [Icy Moons: Hidden Ocean Worlds in Our Solar System](#item-10) ⭐️ 7.0/10
11. [OpenAI Researchers&\#x27; Daily Spending on Coding Agents Soars](#item-11) ⭐️ 7.0/10
12. [Report: 10-20% of New gTLD Registrations Are Scams](#item-12) ⭐️ 7.0/10
13. [Simon Willison Warns Against Rewriting Codebases from Scratch](#item-13) ⭐️ 7.0/10
14. [Tiny recurrent network generates full Bad Apple video from single initial state](#item-14) ⭐️ 7.0/10
15. [ML Reproducibility Declining Due to Hardware, Secrecy, and Cherry-Picked Demos](#item-15) ⭐️ 7.0/10
16. [Longitudinal Benchmarking Reveals LLM Performance Drift in API Models](#item-16) ⭐️ 7.0/10
17. [Mercator ↔ Equal Earth: Interactive D3 Animated Map Transition](#item-17) ⭐️ 6.0/10
18. [PINNStudio Brings No-Code GUI to Physics-Informed Neural Networks](#item-18) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [LG Smart TVs Found Logging Audio and Snooping on Local Devices](https://www.youtube.com/watch?v=6IFVTcM28KA) ⭐️ 8.0/10

LG smart TVs have been discovered to record audio through the built-in microphone even when the screen is off, and to actively scan the user&\#x27;s home network for connected devices, sending this data to remote servers. This invasive behavior raises serious privacy concerns, as it suggests LG may be eavesdropping on users without meaningful consent, potentially violating wiretapping laws and eroding trust in smart home devices. The TV&\#x27;s microphone stays active in standby mode, capturing and storing audio until a network connection is available to exfiltrate it. The TV also scans the local network for other devices, potentially fingerprinting the home environment.

hackernews · treve · Sep 7, 00:22 · [Discussion](https://news.ycombinator.com/item?id=49592375)

**Background**: Smart TVs commonly use Automatic Content Recognition \(ACR\) to identify what users watch for ad targeting. However, LG&\#x27;s TVs have been found to go beyond this by actively recording ambient audio and scanning the home network, even when the screen is off. This transforms the TV into a surveillance device, not just a viewership tracker.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Automatic_content_recognition">Automatic content recognition - Wikipedia</a></li>
<li><a href="https://www.theprotec.com/blog/lg-smart-tv-privacy-standby-audio-network-scanning/">LG Smart TV Privacy: Standby Audio and Home Network Scanning</a></li>
<li><a href="https://digiday.com/future-of-tv/wtf-is-automatic-content-recognition/">WTF is automatic content recognition?</a></li>

</ul>
</details>

**Discussion**: The community is overwhelmingly critical, highlighting LG&\#x27;s invasive terms of service that require users to notify all guests about recording. Users share personal experiences of disabling network features, and some raise legal concerns about potential wiretap violations. A sense of vindication is common among those who previously refused to connect their TVs to the internet.

**Tags**: `#privacy`, `#smart-tv`, `#LG`, `#surveillance`, `#IoT`

---

<a id="item-2"></a>
## [Caltech Mathathon: First-ever AI Hackathon for Research Mathematics](https://mathathonchallenge.com/index.html) ⭐️ 8.0/10

Caltech undergraduates organized the first hackathon focused on applying AI to solve research-level mathematics problems, running as a 40-hour event. This event pioneers a new format for AI-assisted mathematical research, highlighting both the potential and the debate over using LLMs in serious math, while also reflecting student-driven efforts to fill gaps in AI education at institutions like Caltech. The hackathon is a 40-hour event, with organizers emphasizing responsible AI use. The format involves long model runtimes, which some critics note contrasts with traditional hackathon intensity.

hackernews · astroanax · Sep 7, 09:26 · [Discussion](https://news.ycombinator.com/item?id=49596055)

**Background**: Hackathons are short, intense events where participants collaborate on software projects. Research-level mathematics involves advanced problems that often require deep expertise. Recently, AI models like large language models have shown promise in assisting mathematicians by generating proofs or conjectures, but systematic integration into hackathons is new. This event merges these domains.

**Discussion**: The organizer hosted an AMA, clarifying the student-led nature and funding model. A Caltech graduate noted the weak CS department, explaining that the hackathon stems from a lack of AI learning opportunities. Some commenters criticized the format, arguing that waiting for LLM outputs for 40 hours contradicts the intense, collaborative spirit of hackathons and may not align with how AI math research is typically conducted.

**Tags**: `#hackathon`, `#mathematics`, `#AI`, `#research`, `#education`

---

<a id="item-3"></a>
## [Abusive Crawlers Consume 14 CPU Cores Rendering Git Commits on kernel.org](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 8.0/10

Konstantin Ryabitsev, maintainer of git.kernel.org, published a report detailing the resource drain from abusive crawlers. He revealed that at any given time, across five geo-distributed nodes, 14 CPU cores are devoted solely to rendering Git commits as HTML for scrapers, consuming more CPU cycles than all legitimate access combined. This issue underscores a growing threat to open-source infrastructure: poorly-behaved crawlers can waste precious computational resources, potentially threatening the availability of public services like code hosting. It also highlights the hidden costs of AI data collection for open-source maintainers. Among the 90 CPU cores distributed across five nodes, 14 to 16 cores are always occupied rendering HTML commits. The crawlers fetch commit pages that are rarely accessed by humans, and the rendering process is expensive because it involves generating diffs, syntax highlighting, and formatting. This wasteful load exceeds even the resources used for git clones, which are the primary legitimate use case.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org uses cgit, a fast web interface for Git repositories, to render commit pages as HTML. Rendering commits involves applying diffs, syntax highlighting, and formatting, which is CPU-intensive. Abusive crawlers, often associated with AI training data collection, indiscriminately scrape large numbers of pages, ignoring robots.txt and rate limits. The Linux kernel repository is one of the largest and most active open-source projects, making its infrastructure a visible target.

<details><summary>References</summary>
<ul>
<li><a href="https://securityonline.info/ai-crawlers-git-kernel/">AI Crawlers Strain git .kernel.org Servers</a></li>
<li><a href="https://wiki.archlinux.org/title/Cgit">cgit - ArchWiki</a></li>

</ul>
</details>

**Tags**: `#crawling`, `#git`, `#infrastructure`, `#web-scraping`, `#open-source`

---

<a id="item-4"></a>
## [OpenAI Chief Scientist: Build Powerful AI for Defense, but Avoid Recklessness](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 8.0/10

Jakub Pachocki, Chief Scientist at OpenAI, argued that developing increasingly capable AI models is essential for creating defensive systems against AI threats, but he cautioned that this rationale must not become an excuse for reckless acceleration. This statement from a leading AI lab&\#x27;s chief scientist underscores the high-stakes dilemma facing the industry: the need to rapidly advance AI for security and alignment, while simultaneously managing the existential risks of moving too fast. Pachocki specifically highlighted the need for aligned AI to secure infrastructure, protect against rogue AI agents in real time, and invent new protective measures, noting this will be a primary focus of OpenAI&\#x27;s deployment efforts.

rss · Simon Willison · Sep 7, 22:26

**Background**: AI alignment is the field of ensuring AI systems act in accordance with human intentions and values, preventing misaligned behaviors like reward hacking or strategic deception. Defensive AI refers to using AI to protect against next-generation cyber threats and other AI attacks. Rogue AI agents are autonomous systems that can exhibit unintended harmful behaviors, such as unauthorized data deletion or violating user instructions, which have been documented in real-world incidents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://blog.cloudflare.com/defensive-ai/">Defensive AI: Cloudflare’s framework for defending against next-gen threats | Cloudflare Blog</a></li>
<li><a href="https://www.notus.org/technology/rogue-ai-agents-hacks-alarming-researchers">Rogue AI Agents Are Alarming Researchers More Than Ever</a></li>

</ul>
</details>

**Tags**: `#ai-safety`, `#ai-ethics`, `#openai`, `#defensive-ai`, `#alignment`

---

<a id="item-5"></a>
## [Rustuna: High-Performance Rust Implementation of Optuna Released](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 8.0/10

Rustuna, a high-performance Rust reimplementation of the Optuna hyperparameter optimization framework, has been released with API compatibility, a reduced memory footprint, and zero Python dependencies. This release significantly improves the speed and security of hyperparameter tuning for production machine learning pipelines by eliminating Python dependency chains and reducing supply chain attack risks, aligning with the growing adoption of Rust in performance-critical ML infrastructure. Built in Rust, Rustuna leverages native memory management for lower memory usage and eliminates the Python runtime to mitigate supply chain attacks, while maintaining Optuna&\#x27;s familiar API.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is a popular open-source Python library for automatic hyperparameter tuning, developed by Preferred Networks, featuring a define-by-run API, trial pruning, and distributed optimization. Hyperparameter optimization is the process of systematically selecting optimal hyperparameters for a learning algorithm to maximize model performance. Rustuna reimplements Optuna&\#x27;s core in Rust, a systems programming language known for memory safety and high performance, to overcome the overhead of Python-based tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optuna">Optuna</a></li>
<li><a href="https://optuna.org/">Optuna - A hyperparameter optimization framework</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hyperparameter_optimization">Hyperparameter optimization</a></li>

</ul>
</details>

**Tags**: `#rust`, `#hyperparameter-optimization`, `#machine-learning`, `#optuna`, `#performance`

---

<a id="item-6"></a>
## [LLM-Guided Program Evolution Breaks 10 Circle-Packing Records for $28](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

An LLM-guided program evolution approach iteratively improved the best-known circle-packing solutions for 10 instances \(N=101–114\) on the Packomania csqv benchmark, achieving gains of 2.4–5.4% at a total LLM cost of $27.72. This work demonstrates that LLMs can serve as cost-effective creative engines for algorithm discovery, outperforming traditional optimization methods on a classic problem and opening new avenues for AI-driven scientific research. The system uses a scoreboard and history of prior attempts to guide LLM proposals, with an independent verifier ensuring only genuine improvements are retained. The plateau-detection stopping rule is noted as an area needing further critique.

reddit · r/MachineLearning · /u/SIGH\_I\_CALL · Sep 7, 16:54

**Background**: Circle packing is a classic optimization problem where the goal is to pack circles into a container \(here, maximize the sum of radii of N variable-radius circles in a unit square\). Packomania is a community-maintained catalog of best-known packings. Evolutionary programming is a technique where programs are mutated and selected for fitness. LLM-guided program evolution uses a large language model to propose modifications to code, which are then evaluated by a verifier.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.05093">[2609.05093] LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28</a></li>
<li><a href="https://www.packomania.com/csqv/csqv.html">The best known packings of variable-sized circles in a square with maximized sum of radii (complete up to N</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#program evolution`, `#optimization`, `#circle packing`, `#novel applications`

---

<a id="item-7"></a>
## [KV Cache as an Agent Runtime for Interactive LLM Systems](https://www.reddit.com/r/MachineLearning/comments/1w9myqc/kv_cache_as_an_agent_runtime_r/) ⭐️ 8.0/10

A research team proposes using the KV cache as an agent runtime, modifying the model&\#x27;s inference state to enable more interactive and responsive LLM systems. This approach builds on their prior work, &\#x27;Hogwild\! Inference&\#x27; and &\#x27;AsyncReasoning&\#x27;, and previews a Qwen3.8-27B agent playing DOOM interactively. This approach highlights inference design as an under-explored axis for agent capabilities, offering a middle ground between abstract harnesses and costly model modifications. It could enable more efficient, real-time interactions in LLM-powered agents and applications. The KV cache stores intermediate key and value vectors from previous tokens during autoregressive inference, enabling reuse and speedup. The proposed method modifies this cache state to achieve interactive behavior, as demonstrated in parallel generation \(Hogwild\! Inference\) and concurrent thinking \(AsyncReasoning\).

reddit · r/MachineLearning · /u/\_puhsu · Sep 7, 09:03

**Background**: The KV cache is an optimization in transformer-based language models that stores computed key and value vectors for past tokens during autoregressive text generation, avoiding redundant computation and speeding up inference. Hogwild\! Inference uses parallel LLM instances sharing the same attention cache to improve hardware utilization, while AsyncReasoning enables reasoning models to think and listen concurrently without training. The new proposal extends these ideas by treating the KV cache as a dynamic runtime state for agents, allowing interactive control of model behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>
<li><a href="https://arxiv.org/abs/2504.06261">Hogwild ! Inference : Parallel LLM Generation via Concurrent Attention</a></li>
<li><a href="https://www.alphaxiv.org/overview/2512.10931">Asynchronous Reasoning : Training-Free Interactive... | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#KV cache`, `#agent runtime`, `#inference`, `#interactive AI`

---

<a id="item-8"></a>
## [IEEE T-PAMI EIC Confirms Ghost Reviewer in Paper Rejection](https://www.reddit.com/r/MachineLearning/comments/1w9v43o/update_eic_confirmed_ghost_reviewerhow_to_get/) ⭐️ 8.0/10

The Editor-in-Chief of IEEE T-PAMI acknowledged that a ghost reviewer was involved in the rejection of a paper that had received &\#x27;Excellent&\#x27; scores from other reviewers. This incident directly undermines trust in the peer review process of a top machine learning journal, raising concerns about review integrity and the potential for unfair rejections. The paper received &\#x27;Excellent&\#x27; scores but was rejected; the EIC&\#x27;s confirmation suggests the ghost reviewer may have been unqualified or fabricated, leading to a flawed editorial decision.

reddit · r/MachineLearning · /u/cussealin · Sep 7, 15:22

**Background**: IEEE T-PAMI is a leading monthly journal in pattern analysis and machine intelligence, known for rigorous peer review. A ghost reviewer typically refers to a reviewer who did not actually perform the review or whose identity is not genuine, compromising the review process. The incident was revealed on Reddit, highlighting how social media can surface concerns in academic publishing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IEEE_PAMI">IEEE PAMI</a></li>

</ul>
</details>

**Tags**: `#peer review`, `#academic publishing`, `#machine learning`, `#IEEE T-PAMI`, `#ghost reviewer`

---

<a id="item-9"></a>
## [Interactive Map Charts LA Building Construction Dates from 1880 to 2026](https://lax-skyline.parcelscope.net/) ⭐️ 7.0/10

An interactive map visualizes the construction dates of existing buildings in Los Angeles, revealing the city&\#x27;s urban development patterns over nearly 150 years. The visualization sparked a discussion on data accuracy, survivorship bias, and the impact of zoning policies on housing affordability. The map offers a tangible view of LA&\#x27;s growth, highlighting the effects of historical downzoning and the resulting housing shortage. It serves as a tool for urban planners and residents to understand how policy decisions shape the built environment. The map uses public data from the LA County Assessor, but it only shows buildings that still exist, so older neighborhoods that have been completely rebuilt appear sparsely. The visualization spans from 1880 to 2026, including future projections.

hackernews · rustywasm · Sep 7, 18:52 · [Discussion](https://news.ycombinator.com/item?id=49601655)

**Background**: Los Angeles experienced significant downzoning in the 1980s, which restricted new construction and contributed to a chronic housing shortage. Building age data comes from county assessor records, which record the year each structure was built, but only for existing buildings. This leads to survivorship bias: areas with older construction dates that have been demolished and rebuilt are misrepresented as having only newer buildings. The interactive map is built using modern web mapping technologies like vector tiles.

**Discussion**: Commenters noted that the map shows surviving buildings&\#x27; ages, not original construction periods, leading to survivorship bias. Some criticized LA&\#x27;s downzoning for creating artificial housing scarcity, while others recalled the city&\#x27;s lost public transit network. A developer mentioned a similar past project using Mapbox GL, and the data source was identified as the LA County Assessor portal.

**Tags**: `#data visualization`, `#urban planning`, `#Los Angeles`, `#open data`, `#historical mapping`

---

<a id="item-10"></a>
## [Icy Moons: Hidden Ocean Worlds in Our Solar System](https://mceglowski.substack.com/p/icy-moons-are-ocean-worlds) ⭐️ 7.0/10

A new article provides a visually engaging synthesis of evidence that many icy moons in the solar system, including Europa, Enceladus, and Pluto, harbor subsurface liquid water oceans, transforming our understanding of habitable environments. This discovery expands the search for extraterrestrial life beyond Earth, positioning these ocean worlds as prime targets for future astrobiology missions and potentially reshaping planetary science and exploration priorities. The Europa Clipper mission, launched in 2024, will begin flybys in March 2031, while the Dragonfly rotorcraft is scheduled to arrive at Titan in 2034. However, a thick ice layer between the ocean and rocky interior may limit the direct water-rock contact needed for life.

hackernews · worldvoyageur · Sep 6, 13:07 · [Discussion](https://news.ycombinator.com/item?id=49586207)

**Background**: Over the past few decades, data from the Voyager, Galileo, Cassini, and New Horizons missions have revealed that icy moons such as Europa, Enceladus, and Titan harbor subsurface oceans, kept liquid by tidal heating from their host planets. These discoveries have shifted the focus of astrobiology from planets to moons.

**Discussion**: Commenters highlighted key upcoming mission dates \(Europa Clipper flybys in 2031, Dragonfly arriving at Titan in 2034\) and noted that the article omitted New Horizons&\#x27; contribution to Pluto&\#x27;s ocean discovery. Some discussed the extreme radiation on Europa&\#x27;s surface and the challenge of rock-water contact beneath ice.

**Tags**: `#space`, `#planetary-science`, `#astrobiology`, `#ocean-worlds`, `#science`

---

<a id="item-11"></a>
## [OpenAI Researchers&\#x27; Daily Spending on Coding Agents Soars](https://simonwillison.net/2026/Sep/6/research-acceleration-the-view-inside-openai/) ⭐️ 7.0/10

OpenAI&\#x27;s internal researchers are increasingly relying on AI coding agents, with median daily spending per researcher skyrocketing from near zero to about $600 by late August 2026, according to a newly released internal chart. This signals that AI-powered coding agents are becoming integral to cutting-edge AI research, potentially accelerating recursive self-improvement loops and reshaping how AI companies develop future models. The chart shows a plateau around $150–165 through July, followed by a steep climb to roughly $600 in late August, which Simon Willison speculates may coincide with internal access to GPT-6 Astra. The report uses the term &\#x27;RSI&\#x27; \(Recursive Self-Improvement\) without expansion.

rss · Simon Willison · Sep 6, 23:57

**Background**: Agentic engineering is an emerging practice where autonomous AI agents handle coding tasks under human direction. Recursive self-improvement \(RSI\) refers to the hypothetical process where AI systems rewrite their own code, potentially leading to an intelligence explosion. Coding agents apply generative AI to software development, and their rapid adoption within OpenAI illustrates how AI is being used to accelerate AI research itself.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>

</ul>
</details>

**Tags**: `#ai`, `#openai`, `#agents`, `#coding`, `#research`

---

<a id="item-12"></a>
## [Report: 10-20% of New gTLD Registrations Are Scams](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 7.0/10

A blog post by Terence Eden, highlighted by Simon Willison, reveals that an Interisle report found 10-20% of newly registered generic top-level domains \(gTLDs\) in 2025 were scams, with 8.5 million of the 85 million new registrations added to blocklists within months. This statistic exposes a critical failure in domain name governance, as the DNS—a foundational internet infrastructure—is being exploited at an alarming scale for scams, phishing, and malware, threatening user safety and trust in the entire web ecosystem. The Interisle report analyzed 85 million new gTLD registrations in 2025; by May 2025, 8.5 million were already on security blocklists, indicating a minimum abuse rate of 10%, with the actual rate likely closer to 20% due to underreporting by blocklists.

rss · Simon Willison · Sep 6, 14:40

**Background**: The Domain Name System \(DNS\) translates human-readable domain names into IP addresses, enabling website access. Generic top-level domains \(gTLDs\) are the suffixes like .com, .org, and newer ones introduced after ICANN&\#x27;s expansion in 2012, such as .shop and .online. ICANN is the organization that coordinates DNS and domain name allocation globally. DNS blocklists are real-time lists used by security tools to filter out malicious domains, often employed by email providers and web browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generic_top-level_domain">Generic top-level domain - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ICANN">ICANN</a></li>
<li><a href="https://en.wikipedia.org/wiki/DNS_Blacklist">DNS Blacklist</a></li>

</ul>
</details>

**Tags**: `#DNS`, `#cybersecurity`, `#domain abuse`, `#scams`, `#internet governance`

---

<a id="item-13"></a>
## [Simon Willison Warns Against Rewriting Codebases from Scratch](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 7.0/10

Simon Willison shared his experience that rewriting a software system from scratch rarely succeeds, as the old system remains a moving target and the new team faces unrealistic expectations, often leading to two parallel systems. This insight is crucial for software teams dealing with technical debt; it challenges the common instinct to &\#x27;burn it down&\#x27; and highlights a more practical approach of incremental refactoring and testing. Willison references Will Larson&\#x27;s article &\#x27;Migrations: the sole scalable fix to tech debt&\#x27; and recommends shoring up legacy systems with automated testing and targeted refactors instead of starting over.

rss · Simon Willison · Sep 6, 09:08

**Background**: The original discussion on Lobste.rs was inspired by Zach Kehs&\#x27;s article &\#x27;There&\#x27;s No Limit to How Bad Code Can Get,&\#x27; which argues that unlike physical structures, software can endlessly accumulate complexity and technical debt. Rewrites often seem appealing when a codebase becomes unmaintainable, but they frequently fail due to the moving target of the existing system and the knowledge gap between the old and new teams. Technical debt refers to the implied cost of future refactoring incurred by prioritizing quick delivery over clean code.

**Tags**: `#software engineering`, `#technical debt`, `#rewrite`, `#code quality`, `#best practices`

---

<a id="item-14"></a>
## [Tiny recurrent network generates full Bad Apple video from single initial state](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/) ⭐️ 7.0/10

A compact 417k-parameter LSTM-style recurrent neural network has been trained to memorize the entire 6,500-frame Bad Apple animation and autonomously generate the full video sequence, starting from a single pair of 64-dimensional latent vectors without any timestamp inputs during inference. It demonstrates that a tiny recurrent dynamical system can learn a long, stable trajectory in latent space, enabling efficient autonomous video generation. The training techniques for long-horizon stability offer practical insights for building compact generative models under resource constraints. The model uses a 64D hidden state and a 64D memory cell, with a 4-gate LSTM-style transition \(16,640 parameters\) and a depthwise-separable convolutional decoder \(400,361 parameters\). Training employed a curriculum of rollout horizons from 2 to 512 frames, latent teacher tables, state perturbation noise, and second-difference acceleration regularization, enabling stable rollouts that far exceed the training horizon.

reddit · r/MachineLearning · /u/SEBADA321 · Sep 8, 00:05

**Background**: Bad Apple\!\! is a classic monochrome silhouette animation from the Touhou Project, often used as a benchmark for video compression and generation. SIREN \(Sinusoidal Representation Networks\) are coordinate‑based MLPs that can implicitly memorize signals like images or videos; a previous work used a SIREN to map \(t, y, x\) to pixel values. This project instead uses a recurrent dynamical system, a neural network that evolves its state over time, to learn the temporal dynamics in latent space without explicit time coordinates. The approach builds on concepts from recurrent neural network dynamical systems, a field that models sequences as continuous-time trajectories.

<details><summary>References</summary>
<ul>
<li><a href="https://openreview.net/pdf?id=ZZ94aLbMOK">Recurrent neural network dynamical systems</a></li>

</ul>
</details>

**Tags**: `#recurrent neural networks`, `#dynamical systems`, `#video generation`, `#latent space`, `#memorization`

---

<a id="item-15"></a>
## [ML Reproducibility Declining Due to Hardware, Secrecy, and Cherry-Picked Demos](https://www.reddit.com/r/MachineLearning/comments/1w92eis/reproducibility_seems_to_be_headed_towards/) ⭐️ 7.0/10

A Reddit discussion argues that reproducibility in machine learning research is becoming a lost cause, driven by expensive hardware for physical AI, unverifiable corporate claims, and researchers cherry-picking demos that only show successes. This highlights a growing crisis in scientific integrity, potentially undermining trust in ML research and slowing progress if results cannot be independently verified, especially as the field moves toward physical AI and closed-source models. The post identifies three main drivers: physical AI experiments requiring costly labs and hardware, big AI companies releasing unverifiable tools, and researchers cherry-picking working demos while hiding failures, compounded by incentives to avoid sharing code.

reddit · r/MachineLearning · /u/NeighborhoodFatCat · Sep 6, 17:29

**Background**: Physical AI refers to AI systems that interact with the physical world, often combining models with sensors, actuators, and robots, as defined by NVIDIA, IBM, and Wikipedia. Reproducibility in ML has long been a concern, but the increasing scale of models and hardware costs, along with corporate secrecy, have intensified the issue. The Reddit post reflects broader debates about open science versus proprietary interests in AI development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Physical_artificial_intelligence">Physical artificial intelligence - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/generative-physical-ai/">What is Physical AI? | NVIDIA Glossary</a></li>
<li><a href="https://www.ibm.com/think/topics/physical-ai">What is Physical AI? | IBM</a></li>

</ul>
</details>

**Tags**: `#reproducibility`, `#machine learning`, `#research ethics`, `#physical AI`, `#community discussion`

---

<a id="item-16"></a>
## [Longitudinal Benchmarking Reveals LLM Performance Drift in API Models](https://www.reddit.com/r/MachineLearning/comments/1w9llr4/measuring_llm_performance_drift_observations_and/) ⭐️ 7.0/10

A new methodology uses 31,352 repeated benchmark measurements across 49 models to detect performance drift in API-served LLMs, finding a 3:1 ratio of between-day to within-day variability. The paper proposes versioned, execution-based evaluation and change detection on time series rather than static leaderboard snapshots. API-served LLMs can change silently without version bumps, undermining reliability for downstream applications. This longitudinal approach shifts benchmarking from a one-time race to continuous monitoring, crucial for production deployment. The study observed a within-day standard deviation of 2.80 points and a between-day daily median standard deviation of 8.43 points across 31,352 score observations. Methodology includes versioned benchmark configurations, execution-based evaluation \(not LLM judge\), tracking serving metadata, and separating availability failures from capability changes.

reddit · r/MachineLearning · /u/ionutvi · Sep 7, 07:44

**Background**: LLM benchmarks like MMLU or HumanEval typically evaluate models at a single point in time, producing a leaderboard. However, API-served models \(e.g., from OpenAI, Anthropic\) can be updated by providers without notifying users, leading to &\#x27;model drift&\#x27; where behavior changes. Performance drift is a known issue in machine learning where model accuracy degrades due to data distribution shifts, but in LLMs it can also stem from infrastructure or configuration changes. This work frames benchmarking as a longitudinal measurement problem, similar to monitoring in production ML systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Language_model_benchmark">Language model benchmark - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/posts/alithm_machinelearning-mlops-aiengineering-activity-7439921091621543936-WTey">ML Model Retraining: When to Act on Performance Drift | LinkedIn</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11217161/">Authors’ Response to Peer Reviews of “ Performance Drift in Machine ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmarking`, `#performance drift`, `#monitoring`, `#API models`

---

<a id="item-17"></a>
## [Mercator ↔ Equal Earth: Interactive D3 Animated Map Transition](https://simonwillison.net/2026/Sep/7/equal-earth/) ⭐️ 6.0/10

Simon Willison used GPT-6 Astra to create an interactive web tool that animates the transition between the Mercator and Equal Earth map projections, highlighting the visual distortion of the Mercator projection. The tool is available at tools.simonwillison.net/equal-earth and was prompted by the UN&\#x27;s recent vote encouraging the use of equal-area projections. The tool visually exposes the well-known size distortion of the Mercator projection, where Greenland appears larger than Africa, and demonstrates the equal-area Equal Earth projection as an accurate alternative. Combined with the UN&\#x27;s September 2026 resolution, it underscores the growing push for more truthful map representations in education and technology, while also showcasing how AI can rapidly prototype such visualizations. The animation is built with D3.js, a JavaScript library for data-driven documents, and was generated by GPT-6 Astra \(medium\) via ChatGPT Work. The Equal Earth projection, invented in 2018, is an equal-area pseudocylindrical projection specifically mentioned in the UN resolution.

rss · Simon Willison · Sep 7, 16:24

**Background**: Map projections transform the 3D Earth onto a 2D plane. The Mercator projection \(1569\) preserves angles for navigation but drastically inflates areas near the poles, making Greenland look as large as Africa. The Equal Earth projection \(2018\) is an equal-area projection that maintains the correct relative sizes of landmasses. In September 2026, the United Nations General Assembly voted to encourage the adoption of equal-area projections like Equal Earth in educational and technological applications. D3.js is a widely used JavaScript library for creating interactive visualizations on the web.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Equal_Earth_map_projection">Equal Earth map projection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mercator_projection">Mercator projection</a></li>
<li><a href="https://en.wikipedia.org/wiki/D3.js">D3.js</a></li>

</ul>
</details>

**Tags**: `#geospatial`, `#map projections`, `#data visualization`, `#AI-assisted development`, `#D3`

---

<a id="item-18"></a>
## [PINNStudio Brings No-Code GUI to Physics-Informed Neural Networks](https://www.reddit.com/r/MachineLearning/comments/1w9a2i7/pinnstudio_a_free_opensource_nocode_gui_for/) ⭐️ 6.0/10

A developer has released PINNStudio, a free and open-source no-code GUI that automatically generates DeepXDE-based code for defining, training, and visualizing physics-informed neural networks \(PINNs\). It supports 1D/2D domains, coupled PDE systems, forward and inverse problems, and includes built-in templates for classic equations. By eliminating the need to write boilerplate code, PINNStudio lowers the barrier for students and researchers with limited coding experience, enabling them to focus on physics rather than implementation. This can accelerate experimentation and prototyping in scientific machine learning, where setting up PINN problems is often repetitive and error-prone. The tool is built on DeepXDE, a popular PINN library, and provides features like custom training schedules, live loss curves, solution plots, and templates for Heat, Allen-Cahn, and Cahn-Hilliard equations. It can be installed via pip and is available on GitHub under the MIT license.

reddit · r/MachineLearning · /u/Impossible-Jello2749 · Sep 6, 22:19

**Background**: Physics-informed neural networks \(PINNs\) are neural networks that incorporate physical laws, typically described by partial differential equations \(PDEs\), into their training process. This allows them to solve forward and inverse problems with limited data, making them valuable for engineering and scientific applications. DeepXDE is a widely used open-source library for building and training PINNs, but it still requires users to write Python code to set up problems. PINNStudio provides a graphical interface on top of DeepXDE, automating code generation and visualization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Physics-informed_neural_networks">Physics-informed neural networks</a></li>
<li><a href="https://www.mathworks.com/discovery/physics-informed-neural-networks.html">What Are Physics-Informed Neural Networks (PINNs)? - MATLAB &amp; Simulink</a></li>

</ul>
</details>

**Tags**: `#PINN`, `#scientific machine learning`, `#no-code`, `#GUI`, `#open-source`

---