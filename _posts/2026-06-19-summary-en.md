---
layout: default
title: "Horizon Summary: 2026-06-19 (EN)"
date: 2026-06-19
lang: en
---

> From 43 items, 22 important content pieces were selected

---

1. [10k GitHub Repositories Found Distributing Trojan Malware Targeting AI Coding Agents](#item-1) ⭐️ 9.0/10
2. [Elkjop Fined €1.8M for GDPR Forced Consent Violation](#item-2) ⭐️ 8.0/10
3. [Hospitals and Universities Repurpose Drugs for 90% Lower Costs](#item-3) ⭐️ 8.0/10
4. [Tool Reveals How Much LLMs Remember About You](#item-4) ⭐️ 8.0/10
5. [Transformer Co-Author Noam Shazeer Leaves Google Gemini for OpenAI](#item-5) ⭐️ 8.0/10
6. [Beyond .gitignore: Global Excludes and .gitattributes for Git Ignore](#item-6) ⭐️ 8.0/10
7. [Modos Flow Monitor Pushes Color E-Paper to 60Hz and 3200x2400](#item-7) ⭐️ 8.0/10
8. [GLM-5.2 Released: 753B Open Weights LLM with 1M Context](#item-8) ⭐️ 8.0/10
9. [Charity Majors: AI Made Code Free and Instant, Upending Economics](#item-9) ⭐️ 8.0/10
10. [Safe GPU inference in Rust rivals vLLM/SGLang with cuTile Rust](#item-10) ⭐️ 8.0/10
11. [Ubiquiti Announces Enterprise NAS Built on ZFS](#item-11) ⭐️ 7.0/10
12. [Cornell CS 6120: Self-Guided Advanced Compilers Course](#item-12) ⭐️ 7.0/10
13. [W Social Criticized as Profit-Driven, Shady EU Digital Sovereignty Project](#item-13) ⭐️ 7.0/10
14. [Datasette Apps: Host Custom HTML Applications Inside Datasette](#item-14) ⭐️ 7.0/10
15. [Simon Willison's <click-to-play> Web Component Defers GIF Loading Until Click](#item-15) ⭐️ 7.0/10
16. [Conversation-level debugging reveals voice AI flaws that isolated benchmarks miss](#item-16) ⭐️ 7.0/10
17. [Microsoft Research's Next-Latent Prediction for Self-Supervised Transformers](#item-17) ⭐️ 7.0/10
18. [Swiss Parliament Lifts Ban on New Nuclear Power Plants](#item-18) ⭐️ 6.0/10
19. [datasette-acl 0.6a0 Expands from Table-Only to General Resource Sharing](#item-19) ⭐️ 6.0/10
20. [Speculative Decoding Spotlight: SGLang's Latest Latency Advances](#item-20) ⭐️ 6.0/10
21. [Balancing Probe and Network Capacity: Seeking Theoretical Guarantees for Probing](#item-21) ⭐️ 6.0/10
22. [Contrastive Targeted SFT Proposed as Mechanistic Interpretability Method to Map Causal Dependencies](#item-22) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [10k GitHub Repositories Found Distributing Trojan Malware Targeting AI Coding Agents](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

An investigation uncovered approximately 10,000 GitHub repositories actively distributing Trojan malware, with evidence suggesting they are specifically designed to infect AI coding agents and automated dependency-resolution systems. The malicious repos use rapid commit cycles and impersonation of legitimate projects to appear in agent-driven searches. This represents a novel supply chain attack vector that exploits the explosive growth of AI coding agents, which autonomously fetch and integrate code dependencies. If successful, such attacks could compromise developer environments, steal credentials, and seed malware into downstream software at scale. The malicious repositories often clone legitimate projects, then delete and push a new commit every few hours to stay atop 'Last Updated' searches, exactly targeting the behavior of AI agents that look for fresh dependencies. The Trojan payloads are likely designed for credential theft or further infection, and the campaign appears focused on exploiting the automated trust relationships in modern development pipelines.

hackernews · theorchid · Jun 18, 11:45 · [Discussion](https://news.ycombinator.com/item?id=48583928)

**Background**: AI coding agents, such as Cursor, Claude Code, and Devin, can autonomously write, modify, and manage code across entire projects, often pulling dependencies directly from GitHub. A supply chain attack compromises a less-secure element in the software supply chain—such as a library or repository—to inject malware into a wider ecosystem. The recent proliferation of AI agents has created a new attack surface where automated decisions replace human oversight, making it easier for malicious packages to slip through.

<details><summary>References</summary>
<ul>
<li><a href="https://agentic.ai/best/coding-agents">18 Best AI Coding Agents in 2026 — Agentic.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack</a></li>

</ul>
</details>

**Discussion**: Commenters highlighted that the attack pattern—cloning only new repos, frequent commits—is tailored to AI agents, not humans, and some shared personal experiences of their own projects being impersonated. The discussion also referenced a real-world incident where a Disney engineer downloaded a malicious AI tool from GitHub, underscoring the tangible risk. Overall sentiment is one of alarm about this emerging threat vector.

**Tags**: `#security`, `#malware`, `#github`, `#supply-chain-attack`, `#AI-agents`

---

<a id="item-2"></a>
## [Elkjop Fined €1.8M for GDPR Forced Consent Violation](https://www.thatprivacyguy.com/blog/elkjop-forced-consent-fine/) ⭐️ 8.0/10

A privacy advocate's complaint resulted in a €1.8 million GDPR fine against Norwegian electronics retailer Elkjop for forcing customers to consent to marketing in order to join its customer club. The decision, issued five years after the complaint, confirms that such forced consent is unlawful. This case sets a strong precedent that bundling consent with a service violates GDPR, reinforcing that consent must be freely given. It may deter other companies from similar practices and empower individuals to challenge forced consent. The €1.8 million fine was imposed by the Norwegian Data Protection Authority (Datatilsynet) after a five-year investigation, and the decision also addressed other GDPR violations. The company's own statement that membership was conditional on receiving marketing was central to the case.

hackernews · speckx · Jun 18, 18:31 · [Discussion](https://news.ycombinator.com/item?id=48589501)

**Background**: The GDPR, enforced since May 2018, requires that consent for data processing be freely given. Article 7(4) specifically prohibits making a service conditional on consent unrelated to the service's core function. This 'forced consent' or 'bundling' has been a focus of privacy advocates, with early complaints against tech giants like Google and Facebook.

<details><summary>References</summary>
<ul>
<li><a href="https://gdpr-info.eu/issues/consent/">Consent - General Data Protection Regulation ( GDPR )</a></li>
<li><a href="https://martech.org/gdpr-day-1-google-and-facebook-sued-for-forced-consent/">GDPR day 1: Google and Facebook sued for ' forced consent '</a></li>

</ul>
</details>

**Discussion**: Community members applauded the outcome, noting the Norwegian DPA's consistent user-centric approach, but expressed frustration with the five-year delay. Some observed that asserting privacy rights in the US often puts individuals at a disadvantage, contrasting with the EU's enforcement.

**Tags**: `#GDPR`, `#privacy`, `#data-protection`, `#consent`, `#enforcement`

---

<a id="item-3"></a>
## [Hospitals and Universities Repurpose Drugs for 90% Lower Costs](https://www.kcl.ac.uk/news/hospitals-and-universities-repurposing-drugs-at-90-lower-cost) ⭐️ 8.0/10

A recent report from King's College London highlights how hospitals and universities are repurposing existing approved drugs for new indications, achieving cost reductions of up to 90%. Community examples include using the cancer drug bevacizumab (Avastin) for macular degeneration instead of the far more expensive ranibizumab (Lucentis), accelerating rare disease therapies, and exposing patent manipulation around ketamine. This widespread off-label repurposing challenges the high pricing of specialized drugs and highlights systemic incentives that prioritize profits over affordable care. It directly improves access to life-changing treatments, especially for rare disease patients and those facing high out-of-pocket costs, and pressures regulators to reconsider pathways for approving new uses of old drugs. Avastin and Lucentis are molecularly identical, yet Avastin costs ~$50/dose versus Lucentis at ~$1,500/dose. Ketamine, an off-patent anesthetic, has been modified into esketamine (Spravato) to obtain a new patent, despite evidence that esketamine may be less effective than generic ketamine. Regulatory barriers prevent expanding labeled indications for existing drugs without manufacturer consent, limiting formal repurposing.

hackernews · giuliomagnifico · Jun 18, 10:33 · [Discussion](https://news.ycombinator.com/item?id=48583386)

**Background**: Drug repurposing (or repositioning) involves finding new therapeutic uses for existing medications, a faster and cheaper path than developing new drugs because safety profiles are already established. Bevacizumab (Avastin), originally approved for cancer, is widely used off-label for wet age-related macular degeneration because it targets the same VEGF pathway as the approved eye drug ranibizumab (Lucentis). Ketamine, a decades-old anesthetic, has rapid antidepressant effects, but its manufacturer developed a patented derivative (esketamine) to maintain exclusivity and high prices. Rare disease communities often rely on repurposing because the small patient populations make new drug development commercially unattractive.

<details><summary>References</summary>
<ul>
<li><a href="https://www.healthline.com/health/drugs/lucentis-vs-avastin">Lucentis vs. Avastin: Is One of Them Right for You? - Healthline</a></li>
<li><a href="https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2024.1352803/full">Drug repurposing for rare: progress and opportunities for the rare disease community - Frontiers</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/33563480/">Drug Repurposing for Rare Diseases - PubMed</a></li>

</ul>
</details>

**Discussion**: Commenters shared real-world examples: atourgates detailed the Avastin/Lucentis cost disparity; jawns highlighted the nonprofit Cures Within Reach repurposing drugs for rare diseases like Huntington's; dabinat criticized the Spravato patent manipulation and lower efficacy; functionmouse linked to an article on Revlimid pricing; oezi noted that regulatory pathways block repurposing without manufacturer involvement. Overall, the discussion praised repurposing's potential but condemned the misaligned incentives that hinder it.

**Tags**: `#drug-repurposing`, `#healthcare-costs`, `#pharmaceuticals`, `#policy`, `#rare-diseases`

---

<a id="item-4"></a>
## [Tool Reveals How Much LLMs Remember About You](https://www.intheweights.com/) ⭐️ 8.0/10

A developer built a website that checks how strongly multiple frontier and small language models recognize a person's name, querying them in parallel and clustering responses to show the extent of personal data memorized from training data. This tool exposes the privacy implications of LLM training, showing that models have absorbed personal information from web scraping without explicit consent, raising concerns about data usage and the right to be forgotten. The site queries models in parallel, clusters responses, and calculates a recognition strength score. It covers both cutting-edge frontier models like GPT-4 and smaller open-source ones, and even includes a comparison with hallucinated responses.

hackernews · turtlesoup · Jun 18, 20:49 · [Discussion](https://news.ycombinator.com/item?id=48591348)

**Background**: Frontier models are the most advanced large language models, often closed-source and cloud-based, trained on vast internet data. LLM memorization refers to the phenomenon where models store verbatim or near-verbatim fragments of their training data, which can include personal information, leading to privacy risks. This tool probes that memorization for individuals.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>
<li><a href="https://arxiv.org/html/2507.05578v1">The Landscape of Memorization in LLMs: Mechanisms,</a></li>

</ul>
</details>

**Discussion**: Comments reveal both fascination and unease: some users found their names strongly recognized, while others warned against using real names. One example showed a hallucination from a small model, misidentifying a person. The discussion highlighted the lack of consent in data scraping and the surprising permanence of online traces in AI models.

**Tags**: `#LLM`, `#privacy`, `#training-data`, `#web-scraping`, `#data-recognition`

---

<a id="item-5"></a>
## [Transformer Co-Author Noam Shazeer Leaves Google Gemini for OpenAI](https://twitter.com/NoamShazeer/status/2067400851438932297) ⭐️ 8.0/10

Noam Shazeer, a co-author of the groundbreaking 2017 paper 'Attention Is All You Need,' has resigned from his position as co-lead of Google's Gemini team to join OpenAI. The move was confirmed on June 18, 2026, marking a significant shift in AI talent. His departure highlights the fierce competition for elite AI researchers between tech giants, and his deep expertise in transformer architectures could significantly influence OpenAI's future model development. Shazeer had rejoined Google in 2024 through a $2.7 billion licensing deal with Character.AI, a company he co-founded, and was appointed co-lead of Gemini shortly after. His departure after roughly a year raises questions about the internal dynamics at Google.

hackernews · lukasgross · Jun 18, 00:26 · [Discussion](https://news.ycombinator.com/item?id=48578913)

**Background**: The transformer architecture, introduced in 2017, revolutionized natural language processing by enabling parallel processing of sequential data and became the backbone of large language models. Shazeer, a veteran Google engineer since 2000, was instrumental in its development. He left Google in 2021 to co-found Character.AI, a conversational AI startup, before returning in 2024 through a major licensing deal.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Attention_Is_All_You_Need">Attention Is All You Need - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_architecture">Transformer architecture</a></li>

</ul>
</details>

**Discussion**: The community expresses deep respect for Shazeer's technical contributions, with many calling him a 'legend' at Google. There is considerable surprise and speculation about his rapid departure from Gemini after the high-profile return, with some linking to rumors of internal friction. Overall, sentiment is one of excitement and curiosity about the implications for the AI race.

**Tags**: `#AI`, `#transformers`, `#OpenAI`, `#Google`, `#personnel`

---

<a id="item-6"></a>
## [Beyond .gitignore: Global Excludes and .gitattributes for Git Ignore](https://nelson.cloud/.gitignore-isnt-the-only-way-to-ignore-files-in-git/) ⭐️ 8.0/10

An article explains multiple ways to ignore files in Git beyond .gitignore, including per-repo .git/info/exclude and global core.excludesFile, and community comments highlight using .gitattributes to suppress diffs for noise files like package-lock.json. These techniques help developers keep repositories clean without polluting project .gitignore with personal or environment-specific files, and reduce noise in code reviews by suppressing irrelevant diffs, improving productivity for teams. The global ignore file can be set via git config --global core.excludesFile, and .gitattributes can use the 'diff' attribute to treat files as binary (suppressing textual diffs) or specific patterns to collapse diffs. The per-repo .git/info/exclude is not committed, but must be recreated per clone.

hackernews · FergusArgyll · Jun 18, 10:29 · [Discussion](https://news.ycombinator.com/item?id=48583356)

**Background**: Git's .gitignore is a file listing patterns to tell Git which files to ignore in a repository. However, the .gitignore file is shared with all collaborators, so adding personal editor or OS files (like .DS_Store) can pollute it. Git also provides a per-repo exclude file at .git/info/exclude that is not shared, and a global ignore file that ignores files across all repositories on a user's machine. The .gitattributes file controls how Git handles certain files, including diff behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://jumptuck.com/blog/2020-11-25-git-core-excludes/">Quick Tip: Git Global Exclude File - Jumptuck</a></li>
<li><a href="https://gist.github.com/subfuzion/db7f57fff2fb6998a16c">Global gitignore · GitHub</a></li>
<li><a href="https://git-scm.com/docs/gitattributes">Git - gitattributes Documentation</a></li>

</ul>
</details>

**Discussion**: Commenters enthusiastically shared additional tips: hungryhobbit recommended .gitattributes for suppressing diffs of noise files like package-lock.json; kevincox emphasized the global exclude to avoid polluting project .gitignore; hk1337 pointed out the proper XDG-compliant config path ~/.config/git/ignore; judofyr suggested an 'attic' directory globally ignored as a scratch space; dofm noted that global excludes are user-specific and not shared, so OS-specific files like .DS_Store still need per-user discipline.

**Tags**: `#git`, `#version control`, `#developer tools`, `#productivity`, `#tips`

---

<a id="item-7"></a>
## [Modos Flow Monitor Pushes Color E-Paper to 60Hz and 3200x2400](https://spectrum.ieee.org/modos-e-paper-monitor) ⭐️ 8.0/10

Modos, a two-person startup, is developing the Flow, a 13.3-inch color e-paper monitor with a native resolution of 3200x2400, a 60Hz refresh rate, and touch input—a breakthrough combination that far exceeds the specifications of most existing e-paper displays. This leap in responsiveness and resolution makes e-paper viable for general-purpose desktop use, significantly reducing eye strain and power consumption compared to traditional LCD monitors, and opening the door to a new class of auxiliary, outdoor-usable, and eye-friendly devices. The monitor leverages a custom FPGA-driven timing controller and open-hardware design to achieve sub-100ms latency. While the 60Hz rate is impressive, some community members raised concerns about the possible impact on the e-paper panel's longevity, as the physical ink particles may degrade faster with frequent rapid switching.

hackernews · Vinnl · Jun 18, 11:41 · [Discussion](https://news.ycombinator.com/item?id=48583897)

**Background**: E-paper is a reflective display technology that mimics ink on paper, consuming very low power and remaining readable in direct sunlight. Historically, it has been limited to slow refresh rates and monochrome or limited color, confining it mostly to e-readers. Recent advances like E Ink's Kaleido and Gallery panels have introduced color, but general-purpose computing still demanded faster response. Modos, a startup focused on technology that respects user attention, previously worked on open-source e-paper controllers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.modos.tech/">Home | Modos</a></li>
<li><a href="https://www.embedsbc.com/modos-flow-open-hardware-60hz-epaper-monitor/">Modos Flow Open-Hardware E - Paper Monitor: 60 Hz High-Refresh...</a></li>
<li><a href="https://spectrum.ieee.org/e-paper-display-modos">E - Paper Display Refresh Rate Reaches New Heights - IEEE Spectrum</a></li>

</ul>
</details>

**Discussion**: Comments are enthusiastic, with many calling the specs 'mighty' and 'impressive' and relating it to upcoming devices like the Daylight tablet. Some users question panel longevity at 60Hz and wonder about practical use cases for a standalone e-ink monitor, while others see it as a step toward always-on, eye-friendly auxiliary screens.

**Tags**: `#e-paper`, `#display technology`, `#hardware`, `#monitor`, `#color e-ink`

---

<a id="item-8"></a>
## [GLM-5.2 Released: 753B Open Weights LLM with 1M Context](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 8.0/10

Z.ai released GLM-5.2, a 753B parameter text-only LLM with Mixture of Experts, under MIT license, featuring a 1 million token context window and top benchmark scores; the model weights were made fully open on June 16th after an initial subscriber release. GLM-5.2 sets a new bar for open weights language models, topping the Artificial Analysis Intelligence Index and offering competitive pricing, which could accelerate innovation and accessibility in AI development. GLM-5.2 uses significantly more output tokens (43k per task) than comparable models, and despite being text-only, it achieved second place on the Code Arena WebDev leaderboard; the model weights occupy 1.51TB.

rss · Simon Willison · Jun 17, 23:58

**Background**: Open weights models provide the trained parameters for anyone to use, modify, and distribute, often under permissive licenses like MIT, but they may not include training data or code. Mixture of Experts (MoE) is an architecture where only a small fraction of the model's total parameters (the 'experts') are activated for each input, reducing computational cost while maintaining high capacity. The context window defines the amount of text the model can consider at once; 1 million tokens allows processing of very long documents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#LLM`, `#AI`, `#machine learning`, `#GLM-5.2`

---

<a id="item-9"></a>
## [Charity Majors: AI Made Code Free and Instant, Upending Economics](https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything) ⭐️ 8.0/10

Charity Majors, in a post shared by Simon Willison, stated that 2025 turned the economics of code production upside down, making code generation effectively free and instant, and transforming code from a treasured asset into a disposable commodity. This shift dramatically lowers the barrier to creating software, forces teams to rethink practices around code review and technical debt, and emphasizes that the real value now lies in engineering discipline rather than in the code itself. Majors highlights that the cost of generating code has plummeted, but the need for rigorous testing, clear architecture, and deep understanding remains critical because bad code, even if generated instantly, can still cause significant harm.

rss · Simon Willison · Jun 17, 17:12

**Background**: Traditionally, software development was a labor-intensive process where writing code was time-consuming and expensive, making each line valuable. In recent years, AI-powered coding assistants like GitHub Copilot and large language models have advanced rapidly, allowing developers to generate code from natural language prompts. By 2025, these tools reached a tipping point where code generation became nearly instantaneous and cost-free, altering the fundamental economics of software. Charity Majors, a prominent engineering leader and CTO, is known for her insights on observability and software practices.

**Tags**: `#charity-majors`, `#ai-assisted-programming`, `#generative-ai`, `#software-engineering`, `#economics`

---

<a id="item-10"></a>
## [Safe GPU inference in Rust rivals vLLM/SGLang with cuTile Rust](https://www.reddit.com/r/MachineLearning/comments/1u9j7md/fearless_concurrency_on_the_gpu_safe_gpu/) ⭐️ 8.0/10

cuTile Rust extends Rust's ownership and borrow checking to GPU kernels, ensuring compiler-verified memory safety and data-race freedom. The team built Grout, an inference engine for Qwen3 models, which achieves 171 tok/s on an RTX 5090 for Qwen3-4B and 82 tok/s on a B200 for Qwen3-32B at batch-1 decode, matching vLLM and SGLang performance. As AI-generated GPU code becomes more common, the bottleneck shifts from writing code to trusting it. cuTile Rust provides a verifiable target for generated kernels, reducing bugs and enabling safe, high-performance GPU programming without sacrificing speed. The library is tile-based and lowers to CUDA Tile IR, a new virtual ISA. While Grout currently uses some unsafe kernels, the safe GEMM is within 0.3% of a hand-written low-level version and element-wise ops hit ~7 TB/s. It is NVIDIA-only, batch-1, and GEMM slightly trails cuBLAS at some sizes.

reddit · r/MachineLearning · /u/Exciting_Suspect9088 · Jun 18, 21:36

**Background**: CUDA Tile IR is a virtual instruction set architecture introduced in CUDA 13.1 that shifts GPU programming from thread-level SIMT to tile-based operations. Rust's ownership model enforces memory safety at compile time, preventing common bugs like use-after-free and data races. vLLM and SGLang are popular high-performance LLM inference engines, and Qwen3 is a series of large language models. cuTile Rust leverages these concepts to bring safe, high-level abstractions to GPU kernels.

<details><summary>References</summary>
<ul>
<li><a href="https://nvlabs.github.io/cutile-rs/">cuTile Rust — cuTile Rust</a></li>
<li><a href="https://github.com/nvlabs/cutile-rs">GitHub - NVlabs/ cutile -rs: cuTile Rust provides a safe, tile-based...</a></li>
<li><a href="https://www.buysellram.com/blog/cuda-13-1-reinvents-gpu-development-the-biggest-leap-in-two-decades/">CUDA 13.1 Reinvents GPU Development — The Biggest Leap in Two Decades - BuySellRam</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#GPU`, `#CUDA`, `#LLM inference`, `#memory safety`

---

<a id="item-11"></a>
## [Ubiquiti Announces Enterprise NAS Built on ZFS](https://blog.ui.com/article/introducing-enterprise-nas) ⭐️ 7.0/10

Ubiquiti has announced a new enterprise NAS device that leverages the ZFS file system, featuring dual 25 Gigabit SFP28 ports and redundant power supplies. Ubiquiti's entry into enterprise storage with a ZFS-based NAS challenges subscription-heavy competitors by offering a no-recurring-cost model, potentially attracting cost-sensitive businesses and enthusiasts. The device boasts dual 25 GbE SFP28 ports and redundant power supplies, but community members express concerns about Ubiquiti's software reliability given past security lapses such as exposed AWS keys and misconfigured camera feeds.

hackernews · ksec · Jun 18, 14:24 · [Discussion](https://news.ycombinator.com/item?id=48585866)

**Background**: ZFS is a sophisticated file system with built-in volume management, checksums for data integrity, and support for snapshots and RAID. Ubiquiti is a networking hardware company known for its UniFi product line and a business model that avoids recurring subscription fees, which has built a loyal user base despite occasional software quality issues.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ZFS">ZFS - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is divided: while many praise the ZFS implementation and the no-subscription model, others strongly caution about Ubiquiti's software quality and security history, with some arguing it is not suitable for true enterprise use. There are also questions about whether the hardware can saturate the 25 GbE links with HDDs.

**Tags**: `#Ubiquiti`, `#NAS`, `#ZFS`, `#Enterprise Storage`, `#Product Announcement`

---

<a id="item-12"></a>
## [Cornell CS 6120: Self-Guided Advanced Compilers Course](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 7.0/10

Cornell University's CS 6120: Advanced Compilers is now available as a free, self-guided online course. It covers topics such as static single assignment (SSA), data flow analysis, and various compiler optimizations. This makes high-quality compiler design education accessible to a global audience, helping learners and professionals understand the inner workings of modern compilers, which are fundamental to programming languages and performance optimization. The course is entirely self-paced with lecture videos, slides, and assignments available online. Community comments note that the dynamic compilation section overemphasizes trace compilation—a largely abandoned technique—and some question whether the course is truly 'advanced' as many topics appear in introductory compilers courses.

hackernews · ibobev · Jun 18, 11:04 · [Discussion](https://news.ycombinator.com/item?id=48583606)

**Background**: Static single assignment (SSA) is an intermediate representation where each variable is assigned exactly once, simplifying many compiler optimizations. Data flow analysis is a technique for reasoning about the flow of values through a program, used for optimizations like dead code elimination. These concepts are typically taught in a first compilers course, but the course also covers more advanced topics like dynamic compilation and optimization tiering.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Static_single-assignment_form">Static single-assignment form</a></li>
<li><a href="https://www.cs.cornell.edu/courses/cs6120/2022sp/lesson/6/">CS 6120: Static Single Assignment</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data-flow_analysis">Data - flow analysis - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community widely appreciates the free resource but offers critiques: one commenter notes that the dynamic compilation section overemphasizes trace compilation, a dead-end approach; another questions whether the course is truly 'advanced' as many topics are foundational. Others praise the course's accessibility and share related discussions on Rust compiler ML integration.

**Tags**: `#compilers`, `#education`, `#computer-science`, `#self-guided`, `#programming-languages`

---

<a id="item-13"></a>
## [W Social Criticized as Profit-Driven, Shady EU Digital Sovereignty Project](https://blog.elenarossini.com/w-social-public-institutions-and-the-theater-of-european-digital-sovereignty/) ⭐️ 7.0/10

A critical blog post reveals that W Social, touted as a European digital sovereignty platform, is a for-profit LLC with limited transparency, and the community highlights open-source alternative Eurosky. This scrutiny exposes the gap between political rhetoric and genuine digital sovereignty, as EU politicians may be endorsing a profit-driven platform instead of supporting transparent, open-source projects like Eurosky. W Social is a limited liability company with a founder from finance, not a nonprofit; it is closed-source and plans ads or paid features. Eurosky, built on ATproto, is run by a nonprofit foundation openly sharing its roadmap.

hackernews · nemoniac · Jun 18, 12:46 · [Discussion](https://news.ycombinator.com/item?id=48584497)

**Background**: ATproto (Authenticated Transfer Protocol) is an open standard for decentralized social networking, originally developed by Bluesky. European digital sovereignty aims to reduce dependence on US tech platforms. While W Social launched with high-profile political backing, open-source alternatives like Eurosky, built on ATproto, exist with more transparency.

<details><summary>References</summary>
<ul>
<li><a href="https://eurosky.tech/">Eurosky – mu is here. The first of a thousand social apps.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Atproto">Atproto</a></li>

</ul>
</details>

**Discussion**: Commenters widely view W Social as shady, noting it's a for-profit LLC like Truth Social for EU politicians, and highlight the open-source Eurosky as a more transparent alternative. Many express skepticism about its success and legitimacy.

**Tags**: `#digital sovereignty`, `#social media`, `#EU politics`, `#ATproto`, `#platform criticism`

---

<a id="item-14"></a>
## [Datasette Apps: Host Custom HTML Applications Inside Datasette](https://simonwillison.net/2026/Jun/18/datasette-apps/#atom-everything) ⭐️ 7.0/10

Datasette Apps, a new plugin launched today, enables hosting self-contained HTML+JavaScript applications inside a tightly constrained iframe sandbox on Datasette instances. These apps can run read-only SQL queries against the underlying data, and can be configured to perform write queries as well. This plugin significantly extends Datasette's flexibility, enabling developers to build and deploy custom interactive data tools directly within the platform without external hosting. It makes Datasette a more self-contained environment for data exploration and lightweight application development, while maintaining strong security through sandboxing. The apps run in an iframe with `sandbox="allow-scripts allow-forms"`, which blocks access to cookies and localStorage, and a Content Security Policy (CSP) header is injected to prevent external HTTP requests, eliminating data exfiltration risks. Write queries are only possible if the administrator has configured specific stored queries for that purpose.

rss · Simon Willison · Jun 18, 23:58

**Background**: Datasette is an open-source tool for exploring and publishing data, primarily using SQLite databases. It provides a JSON API and a plugin system, making it popular for building lightweight data tools. The iframe sandbox attribute is a web security mechanism that restricts embedded content's capabilities, preventing it from accessing the parent page's resources. This plugin builds on those concepts to allow secure, self-contained applications within Datasette.

<details><summary>References</summary>
<ul>
<li><a href="http://www.w3schools.com/TAGs/att_iframe_sandbox.asp">HTML iframe sandbox Attribute</a></li>
<li><a href="https://web.dev/articles/sandboxed-iframes">Play safely in sandboxed IFrames | Articles | web.dev</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#sql`, `#web-applications`, `#plugin`, `#open-source`

---

<a id="item-15"></a>
## [Simon Willison's <click-to-play> Web Component Defers GIF Loading Until Click](https://simonwillison.net/2026/Jun/17/click-to-play-component/#atom-everything) ⭐️ 7.0/10

Simon Willison introduced a new web component called <click-to-play> that defers the loading of animated GIFs until the user clicks a play button. It uses progressive enhancement to wrap a static first-frame image and a link to the full GIF, so pages load faster and only download the heavy animation on demand. Large GIFs can significantly slow down page loads and waste bandwidth, especially on mobile. This component offers a lightweight, standard-based solution that improves performance and user experience without breaking accessibility or requiring JavaScript frameworks. The component transforms a simple HTML block containing a link to the GIF and an image of its first frame into a playable unit. It uses the Custom Elements API, loads the GIF only on user interaction, and was originally built for a Datasette blog post demonstrating new row editing features.

rss · Simon Willison · Jun 17, 03:56

**Background**: Web Components are a set of browser standards that allow developers to create reusable custom HTML elements with encapsulated behavior. Progressive enhancement is a design philosophy that delivers core content and functionality to all users, then adds richer experiences for capable browsers, ensuring the page works even without JavaScript. Page performance is critical for user retention and SEO, and large multimedia files like GIFs are a common bottleneck.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Web_Components">Web Components</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement">Progressive enhancement - Glossary | MDN</a></li>

</ul>
</details>

**Tags**: `#gif`, `#web-component`, `#progressive-enhancement`, `#performance`, `#javascript`

---

<a id="item-16"></a>
## [Conversation-level debugging reveals voice AI flaws that isolated benchmarks miss](https://www.reddit.com/r/MachineLearning/comments/1u99fe5/voice_debugging_at_the_conversation_level_seems/) ⭐️ 7.0/10

A practitioner argues that evaluating voice AI systems through conversation-level debugging is far more useful than traditional isolated metrics like STT accuracy or task completion rate, because many real-world failures emerge from multi-turn interaction dynamics rather than single model errors. The author is now experimenting with automated conversation-level QA to scale this debugging approach. This insight highlights a critical gap in current voice AI evaluation, where high benchmark scores may still result in frustrating user experiences. It shifts the focus toward holistic, multi-turn conversation quality, directly impacting the deployment of more natural and usable voice agents in production. The author notes that emergent failures like timing errors, repetitive confirmations, and unnatural turn-taking only become visible in multi-turn traces. Instead of hunting individual model errors, their debugging efforts now target recurring conversational patterns, and they are building automated QA pipelines to avoid the cost of manual trace review.

reddit · r/MachineLearning · /u/OwlZealousideal4779 · Jun 18, 15:29

**Background**: Traditional voice AI evaluation often relies on component-level metrics like speech-to-text word error rate, endpoint latency, and single-turn task success. However, in multi-turn conversations, systems must handle context retention, turn-taking, interruptions, and speech repairs. Recent research has introduced benchmarks such as Audio MultiChallenge and frameworks like EVA that explicitly test multi-turn spoken dialogue, reflecting the industry's growing recognition that conversation-level assessment is essential for realistic voice agent evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://hamming.ai/resources/debugging-voice-agents-real-time-logs-missed-intents-error-dashboards">Debugging Voice Agents: Real-Time Logs... | Hamming AI Resources</a></li>
<li><a href="https://arxiv.org/abs/2512.14865">[2512.14865] Audio MultiChallenge: A Multi-Turn Evaluation of Spoken Dialogue Systems on Natural Human Interaction</a></li>
<li><a href="https://huggingface.co/blog/ServiceNow-AI/eva">A New Framework for Evaluating Voice Agents (EVA)</a></li>

</ul>
</details>

**Tags**: `#voice AI`, `#conversational AI`, `#evaluation metrics`, `#debugging`, `#speech systems`

---

<a id="item-17"></a>
## [Microsoft Research's Next-Latent Prediction for Self-Supervised Transformers](https://www.reddit.com/r/MachineLearning/comments/1u84mio/nextlatent_prediction_transformers_r/) ⭐️ 7.0/10

Microsoft Research introduced Next-Latent Prediction (NextLat), a self-supervised training method that extends next-token prediction by having the transformer predict its own next latent state. This enables more compact representations, denser supervision, and up to 3.3x faster inference via self-speculative decoding. This approach addresses the myopic nature of next-token prediction by compressing history into compact belief states, potentially improving data efficiency and enabling world models for reasoning and planning. The self-speculative decoding also offers significant inference speedups without additional model components. NextLat adds a latent prediction loss alongside the standard next-token loss, training the transformer to predict its own internal state at the next time step. The self-speculative decoding uses the model's own latent predictions for multi-step lookahead, achieving up to 3.3x speedup without loss of accuracy.

reddit · r/MachineLearning · /u/jayden_teoh_ · Jun 17, 08:44

**Background**: Large language models are typically trained with next-token prediction, which provides one supervision signal per token. Self-speculative decoding is a lossless technique that speeds up inference by having the model draft multiple tokens in parallel using its own internal states, then verify them in a single forward pass. The method's latent states are the compressed representations of the context at each step.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/next-latent-prediction-nextlat">Next - Latent Prediction Overview</a></li>
<li><a href="https://arxiv.org/html/2511.05963v1">Next - Latent Prediction Transformers Learn Compact World Models</a></li>
<li><a href="https://www.emergentmind.com/topics/self-speculative-decoding">Self - Speculative Decoding</a></li>

</ul>
</details>

**Tags**: `#Transformers`, `#Self-Supervised Learning`, `#Latent Prediction`, `#World Models`, `#Speculative Decoding`

---

<a id="item-18"></a>
## [Swiss Parliament Lifts Ban on New Nuclear Power Plants](https://www.bluewin.ch/en/news/switzerland/parliament-lifts-ban-on-new-nuclear-power-plants-3257535.html) ⭐️ 6.0/10

The Swiss parliament voted to lift the ban on new nuclear power plants, a prohibition in place since a 2017 referendum. The decision is not yet final and must survive a forthcoming public referendum. This reversal signals a potential pivot in Swiss energy policy away from a nuclear phase-out, driven by reliability concerns and seasonal supply gaps. It could influence broader European debates on nuclear power as a low-carbon baseload source. The ban was originally enacted by a 2017 public vote, and the new bill must be approved again. The controversy centers on Switzerland's seasonal energy challenge: hydropower peaks in spring and summer due to snowmelt, while winter demand relies on imports, making nuclear an attractive baseload solution.

hackernews · leonidasrup · Jun 18, 14:17 · [Discussion](https://news.ycombinator.com/item?id=48585746)

**Background**: Switzerland operates four aging nuclear reactors that supply roughly one-third of its electricity. In 2017, a referendum banned new nuclear construction as part of a gradual phase-out. The country has abundant hydropower and growing solar capacity, but both are highly seasonal, creating a winter deficit often met by imports. The recent European energy crisis has intensified the debate over lifting the ban to ensure year-round supply security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vtcenerji.com/en/seasonality-analysis-and-multiple-seasonality-applications-in-electric-load-forecasting/">Seasonality Analysis and Multiple Seasonality ... - VTC Enerji</a></li>

</ul>
</details>

**Discussion**: Comments are deeply divided. Skeptics argue nuclear is too slow and expensive, citing cost overruns of Vogtle and Ontario, and suggest Switzerland should instead expand hydropower storage or join French nuclear projects. Optimists see a renaissance, especially for small modular reactors from ETH startups, while many emphasize the seasonal winter energy gap that nuclear could help fill. The referendum is expected to be contentious.

**Tags**: `#nuclear-energy`, `#energy-policy`, `#switzerland`, `#politics`, `#technology`

---

<a id="item-19"></a>
## [datasette-acl 0.6a0 Expands from Table-Only to General Resource Sharing](https://simonwillison.net/2026/Jun/18/datasette-acl/#atom-everything) ⭐️ 6.0/10

The alpha release of datasette-acl 0.6a0 moves beyond table-level permissions, introducing a general resource-sharing system that can control access to any resource type defined by Datasette plugins, such as documents, lists, and workbooks. This upgrade is a key step toward making Datasette a viable multi-user platform, enabling fine-grained access control for collaborative data exploration and publication, and expanding the plugin's utility beyond simple table-based data sharing. The release is primarily the work of Alex Garcia and is still in an alpha stage, meaning it may have stability issues and is not yet recommended for production. It now supports grants for arbitrary resource types, storing and resolving permissions via a plugin-based architecture.

rss · Simon Willison · Jun 18, 19:03

**Background**: Datasette is an open-source tool for exploring and publishing data, often used to create interactive websites from SQLite databases. Access-control lists (ACLs) are a standard security mechanism to define which users or groups can perform specific operations on resources. The datasette-acl plugin originally provided a user interface for managing table-level permissions; this release extends that model to cover any resource type within a Datasette instance, moving toward a full multi-user permission system.

<details><summary>References</summary>
<ul>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and publishing data</a></li>
<li><a href="https://github.com/datasette/datasette-acl">datasette/datasette-acl: Advanced permission management for Datasette - GitHub</a></li>
<li><a href="https://pypi.org/project/datasette-acl/">datasette-acl - PyPI</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#acl`, `#permissions`, `#plugin`, `#access-control`

---

<a id="item-20"></a>
## [Speculative Decoding Spotlight: SGLang's Latest Latency Advances](https://www.reddit.com/r/MachineLearning/comments/1u83kzt/what_is_speculative_decoding_trending_on/) ⭐️ 6.0/10

Speculative decoding, a technique trending on Papers with Code, accelerates LLM inference by using a small draft model to propose tokens that a larger target model verifies in parallel. SGLang's recent blog post details how they achieve state-of-the-art latencies with Modal and Z.ai's DFlash models. This matters because it can significantly reduce the latency of large language model inference without compromising output quality, making LLM-powered applications more responsive and cost-effective. As LLMs grow, such optimizations are crucial for real-world deployment. The technique uses a draft model to propose multiple future tokens at once, and the target model verifies them in a single forward pass, accepting only correct tokens. SGLang's implementation leverages DFlash v2 models and Modal's infrastructure, detailed in a blog post from LMSYS.

reddit · r/MachineLearning · /u/NielsRogge · Jun 17, 07:41

**Background**: Large language models typically generate text one token at a time, each requiring a full model forward pass, making inference slow. Speculative decoding, first introduced in late 2022, uses a smaller, faster 'draft' model to propose several future tokens, which the larger target model then verifies in a single parallel pass. This allows the model to accept multiple tokens per step, speeding up generation without quality loss. SGLang is an open-source LLM serving framework, and Modal is a serverless cloud platform for AI.

**Tags**: `#speculative-decoding`, `#large-language-models`, `#inference-optimization`, `#sglang`

---

<a id="item-21"></a>
## [Balancing Probe and Network Capacity: Seeking Theoretical Guarantees for Probing](https://www.reddit.com/r/MachineLearning/comments/1u8lo60/how_do_you_analyze_the_relative_strength_of/) ⭐️ 6.0/10

A Reddit post asks how to balance probing classifier capacity against network capacity and seeks theoretical guarantees (e.g., overfitting bounds, Nyquist-like sampling guarantees) for probing methods, citing a failure of Google Gemini in token decomposition as a cautionary example. This question is important because probing is a widely used interpretability tool, but without rigorous theoretical grounding, conclusions about what a model 'knows' can be unreliable and may mislead high-stakes applications like factuality guarantees. The author details a logistic regression probe for word position that may overestimate performance due to limited word classes, and questions whether language data frequency can provide Nyquist-like sampling guarantees. The post also notes that Google Gemini failed to count letters in 'Google' despite spelling it out, undermining claims that models learn token positions.

reddit · r/MachineLearning · /u/RepresentativeBee600 · Jun 17, 20:29

**Background**: Probing classifiers are small models trained on neural network activations to predict linguistic properties, aiming to reveal what the network has learned. However, high probe performance can be misleading if the probe itself has sufficient capacity to learn the task independently. Mechanistic interpretability uses circuit analysis to identify computational subgraphs in models, but suffers from similar reliability concerns. The Nyquist-Shannon sampling theorem from signal processing states that a continuous signal must be sampled at least twice its highest frequency to be perfectly reconstructed; the author draws an analogy to whether language data is sampled densely enough to guarantee reliable learning of patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and">Probing Classifiers: Promises, Shortcomings, and Advances | Computational Linguistics | MIT Press</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nyquist–Shannon_sampling_theorem">Nyquist–Shannon sampling theorem - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#interpretability`, `#probing`, `#transformer`, `#machine-learning`, `#circuit-analysis`

---

<a id="item-22"></a>
## [Contrastive Targeted SFT Proposed as Mechanistic Interpretability Method to Map Causal Dependencies](https://www.reddit.com/r/MachineLearning/comments/1u8if6l/contrastive_targeted_sft_as_a_mechinterp_method/) ⭐️ 6.0/10

A Reddit user proposes using contrastive targeted supervised fine-tuning (SFT) to locate capability-specific circuits in a 31B language model, by creating checkpoint pairs with a dimension deep vs. shallow and then ablating heads to measure how other quality dimensions degrade, building a causal dependency graph. This approach could systematically reveal how different capabilities (e.g., reasoning, factuality) causally interact inside a model, enabling optimal training ordering and targeted capability improvement, and advancing mechanistic interpretability research. The idea is preliminary with no published results; it uses a judge scoring 40 domains on six independent quality dimensions. The plan includes multi-layer ablation to distinguish direct from indirect causal dependencies, and activation steering as a diagnostic for composition failures.

reddit · r/MachineLearning · /u/Substantial_Diver469 · Jun 17, 18:31

**Background**: Mechanistic interpretability aims to reverse-engineer neural networks by analyzing their internal computations, similar to decompiling binary code. In transformer models, the residual stream acts as a shared communication channel where each attention and MLP layer reads from and writes to, enabling information flow across layers. Contrastive fine-tuning uses paired examples to steer the model away from undesired outputs by learning distinctions. Targeted SFT focuses fine-tuning on specific skill dimensions to boost particular capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://medium.com/@zepingyu/123-cb62513f5d50">Exploring the Residual Stream of Transformers for Mechanistic Interpretability — Explained | by Zeping Yu | Medium</a></li>
<li><a href="https://arxiv.org/pdf/2310.02263">Automatic Pair Construction for Contrastive Post-training</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#causal dependency`, `#supervised fine-tuning`, `#contrastive learning`, `#language model circuits`

---