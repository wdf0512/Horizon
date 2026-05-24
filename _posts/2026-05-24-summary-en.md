---
layout: default
title: "Horizon Summary: 2026-05-24 (EN)"
date: 2026-05-24
lang: en
---

> From 34 items, 9 important content pieces were selected

---

1. [Pydantic 2.14.0a1 Drops Python 3.9 and eval_type_backport](#item-1) ⭐️ 9.0/10
2. [Nemotron-Labs Diffusion Model Promises Speed-of-Light Text Generation](#item-2) ⭐️ 9.0/10
3. [Anthropic's Project Glasswing Finds Over 10,000 Critical Vulnerabilities in One Month](#item-3) ⭐️ 9.0/10
4. [Apple Open Sources corecrypto with Formal Verification of Quantum-Safe Algorithms](#item-4) ⭐️ 9.0/10
5. [HTML <dl> Element Deep Dive Triggers Semantic and Accessibility Discussion](#item-5) ⭐️ 8.0/10
6. [C# Finally Gets Union Types in .NET 11 Preview 2](#item-6) ⭐️ 8.0/10
7. [Intel 80386 microcode disassembled from die images](#item-7) ⭐️ 8.0/10
8. [Making Deep Learning Go Brrrr from First Principles](#item-8) ⭐️ 8.0/10
9. [Cloudflare's WAF misconfiguration caused 25-minute global outage impacting 28% of HTTP traffic](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Pydantic 2.14.0a1 Drops Python 3.9 and eval_type_backport](https://github.com/pydantic/pydantic/releases/tag/v2.14.0a1) ⭐️ 9.0/10

Pydantic's v2.14.0a1 alpha release drops support for Python 3.9 and removes the `eval_type_backport()` compatibility shim, introducing breaking changes alongside a new PyEmscripten wheel for pydantic-core and fixes for the Mypy plugin. Production systems still running Python 3.9 will be unable to upgrade to this version, compelling them to migrate to a newer Python runtime to receive future updates, security patches, and features. The removal of eval_type_backport eliminates a historical workaround for type annotation evaluation on legacy interpreters. The `eval_type_backport()` function, previously used to evaluate PEP 604 union types and other modern annotations on older Python versions, is removed; pydantic now relies on Python 3.10+ native mechanisms. The new PyEmscripten wheel (with the `pyemscripten_2026_0` tag) targets the still-in-development Pyodide 314.0 runtime for WebAssembly environments.

github · Viicos · May 22, 13:46

**Background**: Python 3.9 reached its end-of-life in November 2025, so many libraries are dropping support. The eval_type_backport package was a temporary bridge that allowed pydantic (and others) to evaluate newer typing constructs on Python <3.10 by backporting the `typing._eval_type` function. The PyEmscripten platform tag denotes Python builds compiled for Emscripten/Wasm, commonly used with Pyodide to run Python in the browser.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pydantic/pydantic/issues/9910">get install the `eval_type_backport` error, though don't use new types syntax · Issue #9910 · pydantic/pydantic</a></li>
<li><a href="https://github.com/alexmojaki/eval_type_backport/">GitHub - alexmojaki/eval_type_backport: Like `typing._eval_type`, but lets older Python versions use newer typing features. · GitHub</a></li>
<li><a href="https://pyodide.org/en/latest/development/abi.html">The PyEmscripten Platform — Version 314.0.0.dev0</a></li>

</ul>
</details>

**Tags**: `#breaking-change`

---

<a id="item-2"></a>
## [Nemotron-Labs Diffusion Model Promises Speed-of-Light Text Generation](https://huggingface.co/blog/nvidia/nemotron-labs-diffusion) ⭐️ 9.0/10

NVIDIA has introduced Nemotron-Labs Diffusion, a tri-mode language model that combines autoregressive, diffusion, and self-speculation decoding for dramatically faster text generation, as detailed in a research paper published five days ago. This breakthrough challenges the dominant autoregressive paradigm by enabling parallel token generation, potentially reducing inference time and costs by orders of magnitude for real-time applications. The model uses a joint AR-diffusion training objective and can dynamically switch between modes: autoregressive for quality, diffusion for speed via iterative denoising, and self-speculation for further acceleration while maintaining throughput.

rss · Hugging Face Blog · May 23, 00:02

**Background**: Traditional autoregressive models generate text one token at a time, causing latency proportional to output length. Diffusion language models instead iteratively denoise a sequence of masked tokens in parallel, akin to image generation, but text's discrete nature made this challenging. Nemotron-Labs Diffusion bridges this gap by combining both approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://research.nvidia.com/publication/2026-05_nemotron-labs-diffusion-tri-mode-language-model-unifying-autoregressive">Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding | Research</a></li>
<li><a href="https://medium.com/@vickythevgn/large-language-diffusion-models-b4d0e6826057">Large Language Diffusion Models . Welcome to a new... | Medium</a></li>

</ul>
</details>

**Tags**: `#diffusion language models`, `#text generation`, `#NVIDIA`, `#speed optimization`, `#natural language processing`

---

<a id="item-3"></a>
## [Anthropic's Project Glasswing Finds Over 10,000 Critical Vulnerabilities in One Month](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic's Project Glasswing, powered by the Claude Mythos Preview model, discovered over 10,000 high or critical vulnerabilities in software from about 50 partners and scanned thousands of open-source projects, uncovering 6,202 such flaws with a 90.6% true positive rate among verified reports. This demonstrates that AI can dramatically accelerate vulnerability discovery, shifting the bottleneck from detection to remediation and pressuring the industry to shorten patch cycles as automated bug hunting becomes mainstream. The model achieved a 90.6% true positive rate on verified reports, but the sheer volume overwhelmed human triage and patching, leading open-source maintainers to ask for slower vulnerability reports. Anthropic has released Claude Security tools and partnered with the Open Source Security Foundation to help enterprises manage the flood.

telegram · zaihuapd · May 23, 03:16

**Background**: Project Glasswing is a defensive cybersecurity initiative by Anthropic, launched in April 2026, built around Claude Mythos Preview, a new frontier model more capable than previous Opus models. The project aims to secure critical software by leveraging this model's advanced code analysis, and it marks one of the first large-scale deployments of AI for automated vulnerability discovery.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/claude-mythos-preview-on-vertex-ai">Claude Mythos Preview on Vertex AI | Google Cloud Blog</a></li>

</ul>
</details>

**Tags**: `#AI安全`, `#漏洞挖掘`, `#Anthropic`, `#安全自动化`

---

<a id="item-4"></a>
## [Apple Open Sources corecrypto with Formal Verification of Quantum-Safe Algorithms](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 9.0/10

Apple has open-sourced its corecrypto library, releasing implementations of the post-quantum algorithms ML-KEM and ML-DSA along with end-to-end formal verification proofs. These proofs guarantee that both C code and hand-optimized ARM64 assembly strictly conform to NIST standards. This is the first public release of end-to-end formal verification for quantum-safe algorithms on such a massive scale, deployed on over 2.5 billion active devices where corecrypto provides foundational encryption. It sets a new benchmark for cryptographic assurance and demonstrates a strong commitment to post-quantum security. The verification covers both C code and hand-optimized ARM64 assembly; Apple also released custom verification tools and Isabelle theory libraries for independent expert assessment. The algorithms are lattice-based, standardized by NIST as FIPS 203 and FIPS 204, and resistant to attacks from future quantum computers.

telegram · zaihuapd · May 23, 04:49

**Background**: ML-KEM (Module-Lattice-Based Key-Encapsulation Mechanism) and ML-DSA (Module-Lattice-Based Digital Signature Algorithm) are post-quantum cryptographic algorithms recently standardized by NIST in 2024, designed to replace current public-key schemes vulnerable to quantum Shor's algorithm. Formal verification is a mathematical process that proves software exactly meets its specification, eliminating implementation bugs at the highest assurance level. Apple's corecrypto is the low-level cryptographic engine used across iOS, macOS, and other platforms for operations like encryption, key exchange, and digital signatures. The public release of these proofs advances trust in Apple's security infrastructure and encourages wider adoption of formal methods in critical software.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>

</ul>
</details>

**Tags**: `#密码学`, `#形式化验证`, `#量子安全`

---

<a id="item-5"></a>
## [HTML <dl> Element Deep Dive Triggers Semantic and Accessibility Discussion](https://benmyers.dev/blog/on-the-dl/) ⭐️ 8.0/10

A detailed 2021 blog post exploring the semantics, accessibility pitfalls, and real-world use of the HTML <dl> element gained renewed attention on Hacker News, sparking a lively debate with 370 upvotes and 110 comments. The discussion highlights the persistent ambiguity and implementation challenges of semantic HTML, directly affecting how screen readers and other assistive technologies interpret content, making it a crucial topic for inclusive web development. The <dl> element, renamed from 'definition list' to 'description list' in HTML5, has no inherent ARIA role; using aria-label on it is non-conforming, as noted by commenters. Its lineage extends to IBM's 1985 GML, and Tim Berners-Lee's first website heavily employed it.

hackernews · ravenical · May 23, 13:03 · [Discussion](https://news.ycombinator.com/item?id=48247325)

**Background**: Semantic HTML uses markup to convey meaning, not just presentation, aiding accessibility and SEO. The <dl> element represents a description list of term-description pairs (<dt> and <dd>). Proper ARIA roles and labels are crucial for screen readers, which rely on semantic information to navigate and interpret page structure.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl">HTML description list element - HTML | MDN</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semantic_HTML">Semantic HTML</a></li>

</ul>
</details>

**Discussion**: Commenters debated the practicality of semantic HTML: one argued that <dl> is too inflexible for real-world designs, while others provided technical corrections about invalid aria-label usage. Historical roots from IBM's GML and the first website's heavy <dl> usage were highlighted, adding context about the element's evolution. The discussion reflected a mix of pragmatic frustration and a desire for cleaner, more accessible markup.

**Tags**: `#HTML`, `#semantic HTML`, `#accessibility`, `#web development`, `#front-end`

---

<a id="item-6"></a>
## [C# Finally Gets Union Types in .NET 11 Preview 2](https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/) ⭐️ 8.0/10

C# is introducing union types in .NET 11 Preview 2, a long-requested language feature that allows developers to define types that can hold values of different kinds, improving type safety and expressiveness. Union types enable more precise modeling of data that can be in several states, reducing boilerplate code and runtime errors. This enhancement brings C# closer to languages like F# and TypeScript, making it more attractive for modern application development. The feature introduces a `union` keyword and supports pattern matching for exhaustiveness checks, but the precise syntax and integration details are still being refined. The current implementation is in preview and may evolve.

hackernews · ingve · May 22, 12:28 · [Discussion](https://news.ycombinator.com/item?id=48234954)

**Background**: Union types, also known as sum types or discriminated unions, are a fundamental concept in functional programming languages. They allow a variable to be one of several predefined types, each possibly carrying different data. C# already has enums and class hierarchies, but union types provide a more concise and type-safe way to express alternatives without the overhead of inheritance or the limitations of enums. In the C# community, this feature has been one of the most requested for over a decade, as it addresses common patterns like representing success/failure results or state machines.

<details><summary>References</summary>
<ul>
<li><a href="https://www.typescriptlang.org/docs/handbook/2/everyday-types.html">TypeScript: Documentation - Everyday Types</a></li>

</ul>
</details>

**Discussion**: The community is largely enthusiastic, with long-time C# developers expressing relief that union types are finally arriving. Comments highlight that this feature has been awaited for a decade, and some note that F# has had it for years, pointing out C# gradually adopting functional features. Others appreciate that C# is adding high-performance capabilities while maintaining ease of use. A few joke about classic bugs that could be avoided with union types.

**Tags**: `#c#`, `#dotnet`, `#union-types`, `#programming-languages`, `#language-design`

---

<a id="item-7"></a>
## [Intel 80386 microcode disassembled from die images](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

A detailed disassembly of the Intel 80386 microprocessor's microcode has been published, extracted from high-resolution die photographs on the reenigne blog. This reveals the internal microprogram sequences that control instruction execution. This reverse-engineering achievement provides unprecedented visibility into a historically significant CPU's design, offering insights for x86 architecture study and inspiring open-source hardware projects like the z386 core. The microcode was lifted from a specific 80386 die revision, but the exact stepping is unknown; the disassembly likely covers instruction decode and complex execution sequences. Extraction relied on identifying the microcode ROM layout from die photos and decoding the bit patterns.

hackernews · nand2mario · May 23, 12:11 · [Discussion](https://news.ycombinator.com/item?id=48247004)

**Background**: Microcode is a low-level firmware inside a CPU that translates machine instructions (e.g., x86) into sequences of internal control signals, allowing complex instructions to be implemented with more flexibility than pure hardware. The Intel 80386, launched in 1985, was a landmark 32-bit processor that used microcode for many operations. Die shots are high-resolution photographs of a chip's silicon die, which reverse engineers can analyze to trace circuits and extract stored data like microcode.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microcode">Microcode - Wikipedia</a></li>
<li><a href="https://www.hackster.io/news/ken-shirriff-offers-an-introduction-to-reverse-engineering-cmos-chips-from-die-shots-baa40e81ca5a">Ken Shirriff Offers an Introduction to Reverse Engineering CMOS Chips From Die Shots - Hackster.io</a></li>

</ul>
</details>

**Discussion**: Readers were intrigued by the extraction process, asking how microcode can be reconstructed from die images. A related discussion about an open-source 80386 core built from the original microcode was linked, and a commenter stressed the importance of identifying the specific 80386 stepping due to many small changes during its long production run.

**Tags**: `#microcode`, `#80386`, `#reverse-engineering`, `#CPU-architecture`, `#retro-computing`

---

<a id="item-8"></a>
## [Making Deep Learning Go Brrrr from First Principles](https://horace.io/brrr_intro.html) ⭐️ 8.0/10

A 2022 blog post, 'Making deep learning go brrrr from first principles', has resurfaced on Hacker News with 159 points and 59 comments, offering a systematic, low-level analysis of deep learning performance bottlenecks and optimization tactics. The post bridges the gap between hardware capabilities and real-world ML software efficiency, exposing how even powerful GPUs are often underutilized. The ensuing discussion highlights fragmentation in inference runtimes and Python overhead, issues that directly affect cost and scalability for anyone deploying models. The analysis quantifies Python’s overhead: one Python FLOP corresponds to 9.75 million FLOPs on an A100 GPU. Commenters note NVIDIA’s sustained exponential growth in compute and bandwidth, the portability mess between ONNX, CUDA, and TensorRT runtimes, and the counterintuitive speed of chained method calls like x.cos().cos().

hackernews · tosh · May 23, 11:50 · [Discussion](https://news.ycombinator.com/item?id=48246889)

**Background**: Deep learning models rely on GPUs for massive parallel computation. Performance depends on memory bandwidth, compute throughput, and software stack efficiency. ONNX is a model interchange format, and TensorRT is an NVIDIA inference optimizer, but they often yield inconsistent performance across different hardware and configurations.

**Discussion**: The community widely praised the post as a classic, with appreciation for its clarity on hardware-software mismatches. Key viewpoints: NVIDIA’s lead has been remarkably sustained; the inference runtime landscape (ONNX, TensorRT, etc.) is a “humongous mess”; and the staggering Python overhead prompted a detailed question about how x.cos().cos() outperforms two separate cos calls.

**Tags**: `#deep learning`, `#performance optimization`, `#GPU`, `#systems`, `#machine learning`

---

<a id="item-9"></a>
## [Cloudflare's WAF misconfiguration caused 25-minute global outage impacting 28% of HTTP traffic](https://t.me/zaihuapd/41527) ⭐️ 8.0/10

Cloudflare experienced a global network outage lasting 25 minutes on December 5, 2025, due to an erroneous WAF change made while patching the Next.js vulnerability CVE-2025-55182. The incident affected approximately 28% of HTTP traffic, primarily impacting customers using the legacy FL1 proxy with Cloudflare-managed rulesets. This outage highlights how even a well-intentioned security fix can cascade into a massive infrastructure failure, affecting millions of websites. It serves as a critical lesson for SREs and DevOps teams on the need for rigorous testing and canary deployments before applying WAF rule changes in production environments. The outage started at 08:47 UTC and fully recovered by 09:12 UTC. The root cause was a WAF rule change that incorrectly handled traffic when mitigating the React2Shell RCE (CVE-2025-55182), specifically impacting users on the legacy FL1 proxy infrastructure with Cloudflare's managed rules enabled.

telegram · zaihuapd · May 22, 16:15

**Background**: CVE-2025-55182 is a critical unauthenticated RCE in React Server Components, often targeted via Next.js's App Router. Cloudflare's Web Application Firewall (WAF) uses managed rulesets to protect against such exploits. The FL1 proxy is a legacy component of Cloudflare's edge network, and customers still using it were uniquely exposed to this misconfiguration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/react2shell-cve-2025-55182-critical-rce-vulnerability-react-wjfgc">React2Shell ( CVE - 2025 - 55182 ): Critical RCE Vulnerability in React...</a></li>
<li><a href="https://www.kaspersky.com/blog/react4shell-vulnerability-cve-2025-55182/54915/">CVE - 2025 - 55182 vulnerability in React and... | Kaspersky official blog</a></li>
<li><a href="https://react.dev/reference/rsc/server-components">Server Components – React</a></li>

</ul>
</details>

**Tags**: `#事故复盘`, `#基础设施`, `#WAF`, `#Cloudflare`, `#可观测性`

---