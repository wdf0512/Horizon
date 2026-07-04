---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 27 items, 10 important content pieces were selected

---

1. [Contrastive Decoding Diffing Recovers Finetuning Data from Logits Alone](#item-1) ⭐️ 9.0/10
2. [Jamesob's guide highlights $40K+ cost of running SOTA LLMs locally](#item-2) ⭐️ 8.0/10
3. [Citizen Lab Confirms Pegasus Spyware Infected EU Lawmaker's iPhone](#item-3) ⭐️ 8.0/10
4. [SearXNG: A free internet metasearch engine](#item-4) ⭐️ 7.0/10
5. [Costco is the anti-Amazon](#item-5) ⭐️ 7.0/10
6. [Open Source AI Gap Map catalogs 421 open source AI products](#item-6) ⭐️ 7.0/10
7. [Josh W. Comeau Reports Declining Course Sales Due to AI](#item-7) ⭐️ 7.0/10
8. [Using DSPy to Evaluate and Improve Datasette Agent's SQL System Prompts](#item-8) ⭐️ 7.0/10
9. [Geoffrey Litt's 'Understand to Participate' for AI Coding Agents](#item-9) ⭐️ 7.0/10
10. [Fable's Judgement: Letting AI Models Decide Task Delegation](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Contrastive Decoding Diffing Recovers Finetuning Data from Logits Alone](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 9.0/10

Researchers introduced Contrastive Decoding Diffing (CDD), a grey-box attack that recovers verbatim fine-tuning data by comparing logit outputs of base and finetuned models, without needing weights or activations. It achieved a verbatim recovery score of 4+/5 on 19/20 model pairs, surpassing the white-box Activation Difference Lens method. This work significantly advances model inversion research, showing that even black-box logit access can leak detailed training data, with major implications for the security and privacy of fine-tuned LLMs. It may change how organizations assess data leakage risks when deploying models. CDD uses a single default configuration without per-model calibration, and works across four model families from 1B to 32B parameters. An unexpected finding was the recurrence of the fictional persona 'Dr. Elena Rodriguez' across all finetuning domains, a result of using Claude Sonnet 3.6 for synthetic data generation.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Contrastive decoding is a technique that generates text by maximizing the difference in log probabilities between a strong expert model and a weaker amateur model. In fine-tuning, a pre-trained language model is further trained on a specific dataset, which can leave traces of that data in the model's outputs. The prior Activation Difference Lens (ADL) method used activation differences between base and finetuned models to steer generation, but required full weight access and only recovered domain-level descriptions, not verbatim text.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/nlp/contrastive-decoding-in-natural-language-processing/">Contrastive Decoding in Natural Language... - GeeksforGeeks</a></li>
<li><a href="https://arxiv.org/abs/2210.15097">Contrastive Decoding : Open-ended Text Generation as Optimization</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#model inversion`, `#privacy`, `#finetuning`, `#logit analysis`

---

<a id="item-2"></a>
## [Jamesob's guide highlights $40K+ cost of running SOTA LLMs locally](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob published a comprehensive GitHub guide on building local LLM setups, and the community discussion immediately surfaced the steep hardware costs, quantization trade-offs, and performance limitations. The guide and discussion lay bare the massive financial and technical barriers to running state-of-the-art models locally, helping potential adopters realistically weigh cost, quality, and convenience. The top‑tier build starts at $40K with four $12K GPUs, but real‑world cost may exceed $50K; a more frugal option is dual RTX 3090s (48GB VRAM) for Qwen3.6‑27B. One commenter noted that GLM‑5.2 truly needs 8× H200 GPUs (≈$400K) for comfortable inference, far above the guide’s estimate.

hackernews · livestyle · Jul 3, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48775921)

**Background**: Running large language models locally requires GPUs with huge VRAM to hold the model parameters. Quantization reduces precision to shrink memory usage but can harm output quality. Unified memory architectures, like Apple Silicon, pool CPU and GPU memory, allowing larger models on cheaper hardware. The guide references top models such as Claude Opus, GPT‑5.5, DeepSeek V4, GLM‑5.2, and Qwen3.6.

**Discussion**: Commenters overwhelmingly stress the prohibitive cost of high‑end local LLM builds, with one noting that $40K equals 16.8 years of a $200/month cloud subscription. They also warn about quality degradation from heavy quantization and potential risks of backdoored models. Several users recommend affordable alternatives, such as dual RTX 3090s or unified memory systems, to run capable models like Qwen3.6‑27B or DeepSeek V4 at a fraction of the cost.

**Tags**: `#local-llm`, `#hardware`, `#cost-analysis`, `#deep-learning`, `#machine-learning`

---

<a id="item-3"></a>
## [Citizen Lab Confirms Pegasus Spyware Infected EU Lawmaker's iPhone](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

Citizen Lab forensically confirmed that the iPhone of European Parliament member Stelios Kouloglou was infected with Pegasus spyware on October 21, 2022, and again on March 6–7, 2023. The first infection overlapped with a campaign targeting Russian and Belarusian-speaking exiled journalists and activists in Europe. The infection reveals that a Pegasus customer with authorization to spy in multiple European countries may be targeting EU officials, exposing cross-border surveillance risks and a breakdown of safeguards. It highlights the potential compromise of both personal medical data and confidential government documents on a single device. The forensic analysis found that the first infection likely occurred via a zero-click exploit, and the second infections came shortly after the device was updated. Kouloglou serves on the committee investigating the use of spyware against EU citizens, and his phone was used for both parliamentary work and personal health management.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is spyware developed by the Israeli company NSO Group, capable of remotely compromising iOS and Android devices to extract messages, calls, passwords, and camera/microphone data. Citizen Lab is a University of Toronto research group that has uncovered numerous Pegasus abuses since 2016, including the 2021 Pegasus Project that revealed a list of 50,000 targeted numbers. NSO Group sells Pegasus exclusively to governments, but its misuse against journalists, activists, and politicians has been widely documented.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Greece had a scandal involving Pegasus hacks of politicians, with evidence pointing to the prime minister's office, and that EU countries like Italy, Poland, and Greece have abused the spyware. Some questioned why EU parliamentarians do not separate work and personal devices, while others suggested the attack was part of a domestic Greek operation rather than an attack on the European Parliament.

**Tags**: `#spyware`, `#cybersecurity`, `#surveillance`, `#pegasus`, `#european-parliament`

---

<a id="item-4"></a>
## [SearXNG: A free internet metasearch engine](https://github.com/searxng/searxng) ⭐️ 7.0/10

The Hacker News discussion highlights the original creator's new search project Hister, real-world daily usage experiences with SearXNG, and the AI agent tool TinySearch that wraps SearXNG. The discussion underscores the ongoing demand for self-hosted, privacy-respecting search tools, the challenges of metasearch, and the emerging role of such engines in powering local AI agents. SearXNG's original creator notes metasearch limitations; his new project Hister indexes full page content via browser rendering. Users report slower results and occasional CAPTCHA blocks, but the engine supports JSON output for RAG applications and is used by tools like TinySearch to optimize agent context.

hackernews · theanonymousone · Jul 3, 20:15 · [Discussion](https://news.ycombinator.com/item?id=48779454)

**Background**: SearXNG is a free, open-source metasearch engine that aggregates results from various search engines while preserving user privacy and not tracking users. It is a fork of the discontinued searX project. The original creator, asciimoo, has since developed Hister, a full-text indexing tool that stores browser-rendered pages for offline search. SearXNG is often self-hosted and used to provide search capabilities for local AI models and retrieval-augmented generation (RAG) applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SearXNG">SearXNG - Wikipedia</a></li>
<li><a href="https://github.com/searxng/searxng">GitHub - searxng/searxng: SearXNG is a free internet metasearch engine ...</a></li>

</ul>
</details>

**Discussion**: The community response is largely positive, with many users relying on SearXNG for daily privacy-focused search, accepting slower speeds and occasional CAPTCHA blocks. Original creator asciimoo explains his shift to Hister due to metasearch limitations. Some debate the privacy trade-off of querying multiple engines. The tool's integration with AI agents via TinySearch is highlighted as a significant use case.

**Tags**: `#search`, `#privacy`, `#open-source`, `#metasearch`, `#self-hosted`

---

<a id="item-5"></a>
## [Costco is the anti-Amazon](https://phenomenalworld.org/analysis/the-anti-amazon/) ⭐️ 7.0/10

An analysis published on Phenomenal World contrasts Costco's warehouse model, where customers drive to pick up bulk goods, with Amazon's home delivery approach, examining the social and logistical trade-offs between the two business models. This analysis questions the social value of Amazon's last-mile delivery complexity, suggesting that Costco's bulk-warehouse model may be more efficient and sustainable, which could influence how we evaluate retail logistics and urban planning. Costco avoids the expensive 'last-mile' problem by having customers transport goods themselves, shifting the cost structure from individual home deliveries to bulk freight shipments to warehouses, where customers buy in large quantities.

hackernews · bookofjoe · Jul 3, 15:14 · [Discussion](https://news.ycombinator.com/item?id=48776044)

**Background**: Costco is a membership-based warehouse club selling bulk items at low prices, requiring in-store shopping. Amazon dominates e-commerce with fast home delivery of individual packages. The 'last mile' of delivery—from distribution center to doorstep—is the most costly and complex part of the supply chain. This analysis contrasts the social and environmental implications of these two retail paradigms.

**Discussion**: Commenters debated the efficiency of Costco's model: some praised its avoidance of the last-mile problem, quoting a proverb that 'a clever person solves a problem; a wise person avoids it,' while others criticized its car-centric suburban focus and lack of variety, contrasting it with the convenience of home delivery. Several users noted the complexity of modern shopping habits, often blending in-store and online purchases.

**Tags**: `#business`, `#logistics`, `#retail`, `#economics`, `#costco`

---

<a id="item-6"></a>
## [Open Source AI Gap Map catalogs 421 open source AI products](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 7.0/10

Current AI, a non-profit public interest AI partnership with $400M in committed funding, launched the Open Source AI Gap Map v0.1. It indexes 421 open source AI products across software, models, datasets, and hardware, with the underlying data released under an MIT license on GitHub. This comprehensive, well-funded map provides a structured overview of the open source AI ecosystem, helping developers, researchers, and funders identify gaps and opportunities. It promotes transparency and collaboration in a field often dominated by proprietary efforts. The map details 421 products from 228 organizations, organized into 14 categories across 3 layers (model components, product/UX, infrastructure). The data includes 1,184 YAML files and tracks over 24,400 uncategorized artifacts, accessible via GitHub and explorable with tools like Datasette Lite.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI was founded at the AI Action Summit in Paris in February 2025 as a global partnership aiming to build a 'public option' for AI. The Gap Map builds on earlier efforts by experts from Columbia University, Mozilla, and Hugging Face to map the open source AI stack, assessing projects on openness, capability, and adoption. The goal is to reveal what's missing in the open source ecosystem so that investment and development can fill critical gaps.

<details><summary>References</summary>
<ul>
<li><a href="https://www.currentai.org/">Current AI | Building Public Interest AI Technology Together</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1 - currentai.org</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map - simonwillison.net</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#public interest`, `#software tools`

---

<a id="item-7"></a>
## [Josh W. Comeau Reports Declining Course Sales Due to AI](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 7.0/10

Josh W. Comeau, a prominent developer educator, reveals that his new course launch 'Whimsical Animations' is selling only one-third as many copies as previous launches, and overall sales of his existing courses are down significantly from last year. He attributes this decline to AI's dual impact: job market uncertainty and the availability of LLM-based tutoring. This firsthand account signals a broader disruption in the developer education industry, as AI not only dampens learning demand by threatening job security but also undercuts paid content creators by offering free AI tutoring, potentially reshaping the economics of online education. Comeau notes that multiple course creators are experiencing revenue drops of over 50%, and that LLMs are 'slurping up' their work for training and producing answers without consent or compensation, exacerbating the competitive pressure. His new course is on track to sell only about one-third of typical launch numbers.

rss · Simon Willison · Jul 3, 21:25

**Background**: Josh W. Comeau is a well-known web developer and educator who creates courses on CSS, JavaScript, and React, with a large following in the front-end community. Large language models (LLMs) like ChatGPT can generate personalized coding tutorials and answers, substituting for structured courses. The tech industry has seen layoffs and uncertainty about AI's impact on software engineering jobs, making some developers hesitant to invest in learning. Simon Willison, who shared the quote, is a prominent developer and commentator on AI's effects on software development.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LLM">LLM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#developer education`, `#industry trends`, `#LLMs`, `#economic impact`

---

<a id="item-8"></a>
## [Using DSPy to Evaluate and Improve Datasette Agent's SQL System Prompts](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything) ⭐️ 7.0/10

Simon Willison used DSPy to automatically evaluate and optimize the system prompts for Datasette Agent's SQL query feature, discovering that the prompt's advice to avoid table descriptions caused column-name guessing errors. This demonstrates a practical, automated approach to prompt engineering, potentially improving the reliability of AI-generated SQL queries in data exploration tools and reducing manual trial-and-error. The experiment used GPT-4.1 mini and nano, orchestrated by Claude Fable 5. The key improvement: include column names in the schema listing or soften the advice to always describe tables, preventing guesswork and retry loops.

rss · Simon Willison · Jul 2, 18:25

**Background**: DSPy is a framework from Stanford that lets developers define AI tasks declaratively and automatically optimize prompts. Datasette Agent is an AI assistant for Datasette, a tool for exploring and publishing data, that can execute read-only SQL queries. Claude Fable 5 is a publicly available version of Anthropic's Claude Mythos model.

<details><summary>References</summary>
<ul>
<li><a href="https://dspy.ai/">DSPy</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent: an AI assistant for Datasette to help ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>

</ul>
</details>

**Tags**: `#DSPy`, `#prompt engineering`, `#SQL`, `#Datasette`, `#AI agents`

---

<a id="item-9"></a>
## [Geoffrey Litt's 'Understand to Participate' for AI Coding Agents](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 7.0/10

Geoffrey Litt introduced the concept of 'understand to participate' at the 2026 AI Engineer World's Fair, arguing that developers must deeply understand code generated by AI agents to maintain creative participation and avoid cognitive debt. The concept highlights the risk of 'cognitive debt'—the mental overhead incurred when developers rely on AI without understanding—and underscores that maintaining comprehension is essential for creative contribution and long-term project health. Litt's talk at AIE 2026 will be available on YouTube in the coming weeks. The concept builds on Simon Willison's earlier work on cognitive debt and the challenges of AI-assisted development.

rss · Simon Willison · Jul 2, 17:07

**Background**: Cognitive debt is a term describing the mental cost of relying on AI tools without fully understanding the generated code, leading to a loss of ability to reason about and modify the software. AI coding agents, such as GitHub Copilot or Cursor, can autonomously write and refactor code, but they can produce complex, opaque changes. 'Understand to participate' argues that developers must actively learn what the agent is doing to stay effective collaborators.

<details><summary>References</summary>
<ul>
<li><a href="https://www.davidruttenberg.com/post/cognitive-debt-the-hidden-cost-of-ai-reliance-nobody-is-measuring">Cognitive Debt : The Hidden Cost of AI Reliance Nobody Is Measuring</a></li>
<li><a href="https://www.linkedin.com/pulse/cognitive-debt-when-ai-becomes-our-google-maps-k-subramanian-vnguc">Cognitive Debt : When AI Becomes Our Google Maps for Software...</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#cognitive debt`, `#human-AI collaboration`, `#software engineering`, `#AI-assisted development`

---

<a id="item-10"></a>
## [Fable's Judgement: Letting AI Models Decide Task Delegation](https://simonwillison.net/2026/Jul/3/judgement/#atom-everything) ⭐️ 6.0/10

Simon Willison shared a tip from the Claude Code team: instead of explicitly instructing the AI when to write tests or which model to use for smaller tasks, simply tell it to use its own judgment, such as with the prompt 'For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent.' This approach reduces token consumption and costs—especially timely with upcoming Fable price increases—while maintaining quality by delegating routine coding to cheaper models and reserving high-judgment tasks for the main model. The prompt caused Claude to create a project memory file with guidelines: subagents can use Sonnet for substantive implementation or Haiku for trivial edits, while design, auditing, and synthesis stay with the main model. Simon reports it's working well and his Fable allowance is depleting more slowly.

rss · Simon Willison · Jul 3, 18:51

**Background**: Fable is Anthropic's most powerful AI model, a Mythos-class model designed for autonomous coding and knowledge work. Claude Code is an AI-assisted software development tool by Anthropic, and the Claude model family includes Haiku, Sonnet, Opus, and Fable. The upcoming increase in Fable's token pricing makes cost-saving techniques like model delegation particularly relevant.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-fable-5">Claude Fable 5 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude`, `#prompt engineering`, `#development tools`, `#AI coding assistants`

---