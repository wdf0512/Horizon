---
layout: default
title: "Horizon Summary: 2026-08-25 (EN)"
date: 2026-08-25
lang: en
---

> From 34 items, 14 important content pieces were selected

---

1. [Microsoft Paint and Photos embed invisible user-specific watermarks in AI-edited images](#item-1) ⭐️ 8.0/10
2. [San Francisco Transformed into an Interactive 3D Video Game](#item-2) ⭐️ 8.0/10
3. [EU Packaging Waste Rules Spark Debate Over Burden on Makers](#item-3) ⭐️ 8.0/10
4. [Claude Fable&\#x27;s High Cost Ends the &\#x27;Free Lunch&\#x27; Era of AI Model Improvements](#item-4) ⭐️ 8.0/10
5. [AI Generates Programmable 3D Objects via Spatial Programming](#item-5) ⭐️ 8.0/10
6. [Xiaomi ARM CPU Claims Apple-Like Single-Core, Faster Multi-Core](#item-6) ⭐️ 7.0/10
7. [XMPP Marks 25 Years of Digital Independence in Messaging](#item-7) ⭐️ 7.0/10
8. [IPFS Maintainer Shipyard Winding Down Centralized Support](#item-8) ⭐️ 7.0/10
9. [Your executable is a SQLite database](#item-9) ⭐️ 7.0/10
10. [AAAI 2027 Organizers Acknowledge Reviewer Collusion via 2-Cycles](#item-10) ⭐️ 7.0/10
11. [CCPL: Delay-Corrected Bellman Operator and Causal Attribution for Constrained RL](#item-11) ⭐️ 7.0/10
12. [Apple Confirms iCloud+ Hide My Email Addresses Stay on icloud.com](#item-12) ⭐️ 6.0/10
13. [Fringe Chinese Internet Movement Denies Tang Dynasty Existed](#item-13) ⭐️ 6.0/10
14. [Unbounded Labs Open-Sources Bart, a 2.82B Vintage LLM Trained on Pre-1931 Texts](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Microsoft Paint and Photos embed invisible user-specific watermarks in AI-edited images](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

Microsoft Paint and Photos have been found to silently add an invisible, user-specific watermark \(a GUID\) to images edited with AI features, even when the AI processing is performed locally on the device. This hidden watermarking, which cannot be disabled by the user, can be used to trace images back to the creator&\#x27;s Microsoft account, undermining anonymity and raising serious privacy concerns, especially for sensitive or political content. The watermark is a Globally Unique Identifier \(GUID\) embedded in the image metadata or pixel data, and it is applied even when using local AI models like Stable Diffusion for image generation or editing. It is unclear whether non-AI edits also include the watermark.

hackernews · ComputerGuru · Aug 24, 15:28 · [Discussion](https://news.ycombinator.com/item?id=49421158)

**Background**: Invisible digital watermarking is a technique to embed information into media without perceptible alteration, used for authentication and provenance tracking. AI-generated content is increasingly watermarked to distinguish synthetic media. Microsoft&\#x27;s approach uses a GUID tied to the user&\#x27;s account, similar to digital fingerprinting, which can identify the creator if the image is shared publicly.

<details><summary>References</summary>
<ul>
<li><a href="https://www.imatag.com/digital-watermarking">Invisible Digital Watermarking | The smart way to protect your online content</a></li>
<li><a href="https://huggingface.co/blog/watermarking">AI Watermarking 101: Tools and Techniques</a></li>

</ul>
</details>

**Discussion**: The community is broadly concerned about privacy and anonymity. Comments note that the invisible watermark is a &\#x27;weapon against internet anonymity&\#x27; because it can be subpoenaed to reveal the user&\#x27;s identity. Some argue the AI aspect is a red herring, and the real issue is the secret embedding of identifiers. Others recall Microsoft&\#x27;s past sloppy watermark implementations in other tools, and advise against using Paint or any other AI-enabled Microsoft apps.

**Tags**: `#privacy`, `#watermarking`, `#microsoft`, `#reverse-engineering`, `#ai-ethics`

---

<a id="item-2"></a>
## [San Francisco Transformed into an Interactive 3D Video Game](https://sf.thijs.gg/) ⭐️ 8.0/10

A developer released an interactive 3D demo that turns the entire city of San Francisco into a video game-like experience, using real-world map data to render streets, buildings, and terrain. Users can drive around and collect coins, and the project has sparked enthusiastic community engagement. It showcases the potential of combining open geographic data with game engines to create immersive urban simulations, which could inspire applications in gaming, urban planning, or virtual tourism. It also demonstrates the accessibility of such technology, prompting discussions about MMO and GTA-like experiences. The demo is web-based, likely using WebGL and data from OpenStreetMap, with real-time rendering of elevation and buildings. Comments note a collision bug under certain walkways, and while cars can be driven, it remains a tech demo rather than a full game.

hackernews · centrosphere · Aug 24, 17:05 · [Discussion](https://news.ycombinator.com/item?id=49422784)

**Background**: The project leverages open geospatial data \(like OpenStreetMap\) and 3D rendering techniques to create a game-like environment. Technologies such as WebGL enable browser-based 3D graphics. The developer generated 3D meshes for buildings, roads, and terrain from map data, and added simple game mechanics like coin collection. This taps into the trend of &\#x27;digital twins&\#x27; and using real-world data in entertainment.

**Discussion**: Comments are overwhelmingly positive, with excitement about a potential high-resolution offline version, multiplayer mode, and integration with Google Street View. Some expressed nostalgia and emotional connection to the virtual SF. Others discussed technical improvements like adding landmarks and generating GTA-style maps, while a minor collision bug was noted.

**Tags**: `#3D rendering`, `#game development`, `#map data`, `#San Francisco`, `#urban simulation`

---

<a id="item-3"></a>
## [EU Packaging Waste Rules Spark Debate Over Burden on Makers](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) ⭐️ 8.0/10

An article on Lectronz argues that the EU&\#x27;s Packaging and Packaging Waste Regulation imposes excessive compliance costs on micro-entrepreneurs and small hardware makers, potentially stifling innovation. The piece has ignited a heated discussion, with community members pointing out exemptions for micro-enterprises and criticizing the article&\#x27;s interpretation. The debate highlights the tension between environmental regulation and the viability of small-scale entrepreneurship. If the rules are perceived as too burdensome, they could drive away independent makers and startups, weakening Europe&\#x27;s innovation ecosystem and pushing activity toward regions with more centralized or lenient approaches. The EU&\#x27;s FAQ clarifies that micro-enterprises using generic packaging are exempt from many requirements, and the European Commission now advises member states not to enforce the rules until a correction is enacted. The real problem, according to commenters, is the fragmented implementation by 20+ member states, each adopting their own version of the law, rather than the EU regulation itself.

hackernews · l-one-lone · Aug 24, 13:05 · [Discussion](https://news.ycombinator.com/item?id=49419237)

**Background**: The EU Packaging and Packaging Waste Regulation aims to reduce packaging waste and promote a circular economy. It requires producers to register, report data, and pay fees for packaging placed on the market. The maker community, consisting of small hardware startups and individual creators, often ships in small volumes and may lack the resources to navigate complex compliance processes originally designed for large corporations.

**Discussion**: Commenters largely agree that the article overstates the impact, noting that micro-enterprises are exempt and that the European Commission is working on a fix. They highlight the real pain point: the fragmented national implementations, which create a costly patchwork for small businesses. Comparisons are drawn to China&\#x27;s centralized approach, where a single system handles compliance for all platforms, and some express frustration that EU member states sabotage harmonization efforts.

**Tags**: `#EU regulations`, `#entrepreneurship`, `#small business`, `#maker community`, `#policy`

---

<a id="item-4"></a>
## [Claude Fable&\#x27;s High Cost Ends the &\#x27;Free Lunch&\#x27; Era of AI Model Improvements](https://simonwillison.net/2026/Aug/23/drew-breunig/) ⭐️ 8.0/10

The release of Anthropic&\#x27;s Claude Fable, a powerful but costly model, has ended the trend where each new AI model improved performance at the same or lower price. Developers must now decide which coding tasks justify the expense of top-tier models versus cheaper alternatives. This signals a major shift for AI-assisted coding: the era of automatic, cost-free improvements is over. Organizations must now strategically allocate work to different models based on cost-capability tradeoffs, impacting productivity and budgets. Claude Fable excels at frontier coding and reasoning, but Drew Breunig specifically cites Opus, K3, and the open-weight GLM model from Zhipu AI as &\#x27;good enough&\#x27; for most tasks, with Fable&\#x27;s high cost only justified for the hardest problems.

rss · Simon Willison · Aug 23, 19:55

**Background**: The AI industry long saw a pattern where each new model improved performance without increasing cost, leading developers to assume upgrades were always beneficial. Anthropic&\#x27;s Claude Opus family has been a top-tier set of models, and the new Claude Fable is a breakthrough in coding capability but at a premium price. GLM is a series of open-weight models from Chinese company Zhipu AI, offering affordable alternatives for many tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://overchat.ai/models/claude/claude-opus-5">Claude Opus 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_%28AI%29">GLM (AI) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#ai`, `#llm`, `#claude`, `#coding`, `#cost-optimization`

---

<a id="item-5"></a>
## [AI Generates Programmable 3D Objects via Spatial Programming](https://www.reddit.com/r/MachineLearning/comments/1vxcc1h/r_using_ai_as_a_spatial_software_generator_to/) ⭐️ 8.0/10

This paper introduces a method where large language models generate 3D objects as structured, parametric code instead of fixed polygon meshes, creating assets that are inherently hierarchical, articulable, and adaptable from the moment of creation. This approach could revolutionize game development, simulation, AR/VR, and industrial design by enabling objects that are immediately editable, animation-ready, and able to automatically adjust detail levels for different computing environments, drastically reducing manual post-processing. The generated code objects lag behind mesh-based AI generators in producing complex organic shapes, but they excel in structural logic and programmability. The paper, titled &\#x27;Code-native generation of highly programmable 3D assets,&\#x27; includes a live demo at nova3d.xyz and a GitHub repository.

reddit · r/MachineLearning · /u/mhb\_11 · Aug 24, 19:10

**Background**: Traditional AI 3D generators produce mesh models—opaque collections of polygons—that are difficult to edit or animate. Spatial programming uses code to define 3D geometry with parameters, logic, and relationships, making objects inspectable, measurable, and modifiable. As LLMs become more proficient at generating code, they can now produce 3D assets that are essentially software, unlocking capabilities that static meshes cannot offer.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/papers/2607.22738">Paper page - Nova 3 D : Code-Native Generation of Programmable ...</a></li>
<li><a href="https://therevision.co/articles/researchers-generate-3d-assets-as-editable-code-not-meshes">Researchers Generate 3 D Assets as Editable Code... | The Revision</a></li>

</ul>
</details>

**Tags**: `#3D Generation`, `#Spatial Programming`, `#LLMs`, `#Programmable Assets`, `#Neural 3D Synthesis`

---

<a id="item-6"></a>
## [Xiaomi ARM CPU Claims Apple-Like Single-Core, Faster Multi-Core](https://twitter.com/lemire/status/2091894299289874926) ⭐️ 7.0/10

Xiaomi announced its XRing O3 chip, an ARM-based processor that achieves a Geekbench single-core score of 3945, comparable to Apple&\#x27;s M5, and a multi-core score of 15221, surpassing Apple&\#x27;s M5 iPad by leveraging 10 cores against 6. This marks Xiaomi&\#x27;s increasing capability in chip design, threatening MediaTek and Qualcomm as the world&\#x27;s third-largest smartphone maker could reduce its reliance on third-party processors and reshape the mobile chip market. The chip is built on ARM&\#x27;s Cortex C1-Ultra design, identical to the one in MediaTek&\#x27;s Dimensity 9500, but with Xiaomi&\#x27;s custom interconnects, TSMC 3nm process, in-house NPU, and LPDDR6 support. Real-world phone performance may be lower due to thermal constraints, and power efficiency remains unverified.

hackernews · tosh · Aug 24, 15:08 · [Discussion](https://news.ycombinator.com/item?id=49420873)

**Background**: ARM Holdings licenses its processor designs to chipmakers. Apple uses an architecture license to build custom cores, while most others like MediaTek and Xiaomi use ARM&\#x27;s pre-designed Cortex cores. Single-threaded performance is critical for smartphone responsiveness, and Geekbench is a common benchmark.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ARM_Cortex">ARM Cortex</a></li>
<li><a href="https://en.wikipedia.org/wiki/Single_threaded_performance">Single threaded performance</a></li>

</ul>
</details>

**Discussion**: Commenters note that Xiaomi did not design the CPU core itself—it&\#x27;s a standard ARM design—and the multi-threaded lead comes from having more cores. Power efficiency is the missing metric, and some view this as a threat to MediaTek and Qualcomm, while others say it still falls short of Apple&\#x27;s custom silicon.

**Tags**: `#hardware`, `#ARM`, `#mobile-processors`, `#Xiaomi`, `#Apple`

---

<a id="item-7"></a>
## [XMPP Marks 25 Years of Digital Independence in Messaging](https://gultsch.de/posts/25-years-of-digital-independence/) ⭐️ 7.0/10

A retrospective article marks the 25th anniversary of the XMPP protocol, highlighting its sustained role in decentralized messaging and sparking a community discussion on its resilience and future potential. As centralized messaging platforms dominate, XMPP&\#x27;s federated architecture and open standard remain a critical alternative for digital sovereignty, and the ongoing community engagement demonstrates its enduring relevance. The article references modern XMPP projects like Movim and Fluux, phone bridges such as jmp.chat, and community ideas for serverless peer-to-peer communication using Iroh networking.

hackernews · inputmice · Aug 24, 15:51 · [Discussion](https://news.ycombinator.com/item?id=49421536)

**Background**: XMPP \(originally Jabber\) is an open, XML-based protocol for instant messaging and presence. It uses a federated model similar to email, allowing anyone to run their own server and interoperate globally. It was standardized by the IETF in 2004 and was once widely used by Google and Facebook, with numerous clients and servers still actively maintained today.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/XMPP_protocol">XMPP protocol</a></li>
<li><a href="https://xmpp.org/about/technology-overview/">An Overview of XMPP | XMPP - The universal messaging standard</a></li>

</ul>
</details>

**Discussion**: The community response is overwhelmingly positive, nostalgic, and forward-looking. Users expressed regret that Matrix did not build upon XMPP, shared practical use cases like AI agent communication and self-hosted phone bridges, and proposed innovative ideas for removing server dependencies using decentralized networking.

**Tags**: `#xmpp`, `#decentralization`, `#open-protocols`, `#messaging`, `#retrospective`

---

<a id="item-8"></a>
## [IPFS Maintainer Shipyard Winding Down Centralized Support](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 7.0/10

Shipyard, a key maintainer of IPFS implementations, announced it will cease contributions to upstream projects like go-libp2p and js-libp2p, as well as its work on specifications and ecosystem coordination, effectively ending its centralized support role. The IPFS project itself is not shutting down and will shift to individual maintainer grants. This marks a significant shift in IPFS’s decentralization, as a large centralized maintainer team steps back, potentially impacting development pace and stability of key implementations. It highlights the sustainability challenges of open-source decentralized infrastructure and may affect users relying on these implementations. Shipyard was formed in April 2024 as an independent collective of IPFS and libp2p maintainers; its sunset after only about two years underscores the difficulty of sustaining open-source maintenance without a strong business model. The initial blog post was confusing, leading many to believe the entire IPFS project was shutting down, but subsequent clarifications confirmed it is only Shipyard ending its role.

hackernews · iand · Aug 24, 15:48 · [Discussion](https://news.ycombinator.com/item?id=49421489)

**Background**: IPFS \(InterPlanetary File System\) is a decentralized peer-to-peer protocol for storing and sharing data using content addressing rather than location-based HTTP. It relies on multiple implementations and a network of nodes. Interplanetary Shipyard was an independent collective of developers that maintained key implementations like go-libp2p and js-libp2p, and contributed to IPFS specifications and ecosystem coordination. It emerged in 2024 after Protocol Labs reduced centralized support, aiming to decentralize maintenance.

<details><summary>References</summary>
<ul>
<li><a href="https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/">The end of IPFS at Shipyard</a></li>
<li><a href="https://blog.ipfs.tech/shipyard-hello-world/">IPFS &amp; libp2p Devs Go Independent: Meet Interplanetary Shipyard | IPFS Blog &amp; News</a></li>
<li><a href="https://en.wikipedia.org/wiki/IPFS">IPFS</a></li>

</ul>
</details>

**Discussion**: Community members expressed confusion over the misleading announcement, with the top comment clarifying that IPFS is not shutting down. Former maintainers voiced sadness and suggested alternatives like Iroh, built by ex-IPFS developers. Some criticized Protocol Labs&\#x27; priorities and noted Cloudflare’s earlier dropping of IPFS as a sign of decline. Others pointed out the irony of using a Google Form for feedback on a decentralized project. Overall sentiment is disappointment and concern about sustainability.

**Tags**: `#IPFS`, `#decentralization`, `#open-source-maintenance`, `#p2p`, `#ecosystem-shift`

---

<a id="item-9"></a>
## [Your executable is a SQLite database](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria demonstrated a technique to embed ELF executable components into a SQLite database file, making the database directly executable. The file&\#x27;s application ID at offset 68 is set to &\#x27;SELF&\#x27;, and a custom interpreter called self-exec extracts and runs the pieces. This trick cleverly combines two widely used file formats, demonstrating the flexibility of ELF and binfmt\_misc. It could simplify the packaging and distribution of tools that rely on SQLite data, offering a novel approach to executable file creation on Linux. The technique uses a specific SQLite table schema \(self.sql\) and a C interpreter \(self-exec.c\). On Linux, binfmt\_misc can be registered to automatically recognize the &\#x27;SELF&\#x27; magic bytes at offset 68 and hand off execution to self-exec.

rss · Simon Willison · Aug 24, 11:38

**Background**: ELF \(Executable and Linkable Format\) is the standard binary format for executables and shared libraries on Linux. binfmt\_misc is a Linux kernel feature that allows arbitrary file formats to be recognized by magic bytes and passed to user-space interpreters. SQLite database files begin with a header that includes a 4-byte application ID at offset 68, which this technique exploits to masquerade as a custom executable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binfmt_misc">Binfmt misc</a></li>
<li><a href="https://docs.kernel.org/admin-guide/binfmt-misc.html">Kernel Support for miscellaneous Binary Formats (binfmt_misc) — The Linux Kernel documentation</a></li>

</ul>
</details>

**Tags**: `#SQLite`, `#ELF`, `#Linux`, `#executable`, `#file format`

---

<a id="item-10"></a>
## [AAAI 2027 Organizers Acknowledge Reviewer Collusion via 2-Cycles](https://www.reddit.com/r/MachineLearning/comments/1vwujcy/aaai_2027_reviewer_bidding_and_assignment/) ⭐️ 7.0/10

AAAI 2027 organizers sent an email acknowledging collusion during the review process, specifically highlighting &\#x27;2-cycles&\#x27; where authors of paper A and B review each other&\#x27;s work, and hinting that such patterns may be concentrated among authors from a single country. This revelation threatens the integrity of a major machine learning conference, raising concerns about the fairness of peer review and the potential for colluding authors to gain unfair advantages, which could undermine trust in the entire academic publishing process. The email notes that 2-cycles can arise naturally from the assignment algorithm when a large proportion of submissions come from the same country, which may bias detection. The poster also points out that some accepted papers at top venues lack publicly available code, hindering reproducibility.

reddit · r/MachineLearning · /u/Fragrant\_Fan\_6751 · Aug 24, 06:11

**Background**: Machine learning conferences like AAAI, NeurIPS, and ICML use automated reviewer assignment systems to match papers to qualified reviewers while avoiding conflicts of interest. A 2-cycle is a pairing where two authors review each other&\#x27;s papers, which can be exploited for collusion. While such patterns can occur by chance, a country with a dominant share of submissions increases the likelihood of 2-cycles among its authors, making it harder to distinguish coincidence from deliberate collusion.

<details><summary>References</summary>
<ul>
<li><a href="https://mittmattmutt.medium.com/options-for-improving-peer-review-aa21b245fa04">Options for improving peer review | by Matthew McKeever | Medium</a></li>

</ul>
</details>

**Tags**: `#peer review`, `#academic integrity`, `#collusion`, `#AAAI`, `#machine learning`

---

<a id="item-11"></a>
## [CCPL: Delay-Corrected Bellman Operator and Causal Attribution for Constrained RL](https://www.reddit.com/r/MachineLearning/comments/1vx11hz/delaycorrected_bellman_operator_causal/) ⭐️ 7.0/10

Researchers propose CCPL, a constrained RL method that introduces a delay-corrected Bellman operator with an adaptive effective discount factor and a contraction proof valid under unknown stochastic delay, along with an Interventional Consequence Net \(ICN\) that attributes delayed consequences to the true causal action using structural causal model labels. This work addresses a critical real-world gap in constrained RL: penalizing agents based on immediate temporal proximity often misattributes delayed, stochastic violations, leading to unsafe policies. By providing a principled attribution mechanism, it could enable safer deployment in robotics, autonomous driving, and healthcare. The delay-corrected Bellman operator learns an effective discount in expectation over the consequence-delay distribution, and the contraction proof holds even when the delay distribution is unknown. The ICN estimates the marginal causal contribution of each action but requires pretraining labels from the environment&\#x27;s structural causal model, which is a significant practical limitation.

reddit · r/MachineLearning · /u/No\_Cauliflower7923 · Aug 24, 12:11

**Background**: Standard constrained RL imposes constraints on immediate outcomes, but real-world consequences \(e.g., safety violations, component wear\) often appear after a stochastic delay. The Bellman operator is a fundamental update rule in RL that expresses the value of a state in terms of expected future rewards, and its contraction property guarantees convergence of algorithms like value iteration. Causal attribution helps distinguish correlation from causation, which is crucial when assigning blame for delayed events. A structural causal model \(SCM\) explicitly describes how variables influence one another, enabling counterfactual reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://pypi.org/project/ccpl-rl/">Causal Consequence-Penalized Learning for delayed constrained...</a></li>
<li><a href="https://ai.stackexchange.com/questions/11057/what-is-the-bellman-operator-in-reinforcement-learning">terminology - What is the Bellman operator in reinforcement learning?</a></li>
<li><a href="https://web.stanford.edu/class/cme241/lecture_slides/BellmanOperators.pdf">Understanding (Exact) Dynamic Programming through Bellman ...</a></li>

</ul>
</details>

**Tags**: `#constrained-reinforcement-learning`, `#causal-inference`, `#bellman-operator`, `#delay-correction`, `#structural-causal-models`

---

<a id="item-12"></a>
## [Apple Confirms iCloud+ Hide My Email Addresses Stay on icloud.com](https://developer.apple.com/news/?id=1ptvdtcm) ⭐️ 6.0/10

Apple has officially announced that iCloud+ Hide My Email addresses will remain on the icloud.com domain, reversing a potential plan to change the domain in response to user feedback. The decision preserves stability for users who rely on these anonymous addresses across many services, preventing breakage and the need to update countless accounts. It also shows Apple&\#x27;s responsiveness to community concerns. Hide My Email generates random addresses that forward to the user&\#x27;s real inbox; the icloud.com domain is the default. Some users had seen addresses on privaterelay.appleid.com, leading to confusion, but Apple&\#x27;s confirmation keeps the familiar icloud.com.

hackernews · K7PJP · Aug 24, 22:13 · [Discussion](https://news.ycombinator.com/item?id=49426564)

**Background**: Hide My Email is a privacy feature in Apple&\#x27;s iCloud+ subscription that creates unique, random email addresses to shield the user&\#x27;s real email when signing up for websites or services. These addresses forward messages to the user&\#x27;s actual inbox and can be deleted at any time. A potential domain change would have forced users to update or recreate addresses, potentially breaking logins and communications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ICloud">ICloud</a></li>
<li><a href="https://support.apple.com/en-us/102602">About iCloud Private Relay - Apple Support</a></li>

</ul>
</details>

**Discussion**: Users generally welcomed the news, with many expressing gratitude that Apple listened to feedback. Some confusion remained about the privaterelay.appleid.com domain seen by a few users, and one commenter wished Sign in with Apple could be set up without a paid developer license.

**Tags**: `#apple`, `#privacy`, `#email`, `#icloud`, `#product-update`

---

<a id="item-13"></a>
## [Fringe Chinese Internet Movement Denies Tang Dynasty Existed](https://www.cnn.com/2026/08/19/style/china-tang-dynasty-never-existed-hoax-intl-hnk) ⭐️ 6.0/10

A CNN article reports on a fringe Chinese internet movement insisting that the Tang Dynasty never existed, sparking a high-quality Hacker News discussion. The phenomenon echoes the &\#x27;phantom time&\#x27; conspiracy theory and illustrates how fringe narratives can gain traction online, undermining public trust in established historical scholarship. Commenters noted that the Tang Dynasty is well-documented by primary sources, archaeological sites like the Qianling Mausoleum, and contemporary foreign accounts, making the denial absurd.

hackernews · related · Aug 24, 21:03 · [Discussion](https://news.ycombinator.com/item?id=49425819)

**Background**: The Tang Dynasty \(618-907 AD\) was a real and influential period in Chinese history, known for its cultural and economic achievements. The denial of its existence is a fringe conspiracy theory, similar to the Western &\#x27;phantom time&\#x27; hypothesis, which claims that certain historical periods were fabricated. Such theories are often fueled by nationalist or racist narratives.

**Discussion**: The Hacker News community generally dismissed the conspiracy as absurd, with users pointing to overwhelming evidence for the Tang Dynasty. Some compared it to the &\#x27;phantom time&\#x27; theory and noted its potential racist motivations, while others expressed concern about the broader trend of narrative warfare eroding historical truth.

**Tags**: `#misinformation`, `#history`, `#conspiracy-theories`, `#internet-culture`, `#China`

---

<a id="item-14"></a>
## [Unbounded Labs Open-Sources Bart, a 2.82B Vintage LLM Trained on Pre-1931 Texts](https://www.reddit.com/r/MachineLearning/comments/1vx94er/bart_a_vintage_llm_r/) ⭐️ 6.0/10

Unbounded Labs has developed and open-sourced Bart, a 2.82 billion-parameter language model trained exclusively on 20.1 billion tokens of English text written before 1931, aiming to test whether models can generate original scientific ideas like historical scientists. This project challenges the notion that LLMs merely regurgitate patterns; by restricting training data to pre-1931 texts, it provides a unique testbed to evaluate whether models can independently reason about scientific concepts without being exposed to modern knowledge, potentially advancing our understanding of machine creativity. The model was trained on a single H100 GPU in 5 days, achieving 60% model flops utilization \(MFU\); the team also curated the largest vintage SFT dataset \(416k graded Q&amp;A pairs\), built the Vintage CORE benchmark suite of 20 tasks, and conducted autonomous research that ran 100 experiments and found 26 improvements.

reddit · r/MachineLearning · /u/soggydoggy8 · Aug 24, 17:20

**Background**: In machine learning, an ablation study involves removing components to assess their impact. Supervised fine-tuning \(SFT\) is the process of further training a pre-trained model on labeled examples to improve performance on specific tasks. Post-training refers to the stages after initial pre-training, such as SFT and alignment, that adapt a model for practical use. A &\#x27;vintage LLM&\#x27; is a language model trained exclusively on historical texts from a specific era, in this case before 1931, to emulate the knowledge and style of that period.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ablation_%28machine_learning%29">Ablation (machine learning)</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/supervised-fine-tuning-sft-for-llms/">Supervised Fine-Tuning (SFT) for LLMs - GeeksforGeeks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-training_of_large_language_models">Post-training of large language models</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#historical-text`, `#training-from-scratch`, `#NLP`, `#experiment`

---