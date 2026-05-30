---
layout: default
title: "Horizon Summary: 2026-05-30 (EN)"
date: 2026-05-30
lang: en
---

> From 43 items, 9 important content pieces were selected

---

1. [Huawei Unveils 'Tao Law': Time Shrinkage Replaces Geometric Scaling for Chips](#item-1) ⭐️ 9.0/10
2. [The Dead Economy Theory: AI Automation Could Cannibalize Its Consumers](#item-2) ⭐️ 8.0/10
3. [SQLite Is All You Need for Durable Workflows](#item-3) ⭐️ 8.0/10
4. [UC Math Faculty Urge SAT/ACT Return for STEM Admissions](#item-4) ⭐️ 8.0/10
5. [Blog Post Defines AI Slop as Hollow LLM Output, Urges Sending Prompts Instead](#item-5) ⭐️ 8.0/10
6. [Deep Dive: Optimizing Code Diff Rendering for Large Diffs](#item-6) ⭐️ 8.0/10
7. [Is AI causing a repeat of frontend's lost decade?](#item-7) ⭐️ 8.0/10
8. [Rockstar Games Developers Unionize Over Pay and Crunch Culture](#item-8) ⭐️ 8.0/10
9. [We should be more tired than the model](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Huawei Unveils 'Tao Law': Time Shrinkage Replaces Geometric Scaling for Chips](https://t.me/zaihuapd/41648) ⭐️ 9.0/10

At the 2026 International Symposium on Circuits and Systems, Huawei introduced the 'Tao Law,' a new principle that targets time shrinkage—reducing signal propagation delay across device, circuit, and system levels—rather than traditional transistor miniaturization. The company revealed it has already used this approach to mass-produce 381 chips, with a new Kirin phone chip featuring logic folding technology set to launch this fall. The Tao Law addresses the economic and physical limits of Moore's Law, offering a path to sustain performance gains critical for AI and high-speed optical communication. It signals Huawei's bid to set a new industry direction at a time when traditional geometric scaling is stalling. Symbolized by τ (tau), the law targets time constant reduction to achieve coordinated optimization. Huawei projects that by 2031, its high-end chips using time shrinkage and logic folding will match the transistor density of a 1.4nm geometric-process node.

telegram · zaihuapd · May 30, 02:18

**Background**: Moore's Law historically drove chip progress by shrinking feature sizes (geometric scaling) to double transistor density. That approach now faces atomic-scale physical barriers and soaring costs. Time shrinkage instead focuses on making electrons 'travel faster' through advanced circuit and system design, reducing the delay τ and effectively increasing performance without ever-smaller lithography.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/955/839.htm">华为 韬 定 律 ，全球权威媒体 / 机构 / 顶级专家们都怎么看 - IT之家</a></li>
<li><a href="https://www.cls.cn/detail/2383556">华为公司董事、半导体业务部总裁何庭波：华为比同行更早遇到这堵“墙”</a></li>
<li><a href="https://36kr.com/p/3827586768688002">这两天，你τ了吗？ 扔掉制程的傻大憨粗，拥抱系统协同-36氪</a></li>

</ul>
</details>

**Tags**: `#半导体`, `#摩尔定律`, `#华为`, `#芯片设计`

---

<a id="item-2"></a>
## [The Dead Economy Theory: AI Automation Could Cannibalize Its Consumers](https://www.owenmcgrann.com/p/the-dead-economy-theory) ⭐️ 8.0/10

An article published on Owen McGrann's blog presents the 'dead economy theory', arguing that AI-driven automation could shrink its own consumer base, potentially triggering economic collapse. The piece ignited intense discussion on Hacker News, with 818 upvotes and over 1000 comments debating the paradox. This theory challenges the optimistic view of AI-driven productivity by exposing a potential feedback loop where cost-cutting layoffs erode the very market demand that sustains businesses. It raises urgent questions about sustainable economic models in an age of rapid automation. The article uses vivid analogies like the Ouroboros to illustrate the self-consuming nature of AI-driven cost cuts, and community discussion points out real-world examples of tech overcapacity, such as excessive developers on projects like Facebook Messenger. It also questions whether universal basic income would actually provide meaning, contrasting with the contentment of retirees.

hackernews · WillDaSilva · May 29, 15:46 · [Discussion](https://news.ycombinator.com/item?id=48324712)

**Background**: The 'dead economy theory' echoes long-standing debates about technological unemployment and the 'paradox of automation', where machines that boost productivity can undercut the purchasing power of workers. Unlike past industrial revolutions that eventually created new jobs, some economists fear that AI may displace workers faster than new roles can emerge, leading to structural demand deficits.

**Discussion**: Commenters broadly engaged with the theory, using metaphors like the Ouroboros and a greedy farmer to depict the self-defeating nature of AI-driven cost cutting. Some argued that overcapacity was already endemic in tech, while others debated whether a post-work society would lead to meaninglessness or, as with retirees, fulfillment. A few awaited real financial data from upcoming AI company IPOs to test sustainability.

**Tags**: `#economy`, `#AI`, `#automation`, `#future of work`, `#tech industry`

---

<a id="item-3"></a>
## [SQLite Is All You Need for Durable Workflows](https://obeli.sk/blog/sqlite-is-all-you-need-for-durable-workflows/) ⭐️ 8.0/10

A blog post argues that SQLite alone can serve as a sufficient backend for durable workflows, sparking debate on Hacker News about its concurrency limits and the growing use of embedded databases in production. This challenges the common reliance on complex workflow orchestrators or dedicated database servers, highlighting a movement toward minimal infrastructure that can cut costs and operational overhead for many applications. The discussion notes that with WAL mode, SQLite can handle moderate concurrency, though high-concurrency multi-process workloads still benefit from dedicated servers like PostgreSQL. One user replaced a full SaaS stack with Go + SQLite, cutting costs to one-tenth.

hackernews · tomasol · May 29, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48326802)

**Background**: Durable workflows persist execution state across failures and long waits, traditionally requiring external databases or services like Temporal or Inngest. SQLite is an embedded, serverless database that runs in-process; while historically limited in concurrent writes, modern improvements like WAL mode have expanded its production viability for many non-distributed workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://www.inngest.com/uses/durable-workflows">Inngest - Durable Workflows</a></li>
<li><a href="https://medium.com/@gwendal.roue/four-different-ways-to-handle-sqlite-concurrency-db3bcc74d00e">Four different ways to handle SQLite concurrency | Medium</a></li>
<li><a href="https://www.sqlite.org/lockingv3.html">File Locking And Concurrency In SQLite Version 3</a></li>

</ul>
</details>

**Discussion**: Comments are divided: proponents praise SQLite's simplicity and cost savings, with one replacing many SaaS tools using Go + SQLite. Critics argue that SQLite's concurrency model is fundamentally unsuitable for production applications, recommending dedicated database servers. Some note that DuckDB may outperform SQLite for ETL tasks.

**Tags**: `#sqlite`, `#workflows`, `#software-architecture`, `#databases`, `#concurrency`

---

<a id="item-4"></a>
## [UC Math Faculty Urge SAT/ACT Return for STEM Admissions](https://www.latimes.com/california/story/2026-05-27/uc-math-professors-demand-return-of-sat-for-stem-admissions) ⭐️ 8.0/10

University of California math faculty are demanding the reinstatement of SAT/ACT scores for STEM admissions, citing severe math deficiencies among incoming students that force instructors to re-teach middle-school math. This pushback against test-optional policies was made public through a faculty letter. The debate highlights systemic failures in K-12 math education that could undermine STEM workforce development, equity in admissions, and the academic readiness of future scientists and engineers. The faculty letter warns instructors must reteach middle-school mathematics while covering college material, and critics counter that placement tests and prerequisites could filter unprepared students without reinstating the SAT.

hackernews · brandonb · May 28, 14:13 · [Discussion](https://news.ycombinator.com/item?id=48309233)

**Background**: Starting in 2020, the University of California system and many other universities dropped SAT/ACT requirements to promote equity amid concerns about socioeconomic bias. However, faculty have increasingly reported that incoming students lack fundamental math skills, leading to calls for reinstatement. The SAT historically served as a common benchmark for college readiness across diverse high schools.

**Discussion**: Comments reveal contrasting views: one contributor from Italy notes that rigorous university exams, not entrance tests, ensure quality. Others argue professors should enforce prerequisites rather than reteach middle school math, and some blame digital distractions in high school math classes for declining skills.

**Tags**: `#education`, `#standardized-testing`, `#STEM`, `#math-education`, `#higher-education`

---

<a id="item-5"></a>
## [Blog Post Defines AI Slop as Hollow LLM Output, Urges Sending Prompts Instead](https://noperator.dev/posts/you-can-just-say-it/) ⭐️ 8.0/10

The blog post by noperator.dev defines 'AI slop' as large, motivation-lacking text generated by LLMs, and argues that sending the raw prompt would be more authentic than the inflated, hollow final message. This definition directly addresses growing unease about authenticity in AI-mediated communication, encouraging people to prioritize genuine intent over polished but meaningless filler in personal and professional correspondence. The post distinguishes between using AI and misusing it, emphasizing that slop arises from a lack of fundamental motivation or understanding, not the technology itself. The community deepened the discussion with philosophical reflections, including a C.S. Lewis quote on human dignity.

hackernews · antirez · May 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48324853)

**Background**: The term 'AI slop' emerged in the 2020s to describe low-effort, high-volume synthetic content, often generated for clickbait or monetary gain. This blog post extends the concept to everyday interpersonal communication, contrasting genuine human expression with hollow AI-generated text. Similar to spam, AI slop is widely criticized for degrading online content quality.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop</a></li>
<li><a href="https://theconversation.com/what-is-ai-slop-a-technologist-explains-this-new-and-largely-unwelcome-form-of-online-content-256554">What is AI slop? A technologist explains this new and largely unwelcome form of online content</a></li>

</ul>
</details>

**Discussion**: The commenters overwhelmingly endorse the definition, linking it to broader issues of dehumanization and the intrinsic value of human effort. Many share personal reflections on identity crises in the AI era, while others, like antirez, praise the post's conciseness and its capacity to blame misuse rather than AI itself. The discussion is enriched by literary quotes, reinforcing the call for authenticity.

**Tags**: `#AI slop`, `#communication`, `#LLM ethics`, `#authenticity`, `#human-AI interaction`

---

<a id="item-6"></a>
## [Deep Dive: Optimizing Code Diff Rendering for Large Diffs](https://pierre.computer/writing/on-rendering-diffs) ⭐️ 8.0/10

An in-depth article details several techniques to drastically speed up rendering of large code diffs in web-based editors, such as deferred syntax highlighting and an innovative 'inverse sticky' scrolling method, receiving enthusiastic feedback from developers. Optimizing diff rendering is crucial for developer productivity, as slow interfaces can make reviewing large pull requests frustrating; these techniques could directly influence future improvements in major platforms like GitHub and code editors, enhancing the daily workflow of millions of developers. Key techniques include deferring syntax highlighting to idle time and using an 'inverse sticky' viewport lock to prevent blank flashes; however, the sticky method has a drawback where fast scrolling can temporarily halt scroll, as noted by a commenter.

hackernews · amadeus · May 29, 19:04 · [Discussion](https://news.ycombinator.com/item?id=48327809)

**Background**: Code diff rendering is the visual display of file changes between versions, often shown in split or unified views. For large diffs with thousands of changed lines, browser-based editors can become slow due to the need to compute layout, apply syntax highlighting, and update the DOM for each line. Performance optimizations typically involve incremental rendering, virtualization, and deferred work.

**Discussion**: Community reaction is largely enthusiastic, with many praising the article's clarity and practical value. A developer building a CAD diff tool found the deferred highlighting technique applicable to their work. Some skepticism was raised about the 'inverse sticky' scrolling, which a commenter noted can disrupt scrolling if too fast, and questioned whether browsers should handle rendering more efficiently without such tricks.

**Tags**: `#diff`, `#rendering`, `#performance`, `#optimization`, `#frontend`

---

<a id="item-7"></a>
## [Is AI causing a repeat of frontend's lost decade?](https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/) ⭐️ 8.0/10

A blog post by Mastro argues that AI-assisted coding tools risk repeating the 'lost decade' of frontend development, where JavaScript frameworks abstracted away core skills and led to a decline in deep expertise, sparking a high-volume debate among developers. The discussion highlights a critical tension in software engineering: the trade-off between accessibility and quality. If AI deskills developers en masse, the long-term health of the web ecosystem—including security, accessibility, and performance—could be compromised. The article draws an analogy between JavaScript frameworks (which treat the browser as a compilation target) and AI coding assistants (which may render knowledge of HTML/CSS obsolete). Commenter kangalioo argues that much of the lost 'deep expertise' was accidental complexity, while kristianc emphasizes that more people building things is a net positive even if quality varies.

hackernews · xyzal · May 29, 11:09 · [Discussion](https://news.ycombinator.com/item?id=48321631)

**Background**: The 'lost decade' of frontend development refers to the era when frameworks like React and Angular became dominant, abstracting away direct HTML/CSS/JS manipulation. This enabled faster development but resulted in many developers lacking foundational knowledge of browser APIs, performance optimization, and web standards. The concern now is that AI tools like GitHub Copilot may further deskill developers by generating code without understanding, analogous to earlier framework-induced abstraction.

<details><summary>References</summary>
<ul>
<li><a href="https://mastrojs.github.io/blog/2026-05-23-is-AI-causing-a-repeat-of-frontends-lost-decade/">Is AI causing a repeat of Frontend ’s Lost Decade? | Mastro Blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=48321631">Is AI causing a repeat of frontend's lost decade? - Hacker News</a></li>
<li><a href="https://kpwags.com/posts/2026/is-ai-causing-a-repeat-of-frontends-lost-decade/">Extended Note: Is AI causing a repeat of Frontend's Lost Decade?</a></li>

</ul>
</details>

**Discussion**: Community sentiment largely disputes the article's premise, arguing that the lost 'deep expertise' was often accidental complexity like browser quirks rather than valuable skill. Several commenters note that AI can enforce a 'latent rigor' missing from framework-era abstractions, and that prior to AI, much web work was already mediocre. The overall view is that increased accessibility and speed outweigh potential quality drops.

**Tags**: `#AI`, `#frontend`, `#web development`, `#software engineering`, `#developer experience`

---

<a id="item-8"></a>
## [Rockstar Games Developers Unionize Over Pay and Crunch Culture](https://rockstarintel.com/gta-6-developers-announce-rockstar-games-union/) ⭐️ 8.0/10

Rockstar Games developers have formally announced a union, demanding pay transparency, flexible working, and an end to crunch culture at the studio behind Grand Theft Auto 6. This unionization at a high-profile game studio highlights long-standing issues of wage disparity and excessive overtime in game development, and could pressure the broader tech industry to improve labor standards. The union's initial platform focuses on three demands: pay transparency, flexible working arrangements, and an end to crunch—the compulsory, often unpaid overtime common during game development.

hackernews · AndrewKemendo · May 29, 15:32 · [Discussion](https://news.ycombinator.com/item?id=48324499)

**Background**: Crunch is a widespread practice in game development where workers put in extreme overtime, sometimes 65–80 hours per week, often without extra compensation. Unionization in the tech and gaming sectors has historically been rare, though recent efforts at companies like Activision Blizzard and now Rockstar indicate a growing movement.

**Discussion**: Commenters discussed wage gaps between game and big tech, condemned crunch as predatory, and debated how outsourcing and H1B visas weaken union leverage. Overall sentiment was largely supportive of the union, with some cynicism about employer resistance.

**Tags**: `#unionization`, `#gaming industry`, `#labor rights`, `#tech culture`, `#crunch`

---

<a id="item-9"></a>
## [We should be more tired than the model](https://vickiboykis.com/2026/05/28/we-should-be-more-tired-than-the-model/) ⭐️ 8.0/10

A recent essay by Vicki Boykis argues that in the age of AI coding assistants, developers should be more tired than the model — meaning they must invest more effort in understanding code than the model spends generating it, to avoid a decline in code quality. This perspective challenges the industry’s focus on AI-driven productivity, warning that overreliance on generated code without deep understanding can erode developer skills and lead to brittle, hard-to-maintain systems. It matters to anyone building long-lived software, as the author emphasizes that comprehension remains the bottleneck for quality. The article claims understanding is the bottleneck in AI-assisted development, and developers must actively direct agents for tasks like refactoring and test deduplication rather than passively accepting code. Community commenters highlight that abstraction skills and programming fundamentals remain critical, though some note that ‘taste’ (the ability to judge code) might degrade differently than specific technical skills.

hackernews · tosh · May 29, 12:12 · [Discussion](https://news.ycombinator.com/item?id=48322118)

**Background**: AI coding assistants such as GitHub Copilot, Cursor, and ChatGPT have surged in popularity, enabling developers to generate large amounts of code quickly. However, concerns have emerged that developers may accept AI-generated code without fully understanding it, leading to technical debt, security flaws, and erosion of fundamental programming skills. The article by Vicki Boykis enters this ongoing debate, advocating that true software engineering still requires deep comprehension and deliberate effort.

**Discussion**: The community broadly agrees that understanding is the core bottleneck, but offers varied adaptation strategies. Simonw describes directing agents for refactoring to maintain code structure, while paulmooreparks sees moving to a higher-level product role as acceptable. CraigJPerry emphasizes abstraction as the key tool, and adamtaylor_13 questions whether skill loss is truly problematic if ‘taste’ remains. The discussion reveals a spectrum of approaches rather than a single right answer.

**Tags**: `#AI`, `#software-engineering`, `#developer-productivity`, `#coding-assistants`, `#code-quality`

---