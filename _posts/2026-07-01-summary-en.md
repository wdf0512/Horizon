---
layout: default
title: "Horizon Summary: 2026-07-01 (EN)"
date: 2026-07-01
lang: en
---

> From 35 items, 21 important content pieces were selected

---

1. [Google's AI Peer-Reviewer Handled 10K Papers at ICML/STOC, Catches 34% More Errors](#item-1) ⭐️ 9.0/10
2. [Claude Code Secretly Embeds Steganographic Marks to Detect Misuse](#item-2) ⭐️ 8.0/10
3. [US Lifts Export Controls on Claude Fable 5 and Mythos 5](#item-3) ⭐️ 8.0/10
4. [Anthropic Launches Claude Science, an AI Workbench for Scientific Research](#item-4) ⭐️ 8.0/10
5. [Anthropic Releases Claude Sonnet 5 with Performance Close to Opus 4.8 at Lower Cost](#item-5) ⭐️ 8.0/10
6. [REAP: Automatic Curation of Coding Agent Benchmarks from Production Usage](#item-6) ⭐️ 8.0/10
7. [Google's Copybara tool for code migration gains developer attention](#item-7) ⭐️ 7.0/10
8. [Google DeepMind Releases Nano Banana 2 Lite, a Distilled Fast Image Generator](#item-8) ⭐️ 7.0/10
9. [Mistral Releases Leanstral 1.5 for Automated Theorem Proving in Lean 4](#item-9) ⭐️ 7.0/10
10. [Meta AI's Brain2Qwerty: non-invasive brain-to-text decoder with open code](#item-10) ⭐️ 7.0/10
11. [CERN begins LHC Long Shutdown 3 for High-Luminosity upgrade](#item-11) ⭐️ 7.0/10
12. [Kubernetes Ported to the Browser via WebAssembly for Interactive Demos](#item-12) ⭐️ 7.0/10
13. [shot-scraper video: Record Playwright-powered agent demos](#item-13) ⭐️ 7.0/10
14. [Ornith-1.0: MIT-Licensed Self-Scaffolding LLMs for Agentic Coding](#item-14) ⭐️ 7.0/10
15. [80TB+ Astronomy Dataset Now Accessible for Crossmatching on Laptops](#item-15) ⭐️ 7.0/10
16. [Cerebras-OpenAI $20B Deal Kills API Waitlist for Smaller Companies](#item-16) ⭐️ 7.0/10
17. [Simon Willison's HTML Table Extractor Converts Pasted Tables to Multiple Formats](#item-17) ⭐️ 6.0/10
18. [A Map of 11 Million Papers by Semantic Similarity and Time](#item-18) ⭐️ 6.0/10
19. [CVIL: Free CV Interview Prep Checklist Now Covers Segmentation, OCR, and VLMs](#item-19) ⭐️ 6.0/10
20. [EML Trees Proven Universal Approximators for Continuous Functions](#item-20) ⭐️ 6.0/10
21. [Reddit User Asks if Recursive Self-Improvement is a Viable PhD Topic After ICLR Workshop](#item-21) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Google's AI Peer-Reviewer Handled 10K Papers at ICML/STOC, Catches 34% More Errors](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 9.0/10

Google deployed an agentic AI peer-reviewer at the ICML and STOC conferences, reviewing approximately 10,000 papers with a 30-minute turnaround, and the formal research paper now shows it caught 34% more mathematical errors than zero-shot prompting. This demonstrates that AI can augment human peer review at scale, potentially improving the quality and speed of scientific publishing. The 34% improvement in error detection over zero-shot prompting suggests that agentic workflows can significantly outperform simpler AI approaches, which could reshape academic peer review processes. The system used an agentic AI workflow, allowing it to pursue goals and use tools, not just a single prompt. The 30-minute turnaround per paper and the 34% improvement in detecting mathematical errors were key metrics. The paper is formally documented at arXiv:2606.28277.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Agentic AI, or AI agents, are systems that can autonomously pursue goals, use tools, and take actions with varying degrees of autonomy, often within human-defined constraints. Zero-shot prompting is a technique where an AI model is given a task without any examples or demonstrations, relying purely on its pre-trained knowledge. ICML (International Conference on Machine Learning) and STOC (Symposium on Theory of Computing) are top-tier conferences in computer science. The peer review process in these conferences is critical for ensuring research quality but faces challenges due to volume and workload.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_prompting">Zero-shot prompting</a></li>

</ul>
</details>

**Tags**: `#AI`, `#peer review`, `#automation`, `#machine learning`, `#scientific publishing`

---

<a id="item-2"></a>
## [Claude Code Secretly Embeds Steganographic Marks to Detect Misuse](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

Anthropic's Claude Code tool has been found to secretly embed steganographic marks in its API requests to detect and prevent misuse, such as unauthorized model distillation by Chinese firms. This non-transparent behavior raises significant concerns about user trust and transparency, as it involves covert monitoring of user activities without explicit disclosure, potentially impacting developers who rely on the tool for legitimate purposes. The steganographic implementation was reportedly sloppy and easily detectable via reverse engineering, suggesting it was hastily deployed. The marks are intended to identify usage by Chinese firms suspected of model distillation, but it remains unclear how this affects normal developers.

hackernews · kirushik · Jun 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=48734373)

**Background**: Steganography is the practice of hiding information within another message or file so that the presence of the hidden data is not evident. Claude Code is an AI-powered coding agent developed by Anthropic that reads codebases, edits files, and runs commands. The discovery that it covertly embeds steganographic markers in requests highlights a potential privacy and trust issue.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Steganography">Steganography</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed. Some downplay the severity, arguing the intent is clearly to combat model distillation by Chinese firms and doesn't harm normal developers. Others criticize the lack of transparency, calling it a breach of trust. Some note the sloppy implementation, while others advocate for open-source alternatives like Codex CLI to avoid such hidden behaviors.

**Tags**: `#AI`, `#steganography`, `#transparency`, `#Anthropic`, `#security`

---

<a id="item-3"></a>
## [US Lifts Export Controls on Claude Fable 5 and Mythos 5](https://twitter.com/AnthropicAI/status/2072106151890809341) ⭐️ 8.0/10

On June 30, 2026, the US Department of Commerce lifted export controls on Anthropic's Claude Fable 5 and Mythos 5, but the models now include new classifiers that block cybersecurity tasks and cause coding tasks to fall back to the older Opus 4.8 model. The lifting marks a significant policy shift, but the restrictions on cybersecurity and coding undermine trust in the predictability of US AI models, making it risky for businesses to depend on them for critical functions; it also highlights the absence of clear legal frameworks for AI export controls. Claude Fable 5 is Anthropic's most capable model for reasoning and agentic work, while Mythos 5 shares the same capabilities but is only available in limited release through Project Glasswing. The new classifiers specifically target cybersecurity tasks, and coding tasks fall back to Opus 4.8. The Commerce Department's letter was addressed to Tom Brown, Chief Compute Officer at Anthropic, and references previous letters from June 12 and 26, showing rapid government intervention.

hackernews · Pragmata · Jun 30, 23:55 · [Discussion](https://news.ycombinator.com/item?id=48740771)

**Background**: Claude Fable 5 is Anthropic's frontier model for complex reasoning and agentic automation, while Mythos 5 is a specialized model for vulnerability discovery, released only in a limited preview due to safety concerns. The US government had imposed export controls on these models, citing national security risks, but the lack of a clear legal framework for such controls has created uncertainty for the AI industry.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude Platform Docs</a></li>

</ul>
</details>

**Discussion**: The community is highly critical: users note that Fable 5's coding restrictions render it impractical for development, and the unpredictable government intervention has irreparably damaged trust in US AI companies. Many argue that without clear laws, businesses cannot safely build on these models, and the ad-hoc controls will deter investment. The letter's addressing to the Chief Compute Officer rather than the CEO is seen as unusual.

**Tags**: `#AI`, `#export controls`, `#Anthropic`, `#regulation`, `#trust`

---

<a id="item-4"></a>
## [Anthropic Launches Claude Science, an AI Workbench for Scientific Research](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic launched Claude Science on June 30, 2026, a customizable AI workbench that integrates with databases and computational tools, running a local server for secure data access and enabling auditable, reproducible research workflows. This product targets scientists in pharma, biotech, and other fields, offering a streamlined environment that reduces the need to switch between multiple tools; its local-server architecture addresses security constraints in locked-down institutional environments, potentially accelerating computational research and data science workflows. Claude Science is a workflow-focused product, not a new model; it generates auditable artifacts and supports flexible computing resources, including institutional clusters. The local server and web-based UI design is particularly suited for tightly locked-down pharma environments that restrict direct device connections.

hackernews · lebovic · Jun 30, 17:07 · [Discussion](https://news.ycombinator.com/item?id=48735770)

**Background**: Anthropic is the AI company behind Claude, a large language model competitor to OpenAI's GPT models. Previously, Anthropic released Claude Code, a coding assistant. Claude Science applies a similar AI-assisted approach to scientific research, offering a workbench that connects to databases, computational pipelines, and institutional high-performance computing (HPC) clusters, enabling researchers to perform data analysis, modeling, and visualization in a secure environment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists, is now available</a></li>
<li><a href="https://www.technologyreview.com/2026/06/30/1139987/claude-science-is-anthropics-newest-flagship-product/">Claude Science is Anthropic’s newest flagship product | MIT Technology Review</a></li>
<li><a href="https://techcrunch.com/2026/06/30/anthropics-claude-science-bets-on-workflow-not-a-new-model-to-win-over-scientists/">Anthropic’s Claude Science bets on workflow, not a new model, to win over scientists | TechCrunch</a></li>

</ul>
</details>

**Discussion**: Community discussion highlighted excitement about the local server architecture that enables use in locked-down pharma environments, and the integration with institutional HPC clusters. Some users noted that the product is more focused on data science than general 'science,' and early testing showed it can produce workable but naive results. Overall, the reception was cautiously optimistic, with many seeing value in the workflow unification and secure data access.

**Tags**: `#AI`, `#data-science`, `#Anthropic`, `#Claude`, `#product-launch`

---

<a id="item-5"></a>
## [Anthropic Releases Claude Sonnet 5 with Performance Close to Opus 4.8 at Lower Cost](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) ⭐️ 8.0/10

Anthropic released Claude Sonnet 5, offering performance close to Opus 4.8 but at lower prices, with a new tokenizer that increases token count by about 30% and intentionally reduced cyber capabilities to avoid US government blocking. The model provides near-high-end LLM capabilities at a lower cost, potentially making advanced AI more accessible, while the deliberate reduction in cyber capabilities reflects a strategy to navigate government regulation, which could influence how other AI labs release powerful models. Sonnet 5 has a 1 million token context window, 128,000 max output tokens, adaptive thinking on by default, and the same pricing per token as Sonnet 4.6 but with an effective ~30% price increase due to the new tokenizer; sampling parameters temperature, top_p, top_k are no longer supported.

rss · Simon Willison · Jun 30, 21:23

**Background**: Claude Sonnet 5 follows earlier models like Opus 4.8 and Mythos 5. Mythos 5 was initially blocked by the US government due to its high cyber capabilities, then partially reprieved after negotiations. Anthropic reduced Sonnet 5's cyber skills to avoid similar restrictions, designating it as less capable than Mythos 5 in that domain.

<details><summary>References</summary>
<ul>
<li><a href="https://natural20.beehiiv.com/p/anthropic-debuts-claude-fable-5-and-mythos-5">Anthropic Debuts Claude Fable 5 and Mythos 5</a></li>
<li><a href="https://aichief.com/news/anthropic-relaunches-mythos-5/">Anthropic Relaunches Mythos 5</a></li>

</ul>
</details>

**Discussion**: Commenters questioned the value proposition: some pointed out that for medium to high effort tasks, Opus 4.8 is more cost-effective, and that Sonnet 5's benchmarks show it's comparable to GLM-5.2 at twice the cost. Others noted weak performance in trivia, tool-calling, and puzzle solving, and expressed concern that optimizations for agentic use may degrade the developer experience.

**Tags**: `#AI`, `#Claude`, `#Anthropic`, `#Model Release`, `#LLM`

---

<a id="item-6"></a>
## [REAP: Automatic Curation of Coding Agent Benchmarks from Production Usage](https://www.reddit.com/r/MachineLearning/comments/1uk713d/reap_automatic_curation_of_coding_agent/) ⭐️ 8.0/10

The paper introduces REAP, a pipeline that automatically constructs executable coding agent benchmarks from real developer-agent interaction sessions by applying LLM-based filtering and execution auditing. This addresses the critical need for realistic, diverse evaluation of coding agents, as current static benchmarks often fail to capture real-world usage patterns, potentially leading to more robust and practical AI coding assistants. REAP uses multiple filtering stages including LLM-based task relevance checks and execution auditing to ensure benchmark reliability. The paper is dated May 2026.

reddit · r/MachineLearning · /u/julian88888888 · Jul 1, 00:50

**Background**: Coding agents are AI systems that can write, debug, and execute code interactively. Benchmarking them is essential for measuring progress, but creating benchmarks that reflect real-world complexity is challenging. REAP leverages data from production environments where developers already use coding agents, capturing authentic tasks and interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.01527">REAP: Automatic Curation of Coding Agent Benchmarks from Interactive Production Usage</a></li>

</ul>
</details>

**Tags**: `#benchmarks`, `#coding agents`, `#evaluation`, `#machine learning`, `#software engineering`

---

<a id="item-7"></a>
## [Google's Copybara tool for code migration gains developer attention](https://github.com/google/copybara) ⭐️ 7.0/10

Google's open-source Copybara tool, designed to move and sync code between repositories, has sparked a discussion on Hacker News about practical use cases and alternatives. It addresses a common pain point for teams managing monorepos or sharing code across multiple repositories, offering a lightweight alternative to full library dependency management. Users report it is most useful for simple one-way exports with history preservation, while bidirectional syncing is complex and often avoided. The tool is compared to others like Josh (used by Rust) and Meta's fbshipit, which is now archived.

hackernews · reconnecting · Jun 30, 23:45 · [Discussion](https://news.ycombinator.com/item?id=48740698)

**Background**: A monorepo is a version-control strategy where multiple projects are stored in a single repository, used by companies like Google to manage large codebases. Copybara helps extract parts of such a monorepo into standalone repos or sync code between them, which is often needed when sub-projects grow large enough to be independent or when code needs to be shared without tight coupling.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Monorepo">Monorepo</a></li>
<li><a href="https://monorepo.tools/">Monorepo Explained</a></li>

</ul>
</details>

**Discussion**: Overall, users find Copybara practical for simple exports but note that bidirectional setups are a hassle. Alternatives like Josh and fbshipit are mentioned, and some developers have built custom solutions. New users are curious about potential downsides and best practices.

**Tags**: `#code-migration`, `#monorepo`, `#version-control`, `#dev-tools`, `#google`

---

<a id="item-8"></a>
## [Google DeepMind Releases Nano Banana 2 Lite, a Distilled Fast Image Generator](https://deepmind.google/models/gemini-image/flash-lite/) ⭐️ 7.0/10

Google DeepMind launched Nano Banana 2 Lite, a distilled version of its image generation model, on June 30, 2026. It offers significantly faster generation (under 5 seconds) and improved text rendering but lacks programmatic aspect ratio control. The model makes high-quality AI image generation more accessible and affordable, enabling real-time applications and faster prototyping. Its speed improvement over the base model could broaden adoption in consumer apps and creative workflows. Distilled from Nano Banana 2, it retains strong text rendering but cannot programmatically force aspect ratios. It requires a Google One account, excluding Workspace users, and is available via AI Studio and Gemini API.

hackernews · minimaxir · Jun 30, 16:48 · [Discussion](https://news.ycombinator.com/item?id=48735444)

**Background**: Nano Banana is Google DeepMind's brand for its Gemini-based image generation models. Model distillation transfers knowledge from a large model to a smaller one, yielding faster inference with minimal quality loss. The original Nano Banana 2 is a full-sized model, while Lite is a compressed variant optimized for speed and cost.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/google-introduces-a-faster-cheaper-image-generator-with-nano-banana-2-lite/">Google introduces a faster, cheaper image generator with Nano ...</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-and-nano-banana-pro-are-generally-available">Nano Banana 2 and Nano Banana Pro available for everyone | Google Cloud Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: users praise the speed and text rendering, but many are frustrated by the Google One account requirement, which excludes Workspace users. Some criticize the lack of ChatGPT in the comparison chart, while others note real-world applications like generating stylized illustrations with character likeness.

**Tags**: `#image generation`, `#AI`, `#Google DeepMind`, `#model release`, `#distillation`

---

<a id="item-9"></a>
## [Mistral Releases Leanstral 1.5 for Automated Theorem Proving in Lean 4](https://docs.mistral.ai/models/model-cards/leanstral-1-5-26-06) ⭐️ 7.0/10

Mistral has released Leanstral 1.5, a specialized model for the Lean 4 proof assistant that improves automated theorem proving capabilities. The previous Leanstral model was deprecated on May 22nd, and this new version is available through Mistral's Labs. This release advances AI-assisted formal verification, enabling more efficient and reliable theorem proving in Lean 4, which is crucial for verifying software, hardware, and mathematical proofs. It could spur adoption of AI in formal methods and benefit the broader formal verification community. The model is designed for Lean 4, a proof assistant based on the calculus of constructions with inductive types. It is available through Mistral's Labs, but some users have reported difficulties with account setup and access. The open-source tool OpenATP will support Leanstral 1.5 via Mistral’s Vibe harness.

hackernews · vetronauta · Jun 30, 20:44 · [Discussion](https://news.ycombinator.com/item?id=48738938)

**Background**: Lean 4 is a proof assistant and functional programming language used for formal verification. Automated theorem proving (ATP) is a subfield of AI that proves mathematical theorems automatically. Large language models like Leanstral are being fine-tuned to generate proof steps in formal languages, bridging the gap between natural language and formal logic. This approach can reduce the burden on human mathematicians and engineers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>
<li><a href="https://lean-lang.org/">Lean Programming Language</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some users encountered frustrating sign-up and access issues on Mistral's platform, while others are excited about the technical integration with OpenATP. Observers noted that Leanstral is specialized for Lean 4, not other proof assistants like Coq, and that Lean 4 and Idris 2 are seen as underrated for LLM-based code generation.

**Tags**: `#AI`, `#theorem-proving`, `#Lean4`, `#Mistral`, `#formal-verification`

---

<a id="item-10"></a>
## [Meta AI's Brain2Qwerty: non-invasive brain-to-text decoder with open code](https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication/?_fb_noscript=1) ⭐️ 7.0/10

Meta AI has demonstrated Brain2Qwerty, a non-invasive brain-to-text decoder using MEG and EEG that achieves a small but statistically significant improvement over existing methods, and has released the code and dataset publicly. This work advances the possibility of communication without surgical implants, which could aid people with severe speech or motor impairments, though the technology is still far from practical use. The decoder uses a convolutional neural network and a language model; the improvement is modest but validated, and the current setup requires a large, shielded MEG scanner, limiting real-world deployment.

hackernews · alok-g · Jun 30, 21:29 · [Discussion](https://news.ycombinator.com/item?id=48739466)

**Background**: Magnetoencephalography (MEG) and electroencephalography (EEG) are non-invasive techniques that measure magnetic fields and electrical activity produced by the brain, respectively. They offer high temporal resolution, making them suitable for decoding real-time brain activity, but have lower spatial resolution than invasive methods. Decoding speech from brain signals has long been a challenge, with previous work requiring implanted electrodes or achieving limited accuracy with non-invasive sensors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Magnetoencephalography">Magnetoencephalography - Wikipedia</a></li>
<li><a href="https://my.clevelandclinic.org/health/diagnostics/17218-magnetoencephalography-meg">Magnetoencephalography (MEG): What It Is, Purpose & Uses</a></li>

</ul>
</details>

**Discussion**: Commenters note that the core idea is not new and the improvement is incremental, but praise the open release. Privacy concerns are strongly raised about the potential for neural tracking and data misuse. Others recall Facebook's earlier 2017 BCI project and speculate on combining EEG with LLMs for better results.

**Tags**: `#brain-computer-interface`, `#EEG`, `#MEG`, `#neuroscience`, `#machine-learning`

---

<a id="item-11"></a>
## [CERN begins LHC Long Shutdown 3 for High-Luminosity upgrade](https://home.cern/cern-bids-farewell-to-the-lhc-and-enters-long-shutdown-3/) ⭐️ 7.0/10

The Large Hadron Collider (LHC) has ended its physics run and entered Long Shutdown 3 (LS3), a four-year upgrade period to transform it into the High-Luminosity LHC (HL-LHC), aiming for a tenfold increase in collision power and a restart in 2030. This upgrade will enable scientists to probe rare particle physics phenomena, potentially leading to discoveries beyond the Standard Model, and impacts the global particle physics community by providing far more data for experiments like ATLAS and CMS. LS3 will involve thousands of specialists, upgrading detectors such as ATLAS's inner tracker (ITk) from 8 million to 5 billion channels; the HL-LHC will deliver proton–proton collisions at 14 TeV with an integrated luminosity of 3 ab⁻¹ for ATLAS and CMS, and the shutdown is expected to last until 2030.

hackernews · HelloUsername · Jun 29, 18:52 · [Discussion](https://news.ycombinator.com/item?id=48723484)

**Background**: The Large Hadron Collider (LHC) is the world's largest particle accelerator at CERN, colliding protons to study fundamental particles. Luminosity is a key performance indicator, proportional to the number of collisions per unit time; higher luminosity yields more data to observe rare events. The High-Luminosity LHC (HL-LHC) upgrade will increase the total collision data by a factor of ten over the original LHC, enabling precise measurements of the Higgs boson and searches for new physics such as dark matter. The LHC has undergone two previous long shutdowns to upgrade detectors and accelerators.

<details><summary>References</summary>
<ul>
<li><a href="https://home.cern/cern-bids-farewell-to-the-lhc-and-enters-long-shutdown-3/">CERN bids farewell to the LHC and enters Long Shutdown 3 – Home | CERN</a></li>
<li><a href="https://home.cern/science/long-shutdown-3/">Long Shutdown 3 – Home | CERN</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Luminosity_Large_Hadron_Collider">High Luminosity Large Hadron Collider</a></li>

</ul>
</details>

**Discussion**: Comments reflect excitement about the upgrade's scale, with a former detector developer noting the massive increase in sensor channels for ATLAS. Some lament the canceled Superconducting Super Collider (SSC) and its potential earlier discovery of the Higgs boson, while others point out that the title is overdramatic and that shutdown periods are ideal for underground tours. Overall sentiment is positive, tempered by historical what-ifs.

**Tags**: `#particle-physics`, `#CERN`, `#LHC`, `#scientific-research`, `#infrastructure`

---

<a id="item-12"></a>
## [Kubernetes Ported to the Browser via WebAssembly for Interactive Demos](https://ngrok.com/blog/i-ported-kubernetes-to-the-browser) ⭐️ 7.0/10

A developer has successfully ported a subset of Kubernetes to run entirely in the browser using WebAssembly, creating a project called 'webernetes' that simulates pod lifecycles and other cluster operations without a backend server. This enables interactive, zero-installation educational environments for learning Kubernetes concepts, and could inspire new methods for testing cloud-native applications locally with AI-assisted code generation. The webernetes project implements core Kubernetes components like kubelet, scheduler, and controller manager compiled to WebAssembly, but it does not execute actual containers; instead, it simulates services and requires custom adapters for each workload.

hackernews · peterdemin · Jun 30, 20:48 · [Discussion](https://news.ycombinator.com/item?id=48738985)

**Background**: Kubernetes is the standard container orchestration system for automating deployment, scaling, and management of containerized applications. WebAssembly is a portable binary code format that allows code written in multiple languages to run at near-native speed in web browsers, enabling complex applications to run client-side. Porting Kubernetes to the browser via WebAssembly means the cluster logic can be executed without a remote server, making it ideal for sandboxed learning and demos.

<details><summary>References</summary>
<ul>
<li><a href="https://ngrok.com/blog/i-ported-kubernetes-to-the-browser">I ported Kubernetes to the browser | ngrok blog</a></li>
<li><a href="https://github.com/ngrok/webernetes">GitHub - ngrok/webernetes: Kubernetes in the browser . · GitHub</a></li>

</ul>
</details>

**Discussion**: The community expressed strong enthusiasm, calling it a 'instant classic' and praising its educational potential for Kubernetes concepts. Some commenters highlighted the impressive workflow of testing against a simulated cluster, while others clarified that it does not run actual containers, requiring custom connectors for each service, tempering expectations for real-world use.

**Tags**: `#kubernetes`, `#webassembly`, `#browser`, `#devops`, `#education`

---

<a id="item-13"></a>
## [shot-scraper video: Record Playwright-powered agent demos](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 7.0/10

Simon Willison released shot-scraper 1.10 with a new 'video' command that records browser interactions defined in a YAML storyboard using Playwright, enabling coding agents to automatically produce video demos of their work. This feature addresses the growing need for automated visual proof of what coding agents build, making it easier to verify, share, and demonstrate agentic work, and aligns with the broader shift toward LLM-driven development workflows. The command accepts a storyboard.yml file defining scenes, actions, and server commands, supports authentication via cookie JSON files, and can output MP4 video. It also allows JavaScript injection to mock browser APIs like the clipboard.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a command-line tool by Simon Willison that uses Playwright, an open-source browser automation library from Microsoft, to take screenshots and scrape web pages. It is commonly used for automated documentation, testing, and data dashboards. The new video command extends it to record full browser sessions, making it especially useful for coding agents that need to produce demos of the features they implement.

<details><summary>References</summary>
<ul>
<li><a href="https://shot-scraper.datasette.io/">shot-scraper</a></li>
<li><a href="https://simonwillison.net/2022/Mar/10/shot-scraper/">shot-scraper: automated screenshots for documentation, built on Playwright</a></li>

</ul>
</details>

**Tags**: `#shot-scraper`, `#Playwright`, `#browser automation`, `#video recording`, `#agent demos`

---

<a id="item-14"></a>
## [Ornith-1.0: MIT-Licensed Self-Scaffolding LLMs for Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 7.0/10

DeepReinforce has released Ornith-1.0, a new MIT-licensed open-weight LLM family with four sizes (9B, 31B, 35B MoE, 397B MoE), fine-tuned on top of Gemma 4 and Qwen 3.5, achieving state-of-the-art coding performance among open models of comparable size. This release offers a permissively licensed (MIT) and highly capable coding model for agentic workflows, enabling developers to build autonomous coding agents without restrictive licensing. The self-scaffolding training strategy allows the model to manage tool calls and error recovery internally, making it a practical choice for local agentic coding applications. The 35B MoE variant (GGUF, 20GB) tested by Simon Willison demonstrated proficient agent tool use, handling multiple tool calls and even generating a pelican image at 103 tokens/second. The self-scaffolding is implemented via reinforcement learning that teaches the model to manage its own memory and tool orchestration, rather than relying on external hard-coded scaffolding.

rss · Simon Willison · Jun 29, 16:17

**Background**: Self-scaffolding refers to training a model to learn its own internal agent scaffolding — such as memory layout, retry logic, and tool orchestration — during reinforcement learning, rather than relying on externally hard-coded scaffolding. Agentic coding involves autonomous AI agents that can plan, write, test, and modify code with minimal human intervention. Mixture of Experts (MoE) is a neural network architecture that splits computation into specialized sub-networks, allowing larger models to be more efficient. The base models, Gemma 4 and Qwen 3.5, are both licensed under Apache 2.0, which is permissive and compatible with the MIT license of Ornith-1.0.

<details><summary>References</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/ornith-1-0-self-scaffolding-agentic-coding-llm-2026">Ornith-1.0: Self-Scaffolding Open Models for Agentic Coding</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-coding">What is Agentic Coding? | IBM</a></li>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#LLM`, `#coding`, `#agentic`, `#DeepReinforce`

---

<a id="item-15"></a>
## [80TB+ Astronomy Dataset Now Accessible for Crossmatching on Laptops](https://www.reddit.com/r/MachineLearning/comments/1uk7ec6/80tb_of_astronomy_for_the_hddpoor_crossmatch_the/) ⭐️ 7.0/10

A new resource called the Multimodal Universe has been released, providing over 80TB of pre-crossmatched data from 30+ astronomical surveys, accessible with just 4GB of RAM using the HATS format and LSDB library. This dramatically lowers the barrier to entry for working with massive astronomical datasets, enabling machine learning researchers and citizen scientists without access to large computing clusters to perform complex cross-matching and analysis on a standard laptop. The dataset uses the Hierarchical Adaptive Tiling Scheme (HATS) and the Large Survey DataBase (LSDB) to efficiently partition and query data, allowing crossmatching operations that traditionally required terabytes of storage and high-performance computing to run on machines with as little as 4GB of RAM.

reddit · r/MachineLearning · /u/Smith4242 · Jul 1, 01:07

**Background**: Crossmatching is the process of identifying the same astronomical objects across different surveys, each capturing different wavelengths or properties, to build a richer picture. The HATS format is a modern, efficient way to store and access large astronomical catalogs, while LSDB is a Python library that enables distributed queries on these datasets. Typically, such large-scale crossmatching requires significant infrastructure, but the Multimodal Universe and its tools make it possible on consumer hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/hugging-science/multimodal-universe-hats">80TB+ of astronomy for the HDD-poor: crossmatch the Multimodal...</a></li>
<li><a href="https://faqor.org/blog/crossmatching-jwst-and-hsc-data">Crossmatching JWST & HSC Data In LSDB: A Practical Guide</a></li>

</ul>
</details>

**Tags**: `#astronomy`, `#dataset`, `#large-scale`, `#multimodal`, `#open-science`

---

<a id="item-16"></a>
## [Cerebras-OpenAI $20B Deal Kills API Waitlist for Smaller Companies](https://www.reddit.com/r/MachineLearning/comments/1uiqhiv/cerebras_openai_deal_capacity_has_effectively/) ⭐️ 7.0/10

Cerebras’ $20 billion deal with OpenAI has pre-allocated nearly all their near-term inference capacity, making the API waitlist effectively infinite for smaller companies. This deal concentrates critical AI inference compute in one hyperscaler’s hands, potentially stifling innovation and leaving smaller startups without access to the specialized hardware they need to compete. Cerebras’ WSE-3 chips, built on a 5nm process with 4 trillion transistors and 900,000 AI cores, are specialized for high-throughput ASIC inference; the startup cited 1-2k tokens/second and tight p95 latency requirements that these chips can meet, but the supply is now fully committed to OpenAI.

reddit · r/MachineLearning · /u/Kortopi-98 · Jun 29, 12:00

**Background**: Cerebras Systems builds massive wafer-scale AI chips (the WSE-3) that are many times larger than traditional GPUs and optimized for AI inference workloads. These chips are ASICs, application-specific integrated circuits, designed for high-throughput, low-latency inference rather than training. P95 latency measures the response time below which 95% of requests complete, critical for real-time applications like coding agents. Small companies often rely on cloud APIs to access such specialized hardware without buying their own data centers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine">Cerebras Systems Unveils World’s Fastest AI Chip with ...</a></li>
<li><a href="https://www.glukhov.org/llm-performance/hardware/llm-asics/">LLM ASICs and specialized inference chips (why they matter)</a></li>
<li><a href="https://redis.io/blog/p95-latency/">P95 Latency: What It Is & Why It Matters</a></li>

</ul>
</details>

**Tags**: `#Cerebras`, `#OpenAI`, `#inference`, `#compute capacity`, `#AI startups`

---

<a id="item-17"></a>
## [Simon Willison's HTML Table Extractor Converts Pasted Tables to Multiple Formats](https://simonwillison.net/2026/Jun/29/html-table-extractor/#atom-everything) ⭐️ 6.0/10

Simon Willison released an HTML table extractor tool that accepts pasted rich text from browsers and converts detected tables into HTML, Markdown, CSV, TSV, or JSON. An update added Wikipedia search capability, automatically importing tables from pages using the Wikipedia CORS API. This tool simplifies extracting tabular data from web pages, saving time for developers, researchers, and content creators. It exemplifies a growing trend of lightweight, browser-based utilities that require no installation. The tool is available at tools.simonwillison.net/html-table-extractor. The Wikipedia search feature uses the open CORS API at `https://en.wikipedia.org/w/api.php?action=parse&...` and was implemented with the help of the Codex AI assistant.

rss · Simon Willison · Jun 29, 23:38

**Background**: Tab-separated values (TSV) is a plain-text format for tabular data where fields are separated by tab characters, widely used for data exchange. Markdown is a lightweight markup language, and CSV uses commas to separate values. Simon Willison is a developer known for creating a collection of small, browser-based paste-conversion tools that leverage the Clipboard API and modern web APIs to process data without a server.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tab-separated_values">Tab-separated values - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/techtips/what-is-a-tsv-file/">What is a TSV File and How to Open It - GeeksforGeeks</a></li>

</ul>
</details>

**Tags**: `#web development`, `#data conversion`, `#utilities`, `#HTML`, `#tools`

---

<a id="item-18"></a>
## [A Map of 11 Million Papers by Semantic Similarity and Time](https://www.reddit.com/r/MachineLearning/comments/1ujn3u5/a_map_of_the_latest_11_million_papers_split_by/) ⭐️ 6.0/10

A new interactive visualization tool called The Global Research Space has been released, mapping 11 million scientific papers from OpenAlex and arXiv by semantic similarity using SPECTER 2 embeddings and UMAP, and allowing users to slide through time slices to see trends. This tool helps researchers and the public quickly grasp macro-level trends in scientific literature, making it easier to keep up with the vast daily output of papers across disciplines. The tool encodes titles and abstracts with SPECTER 2, reduces dimensions via UMAP, and labels clusters using Voronoi cells around high-density peaks; it also supports keyword and semantic queries, and provides analytics ranking institutions, authors, and topics.

reddit · r/MachineLearning · /u/icannotchangethename · Jun 30, 11:55

**Background**: SPECTER 2 is a scientific document embedding model from Allen AI, trained on citation triplets to generate task-specific embeddings. UMAP (Uniform Manifold Approximation and Projection) is a dimensionality reduction algorithm that preserves both local and global data structure, often used for visualization. Voronoi diagrams partition a plane into regions based on proximity to seed points, here used to create non-overlapping labels around clusters of papers.

<details><summary>References</summary>
<ul>
<li><a href="https://allenai.org/blog/specter2-adapting-scientific-document-embeddings-to-multiple-fields-and-task-formats-c95686c06567">SPECTER2: Adapting scientific document embeddings to ... - Medium</a></li>
<li><a href="https://arxiv.org/abs/1802.03426">[1802.03426] UMAP: Uniform Manifold Approximation and ... How to Use UMAP — umap 0.5.8 documentation UMAP Dimensionality Reduction - An Incredibly Robust Machine ... Understanding UMAP: A Comprehensive Guide to Dimensionality ... A Comparative Study of UMAP and Other Dimensionality ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Voronoi_diagram">Voronoi diagram</a></li>

</ul>
</details>

**Tags**: `#literature-mapping`, `#visualization`, `#semantic-similarity`, `#UMAP`, `#research-tools`

---

<a id="item-19"></a>
## [CVIL: Free CV Interview Prep Checklist Now Covers Segmentation, OCR, and VLMs](https://www.reddit.com/r/MachineLearning/comments/1ujlmy2/update_on_cvil_the_free_cv_interview_prep/) ⭐️ 6.0/10

The community-driven CVIL checklist, originally created by a developer who landed a CV internship, has been updated with three new specialization tracks: Segmentation, OCR, and Vision-Language Models (VLMs). The repository was also restructured and now includes contributing guidelines to encourage community additions such as 3D vision or pose estimation. This free, phase-by-phase roadmap helps job seekers navigate the expanding landscape of CV interview topics, which now frequently include VLMs and other modern architectures. It lowers the barrier for candidates who lack structured study resources and reflects the growing industry demand for multimodal skills. The checklist is organized into phases from math foundations to CNNs, ViTs, detection, and tracking, with optional specialization tracks. Existing tracks include ReID and Deployment; the new additions are Segmentation, OCR, and VLMs. The GitHub repository is open for contributions, with several other tracks marked as open.

reddit · r/MachineLearning · /u/PolarIceBear_ · Jun 30, 10:40

**Background**: Computer vision (CV) is an AI field that enables machines to interpret visual data. Vision Transformers (ViTs) apply the transformer architecture to image patches, achieving strong results in image recognition. Vision-Language Models (VLMs) are multimodal models that jointly process images and text, powering applications like GPT-4V and Gemini; they represent a recent shift in CV research and industry expectations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision-language_model_(VLM)">Vision-language model (VLM)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#computer-vision`, `#interview-prep`, `#machine-learning`, `#resource`, `#github`

---

<a id="item-20"></a>
## [EML Trees Proven Universal Approximators for Continuous Functions](https://www.reddit.com/r/MachineLearning/comments/1uipl1t/eml_trees_are_universal_approximators_r/) ⭐️ 6.0/10

A new proof establishes that tree structures composed of a generalized EML function (with learnable parameters) can universally approximate any continuous function, extending the classic universal approximation theorem to this compositional setting. This theoretical result validates that the EML compositional framework is as expressive as neural networks in principle, potentially opening a new research direction for function approximators based on elementary function composition. It also provides a rigorous foundation for the viral EML 'trick'. The proof explicitly constructs binary operations, polynomials, hyperbolic tangent, and approximate partitions of unity using EML-type trees. Key technical challenges, such as the natural logarithm's ill-definedness for nonpositive inputs, are resolved through sign-based decompositions and affine maps. The original EML function is generalized by adding learnable parameters.

reddit · r/MachineLearning · /u/JoeGermany · Jun 29, 11:16

**Background**: The EML function is a single mathematical operator that can generate all elementary functions through composition, analogous to a NAND gate in logic. The universal approximation theorem is a cornerstone of machine learning theory, stating that certain structures, such as neural networks with hidden layers, can approximate any continuous function to arbitrary accuracy. This paper proves that EML trees—tree-like compositions of the generalized EML function—also possess this universal approximation property.

<details><summary>References</summary>
<ul>
<li><a href="https://graphicmaths.com/pure/special-functions/universal-eml-function/">GraphicMaths - A universal elementary function , EML</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universal_approximation_theorem">Universal approximation theorem</a></li>
<li><a href="https://monkfrom.earth/blogs/eml-operator-math-nand-gate">EML : The Single Operator That Generates All Math — Sameer Khan</a></li>

</ul>
</details>

**Tags**: `#universal approximation`, `#EML`, `#function composition`, `#machine learning theory`, `#mathematical foundations`

---

<a id="item-21"></a>
## [Reddit User Asks if Recursive Self-Improvement is a Viable PhD Topic After ICLR Workshop](https://www.reddit.com/r/MachineLearning/comments/1uip4yo/what_do_you_think_of_recursive_self_improvement_d/) ⭐️ 6.0/10

A Reddit user asked the r/MachineLearning community whether recursive self-improvement (RSI) is a worthwhile PhD research topic, referencing a recent ICLR workshop on the subject. The question highlights growing academic interest in RSI, a concept central to AI safety and the potential for intelligence explosion, and its recognition as a legitimate research area at top-tier conferences like ICLR. The post mentions the ICLR workshop website (recursive-workshop.github.io) but provides no further details. Recursive self-improvement involves AI systems rewriting their own code, potentially leading to superintelligence.

reddit · r/MachineLearning · /u/Successful_Bowl2564 · Jun 29, 10:52

**Background**: Recursive self-improvement (RSI) is a theoretical process where an AI system iteratively upgrades its own code, leading to rapid capability gains and an intelligence explosion. This concept is closely tied to AI safety research, as uncontrolled RSI could result in unforeseeable behaviors. The ICLR workshop on this topic suggests that the academic community is beginning to explore it formally, moving beyond speculative discussions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#recursive self improvement`, `#PhD`, `#ICLR`, `#AI safety`, `#machine learning`

---