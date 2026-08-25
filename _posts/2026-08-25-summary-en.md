---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 36 items, 16 important content pieces were selected

---

1. [Microsoft Paint and Photos Secretly Embed Invisible GUID Watermarks in AI-Edited Images](#item-1) ⭐️ 8.0/10
2. [Bartosz Ciechanowski&\#x27;s &\#x27;Moon&\#x27; \(2024\): An Interactive Exploration of the Moon](#item-2) ⭐️ 8.0/10
3. [San Francisco Recreated as an Interactive 3D City Sim in Your Browser](#item-3) ⭐️ 8.0/10
4. [Bart: A 2.82B Parameter LLM Trained on Pre-1931 English Text](#item-4) ⭐️ 8.0/10
5. [Apple Reverses Decision: iCloud+ Hide My Email Stays on icloud.com](#item-5) ⭐️ 7.0/10
6. [Xiaomi&\#x27;s ARM chip matches Apple single-core, faster multi-core](#item-6) ⭐️ 7.0/10
7. [EU packaging regulations debate: are they really killing micro-entrepreneurs?](#item-7) ⭐️ 7.0/10
8. [XMPP Celebrates 25 Years of Federated Messaging and Digital Independence](#item-8) ⭐️ 7.0/10
9. [IPFS Shipyard Maintainer Team Announces Winding Down, Project Continues](#item-9) ⭐️ 7.0/10
10. [seL4 Microkernel Achieves Full Security Proofs on AArch64](#item-10) ⭐️ 7.0/10
11. [Technique Creates Executable That Is Also a Valid SQLite Database](#item-11) ⭐️ 7.0/10
12. [Using LLMs as Spatial Software Generators for Programmable 3D Objects](#item-12) ⭐️ 7.0/10
13. [Delay-Corrected Bellman Operator and Causal Attribution for Constrained RL](#item-13) ⭐️ 7.0/10
14. [Chinese Internet Hoax Denies Existence of Tang Dynasty](#item-14) ⭐️ 6.0/10
15. [Anthropic&\#x27;s revenue hits $65bn but premium models lose user adoption](#item-15) ⭐️ 6.0/10
16. [Fable Model&\#x27;s High Cost Ends the Era of Constant AI Improvement at Same Price](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Microsoft Paint and Photos Secretly Embed Invisible GUID Watermarks in AI-Edited Images](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

Microsoft’s Paint and Photos apps now silently embed an invisible, non-removable watermark containing a unique GUID into any image that has been AI-manipulated, even when the AI processing is performed locally on the device, with no user notice or opt-out. This hidden identifier can be linked to the user&\#x27;s Microsoft account, potentially enabling de-anonymization through legal subpoenas and undermining user privacy and control over their own digital content. The invisible watermark is embedded directly into image pixels via a custom algorithm in Watermarker.dll, independent of the visible watermark toggle; the same GUID is also stored in C2PA metadata, so even if metadata is stripped, the pixel-based watermark remains.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: A GUID \(Globally Unique Identifier\) is a 128-bit number used to uniquely identify information in computer systems, often associated with specific accounts or sessions. C2PA \(Coalition for Content Provenance and Authenticity\) is an industry standard for attaching provenance metadata to digital content, adopted by Microsoft to label AI-generated images. The invisible watermarking technique goes beyond C2PA metadata by embedding the identifier into the image pixels, making it persistent even if the metadata is removed.

<details><summary>References</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs as Invisible ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community expressed shock and concern, viewing the secret embedding of unique identifiers as a serious privacy threat. Many noted that the AI aspect is a distraction; the real issue is the silent, non-removable identifier that can be tied to a Microsoft account, potentially enabling deanonymization through subpoenas. Some also pointed out Microsoft&\#x27;s sloppy implementations, with one user reporting the watermark triggering incorrectly.

**Tags**: `#privacy`, `#microsoft`, `#ai-watermarking`, `#digital-rights`, `#security`

---

<a id="item-2"></a>
## [Bartosz Ciechanowski&\#x27;s &\#x27;Moon&\#x27; \(2024\): An Interactive Exploration of the Moon](https://ciechanow.ski/moon/) ⭐️ 8.0/10

Bartosz Ciechanowski released a new interactive article titled &\#x27;Moon&\#x27; \(2024\), which uses web-based 3D visualizations and simulations to let readers explore the moon&\#x27;s orbit, phases, and libration through hands-on learning. This article showcases the power of explorable explanations, setting a new standard for web-based educational content by making complex astronomical concepts intuitive. It also influences the broader trend of AI-assisted interactive web development, as noted by the community. The article offers a comprehensive exploration of the Moon&\#x27;s orbit, phases, and libration, including a unique perspective from a virtual planet. It lacks a table of contents, a deliberate editorial choice that encourages immersive reading, according to the author&\#x27;s style.

hackernews · simonebrunozzi · Aug 24, 22:06 · [Discussion](https://news.ycombinator.com/item?id=49426466)

**Background**: Explorable explanations are interactive digital media that allow users to learn by manipulating simulations. Bartosz Ciechanowski is a renowned independent creator who publishes detailed, self-contained interactive articles on topics like physics, engineering, and astronomy, using web technologies such as Three.js. His work is widely praised for its clarity and depth, often compared to interactive museum exhibits.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Explorable_explanation">Explorable explanation</a></li>
<li><a href="https://ciechanow.ski/">Bartosz Ciechanowski</a></li>

</ul>
</details>

**Discussion**: The community discussion is overwhelmingly positive, with users praising the article&\#x27;s interactive depth and visual clarity. Some commenters note the absence of a table of contents, and one user raises a question about the ethics of using Ciechanowski&\#x27;s style in AI-generated personal learning tools. Others highlight how his work has influenced the broader adoption of interactive web pages, especially with AI-assisted development.

**Tags**: `#interactive-web`, `#education`, `#astronomy`, `#visualization`, `#web-development`

---

<a id="item-3"></a>
## [San Francisco Recreated as an Interactive 3D City Sim in Your Browser](https://sf.thijs.gg/) ⭐️ 8.0/10

A developer has turned the entire city of San Francisco into a web-based interactive simulation, using reverse-engineered 3D map data to create a driveable and explorable game-like experience with coin collection. This demo highlights the creative potential of repurposing real-world geospatial data for immersive experiences, bridging the gap between digital twins and gaming, and has resonated emotionally with former residents. The simulation runs entirely in the browser, likely built from 3D tiles extracted via reverse-engineering of Apple Maps data \(similar to the retroplasma approach\), and currently supports vehicle driving and coin collection without deeper game mechanics.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Background**: Modern 3D city models are often created from aerial imagery and LIDAR scans, then streamed efficiently using standards like 3D Tiles. Web-based renderers such as CesiumJS can display these massive datasets, and hobbyists have reverse-engineered proprietary map data from services like Apple Maps to build interactive urban simulations. This project builds on that community effort to make a real city explorable as a lightweight game.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ogc.org/standards/3dtiles/">3D Tiles Standard – Streaming Massive 3D Geospatial Data</a></li>
<li><a href="https://cesium.com/learn/cesiumjs-learn/cesiumjs-interactive-building/">Visualize a Proposed Building in a 3D City – Cesium</a></li>

</ul>
</details>

**Discussion**: Commenters praised the technical achievement and expressed nostalgia, with one former SF resident saying it made them emotional. Many requested features like street names, address teleporting, and a higher-resolution local version, while others noted the reverse-engineering origins and shared a similar Seattle project in N64 style.

**Tags**: `#3D-graphics`, `#game-development`, `#mapping`, `#san-francisco`, `#web-technologies`

---

<a id="item-4"></a>
## [Bart: A 2.82B Parameter LLM Trained on Pre-1931 English Text](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 8.0/10

Unbounded Labs built Bart, a 2.82B parameter LLM trained from scratch on 20.1B tokens of pre-1931 English text, achieving state-of-the-art vintage language model performance on their custom Vintage CORE benchmark suite. This project investigates whether LLMs can replicate historical scientific reasoning, addressing the core AI question of whether models can generate original ideas or merely parrot training data; it also demonstrates that domain-specific model training on curated datasets can yield competitive results with limited resources. The model was trained in 5 days on a single H100 GPU with 60% MFU, and the team open-sourced the largest vintage SFT dataset \(416k graded Q&amp;A pairs\), cleaned Harvard&\#x27;s Institutional Books from 242B to 23B tokens, and created Vintage CORE, a suite of 20 benchmarks for vintage models.

reddit · r/MachineLearning · /u/soggydoggy8 · Aug 24, 17:20

**Background**: An ablation study in machine learning involves removing components to assess their contribution to performance. Supervised fine-tuning \(SFT\) is a post-training alignment step where a model is further trained on labeled examples to improve task-specific behavior. Corpus curation is the process of carefully selecting and cleaning a text dataset to ensure quality and relevance for training language models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ablation_%28artificial_intelligence%29">Ablation (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://cameronrwolfe.substack.com/p/understanding-and-using-supervised">Understanding and Using Supervised Fine - Tuning ( SFT ) for...</a></li>

</ul>
</details>

**Tags**: `#vintage-llm`, `#training-from-scratch`, `#corpus-curation`, `#machine-learning`, `#natural-language-processing`

---

<a id="item-5"></a>
## [Apple Reverses Decision: iCloud+ Hide My Email Stays on icloud.com](https://developer.apple.com/news/?id=1ptvdtcm) ⭐️ 7.0/10

Apple has reversed its earlier plan to move iCloud+ Hide My Email addresses to a separate private.icloud.com domain, and will now keep them on the main icloud.com domain. This change comes after user backlash in June when the company announced the domain unification. Keeping Hide My Email addresses on icloud.com makes them indistinguishable from regular iCloud addresses, preventing websites from blocklisting them as disposable or temporary emails. This preserves the privacy feature&\#x27;s usability for millions of users and reduces the risk of lock-in criticism. Apple&\#x27;s original plan would have generated new addresses under private.icloud.com, making them easy to detect and block. The reversal keeps all addresses in the same format as regular icloud.com emails, a direct response to community feedback and the practical need to avoid anti-spam filters.

hackernews · K7PJP · Aug 24, 22:13 · [Discussion](https://news.ycombinator.com/item?id=49426564)

**Background**: Hide My Email is an iCloud+ privacy feature that creates random, unique email addresses forwarding to a user&\#x27;s real inbox, protecting their real email when signing up for services. Many online platforms block disposable or temporary email addresses to fight abuse, and if private relay addresses use a distinct domain, they can be flagged and blocked. By staying on the same domain as legitimate iCloud accounts, these addresses blend in seamlessly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mactech.com/2026/08/24/apple-wont-change-the-email-domain-used-for-the-icloud-hide-my-email-feature/">Apple WON’T change the email domain used for the iCloud+ Hide ...</a></li>
<li><a href="https://support.apple.com/guide/icloud/set-up-hide-my-email-mm9d9012c9e8/icloud">Set up and use Hide My Email in iCloud+ on all your devices</a></li>

</ul>
</details>

**Discussion**: The community reaction is largely positive, with users glad Apple listened. Many note that this prevents blocking and that only Fastmail offers a similar approach. Some criticize Apple&\#x27;s &\#x27;lock-in&\#x27; strategy, but acknowledge it&\#x27;s necessary for the feature to work effectively.

**Tags**: `#privacy`, `#email`, `#Apple`, `#iCloud`, `#security`

---

<a id="item-6"></a>
## [Xiaomi&\#x27;s ARM chip matches Apple single-core, faster multi-core](https://twitter.com/lemire/status/2091894299289874926) ⭐️ 7.0/10

Xiaomi&\#x27;s new Xring O3 processor, an ARM Cortex design, reportedly achieves Geekbench single-core scores matching Apple&\#x27;s M5 iPad and higher multi-core scores in AnTuTu, owing to its 10-core configuration. This signals that Xiaomi, as the third-largest smartphone maker, can now produce competitive in-house chips, potentially reducing reliance on Qualcomm and MediaTek and intensifying mobile SoC competition. The chip is an ARM Cortex design, not a custom core, with a 10-core CPU \(vs. Apple&\#x27;s 6-core\), fabricated on TSMC 3nm, and includes an in-house NPU and LPDDR6 support; real-world efficiency and per-watt performance remain unverified.

hackernews · tosh · Aug 24, 15:08 · [Discussion](https://news.ycombinator.com/item?id=49420873)

**Background**: Single-threaded performance measures how fast a CPU completes one task, crucial for app responsiveness. Multi-threaded performance handles multiple tasks simultaneously, benefiting from more cores. ARM reference designs are pre-built CPU blueprints licensed by Arm, letting companies configure core counts without custom core design. Apple uses a custom ARM architecture.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Single_threaded_performance">Single threaded performance</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multithreading_%28computer_architecture%29">Multithreading (computer architecture) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ARM_architecture_family">ARM architecture family - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community notes the chip is essentially an ARM reference design, not a custom core, and the multi-threaded lead is largely due to more cores. Doubts are raised about real-world efficiency and power consumption, with some pointing out Apple&\#x27;s last-gen chip still leads in per-watt single-core performance. Others see Xiaomi&\#x27;s move as a threat to Qualcomm and MediaTek.

**Tags**: `#mobile processors`, `#ARM`, `#Xiaomi`, `#Apple Silicon`, `#chip design`

---

<a id="item-7"></a>
## [EU packaging regulations debate: are they really killing micro-entrepreneurs?](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) ⭐️ 7.0/10

An article claimed that EU packaging rules, particularly the PPWR, impose excessive burdens on small electronics makers, but community members quickly pointed out that official EU guidance exempts micro-enterprises and non-branded packaging. The debate highlights the real tension between regulation and small-scale innovation, and shows how misinterpretation of complex laws can fuel unnecessary panic among makers and entrepreneurs. The EU&\#x27;s FAQ on packaging rules states that obligations do not apply to micro-enterprises or to packaging that is not branded; the original article may have misunderstood the scope. The European Commission is also working on a correction to centralize registration, after member states blocked a single registry.

hackernews · l-one-lone · Aug 24, 13:05 · [Discussion](https://news.ycombinator.com/item?id=49419237)

**Background**: The Packaging and Packaging Waste Regulation \(PPWR\) is an EU law aimed at reducing packaging waste and promoting recycling. Micro-enterprises are defined as businesses with fewer than 10 employees and a turnover below €2 million. The regulation&\#x27;s implementation varies across EU member states, leading to a fragmented compliance landscape that can confuse small businesses.

**Discussion**: Commenters generally agreed the article overstated the problem, with one providing the official EU FAQ that clarifies the exemption. Others noted that the real issue is the federated nature of EU law implementation, where member states create divergent rules, and that China&\#x27;s approach of regulating through major platforms may offer a simpler model. A few pointed out that the EU Commission itself wanted a centralized system but was blocked by member states.

**Tags**: `#EU regulations`, `#entrepreneurship`, `#hardware`, `#compliance`, `#policy`

---

<a id="item-8"></a>
## [XMPP Celebrates 25 Years of Federated Messaging and Digital Independence](https://gultsch.de/posts/25-years-of-digital-independence/) ⭐️ 7.0/10

The article offers a retrospective on XMPP&\#x27;s 25-year history as a pioneering open federated messaging protocol, reflecting on its resilience and ongoing development. XMPP&\#x27;s longevity underscores the value of decentralized, standards-based communication in an era of walled gardens, serving as a model for digital sovereignty and interoperability. Projects like Movim, Fluux, and jmp.chat extend XMPP&\#x27;s utility, while community debates contrast its lean, extensible design with Matrix&\#x27;s approach.

hackernews · inputmice · Aug 24, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49421536)

**Background**: XMPP \(formerly Jabber\) is an open, XML-based protocol for instant messaging, presence, and more, using a federated architecture similar to email where anyone can run a server. It was formalized as an IETF standard in 2004 and once powered major platforms like Google Talk and Facebook Chat. Matrix is a newer federated protocol with a different technical stack, often seen as a competitor.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XMPP_protocol">XMPP protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/Matrix_%28protocol%29">Matrix (protocol)</a></li>

</ul>
</details>

**Discussion**: Comments express nostalgia for XMPP&\#x27;s heyday, practical use cases like telephony bridges and agent communication, and a debate over whether Matrix&\#x27;s funding was wasted; some users lament XMPP&\#x27;s diminished visibility, while others actively use it and advocate for its potential.

**Tags**: `#XMPP`, `#federated messaging`, `#protocol history`, `#digital sovereignty`, `#Matrix`

---

<a id="item-9"></a>
## [IPFS Shipyard Maintainer Team Announces Winding Down, Project Continues](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 7.0/10

IPFS Shipyard, one of the maintainer teams of the InterPlanetary File System, has announced it will wind down its support. The broader IPFS project will continue by transitioning to individual maintainer grants. This shift signals a move from centralized team maintenance to a decentralized grant model, which could affect the protocol&\#x27;s development pace and community confidence. It also reflects ongoing challenges in sustaining open-source decentralized infrastructure. The announcement specifically concerns the Shipyard team, not the entire IPFS project; prior to this, Cloudflare had already discontinued IPFS support. The project will now rely on individual grants to fund maintenance.

hackernews · iand · Aug 24, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49421489)

**Background**: IPFS is a decentralized peer-to-peer file sharing protocol that uses content addressing instead of location-based URLs, similar to BitTorrent. It is maintained by multiple teams and individual contributors. Shipyard was one of the organized maintainer teams supporting IPFS implementations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IPFS">IPFS</a></li>

</ul>
</details>

**Discussion**: Community members clarified that the announcement is not about IPFS shutting down, only Shipyard winding down. Some expressed sadness and suggested alternatives like Iroh, while others pointed out the irony of using a Google Form for feedback in a decentralized project.

**Tags**: `#IPFS`, `#decentralized web`, `#open source`, `#maintainers`, `#community`

---

<a id="item-10"></a>
## [seL4 Microkernel Achieves Full Security Proofs on AArch64](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 7.0/10

The seL4 microkernel has achieved complete formal security proofs for the AArch64 \(ARM 64-bit\) architecture, marking a major milestone in the project&\#x27;s formal verification journey. However, the proofs currently cover only unicore and non-MCS configurations, leaving out multicore and mixed-criticality support. This achievement extends the mathematical guarantees of seL4&\#x27;s security to one of the most widely used processor architectures, bolstering trust for safety-critical and security-sensitive systems in embedded, automotive, and military domains. It demonstrates that the kernel&\#x27;s implementation is provably free of certain classes of bugs, though the limitations highlight that real-world deployments with multicore and mixed-criticality features still lack formal assurance. The proofs are for the non-MCS, unicore configuration of seL4 on AArch64, meaning they do not cover mixed-criticality scheduling or multicore concurrency, which are important for many real-world applications. Community members also note that side-channel attacks like timing leaks are not within the scope of these functional correctness proofs.

hackernews · snvzz · Aug 24, 11:32 · [Discussion](https://news.ycombinator.com/item?id=49418255)

**Background**: seL4 is a formally verified microkernel with a capability-based security model, meaning its C implementation has been mathematically proven to follow an abstract specification free of certain bugs. AArch64 is the 64-bit execution state of the ARM architecture, used in most modern smartphones, servers, and embedded devices. Mixed-Criticality Systems \(MCS\) allow tasks of different safety levels to share the same hardware with temporal isolation, a feature that seL4 supports in its MCS configuration but is not yet verified. Formal verification at the binary level ensures that the compiled machine code matches the verified source, providing end-to-end assurance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/L4_microkernel_family">L 4 microkernel family - Wikipedia</a></li>
<li><a href="https://sel4.systems/">The seL 4 Microkernel | seL 4</a></li>
<li><a href="https://sel4.systems/About/seL4-whitepaper.pdf">The seL4® Foundation https://sel4.systems/Foundation The seL4 Microkernel</a></li>

</ul>
</details>

**Discussion**: Community reaction is mixed: some express skepticism that side-channel timing attacks could undermine the proofs, while others point out the limitations of unicore and non-MCS scope. There is interest in real-world deployments \(e.g., GenodeOS, LionsOS, automotive hypervisors\) but also criticism that a native Linux integration is needed to truly improve system security. The sentiment reflects cautious optimism about the milestone, tempered by awareness of remaining gaps.

**Tags**: `#formal verification`, `#seL4`, `#operating systems`, `#security`, `#ARM`

---

<a id="item-11"></a>
## [Technique Creates Executable That Is Also a Valid SQLite Database](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria demonstrated a technique to create a file that is both a valid ELF executable and a valid SQLite database, by embedding the executable&\#x27;s components into SQLite tables and using a custom interpreter with binfmt\_misc. This clever combination of file formats and kernel features highlights the flexibility of Linux systems, potentially inspiring novel approaches to software packaging, distribution, or polyglot file design. The technique sets the SQLite application ID at byte offset 68 to &\#x27;SELF&\#x27;, stores ELF components in multiple SQLite tables per a defined schema, and uses a custom C interpreter \(self-exec\) along with binfmt\_misc registration to directly execute such files.

rss · Simon Willison · Aug 24, 11:38

**Background**: ELF \(Executable and Linkable Format\) is the standard binary format for executables and shared libraries on Linux. SQLite is a library that implements a self-contained, serverless, zero-configuration SQL database engine, storing the entire database as a single file. binfmt\_misc is a Linux kernel feature that allows arbitrary executable file formats to be recognized and passed to user-space applications, enabling non-native binaries to be executed transparently.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Binfmt_misc">Binfmt misc</a></li>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#elf`, `#linux`, `#executable`, `#binfmt\_misc`

---

<a id="item-12"></a>
## [Using LLMs as Spatial Software Generators for Programmable 3D Objects](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 7.0/10

A new research paper demonstrates that large language models \(LLMs\) can act as spatial software generators, producing 3D objects that are inherently structured, animation-ready, and programmable, unlike traditional monolithic mesh generation. This approach could transform industries such as game development, industrial design, and AR/VR by enabling 3D objects that are more flexible, editable, and adaptive, potentially reducing the need for manual rigging and programming. The generated 3D objects are composed of logical parts with hinge/socket articulation, and can include logic to adjust appearance based on device capabilities. They currently lag behind traditional methods in creating complex organic shapes.

reddit · r/MachineLearning · /u/mhb\_11 · Aug 24, 19:10

**Background**: Traditional AI 3D generators produce monolithic meshes—single, unstructured blobs that are difficult to edit or animate. Spatial programming, in contrast, represents 3D objects as software with hierarchical structures, logic, and articulation, making them more interactive. The researchers treat 3D generation as a coding task, leveraging LLMs&\#x27; coding abilities to generate spatial programs that describe 3D objects.

<details><summary>References</summary>
<ul>
<li><a href="https://spatialtoolbox.vuforia.com/docs/use/spatial-programming">Spatial Programming | Vuforia Spatial Toolbox</a></li>
<li><a href="https://cubepar.org/">Try CubePart Demo &amp; Generate Part... — CubePar | AI 3D Mesh Guide</a></li>

</ul>
</details>

**Tags**: `#3D generation`, `#spatial programming`, `#LLM`, `#procedural generation`, `#AI research`

---

<a id="item-13"></a>
## [Delay-Corrected Bellman Operator and Causal Attribution for Constrained RL](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 7.0/10

Researchers proposed a delay-corrected Bellman operator that adjusts the effective discount factor based on the consequence-delay distribution, along with an Interventional Consequence Net \(ICN\) for causal action attribution in constrained RL. The contraction proof holds under unknown stochastic delays, but the ICN requires access to the environment&\#x27;s structural causal model for pretraining. This work addresses the critical challenge of delayed and stochastic consequences in constrained RL, which is common in real-world applications like autonomous driving and healthcare. It paves the way for more reliable credit assignment and safer exploration. The delay-corrected Bellman operator learns an adaptive effective discount from the delay distribution, and the ICN estimates marginal causal contribution per action, not just temporal proximity. The main limitation is that the ICN relies on a known structural causal model, hindering end-to-end learning from data alone.

reddit · r/MachineLearning · /u/No\_Cauliflower7923 · Aug 24, 12:11

**Background**: The Bellman equation is a fundamental recursive decomposition in dynamic programming and reinforcement learning, used to compute optimal value functions. The Bellman operator applies this equation to update value estimates. In constrained RL, an agent must maximize reward while satisfying safety constraints, but delayed and stochastic consequences make it hard to assign credit to the correct action, often causing the most recent action to be wrongly penalized.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bellman_equation">Bellman equation - Wikipedia</a></li>
<li><a href="https://www.baeldung.com/cs/bellman-operator-reinforcement-learning">What Is the Bellman Operator in Reinforcement Learning? | Baeldung on Computer Science</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#causal inference`, `#constrained RL`, `#credit assignment`, `#delayed consequences`

---

<a id="item-14"></a>
## [Chinese Internet Hoax Denies Existence of Tang Dynasty](https://www.cnn.com/2026/08/19/style/china-tang-dynasty-never-existed-hoax-intl-hnk) ⭐️ 6.0/10

CNN reports on a fringe online conspiracy theory within China that claims the Tang Dynasty \(618–907 AD\) was a fabrication, sparking fresh debate over historical denialism. This phenomenon illustrates how conspiracy theories can erode public trust in established scholarship, reflecting a broader global trend of narrative warfare where historical facts are replaced by ideological fictions. The hoax ignores extensive primary sources, including the Old Book of Tang, the Qianling Mausoleum, and contemporary Japanese records, and it closely mirrors the Western phantom time conspiracy theory that also targets a similar historical period.

hackernews · related · Aug 24, 21:03 · [Discussion](https://news.ycombinator.com/item?id=49425819)

**Background**: The Tang Dynasty is widely regarded as a golden age of Chinese civilization, renowned for its poetry, trade along the Silk Road, and cultural influence. Its existence is documented by numerous Chinese annals, archaeological sites, and foreign accounts from Japan, Korea, and the Islamic world. The phantom time hypothesis is a fringe idea that the early Middle Ages were fabricated by the Holy Roman Empire, similar in its denial of well-attested historical periods.

**Discussion**: Commenters overwhelmingly reject the hoax, citing abundant archaeological and textual evidence. Some draw parallels to the phantom time conspiracy theory and note a possible racist motive, while others lament the rise of narrative warfare in public discourse.

**Tags**: `#history`, `#conspiracy`, `#china`, `#internet-culture`, `#denialism`

---

<a id="item-15"></a>
## [Anthropic&\#x27;s revenue hits $65bn but premium models lose user adoption](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 6.0/10

Anthropic&\#x27;s annualized revenue reached $65 billion in July, up from $47 billion in May, while OpenAI&\#x27;s revenue surged to over $40 billion after the launch of GPT-5.6. Ramp billing data shows that Anthropic&\#x27;s expensive Fable 5 model accounts for only 8% of its model spend, far behind cheaper options like Opus 4.8 at 28%. This highlights a growing trend where cost-effectiveness drives AI model adoption more than raw capability, potentially reshaping pricing strategies and market competition among AI providers. Anthropic expects Q3 profitability and has 6,000 customers spending over $100,000 annually; the Ramp AI Index, based on data from 70,000 companies, reveals that even among Anthropic&\#x27;s own models, cheaper ones dominate usage.

rss · Simon Willison · Aug 23, 20:24

**Background**: Anthropic is a major AI company known for its Claude family of models; OpenAI is its main rival, creator of GPT models. The Ramp AI Index tracks corporate spending on AI services using credit card transaction data, and GPT-5.6 was OpenAI&\#x27;s latest release in July 2026 with multiple tiers.

<details><summary>References</summary>
<ul>
<li><a href="https://ramp.com/data/ai-index">Ramp AI Index</a></li>
<li><a href="https://ramp.com/data/ai-index-august-2026">August 2026 Ramp AI Index: Cracks in the AI thesis</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>

</ul>
</details>

**Tags**: `#AI`, `#business`, `#Anthropic`, `#OpenAI`, `#revenue`

---

<a id="item-16"></a>
## [Fable Model&\#x27;s High Cost Ends the Era of Constant AI Improvement at Same Price](https://simonwillison.net/2026/Aug/23/drew-breunig/) ⭐️ 6.0/10

Drew Breunig observes that Anthropic&\#x27;s Fable model, while incredibly capable, is so expensive that it breaks the trend of each new model being cheaper or equal in cost. This forces developers to abandon the old assumption that a new model would always paper over problems and instead start thinking strategically about which model to use for which task. This shift marks the end of the &\#x27;free lunch&\#x27; in AI, where developers could rely on constant model improvements at the same price. It now compels them to manage cost-performance trade-offs explicitly, changing how AI-powered software is built and operated. Breunig&\#x27;s quote mentions that models like Opus, 5.6, K3, and GLM are &\#x27;good enough&\#x27; for most coding tasks, making Fable&\#x27;s high cost hard to justify for routine work. Fable 5, released in June 2026, is Anthropic&\#x27;s most capable widely available model, targeting demanding reasoning and agentic tasks, but its expense forces a new routing strategy.

rss · Simon Willison · Aug 23, 19:55

**Background**: For years, each new generation of large language models \(like those from OpenAI and Anthropic\) delivered better performance at the same or lower cost. This created a &\#x27;free lunch&\#x27; mentality where developers didn&\#x27;t need to optimize their tooling. Anthropic&\#x27;s Claude models include Opus \(high-end\) and later Fable, a Mythos-class model. GLM is an open-weight Chinese model series from Z.ai, also competitive. The quote was shared by Simon Willison, a prominent developer and commentator on AI.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_%28AI%29">GLM (AI) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#language models`, `#Anthropic`, `#Claude`, `#economics`

---