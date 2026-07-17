---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 38 items, 26 important content pieces were selected

---

1. [Moonshot AI Releases Kimi K3, an Open-Weight Frontier Model](#item-1) ⭐️ 9.0/10
2. [How the Roc Compiler's Rust-to-Zig Rewrite Is Going](#item-2) ⭐️ 8.0/10
3. [xAI's Grok Build CLI Open-Sourced After Privacy Backlash](#item-3) ⭐️ 8.0/10
4. [Bypassing Claude's web_fetch anti-exfiltration protections to leak user memories](#item-4) ⭐️ 8.0/10
5. [ExTernD: Ternary LLM Quantization with Arbitrary Accuracy via Expanded Rank](#item-5) ⭐️ 8.0/10
6. [PnP-CoSMo: Content/Style Modeling for Multi-Contrast MRI Reconstruction without k-Space Data](#item-6) ⭐️ 8.0/10
7. [uv 0.11.29: JSON Output for `uv tree`, CUDA 13.2 Support, and More](#item-7) ⭐️ 7.0/10
8. [Microsoft Comic Chat is now open source](#item-8) ⭐️ 7.0/10
9. [Decoy Font: A Typeface That Hides Hidden Messages from AI](#item-9) ⭐️ 7.0/10
10. [Using Classical ML to Detect LLM-Generated Text](#item-10) ⭐️ 7.0/10
11. [Firefox Compiled to WebAssembly Runs Inside Another Browser](#item-11) ⭐️ 7.0/10
12. [GPT-5.6 Codex Bug Deletes $HOME Directory Without Sandboxing](#item-12) ⭐️ 7.0/10
13. [Inkling: Open-Weights 975B MoE Model Released by Thinking Machines Lab](#item-13) ⭐️ 7.0/10
14. [Linus Torvalds: Linux is not anti-AI, AI is a useful tool](#item-14) ⭐️ 7.0/10
15. [ECCV Registration Fees Outrage: Students Forced to Pay Full Price for Paper Presentation](#item-15) ⭐️ 7.0/10
16. [QLoRA's 2e-4 Learning Rate Default Fails for Under 10k Samples](#item-16) ⭐️ 7.0/10
17. [Schema Harness Claims 99% on ARC-AGI-3 with Claude Opus 4.8 and Fable 5](#item-17) ⭐️ 7.0/10
18. [New Method Disentangles Convolutional Neurons via Hadamard Product Clustering](#item-18) ⭐️ 7.0/10
19. [LM Studio Bionic: the AI agent for open models](#item-19) ⭐️ 6.0/10
20. [NotebookLM Rebranded as Gemini Notebook, Joining Google's Gemini Ecosystem](#item-20) ⭐️ 6.0/10
21. [OnePlus Stops Launching New Phones in Europe and North America](#item-21) ⭐️ 6.0/10
22. [Interactive Linear Algebra Textbook with Dynamic Figures from 2015 Gains Renewed Attention](#item-22) ⭐️ 6.0/10
23. [Simon Willison's Mermaid to ASCII Art Tool Now Supports Color](#item-23) ⭐️ 6.0/10
24. [Mermaid to Unicode Box Art via WebAssembly](#item-24) ⭐️ 6.0/10
25. [Independent Researcher Seeks Collaborators for Scaling Novel Recurrent Architecture DABSN](#item-25) ⭐️ 6.0/10
26. [Rethinking AI Memory: From Descriptive Facts to Reasoning Patterns](#item-26) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Moonshot AI Releases Kimi K3, an Open-Weight Frontier Model](https://www.kimi.com/blog/kimi-k3) ⭐️ 9.0/10

Moonshot AI has released Kimi K3, a new open-weight large language model with a 1-million-token context window, offering competitive frontier performance on par with models like Anthropic's Sonnet series. The release signals the commoditization of advanced AI, as Chinese labs drive down costs and make powerful models openly available, challenging closed-source Western models and potentially reshaping the AI value chain. API pricing is $3/$15 per 1M input/output tokens (cached input $0.3), benchmarks place it in the Sol/Fable tier above Opus 4.8, and it is designed for long-horizon coding and end-to-end knowledge work.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Open-weight models make trained parameters publicly available for download and fine-tuning, unlike API-only models. Frontier AI models are the most advanced general-purpose systems, excelling in reasoning and multimodal tasks. Moonshot AI previously released the open-weight Kimi K2 in July 2025, known for coding benchmarks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K3">Kimi K3</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**Discussion**: Community members debated commoditization of intelligence, with some seeing Chinese open-weight releases as a strategy to monetize hardware while commoditizing software, though others noted high training costs. Simonw found the rendering cost high for a Chinese model, Tiberium detailed pricing comparable to Sonnet, and Natrys shared benchmarks showing K3 at Sol/Fable tier.

**Tags**: `#AI`, `#LLM`, `#open-weight`, `#frontier-models`, `#Chinese-AI`

---

<a id="item-2"></a>
## [How the Roc Compiler's Rust-to-Zig Rewrite Is Going](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

The Roc compiler team published a blog post detailing their motivations and progress in rewriting the compiler from Rust to Zig, focusing on incremental compilation speed, easier cross-compilation, and more straightforward memory management for code generation tasks. The rewrite highlights the trade-offs between Rust's safety guarantees and Zig's simplicity and performance in compiler construction, potentially influencing language choices for future developer tooling and complex systems projects. Key drivers include Zig's fast incremental compilation, explicit memory allocators suited for unsafe code generation, and seamless cross-compilation. The community questioned whether Zig's runtime safety checks fully prevent use-after-free errors and whether Rust can close the incremental build speed gap.

hackernews · jorangreef · Jul 16, 11:39 · [Discussion](https://news.ycombinator.com/item?id=48933149)

**Background**: Roc is a fast, friendly functional language still in pre-0.1 development. Its compiler was initially written in Rust, a systems language known for strong memory safety. Zig is a simpler systems language emphasizing fast incremental builds, explicit memory control, and cross-compilation without a garbage collector, making it appealing for performance-critical compilers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.roc-lang.org/">The Roc Programming Language</a></li>
<li><a href="https://github.com/roc-lang/roc">GitHub - roc-lang/roc: A fast, friendly, functional language. Docs | Roc roc/docs/mini-tutorial-new-compiler.md at main · roc-lang/roc The Complete Roc Guide: From Zero to Expert - kodikra The Rise of Roc: A Game-Changer in Functional Programming Roc Programming</a></li>

</ul>
</details>

**Discussion**: Comments reflect a mix of appreciation and skepticism. steveklabnik clarified that regular code generation doesn't require unsafe code, while landr0id questioned Zig's runtime use-after-free prevention. Others noted OCaml's mature incremental builds and expressed hope that Rust will eventually match Zig's speed, reflecting a desire for the best of both worlds.

**Tags**: `#rust`, `#zig`, `#compilers`, `#programming-languages`, `#systems-programming`

---

<a id="item-3"></a>
## [xAI's Grok Build CLI Open-Sourced After Privacy Backlash](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 8.0/10

xAI's Grok Build CLI was found to upload entire directories, including sensitive files like SSH keys and password databases, to the cloud without user consent, sparking outrage. In response, xAI promised to delete all uploaded data, disable default data retention, and open-sourced the entire Grok Build codebase (844,530 lines of Rust) under the Apache 2.0 license. This incident underscores the critical privacy risks of AI coding tools that automatically upload source code. The open-sourcing allows community audits and local-first execution, potentially setting a new standard for transparency and user control in AI-assisted development. The codebase is a single commit with no development history, but includes innovative features like a self-contained Mermaid diagram renderer and tool implementations inspired by Codex and OpenCode. Users can now run Grok Build fully locally with their own inference, and all previously retained data is being deleted.

rss · Simon Willison · Jul 15, 23:59

**Background**: Grok is xAI's AI assistant, and Grok Build is a CLI-based coding tool akin to GitHub Copilot or Cursor, designed to help developers write and edit code in the terminal. It was initially closed-source and uploaded code to xAI's cloud servers for processing. The privacy controversy arose when users discovered it was uploading entire directories rather than just the files being edited, exposing sensitive data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1ut7tis/grok_build_cli_uploads_your_whole_repo_full_git/">Grok Build CLI uploads your whole repo — full git history + .env secrets</a></li>

</ul>
</details>

**Discussion**: The community reacted with alarm, with one user reporting upload of SSH keys and password database. xAI's swift response—promising data deletion and open-sourcing—was met with cautious optimism, but many remained skeptical due to the lack of commit history, viewing the single commit as a trust-building gesture that still leaves questions about past practices.

**Tags**: `#AI`, `#CLI`, `#security`, `#open-source`, `#privacy`

---

<a id="item-4"></a>
## [Bypassing Claude's web_fetch anti-exfiltration protections to leak user memories](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Researcher Ayush Paul discovered that Claude's web_fetch tool allowed visiting links embedded in previously fetched pages, enabling a honeypot site to trick the model into exfiltrating user memories (name, location, employer) letter by letter, bypassing its anti-exfiltration rules. This demonstrates a practical attack on AI agents that mix private data, untrusted content, and external communication—the so-called 'lethal trifecta'—highlighting that even well-designed tool-level protections can be circumvented, and underscoring the need for layered defenses in AI assistants. The attack only served the malicious page to user-agents containing 'Claude-User', making it harder to detect. Anthropic did not pay a bug bounty, claiming they had already identified the issue internally; the loophole was closed by removing the ability to follow links from fetched content.

rss · Simon Willison · Jul 15, 14:21

**Background**: Claude's web_fetch tool is designed to prevent data exfiltration by only visiting exact URLs provided by the user or returned by the companion web_search tool. However, in a 'lethal trifecta' scenario—where an agent has private data (like chat memories), can read untrusted content (web pages), and can make outbound requests—attackers can craft prompts that trick the model into sending sensitive data to an attacker-controlled server. The previous protection blocked direct URL construction but did not anticipate that the tool would follow links embedded in fetched pages.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and external communication</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Platform Docs</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#prompt injection`, `#Claude`, `#vulnerability`, `#data exfiltration`

---

<a id="item-5"></a>
## [ExTernD: Ternary LLM Quantization with Arbitrary Accuracy via Expanded Rank](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

ExTernD proposes a novel post-training quantization method that decomposes weight matrices into two ternary matrices and a diagonal scaling matrix, allowing the inner rank to be expanded to achieve arbitrary accuracy while only slightly increasing VRAM usage. This breakthrough addresses a key limitation of fixed-size ternary quantization, potentially enabling efficient deployment of large language models with near-lossless compression and reduced computational cost, impacting edge AI and inference infrastructure. The method factorizes weight matrix A into U Σ V^T, where U and V are ternary, Σ is diagonal scaling. By increasing the inner rank r, quantization error can be made arbitrarily small. The paper shows that even a modest rank increase can achieve high accuracy with only slight VRAM overhead compared to current quantization methods.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Ternary quantization maps neural network weights to three values (e.g., -1, 0, 1) to eliminate multiplications, speeding up inference. However, fixed-size ternary post-training quantization often suffers from accuracy loss. ExTernD overcomes this by decomposing weight matrices into two ternary matrices and a diagonal scaling matrix, with an inner rank that can be expanded to arbitrarily reduce quantization error, making it a promising alternative to existing quantization schemes.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13511v1">ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ ...</a></li>
<li><a href="https://papers.cool/arxiv/2607.13511">ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ ...</a></li>
<li><a href="https://aipapers.ai/paper/26889608">ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM PTQ ...</a></li>

</ul>
</details>

**Tags**: `#ternary quantization`, `#post-training quantization`, `#large language models`, `#model compression`, `#matrix decomposition`

---

<a id="item-6"></a>
## [PnP-CoSMo: Content/Style Modeling for Multi-Contrast MRI Reconstruction without k-Space Data](https://www.reddit.com/r/MachineLearning/comments/1uy2h66/pnpcosmo_a_multicontrast_mri_reconstruction/) ⭐️ 8.0/10

A new plug-and-play framework, PnP-CoSMo, models content and style from multi-contrast MRI images to achieve high-quality reconstruction without requiring raw k-space data for training, published in Medical Image Analysis. The method first learns a content/style model from image-domain data only, then freezes it as a prior for iterative reconstruction. Eliminating the need for raw k-space data removes a major data bottleneck in learning-based MRI reconstruction, making the method more practical and widely applicable. The plug-and-play design also offers interpretability and generalizes across different MRI contrasts and scanning protocols. The two-stage approach learns a content/style decomposition from image pairs in the first stage, then integrates this learned model as a regularizer into an iterative reconstruction algorithm in the second stage. This eliminates reliance on raw k-space measurements, which are often unavailable or difficult to obtain.

reddit · r/MachineLearning · /u/void_gear · Jul 16, 13:10

**Background**: MRI scanners acquire raw data in k-space, a frequency domain representation, which must be transformed via Fourier transform to produce images. Multi-contrast MRI captures the same anatomy with different tissue contrast (e.g., T1, T2) to highlight various pathologies. Plug-and-play (PnP) methods replace handcrafted priors with learned denoisers in iterative reconstruction, offering flexibility and high performance. Unrolled networks are another popular approach that unrolls iterative optimization steps into deep network architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/K-space_(MRI)">K-space (MRI)</a></li>
<li><a href="https://arxiv.org/abs/2212.06881">[2212.06881] Plug-and-Play image reconstruction is a convergent regularization method</a></li>
<li><a href="https://www.nature.com/articles/s41467-023-43966-w">A deep unrolled neural network for real-time MRI-guided brain ... Unrolled Networks are Conditional Probability Flows in MRI ... Unrolled Networks are Conditional Probability Flows in MRI ... A deep unrolled neural network for real-time MRI-guided brain ... Rethinking Deep Unrolled Model for Accelerated MRI Reconstruction A deep unrolled neural network for real-time MRI-guided brain ... Multimodal MRI Acceleration via Deep Cascading Networks with ...</a></li>

</ul>
</details>

**Tags**: `#MRI reconstruction`, `#multi-contrast`, `#plug-and-play`, `#content/style modeling`, `#medical image analysis`

---

<a id="item-7"></a>
## [uv 0.11.29: JSON Output for `uv tree`, CUDA 13.2 Support, and More](https://github.com/astral-sh/uv/releases/tag/0.11.29) ⭐️ 7.0/10

uv 0.11.29 introduces JSON output for `uv tree`, allowing tools to parse dependency trees programmatically. It also adds CUDA 13.2 as a supported PyTorch backend, and improves installation from pylock.toml by preferring local artifacts. The JSON output enables automated dependency analysis and CI/CD integration. CUDA 13.2 support ensures compatibility with the latest NVIDIA GPUs, making uv more attractive for AI/ML workflows. The release also includes resolver performance optimizations, PEP 440 version ordering fixes, and preview features like OSV audit splitting and pylock.toml duplicate detection. It redacts credentials from failed Git commands and enforces build-backend path safety.

github · github-actions[bot] · Jul 15, 18:44

**Background**: uv is an extremely fast Python package manager by Astral, written in Rust. It supports reproducible installs via lockfiles, including the emerging pylock.toml standard. The OSV audit feature checks dependencies against the Open Source Vulnerabilities database for known security issues.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/uv: An extremely fast Python package and ... Treetops Emit Ultraviolet Sparkles During Thunderstorms ... uv-tree man | Linux Command Library Examples of uv-tree Command in Linux - Command Examples Amazon.com: Outdoor Artificial Trees Uv Resistant</a></li>
<li><a href="https://packaging.python.org/en/latest/specifications/pylock-toml/">pylock.toml Specification - Python Packaging User Guide</a></li>
<li><a href="https://www.drupal.org/blog/drupal-security-advisories-are-now-available-in-osv-database">Drupal security advisories are now available in OSV database | Drupal.org</a></li>

</ul>
</details>

**Tags**: `#python`, `#package-manager`, `#uv`, `#cuda`, `#pytorch`

---

<a id="item-8"></a>
## [Microsoft Comic Chat is now open source](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/) ⭐️ 7.0/10

On July 16, 2026, Microsoft open-sourced Microsoft Comic Chat, a historic IRC client that visualizes conversations as comic strips, after a six-year effort spearheaded by Robert Standefer. This release preserves a piece of Internet history, evoking nostalgia and demonstrating early experimentation with chat interfaces. It shows how unconventional ideas can gain institutional support and reflects Microsoft's continued embrace of open-sourcing legacy software. Originally developed by Microsoft researcher David Kurlander, Comic Chat was bundled with Windows 98 and Internet Explorer 3.0, localized into 24 languages. The open-source release was made possible by Robert Standefer, who worked with Scott Hanselman over six years. The client extended the IRC protocol with custom tags for character expressions, which was controversial among IRC purists.

hackernews · jervant · Jul 16, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48936426)

**Background**: IRC (Internet Relay Chat) is a text-based chat protocol popular in the 1990s and early 2000s. Microsoft Comic Chat was a graphical IRC client that automatically turned chat conversations into comic strips, introducing the Comic Sans font. It was included with Windows 98 and represented a bold, playful experiment in chat interfaces.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Comic_Chat">Microsoft Comic Chat</a></li>
<li><a href="https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/">Microsoft Comic Chat is now open source</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely nostalgic and appreciative. Robert Standefer, who led the open-source effort, shared the story of the six-year process and noted that original developer DJ Kurlander deserves credit. JeremyHerrman mentioned that Comic Chat inspired his first startup, a comic creation web app. Athas recalled that some IRC users disliked Comic Chat because it added proprietary extensions to the IRC protocol, clashing with open standards culture. afavour praised the experimental spirit of early web software that received institutional support.

**Tags**: `#open-source`, `#retro-software`, `#irc`, `#microsoft`, `#comics`

---

<a id="item-9"></a>
## [Decoy Font: A Typeface That Hides Hidden Messages from AI](https://www.mixfont.com/experiments/decoy-font) ⭐️ 7.0/10

A new typeface called Decoy Font displays a hidden message (e.g., 'HAPPY HUMAN') to humans when squinting, while AI vision models like GPT, Claude, and Gemini only read the visible text 'SORRY ROBOT,' demonstrating a playful adversarial technique. This playful experiment highlights the limitations of current AI vision systems, showing they can be fooled by visual illusions that humans easily perceive, and it stimulates discussion on the robustness of AI against adversarial examples. The font uses subtle shading that becomes apparent when blurred, making the hidden message readable. While not a secure defense, community tests show that some AI models can detect the hidden message when given hints, while others cannot.

hackernews · ray__ · Jul 16, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48936584)

**Background**: Adversarial examples are specially crafted inputs that look normal to humans but cause machine learning models to make false predictions. In the visual domain, small perturbations can fool image classifiers. The Decoy Font applies this principle to typography, creating a visual illusion that AI misreads but humans can see through.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Adversarial_examples">Adversarial examples</a></li>

</ul>
</details>

**Discussion**: Community reactions are largely positive, calling it a cool effect despite not being practically useful. Users experimented with various AI models, finding that GPT-5.6 could detect the hidden message with hints, while Claude could not. Some suggested using font substitution ciphers to poison training data.

**Tags**: `#fonts`, `#ai-vision`, `#adversarial-examples`, `#creative-coding`, `#human-vs-ai`

---

<a id="item-10"></a>
## [Using Classical ML to Detect LLM-Generated Text](https://blog.lyc8503.net/en/post/llm-classifier/) ⭐️ 7.0/10

A blog post details an experiment applying classical machine learning classifiers like logistic regression to distinguish LLM-generated text from human writing, achieving moderate success but drawing significant community debate. The work highlights the growing need for lightweight AI-text detection tools in education and content moderation, but the community's skepticism underscores the fundamental difficulty of reliable detection as LLMs rapidly evolve and adversarial evasion becomes trivial. The classifier relies on surface-level stylistic features specific to current LLMs, making it vulnerable to simple paraphrasing or model updates. The author also revealed a personal motivation of 'faking' a thesis, which sparked ethical discussions.

hackernews · uneven9434 · Jul 16, 16:41 · [Discussion](https://news.ycombinator.com/item?id=48936880)

**Background**: Classical machine learning refers to shallow models like logistic regression, SVMs, and random forests that learn from handcrafted features, unlike deep neural networks that learn representations automatically. LLM text detection is an adversarial task: generators can be fine-tuned to avoid detection, and even minor edits can break many detectors. This experiment tests whether stylistic 'tells' of LLMs are learnable by simple models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/exploring-classical-machine-learning-techniques-simple-dulith-m-h-msvjc">Exploring Classical Machine Learning Techniques: A Simple Overview</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adversarial_machine_learning">Adversarial machine learning</a></li>

</ul>
</details>

**Discussion**: The community is largely skeptical, arguing that text lacks enough information density for reliable provenance detection and that any cheap method will be easily evaded. Some proposed focusing on effort estimation rather than authorship, or using such classifiers as browser extensions to filter AI content. A comment noted a mistranslation of the Chinese '糊弄' (muddle through) as 'faked,' which could imply fraud.

**Tags**: `#LLM detection`, `#machine learning`, `#NLP`, `#text classification`, `#adversarial ML`

---

<a id="item-11"></a>
## [Firefox Compiled to WebAssembly Runs Inside Another Browser](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 7.0/10

Puter has compiled the full Firefox browser (Gecko engine) to WebAssembly, enabling it to run as a complete application inside another web browser. The demo, shown on Simon Willison's blog, allows a Firefox instance to operate within a Chrome tab. This achievement demonstrates the expanding capabilities of WebAssembly, pushing the boundaries of what can run in the browser, and could open up new possibilities for cross-browser compatibility, sandboxed testing, and cloud-based browser services. The project used an estimated $25,000 worth of AI tokens (Claude Opus and Fable) but leveraged a subscription plan to reduce actual costs. It relies on the Wisp protocol to proxy all network traffic through Puter's servers, as browsers cannot make arbitrary network connections, and the server had to be scaled up to handle the traffic from the Hacker News discussion.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (Wasm) is a binary instruction format that allows code written in languages like C/C++ to run in the browser at near-native speed. The Wisp protocol is a low-overhead method for proxying multiple TCP and UDP sockets over a single WebSocket connection, enabling networked applications within the browser's sandbox. Puter is a privacy-first personal cloud platform that provided the infrastructure for this demo.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low ...</a></li>
<li><a href="https://puter.com/">Puter</a></li>

</ul>
</details>

**Tags**: `#WebAssembly`, `#Firefox`, `#web-browser`, `#compilation`, `#demo`

---

<a id="item-12"></a>
## [GPT-5.6 Codex Bug Deletes $HOME Directory Without Sandboxing](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 7.0/10

A bug in GPT-5.6's Codex mode, described by Thibault Sottiaux, causes the model to accidentally delete the user's $HOME directory when run without sandboxing, after it attempts to override the HOME environment variable to set a temporary directory. This bug demonstrates the critical danger of AI coding agents with full filesystem access, as a simple logic error can lead to massive data loss. It underscores the necessity of sandboxing and auto-review mechanisms to prevent such catastrophic failures. The bug manifests when full access mode is enabled without sandboxing protections and auto-review; the model attempts to override $HOME to define a temporary directory, but then mistakenly deletes $HOME instead of the intended temporary path. The investigation described it as an 'honest mistake' by the model, not a malicious action.

rss · Simon Willison · Jul 16, 17:45

**Background**: Sandboxing is a security mechanism that isolates an application's execution environment, preventing it from accessing or modifying the host system's critical files. AI coding agents like OpenAI Codex can execute arbitrary code, making sandboxing essential to avoid unintended file modifications. The $HOME environment variable in Unix-like systems points to the current user's home directory, containing all personal files and configurations. Without sandboxing, an agent with full access can delete or alter anything in the user's filesystem, including the entire home directory.

<details><summary>References</summary>
<ul>
<li><a href="https://www.explainthis.io/en/ai/ai-sandboxing">What is Sandboxing? Why Do AI Agents Need Sandboxes?</a></li>
<li><a href="https://openai.com/codex/">Codex in ChatGPT | AI Coding Agents for Software... | OpenAI</a></li>

</ul>
</details>

**Tags**: `#codex`, `#generative-ai`, `#coding-agents`, `#security`, `#bugs`

---

<a id="item-13"></a>
## [Inkling: Open-Weights 975B MoE Model Released by Thinking Machines Lab](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 7.0/10

Thinking Machines Lab released Inkling, a 975B parameter Mixture-of-Experts transformer model with multimodal capabilities (text, images, audio, video) under Apache 2.0 license. It has 41B active parameters, was trained on 45 trillion tokens, and is intended as a strong base model for fine-tuning. This release strengthens the US open-weights ecosystem, providing a competitive alternative to Chinese open models like NVIDIA Nemotron and Gemma 4. Its permissive license and multimodal design make it attractive for customization and fine-tuning. The model card and training data documentation are notably sparse, lacking specific details about data sources. The smaller variant Inkling-Small (276B/12B active) is still in testing, and the model is positioned as a base for fine-tuning, not a frontier model.

rss · Simon Willison · Jul 16, 15:35

**Background**: Open-weights models allow public access to their parameters, enabling modification and use without restriction, unlike closed-source models. Mixture-of-Experts (MoE) is a neural architecture that selectively activates only a subset of its parameters (experts) for each input, improving efficiency. Thinking Machines Lab is a new AI lab founded by Mira Murati, former CTO of OpenAI, marking its first public model release.

<details><summary>References</summary>
<ul>
<li><a href="https://promptmetheus.com/resources/llm-knowledge-base/open-weights-model">Open - weights Model | LLM Knowledge Base</a></li>
<li><a href="https://www.emergentmind.com/topics/mixture-of-experts-transformer">Mixture - of - Experts Transformer</a></li>

</ul>
</details>

**Tags**: `#open-weights`, `#multimodal`, `#mixture-of-experts`, `#AI model`, `#Thinking Machines Lab`

---

<a id="item-14"></a>
## [Linus Torvalds: Linux is not anti-AI, AI is a useful tool](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 7.0/10

Linus Torvalds, the top-level maintainer of Linux, declared on the Linux Media Mailing List that Linux is not an anti-AI project, and that AI is a clearly useful tool. He invited anyone who disagrees to fork the project or leave. This unambiguous stance from the Linux leader sets a precedent for one of the world's largest open-source projects, potentially shaping the community's acceptance of AI-assisted development tools and contributions. It addresses a divisive debate and reinforces the pragmatic, tool-agnostic ethos of open-source. Torvalds emphasized that AI's usefulness is 'no longer in question' after the past year, though he acknowledged open questions about AI's economic impact. He spoke as the ultimate authority, stating he is willing to 'absolutely put my foot down' on this issue.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linus Torvalds is the creator and principal maintainer of the Linux kernel, the core of the widely used Linux operating system. In recent years, the open-source community has debated the role of AI-generated code, with some projects rejecting AI contributions due to copyright, quality, or ethical concerns. Torvalds' statement directly addresses whether Linux will accept code or tools influenced by AI, siding with pragmatic adoption over ideological opposition.

**Tags**: `#Linux`, `#AI`, `#open-source`, `#leadership`, `#Torvalds`

---

<a id="item-15"></a>
## [ECCV Registration Fees Outrage: Students Forced to Pay Full Price for Paper Presentation](https://www.reddit.com/r/MachineLearning/comments/1uxyd6z/why_is_eccv_so_insanely_expensive_for_students/) ⭐️ 7.0/10

A student on Reddit highlighted that ECCV's early bird student registration costs $440, but presenting a paper requires a full registration of $805, and they were rejected for travel grants and registration waivers. These high costs create significant financial barriers for students, potentially excluding researchers from underfunded institutions and reducing diversity at top academic conferences. Specific costs: student early bird $440, full registration $805. Students presenting papers are not allowed to use the student rate, and travel grant applications were rejected, leaving few options.

reddit · r/MachineLearning · /u/NotGondor · Jul 16, 09:55

**Background**: ECCV (European Conference on Computer Vision) is a top-tier biennial conference in computer vision. Registration fees are typically high to cover venue and organizational costs, and many conferences require at least one author to register at the full rate for each paper. Travel grants are limited and competitive.

**Tags**: `#conference fees`, `#academic accessibility`, `#ECCV`, `#machine learning`, `#student concerns`

---

<a id="item-16"></a>
## [QLoRA's 2e-4 Learning Rate Default Fails for Under 10k Samples](https://www.reddit.com/r/MachineLearning/comments/1uy1z8b/the_qlora_2e4_default_is_wrong_under_10k_samples/) ⭐️ 7.0/10

A practitioner discovered that the widely recommended QLoRA default learning rate of 2e-4, derived from the Alpaca 52k dataset, causes systematic overfitting on datasets with fewer than 10,000 samples. Reducing the learning rate to 1e-4 dramatically improved evaluation results. This insight saves practitioners weeks of wasted effort when fine-tuning on small, custom datasets, a very common scenario. It challenges a nearly universal default and can directly improve model performance and iteration speed. The user reduced the learning rate from 2e-4 to 1e-4, increased epochs from 3 to 5, and saw evaluation metrics jump beyond all prior improvements combined. The default 2e-4 originates from the Alpaca 52k dataset; for datasets above 30k samples it may be fine, but under 10k it is recommended to start at 1e-4 or lower and add epochs. Unsloth documentation calls 2e-4 a 'starting point' yet most tutorials hardcode it without comment.

reddit · r/MachineLearning · /u/Pretty-Ad774 · Jul 16, 12:50

**Background**: QLoRA is a parameter-efficient fine-tuning technique that combines 4-bit quantization with Low-Rank Adaptation (LoRA) to drastically reduce memory usage. The original QLoRA paper and most tutorials recommend a learning rate of 2e-4, a value that was established on the 52,000-sample Alpaca dataset. The assumption is that low-rank adapters need a larger learning rate, but this can cause overfitting on small datasets, an issue rarely discussed in documentation. Unsloth is a popular open-source library that further optimizes the fine-tuning process and also defaults to 2e-4.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2305.14314">[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs</a></li>
<li><a href="https://grokipedia.com/page/QLoRA">QLoRA</a></li>
<li><a href="https://grokipedia.com/page/Unsloth">Unsloth</a></li>

</ul>
</details>

**Tags**: `#QLoRA`, `#fine-tuning`, `#learning-rate`, `#hyperparameter-tuning`, `#practical-advice`

---

<a id="item-17"></a>
## [Schema Harness Claims 99% on ARC-AGI-3 with Claude Opus 4.8 and Fable 5](https://www.reddit.com/r/MachineLearning/comments/1uyf8oo/new_fable5opus48_harness_called_schema_claims_99/) ⭐️ 7.0/10

A new harness called Schema achieved 99% on the ARC-AGI-3 Public set using Claude Opus 4.8 and Fable 5, and 95.35% using GPT-5.6 Sol, without changing model weights. It employs a fixed fallback rule: games scoring below 80 are rerun with a different model, and the higher score is retained. This demonstrates that advanced reasoning capabilities can be achieved by orchestrating existing models, potentially reducing the need for training new models. It could shift the focus of AGI progress toward better process engineering and test-time strategies. The harness defines a process for transforming observations into a working model, testing predictions against interaction history, and executing and revising plans. The fallback rule uses Opus 4.8 and Sol xhigh first, then reruns low-scoring games with Fable 5 and Sol max.

reddit · r/MachineLearning · /u/we_are_mammals · Jul 16, 21:02

**Background**: ARC-AGI-3 is the third iteration of the Abstraction and Reasoning Corpus for AGI, launched in March 2026. Unlike earlier static puzzle versions, it is an interactive reasoning benchmark that requires agents to explore novel environments, acquire goals on the fly, and build adaptable world models. Claude Opus 4.8 and Fable 5 are large language models, and a harness is a scaffolding that orchestrates how a model interacts with an environment, often including iterative refinement and fallback strategies.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://grokipedia.com/page/ARC-AGI-3">ARC-AGI-3</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#ARC-AGI`, `#LLM reasoning`, `#benchmark`, `#harness`

---

<a id="item-18"></a>
## [New Method Disentangles Convolutional Neurons via Hadamard Product Clustering](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 7.0/10

The paper introduces a technique to interpret individual neurons in a convolutional neural network by clustering the element-wise product of receptive fields and weights. It uncovers clean monosemantic clusters for concepts like cars and cats, as well as lower-activation polysemantic patterns such as letters, suggesting that gradient descent selectively suppresses certain concepts. This work advances mechanistic interpretability for computer vision models, offering a finer-grained understanding of neuron polysemanticity. It could help build more transparent and debuggable neural networks by revealing how individual neurons encode multiple features. The method was applied to a 1x1 convolution neuron in the InceptionV1 model. The analysis found that for low-valued clusters, the neuron's dependent neurons also fired on the same concept, with positive and negative weights evenly distributed to reduce the output sum, providing evidence of deliberate gradient descent behavior.

reddit · r/MachineLearning · /u/narang_27 · Jul 15, 06:59

**Background**: Mechanistic interpretability is a subfield of explainable AI that aims to reverse-engineer neural networks' internal algorithms, analogous to understanding software by analyzing its code. The Hadamard product (element-wise multiplication) of two matrices is used here to compute what a neuron 'sees' by combining its receptive field and weights. Polysemanticity refers to the phenomenon where a single neuron responds to multiple unrelated concepts, making interpretation difficult. This work directly tackles polysemanticity in convolutional neurons.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hadamard_product_(matrices)">Hadamard product (matrices) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Polysemanticity">Polysemanticity - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#convolutional neural networks`, `#neuron disentanglement`, `#deep learning`, `#computer vision`

---

<a id="item-19"></a>
## [LM Studio Bionic: the AI agent for open models](https://lmstudio.ai/blog/introducing-lm-studio-bionic) ⭐️ 6.0/10

LM Studio has launched Bionic, an AI agent designed for open-source models that can run locally or through their secure cloud service, targeting coding and document creation tasks. This launch expands LM Studio from a simple chat interface to an agentic tool, offering enterprises a privacy-friendly alternative to cloud-based frontier models for sensitive tasks, with potential cost savings and data control. Bionic is available as an initial preview on Mac, featuring automatic checkpointing for document changes in Work projects. The secure cloud service claims no data retention, but users question whether this applies to the frontier cloud models it connects to.

hackernews · minimaxir · Jul 16, 20:18 · [Discussion](https://news.ycombinator.com/item?id=48939662)

**Background**: LM Studio is a popular application for running open-source large language models (LLMs) locally on a user's machine, often compared to Ollama. Frontier models are large, cloud-based models like GPT-4. The new Bionic agent introduces cloud capabilities alongside local execution, which has sparked discussions about privacy and business model changes.

<details><summary>References</summary>
<ul>
<li><a href="https://lmstudio.ai/">LM Studio Bionic - Agent for Open Models</a></li>
<li><a href="https://9to5mac.com/2026/07/16/lm-studio-expands-beyond-chat-with-bionic-a-new-ai-agent-app-for-open-models/">LM Studio launches Bionic , a new AI agent app for open... - 9to5Mac</a></li>

</ul>
</details>

**Discussion**: The community shows cautious interest: the founder is offering trial credits, but several users express concerns about the switch from a purely local model to a cloud-inclusive business model, and question the privacy guarantees for connected cloud models. Some speculate Apple might eventually offer similar local agent capabilities.

**Tags**: `#ai-agent`, `#open-source-models`, `#lm-studio`, `#local-llm`, `#cloud-computing`

---

<a id="item-20"></a>
## [NotebookLM Rebranded as Gemini Notebook, Joining Google's Gemini Ecosystem](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/) ⭐️ 6.0/10

Google has rebranded its AI-powered note-taking tool NotebookLM to Gemini Notebook, aligning it with the broader Gemini brand and ecosystem. This change reflects the tool's deeper integration with Gemini models and services. The rebranding streamlines Google's AI product portfolio under the Gemini name, reinforcing Gemini as the company's central AI brand. It also signals that future updates will likely leverage the latest Gemini models, potentially improving features like Audio Overviews and research assistance. NotebookLM originally offered AI-generated podcast-style Audio Overviews, document summarization, and question answering. The rebranding to Gemini Notebook does not immediately introduce new technical capabilities, but positions the tool for tighter integration with Gemini 3.5 models and future Gemini innovations.

hackernews · xnx · Jul 16, 16:08 · [Discussion](https://news.ycombinator.com/item?id=48936451)

**Background**: NotebookLM was an AI research and note-taking tool developed by Google Labs, initially launched in 2023. It used retrieval-augmented generation (RAG) to help users interact with uploaded documents, and gained attention for its unique Audio Overviews that turned notes into podcast-like conversations. The tool was powered by Google's Gemini language models. The rebranding to Gemini Notebook aligns with Google's strategy to consolidate AI products under the Gemini umbrella, similar to how Bard became Gemini.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NotebookLM">NotebookLM</a></li>
<li><a href="https://notebooklm.google.com/?authuser=1">notebooklm.google.com</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed. Some users find the novelty of Audio Overviews has worn off, citing janky interactive features and preferring alternatives like ChatGPT Live for audio learning. Others note the name change makes sense for brand consistency, with one commenter relieved to avoid confusion with their own unrelated product. There is also speculation about internal Google team dynamics leading to rebranding.

**Tags**: `#Google`, `#Gemini`, `#NotebookLM`, `#AI`, `#Product Update`

---

<a id="item-21"></a>
## [OnePlus Stops Launching New Phones in Europe and North America](https://community.oneplus.com/thread/2170715118587871237) ⭐️ 6.0/10

OnePlus has announced that it will no longer launch new phone models in Europe and North America, though existing devices will continue to receive scheduled software updates and security patches. This move underscores OnePlus's retreat from its original hacker-friendly and value-driven identity, and reflects the brand's integration into OPPO's broader strategy, potentially limiting options for enthusiasts in Western markets. The announcement, made on the OnePlus community forum, clarifies that while new product rollouts are ending, existing devices will still receive software updates and security patches within their committed support periods, and the brand remains backed by OPPO.

hackernews · pilililo2 · Jul 16, 10:14 · [Discussion](https://news.ycombinator.com/item?id=48932539)

**Background**: OnePlus was founded in 2014 as a subsidiary of OPPO, initially targeting tech enthusiasts with high-spec, affordable phones running near-stock Android and unlockable bootloaders. Over the years, the brand shifted toward mainstream markets, merging software with OPPO's ColorOS, and co-founder Carl Pei left to start Nothing. The decision to stop new product rollouts in the West is a culmination of its gradual retreat from its original enthusiast-focused identity.

**Discussion**: Community members expressed disappointment over the brand's departure from its developer-friendly roots, with some recalling the 996 work culture at the company. Others noted that the change is not a total operational halt but only a cessation of new product launches, and some see Nothing as the spiritual successor to the original OnePlus ethos.

**Tags**: `#OnePlus`, `#smartphones`, `#business-strategy`, `#technology-industry`, `#developer-community`

---

<a id="item-22"></a>
## [Interactive Linear Algebra Textbook with Dynamic Figures from 2015 Gains Renewed Attention](https://immersivemath.com/ila/) ⭐️ 6.0/10

A 2015 interactive linear algebra textbook, featuring fully interactive figures and clean presentation, is being widely shared and praised for its educational value. It exemplifies how interactive visualization can make abstract mathematical concepts more intuitive, and the renewed interest coincides with advances in AI that make creating such interactive content more accessible. The book, authored by J. Ström, K. Åström, and T. Akenine-Möller, was the world's first linear algebra textbook with fully interactive figures, and includes tooltips and a structured chapter flow.

hackernews · srean · Jul 16, 15:32 · [Discussion](https://news.ycombinator.com/item?id=48935951)

**Background**: Linear algebra is fundamental to computer graphics, machine learning, and engineering. Interactive figures help learners visualize vectors, dot products, and transformations, overcoming the abstraction of static textbooks. The book was published before the recent wave of large language models and AI-assisted content creation.

<details><summary>References</summary>
<ul>
<li><a href="http://immersivemath.com/ila/index.html">Immersive Math</a></li>
<li><a href="https://www.immersivemath.com/ila/learnmore.html">immersivemath: Immersive Linear Algebra</a></li>
<li><a href="https://www.goodreads.com/book/show/34624307-immersive-linear-algebra">Immersive Linear Algebra by J. Ström | Goodreads Immersive Linear Algebra - lup.lub.lu.se Immersive Linear Algebra by J. Ström, K. Åström, and T ... Immersive Linear Algebra by J. Strom, K. Astrom, T. Akenine ... Interactive Linear Algebra Images</a></li>

</ul>
</details>

**Discussion**: Comments are overwhelmingly positive, with users expressing nostalgia and wishing more subjects were taught this way. Some note that large language models now make creating such interactive illustrations much easier, and one suggests adding an 'Explain this' popup for any highlighted text or symbol.

**Tags**: `#linear-algebra`, `#interactive`, `#education`, `#math`, `#visualization`

---

<a id="item-23"></a>
## [Simon Willison's Mermaid to ASCII Art Tool Now Supports Color](https://simonwillison.net/2026/Jul/16/mermaid-ascii/#atom-everything) ⭐️ 6.0/10

Simon Willison built a new web tool that converts Mermaid diagrams to ASCII art by compiling the Go library AlexanderGrooff/mermaid-ascii to WebAssembly, and it now includes color support for the rendered diagrams. This makes it easy to embed diagrams in plain-text environments like terminal output, documentation, or code comments, and the color support improves readability, making it a practical tool for developers who work with text-based workflows. The tool runs entirely in the browser via WebAssembly, using the Go library to parse Mermaid syntax and output colored ASCII art. It features a tabbed editor with example diagrams, adjustable padding, an 'ASCII only' toggle, and copy-to-clipboard functionality. It is an incremental improvement over a previous Rust-based version, now with color rendering via class definitions.

rss · Simon Willison · Jul 16, 14:57

**Background**: Mermaid is a text-based diagramming language that lets users describe diagrams using simple code-like syntax. WebAssembly is a portable binary format that allows languages like Go, Rust, or C/C++ to be compiled and run efficiently in web browsers. The Go library mermaid-ascii parsed Mermaid definitions and generated ASCII art; compiling it to WebAssembly makes this functionality available directly in a web tool without server-side processing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://mermaid.live/">Online FlowChart & Diagrams Editor - Mermaid Live Editor</a></li>

</ul>
</details>

**Tags**: `#mermaid`, `#ascii-art`, `#webassembly`, `#tools`, `#diagrams`

---

<a id="item-24"></a>
## [Mermaid to Unicode Box Art via WebAssembly](https://simonwillison.net/2026/Jul/16/grok-mermaid/#atom-everything) ⭐️ 6.0/10

Simon Willison built a browser-based tool that converts Mermaid diagram syntax into Unicode box art by compiling a Rust terminal renderer from xAI's Grok CLI to WebAssembly. This demonstrates the power of WebAssembly to bring terminal-based Rust tools to the browser, providing a handy way to generate ASCII art diagrams for use in text-only environments. The Rust crate, xai-grok-markdown, is a self-contained terminal Mermaid renderer. Simon used Claude Code (Fable 5) to build the web interface, which includes width fitting, text copy, and link sharing features.

rss · Simon Willison · Jul 16, 00:33

**Background**: Mermaid is a popular text-based diagramming tool that uses a simple syntax to generate flowcharts, sequence diagrams, and more. WebAssembly is a low-level binary format that allows code written in languages like Rust to run in web browsers at near-native speed. Rust is a systems programming language known for its performance and safety, often used for terminal tools and command-line utilities.

<details><summary>References</summary>
<ul>
<li><a href="https://mermaid.js.org/">Mermaid | Diagramming and charting tool</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>

</ul>
</details>

**Tags**: `#mermaid`, `#WebAssembly`, `#Rust`, `#tool`, `#terminal-ui`

---

<a id="item-25"></a>
## [Independent Researcher Seeks Collaborators for Scaling Novel Recurrent Architecture DABSN](https://www.reddit.com/r/MachineLearning/comments/1uycffg/seeking_collaborators_for_scaling_and_independent/) ⭐️ 6.0/10

An independent researcher has released a preprint and code for DABSN (Dynamic Adaptive Bias State Network), a novel recurrent architecture, along with promising small-scale language model results. They are now seeking collaborators to help scale the model, design stronger baselines, and independently evaluate its performance. Recurrent architectures are a promising alternative to Transformers for long-context and efficient language modeling, and open, reproducible research can accelerate progress in this direction. Successful scaling could provide a more accessible alternative to large proprietary models. The initial language model has 24M parameters, was trained on 1B tokens with a GPT-2 tokenizer, and the code includes PyTorch, C++, and Triton implementations. The paper evaluates DABSN on synthetic reasoning and memory benchmarks like MQAR (Multi-Query Associative Recall), Copy, and Key-Value retrieval.

reddit · r/MachineLearning · /u/BleedingXiko · Jul 16, 19:17

**Background**: Recurrent neural networks process sequences step by step, maintaining a hidden state, which can naturally handle long contexts without the quadratic memory cost of attention. The MQAR benchmark, from the Zoology project, tests a model's ability to perform multiple key-value lookups from context, measuring a crucial skill for language modeling. DABSN introduces a dynamic bias mechanism to improve state updates.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2312.04927">[2312.04927] Zoology: Measuring and Improving Recall in ... GitHub - HazyResearch/zoology: Understand and test language ... GitHub - howard-hou/Visual-MQAR: Understand and test multi ... MQAR: Multi-Query Associative Recall - emergentmind.com Zoology (Blogpost 1): Measuring and Improving Recall in ... Zoology: Measuring and Improving Recall in Efficient Language ... Published as a workshop paper at SCOPE - ICLR 2025 - OpenReview</a></li>
<li><a href="https://github.com/HazyResearch/zoology">GitHub - HazyResearch/zoology: Understand and test language ... GitHub - howard-hou/Visual-MQAR: Understand and test multi ... MQAR: Multi-Query Associative Recall - emergentmind.com Zoology (Blogpost 1): Measuring and Improving Recall in ... Zoology: Measuring and Improving Recall in Efficient Language ... Published as a workshop paper at SCOPE - ICLR 2025 - OpenReview</a></li>

</ul>
</details>

**Tags**: `#RNN`, `#language-model`, `#architecture`, `#collaboration`, `#preprint`

---

<a id="item-26"></a>
## [Rethinking AI Memory: From Descriptive Facts to Reasoning Patterns](https://www.reddit.com/r/MachineLearning/comments/1uy6yht/are_current_ai_memory_architectures_optimizing/) ⭐️ 6.0/10

A Reddit discussion post questions whether current AI memory systems are optimizing for the wrong abstraction by primarily storing descriptive facts about users, instead of inferring higher-level reasoning patterns like preferred abstractions and explanatory frameworks. This perspective could shift the paradigm of persistent context, leading to more personalized AI interactions that adapt to a user's thinking style, potentially improving collaborative problem-solving and long-term assistance. The post contrasts descriptive memory (e.g., 'user is interested in economics') with inferential memory (e.g., 'user explains economics through incentives and institutional constraints'), and speculates whether such representations could emerge naturally from advanced AI or require fundamentally different architectures.

reddit · r/MachineLearning · /u/Boris_Ljevar · Jul 16, 16:00

**Background**: Current AI systems maintain persistent context through stored memories, conversation summaries, and user preferences, which are mostly descriptive. AI agent memory architectures typically combine short-term and long-term layers to store facts and interactions. The post proposes a shift toward modeling a user's recurring explanatory frameworks, preferred abstractions, and characteristic reasoning styles, moving from a collection of notes to an evolving model of how the user thinks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/memory-architectures-ai-agents-short-term-context-long-term-gareth-e7vuf">Memory Architectures for AI Agents: Short-Term Context, Long-Term...</a></li>
<li><a href="https://www.linkedin.com/posts/element-pactify_ai-aiworkflow-pkm-activity-7466481639049609216-iAa2">Moving Beyond Prompts: Building a Persistent Context Layer for AI</a></li>

</ul>
</details>

**Tags**: `#AI memory`, `#context management`, `#reasoning patterns`, `#machine learning`, `#discussion`

---