---
layout: default
title: "Horizon Summary: 2026-06-24 (EN)"
date: 2026-06-24
lang: en
---

> From 37 items, 17 important content pieces were selected

---

1. [Rhombus Language 1.0 Officially Released with New Syntax and Macro System](#item-1) ⭐️ 9.0/10
2. [Prompt Injection as Role Confusion](#item-2) ⭐️ 9.0/10
3. [FUTO Swipe: Open-Source Swipe Typing Model and Keyboard App](#item-3) ⭐️ 8.0/10
4. [Meta Pauses Employee-Tracking Program After Internal Data Leak](#item-4) ⭐️ 8.0/10
5. [WYSIWYG TikZ Editor for LaTeX Figure Creation](#item-5) ⭐️ 8.0/10
6. [The Coming Loop: LLMs, Software Development, and the Loss of Human Understanding](#item-6) ⭐️ 8.0/10
7. [Porting the Moebius 0.2B Image Inpainting Model to Run in the Browser](#item-7) ⭐️ 8.0/10
8. [DeepSWE: A Contamination-Free Benchmark for Frontier Coding Agents](#item-8) ⭐️ 8.0/10
9. [Vulnerability reports are not special anymore](#item-9) ⭐️ 7.0/10
10. [Swift Package Index Joins Apple](#item-10) ⭐️ 7.0/10
11. [The Worthlessness of Vitamin D Is Mildly Exaggerated](#item-11) ⭐️ 7.0/10
12. [Extreme Heat conference cancelled due to extreme heat warning](#item-12) ⭐️ 7.0/10
13. [Datasette 1.0a35: New JSON API and UI for Table Creation and Alteration](#item-13) ⭐️ 7.0/10
14. [Remembering the Creator of Word's Red and Green Squiggles](#item-14) ⭐️ 6.0/10
15. [Kevin Mitnick Gifts Dream Car to the Man Who Helped Imprison Him](#item-15) ⭐️ 6.0/10
16. [A Test Harness for OPFS + Pyodide Persistent SQLite Editing in Datasette Lite](#item-16) ⭐️ 6.0/10
17. [Non-deterministic LLM Vulnerability Detection Benchmark Using Hidden Juliet Cases](#item-17) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Rhombus Language 1.0 Officially Released with New Syntax and Macro System](https://blog.racket-lang.org/2026/06/rhombus-v1.0.html) ⭐️ 9.0/10

The Rhombus programming language has reached its 1.0 milestone, bringing a conventional syntax and a powerful macro system to the Racket ecosystem, as announced on the Racket blog. This release makes Racket's renowned macro capabilities more accessible to developers who prefer familiar syntax, potentially broadening the adoption of language-oriented programming and enabling more intuitive language design. A standout feature is the `…` operator, which is itself a macro – not a built-in – and can manipulate nested data structures in place of map operations. Rhombus uses a 'shrubbery' notation to define macros, allowing syntax extensions to be implemented as libraries.

hackernews · Decabytes · Jun 22, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48633473)

**Background**: Racket is a Lisp descendant known for its language creation capabilities, but its parenthesized syntax can be a barrier. Rhombus is an experiment to provide a conventional surface syntax while retaining Racket's macro system, using a novel 'shrubbery' notation. This 1.0 release represents years of development to make language design more approachable.

<details><summary>References</summary>
<ul>
<li><a href="https://rhombus-lang.org/">Rhombus Programming Language</a></li>
<li><a href="https://github.com/racket/rhombus">GitHub - racket/rhombus: Rhombus programming language · GitHub</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion is enthusiastic, with developers praising the `…` operator's macro-based flexibility. Some long-time Racket users still prefer s-expressions, but overall the community is excited about Rhombus's potential for macro extensibility and its impact on language design.

**Tags**: `#programming-languages`, `#racket`, `#rhombus`, `#macros`, `#syntax`

---

<a id="item-2"></a>
## [Prompt Injection as Role Confusion](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything) ⭐️ 9.0/10

New research by Charles Ye, Jasmine Cui, and Dylan Hadfield-Menell demonstrates that LLMs prioritize the writing style of input over explicit role tags like <system> and <user>, leading to successful jailbreaks. The paper also introduces 'destyling' as a mitigation, which reduces attack success rates from 61% to 10%. This finding exposes a fundamental flaw in current LLM safety mechanisms: models cannot reliably distinguish between system instructions and user input based on role tags alone. It undermines the security of AI assistants, agents, and any system that relies on prompt formatting to separate trusted from untrusted data, making prompt injection a perpetual challenge. The attack appends text that mimics the style of model internal thinking blocks, causing models like gpt-oss-20b to override safety policies. 'Destyling'—rewriting untrusted text in a slightly different way—reduces attack success from 61% to 10%, a change nearly invisible to humans but drastic for LLMs.

rss · Simon Willison · Jun 22, 23:59

**Background**: Prompt injection is a cybersecurity attack on LLMs where adversarial inputs are designed to cause unintended behavior, exploiting the model's inability to distinguish between developer instructions and user inputs. Many AI systems use special role tags (e.g., <system>, <user>, <assistant>) to separate trusted and untrusted text. Jailbreaking refers to bypassing these safety filters to make the model comply with harmful requests. This new research shows that even with role tags, models can be confused by mimicking the style of trusted text, undermining a key defense.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.ibm.com/think/topics/prompt-injection">What Is a Prompt Injection Attack? | IBM</a></li>

</ul>
</details>

**Tags**: `#prompt injection`, `#AI safety`, `#large language models`, `#jailbreak`, `#security`

---

<a id="item-3"></a>
## [FUTO Swipe: Open-Source Swipe Typing Model and Keyboard App](https://swipe.futo.tech/) ⭐️ 8.0/10

FUTO has released FUTO Swipe, an open-source swipe typing model, along with its FUTO Keyboard app for Android, which runs fully offline and offers privacy-focused features like autocorrect and predictive text. This provides a privacy-respecting alternative to commercial swipe keyboards like Gboard, which often require internet access and data collection. It empowers users with full control over their typing data and model customization. The model is available for download, and the keyboard app is currently Android-only. It supports swipe typing, autocorrect, and predictive text, but early users report issues like random capitalization and lack of context-aware word suggestions.

hackernews · futohq · Jun 23, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48648619)

**Background**: Swipe typing allows users to slide a finger across letters to form words, speeding up mobile text input. Existing popular options like Google's Gboard and Apple's keyboard often rely on cloud services. FUTO is a technology organization focused on giving users control of their computing devices, and its keyboard is designed to operate entirely on-device without internet access.

<details><summary>References</summary>
<ul>
<li><a href="https://swipe.futo.tech/">FUTO Swipe</a></li>
<li><a href="https://keyboard.futo.org/">FUTO Keyboard</a></li>
<li><a href="https://grokipedia.com/page/futo">Futo</a></li>

</ul>
</details>

**Discussion**: Community feedback is enthusiastic, with many users expressing interest in switching from Gboard. Common requests include multi-language support without switching, a keyboard layout optimized for swiping, and better iOS support. Some users report minor bugs like random capitalization and limited context awareness, but the recent update has convinced some to switch permanently.

**Tags**: `#swipe-typing`, `#open-source`, `#keyboard`, `#machine-learning`, `#mobile`

---

<a id="item-4"></a>
## [Meta Pauses Employee-Tracking Program After Internal Data Leak](https://www.wired.com/story/meta-pauses-employee-tracking-program-following-internal-security-breach/) ⭐️ 8.0/10

Meta suspended an internal employee-tracking program after a leak exposed sensitive performance data and full-screen recordings of employees. This incident highlights the tension between corporate surveillance and employee privacy, raising questions about Meta's data handling practices and its impact on trust. The leaked data included plain-text private conversations and performance metrics, suggesting the tracking program captured full-screen recordings without adequate anonymization.

hackernews · 1vuio0pswjnm7 · Jun 24, 00:28 · [Discussion](https://news.ycombinator.com/item?id=48653575)

**Discussion**: Comments overwhelmingly condemn Meta, calling it shameless and untrustworthy, and questioning the ethics of the surveillance and the leak. Some note the recordings were not anonymized, and sarcasm suggests high pay is the only draw.

**Tags**: `#Meta`, `#employee surveillance`, `#data leak`, `#privacy`, `#corporate ethics`

---

<a id="item-5"></a>
## [WYSIWYG TikZ Editor for LaTeX Figure Creation](https://tikz.dev/editor/) ⭐️ 8.0/10

An open-source WYSIWYG editor for TikZ figures in LaTeX was released, enabling simultaneous visual and code editing with real-time synchronization. The tool was built with the help of the Codex coding agent, reimplementing much of TikZ. TikZ is widely used in academic papers for technical figures, but hand-coding is tedious and error-prone. This editor dramatically lowers the barrier, potentially saving researchers time and making high-quality diagrams more accessible. The editor parses TikZ code to track source positions of each object, so dragging updates only coordinate numbers without changing the rest of the code. It includes converters from SVG, PPTX, and IPE to TikZ, a reimplementation of LaTeX's hyphenation algorithm for multi-line nodes, and a color picker supporting the red!20!black mixing notation. Some users noted that the generated code relies on absolute coordinates, which may be less flexible than relative positioning.

hackernews · DominikPeters · Jun 23, 14:24 · [Discussion](https://news.ycombinator.com/item?id=48645437)

**Background**: TikZ is a popular LaTeX package for creating vector graphics programmatically, using commands like \draw to specify lines, shapes, and nodes. It is favored in academic publishing for its ability to produce publication-quality diagrams that blend seamlessly with document typography. Traditionally, users must write and compile the code repeatedly to adjust positions, which is a time-consuming process. The WYSIWYG editor aims to simplify this by providing direct visual manipulation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TikZ">TikZ</a></li>

</ul>
</details>

**Discussion**: Community feedback was mostly positive, praising the UI and the concept. Some users expressed concern that the generated code uses absolute coordinates, which is not idiomatic TikZ, suggesting that relative positioning would be better. The author shared that the project was developed using Codex over months, consuming 700M tokens and costing approximately $15k in API usage, but only $500 in ChatGPT subscription fees.

**Tags**: `#tikz`, `#latex`, `#wysiwyg`, `#editor`, `#academic-tools`

---

<a id="item-6"></a>
## [The Coming Loop: LLMs, Software Development, and the Loss of Human Understanding](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) ⭐️ 8.0/10

A prominent software developer reflects on the growing reliance on LLMs in coding, warning that it may erode human understanding of code and lead to codebases that are unmaintainable by humans alone. The discussion highlights the risk of creating unmaintainable systems and losing the aesthetic judgment that comes from deep human understanding, which could degrade software quality and development practices. The article notes that LLMs are great at finishing tasks but lack aesthetic judgment, and that the bottleneck shifts to writing clear specifications; meanwhile, some developers merge code they cannot fully explain and rely on LLMs to summarize discussions.

hackernews · ingve · Jun 23, 11:06 · [Discussion](https://news.ycombinator.com/item?id=48643180)

**Background**: LLMs (large language models) like GPT-4 and Claude are increasingly used to generate and debug code. The author, Armin Ronacher, is a well-known open-source developer (creator of Flask) whose opinions carry weight in the software community. The 'coming loop' refers to a future where software development may become a cycle of LLM-generated code that humans can no longer fully understand or maintain, shifting the role of developers from creators to mere prompt engineers.

**Discussion**: Community members broadly agree that LLMs accelerate coding but cannot replace the clarity and iterative thinking needed for good design. Key concerns include the creation of codebases that assume machine maintenance, loss of human ability to discuss code without LLM assistance, and the shift of the bottleneck to writing precise specifications.

**Tags**: `#llm`, `#software-development`, `#ai-ethics`, `#technical-debt`, `#human-in-the-loop`

---

<a id="item-7"></a>
## [Porting the Moebius 0.2B Image Inpainting Model to Run in the Browser](https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything) ⭐️ 8.0/10

Simon Willison ported the Moebius 0.2B image inpainting model to the browser using WebGPU, assisted by Claude Code, and released a live demo at simonw.github.io/moebius-web/. This enables inpainting directly in the browser without requiring a powerful GPU or CUDA, democratizing access to AI-powered image editing and lowering barriers for users. The port used ONNX Runtime Web on the WebGPU backend, leveraging the small 0.2B parameter model. The original Moebius model required PyTorch and NVIDIA CUDA, but the port runs entirely client-side.

rss · Simon Willison · Jun 22, 23:43

**Background**: Image inpainting is a technique to reconstruct missing or damaged parts of an image. WebGPU is a modern web API that provides low-level GPU access in browsers, enabling high-performance graphics and AI computations. ONNX Runtime Web is a library that executes ONNX models in the browser, often on WebGPU. By porting a model to run in the browser, it eliminates the need for server-side infrastructure and specialized hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Image_inpainting">Image inpainting</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU</a></li>

</ul>
</details>

**Tags**: `#WebGPU`, `#inpainting`, `#browser`, `#AI`, `#porting`

---

<a id="item-8"></a>
## [DeepSWE: A Contamination-Free Benchmark for Frontier Coding Agents](https://www.reddit.com/r/MachineLearning/comments/1ue0hlp/deepswe_new_benchmark_looking_at_how_well_todays/) ⭐️ 8.0/10

DeepSWE introduces a new benchmark with contamination-free tasks written from scratch, spanning 91 repositories and 5 languages, and reveals that even top models like GPT and Claude struggle with complex, under-specified software engineering problems. This benchmark addresses critical flaws in existing coding evaluations—such as data contamination and limited diversity—and provides a more realistic measure of how frontier coding agents perform on actual engineering work, directly impacting model selection and research direction. Tasks are curated from scratch, avoiding any overlap with pretraining data; prompts are about half the length of SWE-bench Pro's, yet solutions require 5.5× more code and roughly twice the output tokens; verifiers are hand‑written to test software behavior rather than implementation details.

reddit · r/MachineLearning · /u/we_are_mammals · Jun 24, 02:03

**Background**: Existing coding benchmarks like SWE-bench often suffer from contamination, where models may have seen the solutions during pretraining, and they may not reflect the true complexity of real‑world software engineering. DeepSWE is designed to overcome these issues by offering a diverse set of original, long‑horizon tasks that are harder and more representative of what engineers actually do.

<details><summary>References</summary>
<ul>
<li><a href="https://deepswe.datacurve.ai/">DeepSWE</a></li>
<li><a href="https://benchlm.ai/benchmarks/deepSwe">DeepSWE Benchmark 2026: 8 pass@1 rows | BenchLM.ai</a></li>
<li><a href="https://deepswe.net/">DeepSWE Benchmark: GPT vs Claude for Agentic Coding</a></li>

</ul>
</details>

**Tags**: `#AI`, `#benchmark`, `#software engineering`, `#LLM`, `#code generation`

---

<a id="item-9"></a>
## [Vulnerability reports are not special anymore](https://words.filippo.io/vuln-reports/) ⭐️ 7.0/10

Filippo Valsorda argues that the influx of LLM-generated low-quality vulnerability reports has devalued the reporting process, making them no longer special for either researchers or maintainers. This undermines trust in vulnerability disclosure, potentially causing maintainers to ignore genuine reports and altering the dynamics of security research, with broad implications for software security. Many reports are now spam or extortion attempts, half of unsolicited reports are LLM-generated trivialities, and some projects may choose to ignore all reports, while researchers may find it easier to just use zero-days.

hackernews · goranmoomin · Jun 23, 23:42 · [Discussion](https://news.ycombinator.com/item?id=48653216)

**Background**: Vulnerability disclosure is a process where security researchers report flaws to software maintainers for responsible fixing. Traditionally, it relied on trust and collaboration. The rise of LLMs has enabled the mass generation of plausible but often false or trivial bug reports, overwhelming maintainers and devaluing genuine efforts, similar to AI-generated spam in other fields.

**Discussion**: Commenters note that spam has overrun vulnerability reporting, with many reports being LLM-based trivialities or extortion. Some argue that the process benefits the project, not the researcher, and that projects could always refuse reports. Others believe this is temporary, as LLMs will eventually help fix bugs and reduce future reports, and call for engineering solutions to eliminate bug classes.

**Tags**: `#cybersecurity`, `#vulnerability-disclosure`, `#LLMs`, `#software-security`, `#bug-bounty`

---

<a id="item-10"></a>
## [Swift Package Index Joins Apple](https://swiftpackageindex.com/blog/swift-package-index-joins-apple) ⭐️ 7.0/10

The community-run Swift Package Index, a search engine indexing over 11,000 Swift packages, announced it is joining Apple, with the founding team becoming full-time Apple employees. This move could strengthen the Swift package ecosystem by providing Apple's resources, but raises concerns about corporate control over a community resource and Apple's commitment to open-source maintenance. The SPI currently indexes metadata from over 11,000 packages and only supports GitHub repositories. The announcement mentions developer identity as a future direction and pledges the project will remain open source.

hackernews · JDevlieghere · Jun 23, 18:00 · [Discussion](https://news.ycombinator.com/item?id=48648779)

**Background**: The Swift Package Index is a community-built search engine for Swift packages, providing metadata like compatibility, quality, and dependencies to help developers choose packages. It is distinct from the official Swift Package Registry on Swift.org. Apple has a mixed open-source reputation: while Swift and many tools are open source, some developer services and processes remain proprietary.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/06/23/swift-package-index-joins-apple-pledges-to-remain-open-source/">Swift Package Index joins Apple, pledges to remain open ...</a></li>
<li><a href="https://swiftpackageindex.com/">Swift Package Index</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some congratulate the team on the recognition, while others are skeptical about Apple's open-source track record. The limitation to GitHub-only repos and the mention of developer identity as a future direction raise concerns about potential lock-in and the project's independence.

**Tags**: `#swift`, `#apple`, `#package-management`, `#open-source`, `#community`

---

<a id="item-11"></a>
## [The Worthlessness of Vitamin D Is Mildly Exaggerated](https://dynomight.net/vitamin-d/) ⭐️ 7.0/10

A balanced analysis of Vitamin D studies shows that supplementation primarily benefits those with severe deficiency, while many general health claims are unsupported by rigorous evidence. This nuanced perspective helps clarify the true value of Vitamin D supplementation, countering both excessive hype and unwarranted nihilism, which could influence public health guidelines and personal health choices. Researchers note that current Vitamin D intake recommendations are based on faulty statistical interpretation, and many studies fail to measure blood levels or account for co-factors like Vitamin K2.

hackernews · surprisetalk · Jun 23, 16:30 · [Discussion](https://news.ycombinator.com/item?id=48647486)

**Background**: Vitamin D research has been mired in controversy, with observational studies often showing strong associations between low levels and poor health, but randomized controlled trials (RCTs) failing to replicate many benefits. This discrepancy may be due to confounding variables (e.g., healthy lifestyle factors), p-hacking (manipulating data to find significant results), and limitations of RCTs like short duration or low doses. The debate is further fueled by health influencers making exaggerated claims.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/P-hacking">P-hacking</a></li>
<li><a href="https://www.biostatistics.ca/the-influence-of-confounding-variables-in-observational-studies/">The Influence of Confounding Variables in Observational Studies</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/32560898/">Limitations of Randomized Clinical Trials - PubMed</a></li>

</ul>
</details>

**Discussion**: Commenters generally praised the balanced analysis. They pointed out specific study flaws, such as NHANES' seasonal data collection bias, and the misapplication of statistical confidence intervals in setting recommended daily allowances. Some noted that without measuring blood levels or accounting for co-factors like K2, studies may miss real benefits. Others shared personal anecdotes of needing higher doses to achieve normal levels.

**Tags**: `#vitamin-d`, `#evidence-based-medicine`, `#health`, `#study-design`, `#nutrition`

---

<a id="item-12"></a>
## [Extreme Heat conference cancelled due to extreme heat warning](https://www.lse.ac.uk/granthaminstitute/events/extreme-heat-improving-governance-and-strengthening-action-around-the-world/) ⭐️ 7.0/10

The 'Extreme Heat: improving governance and strengthening action around the world' conference, scheduled to be held at the London School of Economics, was cancelled due to an extreme heat warning issued for the area. The cancellation ironically demonstrates that even experts planning to discuss heat resilience are not immune to its effects, exposing infrastructure and cultural unpreparedness for rising temperatures. The conference was organized in collaboration with the Zurich Climate Resilience Alliance and was scheduled to conclude with a 'fireside chat,' a detail that now adds to the irony.

hackernews · rendx · Jun 23, 23:26 · [Discussion](https://news.ycombinator.com/item?id=48653060)

**Background**: Many European buildings, including in the UK, are designed to retain heat and lack air conditioning, making them vulnerable to heatwaves. Climate change is increasing the frequency of extreme heat events, exposing regions with historically temperate climates to dangerous temperatures. Heatwaves cause thousands of preventable deaths annually, and some European countries experience higher heat-related mortality rates than hotter nations due to infrastructure and cultural differences.

**Discussion**: Commenters widely acknowledged the irony as genuine, contrasting it with the often-misused term. Discussions highlighted Europeans' resistance to air conditioning, noting that Greece has double the heat-related deaths per capita than Mississippi's gun deaths. Others from hotter climates, like Australia, found the temperatures mundane but pointed to inadequate building design. The planned 'fireside chat' and the involvement of a climate resilience alliance were noted as particularly ironic.

**Tags**: `#irony`, `#climate-change`, `#heat-waves`, `#conference`, `#adaptation`

---

<a id="item-13"></a>
## [Datasette 1.0a35: New JSON API and UI for Table Creation and Alteration](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a35 introduces new JSON API endpoints and a user interface for creating and altering tables directly from the browser, along with stable template context documentation for custom templates. These features mark a major step toward the 1.0 milestone, transforming Datasette from a read-only data exploration tool into a platform that allows full table management, which will greatly benefit developers and non-technical users working with SQLite databases. The create table API supports defining columns, primary keys, custom column types, NOT NULL constraints, literal defaults, expression defaults, and single-column foreign keys. The alter table API allows adding, renaming, reordering, dropping columns, changing types, defaults, constraints, foreign keys, and table renaming, with a drop table button included.

rss · Simon Willison · Jun 23, 21:34

**Background**: Datasette is an open-source tool by Simon Willison that enables users to explore and publish SQLite databases via a web interface and JSON API. It has long been read-only, focusing on querying and visualizing data. The 1.0 alpha series is actively adding write capabilities, with this release providing the first built-in table creation and alteration features.

**Tags**: `#datasette`, `#sqlite`, `#data-tools`, `#open-source`, `#release`

---

<a id="item-14"></a>
## [Remembering the Creator of Word's Red and Green Squiggles](https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451) ⭐️ 6.0/10

The blog post 'In memory of the man who put red and green squiggles under words' pays tribute to the originator of Microsoft Word's iconic spell-check and grammar-check underlines, revealing that the feature arose from a single person's whimsical decision. This story illustrates how a seemingly minor UI choice can become a universal standard, influencing millions of users and inspiring countless imitations in productivity software. The article contains a circular reference: it cites Wikipedia as evidence, which in turn cites the article itself. The feature was reportedly ported by engineer Tony Krueger.

hackernews · saikatsg · Jun 23, 18:10 · [Discussion](https://news.ycombinator.com/item?id=48648959)

**Background**: Red and green squiggly underlines are universal indicators of spelling and grammar errors in word processors, first introduced in Microsoft Word. The decision to use wavy lines rather than other visual cues was a subjective choice that became a de facto standard.

**Discussion**: The community discussion is largely positive, with one commenter pointing out a humorous circular reference in the article's sourcing. Others appreciate the whimsical origin story, though some note practical frustrations with squiggles in multilingual settings, and there are lighthearted suggestions for yellow 'logic error' squiggles.

**Tags**: `#spell-check`, `#UI-history`, `#Microsoft`, `#HCI`, `#anecdote`

---

<a id="item-15"></a>
## [Kevin Mitnick Gifts Dream Car to the Man Who Helped Imprison Him](https://www.thedrive.com/news/this-man-was-gifted-his-dream-car-by-the-notorious-hacker-he-put-in-prison) ⭐️ 6.0/10

Notorious hacker Kevin Mitnick gave a 1969 Chevrolet Camaro, his dream car, to Shawn Nunley, the computer security expert who helped the FBI capture him in the 1990s. The gift is a remarkable act of reconciliation between two former adversaries. This story transcends technical security news, illustrating the human capacity for forgiveness and the complex bonds within hacker culture. It also rekindles discussion about Mitnick’s enduring legacy as a controversial figure who inspired a generation of hackers. The car was a 1969 Chevrolet Camaro, a model Mitnick had long admired. Nunley, who had tracked Mitnick’s digital footprints and aided in his arrest, later became friends with Mitnick after his release, and the gift was a gesture of that unexpected friendship.

hackernews · mauvehaus · Jun 22, 18:03 · [Discussion](https://news.ycombinator.com/item?id=48633643)

**Background**: Kevin Mitnick was one of the most famous hackers of the 1980s and 1990s, known for social engineering and system intrusions. His high-profile pursuit by the FBI culminated in a 1995 arrest, after which he served prison time. He later reformed, becoming a security consultant, author, and public speaker. Shawn Nunley was a computer security expert who worked with law enforcement to track Mitnick down.

**Discussion**: Comments reflect a mix of nostalgia and critique. George Hotz and others praised Mitnick’s influence on their early hacking interests, while a former colleague criticized his consulting work as superficial. Many lamented his passing, remembering his books and lock-pick business cards, with suggestions for a film adaptation of his life.

**Tags**: `#hacking`, `#security`, `#Kevin Mitnick`, `#human-interest`, `#hacker culture`

---

<a id="item-16"></a>
## [A Test Harness for OPFS + Pyodide Persistent SQLite Editing in Datasette Lite](https://simonwillison.net/2026/Jun/23/opfs-pyodide/#atom-everything) ⭐️ 6.0/10

Simon Willison released a test harness at tools.simonwillison.net/opfs-pyodide to explore using Origin Private File System (OPFS) with Pyodide for persistent SQLite editing in Datasette Lite, the browser-based Python data exploration tool. This experiment could bring offline-capable, persistent data editing to browser-based Python tools like Datasette Lite, expanding the use cases for client-side WebAssembly applications without a server backend. The harness is a playground UI built with Claude Code for web, allowing users to test OPFS support across different browsers; OPFS is a sandboxed, origin-specific virtual filesystem optimized for performance.

rss · Simon Willison · Jun 23, 18:58

**Background**: Datasette Lite is a version of Datasette that runs entirely in the browser using Pyodide, a port of CPython to WebAssembly. Pyodide enables Python scripts and packages to run client-side. OPFS is a browser API that provides a fast, sandboxed filesystem private to each website origin. This test harness investigates whether these can be combined to edit SQLite databases stored in OPFS, making Datasette Lite capable of persistent data manipulation without a server.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system">Origin private file system - Web APIs | MDN</a></li>
<li><a href="https://pyodide.org/">Pyodide — Version 314.0.0</a></li>
<li><a href="https://lite.datasette.io/">Datasette</a></li>

</ul>
</details>

**Tags**: `#browsers`, `#pyodide`, `#datasette-lite`, `#sqlite`, `#webassembly`

---

<a id="item-17"></a>
## [Non-deterministic LLM Vulnerability Detection Benchmark Using Hidden Juliet Cases](https://www.reddit.com/r/MachineLearning/comments/1ud0rft/nondeterministic_vulnerability_detection/) ⭐️ 6.0/10

A partially completed benchmark system (80% done) hides Juliet CWE test cases within realistic codebases and injects misleading comments to evaluate how robustly LLMs detect vulnerabilities when faced with adversarial natural language manipulation. It addresses a critical blind spot: current LLM vulnerability detectors may over-rely on known code patterns and be easily thrown off by comment-based manipulation, so this benchmark offers a more realistic evaluation of robustness in security-critical code analysis. The benchmark uses the NIST Juliet test suite (over 81,000 synthetic programs with known flaws) and obfuscates them to remove LLMs' advantage of recognizing familiar CWE patterns. It injects accurate, neutral, or misleading comments to study adversarial influence, but work on presentation, actual LLM benchmarking, and pruning of some CWE cases that may still be recognized as Juliet code remains unfinished.

reddit · r/MachineLearning · /u/Psychological_Meat_6 · Jun 22, 23:34

**Background**: The Juliet Test Suite is a NIST-developed collection of synthetic C/C++ and Java programs with known flaws, widely used to evaluate static analysis tools. Mythos (Claude Mythos) is an AI-powered vulnerability scanner that recently found zero-days in critical open-source software, fueling interest in LLM-based vulnerability detection. This benchmark aims to test whether LLMs can detect vulnerabilities without relying on the artificial patterns of Juliet alone, and to examine how comments can manipulate detection.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nist.gov/publications/juliet-11-cc-and-java-test-suite">The Juliet 1.1 C/C++ and Java Test Suite | NIST</a></li>
<li><a href="https://venturebeat.com/security/mythos-detection-ceiling-security-teams-new-playbook">Mythos autonomously exploited vulnerabilities that survived 27 years of ...</a></li>

</ul>
</details>

**Tags**: `#vulnerability detection`, `#benchmark`, `#LLM robustness`, `#adversarial comments`, `#code analysis`

---