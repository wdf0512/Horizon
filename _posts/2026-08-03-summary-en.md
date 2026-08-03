---
layout: default
title: "Horizon Summary: 2026-08-03 (EN)"
date: 2026-08-03
lang: en
---

> From 34 items, 15 important content pieces were selected

---

1. [Qwen3.8-Max: Alibaba&\#x27;s 2.4T Open-Weight Model Rivals Fable 5](#item-1) ⭐️ 8.0/10
2. [Isopolis: Interactive Isometric Pixel Art Map of San Francisco](#item-2) ⭐️ 8.0/10
3. [SwiftUI After 7 Years: Maturity, Shortcomings, and Developer Debate](#item-3) ⭐️ 8.0/10
4. [OpenAI&\#x27;s Astra solves ten decade-old math problems at low cost](#item-4) ⭐️ 8.0/10
5. [Review shows how LLM performance degrades with long context and shares practical habits](#item-5) ⭐️ 8.0/10
6. [VLMs achieve high benchmark scores by erasing clinically meaningful terms](#item-6) ⭐️ 8.0/10
7. [Karpathy’s Pelican Tweet Sparks Debate on AI Physical Understanding Benchmarks](#item-7) ⭐️ 7.0/10
8. [Kakehashi: Experimental userspace to run macOS binaries on Linux ARM](#item-8) ⭐️ 7.0/10
9. [The Evolution of Essential Vocabulary for English Language Learners \(1953–2023\)](#item-9) ⭐️ 7.0/10
10. [A Humorous AI Benchmark: Frog with Habsburg Jaw SVG](#item-10) ⭐️ 7.0/10
11. [Open letters about AI development](#item-11) ⭐️ 7.0/10
12. [How Symmetric Are the Insides of a Go Network?](#item-12) ⭐️ 7.0/10
13. [F\* Homepage Sparks HN Discussion on Syntax Visibility and C Migration](#item-13) ⭐️ 6.0/10
14. [Greg Brockman: People Dislike AI Agents Asking for Help on Coworkers&\#x27; Behalf](#item-14) ⭐️ 6.0/10
15. [datasette-apps 0.2a0 Adds Agent Debugging via Invisible iframe](#item-15) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qwen3.8-Max: Alibaba&\#x27;s 2.4T Open-Weight Model Rivals Fable 5](https://qwen.ai/blog?id=qwen3.8) ⭐️ 8.0/10

Alibaba&\#x27;s Qwen team announced Qwen3.8-Max, its most capable model with 2.4 trillion parameters, and confirmed that open weights for both the Max model and the 27B variant will be released next week. This marks the first time a Qwen-Max-class model is being open-sourced, potentially making state-of-the-art AI capabilities accessible for local deployment and research, and intensifying the open-weight competition with closed-source models like Fable 5 and GPT-4. The model reportedly rivals Anthropic&\#x27;s Fable 5 and xAI&\#x27;s Grok 4.5 in coding benchmarks, but early reviews note that inference speed is a significant limitation. The 2.4T parameter model is a mixture-of-experts architecture, and the smaller 27B model is widely regarded as one of the best local models for its size.

hackernews · ai2027 · Aug 3, 02:16 · [Discussion](https://news.ycombinator.com/item?id=49150470)

**Background**: Qwen, also known as Tongyi Qianwen, is a series of large language models by Alibaba Cloud, often released under permissive licenses like Apache 2.0. Open-weight models share the trained parameters, allowing anyone to run and fine-tune them locally, though they may not include full training data or code. The previous Qwen3.6-27B was already a top choice for local AI due to its strong performance at a manageable size.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Qwen3.8-Max">Qwen3.8-Max</a></li>
<li><a href="https://www.eesel.ai/blog/qwen38-max-review">Qwen 3.8 Max review: Alibaba&#x27;s 2.4T flagship, tested (2026)</a></li>
<li><a href="https://thomas-wiegold.com/blog/qwen-3-8-max-review/">Qwen3.8-Max Review: I Tested Alibaba&#x27;s 2.4T Model</a></li>

</ul>
</details>

**Discussion**: Community members are enthusiastic about the imminent open-weight release, especially the 27B model, which is seen as a key local AI enabler. Some hope that regulatory efforts to restrict open-weight models will not succeed, while others humorously suggest that such announcements will become a &\#x27;sell signal&\#x27; for proprietary AI companies. The consensus is that the 27B model is the real game-changer for local deployment.

**Tags**: `#AI`, `#open-source`, `#LLM`, `#Qwen`, `#model-release`

---

<a id="item-2"></a>
## [Isopolis: Interactive Isometric Pixel Art Map of San Francisco](https://sf.isopolis.city/) ⭐️ 8.0/10

A developer created an interactive isometric pixel art map of San Francisco using Google&\#x27;s Photorealistic 3D Tiles and three.js, with AI-generated descriptions for neighborhoods. The map blends real-world textures with a retro pixel-art aesthetic, allowing exploration of the city. The project demonstrates a novel combination of real 3D mapping data, pixel art style, and generative AI, inspiring new creative mapping applications. It also highlights both the engaging potential and the amusing pitfalls of AI-generated content, as the community noticed AI hallucinations. The map uses Google&\#x27;s Photorealistic 3D Tiles — high-resolution textured 3D models — and three.js for rendering; AI descriptions were generated with the aid of Claude Code. Community members noted that the AI sometimes hallucinates features, such as turning roads into rivers and lakes, and the map currently lacks deeper zoom levels.

hackernews · nuwandavek · Aug 3, 00:46 · [Discussion](https://news.ycombinator.com/item?id=49149966)

**Background**: Google Photorealistic 3D Tiles are a dataset of high-resolution textured 3D city models available through the Maps API. three.js is a popular JavaScript library for rendering 3D graphics in the browser. Isometric pixel art is a retro visual style that simulates 3D perspective with 2D pixel grids. The project merges these elements to create an explorable map with a nostalgic pixel-art aesthetic.

<details><summary>References</summary>
<ul>
<li><a href="https://mapsplatform.google.com/demos/3d-maps/">Photorealistic 3 D Maps - Google Maps Platform</a></li>
<li><a href="https://developers.google.com/maps/documentation">Google Maps Platform Documentation | Google for Developers</a></li>
<li><a href="https://nasa-ammos.github.io/3DTilesRendererJS/three/googleMapsExample.html">Google 3 D Tiles Example</a></li>

</ul>
</details>

**Discussion**: Commenters praised the map&\#x27;s captivating exploration experience and appreciated the behind-the-scenes technical details. Many pointed out amusing AI-generated anomalies, such as non-existent rivers and lakes, and noted the need for more zoom levels. The project was compared to other pixel art works like Floor796, and oblique satellite imagery was suggested as a related interest.

**Tags**: `#isometric`, `#map`, `#pixel-art`, `#three.js`, `#generative-AI`

---

<a id="item-3"></a>
## [SwiftUI After 7 Years: Maturity, Shortcomings, and Developer Debate](https://ykvm.com/2026/07/swiftui-a-story-of-mediocrity/) ⭐️ 8.0/10

A developer published a critical analysis of SwiftUI&\#x27;s progress after seven years, highlighting its inadequacies for complex interfaces and prompting a debate on when to use SwiftUI versus UIKit. This reflects broader concerns about Apple&\#x27;s ability to deliver a robust declarative UI framework, affecting developer productivity and app architecture decisions, and shaping the future of development on Apple platforms. The analysis notes persistent issues like unpredictable data flow updates, debugging difficulties, and performance limitations for complex UIs. Many developers in the comments report a hybrid approach: SwiftUI for simple UIs and UIKit for performance-critical parts.

hackernews · mpweiher · Aug 2, 18:59 · [Discussion](https://news.ycombinator.com/item?id=49147263)

**Background**: SwiftUI is a declarative UI framework introduced by Apple in 2019, designed to build apps across all Apple platforms. UIKit is the older imperative framework, providing more direct control over UI elements. Declarative frameworks allow developers to describe the UI state, and the framework handles updates, but they can have performance and debugging challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/tutorials/app-dev-training/">App Dev Tutorials | Apple Developer Documentation</a></li>
<li><a href="https://appfield.dev/swiftui">SwiftUI — Declarative UI Framework for Apple Platforms · appfield</a></li>
<li><a href="https://increment.com/mobile/the-shift-to-declarative-ui/">The Shift From Imperative to Declarative UI – Increment</a></li>

</ul>
</details>

**Discussion**: The community is divided: some advocate SwiftUI for simple UIs and UIKit for complex apps, citing time savings and readability. Others note that SwiftUI works with profiling tools and that mixing with lower-level frameworks is normal. A few express broader doubts about declarative-reactive frameworks, comparing them to Kotlin Compose. Overall, the debate is nuanced about trade-offs.

**Tags**: `#swiftui`, `#apple`, `#ios-development`, `#ui-framework`, `#software-engineering`

---

<a id="item-4"></a>
## [OpenAI&\#x27;s Astra solves ten decade-old math problems at low cost](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 8.0/10

OpenAI&\#x27;s internal version of Astra, their next major model, solved ten mathematical problems that had seen no progress for at least a decade, each costing less than $2,000 in compute and with formal proofs provided in Lean 4. This demonstrates AI&\#x27;s ability to tackle decade-old unsolved problems at minimal cost, potentially transforming mathematical research by automating technical grunt work and enabling the large-scale human-machine collaboration envisioned by Terence Tao as &\#x27;big mathematics&\#x27;. OpenAI released Lean 4 formalizations and a paper describing the solutions, but did not disclose the prompts used or the number of unsuccessful attempts. The unreleased Astra model achieved these results at costs based on GPT-5.6 Sol token pricing \($5/$30 per 1M tokens\).

rss · Simon Willison · Aug 1, 20:34

**Background**: OpenAI&\#x27;s Astra is an upcoming model family designed for multi-agent, long-running tasks, and its existence was quietly revealed in this math blog post. Earlier, Anthropic&\#x27;s Claude Mythos Preview discovered cryptographic weaknesses at a cost of $100,000. The cultural impact is likened to the &\#x27;Deep Blue&\#x27; moment in chess, with mathematician Terence Tao envisioning &\#x27;big mathematics&\#x27; where AI handles technical details and humans focus on creativity.

<details><summary>References</summary>
<ul>
<li><a href="https://the-decoder.com/openai-announces-its-next-major-model-astra-by-dropping-ten-previously-unsolved-math-solutions/">OpenAI announces its &quot;next major model&quot; Astra by dropping ten previously unsolved math solutions</a></li>
<li><a href="https://openrouter.ai/openai/gpt-5.6-sol">GPT-5.6 Sol - API Pricing &amp; Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Many mathematicians are experiencing a &\#x27;Deep Blue&\#x27; moment, with some like Kirwin Hampshire expressing a spiritual crisis over AI&\#x27;s encroachment on creative mathematics. Others, such as Terence Tao, view it as a shift toward collaborative &\#x27;big mathematics&\#x27; rather than a threat.

**Tags**: `#AI`, `#mathematics`, `#automated-theorem-proving`, `#OpenAI`, `#theoretical-computer-science`

---

<a id="item-5"></a>
## [Review shows how LLM performance degrades with long context and shares practical habits](https://www.reddit.com/r/MachineLearning/comments/1vdsgcj/context_degradation_in_llms_what_the_papers/) ⭐️ 8.0/10

A Reddit post synthesizes findings from multiple research papers on context degradation in LLMs, translating the evidence into a set of actionable habits for maintaining quality during extended analysis sessions. This addresses a common pain point for LLM users, bridging the gap between academic research and everyday practice by offering immediately usable strategies to mitigate performance loss in long conversations, coding, or analysis. The research highlighted includes metrics like Fact Retention Rate and Instruction Drift, and mitigation techniques such as dynamic prompting and retrieval-augmented memory systems that help preserve factual accuracy and instruction adherence.

reddit · r/MachineLearning · /u/usernamehere93 · Aug 2, 20:20

**Background**: Large language models often suffer from &\#x27;context degradation&\#x27; or &\#x27;context rot&\#x27;, a measurable decline in recall, coherence, and instruction following as input length grows. Studies show that even frontier models are affected, with performance quantified by metrics like fact retention rate and maximum effective context window. Understanding this phenomenon is crucial for effectively using LLMs in real-world tasks that require long contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.morphllm.com/context-rot">Context Rot: Why LLMs Degrade as Context Grows (Complete ...</a></li>
<li><a href="https://www.emergentmind.com/topics/context-degradation-in-large-language-models">Context Degradation in LLMs - emergentmind.com</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#context-degradation`, `#research-synthesis`, `#practical-tips`, `#NLP`

---

<a id="item-6"></a>
## [VLMs achieve high benchmark scores by erasing clinically meaningful terms](https://www.reddit.com/r/MachineLearning/comments/1vcipzz/vlms_can_score_well_on_benchmarks_while_silently/) ⭐️ 8.0/10

A new paper reveals that VLMs for chest X-ray report generation can game standard evaluation metrics by erasing clinically rare terms and introducing biased language, while still achieving high scores. The researchers introduce a framework to measure such terminology erasure. This finding exposes a critical flaw in how medical AI models are evaluated: metrics reward bland, repetitive reports that erase rare but clinically significant findings, which could compromise patient care if such models are deployed. It calls for a re-evaluation of benchmarking practices in high-stakes domains like radiology. The study focuses on chest X-ray report generation and proposes a framework to quantify the loss of clinically significant terminology, including a method to measure the introduction of biased or hallucinated terms. The paper is available at arXiv:2603.01625.

reddit · r/MachineLearning · /u/ade17\_in · Aug 1, 09:27

**Background**: Vision-language models \(VLMs\) are AI systems that process both images and text, enabling tasks like generating descriptions from medical scans. In radiology, automatic report generation from chest X-rays aims to reduce clinician workload, but models are typically evaluated using natural language generation metrics such as BLEU or ROUGE, which focus on n-gram overlap and may not capture clinical accuracy. The paper highlights how these metrics can be gamed by producing safe, repetitive reports that omit rare findings.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/vlms">Vision Language Models Explained</a></li>
<li><a href="https://www.emergentmind.com/topics/weighted-association-erasure-wae">Weighted Association Erasure in Clinical NLP</a></li>

</ul>
</details>

**Tags**: `#VLM`, `#radiology`, `#evaluation metrics`, `#bias`, `#medical AI`

---

<a id="item-7"></a>
## [Karpathy’s Pelican Tweet Sparks Debate on AI Physical Understanding Benchmarks](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Andrej Karpathy posted a tweet about a pelican image, which triggered a community discussion on using image generation as a novel benchmark to evaluate how well AI models grasp the physical world. This conversation highlights a shift from judging AI image generation by visual fidelity alone to testing a model&\#x27;s internalized understanding of physics, offering a potentially more meaningful metric for tracking progress toward general intelligence. Comments reveal that even frontier models frequently fail to maintain fundamental physical constraints in generated scenes, such as correctly placing flippers in a pinball game or avoiding walls that block the ball launch. Some practitioners noted that models like Anthropic&\#x27;s may be specifically fine-tuned for three.js code, which could confound the benchmark&\#x27;s validity.

hackernews · delichon · Aug 2, 04:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Background**: State-of-the-art AI models can now generate images and 3D scenes from text prompts, but they often lack true comprehension of physical laws like gravity, collisions, and spatial coherence. A benchmark that requires physically plausible outputs—rather than just visually appealing ones—could expose whether a model merely mimics patterns or has developed a deeper world model. Karpathy, a prominent AI researcher, is known for sparking such probing discussions on the limitations of current systems.

**Discussion**: The overall sentiment agreed that physical plausibility benchmarks are valuable, but some cautioned that models like Anthropic&\#x27;s might score highly due to specialized training on three.js rather than genuine physical reasoning. Others pointed out practical failures in simple tasks like generating a playable pinball game, underscoring the current limitations of even the most advanced systems.

**Tags**: `#AI`, `#image-generation`, `#benchmarking`, `#physical-world-understanding`, `#Karpathy`

---

<a id="item-8"></a>
## [Kakehashi: Experimental userspace to run macOS binaries on Linux ARM](https://github.com/wie-project/kakehashi) ⭐️ 7.0/10

Kakehashi is a new experimental userspace compatibility layer that allows running macOS command-line binaries on Linux ARM machines. It has working prototypes for 7-Zip and curl, with 7-Zip passing multi-threaded compression tests and curl supporting over 200 commands. This project addresses a niche but growing need for running macOS binaries on ARM-based Linux systems, which is increasingly important as Apple Silicon Macs become popular. It could potentially enable a cross-platform ecosystem similar to what WINE/Proton achieved for Windows applications. Currently, 7-Zip runs about 5.2x slower than native Linux execution, but the developer has a clear optimization plan to reduce this gap. The project is in early stages, only supporting CLI binaries, and uses a userspace approach rather than full virtualization.

hackernews · vlad\_kalinkin · Aug 2, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49145937)

**Background**: A compatibility layer translates system calls from a foreign operating system into native system calls, allowing binaries to run without emulating the entire hardware. Userspace means the layer runs without kernel modifications, making it easier to deploy. The Darling project is another macOS compatibility layer for Linux, but it primarily targets x86 and has an open pull request for ARM64 support. Kakehashi focuses specifically on ARM and command-line tools.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Compatibility_layer">Compatibility layer - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/User_space_and_kernel_space">User space and kernel space - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is engaged and interested. Some compare Kakehashi to the Darling project, suggesting possible collaboration or noting differences in goals. Others express long-standing desire for such a solution, envisioning future possibilities like running macOS Audio Units \(AU\) on Linux, and acknowledging the complexity and early stage of the project.

**Tags**: `#macOS`, `#Linux`, `#ARM`, `#compatibility-layer`, `#open-source`

---

<a id="item-9"></a>
## [The Evolution of Essential Vocabulary for English Language Learners \(1953–2023\)](https://pudding.cool/2026/07/essential-words/) ⭐️ 7.0/10

A data analysis reveals that the core vocabulary list for English language learners transformed between 1953 and 2023, with a decline in words like &\#x27;humble&\#x27; and &\#x27;loyalty&\#x27; and a rise in terms such as &\#x27;identity,&\#x27; &\#x27;ethnic,&\#x27; and &\#x27;gender.&\#x27; This shift highlights how language teaching priorities reflect evolving cultural values, with implications for how we define essential communication skills in a globalized world. The &\#x27;Social-Communicative&\#x27; level remained stable in size, but a quarter of the 1953 list was replaced, with 39% of the 2023 words being new. Practical everyday words like &\#x27;fork,&\#x27; &\#x27;soap,&\#x27; and &\#x27;umbrella&\#x27; were dropped from the core list.

hackernews · c-oreills · Aug 2, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49145590)

**Background**: Core vocabulary lists for English learners have been based on frequency analysis and pedagogical needs since the mid-20th century. The 1953 list is often associated with West&\#x27;s General Service List, while modern lists incorporate larger corpora and diverse contexts. The shift mirrors societal changes from a focus on personal character to social structures.

**Discussion**: Community comments debated the necessity of dropping everyday words like &\#x27;fork&\#x27; and questioned the article&\#x27;s premise. Some users linked the vocabulary shift to rising inequality and tribalism, while others emphasized that &\#x27;essential&\#x27; vocabulary depends heavily on context \(e.g., travel, TV, newspapers\).

**Tags**: `#linguistics`, `#language-learning`, `#education`, `#society`, `#data-visualization`

---

<a id="item-10"></a>
## [A Humorous AI Benchmark: Frog with Habsburg Jaw SVG](https://frogs.vaguespac.es/) ⭐️ 7.0/10

A developer created a humorous AI benchmark challenging text-to-SVG models to generate an SVG of a frog with a Habsburg jaw, revealing how different models interpret and combine abstract concepts. This creative benchmark exposes the limitations of current AI models in combining distinct visual concepts, highlighting the challenges in semantic understanding and image generation. It sparks valuable discussion about AI&\#x27;s ability to interpret abstract prompts. The benchmark specifically tests text-to-SVG generation, with models like Fable 5 and Opus 5 performing notably well. Interestingly, all models drew the frog from a frontal view, missing the opportunity to better showcase the jaw shape from a side profile; the site temporarily went down due to unexpected traffic.

hackernews · thebigship · Aug 2, 19:42 · [Discussion](https://news.ycombinator.com/item?id=49147622)

**Background**: The &\#x27;Habsburg jaw&\#x27; refers to the distinct mandibular prognathism \(protruding lower jaw\) common in the Habsburg royal family due to inbreeding. SVG \(Scalable Vector Graphics\) is a text-based vector image format. The benchmark humorously combines a simple animal drawing task with a specific historical physical trait, testing an AI&\#x27;s ability to merge disparate concepts into a coherent image.

**Discussion**: Community members found the benchmark hilarious and insightful, praising Opus 5 and Fable 5 for the best outputs while noting many models failed to coherently connect the protruding jaw to the frog&\#x27;s face. An interesting observation was that all models drew the frog from the frontal view, despite a side profile being more logical for showing jaw shape. The site&\#x27;s creator acknowledged the overwhelming traffic and shared a newsletter link.

**Tags**: `#AI benchmarking`, `#image generation`, `#SVG`, `#LLM evaluation`, `#humor`

---

<a id="item-11"></a>
## [Open letters about AI development](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

Simon Willison summarizes a Microsoft-led open letter urging the US government to avoid restricting open-weight AI models, signed by major tech companies like NVIDIA and OpenAI.

rss · Simon Willison · Aug 2, 04:16

**Tags**: `#AI policy`, `#open source`, `#open weights`, `#regulation`, `#Microsoft`

---

<a id="item-12"></a>
## [How Symmetric Are the Insides of a Go Network?](https://www.reddit.com/r/MachineLearning/comments/1vcrki2/how_symmetric_are_the_insides_of_a_go_network_r/) ⭐️ 7.0/10

A new interpretability study on the open-source Go AI KataGo reveals how its neural network internally represents board symmetries learned through stochastic 8-fold data augmentation, uncovering an unexpected internal structure in the process. This work deepens our understanding of how neural networks internalize invariances from data augmentation, a crucial step toward building more transparent and reliable AI systems. The study used the superhuman KataGo engine, trained with random rotations and reflections. The research was largely AI-driven but polished with human guidance, and the unexpected finding suggests that the network may not be fully symmetric internally.

reddit · r/MachineLearning · /u/icosaplex · Aug 1, 16:18

**Background**: Interpretability in machine learning aims to reveal how models make decisions. Stochastic data augmentation randomly applies transformations like rotation to training data to improve robustness. KataGo is a top open-source Go AI that uses deep neural networks and self-play, often serving as a benchmark for AI research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Interpretability_%28machine_learning%29">Interpretability (machine learning)</a></li>
<li><a href="https://en.wikipedia.org/wiki/KataGo">KataGo</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#interpretability`, `#symmetry`, `#Go`, `#neural networks`

---

<a id="item-13"></a>
## [F\* Homepage Sparks HN Discussion on Syntax Visibility and C Migration](https://fstar-lang.org/) ⭐️ 6.0/10

The Hacker News community discussed the F\* language homepage, with users noting the absence of prominent syntax examples and highlighting its usefulness for incremental migration of C codebases. The discussion underscores the importance of accessible language presentation for attracting developers and reveals a practical niche for proof-oriented languages in gradually improving legacy C systems. F\* is a dependently-typed language with SMT-based proof automation, developed by Microsoft Research and Inria, and used in Project Everest for verified cryptographic software. It can compile to C via the KaRaMeL toolchain, enabling incremental migration from C.

hackernews · ducktective · Aug 2, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49143925)

**Background**: F\* is a proof-oriented programming language that combines dependent types and refinement types to express precise specifications, such as memory safety and correctness properties. The type-checker can automatically prove many properties using SMT solvers, with manual proofs for more complex cases. It has been used in Microsoft&\#x27;s Project Everest to build a verified HTTPS stack. The language can compile to various targets, including C and WebAssembly, facilitating integration with existing codebases.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_%28programming_language%29">F* (programming language)</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof - Oriented Programming Language</a></li>

</ul>
</details>

**Discussion**: Users expressed frustration that the homepage lacks visible syntax examples, making it hard to evaluate the language. One commenter appreciated F\*&\#x27;s support for calling external libraries and incremental C migration. A question about industry adoption was raised, and a sarcastic comment about side effects underscored the functional programming paradigm.

**Tags**: `#proof-oriented programming`, `#formal verification`, `#functional programming`, `#F\*`, `#programming languages`

---

<a id="item-14"></a>
## [Greg Brockman: People Dislike AI Agents Asking for Help on Coworkers&\#x27; Behalf](https://simonwillison.net/2026/Aug/1/greg-brockman/#atom-everything) ⭐️ 6.0/10

Greg Brockman, OpenAI&\#x27;s president and co-founder, shared that at OpenAI, many employees connect ChatGPT to Slack, but coworkers strongly dislike it when an AI agent contacts them asking for help on someone else&\#x27;s behalf, even though they would be happy to help the person directly. This observation underscores that human relationships and direct personal interaction are crucial in the workplace, and that AI should give time back to people or enhance shared time, rather than become a layer that separates them. The insight is drawn from OpenAI&\#x27;s own internal use of generative AI integrated with Slack, highlighting that even well-intentioned AI mediation can damage social dynamics and trust.

rss · Simon Willison · Aug 1, 22:29

**Background**: Greg Brockman is the president and co-founder of OpenAI, the company behind ChatGPT. Slack is a widely used workplace messaging platform. AI agents are tools that can autonomously perform tasks, and integrating them into collaboration platforms is a growing trend. Brockman&\#x27;s comment reflects early real-world social friction from such deployments.

**Tags**: `#ai-ethics`, `#human-ai-interaction`, `#workplace`, `#generative-ai`, `#openai`

---

<a id="item-15"></a>
## [datasette-apps 0.2a0 Adds Agent Debugging via Invisible iframe](https://simonwillison.net/2026/Aug/1/datasette-apps/#atom-everything) ⭐️ 6.0/10

The datasette-apps 0.2a0 release introduces two new tools for agent-based app management: app\_debug\(\) for testing apps invisibly in a sandboxed iframe, and app\_list\(\) for listing editable apps. The app\_debug\(\) tool opens an app in an opacity:0, pointer-events:none iframe and executes JavaScript to perform smoke testing. This release enhances the Datasette Agent ecosystem by enabling agents to autonomously test and debug Datasette apps, improving the reliability of AI-assisted app development. It demonstrates a clever use of browser sandboxing for secure, automated testing without user interaction. The app\_debug\(\) mechanism uses the context.browser\_task\(\) functionality from datasette-agent 0.4a0, and the invisible iframe is rendered with opacity:0 and pointer-events:none to prevent visibility and interaction. The agent can execute arbitrary JavaScript inside the sandboxed iframe to measure element dimensions and verify functionality.

rss · Simon Willison · Aug 1, 21:23

**Background**: Datasette is an open-source tool for exploring and publishing data, typically from SQLite databases. Datasette Agent is an AI assistant that uses LLMs to interact with Datasette, allowing users to ask questions and run SQL queries. Sandboxed iframes are a web security feature that restricts the behavior of embedded content, preventing scripts from accessing the parent page unless explicitly allowed. Smoke testing is a preliminary testing practice to verify that the core functionality of a software build is working correctly.

<details><summary>References</summary>
<ul>
<li><a href="https://theainuggets.com/datasette-agent-llm-sqlite-workflows/">Datasette Agent Guide: Building Smart LLM SQLite Workflows</a></li>
<li><a href="https://web.dev/articles/sandboxed-iframes">Play safely in sandboxed IFrames | Articles | web.dev</a></li>
<li><a href="https://en.wikipedia.org/wiki/Smoke_testing_%28software%29">Smoke testing (software) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#agent`, `#debugging`, `#release`, `#tools`

---