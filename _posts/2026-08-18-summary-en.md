---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
lang: en
---

> From 34 items, 19 important content pieces were selected

---

1. [DuckDB v2.0 Preview: Quack Protocol and Semi-Structured Data Shredding](#item-1) ⭐️ 9.0/10
2. [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake&\#x27;s Jira](#item-2) ⭐️ 9.0/10
3. [AI;DR: Growing Reluctance to Read AI-Generated Content](#item-3) ⭐️ 8.0/10
4. [How to Disable or Avoid Intrusive AI Features](#item-4) ⭐️ 8.0/10
5. [Qwen 3.8 27B Achieves 52 on the Artificial Analysis Intelligence Index](#item-5) ⭐️ 8.0/10
6. [Investigation Reveals Amazon Uses Rare Books for AI Training](#item-6) ⭐️ 8.0/10
7. [Exposing Flawed Evaluation Practices in Sparse Attention and KV Cache Compression](#item-7) ⭐️ 8.0/10
8. [Critique: Efficient Channel Attention&\#x27;s 1D Convolution Lacks Topological Basis](#item-8) ⭐️ 8.0/10
9. [OpenAI&\#x27;s GPT-5.6 Sol Price Cut to 50% on OpenRouter](#item-9) ⭐️ 7.0/10
10. [Rust GPU Offloading Research Promises Safe, Portable, and Fast Execution](#item-10) ⭐️ 7.0/10
11. [GPT-5.6 Sol Vision Benchmark: Outperformed by Gemini 3.5 Flash at Lower Cost](#item-11) ⭐️ 7.0/10
12. [Judge Sets Framework for Nine PBS to Recover Archival Data from Defunct Vendor](#item-12) ⭐️ 7.0/10
13. [Sun Clock: Visualizing Sunrise, Sunset, and Golden Hour](#item-13) ⭐️ 7.0/10
14. [Dario Amodei: AI Public Distrust Is a Trust Crisis, Not a Marketing Issue](#item-14) ⭐️ 7.0/10
15. [Linear Attention Models Fail Long-Range Needle-in-Haystack on DNA Sequences](#item-15) ⭐️ 7.0/10
16. [How Bluesky&\#x27;s App Draws Its Logo on Screenshots](#item-16) ⭐️ 6.0/10
17. [Quake Shareware, a CD-ROM just a little too full](#item-17) ⭐️ 6.0/10
18. [SineKAN: Sinusoidal Activations Make KANs Faster](#item-18) ⭐️ 6.0/10
19. [SSOG-Attention: Sub-Quadratic Attention via Sum of Separable Gaussians](#item-19) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DuckDB v2.0 Preview: Quack Protocol and Semi-Structured Data Shredding](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 9.0/10

DuckDB v2.0 preview introduces the Quack client-server protocol, enabling multiple concurrent writers, and automated shredding of semi-structured JSON data for efficient storage and querying. This transforms DuckDB from an embedded analytical database into a networked, multi-writer system, broadening its applicability for real-time analytics and shared data pipelines. The JSON shredding feature significantly reduces storage costs and query latency for semi-structured data, a common pain point in modern data stacks. The Quack protocol is delivered as an extension, allowing DuckDB to function as both server and client. Shredding builds on the VARIANT type \(v1.5\) and extracts common structure into Parquet columns for compression. The preview&\#x27;s fast development pace—10,000 commits in under 6 months—has raised community questions about AI usage.

hackernews · ibotty · Aug 17, 13:46 · [Discussion](https://news.ycombinator.com/item?id=49330781)

**Background**: DuckDB is an in-process, open-source analytical database designed for fast query execution. It is often compared to SQLite for analytics, running embedded in applications without a server. The VARIANT type, introduced in v1.5, stores semi-structured data efficiently, and the v2.0 preview extends this with automatic shredding to further optimize JSON-like data.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/quack/">Quack Remote Protocol – DuckDB</a></li>
<li><a href="https://duckdb.org/2026/05/12/quack-remote-protocol">Quack: The DuckDB Client-Server Protocol – DuckDB</a></li>
<li><a href="https://parquet.apache.org/docs/file-format/types/variantshredding/">Variant Shredding - Apache Parquet</a></li>

</ul>
</details>

**Discussion**: The community shows strong enthusiasm for Quack and JSON shredding, sharing real-world use cases like runtime analytics and stream processing. A minor concern about the high commit count \(10,000\) possibly indicating heavy AI-assisted development was raised, but overall sentiment remains highly positive.

**Tags**: `#duckdb`, `#database`, `#analytics`, `#release-preview`, `#olap`

---

<a id="item-2"></a>
## [AI-Generated GitHub Copilot “Autofix” Allowed Compromise of Snowflake&\#x27;s Jira](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 9.0/10

A GitHub Copilot &\#x27;Autofix&\#x27; suggestion in Snowflake&\#x27;s CI/CD pipeline introduced a critical template injection vulnerability in a GitHub Actions workflow. This allowed an attacker to compromise the company&\#x27;s internal Jira instance. This is the first real-world case of an AI-generated autofix causing a high-impact security breach, highlighting the risks of blindly trusting AI code in CI/CD. It underscores the urgent need for static analysis and human oversight when using AI coding assistants. The vulnerability was a template injection in a GitHub Actions workflow&\#x27;s run block, where Copilot&\#x27;s suggestion to use shell expansion with user input \(e.g., TITLE=$\(echo &\#x27;$\{\{...\}\}&\#x27;\)\) led to command injection. The issue was discovered by Wiz Research&\#x27;s Red Agent team.

hackernews · galnagli · Aug 17, 14:18 · [Discussion](https://news.ycombinator.com/item?id=49331423)

**Background**: GitHub Copilot Autofix is an AI-powered feature that suggests fixes for code scanning alerts and can automatically generate pull requests. GitHub Actions uses YAML-based workflows where $\{\{ \}\} expressions are evaluated at runtime; if user input is injected without sanitization, it can lead to arbitrary command execution. Snowflake is a major cloud data platform company, and Jira is a widely used issue tracking system.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning">About autofix for code scanning - GitHub Docs</a></li>

</ul>
</details>

**Discussion**: Community members stressed the importance of using static analysis tools like zizmor for GitHub Actions, noting the template injection could have been caught. Some questioned whether the vulnerability was directly caused by Copilot Autofix, as the relevant PR did not contain the vulnerable code. There was also criticism of YAML&\#x27;s security pitfalls and a consensus on the need for human review of AI-generated code.

**Tags**: `#security`, `#ai-generated-code`, `#github-actions`, `#supply-chain`, `#copilot`

---

<a id="item-3"></a>
## [AI;DR: Growing Reluctance to Read AI-Generated Content](https://www.rickmanelius.com/p/aidr-ai-didnt-read) ⭐️ 8.0/10

A popular Hacker News discussion highlights the increasing aversion to AI-generated content, citing excessive verbosity, lack of nuance, and perceived intellectual laziness. This sentiment signals a cultural shift in online communities, where AI-generated text is increasingly seen as inauthentic and wasteful, potentially undermining trust in documentation and code reviews. Developers report that AI-generated comments and documentation are flooding codebases, making code less readable, and often contain performative or irrelevant detail. Some suggest sharing the original prompt instead of the generated output.

hackernews · mooreds · Aug 17, 19:47 · [Discussion](https://news.ycombinator.com/item?id=49336573)

**Background**: The term &\#x27;TL;DR&\#x27; \(Too Long; Didn&\#x27;t Read\) is internet slang for a summary. With the proliferation of large language models like GPT-4, AI-generated content has become common in code comments, documentation, and online posts, leading to a backlash against its verbosity and lack of original thought.

**Discussion**: Comments overwhelmingly express frustration with AI-generated verbosity and lack of originality, seeing it as a sign of disrespect. Many note that AI-generated code comments and documentation are reducing readability. A notable suggestion is to share the AI prompt instead of the output, as the prompt contains the user&\#x27;s actual intent.

**Tags**: `#AI`, `#LLM`, `#content-creation`, `#developer-experience`, `#communication`

---

<a id="item-4"></a>
## [How to Disable or Avoid Intrusive AI Features](https://www.librarian.net/notoai/) ⭐️ 8.0/10

A new comprehensive guide at NoToAI.org details how to turn off or bypass AI features in various software and services, including CarPlay, browsers, and office suites, sparking a lively community discussion. The guide addresses growing user frustration with forced AI integration, offering practical workarounds and highlighting the demand for AI-free alternatives. It embodies a broader pushback against intrusive AI in everyday tools. The guide covers disabling Siri for CarPlay, switching to AI-free browsers like LibreWolf, and using Linux or LibreOffice. Users caution that removing AI may break functions, such as CarPlay requiring Siri for certain tasks.

hackernews · ColinWright · Aug 17, 14:07 · [Discussion](https://news.ycombinator.com/item?id=49331220)

**Background**: The guide emerges as AI assistants like Siri, Copilot, and ChatGPT are increasingly embedded into operating systems, browsers, and apps, often without clear opt-out options. This raises concerns about privacy, user autonomy, and resource usage. &quot;Intrusive AI&quot; describes features that are hard to disable or operate without explicit consent. The guide distills community knowledge to help users regain control.

**Discussion**: Comments reveal strong frustration: one user noted that disabling Siri in CarPlay makes it unusable, others recommended Linux, LibreWolf, and LibreOffice, and the author \(jessamyn\) invited further suggestions. The overall sentiment is a desire for non-AI options and shared practical tips.

**Tags**: `#AI`, `#privacy`, `#software`, `#user-experience`, `#alternatives`

---

<a id="item-5"></a>
## [Qwen 3.8 27B Achieves 52 on the Artificial Analysis Intelligence Index](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 8.0/10

Qwen 3.8 27B, a 27-billion parameter model from Alibaba&\#x27;s Qwen lab, scored 52 on the Artificial Analysis Intelligence Index, matching GPT-5.6 Luna and coming within one point of the much larger GLM-5.2 \(753B\) and DeepSeek V4 Pro \(1.6T\). This demonstrates that a relatively small, open-weight model can rival much larger, closed-source models, making high-quality AI more accessible, cost-effective, and deployable on consumer hardware. The model defaults to &\#x27;xhigh&\#x27; reasoning effort, leading to excessive thinking tokens and long generation times, but can be run efficiently on laptops with 4-bit quantization, requiring about 14–16 GB of VRAM.

rss · Simon Willison · Aug 17, 23:58

**Background**: The Artificial Analysis Intelligence Index is a composite benchmark evaluating language models across reasoning, coding, knowledge, instruction following, and scientific tasks. Qwen 3.8 27B is an open-source vision-language model from Alibaba, licensed under Apache 2.0, and is the successor to Qwen 3.6 27B. Its compact size enables it to run on a single GPU or even a high-end laptop, unlike the massive models it competes with.

<details><summary>References</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>
<li><a href="https://www.yottalabs.ai/post/qwen-3-8-27b-specs-hardware-requirements-how-to-run-2026">Qwen 3.8 27B: Specs, Hardware Requirements, and How to Run It (2026) | Yotta Labs</a></li>

</ul>
</details>

**Tags**: `#ai`, `#llms`, `#qwen`, `#model-efficiency`, `#benchmarking`

---

<a id="item-6"></a>
## [Investigation Reveals Amazon Uses Rare Books for AI Training](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 8.0/10

404 Media placed an Apple AirTag in a book from a bulk order of rare books and tracked it to Amazon&\#x27;s LAS8 facility in Las Vegas. Evidence from facility signage and worker discussions suggests the books are being destructively scanned for AI training data. This investigative journalism exposes Amazon&\#x27;s covert acquisition of books for AI training, raising significant ethical and copyright concerns. It highlights the opaque practices of AI companies in sourcing training data, potentially violating authors&\#x27; rights and impacting the publishing industry. The facility&\#x27;s entrance featured a logo of a dinosaur with a book, and online forum discussions among Amazon workers confirmed that VGT3 destructively scans large volumes of books. The AirTag was placed in a book ordered by an anonymous, price-insensitive buyer, typical of such suspected AI training purchases.

rss · Simon Willison · Aug 17, 15:21

**Background**: AirTags are small tracking devices by Apple that use the Find My network to locate items. AI training data often includes large text corpora; books are valuable because they provide high-quality, long-form text. Reports have surfaced of companies buying books in bulk to scan and create training datasets, sometimes without permission or compensation to authors. This practice has been previously documented, such as the Books3 dataset, which included pirated books.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AirTag">AirTag - Wikipedia</a></li>
<li><a href="https://aicopyright.substack.com/p/has-your-book-been-used-to-train">Has your book been used to train the AI?</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#training-data`, `#copyright`, `#amazon`, `#investigative-journalism`

---

<a id="item-7"></a>
## [Exposing Flawed Evaluation Practices in Sparse Attention and KV Cache Compression](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 8.0/10

A meta-analysis reveals how sparse attention and KV cache compression methods can be deceptively made to appear effective through flawed evaluation setups, such as using undemanding retrieval tasks, inflating gains with custom kernels, and hiding weaknesses with aggregated metrics. This work warns the research community about common pitfalls in benchmarking efficient attention methods, which could lead to more rigorous evaluation standards and ultimately more reliable long-context LLM systems. Specific deceptive practices include: using single-hop retrieval without distractors, never isolating the contribution of the new method from a local window, tuning prompts and implementation while leaving baselines untouched, employing saturated benchmarks where all models already perform similarly, and aggregating scores across diverse tasks to hide failures on difficult ones like NIAH-MK3.

reddit · r/MachineLearning · /u/korec1234 · Aug 17, 12:18

**Background**: Sparse attention reduces the quadratic O\(N²\) complexity of self-attention in Transformers by restricting each query to attend to a subset of keys/values, often via patterns like sliding windows or global tokens. KV cache compression aims to reduce the memory footprint of the key-value cache during autoregressive generation by keeping only the most relevant cache entries for the current query. Both are critical for efficient long-context inference in large language models, but their evaluation can be easily gamed if not carefully designed.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Sparse_Attention">Sparse Attention</a></li>
<li><a href="https://github.com/npp369/KVCacheCompression">GitHub - npp369/KVCacheCompression: KV - cache compression ...</a></li>

</ul>
</details>

**Tags**: `#Sparse Attention`, `#KV Cache`, `#Benchmarking`, `#NLP`, `#Evaluation`

---

<a id="item-8"></a>
## [Critique: Efficient Channel Attention&\#x27;s 1D Convolution Lacks Topological Basis](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 8.0/10

A critical analysis argues that applying a 1D convolution across channel means in Efficient Channel Attention \(ECA\) has no sound topological justification, and an experiment on chess endgame tablebases shows that removing cross-channel interaction \(k=1\) performs similarly to the original ECA \(k=3\). This challenges the central hypothesis of a highly cited attention mechanism \(12k citations\), suggesting that the perceived benefit of local cross-channel interaction may be spurious, which could influence future designs of channel attention modules. The experiment used chess 6-piece tablebases as a benchmark, comparing ECA with kernel sizes k=3 \(original\), k=1 \(no cross-channel interaction\), and a center-masked variant, all achieving near 96.6% test accuracy, while a simple per-channel gate performed equally well.

reddit · r/MachineLearning · /u/arkuto · Aug 16, 10:13

**Background**: Efficient Channel Attention \(ECA\), proposed in 2019, is a lightweight channel attention module that uses a fast 1D convolution on channel-wise global average pooled features to generate channel weights, avoiding the dimensionality reduction used in Squeeze-and-Excitation \(SE\) networks. The authors argued that appropriate local cross-channel interaction is crucial for performance. The critique points out that convolutions are designed for data with spatial or temporal topology, but channel indices are arbitrary, making the 1D convolution over channels a &\#x27;cursed convolution&\#x27; with no principled basis.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention - GitHub ECA-Net: Efficient Channel Attention for Deep Convolutional ... Efficient Channel Attention - emergentmind.com Efficient Channel Attention: A Comprehensive Guide for 2025 ... IEEE Xplore 即插即用模块 ECA-Net: Efficient Channel Attention for Deep ...</a></li>
<li><a href="https://github.com/BangguWu/ECANet">ECA-Net: Efficient Channel Attention - GitHub ECA-Net: Efficient Channel Attention for Deep Convolutional ... Efficient Channel Attention - emergentmind.com Efficient Channel Attention: A Comprehensive Guide for 2025 ... IEEE Xplore 即插即用模块 ECA-Net: Efficient Channel Attention for Deep ...</a></li>

</ul>
</details>

**Tags**: `#channel attention`, `#efficient channel attention`, `#deep learning`, `#computer vision`, `#critique`

---

<a id="item-9"></a>
## [OpenAI&\#x27;s GPT-5.6 Sol Price Cut to 50% on OpenRouter](https://openrouter.ai/openai/gpt-5.6-sol) ⭐️ 7.0/10

OpenAI&\#x27;s GPT-5.6 Sol model has seen a 50% price reduction on the OpenRouter API platform, lowering the cost per token for developers and heavy users. The price cut makes the most capable GPT-5.6 model more accessible, potentially boosting adoption and intensifying competition with rivals like Claude and Grok. It also comes shortly after Stripe&\#x27;s $7 billion acquisition of OpenRouter, suggesting a strategic push to capture market share. The price cut is on OpenRouter, but the new price still faces stiff competition from Grok 4.6 at $6 per million tokens. Users note that Sol&\#x27;s efficient token usage \(&\#x27;thinking&\#x27;\) can offset costs, and some suspect the discount may rely on OpenAI&\#x27;s flex tier with fallback to Azure, potentially affecting uptime.

hackernews · Topfi · Aug 17, 21:03 · [Discussion](https://news.ycombinator.com/item?id=49337602)

**Background**: GPT-5.6 Sol is OpenAI&\#x27;s flagship model in the GPT-5.6 family, released in July 2026 alongside Luna and Terra. OpenRouter is a unified API platform that aggregates large language models from multiple providers; it was acquired by Stripe in August 2026 for over $7 billion. The price cut on OpenRouter affects the pay-per-token pricing for Sol, not the flat-rate $200/month Pro plan.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed. Heavy users welcome the cost savings, with some considering switching from Claude. However, skeptics note that OpenRouter&\#x27;s Luna model had 85% uptime after a similar cut, suggesting the Sol discount may rely on lower-tier infrastructure. Some link the move to Stripe&\#x27;s acquisition, while others point out that Grok 4.6 at $6/million tokens remains a cheaper alternative, making Sol&\#x27;s price cut less compelling.

**Tags**: `#AI`, `#LLM`, `#pricing`, `#OpenAI`, `#OpenRouter`

---

<a id="item-10"></a>
## [Rust GPU Offloading Research Promises Safe, Portable, and Fast Execution](https://arxiv.org/abs/2608.13759) ⭐️ 7.0/10

A new research paper proposes a Rust GPU offloading approach that automatically handles data movement between CPU and GPU, aiming to let developers write GPU code directly in Rust with safety and performance by default. This approach addresses the major pain point of maintaining low-level bindings and separate shader languages, making GPU programming more accessible to Rust developers and potentially reducing complexity in high-performance computing and AI inference workloads. The implementation compiles Rust code through LLVM to target GPU backends, though the community notes that directly generating PTX or SPIR-V might be more efficient; the project is under active development with no published code yet, and advanced unsafe interfaces are planned for later.

hackernews · linggen · Aug 17, 17:54 · [Discussion](https://news.ycombinator.com/item?id=49334991)

**Background**: GPU offloading is the technique of running compute-intensive code on a GPU instead of the CPU, typically requiring explicit data transfers and kernel launches. Rust is a systems language known for memory safety and concurrency. Existing offloading frameworks like OpenMP or CUDA often require C/C++ or binding layers, while this Rust-native approach aims to eliminate those extra steps and provide a unified, safe programming model.

<details><summary>References</summary>
<ul>
<li><a href="https://www.intel.com/content/www/us/en/docs/advisor/user-guide/2025-0/model-offloading-to-a-gpu.html">Model Offloading to a GPU - Intel</a></li>
<li><a href="https://enccs.github.io/openmp-gpu/target/">Offloading to GPU — OpenMP for GPU offloading documentation</a></li>

</ul>
</details>

**Discussion**: The community response is mixed: many Rust developers are excited about eliminating binding headaches and want to try it, while others question the design choice of using LLVM instead of targeting PTX or SPIR-V directly and ask whether the code has been published. Overall, the sentiment is cautiously positive, with strong interest in seeing a working implementation.

**Tags**: `#rust`, `#gpu`, `#programming-languages`, `#parallel-computing`, `#research-paper`

---

<a id="item-11"></a>
## [GPT-5.6 Sol Vision Benchmark: Outperformed by Gemini 3.5 Flash at Lower Cost](https://blog.roboflow.com/openai-gpt-5-6/) ⭐️ 7.0/10

A benchmark analysis by Roboflow compared GPT-5.6 Sol&\#x27;s vision capabilities against Gemini 3.5 Flash and other models, revealing that Gemini 3.5 Flash outperformed GPT-5.6 Sol on nearly all tasks while costing only one-third as much. This challenges the narrative that GPT-5.6 Sol is the leading vision model, indicating that for high-volume detection and counting tasks, Gemini 3.5 Flash offers superior practical value and could influence developer choices in computer vision pipelines. GPT-5.6 Sol only won in OCR, where another model, Fable, was the actual top performer. The benchmarks included pill counting and coin detection; one comment noted a possible EXIF orientation issue in a rotated coin sample, and users highlighted latency concerns for real-time robotics.

hackernews · plurby · Aug 17, 12:09 · [Discussion](https://news.ycombinator.com/item?id=49329575)

**Background**: GPT-5.6 Sol is a high-end variant of the GPT-5.6 family released by OpenAI in July 2026, targeting enterprise, coding, and scientific use. Gemini 3.5 Flash is Google&\#x27;s fast and cost-efficient multimodal model, designed for agentic workflows and large-scale deployment. Vision benchmarks evaluate a model&\#x27;s ability to parse images, count objects, and recognize text, critical for applications like automated inspection and pharmacy robots.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash">Gemini 3.5 Flash | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: Commenters widely felt the article&\#x27;s conclusion was understated, emphasizing that Gemini 3.5 Flash not only outperformed GPT-5.6 Sol on all benchmarks except OCR but did so at a fraction of the cost. Some noted GPT-5.6 Sol excels at UI design feedback, while others questioned its latency for real-time tasks and suggested including Gemini 3 Flash for a more complete comparison.

**Tags**: `#ai`, `#vision-models`, `#benchmark`, `#gpt-5.6`, `#gemini`

---

<a id="item-12"></a>
## [Judge Sets Framework for Nine PBS to Recover Archival Data from Defunct Vendor](https://current.org/2026/08/judge-sets-framework-for-nine-pbs-to-retrieve-archival-data/) ⭐️ 7.0/10

A court ruling has established a framework for Nine PBS to retrieve its archival data from Iron Mountain, where it was stored by the now-defunct vendor Open Source Storage \(OSS\) after OSS&\#x27;s bankruptcy. The judge&\#x27;s decision outlines a process for data access, addressing the legal hurdles of vendor lock-in. This case highlights the critical need for clear data custody agreements and the risks of vendor lock-in, especially when a third-party vendor goes bankrupt. It could set a precedent for how organizations can recover their data from custodians during bankruptcy, impacting industries reliant on archival and cloud services. The court appointed a special master to oversee the retrieval process, a method previously used in the TechShop bankruptcy. Iron Mountain, the storage provider, had raised concerns about data ownership and liability, but the ruling provides a legal pathway to access the data.

hackernews · qingcharles · Aug 17, 16:11 · [Discussion](https://news.ycombinator.com/item?id=49333344)

**Background**: Nine PBS is a public television station that relied on Open Source Storage, a vendor with two decades of history, to archive its digital media. OSS stored the data with Iron Mountain, a large data management company. When OSS went bankrupt, Nine PBS was unable to access its archives because Iron Mountain required a court order to release the data, as bankruptcy law often complicates asset retrieval. This situation underscores the importance of contractual agreements that directly address data custody in the event of vendor failure.

**Discussion**: The community largely agrees with the court&\#x27;s decision, viewing it as a necessary step. Commenters highlight the need for clearer regulations around contractor relationships and data custody in bankruptcy, referencing the Synapse case. Some note that Iron Mountain should have anticipated this situation, and the use of a special master is seen as a practical solution. The discussion serves as a reminder for tech professionals to include robust data retrieval clauses in contracts.

**Tags**: `#data-recovery`, `#vendor-lock-in`, `#archives`, `#legal-tech`, `#bankruptcy`

---

<a id="item-13"></a>
## [Sun Clock: Visualizing Sunrise, Sunset, and Golden Hour](https://sunclock.net/) ⭐️ 7.0/10

A web application called Sun Clock was shared on Hacker News, visualizing sunrise, sunset, golden hour, and other solar events using JavaScript. The tool is well-crafted and useful for photographers, outdoor enthusiasts, and anyone curious about daylight patterns, and its Hacker News discussion generated high-quality, constructive technical feedback. The clock relies on the suncalc library for calculations; the library author recently released a major update for higher precision. However, the golden hour is currently hardcoded as the hour before sunset, which may be inaccurate at high latitudes.

hackernews · Gecko4072 · Aug 17, 16:37 · [Discussion](https://news.ycombinator.com/item?id=49333824)

**Background**: Golden hour is the period just after sunrise or before sunset with soft, warm light, highly valued in photography. Solar position algorithms, such as the NREL Solar Position Algorithm, calculate the sun&\#x27;s azimuth and elevation from date, time, and location. The suncalc JavaScript library implements these algorithms, which Sun Clock uses to determine solar event timings.

<details><summary>References</summary>
<ul>
<li><a href="https://dictionary.cambridge.org/us/dictionary/english/golden-hour">GOLDEN HOUR | definition in the Cambridge English Dictionary</a></li>
<li><a href="https://midcdmz.nlr.gov/spa/">Solar Position Algorithm (SPA) - NREL</a></li>

</ul>
</details>

**Discussion**: The community discussion was positive, with the suncalc library author expressing delight and noting a recent precision update. Users suggested improvements like dynamic golden hour calculation, handling of polar day/night edge cases, and adding map click features. A similar tool was also shared.

**Tags**: `#web-application`, `#sun-calculations`, `#javascript`, `#visualization`, `#astronomy`

---

<a id="item-14"></a>
## [Dario Amodei: AI Public Distrust Is a Trust Crisis, Not a Marketing Issue](https://simonwillison.net/2026/Aug/16/dario-amodei/) ⭐️ 7.0/10

Dario Amodei, CEO of Anthropic, argued that the public&\#x27;s negative view of AI is a crisis of trust rooted in decades of distrust towards companies and governments, and that real-world delivery of benefits, not marketing campaigns, is the only way to regain it. This perspective from a leading AI CEO shifts the blame from AI risk communication to broader societal distrust, and insists that companies must deliver on transformative promises to earn credibility, impacting how AI firms approach public relations and product development. Amodei acknowledged that AI companies, including Anthropic, have not yet delivered on their big promises to benefit the world, and he called that the most accurate criticism, rather than focusing on messaging.

rss · Simon Willison · Aug 16, 15:05

**Background**: Dario Amodei is the CEO of Anthropic, an AI safety company known for its Claude model family, which competes with OpenAI&\#x27;s GPT. Public skepticism towards AI has grown alongside rapid deployment, with concerns about job loss, misinformation, and lack of accountability. Amodei&\#x27;s statement comes amid debates about whether AI companies should tone down risk warnings to improve public perception.

**Tags**: `#AI ethics`, `#trust`, `#public perception`, `#Anthropic`, `#Dario Amodei`

---

<a id="item-15"></a>
## [Linear Attention Models Fail Long-Range Needle-in-Haystack on DNA Sequences](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 7.0/10

A user reports that even HyenaDNA, a state-of-the-art linear attention model for genomics, achieves only ~25% accuracy \(random chance\) on a needle-in-a-haystack benchmark for DNA, while a small model at 16K context reaches 50-60%, revealing a severe degradation of long-range recall as context scales to 1M tokens. Long-range recall is critical for modeling DNA sequences, where functional elements can be millions of nucleotides apart. The failure of efficient linear attention methods on this task challenges their viability for genomic foundation models and underscores the need for architectures that preserve retrieval accuracy without quadratic complexity. The user tested HyenaDNA and their own linear attention model, both scoring ~25% on a 4-class DNA needle-in-haystack task \(chance=25%\). Architecture modifications only improved recall to 27%, and the problem worsens significantly with context length—a 16K model performed much better than those at 1M tokens.

reddit · r/MachineLearning · /u/No-Coffee-8227 · Aug 16, 07:47

**Background**: Linear attention replaces quadratic softmax attention with kernelized or low-rank approximations, scaling linearly with sequence length, making it suitable for long contexts like DNA. Needle-in-a-haystack tests measure a model&\#x27;s ability to retrieve a specific piece of information from a long sequence. HyenaDNA is a genomic foundation model based on the Hyena operator, a subquadratic attention alternative, pretrained on the human genome with up to 1 million tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2306.15794">[2306.15794] HyenaDNA: Long-Range Genomic Sequence Modeling ... GitHub - HazyResearch/hyena-dna: Official implementation for ... HyenaDNA: learning from DNA with 1 Million token context HyenaDNA: Long-Range Genomic Sequence Modeling at Single ... Benchmarking DNA foundation models for genomic and genetic ... LongSafari/hyenadna-large-1m-seqlen · Hugging Face [PDF] HyenaDNA: Long-Range Genomic Sequence Modeling at ...</a></li>
<li><a href="https://www.emergentmind.com/topics/linear-attention-mechanism">Linear Attention Mechanism</a></li>
<li><a href="https://grokipedia.com/page/needle_in_the_haystack">Needle in the Haystack</a></li>

</ul>
</details>

**Tags**: `#linear attention`, `#long-range recall`, `#DNA sequence modeling`, `#needle in a haystack`, `#machine learning`

---

<a id="item-16"></a>
## [How Bluesky&\#x27;s App Draws Its Logo on Screenshots](https://timmarinin.net/2026/bluesky-screenshots/) ⭐️ 6.0/10

Bluesky&\#x27;s mobile app automatically inserts its logo onto screenshots, a feature uncovered by developer Tim Marinin. The logo is placed in the area that would normally show the action button, and the responsible code file is named &\#x27;GrowthHack.tsx&\#x27;. This feature raises questions about user control over screenshots and the ethics of apps modifying user-captured content. As apps increasingly seek to brand or watermark shared images, this design choice could influence how other platforms approach user-generated screenshots. The logo is drawn directly onto the screenshot image rather than as an overlay, and the component is named &\#x27;GrowthHack.tsx&\#x27;, suggesting a growth-oriented motive. The insertion occurs in the area occupied by the action button, which is not visible in screenshots, thus not obscuring user content.

hackernews · gavide · Aug 17, 22:20 · [Discussion](https://news.ycombinator.com/item?id=49338459)

**Background**: Bluesky is a decentralized social media platform built on the AT Protocol, designed as an alternative to Twitter/X. It emphasizes user control and algorithmic choice. Screenshot watermarking is a practice where apps add logos or identifiers to screen captures, often for attribution or promotion. Some apps, like Snapchat, implement screenshot detection to notify users, while others prevent screenshots entirely.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bluesky_social_network">Bluesky social network</a></li>
<li><a href="https://savvyshot.app/blog/how-to-watermark-screenshots">How to Add a Watermark to Your Screenshots (and When You ...</a></li>

</ul>
</details>

**Discussion**: Community reactions are divided: some users find the logo insertion unobtrusive and preferable to perpetual watermarks, while others argue that any app modification of screenshots is hostile and a violation of user control. The naming of the file &\#x27;GrowthHack.tsx&\#x27; is seen as humorous, and parallels are drawn to Snapchat&\#x27;s screenshot notification system.

**Tags**: `#mobile apps`, `#user experience`, `#Bluesky`, `#screenshots`, `#design ethics`

---

<a id="item-17"></a>
## [Quake Shareware, a CD-ROM just a little too full](https://fabiensanglard.net/quake_shareware_cd/index.html) ⭐️ 6.0/10

A detailed retrospective examines how id Software deliberately filled the Quake shareware CD-ROM to its 650 MB capacity with dummy files, and how the disc was cracked by the group GNOMON only 39 days after its August 1996 release. This analysis illuminates the practical challenges of physical media distribution in the 1990s, the shareware model&\#x27;s reliance on limited content, and the inevitable cat-and-mouse game with crackers, offering historical insight into how game distribution evolved from CD-ROMs to digital downloads. The CD-ROM was padded with dummy files to reach the full 650 MB, the crack QCRACK appeared 39 days later displaying the message &\#x27;Pray to the one you will pay\!&\#x27;, and the disc contained the Nine Inch Nails soundtrack on audio tracks, with track 1 needing to be skipped. The shareware version could be turned into the full game by adding retail files.

hackernews · shdon · Aug 17, 22:06 · [Discussion](https://news.ycombinator.com/item?id=49338328)

**Background**: Quake, released in 1996 by id Software, was a groundbreaking first-person shooter with a fully 3D engine. The shareware model allowed free distribution of the first episode to encourage full-game purchases. CD-ROMs with 650 MB capacity were becoming standard, but many games of the era did not need that much space, so developers often filled the remaining capacity with bonus content or dummy files.

**Discussion**: Community members shared nostalgic anecdotes of cracking the disc as broke teenagers, marveling at the rapid 39-day crack release. Some recalled the influence of games like Wing Commander III in driving CD-ROM adoption, and the disc&\#x27;s value as the only CD release of the Nine Inch Nails soundtrack. Overall sentiment is fond remembrance of the era&\#x27;s technological quirks, with some suggesting the crack might have been intentionally easy.

**Tags**: `#retro-computing`, `#game-development`, `#cd-rom`, `#quake`, `#shareware`

---

<a id="item-18"></a>
## [SineKAN: Sinusoidal Activations Make KANs Faster](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 6.0/10

A research paper introduces SineKAN, a variant of Kolmogorov-Arnold Networks that replaces traditional B-spline activation functions with sinusoidal functions, achieving faster inference speeds and comparable or better performance. The work was posted on arXiv in July 2024 and later published in the MDPI journal Mathematics in 2025. This advancement could significantly reduce the computational cost of KANs, making them more practical for real-world applications and edge devices. It addresses a key bottleneck of standard KANs, potentially accelerating adoption in resource-constrained environments. SineKAN uses adaptive grids of sinusoidal functions, leveraging the fast computation of sine and cosine compared to the piecewise polynomial B-splines. The paper reports superior inference speed, and the sinusoidal activations are simpler to implement, though they may have limitations in representing certain high-frequency functions compared to splines.

reddit · r/MachineLearning · /u/jacobgorm · Aug 17, 00:46

**Background**: Kolmogorov-Arnold Networks \(KANs\) are a neural network architecture inspired by the Kolmogorov-Arnold theorem, where each weight is replaced by a learnable univariate function, typically a B-spline. B-splines are smooth piecewise polynomials but can be computationally expensive. SineKAN explores sinusoidal functions as a simpler, faster alternative, similar to how SIREN uses periodic activations for implicit neural representations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov-Arnold_Networks">Kolmogorov-Arnold Networks</a></li>
<li><a href="https://arxiv.org/abs/2407.04149">[2407.04149] SineKAN : Kolmogorov-Arnold Networks Using...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11775161/">SineKAN : Kolmogorov-Arnold Networks using sinusoidal activation ...</a></li>

</ul>
</details>

**Tags**: `#Kolmogorov-Arnold Networks`, `#activation functions`, `#sinusoidal`, `#machine learning`, `#research`

---

<a id="item-19"></a>
## [SSOG-Attention: Sub-Quadratic Attention via Sum of Separable Gaussians](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 6.0/10

SSOG-Attention introduces a new attention mechanism that replaces the standard scaled dot-product attention \(SDPA\) with a sum of separable Gaussians, reducing complexity from O\(N²·d\) to O\(N·√N·d\) while maintaining or improving performance on benchmark tasks like CIFAR-100 and ImageNet. This sub-quadratic complexity could make transformer-based models more efficient and scalable, especially for high-resolution vision tasks where the number of tokens N is large. It directly addresses the quadratic bottleneck of SDPA, potentially enabling longer sequences and faster training/inference with less memory. The method learns a few Gaussian &\#x27;atoms&\#x27; per attention head and steers them geometrically based on the query token. Because the Gaussians are factorized into separable components, the attention computation is reduced to O\(N·√N·d\). The authors report that SSOG beats SDPA on small data \(CIFAR-100\) and matches it on ImageNet while converging faster, but the work is currently self-published as a blog post and code repository without peer review.

reddit · r/MachineLearning · /u/4rtemi5 · Aug 16, 10:06

**Background**: Scaled dot-product attention \(SDPA\) is the core mechanism in transformer models, computing attention scores by taking the dot product of query and key vectors, scaled by the square root of the dimension, then applying softmax. This results in O\(N²·d\) complexity, where N is the number of tokens, making it expensive for large N. The idea of separable Gaussians refers to multivariate Gaussian functions that can be decomposed into a product of one-dimensional Gaussians, enabling efficient computation by factorizing the sum. SSOG leverages this property to approximate the attention pattern with a sum of such separable Gaussians, reducing the cost to O\(N·√N·d\).

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@kavierim/transformers-from-scratch-part-2-scaled-dot-product-attention-6c0634ce79af">Transformers From Scratch: Part 2 — Scaled Dot - Product Attention</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sum_of_normally_distributed_random_variables">Sum of normally distributed random variables - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#attention-mechanism`, `#sub-quadratic`, `#efficient-transformers`, `#computer-vision`, `#machine-learning`

---