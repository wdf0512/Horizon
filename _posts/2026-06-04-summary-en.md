---
layout: default
title: "Horizon Summary: 2026-06-04 (EN)"
date: 2026-06-04
lang: en
---

> From 44 items, 12 important content pieces were selected

---

1. [Elixir v1.20 Becomes a Gradually Typed Language](#item-1) ⭐️ 9.0/10
2. [Google Releases Gemma 4 12B Encoder-Free Multimodal Model](#item-2) ⭐️ 9.0/10
3. [Let's Encrypt Plans Post-Quantum Certificates Using Merkle Trees](#item-3) ⭐️ 9.0/10
4. [A Poetic Look at How Neural Network Weights Enable Emergent Language](#item-4) ⭐️ 8.0/10
5. [Ted Chiang Argues AI Is Not Conscious](#item-5) ⭐️ 8.0/10
6. [DaVinci Resolve 21 Adds Photo Editing and AI Video Tools](#item-6) ⭐️ 8.0/10
7. [U.S. Plans to Shut Down AMOC Monitoring System Despite Collapse Risk](#item-7) ⭐️ 8.0/10
8. [Mathematicians Warn of AI's Rapid Advance in Math Problem-Solving](#item-8) ⭐️ 8.0/10
9. [A Deep Dive into the Original PlayStation's Hardware Architecture](#item-9) ⭐️ 8.0/10
10. [Microsoft Launches MAI-Thinking-1 and MAI-Code-1-Flash: Large MoE Models with Low Active Parameters](#item-10) ⭐️ 8.0/10
11. [datasette-agent-micropython 0.1a0: AI-Generated Code Executed Safely in WebAssembly Sandbox](#item-11) ⭐️ 8.0/10
12. [Holo3.1: Fast, Local, Open-Source Computer Use Agents](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Elixir v1.20 Becomes a Gradually Typed Language](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/) ⭐️ 9.0/10

Elixir v1.20 has been released, officially introducing gradual typing, which allows developers to add optional static type annotations to their code while retaining the language's dynamic nature. This marks a significant evolution for Elixir, potentially improving code reliability, documentation, and tooling (like better autocompletion and error checking) without sacrificing flexibility, and may attract more developers from statically-typed language ecosystems. The gradual type system is in its early stages; the community is keen to see how it compares to Erlang's Dialyzer, which uses success typing, and there are open questions about potential performance overhead that gradual typing can introduce.

hackernews · cloud8421 · Jun 3, 19:02 · [Discussion](https://news.ycombinator.com/item?id=48388324)

**Background**: Elixir is a dynamically-typed functional language running on the Erlang VM, previously relying on Dialyzer for optional static analysis. Gradual typing, as defined by Siek and Taha, allows mixing dynamic and static typing within a single program, with type annotations checked at compile time and unannotated code behaving dynamically. This release integrates this concept directly into Elixir's compiler.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gradual_typing">Gradual typing</a></li>
<li><a href="https://jsiek.github.io/home/WhatIsGradualTyping.html">What is Gradual Typing | Jeremy Siek</a></li>

</ul>
</details>

**Discussion**: Overall sentiment is positive and excited, but with technical caution. Users debate whether gradual typing will outperform or be stricter than Dialyzer's success typing, worry about potential runtime slowdowns common in gradual type systems, and discuss the relevance of dynamic typing in the era of AI-assisted coding, with some viewing untyped code as technical debt.

**Tags**: `#Elixir`, `#programming-languages`, `#gradual-typing`, `#functional-programming`, `#type-systems`

---

<a id="item-2"></a>
## [Google Releases Gemma 4 12B Encoder-Free Multimodal Model](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) ⭐️ 9.0/10

On June 3, 2026, Google released Gemma 4 12B, an open-source multimodal model that directly processes images and audio through a lightweight embedding module instead of a traditional vision encoder. The encoder-free design reduces latency and memory usage, enabling advanced vision and audio understanding on consumer laptops. It challenges the prevailing encoder-decoder paradigm and may accelerate on-device AI deployment. The embedding module consists of a single matrix multiplication, positional embedding, and normalization (still 35M parameters). The model is open-sourced on Hugging Face, though some early testers noted minor syntax errors in code generation tasks.

hackernews · rvz · Jun 3, 16:04 · [Discussion](https://news.ycombinator.com/item?id=48385906)

**Background**: Traditional multimodal models often rely on separate vision encoders (like SigLIP) to convert images into language model tokens, adding computational overhead. Encoder-free architectures aim to feed raw or lightly processed pixel data directly to the language model. Gemma is Google's family of open-source models, previously language-only, now expanded to vision and audio. The new design streamlines the pipeline and makes multimodal AI more accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12B/">Introducing Gemma 4 12B - The Keyword</a></li>
<li><a href="https://huggingface.co/google/gemma-4-12B">google/gemma-4-12B · Hugging Face</a></li>
<li><a href="https://techstartups.com/2026/06/03/google-deepmind-launches-gemma-4-12b-bringing-frontier-ai-model-to-everyday-laptops/">Google launches Gemma 4 12B, bringing frontier AI model to ...</a></li>

</ul>
</details>

**Discussion**: Community members debated whether the 35M embedding layer qualifies as truly 'encoder-free', and some questioned Google's business motivation for open-sourcing. One tester ran a minesweeper benchmark and found decent results but had to fix a few trivial syntax errors. Overall sentiment is intrigued but cautiously optimistic about the architecture's robustness.

**Tags**: `#AI`, `#multimodal`, `#Gemma`, `#open-source`, `#Google`

---

<a id="item-3"></a>
## [Let's Encrypt Plans Post-Quantum Certificates Using Merkle Trees](https://letsencrypt.org/2026/06/03/pq-certs) ⭐️ 9.0/10

Let's Encrypt has announced a future transition to post-quantum certificates based on Merkle tree designs, moving away from legacy RSA and ECC systems to counter quantum computing threats. As the world's largest certificate authority, Let's Encrypt's move will impact millions of websites and accelerate the adoption of quantum-resistant encryption, bolstering long-term internet security. The design uses Merkle tree certificates (aligned with draft-ietf-plants-merkle-tree-certs-03), promising efficient verification and smaller certificate sizes, but requires new infrastructure and abandons decades of PKI evolution and battle testing.

hackernews · SGran · Jun 3, 15:06 · [Discussion](https://news.ycombinator.com/item?id=48385114)

**Background**: Post-quantum cryptography (PQC) refers to algorithms secure against attacks by quantum computers, which could break widely used public-key systems like RSA and ECC. Let's Encrypt is a free, automated certificate authority enabling HTTPS for websites. A Merkle tree is a tree structure where leaves are data hashes and internal nodes are hash of child nodes, allowing efficient integrity verification. Certificate Transparency (CT) is a standard that publicly logs all issued certificates to detect misissuance.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.blerify.com/products/post-quantum-certificates">Post Quantum Certificates | Blerify Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Merkle_tree">Merkle tree</a></li>
<li><a href="https://en.wikipedia.org/wiki/Certificate_Transparency">Certificate Transparency</a></li>

</ul>
</details>

**Discussion**: Community comments reflect cautious optimism: many appreciate the quantum-resistant vision but worry about discarding decades of battle-tested PKI infrastructure and tools. Some noted that Certificate Transparency currently has flaws, and a commentator pointed to Cordon, a draft-ietf-plants-merkle-tree-certs-03 compliant CA and ACME server implementation. Others debated the practicality of switching to post-quantum signatures now, referencing specific algorithms like ed25519 versus quantum-resistant ones.

**Tags**: `#post-quantum cryptography`, `#Let's Encrypt`, `#TLS`, `#certificate transparency`, `#quantum computing`

---

<a id="item-4"></a>
## [A Poetic Look at How Neural Network Weights Enable Emergent Language](https://maxleiter.com/blog/weights) ⭐️ 8.0/10

Max Leiter published a poetic blog post reflecting on how neural network weights give rise to emergent language abilities, prompting a philosophical debate on consciousness and AI interpretability. The post connects artistic expression with machine learning, fueling public discourse on whether large language models' linguistic abilities hint at a deeper form of consciousness, and challenging the technical community to make neural network internals more interpretable. A key counterpoint in the discussion cited a 2022 paper showing that for languages with strong grammar, transformer weights are readily interpretable as encoding grammatical rules, directly challenging the idea that weights are entirely opaque.

hackernews · MaxLeiter · Jun 3, 23:37 · [Discussion](https://news.ycombinator.com/item?id=48391611)

**Background**: Neural network weights are adjustable parameters that determine how a model processes inputs. Large language models exhibit emergent language abilities—complex behaviors not explicitly programmed but arising from scale. Interpretability research aims to decode what these models have learned, often revealing that aspects of language structure are encoded in their weights.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/the-role-of-weights-and-bias-in-neural-networks/">Weights and Bias in Neural Networks - GeeksforGeeks</a></li>
<li><a href="https://journal.artificialityinstitute.org/read-write-using-network-theory-to-understand-emergent-language-abilities/">How Network Theory Might Explain Emergent Abilities in AI</a></li>
<li><a href="https://grokipedia.com/page/mechanistic_interpretability">Mechanistic interpretability</a></li>

</ul>
</details>

**Discussion**: Community reactions range from poetic appreciation to strong technical pushback. Some users found deep philosophical resonance with LLMs' possible consciousness, while one commenter argued the post was fundamentally misguided, citing interpretability research that shows transformer weights can encode grammatical structures.

**Tags**: `#neural networks`, `#large language models`, `#philosophy of mind`, `#interpretability`, `#machine learning`

---

<a id="item-5"></a>
## [Ted Chiang Argues AI Is Not Conscious](https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/) ⭐️ 8.0/10

Ted Chiang published an essay in The Atlantic arguing that current AI systems, particularly large language models, are not conscious, because they merely perform statistically likely text continuation without genuine understanding, embodiment, or mutable experience. This intervention by a respected science fiction author and thinker reignites the contentious debate around AI sentience, challenging the hype that often surrounds LLMs and forcing a deeper examination of what consciousness actually means in an era of rapidly advancing technology. Chiang’s central argument is that language models are disguised sentence‑continuation engines whose ‘predict next token’ objective lacks the bodily grounding and persistent, changeable identity required for consciousness; community rebuttals emphasize that simple mechanisms can give rise to complex behavior, and that a static, unlearning model cannot be self-aware.

hackernews · lordleft · Jun 3, 17:51 · [Discussion](https://news.ycombinator.com/item?id=48387270)

**Background**: Consciousness remains a poorly defined and deeply debated concept in neuroscience and philosophy. Large language models like GPT‑4 are built on transformer architectures that generate text by predicting the most probable next token based on training data, without persistent memory or physical interaction. Chiang’s essay pushes back against claims that such systems are sentient, a view that has gained traction with the public emergence of highly fluent chatbots.

**Discussion**: Commenters are divided: some note that debating consciousness is meaningless without a clear definition, and find Chiang’s decomposition-based reasoning flawed; others emphasize that a static, unchanging LLM that does not learn from interactions cannot be conscious, and that a body and senses are prerequisites for desires and intentionality, though some argue that complex understanding can emerge from simple next-token prediction.

**Tags**: `#AI`, `#consciousness`, `#philosophy`, `#LLMs`, `#Ted Chiang`

---

<a id="item-6"></a>
## [DaVinci Resolve 21 Adds Photo Editing and AI Video Tools](https://www.blackmagicdesign.com/products/davinciresolve/whatsnew) ⭐️ 8.0/10

DaVinci Resolve 21 introduces integrated photo management and editing akin to Lightroom, a new motion graphics system, and numerous AI-driven features such as AI-generated subtitles and video stabilization. This update makes DaVinci Resolve a more comprehensive post-production suite that competes with Adobe's Lightroom and After Effects, potentially lowering costs for independent creators and filling a major gap on Linux. The photo management tool offers professional editing and cataloging, while motion graphics aim to replace basic uses of After Effects. However, some users note that the photo features still need polish to fully replace existing workflows.

hackernews · pentagrama · Jun 3, 14:18 · [Discussion](https://news.ycombinator.com/item?id=48384482)

**Background**: DaVinci Resolve is a professional video editing, color grading, and audio post-production software developed by Blackmagic Design. It is known for its high-end capabilities and a generous free version that includes most features. With this release, it expands into still photography and motion graphics, traditionally separate domains requiring additional software subscriptions.

**Discussion**: Community reaction is overwhelmingly positive, with many praising the non-AI additions like photo management and motion graphics as game-changers. Some users express AI fatigue but still acknowledge the practical benefits, while a few suggest an AI agent for automated editing workflows. Overall, the update is seen as substantial and generous.

**Tags**: `#video-editing`, `#software-release`, `#AI`, `#photo-management`, `#post-production`

---

<a id="item-7"></a>
## [U.S. Plans to Shut Down AMOC Monitoring System Despite Collapse Risk](https://e360.yale.edu/digest/trump-ooi-amoc) ⭐️ 8.0/10

The U.S. government intends to dismantle the Ocean Observatories Initiative’s array that monitors the Atlantic meridional overturning circulation (AMOC), a critical ocean current system facing an elevated risk of collapse due to climate change. The AMOC monitoring array is essential for detecting early warning signs of a potential collapse, which could disrupt global climate patterns, trigger extreme weather, and accelerate sea-level rise. Its shutdown jeopardizes climate preparedness and fundamental earth science research. The targeted system is part of the National Science Foundation’s Ocean Observatories Initiative, using deep-sea moorings and sensors that have continuously tracked temperature, salinity, and current speed since the early 2010s. Its dismantling would create an irreplaceable gap in long-term climate data.

hackernews · rguiscard · Jun 4, 00:44 · [Discussion](https://news.ycombinator.com/item?id=48392232)

**Background**: The Atlantic meridional overturning circulation (AMOC) is a vast system of currents that moves warm tropical waters northward and cold deep waters southward, regulating climate for Europe and North America. Climate change weakens the AMOC through ocean warming and freshwater influx from melting ice; a collapse would constitute a major climate tipping point with severe consequences. Continuous monitoring is critical to detect changes and improve predictive models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AMOC">AMOC</a></li>
<li><a href="https://oceanservice.noaa.gov/facts/amoc.html">What is the Atlantic Meridional Overturning Circulation (AMOC)?</a></li>

</ul>
</details>

**Discussion**: Commenters express outrage over the contrast between expensive military spending (e.g., F-35 flights at over $40,000 per hour) and cuts to relatively cheap basic science. Many mock Democrats' pledge to 'fight' the plan as hollow, and note institutional dysfunction in ignoring problems. Others reference scientists like Simon Clark who explain the necessity of AMOC measurements, and criticize big tech for capitulating to the current administration.

**Tags**: `#climate-science`, `#policy`, `#oceanography`, `#science-funding`, `#amoc`

---

<a id="item-8"></a>
## [Mathematicians Warn of AI's Rapid Advance in Math Problem-Solving](https://www.science.org/content/article/mathematicians-issue-warning-ai-rapidly-gains-ground) ⭐️ 8.0/10

A Science article reports that mathematicians are issuing a formal warning about AI's accelerating ability to solve complex mathematical problems, triggering intense debate within the field. Community reactions highlight how large language models produce both striking insights and baffling mistakes, leaving researchers divided. This development could fundamentally reshape mathematical research, potentially automating key aspects of theorem-proving and diminishing the centrality of human insight. The alarm echoes earlier upheavals in art and writing, underscoring a broader societal challenge as AI encroaches on knowledge-intensive professions. The warning comes as LLMs achieve surprising results on mathematical benchmarks, yet they still suffer from a "long tail of stupidity"—generating outputs no competent human would produce. Commenters also note a split: curiosity-driven problems, like Erdős problems, are less likely to welcome AI than directly practical ones.

hackernews · pseudolus · Jun 3, 10:05 · [Discussion](https://news.ycombinator.com/item?id=48382052)

**Background**: Large language models (LLMs) are neural networks trained on massive text corpora to generate and analyze language, forming the basis of modern AI assistants. In mathematics, they can suggest proofs, solve equations, and assist research, but they lack true understanding and often produce plausible falsehoods. Mathematical inquiry has long depended on human intuition and rigorous peer review, processes that AI threatens to bypass with unchecked automation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>

</ul>
</details>

**Discussion**: User comments reveal a layered debate: some argue that mathematics cultivates not just results but human understanding and judgment, which AI could erode. Others highlight the stark inconsistency of LLMs, brilliant one moment and absurd the next, and ask whether current architectures can ever be trusted. Many draw parallels with the initial resistance from artists and writers, suggesting that true alarm only sets in once one's own domain is affected. Accelerationists counter that worries about attribution and verification are merely the growing pains of a dying field.

**Tags**: `#AI`, `#mathematics`, `#LLMs`, `#debate`, `#research`

---

<a id="item-9"></a>
## [A Deep Dive into the Original PlayStation's Hardware Architecture](https://www.copetti.org/writings/consoles/playstation/) ⭐️ 8.0/10

A comprehensive technical analysis of the original PlayStation's CPU, GPU, memory map, and audio has resurfaced, sparking renewed discussion. A former Konami developer shared a clever memory aliasing trick used in the Metal Gear Solid PC port. Such deep-dive analyses preserve retro computing knowledge and reveal the creative engineering behind classic games. They inspire modern developers and assist emulator authors in achieving accurate hardware simulation. The article covers the MIPS R3000A CPU, the custom GPU with a 1 MB framebuffer and 2 KB texture cache, and the SPU handling 24 voices of ADPCM audio. A notable community insight: certain PSX memory regions map to the same physical address, which the Metal Gear Solid port exploited by ORing a pointer with 0x80000000 to distinguish bomb placement states.

hackernews · gregsadetsky · Jun 3, 10:24 · [Discussion](https://news.ycombinator.com/item?id=48382142)

**Background**: Released in 1994, the original PlayStation (PSX) used a 32-bit MIPS R3000A CPU at 33.8 MHz, 2 MB of main RAM, and 1 MB of VRAM. Its custom GPU handled flat and Gouraud shaded polygons with texture mapping, while the SPU provided 24 channels of ADPCM audio and CD-ROM XA streaming. The console's limited and idiosyncratic hardware pushed developers to invent clever memory and performance optimizations, which make it a favorite subject for retro architecture studies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PlayStation_technical_specifications">PlayStation technical specifications - Wikipedia</a></li>
<li><a href="https://psx-spx.consoledev.net/memorymap/">Memory Map - PlayStation Specifications - psx-spx</a></li>
<li><a href="https://psx-spx.consoledev.net/soundprocessingunitspu/">Sound Processing Unit (SPU) - PlayStation Specifications - psx-spx</a></li>

</ul>
</details>

**Discussion**: Comments praised the website's elegant design and the article's clarity. One developer detailed a real-world memory aliasing trick from the Metal Gear Solid PC port, highlighting how the same physical memory could represent different states by altering the pointer. Others asked about XA audio processing location and sought recommendations for web-based PS1 emulators.

**Tags**: `#playstation`, `#hardware`, `#architecture`, `#retro-computing`, `#game-development`

---

<a id="item-10"></a>
## [Microsoft Launches MAI-Thinking-1 and MAI-Code-1-Flash: Large MoE Models with Low Active Parameters](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything) ⭐️ 8.0/10

Microsoft unveiled two Mixture of Experts (MoE) based large language models: MAI-Thinking-1 (1 trillion total parameters, 35 billion active) for reasoning and MAI-Code-1-Flash (137 billion total, 5 billion active) for code generation, with the latter now integrated into GitHub Copilot. The company claims MAI-Thinking-1 was preferred over Anthropic's Claude Sonnet 4.6 in blind human evaluations. By coupling enormous total parameter counts with low active counts, these models deliver competitive performance at reduced inference cost, potentially making advanced reasoning and code assistance more efficient and widely accessible. MAI-Code-1-Flash’s integration into GitHub Copilot could boost developer productivity while lowering operational expenses. Both models are MoE architectures, activating only a fraction of experts per token. Microsoft initially emphasized training on “clean and commercially licensed data,” but the technical paper later revealed the use of a large web crawl, including 24.2 billion Common Crawl pages, reintroducing the same licensing ambiguities faced by other major LLMs.

rss · Simon Willison · Jun 2, 22:21

**Background**: Large language models can employ a Mixture of Experts (MoE) design, where many sub-networks (“experts”) exist but only a few are used per input, reducing computation. Active parameters are those actually used in a single inference, while total parameters represent the full model capacity. Reasoning models like MAI-Thinking-1 are trained to handle complex, multi-step problems, often using chain-of-thought or self-correction techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://www.f22labs.com/blogs/active-vs-total-parameters-whats-the-difference/">Active vs Total Parameters: What’s the Difference?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reasoning_model">Reasoning model</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#Microsoft`, `#reasoning models`, `#code generation`, `#efficiency`

---

<a id="item-11"></a>
## [datasette-agent-micropython 0.1a0: AI-Generated Code Executed Safely in WebAssembly Sandbox](https://simonwillison.net/2026/Jun/2/datasette-agent-micropython/#atom-everything) ⭐️ 8.0/10

Simon Willison released datasette-agent-micropython 0.1a0, an alpha plugin that lets Datasette Agent safely generate and execute Python code within a WebAssembly-based MicroPython sandbox. This solves a critical safety challenge for AI agents, enabling them to perform data transformation, computation, and parsing without risking host system compromise, marking a practical step toward more capable and secure AI assistants. The sandbox runs a MicroPython interpreter compiled to WebAssembly, capturing output via stdout and stderr; initial tests show that GPT-5.5 has so far failed to escape the sandbox.

rss · Simon Willison · Jun 2, 19:28

**Background**: Datasette is an open-source tool for exploring and publishing data, and Datasette Agent is its LLM-powered AI assistant. MicroPython is a lightweight Python implementation, and WebAssembly provides a portable, isolates execution environment, making it ideal for secure code sandboxing.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/datasette/datasette-agent-micropython/">datasette-agent-micropython - GitHub</a></li>
<li><a href="https://simonwillison.net/2026/Jun/2/datasette-agent-micropython/">Release: datasette-agent-micropython 0.1a0 - simonwillison.net</a></li>

</ul>
</details>

**Tags**: `#python`, `#sandboxing`, `#webassembly`, `#datasette`, `#ai-agents`

---

<a id="item-12"></a>
## [Holo3.1: Fast, Local, Open-Source Computer Use Agents](https://huggingface.co/blog/Hcompany/holo31) ⭐️ 8.0/10

Holo3.1 has been released as an open-source AI agent that can autonomously perform GUI tasks across web, desktop, and mobile environments. It ships with quantized checkpoints for the first time, enabling fast local execution on consumer hardware. By enabling truly local, autonomous GUI interaction, Holo3.1 removes cloud dependency for sensitive workflows, ensuring data privacy, low latency, and offline operation. This marks a significant step toward practical, private agentic AI tools that anyone can run and customize. Holo3.1 improves robustness across environments (web, desktop, mobile) and integrates with diverse agent frameworks. The quantized checkpoints optimize performance for local deployment, and the model is designed to work across any agent stack.

rss · Hugging Face Blog · Jun 2, 14:13

**Background**: A computer use agent is an AI system that can control a computer’s graphical interface — clicking buttons, typing text, navigating applications — to complete tasks end-to-end. Until now, many such agents relied on large cloud-hosted models, which can raise privacy concerns and add network latency. Holo3.1 represents a shift toward local-first, open-source models that let developers build private, self-contained automation.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/Hcompany/holo31">Holo3.1: Fast & Local Computer Use Agents</a></li>
<li><a href="https://hcompany.ai/holo3.1">Holo3.1 - H Company</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#computer use`, `#local AI`, `#open-source`, `#GUI automation`

---