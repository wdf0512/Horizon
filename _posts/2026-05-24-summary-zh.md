---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 34 items, 7 important content pieces were selected

---

1. [Pydantic v2.14.0a1 发布：弃用 Python 3.9，增加 Emscripten 平台轮子](#item-1) ⭐️ 9.0/10
2. [特朗普政府要求绿卡申请人必须离开美国递交申请](#item-2) ⭐️ 9.0/10
3. [Anthropic 公布 Project Glasswing 初期成果：AI 发现逾万高危漏洞](#item-3) ⭐️ 9.0/10
4. [苹果开源 CoreCrypto 密码库，附带形式化验证证明量子安全算法正确性](#item-4) ⭐️ 9.0/10
5. [SpaceX 星舰 v3 试飞克服发动机故障实现精准着陆](#item-5) ⭐️ 8.0/10
6. [80386 微码从芯片裸片图像中成功逆向提取并解析](#item-6) ⭐️ 8.0/10
7. [NVIDIA Nemotron-Labs 推出扩散语言模型，实现光速文本生成](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Pydantic v2.14.0a1 发布：弃用 Python 3.9，增加 Emscripten 平台轮子](https://github.com/pydantic/pydantic/releases/tag/v2.14.0a1) ⭐️ 9.0/10

Pydantic v2.14.0a1 是一个预发布版本，弃用了对 Python 3.9 的支持，移除了 `eval_type_backport()` 函数，并增加了面向 Pyodide 314.0+ 环境的 PyEmscripten 平台轮子支持。 该版本包含破坏性变更：弃用 Python 3.9 会迫使仍在使用该版本的项目升级运行时，移除 `eval_type_backport()` 可能破坏自定义类型求值代码。但同时，增加 PyEmscripten 轮子支持使得 Pydantic 能够通过 Pyodide 在浏览器和 WebAssembly 环境中运行，拓展了应用场景。 PyEmscripten 轮子的平台标签为 `pyemscripten_2026_0`，目标运行环境为尚在开发中的 Pyodide 314.0。该 alpha 版本还包含对 Mypy 插件的修复以及 `model_copy()` 的优化。值得注意的是，被移除的 `eval_type_backport()` 函数是一个用于旧式类型提示行为的向后兼容垫片。

github · Viicos · May 22, 13:46

**背景**: Pyodide 是一个基于 WebAssembly 的 Python 发行版，可在浏览器和 Node.js 中运行，实现客户端的 Python 执行。PyEmscripten 平台标签标识了为 Emscripten 编译环境构建的特定应用程序二进制接口（ABI），版本化的标签（`pyemscripten_2026_0`）表示与 Pyodide 314.0 的兼容性。此前，Pydantic 的 `eval_type_backport()` 函数用于在缺少内置 `typing.get_type_hints()` 改进的旧版本 Python（3.9 及更早）中求值类型提示；随着 Python 3.9 支持被弃用，该兼容垫片不再需要。Pydantic 本身是一个广泛使用的、基于 Python 类型注解的数据验证与设置管理库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pyodide.org/en/stable/development/abi.html">The PyEmscripten Platform — Version 0.29.3</a></li>
<li><a href="https://pyodide.org/en/latest/development/abi.html">The PyEmscripten Platform — Version 314.0.0.dev0</a></li>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly · GitHub</a></li>

</ul>
</details>

**标签**: `#breaking-change`, `#deprecation`

---

<a id="item-2"></a>
## [特朗普政府要求绿卡申请人必须离开美国递交申请](https://www.nytimes.com/2026/05/22/us/politics/green-card-changes-trump.html) ⭐️ 9.0/10

特朗普政府发布新政策，要求大多数绿卡申请人必须离开美国并从境外申请，终止了持工作签证在境内调整身份的长期惯例。 这打乱了数十万 H-1B 等签证持有者的合法移民路径，威胁劳动力稳定和家庭团聚，可能促使人才流向其他国家。 该政策依据 USCIS 备忘录 PM-602-0199，仅“特殊情况”允许境内调整身份，迫使申请人进入领事处理，尤其在无美国领事馆的国家，等待时间可长达数年。

hackernews · tlhunter · May 22, 21:27 · [社区讨论](https://news.ycombinator.com/item?id=48241890)

**背景**: “调整身份”允许已持特定签证在美人士无需离境即可申请绿卡。而“领事处理”则要求离境并在海外使领馆面签等待签发，可能导致家庭分离数月甚至数年，对美籍子女家庭尤甚。

**社区讨论**: 评论者震惊愤怒，指出这颠覆了技术移民的标准流程。他们以亲身经历描述了领事处理的多年等待和家庭分离风险，并质疑鉴于绿卡持有者的全球纳税义务，美国是否仍具吸引力。

**标签**: `#immigration`, `#green-card`, `#tech-industry`, `#policy`, `#H-1B`

---

<a id="item-3"></a>
## [Anthropic 公布 Project Glasswing 初期成果：AI 发现逾万高危漏洞](https://www.anthropic.com/research/glasswing-initial-update) ⭐️ 9.0/10

Anthropic 的 Project Glasswing 项目利用 Claude Mythos Preview 模型，在一个月内从关键软件中识别出逾万个高危和严重漏洞，扫描了数千个开源项目并从中发现 6,202 个高危漏洞，其中经审查的漏洞有 90.6%为真阳性。Cloudflare 等合作伙伴表示漏洞发现速率提升了十倍以上。 这些结果表明 AI 能够大幅规模化漏洞发现，将瓶颈从检测转移到验证和修复环节。这凸显了软件行业迫切需要调整修复流程以跟上自动化发现的速度，否则未修复漏洞的积压可能增加安全风险。 在被审查的漏洞中，模型达到了 90.6%的真阳性率，但验证工作仍需人工审查。开源维护者表示不堪重负，甚至请求放缓漏洞报告速度。Anthropic 已与开源安全基金会（OpenSSF）合作并推出 Claude Security 工具辅助修复，同时强调随着同类模型普及，行业必须缩短补丁周期。

telegram · zaihuapd · May 23, 03:16

**背景**: Project Glasswing 是 Anthropic 的一项利用 AI 进行防御性网络安全的计划，专注于关键开源基础设施。它使用了 Claude Mythos Preview 这一通用前沿 AI 模型，该模型仅向有限的行业合作伙伴和开源开发者开放用于安全测试。开源安全基金会（OpenSSF）是 Linux 基金会旗下的跨行业组织，旨在协作提升开源软件安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/04/08/anthropic-claude-mythos-preview-identify-vulnerabilities/">Anthropic's new AI model finds and exploits... - Help Net Security</a></li>
<li><a href="https://openssf.org/">Open Source Security Foundation - Linux Foundation Projects</a></li>

</ul>
</details>

**标签**: `#AI安全`, `#漏洞发现`, `#Anthropic`, `#软件安全`

---

<a id="item-4"></a>
## [苹果开源 CoreCrypto 密码库，附带形式化验证证明量子安全算法正确性](https://security.apple.com/blog/formal-verification-corecrypto/) ⭐️ 9.0/10

苹果公开了其 corecrypto 密码库的源代码，其中包含抗量子算法 ML-KEM 和 ML-DSA 的 C 语言及手工优化的 ARM64 汇编实现，并首次提供了端到端的形式化验证数学证明，确保这些实现与 NIST 标准严格一致。 此举使为超过 25 亿台活跃设备提供加密运算的基础库可被独立审计，为高保障软件实践树立了新的里程碑，并将推动整个行业的抗量子密码迁移进程。 验证覆盖了 ML-KEM（FIPS 203）和 ML-DSA（FIPS 204）两种算法。苹果还公开了其定制的验证工具以及 Isabelle 理论文件，让独立专家能够复现和评估这些证明。

telegram · zaihuapd · May 23, 04:49

**背景**: ML-KEM（原 Kyber）和 ML-DSA 是 NIST 于 2024 年标准化的后量子密码算法，基于格密码难题，旨在抵御未来量子计算机的攻击。形式化验证是一种用数学方法严格证明代码实现与规范完全一致的技术，能从根本上消除特定类别的错误。Isabelle 是一种高阶逻辑证明助手，常用于大规模形式化数学证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ML-KEM">ML-KEM</a></li>
<li><a href="https://en.wikipedia.org/wiki/ML-DSA">ML-DSA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isabelle_(proof_assistant)">Isabelle (proof assistant)</a></li>

</ul>
</details>

**标签**: `#苹果`, `#开源`, `#密码学`, `#形式化验证`, `#量子安全`

---

<a id="item-5"></a>
## [SpaceX 星舰 v3 试飞克服发动机故障实现精准着陆](https://www.space.com/space-exploration/launches-spacecraft/spacex-starship-v3-megarocket-first-test-flight) ⭐️ 8.0/10

SpaceX 的星舰 v3 试飞中，助推器和飞船均出现多台发动机故障，但上面级仍然精准着陆在目标点。飞行还首次展示了无隔热瓦烧穿的全流程再入，验证了制导软件的鲁棒性。 此次飞行验证了 SpaceX 快速迭代的理念，通过真实飞行中的失败学习加速开发。发动机故障下的精准着陆表明制导系统已相当成熟，这对未来的月球和火星任务至关重要。 关键细节：助推器在上升段损失一台发动机，返场点火失败，导致硬溅落且偏离目标。星舰上面级在级间分离后不久也损失一台发动机，但恢复后精确着陆；再入过程中无热斑，模拟星链卫星在舰体后方烧毁可见。

hackernews · busymom0 · May 22, 23:41 · [社区讨论](https://news.ycombinator.com/item?id=48242959)

**背景**: 星舰是 SpaceX 研制的完全可重复使用超重型运载火箭，用于月球、火星等深空任务。v3 是最新原型型号，此前各型号逐步攻克了起飞、级间分离、再入等技术。SpaceX 的开发理念强调快速原型、实战测试和从失败中学习，而非等待地面充分验证。此次试飞旨在验证再入、着陆和系统整体鲁棒性。

**社区讨论**: 社区总体反响积极，对制导系统在发动机故障下仍能精确着陆表示赞叹，但也对助推器返场失败感到失望。评论者欣赏 SpaceX“够用就好”的快速迭代策略与快速数据收集。无烧穿的干净再入和模拟卫星烧毁的视觉奇观成为特别关注的亮点。

**标签**: `#space-exploration`, `#rocketry`, `#guidance-software`, `#iterative-development`, `#spacex`

---

<a id="item-6"></a>
## [80386 微码从芯片裸片图像中成功逆向提取并解析](https://www.reenigne.org/blog/80386-microcode-disassembled/) ⭐️ 8.0/10

一篇由 reenigne 发布的博客详细描述了如何从高分辨率芯片裸片图像中提取并反汇编 Intel 80386 处理器的微码，首次完整揭示了每条机器指令对应的内部微操作序列。 这一突破为硬件历史学者和复古计算爱好者提供了关于经典 80386 架构前所未有的洞察，证实了此前对其微程序设计的猜测，并保存了可能遗失的技术知识。 研究人员通过目视裸片照片中 ROM 区域的晶体管有无来识别位图案，随后进行反汇编，揭示了微指令格式及复杂 CISC 指令的控制序列，但重建过程中可能存在小范围的不确定性。

hackernews · nand2mario · May 23, 12:11 · [社区讨论](https://news.ycombinator.com/item?id=48247004)

**背景**: 微码是许多 CPU 内部的一层隐藏低级控制程序，负责将高阶机器指令（如 x86）翻译成更简单的硬件操作步骤。Intel 80386 于 1985 年发布，是首个具备保护模式等先进特性的 32 位 x86 处理器，其复杂指令实现大量依赖微码。裸片成像能够捕捉芯片晶体管级的物理结构，通过检查 ROM 存储区域，经验丰富的逆向工程师可以重建其中保存的二进制数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microcode">Microcode</a></li>

</ul>
</details>

**社区讨论**: 评论区对这项逆向工程壮举印象深刻，对如何从裸片照片中读取位数据表示好奇。有人提及相关项目（如基于原始微码的开源 80386 z386），也有人推荐了微程序设计书籍。总体氛围充满赞赏和技术兴趣。

**标签**: `#microcode`, `#reverse-engineering`, `#intel-80386`, `#cpu-architecture`, `#retrocomputing`

---

<a id="item-7"></a>
## [NVIDIA Nemotron-Labs 推出扩散语言模型，实现光速文本生成](https://huggingface.co/blog/nvidia/nemotron-labs-diffusion) ⭐️ 8.0/10

NVIDIA 的 Nemotron-Labs 展示了一种扩散语言模型，通过并行迭代去噪生成文本，摒弃了传统的逐词预测，实现了近乎即时的输出速度。 这一突破可能彻底改变文本生成领域，克服自回归模型的顺序瓶颈，实现实时低延迟的 AI 交互，并有望降低大规模部署的计算成本。 该模型采用扩散过程，从随机词元序列中逐步去除噪声以生成连贯文本。它属于 Nemotron 开源模型家族，提供开放权重，但具体架构和训练数据仍在开发中。

rss · Hugging Face Blog · May 23, 00:02

**背景**: 扩散模型最初用于图像生成，通过逆向去噪过程将随机噪声转化为图像。在文本中，它们对受破坏的词元序列进行去噪以形成连贯语句。与 GPT 等自回归模型逐词预测不同，扩散语言模型可同时生成所有词元，使推理速度提升数个量级。NVIDIA 的 Nemotron 计划致力于为专用智能体开发高效的开源 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/collections/nvidia/nemotron-labs-diffusion">Nemotron - Labs -Diffusion - a nvidia Collection</a></li>
<li><a href="https://developer.nvidia.com/nemotron">Nemotron AI Models | NVIDIA Developer</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#language models`, `#text generation`, `#NVIDIA`, `#inference speed`

---