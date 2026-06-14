---
layout: default
title: "Horizon Summary: 2026-06-14 (EN)"
date: 2026-06-14
lang: en
---

> From 31 items, 15 important content pieces were selected

---

1. [PyPI Now Supports Publishing WASM Wheels for Browser-Based Python](#item-1) ⭐️ 9.0/10
2. [US Government Forces Anthropic to Suspend Fable 5 and Mythos 5 Models Globally](#item-2) ⭐️ 9.0/10
3. [10th Gen Honda Civic Firmware Updates Signed with Public AOSP Test Keys](#item-3) ⭐️ 8.0/10
4. [US Census Bureau bans noise infusion, raising privacy fears](#item-4) ⭐️ 8.0/10
5. [Z.ai Releases Open-Source GLM-5.2 Amid US AI Access Restrictions](#item-5) ⭐️ 8.0/10
6. [Targeting KRAS mutation reveals a master switch in pancreatic cancer](#item-6) ⭐️ 8.0/10
7. [Critique of Imperfect Animation Frames in macOS UI Design](#item-7) ⭐️ 7.0/10
8. [Mapping SQLite result columns back to source tables for Datasette](#item-8) ⭐️ 7.0/10
9. [Two-Tier Verification Reveals 'Verifier Tax' in LLM Agent Safety](#item-9) ⭐️ 7.0/10
10. [PaddleOCR v3-v6 deployed via lightweight C++ and ncnn inference](#item-10) ⭐️ 7.0/10
11. [Rust/WASM Edge Semantic Cache for LLMs Proposed to Slash Latency](#item-11) ⭐️ 7.0/10
12. [OpenAI WebRTC audio playground adds GPT-Realtime-2 and document context](#item-12) ⭐️ 6.0/10
13. [Satirical excerpt 'AI Economics for Dummies' mocks AI investment hype](#item-13) ⭐️ 6.0/10
14. [Open-source bilingual Jupyter course on classical machine learning seeks feedback](#item-14) ⭐️ 6.0/10
15. [hubert.cpp: A Lightweight C++ Library for distilHuBERT with On-Par ONNX Performance](#item-15) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [PyPI Now Supports Publishing WASM Wheels for Browser-Based Python](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 9.0/10

Pyodide 314.0 and PEP 783 now enable developers to publish WebAssembly (WASM) Python wheels directly to PyPI, removing the need for Pyodide maintainers to manually curate and host over 300 packages. This decentralizes Pyodide's package ecosystem, dramatically reducing the bottleneck of manual review and accelerating the development of Python-in-browser applications by empowering any maintainer to distribute WASM extensions. Packages built for the PyEmscripten platform, defined in PEP 783, now use the `pyemscripten_*` tag and can be installed at runtime via micropip, as demonstrated by the `luau-wasm` package built with C++ and cibuildwheel.

rss · Simon Willison · Jun 13, 23:55

**Background**: Pyodide is a project that brings Python to the browser by compiling the CPython interpreter and scientific computing libraries to WebAssembly, which is a binary instruction format that runs in web browsers. Previously, any non-pure-Python package had to be manually built and published through the Pyodide team. A wheel is a standard, pre-compiled distribution format for Python packages that allows for faster installation.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.pyodide.org/posts/314-release/">Pyodide 314.0 Release</a></li>
<li><a href="https://pyodide.org/en/latest/development/abi.html">The PyEmscripten Platform — Version 314.0.0a2 - Pyodide</a></li>
<li><a href="https://discuss.python.org/t/pep-783-emscripten-packaging/86862?page=4">PEP 783: Emscripten Packaging - Page 4 - Python Discussions</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion celebrated this as a long-awaited and significant infrastructure improvement that makes Pyodide packaging finally work like native Python packaging, while discussion on Python forums reflected broad consensus and technical refinement during the PEP acceptance process.

**Tags**: `#python`, `#webassembly`, `#pypi`, `#pyodide`, `#pep-783`

---

<a id="item-2"></a>
## [US Government Forces Anthropic to Suspend Fable 5 and Mythos 5 Models Globally](https://simonwillison.net/2026/Jun/13/us-government-directive-to-suspend-access/#atom-everything) ⭐️ 9.0/10

The US government issued an export control directive on June 12, 2026, forcing Anthropic to abruptly suspend global access to its latest Fable 5 and Mythos 5 models, citing national security concerns related to a jailbreaking method. This marks the first time the US government has forced an AI company to abruptly shut down access to frontier models globally, setting a precedent for how export controls may be used to intervene in AI deployment and raising concerns about extraterritorial overreach. The directive targets access by any foreign national, including Anthropic's own employees outside the US, and was triggered by a jailbreak that simply asked the model to read a codebase and fix flaws — a capability Anthropic claims is widely available in other models like GPT-5.5.

rss · Simon Willison · Jun 13, 01:01

**Background**: AI jailbreaks are methods to bypass a model's safety guardrails, and they are a known and pervasive challenge across all LLMs, with vulnerabilities often being architectural rather than model-specific. US export controls on AI have traditionally targeted hardware like chips, but this action extends regulatory reach to software models under national security authorities. Anthropic's Fable 5 and Mythos 5 were their newest and most capable models, launched just days earlier.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.microsoft.com/en-us/security/blog/2024/06/04/ai-jailbreaks-what-they-are-and-how-they-can-be-mitigated/">AI jailbreaks: What they are and how they can be mitigated | Microsoft Security Blog</a></li>
<li><a href="https://cset.georgetown.edu/article/dont-forget-the-catch-all-basics-ai-export-controls/">For Export Controls on AI, Don't Forget the "Catch-All" Basics | Center for Security and Emerging Technology</a></li>

</ul>
</details>

**Discussion**: Commenters questioned why Anthropic informed the government about a known, universal LLM vulnerability, speculating that Amazon's involvement with Anthropic may have triggered the crackdown; others suggested that Fable 5 is actually less capable in exploitation tasks than older models like Opus 4.8, casting doubt on the government's rationale.

**Tags**: `#AI`, `#policy`, `#Anthropic`, `#export-controls`, `#national-security`

---

<a id="item-3"></a>
## [10th Gen Honda Civic Firmware Updates Signed with Public AOSP Test Keys](https://juniperspring.org/posts/honda-evil-valet/) ⭐️ 8.0/10

A security researcher discovered that Honda's over-the-air firmware updates for 10th-generation Civic headunits are signed with publicly-available Android Open Source Project (AOSP) test keys, not private Honda signing keys. This allows anyone with physical USB access to sign and flash arbitrary code onto the vehicle's infotainment system without needing root privileges. This oversight represents a significant security failure by a major automaker, potentially exposing millions of vehicles to attacks via malicious USB drives. It highlights the ongoing tension in the automotive industry between implementing robust security practices and preserving owners' right to repair and modify their vehicles. The updates are essentially Android 4.2.2 recovery packages with Honda-added version checks that can be easily spoofed. The vulnerability requires physical access to the vehicle's front USB port but does not need existing root or superuser privileges on the headunit, and has been successfully demonstrated on a 2021 Civic.

hackernews · librick · Jun 14, 00:49 · [Discussion](https://news.ycombinator.com/item?id=48523080)

**Background**: AOSP test keys are publicly-known cryptographic keys included in the Android source code, intended solely for development and testing purposes. Production devices should always use manufacturer-specific private keys to sign firmware, ensuring only authorized code can run. The discovery that these development keys are used in shipping vehicles follows similar findings reported by Meta's Red Team X in 2024, where several Android device vendors also shipped components signed with the same test keys.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/wfairclough/android_aosp_keys">GitHub - wfairclough/android_aosp_keys: The platform keys that are used as test keys for the AOSP build · GitHub</a></li>
<li><a href="https://rtx.meta.security/exploitation/2024/01/30/Android-vendors-APEX-test-keys.html">Missing signs: how several brands forgot to secure a key piece of Android | Meta Red Team X</a></li>
<li><a href="https://github.com/aosp-mirror/platform_build/blob/master/tools/releasetools/sign_target_files_apks.py">platform_build/tools/releasetools/sign_target_files_apks.py at master · aosp-mirror/platform_build</a></li>

</ul>
</details>

**Discussion**: The community shows mixed reactions, with some humorously noting this ironically proves Honda didn't intend to lock owners out of their cars, while others worry about deeper security implications like CAN bus access. A recurring sentiment suggests that regardless of whether manufacturers lock down systems or leave them open, they face criticism from different camps in the right-to-repair versus security debate.

**Tags**: `#security`, `#embedded-systems`, `#automotive`, `#android`, `#firmware`

---

<a id="item-4"></a>
## [US Census Bureau bans noise infusion, raising privacy fears](https://desfontain.es/blog/banning-noise.html) ⭐️ 8.0/10

The U.S. Census Bureau has decided to ban noise infusion, a technique based on differential privacy, from its statistical products. This move reverses previous privacy-enhancing measures and raises serious concerns about the potential erosion of individual data protection in government statistics. This policy shift could significantly weaken the protection of sensitive personal data collected by the government, making it easier to re-identify individuals from supposedly anonymous aggregate statistics. It impacts the fundamental trust between the public and the state, potentially deterring participation in future censuses and affecting the quality of crucial demographic data. Noise infusion (differential privacy) works by adding mathematically calibrated noise to statistical outputs, providing a provable guarantee against individual re-identification. Critics of the ban argue it was motivated by data users who found the noise inconvenient, overlooking that reconstruction attacks successfully reverse-engineered individual-level data from unprotected 2010 Census aggregate figures.

hackernews · nl · Jun 13, 13:54 · [Discussion](https://news.ycombinator.com/item?id=48517377)

**Background**: Differential privacy is a rigorous mathematical framework for publishing statistical data while limiting information leakage about specific individuals. The Census Bureau adopted it for the 2020 decennial census to counter modern re-identification threats where attackers can combine census tabulations with external commercial databases to unmask respondents' identities. The technique involves a deliberate trade-off between data accuracy and privacy protection.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Differential_privacy">Differential privacy</a></li>

</ul>
</details>

**Discussion**: Discussion reflects a strong consensus that this decision is a major setback for privacy. Commenters, including a former enumerator, express deep concern over broken trust and the increased risk of weaponizing sensitive data. Some note that differential privacy's deliberate resistance to individual-level reconstruction is exactly its intended purpose, suggesting the ban may benefit those seeking to exploit the data.

**Tags**: `#differential privacy`, `#census`, `#data policy`, `#government transparency`, `#privacy`

---

<a id="item-5"></a>
## [Z.ai Releases Open-Source GLM-5.2 Amid US AI Access Restrictions](https://twitter.com/jietang/status/2065784751345287314) ⭐️ 8.0/10

Z.ai has released GLM-5.2 as a fully open-source model under a permissive license, explicitly timed to counter recent US government restrictions on frontier AI models like Fable. This release intensifies the global debate on open-source AI versus controlled access, demonstrating that open-weight models can ensure global scientific progress even when strategic products are gated by geopolitical actors. The model was released at 5:21 pm China time, coinciding with the timing of Anthropic receiving a government letter banning Fable. Detailed benchmark results are not yet available in an official blog post.

hackernews · aloknnikhil · Jun 13, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48518684)

**Background**: GLM is a series of large language models developed by Z.ai, with the previous GLM-4.5 featuring 355 billion total parameters and 32 billion active parameters. The release context involves recent US government actions that suddenly restricted access to certain frontier AI models like Fable for non-technical reasons, prompting calls for more open alternatives.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/zai-org/GLM-4.5">GLM-4.7 & GLM-4.6 & GLM-4.5 - Coding - GitHub</a></li>
<li><a href="https://www.reddit.com/r/vibecoding/comments/1pzwepo/what_is_glm_i_saw_it_under_a_vibecode_video_and/">What is GLM? (I saw it under a vibecode video) And what are allt ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment largely praises the release, with users expressing gratitude for Chinese AI labs' openness and remarking on a perceived role reversal where US companies censor while Chinese labs freely contribute open-weight models.

**Tags**: `#open-source`, `#large-language-models`, `#china-ai`, `#ai-policy`, `#open-weight-models`

---

<a id="item-6"></a>
## [Targeting KRAS mutation reveals a master switch in pancreatic cancer](https://economist.com/science-and-technology/2026/06/12/treating-pancreatic-tumours-may-have-revealed-cancers-master-switch) ⭐️ 8.0/10

A new breakthrough has enabled targeting the KRAS protein, which was previously considered undruggable and is present in about 20% of all cancers, with significant implications for treating pancreatic tumors. This breakthrough opens the door to treating a wide range of cancers that share this common mutation, potentially transforming the prognosis for one of the deadliest forms of cancer and paving the way for drugging other previously unreachable targets. The study referenced in the article is registered as clinical trial NCT06625320, and while promising, the advance applies to cancers driven by a specific KRAS mutation, not all cancer types.

hackernews · andsoitis · Jun 13, 13:34 · [Discussion](https://news.ycombinator.com/item?id=48517199)

**Background**: KRAS is a protein that acts as a molecular switch for cell growth, and mutations in it lead to uncontrolled division found in many cancers, especially pancreatic cancer. For decades, KRAS was labeled 'undruggable' because its smooth surface made it impossible for traditional small-molecule drugs to bind to it. Recent advances in drug design, such as biologic therapies, have begun to overcome this challenge, with scientists now able to develop agents that can latch onto previously hidden pockets in the protein.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10367563/">Emerging Pharmacotherapeutic Strategies to Overcome Undruggable Proteins in Cancer - PMC</a></li>
<li><a href="https://www.nature.com/articles/s41392-023-01589-z">Recent advances in targeting the “undruggable” proteins: from drug discovery to clinical trials | Signal Transduction and Targeted Therapy</a></li>

</ul>
</details>

**Discussion**: Commenters note the title is hyperbolic but still welcome the advance. They emphasize that KRAS was considered 'undruggable,' making this a significant proof-of-concept for future treatments, while also calling for greater investment in early cancer detection alongside therapeutic breakthroughs.

**Tags**: `#cancer-research`, `#biotechnology`, `#oncology`, `#KRAS`, `#medical-breakthrough`

---

<a id="item-7"></a>
## [Critique of Imperfect Animation Frames in macOS UI Design](https://tonsky.me/blog/every-frame-perfect/) ⭐️ 7.0/10

A detailed technical article analyzes specific frames in macOS animations, revealing instances where UI elements are technically incorrect or distorted in isolation, despite appearing smooth during motion. The analysis sparks an important debate about the tradeoffs between pixel-perfect rendering and perceived motion quality, challenging UI engineers to reconsider what constitutes 'correct' animation in human-computer interaction. The article focuses on imperceptible flaws visible only when pausing animations, with commenters noting that these issues appear to have worsened in newer macOS versions, and that some 'wrong' frames may actually be optimal for real-time perception.

hackernews · ravenical · Jun 13, 11:40 · [Discussion](https://news.ycombinator.com/item?id=48516251)

**Discussion**: The community is highly divided. Some argue that exploiting human visual system limitations is fundamental to graphics and that a 'wrong' static frame can look best in motion. Others note a regression in macOS animation quality over versions, while some question the necessity of motion animations entirely, suggesting instantaneous transitions would feel just as good.

**Tags**: `#ui-design`, `#animation`, `#macos`, `#graphics`, `#human-computer-interaction`

---

<a id="item-8"></a>
## [Mapping SQLite result columns back to source tables for Datasette](https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything) ⭐️ 7.0/10

Simon Willison experimented with using Claude Code (Opus 4.8) to solve SQL column provenance mapping for Datasette, discovering multiple technical approaches including APSW, direct C function access via ctypes, and EXPLAIN output interrogation. Solving column provenance would allow Datasette to enrich arbitrary SQL query results with metadata about which tables and columns contributed to each output, significantly improving the user experience for database exploration and analysis. The investigation focused on complex query structures including joins, CTEs, and subqueries; one approach leverages the SQLite C function `sqlite3_column_table_name()` which is not directly exposed in Python's standard library.

rss · Simon Willison · Jun 13, 23:05

**Background**: Datasette is an open-source tool for exploring and publishing SQLite databases as web interfaces. SQLite's Python binding exposes query results as flat column lists, but does not natively indicate which table each column originated from when queries involve joins or complex transformations. Column provenance—tracking the origin of each result column back to its source table and column—is a known challenge in database tools and requires parsing SQL or accessing lower-level database APIs.

**Tags**: `#sqlite`, `#metadata-extraction`, `#ai-assisted-development`, `#datasette`, `#sql-parsing`

---

<a id="item-9"></a>
## [Two-Tier Verification Reveals 'Verifier Tax' in LLM Agent Safety](https://www.reddit.com/r/MachineLearning/comments/1u58mkq/the_verifier_tax_horizondependent_safetysuccess/) ⭐️ 7.0/10

A paper presented at ACM CAIS 2026 introduces a two-tier verification architecture for tool-using LLM agents and discovers a horizon-dependent tradeoff termed the 'Verifier Tax,' where safety verification reduces unsafe outcomes but increasingly impairs task completion as task horizons lengthen. This work provides a crucial safety evaluation framework that distinguishes 'unsafe success' from true success, addressing a blind spot in current agent benchmarks and offering practical insights for building reliable, safety-aware LLM agents in real-world applications. The architecture uses deterministic policy/tool checks as a first layer, followed by an LLM-based verifier for nuanced safety cases. The study demonstrates that as task horizon increases, verification reduces unsafe success but also causes a decline in overall task completion, a phenomenon dubbed the 'Verifier Tax.'

reddit · r/MachineLearning · /u/AccomplishedLeg1508 · Jun 14, 02:09

**Background**: LLM agents are AI systems that use large language models to interact with tools and APIs to perform tasks. Current benchmarks like τ-bench evaluate agents in realistic, multi-turn conversational scenarios, but they typically measure only task success, overlooking whether the agent achieved the goal in a safe or policy-compliant manner. This paper addresses the gap by introducing a safety metric and verification system.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sierra-research/tau-bench">sierra-research/tau-bench: Code and Data for Tau-Bench · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2406.12045">A Benchmark for Tool-Agent-User Interaction in Real-World Domains</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is limited, but the original poster's question highlights a central tension: should the community count an agent's unsafe task completion as a success, a failure, or a distinct third category? This reflects a broader need for standardized, multi-dimensional evaluation metrics in the field.

**Tags**: `#LLM agents`, `#safety evaluation`, `#verification architecture`, `#tool use`, `#AI safety`

---

<a id="item-10"></a>
## [PaddleOCR v3-v6 deployed via lightweight C++ and ncnn inference](https://www.reddit.com/r/MachineLearning/comments/1u4hy2x/paddleocr_v3v4v5v6_implemented_in_c_with_ncnn_p/) ⭐️ 7.0/10

A developer has released a refined C++ implementation of PaddleOCR, now supporting model versions v3 through v6, which uses the ncnn inference framework to significantly simplify deployment compared to the official runtime. By replacing the complex and dependency-heavy official PaddlePaddle runtime with the lightweight ncnn library, this tool makes production deployment of state-of-the-art OCR models significantly easier and faster, benefiting developers integrating OCR into edge or resource-constrained applications. This open-source project covers the PP-OCR model series from v3 to the latest v6, and the author notes ncnn provides both a lighter footprint and faster inference speed for their specific tasks.

reddit · r/MachineLearning · /u/Knok0932 · Jun 13, 05:06

**Background**: PaddleOCR is a popular open-source optical character recognition (OCR) toolkit developed by Baidu, used for extracting text from images. The ncnn inference framework is also from Tencent, designed for high-performance neural network inference on mobile and embedded platforms with no third-party dependencies, making it ideal for lightweight deployments.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/PaddleOCR">PaddleOCR</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#C++`, `#model-deployment`, `#inference`, `#ncnn`

---

<a id="item-11"></a>
## [Rust/WASM Edge Semantic Cache for LLMs Proposed to Slash Latency](https://www.reddit.com/r/MachineLearning/comments/1u3quwk/building_an_open_source_edge_semantic_cache_for/) ⭐️ 7.0/10

A developer has proposed a new open-source architecture that uses a Rust-compiled WebAssembly (WASM) module on CDN edge nodes to perform semantic caching for large language models (LLMs), aiming to serve cached responses in ~5ms without touching the main LLM provider. This approach directly addresses the high API costs and network latency of centralized LLM gateways by moving computation to the edge, potentially making real-time streaming agents and interactive applications faster and cheaper for high-volume, repetitive use cases. The proposed cache works by generating a vector from the prompt using a lightweight model like bge-small-en-v1.5, performing cosine similarity against an edge vector database, and returning a cached response if the score exceeds a threshold like 0.88. It is designed for sub-millisecond execution and a tiny memory footprint suitable for edge runtimes like Cloudflare Workers.

reddit · r/MachineLearning · /u/Real-Huckleberry-934 · Jun 12, 09:53

**Background**: Semantic caching understands the intent behind a prompt rather than matching exact text, allowing it to reuse cached LLM responses for similar queries. Edge computing places computation on servers physically near the end-user within a CDN, avoiding the delay of sending data to a central cloud data center. Rust is a systems programming language known for performance and safety, and it can be compiled to WebAssembly, a binary format that runs securely at high speeds in constrained environments like edge nodes.

<details><summary>References</summary>
<ul>
<li><a href="https://redis.io/blog/what-is-semantic-caching/">What is semantic caching? Guide to faster, smarter LLM apps - Redis</a></li>
<li><a href="https://en.wikipedia.org/wiki/Edge_computing">Edge computing</a></li>
<li><a href="https://www.ibm.com/think/topics/edge-computing">What Is Edge Computing? - IBM</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#edge-computing`, `#wasm`, `#rust`, `#caching`

---

<a id="item-12"></a>
## [OpenAI WebRTC audio playground adds GPT-Realtime-2 and document context](https://simonwillison.net/2026/Jun/12/openai-webrtc/#atom-everything) ⭐️ 6.0/10

Simon Willison updated his OpenAI WebRTC audio playground to support the new GPT-Realtime-2 voice model and allow users to paste document context for conversational audio interactions. This integration demonstrates practical use of OpenAI's latest voice model with GPT-5-class reasoning, enabling richer, context-aware audio conversations directly in the browser. The tool uses the OpenAI WebRTC API, supports voice option 'Coral', and the new model features a knowledge cut-off of September 30, 2024.

rss · Simon Willison · Jun 12, 23:53

**Background**: Simon Willison first built this browser-based audio playground in December 2024 to experiment with OpenAI's then-new WebRTC API for real-time voice models. Last month, OpenAI released GPT-Realtime-2, which the company describes as its first voice model with GPT-5-class reasoning, though it has not yet appeared in the ChatGPT iPhone app. WebRTC enables low-latency, real-time audio communication directly in web browsers.

**Tags**: `#OpenAI`, `#WebRTC`, `#voice AI`, `#GPT-Realtime`, `#tools`

---

<a id="item-13"></a>
## [Satirical excerpt 'AI Economics for Dummies' mocks AI investment hype](https://simonwillison.net/2026/Jun/12/andrew-singleton/#atom-everything) ⭐️ 6.0/10

Simon Willison shared a satirical excerpt from Andrew Singleton's 'AI Economics for Dummies', published on McSweeney's, which uses a fictional story about a crematorium and a propane company to parody the circular, self-dealing financial practices in the AI investment landscape. This satire provides a sharp and accessible critique of opaque financial relationships, inflated valuations, and revenue circularity within the AI industry, resonating with growing concerns about whether AI investment is fueled by genuine value or financial engineering. The fictional scenario involves Jenny's crematorium receiving a $20 billion investment from John's propane company, then using $10 billion to buy propane from John to burn the remaining $10 billion, allowing John to report phantom revenue and asset value. The excerpt is from McSweeney's and was highlighted by Simon Willison on his blog.

rss · Simon Willison · Jun 12, 18:09

**Background**: The AI industry has seen massive capital inflows, with companies like OpenAI and Anthropic raising billions at high valuations, often from strategic investors. This has raised questions about the sustainability and underlying economics, as some transactions involve investors and customers who are the same entities, or revenue generated from subsidiaries, creating a perception of circular funding.

**Tags**: `#satire`, `#ai-investment`, `#economics`, `#commentary`

---

<a id="item-14"></a>
## [Open-source bilingual Jupyter course on classical machine learning seeks feedback](https://www.reddit.com/r/MachineLearning/comments/1u4zbld/im_building_a_free_bilingual_machinelearning/) ⭐️ 6.0/10

A developer has released an open-source, bilingual (English/Persian) Jupyter notebook course covering classical machine learning topics, and is actively soliciting community feedback on its structure and completeness. This project lowers the barrier for non-native English speakers to learn machine learning using free, hands-on materials, contributing to greater accessibility and diversity in the global ML education ecosystem. The curriculum is notebook-first and covers ML foundations, regression, classification, ensembles, clustering, dimensionality reduction, model evaluation, time series, anomaly detection, and MLOps, with the author specifically asking for advice on chapter ordering and missing topics.

reddit · r/MachineLearning · /u/abolfazl1363 · Jun 13, 19:07

**Background**: Classical machine learning refers to established algorithms outside of deep learning, such as linear regression, decision trees, and support vector machines. Jupyter notebooks are interactive documents that combine code, text, and visualizations, making them a popular tool for learning and teaching data science. Bilingual educational resources are particularly valuable in bridging language gaps for learners who are more comfortable studying in their native language.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.redhat.com/articles/2021/05/21/introduction-machine-learning-jupyter-notebooks">Introduction to machine learning with Jupyter notebooks</a></li>
<li><a href="https://datatalks.club/blog/free-machine-learning-courses.html">20+ Best Free Machine Learning Courses - DataTalks.Club</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#education`, `#open-source`, `#jupyter-notebooks`, `#tutorial`

---

<a id="item-15"></a>
## [hubert.cpp: A Lightweight C++ Library for distilHuBERT with On-Par ONNX Performance](https://www.reddit.com/r/MachineLearning/comments/1u3omwk/hubertcpp_a_c_implementation_of_distilhubert_p/) ⭐️ 6.0/10

A developer has released hubert.cpp, a header-only C++ implementation of the distilled speech model distilHuBERT that compiles model weights directly into the library, requires no runtime dependencies, and achieves inference performance comparable to ONNX Runtime. This self-contained library significantly simplifies the deployment of distilHuBERT for edge and embedded devices by removing complex dependency chains, making it easier to integrate into CMake projects and accelerating the adoption of on-device speech processing. The library has no runtime dependencies, embeds pre-trained weights internally, supports dynamic input sizes, and is easily integrable into any CMake project, though it's presented as a personal project with limited community testing so far.

reddit · r/MachineLearning · /u/Competitive_Act5981 · Jun 12, 07:40

**Background**: distilHuBERT is a distilled version of HuBERT, a speech representation model that learns to understand language from audio. The distillation process reduces the model's size by 75% and makes it 73% faster, making it much more suitable for resource-constrained environments. ONNX Runtime is a widely used, cross-platform accelerator for ML models, and matching its performance is a notable achievement for a from-scratch, dependency-free implementation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2110.01900">[2110.01900] DistilHuBERT: Speech Representation Learning by Layer-wise Distillation of Hidden-unit BERT</a></li>
<li><a href="https://grokipedia.com/page/ONNX_Runtime">ONNX Runtime</a></li>

</ul>
</details>

**Tags**: `#hubert`, `#c++`, `#speech-processing`, `#onnx`, `#edge-inference`

---