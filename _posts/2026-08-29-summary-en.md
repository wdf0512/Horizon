---
layout: default
title: "Horizon Summary: 2026-08-29 (EN)"
date: 2026-08-29
lang: en
---

> From 27 items, 13 important content pieces were selected

---

1. [OpenAI Cuts Off Cursor Following SpaceX Acquisition](#item-1) ⭐️ 9.0/10
2. [Blog Post Argues GUIs Should Be Fully Keyboard-Driven](#item-2) ⭐️ 8.0/10
3. [Htmx 4.0 Released: Major Update for Hypermedia-Driven Frontend Library](#item-3) ⭐️ 8.0/10
4. [U.S. Sanctions Italian Hosting Collective A/I as Terrorist Organization](#item-4) ⭐️ 8.0/10
5. [AI Tools Turn Bug Rumors into Exploits, Overwhelming Open Source Maintainers](#item-5) ⭐️ 8.0/10
6. [Accidental LLM Memory System Enables Program Analysis Capabilities](#item-6) ⭐️ 8.0/10
7. [Researcher Bypasses Claude Code Auto Mode Protection with 80% Success](#item-7) ⭐️ 8.0/10
8. [Researchers Introduce HarnessOpt-Bench to Safely Measure Recursive Self-Improvement in LLMs](#item-8) ⭐️ 8.0/10
9. [Boot a Virtual iPhone Using Apple&\#x27;s Virtualization Framework](#item-9) ⭐️ 7.0/10
10. [Inception-style curved map demo for turn-by-turn navigation](#item-10) ⭐️ 7.0/10
11. [Tiny Latent Flow Transformer on RP2350 Microcontroller Generates 128x128 Faces](#item-11) ⭐️ 7.0/10
12. [py-evoFE: Automated Feature Engineering with Genetic Algorithms for Tabular ML](#item-12) ⭐️ 7.0/10
13. [Statistical ML Researchers Seek Alternative Venues as LLMs Dominate Top Conferences](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [OpenAI Cuts Off Cursor Following SpaceX Acquisition](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/) ⭐️ 9.0/10

OpenAI has announced that it is cutting off Cursor&\#x27;s access to its AI models after the AI coding assistant was acquired by SpaceX, a move that underscores the fragility of platform-dependent AI tools. This decision highlights the risks of building applications on third-party AI APIs, especially when ownership changes and competitive dynamics shift. It may accelerate the industry&\#x27;s focus on model portability and multi-provider strategies to avoid vendor lock-in. Cursor had relied on OpenAI&\#x27;s models for code generation and editing. The acquisition by SpaceX \(specifically, Elon Musk&\#x27;s xAI\) likely triggered a Terms of Service violation, as OpenAI prohibits use by competitors. This forces Cursor to pivot to its own models like Grok or other alternatives.

hackernews · meetpateltech · Aug 29, 01:47 · [Discussion](https://news.ycombinator.com/item?id=49486172)

**Background**: Cursor is an AI-powered code editor built on top of VS Code, offering features like inline code completion, chat, and agentic coding. It has integrated multiple AI models, including OpenAI&\#x27;s GPT-4 and Anthropic&\#x27;s Claude. Model portability refers to the ability to switch between underlying AI models without redesigning the application, which is critical for resilience. The acquisition by SpaceX \(or more precisely, xAI\) places Cursor under Elon Musk&\#x27;s control, making it a direct competitor to OpenAI, which Musk co-founded but later left.

<details><summary>References</summary>
<ul>
<li><a href="https://uibakery.io/blog/what-is-cursor-ai">What is Cursor AI ? Free Plan, Pricing &amp; Full Guide... | UI Bakery Blog</a></li>
<li><a href="https://nhimg.org/glossary/model-portability/">What Is Model portability? Definition &amp; Examples - nhimg.org</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed, with sadness over the loss of a versatile tool that allowed switching between OpenAI and Anthropic models. Many users note the platform risk and highlight that Anthropic had already banned xAI for similar terms-of-service violations. Some are seeking alternatives, while others point out that Cursor&\#x27;s value was in its multi-model support, and the acquisition may push them toward canceling subscriptions.

**Tags**: `#OpenAI`, `#Cursor`, `#SpaceX`, `#AI tools`, `#platform risk`

---

<a id="item-2"></a>
## [Blog Post Argues GUIs Should Be Fully Keyboard-Driven](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html) ⭐️ 8.0/10

An August 2026 blog post argues that all graphical user interfaces should be fully operable via keyboard, highlighting the decline of keyboard accessibility in modern software. The article underscores the importance of keyboard accessibility for both users with disabilities and power users, challenging the current trend of mouse-first design in web and desktop applications. The post highlights that many modern UI frameworks neglect keyboard navigation, making full keyboard support difficult, whereas older frameworks like Cocoa/AppKit built it in by default.

hackernews · ckardaris · Aug 28, 15:17 · [Discussion](https://news.ycombinator.com/item?id=49479837)

**Background**: In early graphical user interfaces like Windows 3.1, keyboard support was integrated into the operating system&\#x27;s widget toolkit, making mouse-free navigation trivial. As web technologies and custom UI frameworks became prevalent, developers often prioritized visual design and mouse interactions, leading to a gradual decline in keyboard accessibility. Many modern applications now cannot be fully used without a mouse, creating barriers for users who rely on keyboards.

**Discussion**: The community widely agrees that keyboard accessibility is crucial for accessibility and power users, often blaming modern UI frameworks for its neglect. Some users reminisce about older frameworks&\#x27; built-in keyboard support, while a dissenting view argues that not all applications need full keyboard control and that forcing it on general users is impractical.

**Tags**: `#accessibility`, `#usability`, `#keyboard-driven-uis`, `#gui-design`, `#software-development`

---

<a id="item-3"></a>
## [Htmx 4.0 Released: Major Update for Hypermedia-Driven Frontend Library](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 8.0/10

Htmx 4.0, the latest major version of the hypermedia-driven frontend library, has been officially released, building on the success of its predecessor intercooler.js and introducing new features for building dynamic web interfaces with minimal JavaScript. The release highlights the growing interest in hypermedia-driven approaches as an alternative to complex JavaScript frameworks, enabling developers to build interactive web apps with simpler server-side rendering and reduced client-side complexity. The release is accompanied by meticulously crafted documentation that is both machine-readable and human-friendly. Htmx extends HTML attributes like hx-get and hx-post to perform AJAX requests and swap content, enabling partial page updates without full reloads.

hackernews · rmsaksida · Aug 28, 13:28 · [Discussion](https://news.ycombinator.com/item?id=49478178)

**Background**: Htmx is a JavaScript library that completes HTML as a hypertext by enabling AJAX requests directly from HTML attributes, reducing the need for custom JavaScript. It is the successor to intercooler.js and was created by Carson Gross. The library embraces the hypermedia concept, where the server sends HTML fragments in response to user interactions, allowing for dynamic updates without client-side state management. This approach contrasts with Single Page Application \(SPA\) frameworks that rely heavily on client-side JavaScript and JSON APIs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely positive, with many praising htmx for bringing joy and simplicity to web development, especially when paired with Go and SQLite. Some developers express contrarian views, noting that htmx can complicate separation of concerns by forcing presentation logic into the backend. Others highlight its value for progressive enhancement and commend the exceptional documentation quality.

**Tags**: `#htmx`, `#web development`, `#hypermedia`, `#frontend`, `#release`

---

<a id="item-4"></a>
## [U.S. Sanctions Italian Hosting Collective A/I as Terrorist Organization](https://www.inventati.org/) ⭐️ 8.0/10

The U.S. State Department designated Autistici/Inventati \(A/I\), an Italian digital infrastructure collective that runs services like noblogs.org, as a Specially Designated Global Terrorist \(SDGT\) in August 2026, alleging it supports violent far-left groups. This unprecedented move treats an internet infrastructure provider as a terrorist entity, potentially creating a chilling effect on free speech, privacy-focused services, and hosting providers worldwide, especially those serving activists or dissidents. A/I provides email, mailing lists, web hosting, and the noblogs.org blogging platform for left-wing activists; it was founded in 2001 after the G8 Genoa protests. The designation, part of the Trump administration&\#x27;s broader fight against &\#x27;far-left political terrorism,&\#x27; subjects A/I&\#x27;s assets to U.S. sanctions and may disrupt services for users worldwide.

hackernews · exiguus · Aug 28, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49477854)

**Background**: Autistici/Inventati \(A/I\) is an Italian hacktivist collective that emerged from the anti-globalization movement, providing free, privacy-oriented communication tools for activists. Noblogs.org is a blogging platform hosted by A/I with a strict no-logs policy. The U.S. designation as an SDGT under Executive Order 13224 is a powerful tool typically used against terrorist groups, involving asset freezes and travel bans. This action reflects growing pressure on digital infrastructure providers under anti-terrorism laws.

<details><summary>References</summary>
<ul>
<li><a href="https://www.state.gov/releases/office-of-the-spokesperson/2026/08/designation-of-autistici-inventati-as-a-specially-designated-global-terrorist/">Designation of Autistici/Inventati as a Specially Designated ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autistici/Inventati">Autistici/Inventati - Wikipedia</a></li>
<li><a href="https://www.autistici.org/">autistici.org - Welcome to Autistici/Inventati</a></li>

</ul>
</details>

**Discussion**: Commenters are alarmed by the precedent of targeting infrastructure providers as terrorists, with some drawing parallels to I2P, Monero, Signal, and other privacy tools. Others are confused about A/I&\#x27;s actual activities, while some share links to further reading. The overall sentiment is critical of the U.S. government&\#x27;s action, viewing it as a threat to free speech and digital rights.

**Tags**: `#sanctions`, `#internet freedom`, `#free speech`, `#privacy`, `#infrastructure`

---

<a id="item-5"></a>
## [AI Tools Turn Bug Rumors into Exploits, Overwhelming Open Source Maintainers](https://anil.recoil.org/notes/rumour-is-the-exploit) ⭐️ 8.0/10

AI-powered tools are now capable of rapidly turning mere rumors of software bugs into working exploits, leading to a flood of security reports against open source projects. Maintainers are being overwhelmed by a sharp increase in disclosures, with some projects receiving more reports in a month than in the previous decade. This trend exacerbates the software quality crisis and places unsustainable pressure on volunteer open source maintainers. It highlights a growing tension between the speed of AI-assisted vulnerability discovery and the ability of the ecosystem to responsibly address and fix those issues. The rclone project received over 40 security disclosures in a single month compared to about 20 in its first 10 years, with a 75% validity rate. Even with AI tools used for triage and fix generation, handling the volume consumes significant maintainer time, and deployment of fixes remains a bottleneck.

hackernews · avsm · Aug 28, 15:58 · [Discussion](https://news.ycombinator.com/item?id=49480466)

**Background**: Exploit development is the practice of identifying software vulnerabilities and crafting code to take advantage of them. Large language models \(LLMs\) like GPT-4 are AI systems trained on vast text corpora that can generate code, analyze programs, and assist in reverse engineering. Open source software is often maintained by volunteers who rely on community contributions and responsible disclosure to fix security bugs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.offsec.com/cyberversity/exploit-development/">What is exploit development? Exploit Development 101 | OffSec</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>

</ul>
</details>

**Discussion**: Maintainers confirm the overwhelming increase in security reports, noting that many contain valid issues but the sheer volume is exhausting. Commenters also point out that even with AI-assisted fixes, the lack of organizational will to address bugs and slow deployment pipelines undermine effective remediation. Some argue that rapid exploit generation from minimal information is not new but has been democratized and scaled by LLMs, turning low-value targets into mass exploitation opportunities.

**Tags**: `#security`, `#open-source`, `#LLM`, `#exploit-development`, `#software-maintenance`

---

<a id="item-6"></a>
## [Accidental LLM Memory System Enables Program Analysis Capabilities](https://pwning.systems/posts/llm-memory-program-analysis/) ⭐️ 8.0/10

An author implemented a persistent memory system for an LLM and unexpectedly discovered that it could perform program analysis tasks, revealing new insights into how LLMs reason about code. This finding suggests that LLM memory architectures can be repurposed for formal reasoning, blending neural and symbolic AI. It could improve the reliability of coding assistants and agents by enabling more robust code understanding and verification. The memory system&\#x27;s design allowed the LLM to store and query facts about code, effectively turning it into a program analysis engine. Commenters noted the challenge of invalidating outdated facts, as changes do not automatically propagate through the knowledge base.

hackernews · matt\_d · Aug 28, 23:27 · [Discussion](https://news.ycombinator.com/item?id=49485416)

**Background**: LLMs typically operate within a fixed context window, limiting their long-term recall. Persistent memory systems extend this by storing information externally for retrieval across sessions. Program analysis is a field of computer science that automatically examines programs for properties like correctness and security. The serendipitous discovery showed that such a memory system can structure code-related facts in a way that supports formal reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/ai-memory">AI Memory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Program_analysis">Program analysis</a></li>
<li><a href="https://langchain-ai.github.io/langmem/concepts/conceptual_guide/">Long-term Memory in LLM Applications</a></li>

</ul>
</details>

**Discussion**: Commenters were enthusiastic, sharing similar approaches using Datalog, Prolog, and decision logs. They highlighted the potential of hybrid symbolic-neural systems and the common challenge of propagating fact invalidation, with several suggesting tools for integrating LLMs with formal reasoning engines.

**Tags**: `#LLM`, `#memory`, `#program analysis`, `#formal reasoning`, `#AI`

---

<a id="item-7"></a>
## [Researcher Bypasses Claude Code Auto Mode Protection with 80% Success](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/) ⭐️ 8.0/10

Johann Rehberger discovered a prompt injection attack that tricks Claude Code&\#x27;s auto mode into downloading and executing a malicious local file, bypassing the protection 80% of the time. This attack directly undermines Anthropic&\#x27;s safety claims about auto mode being effective against prompt injection, and demonstrates that the safety mechanism itself can block cleanup commands, making the agent even more dangerous. It highlights the necessity of sandboxing for coding agents. The attack tricks Claude Code into uncompressing a zip archive, then executing code that imports base64, which causes the execution of a local struct.py file extracted from the archive. In some cases, auto mode denied the agent&\#x27;s attempt to terminate the malicious process.

rss · Simon Willison · Aug 27, 22:50

**Background**: Prompt injection is a cybersecurity attack where hidden instructions in prompts or external content trick LLMs into unintended behavior. Claude Code&\#x27;s auto mode, recently made default, uses a classifier to automatically decide whether to allow commands, aiming to balance convenience and safety. Anthropic claimed it could catch dangerous commands, but this attack exploits a bypass using a zip archive and a Python import trick.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://claude.com/blog/auto-mode">Auto mode for Claude Code | Claude by Anthropic</a></li>
<li><a href="https://claude.com/blog/auto-mode-default-in-claude-code">Auto mode is now the default in Claude Code for Pro, Max, and ...</a></li>

</ul>
</details>

**Tags**: `#prompt-injection`, `#AI-safety`, `#Claude`, `#security`, `#coding-agent`

---

<a id="item-8"></a>
## [Researchers Introduce HarnessOpt-Bench to Safely Measure Recursive Self-Improvement in LLMs](https://www.reddit.com/r/MachineLearning/comments/1w052xg/can_ai_improve_itself_rsi_might_be_the_answer_r/) ⭐️ 8.0/10

Researchers introduced HarnessOpt-Bench, a benchmark that measures how well an LLM can recursively improve another agent&\#x27;s evaluation harness while using architectural isolation to prevent cheating. This addresses the critical challenge of safely evaluating recursive self-improvement—a key step toward advanced AI—while demonstrating that model choice has a larger impact on performance gains than harness selection. The benchmark holds out test data, API keys, and budget enforcement entirely outside the optimizer&\#x27;s sandbox; across 5 frontier models, model choice drove 1.8× more improvement than harness choice, and no home-field advantage was found for native harnesses.

reddit · r/MachineLearning · /u/shehio · Aug 27, 20:13

**Background**: Recursive self-improvement \(RSI\) is the idea that an AI system could rewrite its own code or enhance its capabilities, potentially leading to an intelligence explosion. An evaluation harness is the setup that provides tools, error handling, and integration for an AI agent during testing, which can significantly affect results. Sandboxing isolates a process to prevent unauthorized access to external resources, and architectural isolation enforces this by design rather than relying on instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://logicity.in/en/blog/openai-publishes-playbook-for-third-party-ai-evaluations">OpenAI Publishes Playbook for Third-Party AI Evaluations | Logicity</a></li>
<li><a href="https://www.armosec.io/blog/what-is-ai-agent-sandboxing-kubernetes-native-enforcement-explained/">What Is AI Agent Sandboxing ? Kubernetes-Native Enforcement...</a></li>

</ul>
</details>

**Tags**: `#recursive self-improvement`, `#LLM evaluation`, `#AI safety`, `#benchmarking`, `#sandboxing`

---

<a id="item-9"></a>
## [Boot a Virtual iPhone Using Apple&\#x27;s Virtualization Framework](https://github.com/Lakr233/vphone-cli) ⭐️ 7.0/10

A new command-line tool, vphone-cli, leverages Apple&\#x27;s Virtualization.framework to boot a complete virtual iPhone, providing a full iOS virtual machine distinct from the Xcode simulator. This enables a more realistic iOS testing environment than the Xcode simulator, as it boots the entire iOS operating system, allowing for system-level testing, network debugging, and other scenarios not possible with the app-only simulator. The tool requires an iOS IPSW restore image; during setup, selecting Japan or the EU as the region is problematic due to regulatory checks the VM can&\#x27;t satisfy. The virtualized iPhone lacks a virtual baseband, so cellular features are not available, but it can potentially be used for localhost browser testing with proper networking.

hackernews · hentrep · Aug 28, 23:02 · [Discussion](https://news.ycombinator.com/item?id=49485267)

**Background**: Apple&\#x27;s Virtualization.framework is a high-level API for creating virtual machines on Apple silicon and Intel Macs, used by apps like UTM and VirtualBuddy to run macOS VMs. In contrast, the Xcode iOS Simulator runs apps directly on the macOS kernel, sharing the host&\#x27;s filesystem and network stack, and does not boot a full iOS kernel. This makes the simulator unsuitable for testing low-level system behaviors, while a full virtual iPhone boots the entire iOS kernel and userland, providing a more authentic environment.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/virtualization">Virtualization | Apple Developer Documentation</a></li>
<li><a href="https://www.simplymac.com/iphone/emulate-iphone-on-mac">Emulate iPhone on Mac: Step-by-Step - SimplyMac</a></li>

</ul>
</details>

**Discussion**: The community expressed curiosity about the purpose and differences from the Xcode simulator, with some questioning what checks the VM can&\#x27;t pass for Japan/EU regions. Others asked about practical uses like localhost browser testing and whether a virtual baseband is included, indicating interest in the tool&\#x27;s capabilities and limitations.

**Tags**: `#iOS`, `#Virtualization`, `#Apple`, `#Development`, `#Testing`

---

<a id="item-10"></a>
## [Inception-style curved map demo for turn-by-turn navigation](https://www.orbify.eu/demo/) ⭐️ 7.0/10

A web demo presents a novel navigation interface that curves and distorts the map to emphasize the route ahead, mimicking the visual effect from the movie Inception. This proof-of-concept reimagines turn-by-turn navigation, potentially offering more intuitive preview of upcoming turns and lane guidance, addressing common complaints about lack of forward information in apps like Google Maps. The curved projection prioritizes the immediate road ahead but can obscure upcoming turns, especially sharp ones, causing the useful look-ahead distance to vary unpredictably. The shifting perspective may be disorienting for users accustomed to flat maps.

hackernews · smoser · Aug 28, 12:29 · [Discussion](https://news.ycombinator.com/item?id=49477564)

**Background**: The &\#x27;Inception&\#x27; effect refers to the film&\#x27;s bending cityscapes. The idea of a curved navigation map has prior art, such as Berg&\#x27;s &\#x27;Here and There&\#x27; poster \(2009\), which explored similar perspective distortions. This demo turns that concept into an interactive, real-time tool.

**Discussion**: Comments are mixed, with many praising the creative concept but criticizing its practicality: users note that the view loses crucial information just before turns, making consecutive turns difficult. Some joke about nausea, while others suggest it could be improved by adding lane guidance or rotating the view to keep the route visible. Earlier inspiration from Berg&\#x27;s 2009 &\#x27;Here and There&\#x27; poster is also acknowledged.

**Tags**: `#navigation`, `#maps`, `#UI`, `#UX`, `#concept`

---

<a id="item-11"></a>
## [Tiny Latent Flow Transformer on RP2350 Microcontroller Generates 128x128 Faces](https://www.reddit.com/r/MachineLearning/comments/1w10tax/i_implemented_a_very_tiny_image_generation_model/) ⭐️ 7.0/10

A 2.4-4M parameter latent flow transformer, quantized to int8, runs entirely on a RP2350 microcontroller, generating 128x128 face images in about 20 seconds using streaming weight DMA and ReLU² activation sparsity. This shows that generative AI can run on extremely resource-constrained microcontrollers, enabling local image generation on edge devices with privacy, low latency, and off-grid capability. The model has 12 layers, uses AdaLN-Zero conditioning and CFG, and achieves sparsity via ReLU² activation to skip computations. Weights are streamed from flash via DMA while the previous layer computes, and the total inference time is around 20 seconds.

reddit · r/MachineLearning · /u/cpldcpu · Aug 28, 19:48

**Background**: Latent Flow Transformer \(LFT\) is a architecture that compresses a block of transformer layers into a single continuous transport operator trained via flow matching, drastically reducing parameters. ReLU² is the square of the ReLU activation, promoting sparsity and enabling efficient inference on hardware. AdaLN-Zero \(Adaptive Layer Normalization with Zero initialization\) is a conditioning mechanism used in diffusion transformers, where additional scale and shift parameters are initialized to zero for stable training. These techniques together allow a generative vision model to fit and run on a microcontroller with only a few hundred KB of SRAM.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.14513">[2505.14513] Latent Flow Transformer - arXiv.org Latent Flow Transformer - arXiv.org GitHub - itz-sayak/Latent-Flow-Transformer Latent Flow Transformers (LFT) - emergentmind.com GitHub - mtkresearch/latent-flow-transformer Paper page - Latent Flow Transformer - Hugging Face Latent Flow Transformer (LFT) - emergentmind.com</a></li>
<li><a href="https://arxiv.org/abs/2402.03804">[2402.03804] ReLU$^2$ Wins: Discovering Efficient Activation ... ReLU2 Wins: Discovering Efficient Activation Functions for ... An Investigation into the MLP and Relu² Activation - Medium Rectified linear unit - Wikipedia ReLU Activation Function in Deep Learning - GeeksforGeeks The Evolution of Activation Functions: From ReLU to SwiGLU Paper page - ReLU^2 Wins: Discovering Efficient Activation ...</a></li>
<li><a href="https://arxiv.org/html/2608.09438">Unveiling the Secret of AdaLN - Zero in Diffusion Transformer</a></li>

</ul>
</details>

**Tags**: `#tinyML`, `#image generation`, `#microcontroller`, `#latent flow transformer`, `#model optimization`

---

<a id="item-12"></a>
## [py-evoFE: Automated Feature Engineering with Genetic Algorithms for Tabular ML](https://www.reddit.com/r/MachineLearning/comments/1w0788j/pyevofe_automated_evolutionary_feature/) ⭐️ 7.0/10

py-evoFE \(v0.3.0\) is a new open-source Python library that uses genetic programming to automatically discover, combine, and optimize feature transformations for tabular datasets, integrated with scikit-learn and Polars. It automates the tedious and intuition-dependent process of manual feature engineering, discovering compact, high-impact transformations that can improve model generalization while avoiding the overfitting and memory explosion of brute-force generation. It features hierarchical chaining, 40+ built-in transformers \(target encoding, manifold reduction, graph clustering\), vectorized Polars backend, caching for stateful projections, multi-fidelity screening, and an island model with Caruana ensembling, all scikit-learn compatible.

reddit · r/MachineLearning · /u/tanopereira · Aug 27, 21:33

**Background**: Genetic programming is an evolutionary algorithm that optimizes a population of programs \(here, feature recipes\) via selection, crossover, and mutation. Polars is a high-performance DataFrame library built on Apache Arrow, enabling efficient columnar operations. Feature engineering is critical for tabular models like LightGBM and XGBoost, as they often rely on well-crafted features to capture complex relationships.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Genetic_programming">Genetic programming</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polars_%28software%29">Polars (software) - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/evolutionary-feature-engineering-efe">Evolutionary Feature Engineering (EFE)</a></li>

</ul>
</details>

**Tags**: `#feature-engineering`, `#genetic-algorithms`, `#tabular-data`, `#machine-learning`, `#open-source`

---

<a id="item-13"></a>
## [Statistical ML Researchers Seek Alternative Venues as LLMs Dominate Top Conferences](https://www.reddit.com/r/MachineLearning/comments/1w0kipf/where_to_submit_statprob_ml_d/) ⭐️ 6.0/10

A researcher in statistical and probabilistic ML voices concern that top ML conferences like ICLR and NeurIPS are now dominated by LLM papers, and suggests AISTATS and UAI as more appropriate venues for their work. This shift highlights a growing tension between the mainstream ML conference ecosystem and more traditional statistical ML research, potentially marginalizing foundational work and reshaping the field&\#x27;s publication landscape. The post notes that even workshops at top conferences are heavily agentic or LLM-focused, and while some prominent statisticians still publish at the top three, the venues were never specifically intended for statistical ML.

reddit · r/MachineLearning · /u/didimoney · Aug 28, 08:16

**Background**: AISTATS \(International Conference on Artificial Intelligence and Statistics\) and UAI \(Uncertainty in Artificial Intelligence\) are long-standing conferences that focus on the intersection of AI and statistics, probabilistic methods, and uncertainty. They have traditionally been the core venues for statistical ML. The flagship conferences—NeurIPS, ICML, and ICLR—have recently seen a surge in large language model \(LLM\) papers, shifting their focus away from other subfields.

<details><summary>References</summary>
<ul>
<li><a href="https://aistats.org/aistats2025/">Home| Artificial Intelligence and Statistics Conference</a></li>
<li><a href="https://openreview.net/group?id=auai.org/UAI/2026/Conference">UAI 2026 Conference | OpenReview</a></li>

</ul>
</details>

**Tags**: `#statistical ML`, `#probabilistic ML`, `#conference venues`, `#LLM dominance`, `#academic publishing`

---