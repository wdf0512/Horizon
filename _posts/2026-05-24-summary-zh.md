---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 34 items, 9 important content pieces were selected

---

1. [Pydantic 2.14.0a1 放弃 Python 3.9 支持并移除 eval_type_backport](#item-1) ⭐️ 9.0/10
2. [Nemotron-Labs 扩散模型有望实现光速文本生成](#item-2) ⭐️ 9.0/10
3. [Anthropic 公布 Project Glasswing 初期成果：AI 发现逾万高危漏洞](#item-3) ⭐️ 9.0/10
4. [苹果开源 corecrypto 并附形式化验证，确保量子安全算法正确性](#item-4) ⭐️ 9.0/10
5. [深度解析 HTML <dl>元素引发语义与可访问性讨论](#item-5) ⭐️ 8.0/10
6. [C# 终于在 .NET 11 Preview 2 中引入联合类型](#item-6) ⭐️ 8.0/10
7. [英特尔 80386 微码从裸片图像中被成功反汇编](#item-7) ⭐️ 8.0/10
8. [深度学习性能优化：第一性原理剖析](#item-8) ⭐️ 8.0/10
9. [Cloudflare WAF 错误配置导致 25 分钟全球故障，影响 28% HTTP 流量](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Pydantic 2.14.0a1 放弃 Python 3.9 支持并移除 eval_type_backport](https://github.com/pydantic/pydantic/releases/tag/v2.14.0a1) ⭐️ 9.0/10

Pydantic 的 v2.14.0a1 预览版放弃了对 Python 3.9 的支持，并移除了 `eval_type_backport()` 兼容补丁，同时引入了 pydantic-core 的 PyEmscripten 平台 wheel 包、多项 Mypy 插件修复等变更。 仍运行 Python 3.9 的生产环境将无法升级到该版本，迫使它们迁移到较新的 Python 运行时才能获得未来的更新、安全修复和新功能。移除 eval_type_backport 则彻底放弃了在旧解释器上评估类型注解的历史方案。 `eval_type_backport()` 函数此前用于在旧版 Python 上求值 PEP 604 联合类型等现代注解，现已删除；pydantic 转而依赖 Python 3.10+ 的原生机制。新增的 PyEmscripten wheel 包（使用 `pyemscripten_2026_0` 标签）针对尚在开发中的 Pyodide 314.0 WebAssembly 运行时。

github · Viicos · May 22, 13:46

**背景**: Python 3.9 已于 2025 年 11 月结束生命周期，众多库正陆续放弃其支持。eval_type_backport 包是一个临时桥梁，通过反向移植 `typing._eval_type` 函数，让 pydantic 等库能在低于 3.10 的 Python 上求值新型类型构造。PyEmscripten 平台标签标识了为 Emscripten/Wasm 编译的 Python 构建，常配合 Pyodide 在浏览器中运行 Python。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pydantic/pydantic/issues/9910">get install the `eval_type_backport` error, though don't use new types syntax · Issue #9910 · pydantic/pydantic</a></li>
<li><a href="https://github.com/alexmojaki/eval_type_backport/">GitHub - alexmojaki/eval_type_backport: Like `typing._eval_type`, but lets older Python versions use newer typing features. · GitHub</a></li>
<li><a href="https://pyodide.org/en/latest/development/abi.html">The PyEmscripten Platform — Version 314.0.0.dev0</a></li>

</ul>
</details>

**标签**: `#breaking-change`

---

<a id="item-2"></a>
## [Nemotron-Labs 扩散模型有望实现光速文本生成](https://huggingface.co/blog/nvidia/nemotron-labs-diffusion) ⭐️ 9.0/10

NVIDIA 发布了 Nemotron-Labs Diffusion，这是一种三模态语言模型，融合了自回归、扩散和自推测解码，以实现大幅加速的文本生成，相关研究论文于五天前发表。 这项突破通过实现并行 token 生成，挑战了主流的自回归范式，可能将实时应用的推理时间和成本降低数个数量级。 该模型使用联合自回归-扩散训练目标，并能动态切换模式：自回归保证质量，扩散通过迭代去噪提升速度，自推测则在保持吞吐量的同时进一步加速。

rss · Hugging Face Blog · May 23, 00:02

**背景**: 传统自回归模型逐 token 生成文本，导致延迟随输出长度线性增长。扩散语言模型则通过并行方式迭代去噪一组掩码 token 序列（类似图像生成），但文本的离散特性曾使这一方法面临挑战。Nemotron-Labs Diffusion 通过融合两种方法弥合了这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.nvidia.com/publication/2026-05_nemotron-labs-diffusion-tri-mode-language-model-unifying-autoregressive">Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding | Research</a></li>
<li><a href="https://medium.com/@vickythevgn/large-language-diffusion-models-b4d0e6826057">Large Language Diffusion Models . Welcome to a new... | Medium</a></li>

</ul>
</details>

**标签**: `#diffusion language models`, `#text generation`, `#NVIDIA`, `#speed optimization`, `#natural language processing`

---

<a id="item-3"></a>
## [Anthropic 公布 Project Glasswing 初期成果：AI 发现逾万高危漏洞](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic 的 Project Glasswing 项目利用 Claude Mythos Preview 模型，在一个月内从约 50 个合作伙伴的软件中找出逾万个高危或严重漏洞，并扫描数千个开源项目发现 6202 个此类漏洞，经审核的真阳性率达 90.6%。 这表明 AI 可大幅加速漏洞发现，将瓶颈从检测转向修复，并随着自动化挖洞走向普及，迫使行业缩短补丁周期。 模型在已审核的报告上达到 90.6%的真阳性率，但海量漏洞远超人工分诊和修复能力，开源维护者甚至请求放缓报告速度。Anthropic 已发布 Claude Security 工具并与开源安全基金会合作，协助企业应对漏洞洪流。

telegram · zaihuapd · May 23, 03:16

**背景**: Project Glasswing 是 Anthropic 于 2026 年 4 月推出的防御性网络安全项目，基于全新前沿模型 Claude Mythos Preview，其能力超越以往的 Opus 系列。该项目旨在利用该模型的先进代码分析能力保护关键软件，是 AI 在自动化漏洞发现领域的首次大规模应用之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing : Securing critical software for the AI era \ Anthropic</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/claude-mythos-preview-on-vertex-ai">Claude Mythos Preview on Vertex AI | Google Cloud Blog</a></li>

</ul>
</details>

**标签**: `#AI安全`, `#漏洞挖掘`, `#Anthropic`, `#安全自动化`

---

<a id="item-4"></a>
## [苹果开源 corecrypto 并附形式化验证，确保量子安全算法正确性](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 9.0/10

苹果开源了 corecrypto 密码库，首次公开了用于抵御未来量子计算机的 ML-KEM 和 ML-DSA 算法实现，并提供了端到端的形式化验证数学证明，确保其 C 代码和手工优化的 ARM64 汇编与 NIST 标准严格一致。 这是首次在如此大规模上公开为量子安全算法提供端到端形式化验证，已部署于超过 25 亿台活跃设备，为密码学保障树立新标杆，并彰显了对后量子安全的有力承诺。 验证覆盖了 C 代码和手工优化的 ARM64 汇编实现；苹果同时公开了定制验证工具和 Isabelle 理论库，供独立专家评估。这些算法基于格密码，分别被 NIST 标准化为 FIPS 203 和 FIPS 204，能够抵抗未来量子计算机的攻击。

telegram · zaihuapd · May 23, 04:49

**背景**: ML-KEM（基于模格的密钥封装机制）和 ML-DSA（基于模格的数字签名算法）是 NIST 于 2024 年标准化的后量子密码算法，旨在替代易受量子 Shor 算法攻击的现有公钥方案。形式化验证是一种通过数学方法严格证明软件实现与规范完全一致的过程，可消除实现错误，达到最高安全保障等级。苹果的 corecrypto 是用于 iOS、macOS 等平台的低层密码引擎，负责加密、密钥交换和数字签名等基础运算。此次公开发布这些证明，不仅增强了用户对其安全基础设施的信任，也推动了关键软件中形式化方法的广泛采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>

</ul>
</details>

**标签**: `#密码学`, `#形式化验证`, `#量子安全`

---

<a id="item-5"></a>
## [深度解析 HTML <dl>元素引发语义与可访问性讨论](https://benmyers.dev/blog/on-the-dl/) ⭐️ 8.0/10

一篇 2021 年深度解析 HTML <dl>元素语义、无障碍缺陷及实际应用的文章在 Hacker News 上重新引起关注，获得了 370 个点赞并引发了 110 条评论的热烈讨论。 此次讨论突显了语义 HTML 的持续模糊性和实现挑战，直接影响屏幕阅读器等辅助技术对内容的解释方式，这对无障碍网页开发至关重要。 <dl>元素在 HTML5 中从“定义列表”更名为“描述列表”，没有隐式 ARIA 角色；直接在<dl>上使用 aria-label 不符合规范，这一点在评论中被指出。其渊源可追溯至 IBM 1985 年的 GML，而万维网第一个网页也大量使用了<dl>。

hackernews · ravenical · May 23, 13:03 · [社区讨论](https://news.ycombinator.com/item?id=48247325)

**背景**: 语义 HTML 通过标记传达内容含义，而非仅仅控制外观，有助于无障碍访问和 SEO。<dl>元素表示由术语-描述对（<dt>和<dd>）组成的描述列表。合理使用 ARIA 角色和标签对屏幕阅读器至关重要，它们依赖语义信息来导航和解释页面结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl">HTML description list element - HTML | MDN</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semantic_HTML">Semantic HTML</a></li>

</ul>
</details>

**社区讨论**: 评论者中有人认为语义 HTML 过于僵化，例如<dl>在实际设计中缺乏灵活性；也有人纠正了技术细节，指出文章中对<dl>使用 aria-label 不合规范。讨论还揭示了该元素的 GML 渊源及首个网站的用法，体现了对实用性与无障碍标记的不同关注点。

**标签**: `#HTML`, `#semantic HTML`, `#accessibility`, `#web development`, `#front-end`

---

<a id="item-6"></a>
## [C# 终于在 .NET 11 Preview 2 中引入联合类型](https://andrewlock.net/exploring-the-dotnet-11-preview-2-dotnet-gets-union-types/) ⭐️ 8.0/10

C# 在 .NET 11 Preview 2 中引入了联合类型，这是一项期待已久的语言特性，允许开发者定义可持有多种类型值的类型，从而提升类型安全性和表达能力。 联合类型可以对可能处于多种状态的数据进行更精确的建模，减少样板代码和运行时错误。这一增强使 C# 更接近 F# 和 TypeScript 等语言，使其在现代应用开发中更具吸引力。 该特性引入了 `union` 关键字并支持模式匹配以进行穷举检查，但具体语法和集成细节仍在完善中。当前实现处于预览阶段，可能会有所变化。

hackernews · ingve · May 22, 12:28 · [社区讨论](https://news.ycombinator.com/item?id=48234954)

**背景**: 联合类型，也称为求和类型或可区分联合，是函数式编程语言中的一个基本概念。它允许变量是多个预定义类型之一，每种类型可能携带不同的数据。C# 已有枚举和类层次结构，但联合类型提供了一种更简洁且类型安全的方式来表达替代方案，无需继承的开销或枚举的限制。在 C# 社区中，这一特性十多年来一直是最受请求的特性之一，因为它解决了诸如表示成功/失败结果或状态机等常见模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.typescriptlang.org/docs/handbook/2/everyday-types.html">TypeScript: Documentation - Everyday Types</a></li>

</ul>
</details>

**社区讨论**: 社区总体上非常热情，长期使用 C# 的开发者对联合类型终于到来表示欣慰。评论强调这一功能已经等了十年，有人指出 F# 多年前就有此功能，认为 C# 正在逐步吸收函数式特性。还有人赞赏 C# 在增加高性能能力的同时保持了易用性。一些人开玩笑说联合类型本可以避免经典的 bug。

**标签**: `#c#`, `#dotnet`, `#union-types`, `#programming-languages`, `#language-design`

---

<a id="item-7"></a>
## [英特尔 80386 微码从裸片图像中被成功反汇编](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

reenigne 博客发布了一份详细的英特尔 80386 微处理器微码反汇编，该微码是从高分辨率裸片照片中提取的。这揭示了控制指令执行的内部微程序序列。 这一逆向工程成就为深入了解这款历史性 CPU 的设计提供了前所未有的视角，为 x86 架构研究提供了见解，并启发了 z386 内核等开源硬件项目。 该微码提取自某一特定版本的 80386 裸片，但确切步进未知；反汇编内容可能涵盖指令解码和复杂的执行序列。提取过程依赖于从裸片照片识别微码 ROM 布局并解码其比特模式。

hackernews · nand2mario · May 23, 12:11 · [社区讨论](https://news.ycombinator.com/item?id=48247004)

**背景**: 微码是 CPU 内部的一层底层固件，它将机器指令（如 x86）转换为内部控制信号的序列，从而能够以比纯硬件更灵活的方式实现复杂指令。1985 年推出的英特尔 80386 是一款里程碑式 32 位处理器，许多操作都采用微码实现。裸片照片是芯片硅片的高分辨率图像，逆向工程师可借此分析电路并提取存储的数据（如微码）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microcode">Microcode - Wikipedia</a></li>
<li><a href="https://www.hackster.io/news/ken-shirriff-offers-an-introduction-to-reverse-engineering-cmos-chips-from-die-shots-baa40e81ca5a">Ken Shirriff Offers an Introduction to Reverse Engineering CMOS Chips From Die Shots - Hackster.io</a></li>

</ul>
</details>

**社区讨论**: 读者对提取过程很感兴趣，询问如何从裸片图像重建微码。有人链接了一个关于基于原始微码构建开源 80386 的相关讨论，还有评论者强调，鉴于该处理器在漫长生产周期中历经多次小改动，确定具体的 80386 步进版本很重要。

**标签**: `#microcode`, `#80386`, `#reverse-engineering`, `#CPU-architecture`, `#retro-computing`

---

<a id="item-8"></a>
## [深度学习性能优化：第一性原理剖析](https://horace.io/brrr_intro.html) ⭐️ 8.0/10

一篇 2022 年的技术文章《从第一性原理让深度学习飞速运转》在 Hacker News 上重获关注，获得 159 分和 59 条评论，该文从底层系统性地剖析了深度学习的性能瓶颈与优化技巧。 这篇文章揭示了硬件能力与实际机器学习软件效率之间的差距，说明强大 GPU 经常未被充分利用。后续讨论指出了推理运行时的碎片化和 Python 开销问题，这些问题直接影响模型部署的成本和可扩展性。 文章量化了 Python 开销：执行一次浮点运算的时间内，A100 GPU 可完成 975 万次浮点运算。评论指出 NVIDIA 在计算能力和带宽上的持续指数级增长，ONNX、CUDA 和 TensorRT 等运行时之间的移植混乱，以及 x.cos().cos()链式调用为何更快的反直觉现象。

hackernews · tosh · May 23, 11:50 · [社区讨论](https://news.ycombinator.com/item?id=48246889)

**背景**: 深度学习模型依赖 GPU 进行大规模并行计算。性能取决于内存带宽、计算吞吐量和软件栈效率。ONNX 是一种模型交换格式，TensorRT 是 NVIDIA 的推理优化器，但在不同硬件和配置下常表现出不一致的性能。

**社区讨论**: 社区普遍称赞该文章为经典之作，并赞赏其对硬件-软件不匹配的清晰揭示。主要观点包括：NVIDIA 的领先地位令人瞩目地持续；推理运行时（如 ONNX、TensorRT 等）是一片“庞杂的混乱”；Python 的巨大开销引发了对 x.cos().cos()为何比两次单独调用更快的深入提问。

**标签**: `#deep learning`, `#performance optimization`, `#GPU`, `#systems`, `#machine learning`

---

<a id="item-9"></a>
## [Cloudflare WAF 错误配置导致 25 分钟全球故障，影响 28% HTTP 流量](https://t.me/zaihuapd/41527) ⭐️ 8.0/10

2025 年 12 月 5 日，Cloudflare 在修复 Next.js 漏洞 CVE-2025-55182 时，因对 WAF 进行了错误更改，导致全球网络中断 25 分钟。此次故障影响了约 28%的 HTTP 流量，主要波及使用旧版 FL1 代理和 Cloudflare 托管规则集的客户。 此次事故表明，即使是善意的安全修复也可能引发大规模基础设施故障，影响数百万网站。它为 SRE 和 DevOps 团队敲响警钟：在生产环境中修改 WAF 规则前，必须执行严格的测试和灰度发布。 故障于世界标准时间 08:47 开始，09:12 完全恢复。根本原因是 Cloudflare 为缓解 React2Shell 远程代码执行漏洞（CVE-2025-55182）而修改 WAF 规则时，错误地处理了流量，特别影响了使用旧版 FL1 代理并启用了托管规则的客户。

telegram · zaihuapd · May 22, 16:15

**背景**: CVE-2025-55182 是 React Server Components 中的一个严重的无需认证的远程代码执行漏洞，通常通过 Next.js 的 App Router 被利用。Cloudflare 的 Web 应用防火墙（WAF）通过托管规则集提供保护。FL1 代理是 Cloudflare 边缘网络的旧组件，此次错误配置只影响了仍在使用它的客户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/react2shell-cve-2025-55182-critical-rce-vulnerability-react-wjfgc">React2Shell ( CVE - 2025 - 55182 ): Critical RCE Vulnerability in React...</a></li>
<li><a href="https://www.kaspersky.com/blog/react4shell-vulnerability-cve-2025-55182/54915/">CVE - 2025 - 55182 vulnerability in React and... | Kaspersky official blog</a></li>
<li><a href="https://react.dev/reference/rsc/server-components">Server Components – React</a></li>

</ul>
</details>

**标签**: `#事故复盘`, `#基础设施`, `#WAF`, `#Cloudflare`, `#可观测性`

---