---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 26 items, 18 important content pieces were selected

---

1. [trynix.dev Lets You Run Any Nix Package in the Browser via WebAssembly VM](#item-1) ⭐️ 10.0/10
2. [First Zero-Click WeChat Worm Built by AI in Just Over a Week](#item-2) ⭐️ 10.0/10
3. [OpenAI Launches Agents API for Managed LLM Interactions](#item-3) ⭐️ 9.0/10
4. [Critical RCE Vulnerability in Forgejo Versions ≤16.0.3](#item-4) ⭐️ 9.0/10
5. [Microsoft Officially Designates Rust as a Tier-1 Language](#item-5) ⭐️ 9.0/10
6. [OpenAI&\#x27;s Navier-Stokes Release Included a Lean 4 Formal Proof](#item-6) ⭐️ 9.0/10
7. [Shopify Abandons React Native for Native Swift and Kotlin Development](#item-7) ⭐️ 8.0/10
8. [Can Researchers Trust OpenAI with Unpublished Math?](#item-8) ⭐️ 8.0/10
9. [Fruit Fly Connectome Pong Attempt Exposes neuPrint Bug and Missing Neural Pathways](#item-9) ⭐️ 8.0/10
10. [uv 0.12.12 introduces code signing for macOS and Windows executables](#item-10) ⭐️ 7.0/10
11. [PlanetScale Introduces Neki Sharded Postgres Amid Mixed Reactions](#item-11) ⭐️ 7.0/10
12. [Hitachi launches CO2 heat pump water heaters with solar-friendly tariff controls](#item-12) ⭐️ 7.0/10
13. [Small 348M Model Beats GPT-3 175B in Arithmetic by Showing Work](#item-13) ⭐️ 7.0/10
14. [Sante&\#x27;s High DiagnosisArena-MCQ Score: MCQ, Not Open-Ended Reasoning](#item-14) ⭐️ 7.0/10
15. [uv 0.12.13 Released: GraalPy 3.13.0, Faster Resolution, Windows Fixes](#item-15) ⭐️ 6.0/10
16. [Cognition Launches SWE-2 Model, Claims Parity with Fable 5.1 &amp; GPT-Astra](#item-16) ⭐️ 6.0/10
17. [NASA&\#x27;s Decorrelation Stretch Reveals Ancient Rock Art](#item-17) ⭐️ 6.0/10
18. [Stanford Launches Free &\#x27;Probability for AI&\#x27; Course with 1,000+ Volunteers](#item-18) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [trynix.dev Lets You Run Any Nix Package in the Browser via WebAssembly VM](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 10.0/10

Farid Zakaria launched trynix.dev, which uses a qemu-wasm-powered x86\_64 Linux virtual machine to boot any Nix package from the past 13 years directly in the browser. Users get an interactive shell simply by visiting a URL like trynix.dev/?pkg=python3@3.6.2, and a companion GitHub Action, trynix-preview, can comment on pull requests with a link to boot the PR&\#x27;s build. This eliminates the need for local installations or servers for reproducible environments, enabling instant demos, testing, and code reviews. It could dramatically lower the barrier for exploring historical software versions and revolutionize CI workflows. The VM is accessed by visiting URLs like trynix.dev/?pkg=python3@3.6.2, and the service runs entirely client-side with no servers. The trynix-preview GitHub Action extends this to pull requests, letting reviewers boot the PR&\#x27;s build in the browser. Performance is constrained by WebAssembly emulation but remains functional.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a package manager that guarantees reproducibility by isolating each package and tracking exact dependencies, with a repository containing over 13 years of versions. WebAssembly allows high-performance execution of compiled code in browsers. qemu-wasm is a project that compiles the QEMU emulator to WebAssembly, enabling full x86\_64 system emulation within a browser. Together, they enable on-demand recreation of any historical Nix environment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nix_%28package_manager%29">Nix (package manager) - Wikipedia</a></li>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>

</ul>
</details>

**Tags**: `#nix`, `#webassembly`, `#virtualization`, `#developer-tools`, `#reproducibility`

---

<a id="item-2"></a>
## [First Zero-Click WeChat Worm Built by AI in Just Over a Week](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 10.0/10

Calif Research demonstrated WeWorm, the first zero-click worm to spread through WeChat voice calls on iOS and Android without any victim interaction. Leveraging AI, they discovered the bug and developed a remote code execution exploit in roughly two days, completing the full worm in one additional week—work that previously would have taken a larger team months. The rapid creation of WeWorm with AI marks a significant escalation in offensive cyber capabilities, shrinking exploit timelines from months to days. This poses an acute threat to widely used platforms like WeChat \(over 1.4 billion accounts\) and raises urgency for proactive security measures. WeWorm exploits a memory corruption vulnerability in WeChat’s VoIP feature, silently compromising accounts on iOS and Android via incoming calls from existing contacts, without the victim answering. Calif reported the flaw to Tencent, which has since patched it; the proof-of-concept worm spreads through the contact list.

rss · Simon Willison · Sep 10, 00:56

**Background**: Zero-click attacks require no victim interaction, making them especially dangerous. WeChat is a super-app with over 1.4 billion monthly users, integrating messaging, payments, and more. Traditionally, uncovering and weaponizing such vulnerabilities was a months-long manual effort, but AI tools now accelerate vulnerability discovery and exploit generation.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm – First 0-Click Worm Spreading Through WeChat Calls ...</a></li>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and ...</a></li>
<li><a href="https://horizon3.ai/intelligence/blogs/ai-exploit-speed-scale/">AI-Powered Exploit Generation: Speed, Scale &amp; Cyber Risk | Horizon3</a></li>

</ul>
</details>

**Tags**: `#ai-security-research`, `#zero-click`, `#worm`, `#WeChat`, `#exploit-development`

---

<a id="item-3"></a>
## [OpenAI Launches Agents API for Managed LLM Interactions](https://developers.openai.com/api/docs/guides/agents-api/overview) ⭐️ 9.0/10

OpenAI introduces the Agents API, which enables developers to create production-ready agents in a single API call by specifying the task, model, tools, and environment. The API includes managed infrastructure with automatic context compaction, multi-agent orchestration, and programmatic tool calling. This commoditizes agent-based LLM interactions, shifting the industry toward managed agent services and blurring the line between raw LLM endpoints and full agent harnesses. It could accelerate adoption by reducing the complexity of building custom harnesses, though it also risks vendor lock-in. The API supports self-hosting the sandbox environment, easing transitions between providers. Its core concepts include Agent, Environment \(optional sandbox/computer\), Session, and Events/Items, plus support for MCP servers.

hackernews · aquir · Sep 10, 19:43 · [Discussion](https://news.ycombinator.com/item?id=49649213)

**Background**: Agentic AI refers to AI programs that can autonomously pursue goals, use external tools, and perform multi-step tasks, often driven by large language models. Previously, developers had to build complex agent harnesses themselves or use open-source libraries, facing challenges like state persistence and environment coupling. The new Agents API provides a hosted harness that abstracts away this infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/api/docs/guides/agents-api/overview">Agents API | OpenAI API</a></li>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API | OpenAI</a></li>

</ul>
</details>

**Discussion**: Commenters note the eroding distinction between LLM endpoints and agents, debate the right abstraction for agent products, and discuss self-hosted alternatives. Some appreciate the option to self-host the sandbox \(buried in the docs\) as a way to avoid lock-in, while others highlight the value of managed services for reducing complexity.

**Tags**: `#openai`, `#agents`, `#api`, `#llm`, `#agentic-ai`

---

<a id="item-4"></a>
## [Critical RCE Vulnerability in Forgejo Versions ≤16.0.3](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md) ⭐️ 9.0/10

Forgejo versions up to 16.0.3 contain a critical remote code execution vulnerability that can be triggered when initializing a new repository from a template, due to template expansion interfering with git operations. The issue is fixed in version 16.0.4. Forgejo is a widely used self-hosted Git service, and this critical RCE \(score 9.0/10\) could allow attackers to fully compromise servers hosting repositories, risking source code and sensitive data. Immediate upgrade is essential. The flaw occurs because variable template expansion is performed before the new git repository is properly initialized, enabling injection of malicious commands via crafted template files. The fix is in pull request \#14301, and the release notes are temporarily rate-limited on Codeberg.

hackernews · weierstass · Sep 10, 15:57 · [Discussion](https://news.ycombinator.com/item?id=49645907)

**Background**: Forgejo is a self-hosted Git forge, a fork of Gitea, designed to be lightweight and easy to maintain. It supports creating new repositories from templates, where placeholder variables in template files are replaced with user-supplied values. This template expansion feature, when combined with git repository initialization, led to the vulnerability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forgejo">Forgejo</a></li>
<li><a href="https://forgejo.org/">Forgejo – Beyond coding. We forge .</a></li>

</ul>
</details>

**Discussion**: Community comments confirm the severity, with Gitea leadership noting that Gitea is not affected. Some users worry that rejecting AI-generated code contributions might slow vulnerability detection, while others experienced rate limiting that hindered access to the release notes. There is consensus that immediate patching is required.

**Tags**: `#security`, `#RCE`, `#Forgejo`, `#vulnerability`

---

<a id="item-5"></a>
## [Microsoft Officially Designates Rust as a Tier-1 Language](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

Microsoft has officially made Rust a Tier-1 language within the company, meaning it now receives the same level of security review, tooling support, and internal promotion as mature languages like C++ and C\#. This formalizes Rust as a first-class option for systems programming across Microsoft. This is a strong signal that Rust is a mature and production-ready language, endorsed by one of the largest software companies. It could accelerate Rust adoption industry-wide, particularly for security-critical infrastructure, and encourage more organizations to invest in Rust tooling and developer ecosystems. While Rust is now Tier-1, C++ remains dominant in existing codebases; Microsoft aims to leverage automated code conversion tools to migrate legacy C/C++ code to Rust, with a vision of converting one billion lines by 2030. Rust&\#x27;s integration with MSVC and Windows is being improved, and first-class C++ interoperability is seen as the next major challenge.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Background**: At Microsoft, a Tier-1 language is one that receives full, high-priority support across internal tools, security reviews, and quality gates, alongside C++ and C\#. Rust is a systems programming language known for memory safety guarantees without a garbage collector, making it ideal for preventing common vulnerabilities like buffer overflows. Microsoft and other OS vendors are increasingly investing in Rust to reduce memory-related security flaws, which account for about 70% of critical vulnerabilities in large C/C++ codebases. This move follows similar steps by Google, Amazon, and others, signaling a shift in the industry toward safer systems languages.

<details><summary>References</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://lobste.rs/s/eerwba/rust_is_tier_1_language_at_microsoft">Rust Is Tier-1 Language at Microsoft | Lobsters</a></li>

</ul>
</details>

**Discussion**: The community widely views this as a landmark endorsement of Rust&\#x27;s maturity and safety benefits. Commenters highlighted Microsoft&\#x27;s ambitious goal to automatically convert billions of lines of code to Rust by 2030, the importance of seamless C++ interoperability, and how this move could solidify Rust&\#x27;s position as a &\#x27;safer C++&\#x27; over newer alternatives like Zig. Many expressed optimism that this will accelerate Rust adoption in enterprise and operating system development.

**Tags**: `#rust`, `#microsoft`, `#systems-programming`, `#programming-languages`, `#industry-adoption`

---

<a id="item-6"></a>
## [OpenAI&\#x27;s Navier-Stokes Release Included a Lean 4 Formal Proof](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/) ⭐️ 9.0/10

OpenAI&\#x27;s internal AI system generated a solution to the Navier–Stokes existence and smoothness problem, a Millennium Prize problem, and released both a traditional proof write-up and a formal, machine-checkable proof in the Lean 4 language. This demonstrates that AI can not only solve deep mathematical problems but also produce formally verifiable proofs, potentially accelerating research and raising the bar for proof correctness. It signals a practical shift toward AI-assisted formal mathematics. The Lean 4 formalization enables independent mechanical verification, though prior large proofs \(e.g., Fermat&\#x27;s Last Theorem\) required 15 hours and 230GB RAM in Lean, raising performance questions. A timing controversy emerged as mathematician Tristan Buckmaster claimed advances on the same problem 12 hours before OpenAI&\#x27;s announcement, and the estimated AI agent cost of $40M was compared to ~$132M for equivalent human labor.

hackernews · ibobev · Sep 10, 21:22 · [Discussion](https://news.ycombinator.com/item?id=49650326)

**Background**: The Navier–Stokes existence and smoothness problem is one of the seven Millennium Prize Problems, asking whether solutions to the fluid motion equations always exist and remain smooth. Lean 4 is an open-source proof assistant and functional programming language that allows mathematical proofs to be encoded as code and mechanically verified, eliminating human error in verification.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/navier-stokes-solution/">On the Navier–Stokes Millennium Prize Problem | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_priority_controversy">Navier–Stokes priority controversy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_%28proof_assistant%29">Lean (proof assistant)</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed but pragmatic, highlighting Lean&\#x27;s potential performance bottlenecks \(e.g., slow verification of large proofs\), cost savings \(~$40M vs. $132M\), and a desire for more direct or inductive proofs. Some questioned the comparability of cost and effort, while others raised philosophical concerns about proofs that might exceed human verification abilities.

**Tags**: `#formal-verification`, `#lean4`, `#openai`, `#automated-reasoning`, `#navier-stokes`

---

<a id="item-7"></a>
## [Shopify Abandons React Native for Native Swift and Kotlin Development](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify announced it is migrating its mobile apps away from React Native back to native development using Swift for iOS and Kotlin for Android, leveraging large language models \(LLMs\) to assist with code migration and reduce the effort involved. This move by a major tech company signals a potential shift against cross-platform frameworks, as LLM-assisted migrations could make native development more cost-effective, challenging the long-held assumption that shared codebases are essential for efficiency. The migration used LLMs like Codex and testing tools like Maestro to quickly generate native code from the React Native codebase, with most screens ported overnight, though final polishing took a few days. Shopify re-evaluated its 2020 decision after LLMs changed the core cost assumption.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is a cross-platform framework that lets developers write mobile apps in JavaScript for both iOS and Android, popular for sharing code between platforms. Shopify adopted it in 2020 to speed up development. Native apps, using Swift for iOS and Kotlin for Android, typically offer better performance and platform-specific optimizations. LLMs like GitHub Copilot can now automatically translate existing code to native languages, reducing the manual labor traditionally required for such migrations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/experimenting-llm-assisted-software-migrations-java-spring-case-fdose">Experimenting LLM - assisted software migrations : a Java Spring case...</a></li>
<li><a href="https://medium.com/@monojitchoudhury/ideas-for-llm-driven-code-migration-0455faa7a070">Ideas for LLM -driven code migration | by Monojit Choudhury | Medium</a></li>

</ul>
</details>

**Discussion**: The community overwhelmingly validated the move, with many engineers sharing similar overnight LLM-assisted migration successes. Some cautioned that the LLM story may be overstated, as the bulk of work occurred before advanced LLMs were available. A key sentiment is that LLMs diminish React Native&\#x27;s appeal—if code generation is simple, starting native becomes more attractive, challenging the C-suite push for shared codebases.

**Tags**: `#React Native`, `#Swift`, `#Kotlin`, `#Mobile Development`, `#Cross-platform`

---

<a id="item-8"></a>
## [Can Researchers Trust OpenAI with Unpublished Math?](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

A growing discussion among researchers questions whether OpenAI exploits unpublished mathematical ideas shared during collaborations, possibly using them without proper attribution. This controversy threatens trust in AI research partnerships, as it raises ethical concerns about intellectual property and the integrity of scientific collaboration. If researchers feel their ideas can be appropriated, they may hesitate to engage with advanced AI tools, slowing shared progress. Specific cases include Dr. Buckmaster&\#x27;s Codex prompts potentially leaking into model outputs, and OpenAI&\#x27;s suspicious generation of 300 billion tokens right after learning a major proof might be in the training data.

hackernews · pred\_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: Large language models like those from OpenAI are often tested by mathematicians on open problems, with both parties exchanging ideas. This interaction can inadvertently feed fresh, unpublished research into the model&\#x27;s training pipeline. Such models are known to memorize training data, which can include user-provided prompts if used for later training. The situation is exacerbated by the lack of clear norms around data use and attribution in AI collaborations.

**Discussion**: Comments are divided: some compare OpenAI to an unethical human collaborator taking credit, while others suggest it&\#x27;s plausible the model independently rediscovered techniques. There is suspicion over OpenAI&\#x27;s timing of large-scale output generation, and a call for more transparency.

**Tags**: `#AI ethics`, `#OpenAI`, `#research integrity`, `#machine learning`, `#data privacy`

---

<a id="item-9"></a>
## [Fruit Fly Connectome Pong Attempt Exposes neuPrint Bug and Missing Neural Pathways](https://www.reddit.com/r/MachineLearning/comments/1wc67ci/i_tried_to_make_a_real_fly_connectome_learn_to/) ⭐️ 8.0/10

A scientist attempted to train a subgraph of the MaleCNS v1.0 fruit fly connectome to play Pong using dopamine-style plasticity, but it failed to learn; a thorough audit revealed a neuPrint regex bug that silenced two neuron populations and identified missing neural pathways that prevented any signal flow from photoreceptors to motor neurons. This case study demonstrates that negative results and rigorous debugging are scientifically valuable, exposing pitfalls in connectome simulation that viral projects often overlook; it also critiques several high-profile fly-brain gaming projects for lacking proper validation, underscoring the need for scientific rigor in computational neuroscience. The audit identified a neuPrint query bug \(misspecified regex\), a missing layer between photoreceptors and motion detectors, and motor neurons with zero sensory connections that rendered learning impossible; after reconstructing a courtship pursuit circuit, learning did diverge, but only in the form of global punishment-driven suppression, not skill improvement.

reddit · r/MachineLearning · /u/oPeraza2007 · Sep 10, 02:28

**Background**: A connectome is a complete wiring diagram of neural connections, often derived from electron microscopy \(EM\) imaging of brain slices. The MaleCNS v1.0 dataset is a high-resolution EM reconstruction of the male fruit fly central nervous system comprising ~166,000 neurons. neuPrint is an open-access platform for querying and exploring such connectomes programmatically. Researchers often attempt to simulate learning in these circuits by applying dopamine-style plasticity rules, where synaptic strengths change based on reward or punishment signals.

<details><summary>References</summary>
<ul>
<li><a href="https://neuprint.janelia.org/help/api">neuPrintExplorer - Janelia Research Campus</a></li>
<li><a href="https://en.wikipedia.org/wiki/Connectome">Connectome - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#computational neuroscience`, `#connectomics`, `#reinforcement learning`, `#scientific rigor`, `#biomimetic AI`

---

<a id="item-10"></a>
## [uv 0.12.12 introduces code signing for macOS and Windows executables](https://github.com/astral-sh/uv/releases/tag/0.12.12) ⭐️ 7.0/10

uv 0.12.12, released on 2026-09-09, now ships code-signed binaries for macOS and Windows. macOS executables are signed with an Apple Developer ID certificate and notarized by Apple, while Windows executables receive timestamped Authenticode signatures via Azure Artifact Signing. Code signing allows users to verify the publisher and integrity of uv, reducing security warnings and antivirus false positives. It also enables enterprise environments to allowlist the software based on its verified publisher, improving trust and adoption of this popular Python packaging tool. The signing covers the executables in release archives as well as the \`uv\` and \`uv\_build\` wheels on macOS and Windows. Additionally, this release fixed a bug where distributions uploaded after the \`exclude-newer\` cutoff were incorrectly included in lockfiles and requirement hashes.

github · astral-automations-bot\[bot\] · Sep 9, 16:45

**Background**: uv is a fast Python package and project manager written in Rust. Code signing uses digital certificates to cryptographically verify the publisher and integrity of software. Apple&\#x27;s notarization requires submitting software for automated security scanning before it can be signed, while Microsoft&\#x27;s Authenticode is a standard for signing Windows executables; Azure Artifact Signing automates this process with timestamped signatures.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/forums/tags/notarization">Notarization | Apple Developer Forums</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows-hardware/drivers/install/authenticode">Authenticode Digital Signatures - Windows drivers | Microsoft ...</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options">Code signing options for Windows app developers - Windows ...</a></li>

</ul>
</details>

**Tags**: `#uv`, `#Python`, `#packaging`, `#security`, `#release`

---

<a id="item-11"></a>
## [PlanetScale Introduces Neki Sharded Postgres Amid Mixed Reactions](https://planetscale.com/blog/introducing-neki) ⭐️ 7.0/10

PlanetScale announced Neki, a sharded Postgres database solution, but the launch blog post lacks a clear description of the product, leading to confusion. Sharded Postgres is critical for scaling modern applications, and PlanetScale&\#x27;s experience with Vitess could fill a major gap; however, the unclear messaging and CEO&\#x27;s behavior may erode trust. Neki is currently closed-source, with a promise to open-source after production testing; it claims superiority over the open-source alternative multigres, but technical details about its handling of consistency and CAP theorem trade-offs remain unaddressed.

hackernews · simon\_weber · Sep 10, 15:43 · [Discussion](https://news.ycombinator.com/item?id=49645686)

**Background**: Database sharding distributes data across multiple servers for horizontal scalability. PlanetScale famously created Vitess, an open-source sharding layer for MySQL used by Google. PostgreSQL lacks a native sharding solution, prompting various forks. The CAP theorem states that a distributed database cannot simultaneously guarantee consistency, availability, and partition tolerance.

<details><summary>References</summary>
<ul>
<li><a href="https://planetscale.com/neki">Neki — PlanetScale | Sharded Postgres by the Team Behind Vitess.</a></li>
<li><a href="https://neki.dev/">Sharded Postgres by PlanetScale | Neki</a></li>

</ul>
</details>

**Discussion**: The community criticized the launch post for failing to explain what Neki is or what it does. Users expressed annoyance at the CEO&\#x27;s aggressive tone and hypocrisy, given PlanetScale&\#x27;s history with open-source Vitess. Technical questions focused on whether Neki can offer strong consistency without sacrificing availability.

**Tags**: `#database`, `#postgres`, `#sharding`, `#planetscale`, `#launch`

---

<a id="item-12"></a>
## [Hitachi launches CO2 heat pump water heaters with solar-friendly tariff controls](https://www.pv-magazine.com/2026/09/07/hitachi-launches-co2-heat-pump-water-heaters-with-solar-friendly-tariff-controls/) ⭐️ 7.0/10

Hitachi&\#x27;s new CO2 heat pump water heater features tariff-aware controls to leverage daytime solar surpluses, sparking a rich Hacker News discussion on real-world usage and terminology.

hackernews · thelastgallon · Sep 9, 14:54 · [Discussion](https://news.ycombinator.com/item?id=49627634)

**Tags**: `#heat-pump`, `#solar-energy`, `#energy-efficiency`, `#smart-grid`, `#japan`

---

<a id="item-13"></a>
## [Small 348M Model Beats GPT-3 175B in Arithmetic by Showing Work](https://www.reddit.com/r/MachineLearning/comments/1wc7hmu/i_trained_a_348m_model_trained_from_scratch_on/) ⭐️ 7.0/10

A 348M-parameter model trained from scratch on 22.7B tokens can perform multi-digit addition, subtraction, and multiplication by explicitly generating column addition, carries, and borrows, achieving 99.4% average accuracy on GPT-3&\#x27;s arithmetic sub-tasks, far surpassing GPT-3 175B&\#x27;s direct-answer performance. It shows that a small model can master arithmetic through learned procedural reasoning, challenging the belief that scale is necessary for such capability and pointing toward more efficient architectures for reliable, interpretable reasoning. The model&\#x27;s reasoning traces are load-bearing: 95.3% of correct answers have valid workings. When it couldn&\#x27;t name enough place values, it skipped digits; after expanding the place-name list from 6 to 19, it cleanedly reached 14-digit addition. Word problems \(GSM8K 4%\) and division remain unsolved, and greedy decoding is required.

reddit · r/MachineLearning · /u/nkthebass · Sep 10, 03:28

**Background**: Chain-of-thought prompting encourages models to produce intermediate steps, but here the model was fine-tuned to internalize column arithmetic—a structured algorithm. Partial product multiplication, where numbers are broken into parts for multiplication, is a key technique the model uses. This approach contrasts with large language models that often answer arithmetic by pattern recognition rather than step-by-step computation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chain-of-thought_prompting">Chain-of-thought prompting</a></li>
<li><a href="https://www.splashlearn.com/math-vocabulary/multiplication/partial-product">What Is a Partial Product? Definition, Methods ... - SplashLearn</a></li>

</ul>
</details>

**Tags**: `#small language models`, `#arithmetic reasoning`, `#model efficiency`, `#benchmarking`, `#natural language processing`

---

<a id="item-14"></a>
## [Sante&\#x27;s High DiagnosisArena-MCQ Score: MCQ, Not Open-Ended Reasoning](https://www.reddit.com/r/MachineLearning/comments/1wbkxsa/what_santes_8383_on_diagnosisarenamcq_actually/) ⭐️ 7.0/10

Sante scored 83.83 on DiagnosisArena-MCQ, a multiple-choice benchmark where it picks a diagnosis from four given options, not open-ended reasoning tasks. The model also achieved 53.88 on MedXpertQA-Text and 45.73 on HealthBench Professional. This clarification is critical because MCQ performance can be misinterpreted as open-ended clinical reasoning, leading to overestimation of a model&\#x27;s real-world diagnostic capabilities. It underscores the need for nuanced benchmark evaluation in medical AI. DiagnosisArena-MCQ provides case information and tests, then asks for a choice among four diagnoses. HealthBench Professional’s score is rubric-based, not percentage accuracy, and the release didn’t clarify if it was length-adjusted, making direct comparisons uncertain.

reddit · r/MachineLearning · /u/Expert\_Coffee\_203 · Sep 9, 13:01

**Background**: DiagnosisArena is a benchmark for evaluating diagnostic reasoning in large language models, with DiagnosisArena-MCQ being its multiple-choice variant where models select from four diagnoses. MedXpertQA-Text consists of 2,450 board-level, text-only multiple-choice questions with ten options each. HealthBench Professional evaluates LLMs on real clinician tasks—care consultation, writing, and medical research—using physician-graded rubrics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2505.14107">DiagnosisArena : Benchmarking Diagnostic Reasoning for Large...</a></li>
<li><a href="https://medxpertqa.github.io/">MedXpertQA</a></li>
<li><a href="https://arxiv.org/abs/2604.27470">[2604.27470] HealthBench Professional: Evaluating Large ...</a></li>

</ul>
</details>

**Tags**: `#medical AI`, `#benchmarks`, `#model evaluation`, `#clinical reasoning`, `#large language models`

---

<a id="item-15"></a>
## [uv 0.12.13 Released: GraalPy 3.13.0, Faster Resolution, Windows Fixes](https://github.com/astral-sh/uv/releases/tag/0.12.13) ⭐️ 6.0/10

uv 0.12.13, released on 2026-09-10, adds support for GraalPy 3.13.0, speeds up dependency resolution by reusing supported hashes from direct URL fragments, verifies hashes of PEP 658 metadata sidecars, and fixes Windows entry-point launcher issues for Nano Server compatibility. GraalPy support extends uv to a high-performance Python 3.13 runtime built on GraalVM, useful for Java embedding and native images. The resolution performance improvement reduces CI/CD pipeline times and bandwidth usage, while the Windows fix enables smooth operation on lightweight Nano Server containers. The resolver avoids downloading full wheels when metadata is separately available via direct URL fragments, reusing supported hashes; the Windows launcher now edits resources in memory to work on Nano Server, where filesystem modifications are limited. Additionally, uv now prefers the &\#x27;core-metadata&\#x27; key in JSON index responses over legacy aliases.

github · astral-automations-bot\[bot\] · Sep 10, 19:27

**Background**: GraalPy is a Python 3.13 compliant runtime developed by Oracle, built on the GraalVM ecosystem. It offers high performance and first-class support for embedding Python in Java applications and compiling Python programs to native binaries. PEP 658 is a Python Enhancement Proposal that allows package indexes \(like PyPI\) to serve distribution metadata files separately from the full package, enabling faster dependency resolution without downloading entire archives. Windows Nano Server is a minimal, headless installation option for Windows Server, designed for containers and cloud environments, where certain APIs and filesystem operations are restricted.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/oracle/graalpython">GitHub - oracle/graalpython: GraalPy – A high-performance...</a></li>
<li><a href="https://peps.python.org/pep-0658/">PEP 658 – Serve Distribution Metadata in the Simple ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Windows_Nano_Server">Windows Nano Server</a></li>

</ul>
</details>

**Tags**: `#python`, `#package-manager`, `#uv`, `#release-notes`, `#performance`

---

<a id="item-16"></a>
## [Cognition Launches SWE-2 Model, Claims Parity with Fable 5.1 &amp; GPT-Astra](https://cognition.com/blog/swe-2) ⭐️ 6.0/10

Cognition released SWE-2, a proprietary coding model post-trained from the 2.8T-parameter Kimi K33, which it says rivals Anthropic’s Claude Fable 5.1 and OpenAI’s GPT-Astra on agentic coding benchmarks. The launch intensifies AI coding competition, but community skepticism about benchmark overfitting and the closed‑source nature may limit adoption as open‑weight alternatives like DeepSeek Flash 4.1 gain popularity. SWE-2 features a 1M context window and an explicit reasoning mode, yet its Terminal Bench 2.1 score of 92.8% drops sharply to 27.3% on the newer Terminal Bench 4, suggesting poor generalization to unseen tasks.

hackernews · seelos · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645443)

**Background**: SWE-2 is built on Kimi K33, a large model from Moonshot AI that underwent extensive reinforcement learning for agentic coding. Claude Fable 5.1 and GPT‑Astra \(GPT‑6 Astra\) are leading proprietary models known for high scores on coding tasks. Terminal Bench 2.1 and 4 are paired benchmarks where the newer version contains problems unseen during training; a deep score drop often signals ‘benchmaxxing’ instead of genuine coding skill.

<details><summary>References</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE - 2 : Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://benchlm.ai/models/swe-2">SWE - 2 Benchmarks &amp; Context (September 2026) | BenchLM.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT -6 Astra - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters widely questioned SWE-2’s generalization, highlighting the steep score gap between Terminal Bench 2.1 and 4 as evidence of overfitting. Many noted that the model is not open‑weight, reducing its appeal compared to DeepSeek Flash 4.1, and recalled Cognition’s past Devin demo that failed on close inspection. Some found it interesting that Fable‑5.1‑level results were achieved via RL on Kimi K3, but overall sentiment remains skeptical about yet another closed model.

**Tags**: `#AI`, `#coding models`, `#benchmarking`, `#LLMs`, `#skepticism`

---

<a id="item-17"></a>
## [NASA&\#x27;s Decorrelation Stretch Reveals Ancient Rock Art](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images) ⭐️ 6.0/10

NASA&\#x27;s Spinoff program highlighted the use of decorrelation stretch, a satellite image enhancement technique, which has been adapted for decades by archaeologists to reveal faded rock art, notably through the Dstretch plugin. This interdisciplinary technology transfer from space exploration to cultural heritage preservation enables the documentation of ancient art invisible to the naked eye, potentially democratizing heritage research and inspiring further cross-domain applications. Decorrelation stretch amplifies subtle color differences by reducing inter-channel correlation. The Dstretch plugin for ImageJ automates this for rock art, and similar results can be achieved manually in GIMP using LAB color decomposition and contrast adjustments.

hackernews · gumby · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645437)

**Background**: Decorrelation stretch is an image enhancement method that reduces correlation between color channels, making subtle color variations more visible. Originally developed for satellite and aerial remote sensing to distinguish materials like vegetation, minerals, and land use, the technique can reveal pigments that have faded over centuries in rock art. The open-source Dstretch plugin, built on this principle, has been used by archaeologists since 2005.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Decorrelation">Decorrelation - Wikipedia</a></li>
<li><a href="https://dstretch.com/">DStretch.com home page</a></li>

</ul>
</details>

**Discussion**: Community members noted that the technique is not new, as the Dstretch plugin has been available since 2005 and similar enhancement methods existed earlier. They shared personal experiences with false-color composites in remote sensing, manual GIMP workflows, and fieldwork attempts, viewing the story as an interesting but belated recognition of a long-standing tool.

**Tags**: `#image-processing`, `#remote-sensing`, `#archaeology`, `#nasa-spinoff`, `#computer-vision`

---

<a id="item-18"></a>
## [Stanford Launches Free &\#x27;Probability for AI&\#x27; Course with 1,000+ Volunteers](https://www.reddit.com/r/MachineLearning/comments/1wbf3ox/teach_ml_community_service_project_from_stanford_n/) ⭐️ 6.0/10

Stanford professor Chris Piech announced &\#x27;Probability for AI&\#x27;, a free online course starting October 9th that pairs every ten students with one volunteer teacher. Over 1,000 people have already applied to teach, and the course includes hands-on projects like building an AI text detection app alongside a coding agent. This community-driven model radically expands access to high-quality AI education, lowering financial and geographic barriers. By blending rigorous probability foundations with personalized mentorship, it could help close the machine learning talent gap worldwide. The course uses &\#x27;teachable agents&\#x27; for teacher training—allowing volunteers to practice instructing AI before leading student groups. Applications close at the end of September, and the entire program is funded through an alumni donation.

reddit · r/MachineLearning · /u/chrispiech · Sep 9, 07:54

**Background**: Teachable agents are AI systems designed for learning-by-teaching, where a learner instructs an agent to reinforce their own knowledge. The most prominent example is Betty’s Brain, a qualitative reasoning tool used in science education. Stanford’s course adapts this concept, likely using AI-driven agents to simulate student interactions and help volunteer teachers hone their skills—a method known to foster metacognition and self-regulated learning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Teachable_agent">Teachable agent</a></li>
<li><a href="https://microsoft.github.io/autogen/0.2/blog/2023/10/26/TeachableAgent/">AutoGen&#x27;s Teachable Agents | AutoGen 0.2 - GitHub Pages</a></li>

</ul>
</details>

**Tags**: `#education`, `#machine learning`, `#probability`, `#community service`, `#Stanford`

---