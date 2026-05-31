---
layout: default
title: "Horizon Summary: 2026-05-31 (EN)"
date: 2026-05-31
lang: en
---

> From 37 items, 7 important content pieces were selected

---

1. [Microsoft to Disable Offline Editing in Perpetual Office 2019/2021 for Mac](#item-1) ⭐️ 8.0/10
2. [Domain Expertise Is the Real Moat in the AI Era](#item-2) ⭐️ 8.0/10
3. [Zig 0.16.0 Overhauls Build System for Faster Development Cycles](#item-3) ⭐️ 8.0/10
4. [OpenBSD Team Develops Openrsync, a Clean-Room rsync Implementation](#item-4) ⭐️ 8.0/10
5. [Anthropic Shares How It Sandboxes Claude Across Products](#item-5) ⭐️ 8.0/10
6. [Running Python ASGI apps in the browser with Pyodide and a service worker](#item-6) ⭐️ 8.0/10
7. [Huawei's 'Tao's Law' replaces geometry scaling with time scaling, targeting 1.4nm density by 2031](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Microsoft to Disable Offline Editing in Perpetual Office 2019/2021 for Mac](https://consumerrights.wiki/w/Microsoft_Office_2019_and_2021_for_Mac_view-only_conversion_(2026)) ⭐️ 8.0/10

Microsoft has announced that it will convert perpetually licensed Office 2019 and 2021 for Mac into view-only mode, removing offline editing capabilities. This move effectively downgrades a previously purchased 'permanent' software license. This change erodes trust in perpetual software licenses and may violate consumer protection laws in jurisdictions like Australia. It signals a broader industry trend where vendors retroactively alter purchased products, forcing users into recurring subscriptions. The conversion is reportedly planned for 2026, affecting Office 2019 and 2021 for Mac. Users who rely on offline editing will be locked out, with speculation that this move is partly driven by Microsoft's desire to monetize AI agent integrations that use Office applications.

hackernews · antipurist · May 30, 23:26 · [Discussion](https://news.ycombinator.com/item?id=48341578)

**Background**: A perpetual license grants the user the right to use software indefinitely without recurring fees, akin to owning a product. In contrast, modern 'as-a-service' models like Microsoft 365 require ongoing payments. Office 2019 and 2021 for Mac were sold as standalone, non-subscription versions, marketed as classic fixed-in-time releases. Microsoft's decision to later revoke core functionality challenges the permanence of such licenses.

**Discussion**: The community overwhelmingly condemns Microsoft's move. Commenters argue it violates Australian consumer guarantees (right to undisturbed possession) and view it as a betrayal of promised perpetual licensing. Some speculate that the accelerated timeline is driven by Microsoft's desire to charge per AI agent instance, while others advocate switching to open-source alternatives like LibreOffice.

**Tags**: `#Microsoft`, `#software licensing`, `#consumer rights`, `#Office deprecation`, `#AI agents`

---

<a id="item-2"></a>
## [Domain Expertise Is the Real Moat in the AI Era](https://www.brethorsting.com/blog/2026/05/domain-expertise-has-always-been-the-real-moat/) ⭐️ 8.0/10

The blog argues that in an AI-driven world, deep domain expertise has become the enduring competitive advantage over mere proficiency with AI tools, a shift supported by real-world failures of AI-generated applications when lacking domain context. This redefines career value for software engineers: rather than focusing solely on coding, they must cultivate deep knowledge in specific industries to remain indispensable, as AI commoditizes generic development tasks. Community stories included a fishing charter app where the domain expert captain identified data needs invisible to a generalist, and a business app that seemed ready but had a flawed database design, illustrating that domain insight is critical to steer AI effectively.

hackernews · aaronbrethorst · May 30, 20:40 · [Discussion](https://news.ycombinator.com/item?id=48340411)

**Background**: In business, a 'moat' is a sustainable advantage. With AI coding assistants, the bottleneck shifts from writing code to understanding problems. Domain expertise means specialized knowledge of a field like healthcare or logistics. The tech debate centers on whether AI will commoditize software engineering, leaving domain expertise as the last valuable skill.

**Discussion**: Comments largely concurred: a restaurant app's messed-up database and a fishing tool's overlooked data needs showed AI can't replace domain knowledge. Some cautioned that this advice is a moving target, while another argued software engineering itself is a domain expertise worth preserving.

**Tags**: `#domain expertise`, `#AI`, `#software engineering`, `#career development`, `#moat`

---

<a id="item-3"></a>
## [Zig 0.16.0 Overhauls Build System for Faster Development Cycles](https://ziglang.org/devlog/2026/#2026-05-26) ⭐️ 8.0/10

Zig's build system has been completely reworked in version 0.16.0, introducing significant improvements to compilation speed, tooling, and developer feedback loops. The rework reduces edit-compile-run cycles to milliseconds, making Zig more appealing for systems programming where fast iteration is critical. It demonstrates the language's commitment to developer experience and long-term viability. The new build system integrates an updated IO mechanism that enables highly efficient code regardless of concurrency model (single-threaded, multi-threaded, or event loop). The overhaul required many code changes but resulted in a more streamlined and consistent developer workflow.

hackernews · tosh · May 30, 08:38 · [Discussion](https://news.ycombinator.com/item?id=48334048)

**Background**: Zig is a general-purpose systems programming language that emphasizes simplicity, speed, and safety. Its build system, written in Zig itself, replaces traditional external build tools like Make or CMake, providing a seamless development experience. Prior to version 0.16.0, the build system had grown increasingly complex, and this rework aimed to unify and simplify it, improving incremental compilation and overall responsiveness.

**Discussion**: Community members report concrete improvements after upgrading, with particular praise for the new IO abstraction that works efficiently across concurrency models. The focus on tooling and fast feedback loops—rather than adding language features—is widely seen as a smart long-term investment, making Zig a favorite for tinkering and rapid development.

**Tags**: `#zig`, `#build-system`, `#tooling`, `#systems-programming`, `#developer-experience`

---

<a id="item-4"></a>
## [OpenBSD Team Develops Openrsync, a Clean-Room rsync Implementation](https://github.com/kristapsdz/openrsync) ⭐️ 8.0/10

The OpenBSD team has been developing Openrsync, a from-scratch, clean-room reimplementation of the rsync file synchronization tool, with a focus on security and reliability. Community discussion highlights real-world usage experiences, remaining gaps compared to the original Samba rsync, and the project's role in a larger RPKI validator initiative. The project addresses long-standing security concerns with the original rsync codebase, especially after recent rushed, regressive commits. If successful, it could provide a more secure, BSD-licensed alternative for critical file transfer operations, reinforcing defense-in-depth with OpenBSD's hallmark privilege separation features. Openrsync is built as a clean-room design to avoid copyright issues, and it leverages OpenBSD's pledge(2) and unveil(2) calls for privilege separation, though Linux portability of these features remains a challenge. Early adopters note a mismatch when specifying remote file paths using --rsync-path=openrsync, which creates an unintended subdirectory instead of the expected file.

hackernews · sph · May 30, 10:51 · [Discussion](https://news.ycombinator.com/item?id=48334854)

**Background**: Rsync is a widely used utility for efficiently syncing files between systems over a network. A clean-room implementation involves reverse engineering a system's behavior without referencing copyrighted source code, thus creating an independent work. OpenBSD is a security-oriented Unix-like operating system known for innovations like pledge (restrict system calls) and unveil (restrict file system access), which drastically reduce the impact of potential vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Clean_room_implementation">Clean room implementation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Openrsync">Openrsync</a></li>

</ul>
</details>

**Discussion**: Users are generally optimistic, with one noting improved stability over time and looking forward to exclusive use. The main criticism is an inconsistency in remote path handling compared to Samba rsync. Others provide context that the project is part of an RPKI validator, point to an alternative Go implementation, and stress that the security gains rely heavily on pledge/unveil support, which is still lacking on Linux.

**Tags**: `#openbsd`, `#rsync`, `#security`, `#networking`, `#go`

---

<a id="item-5"></a>
## [Anthropic Shares How It Sandboxes Claude Across Products](https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything) ⭐️ 8.0/10

Anthropic published a comprehensive engineering article detailing its sandboxing techniques for Claude across products, revealing how it uses process sandboxes, VMs, filesystem boundaries, and egress controls to set hard security boundaries. This level of transparency addresses a critical trust gap for AI agents, enabling developers to understand and assess the security guarantees, while setting a benchmark for responsible deployment of autonomous AI systems. Claude.ai uses gVisor for process isolation; Claude Code applies Seatbelt on macOS and Bubblewrap on Linux; Cowork runs inside full VMs via Apple's Virtualization framework and Windows HCS. The article also discloses a previously missed exfiltration vector through the files API endpoint.

rss · Simon Willison · May 30, 21:36

**Background**: Sandboxing restricts an application's ability to access the host system, preventing unauthorized actions. gVisor is a user-space kernel from Google that intercepts Linux system calls for container isolation. Seatbelt is Apple's macOS kernel sandbox, while Bubblewrap is an unprivileged sandbox tool commonly used by Flatpak on Linux. Full virtual machines provide the strongest hardware-level isolation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GVisor">GVisor</a></li>
<li><a href="https://github.com/containers/bubblewrap">GitHub - containers/bubblewrap: Low-level unprivileged sandboxing tool used by Flatpak and similar projects · GitHub</a></li>
<li><a href="https://theapplewiki.com/wiki/Dev:Seatbelt">Dev:Seatbelt - The Apple Wiki</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#sandboxing`, `#Claude`, `#Anthropic`, `#security`

---

<a id="item-6"></a>
## [Running Python ASGI apps in the browser with Pyodide and a service worker](https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything) ⭐️ 8.0/10

Simon Willison experimented with using a service worker alongside Pyodide to run Python ASGI apps entirely in the browser, overcoming the previous limitation where JavaScript in <script> tags would not execute in Datasette Lite. This technique could significantly enhance browser-based Python web applications by enabling full compatibility with JavaScript-dependent features and plugins, potentially expanding the use cases for tools like Datasette Lite. It also demonstrates how WebAssembly and service workers can be combined to bring more server-side functionality to the client. Willison used Claude Opus 4.8 via Claude Code for web to implement the prototype, and the demos show a basic ASGI FastCGI app and Datasette 1.0a31 running. The approach requires a service worker to intercept network requests and relay them to a Pyodide Python environment, but the exact mechanism is still being understood by the author.

rss · Simon Willison · May 30, 21:02

**Background**: Datasette Lite is a version of the Datasette tool that runs entirely in the browser using Pyodide, a Python distribution compiled to WebAssembly. Previously, it relied on web workers to run Python and fetch HTML, but any JavaScript inside <script> tags was not executed, breaking certain Datasette features and plugins. Service workers are scripts that the browser runs in the background, separate from a web page, enabling features like intercepting network requests and acting as a proxy, which can be used to serve content even when offline. ASGI (Asynchronous Server Gateway Interface) is a standard interface between web servers and Python web applications that supports asynchronous capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pyodide/pyodide">GitHub - pyodide/pyodide: Pyodide is a Python distribution for the browser and Node.js based on WebAssembly · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Asynchronous_Server_Gateway_Interface">Asynchronous Server Gateway Interface - Wikipedia</a></li>
<li><a href="https://web.dev/learn/pwa/service-workers">Service workers | web.dev</a></li>

</ul>
</details>

**Tags**: `#Pyodide`, `#WebAssembly`, `#ASGI`, `#service-workers`, `#Datasette`

---

<a id="item-7"></a>
## [Huawei's 'Tao's Law' replaces geometry scaling with time scaling, targeting 1.4nm density by 2031](https://t.me/zaihuapd/41648) ⭐️ 8.0/10

On May 25, 2026, at IEEE ISCAS 2026 in Shanghai, Huawei introduced 'Tao's Law,' a new semiconductor scaling principle that uses 'time scaling' (reducing the time constant τ) instead of traditional geometry scaling to improve chip performance and density. The company has already produced 381 chip designs based on this approach and will release a new Kirin phone chip with logic folding technology this autumn. As Moore's Law approaches physical limits and access to advanced lithography remains restricted for Chinese companies, Tao's Law offers a new path to increase transistor density without relying on EUV tools or extreme geometry shrinks. It could reshape the semiconductor roadmap, influence AI hardware development, and challenge the 'process node-centric' mindset. The core of Tao's Law is to systematically compress signal propagation delay through design innovations such as 'logic folding' (a form of 3D integration within a single die). The upcoming Kirin 2026 chip uses double-layer logic folding, achieving a 53.5% increase in transistor density and 41% better energy efficiency. Huawei projects that by 2031 its high-end chips will reach an effective transistor density equivalent to a 1.4nm node.

telegram · zaihuapd · May 30, 02:18

**Background**: Moore's Law has historically driven semiconductor progress by physically shrinking transistor dimensions (geometry scaling), but it is now hitting physical and economic limits, requiring extremely expensive EUV lithography. The time constant τ represents how fast a circuit can switch; reducing τ improves performance without necessarily shrinking transistors. Huawei, facing trade restrictions on advanced process technology, has shifted focus to system-level optimization and design-based density improvements.

<details><summary>References</summary>
<ul>
<li><a href="https://www.21jingji.com/article/20260525/herald/1573642c437a5e4e76a15fc1c40f0a35.html">华为提出的“韬定律”是什么？跟摩尔定律有什么不同？ - 21经济网</a></li>
<li><a href="https://www.cnblogs.com/qiniushanghai/p/20166392">华为韬（τ）定律：用"时间缩微"重写半导体演进规则（2026） - 七牛云行业应用 - 博客园</a></li>
<li><a href="https://www.huxiu.com/article/4861142.html">华为发布"韬定律"半导体新理论 提出以时间缩微替代几何缩微</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#芯片`, `#华为`, `#摩尔定律`, `#算力`

---