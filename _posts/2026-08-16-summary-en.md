---
layout: default
title: "Horizon Summary: 2026-08-16 (EN)"
date: 2026-08-16
lang: en
---

> From 30 items, 13 important content pieces were selected

---

1. [RISC-V Design Critique Sparks Debate on Microcontroller Suitability](#item-1) ⭐️ 8.0/10
2. [AI Codex Agent Auto-Optimizes GPU Kernel for 232x Speedup](#item-2) ⭐️ 8.0/10
3. [Ghost Characters Haunt Unicode: A Deep Dive into CJK Mysteries](#item-3) ⭐️ 8.0/10
4. [Working with AI feels more like leadership than coding](#item-4) ⭐️ 8.0/10
5. [BDH-CQ: 150M-Parameter Model Breaks Cost-Accuracy Pareto Frontier on ARC-AGI-1](#item-5) ⭐️ 8.0/10
6. [Doom Renderer Compiled into a 21B-Parameter Transformer with No Training](#item-6) ⭐️ 8.0/10
7. [Oncothresh: Open-Source Library and Dashboard for Evaluating Oncology AI at Clinical Decision Thresholds](#item-7) ⭐️ 8.0/10
8. [AI has access to a vastly larger working memory than the human brain](#item-8) ⭐️ 7.0/10
9. [LLM Hallucination Leveraged for Content Tagging via Vector Embeddings](#item-9) ⭐️ 7.0/10
10. [Survival of the Fitted: Qwen3.6-27B’s Jacobian lens reads and steers Qwen3.8-27B with zero refitting \[R\]](#item-10) ⭐️ 7.0/10
11. [Semaglutide Linked to Lower Predicted Dementia Risk, but Doubts Remain](#item-11) ⭐️ 6.0/10
12. [At-Home Lateral Flow Test for Ticks Aims to Improve Lyme Disease Diagnosis](#item-12) ⭐️ 6.0/10
13. [Abdominal Visceral Fat Better Predicts Heart Disease Risk Than BMI](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [RISC-V Design Critique Sparks Debate on Microcontroller Suitability](https://dmitry.gr/?r=06.%20Thoughts&amp;proj=12.%20RV) ⭐️ 8.0/10

Dmitry Grinberg published a detailed critique of RISC-V&\#x27;s instruction set architecture, highlighting design flaws that make it less suitable for simple microcontrollers, sparking intense discussion among engineers. The debate exposes the tension between RISC-V&\#x27;s open, extensible philosophy and the need for lean, efficient ISAs in cost-sensitive embedded systems, potentially influencing future extension standardization and adoption. The critique targets instruction encoding complexity, code density, and the burden of managing many optional extensions. Community members note that RISC-V&\#x27;s modularity, while a strength, can cause fragmentation and complications for basic microcontroller designs.

hackernews · dmitrygr · Aug 14, 12:50 · [Discussion](https://news.ycombinator.com/item?id=49298035)

**Background**: RISC-V is a free and open instruction set architecture developed at UC Berkeley in 2010 and now maintained by RISC-V International, a non-profit with over 4,500 members. Unlike proprietary ARM or x86 ISAs, it can be implemented royalty-free. It is built as a base integer set with optional extensions, allowing high customization but also introducing design complexity. It is widely used in microcontrollers, embedded systems, and increasingly in AI accelerators and custom chips.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V</a></li>
<li><a href="https://riscv.org/">Home - RISC-V International</a></li>

</ul>
</details>

**Discussion**: Comments show nuanced views: some see RISC-V&\#x27;s modularity as an unavoidable result of diverse industry needs, while others agree a simpler, curated subset would benefit microcontrollers. Success stories like Meta&\#x27;s AI accelerators and AMD&\#x27;s GPU controllers demonstrate practical value. Overall, RISC-V is seen as adequate but imperfect, with its extension model being a double-edged sword.

**Tags**: `#RISC-V`, `#ISA design`, `#embedded systems`, `#critique`, `#community discussion`

---

<a id="item-2"></a>
## [AI Codex Agent Auto-Optimizes GPU Kernel for 232x Speedup](https://sankalp.bearblog.dev/autoresearch/) ⭐️ 8.0/10

A blog post details using an AI codex agent to automatically research and optimize a GPU kernel, achieving a 232x speed improvement by iterating with profiling, verification, and code generation. This demonstrates AI&\#x27;s potential to automate complex performance optimization, but the community warns that such optimizations often overfit to specific inputs, lacking robustness without human expertise. The method generated 25,000 lines of CUDA code by exploring a vast search space. In a competition, 8 out of 10 top solutions using similar approaches broke on out-of-distribution inputs, while expert-tuned solutions remained robust.

hackernews · tosh · Aug 15, 11:00 · [Discussion](https://news.ycombinator.com/item?id=49309549)

**Background**: OpenAI Codex is an AI model that translates natural language to code, capable of generating and optimizing programs. A GPU kernel is a function executed on a GPU, often written in CUDA for parallel processing. Optimizing kernels is notoriously difficult due to hardware intricacies and memory hierarchies.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-codex/">Introducing Codex | OpenAI</a></li>
<li><a href="https://modal.com/gpu-glossary/device-software/kernel">What is a CUDA Kernel? | GPU Glossary</a></li>

</ul>
</details>

**Discussion**: Comments highlight that AI-driven optimization tends to overfit to specific benchmarks, and human expertise is crucial for verifying correctness. Some note the refreshing non-AI-generated writing, and speculate that GPU kernel training data is particularly rich in language models.

**Tags**: `#AI-assisted programming`, `#GPU optimization`, `#auto-research`, `#CUDA`, `#codex`

---

<a id="item-3"></a>
## [Ghost Characters Haunt Unicode: A Deep Dive into CJK Mysteries](https://www.dampfkraft.com/ghost-characters.html) ⭐️ 8.0/10

An in-depth article by Paul McCann investigates &\#x27;ghost&\#x27; characters in Unicode, particularly CJK ideographs, that were mistakenly included from historical Japanese character standards and have no verifiable meaning or origin. These ghost characters, permanently encoded into Unicode, highlight the tension between standardization accuracy and backward compatibility, and how small historical errors can have lasting consequences in global digital infrastructure. The character 彁 \(U+5F41\) is a prime example, likely originating from a misreading or poor scan of 彊 during the 1978 JIS standard creation. Because Unicode prioritizes round-trip compatibility, removing such characters is now almost impossible.

hackernews · sensanaty · Aug 15, 14:34 · [Discussion](https://news.ycombinator.com/item?id=49310926)

**Background**: Unicode is the universal text encoding standard that assigns a unique code point to every character across all writing systems. CJK unification merged the Chinese, Japanese, and Korean ideographs into a single set, but the process inherited errors from legacy national standards. Ghost characters are spurious entries with no known etymology or usage, often introduced by misprints, misreadings, or administrative mistakes in pre-digital character dictionaries.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ghost_characters">Ghost characters - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/CJK">CJK</a></li>

</ul>
</details>

**Discussion**: Commenters praised the author&\#x27;s expertise in Japanese NLP and noted that the character 彁 may have originated from a poorly scanned newspaper article. Others pointed out that the Kangxi dictionary is full of similar ghost characters, and that while superfluous characters are undesirable, they are preferable to missing real ones.

**Tags**: `#unicode`, `#cjk`, `#ghost-characters`, `#linguistics`, `#history`

---

<a id="item-4"></a>
## [Working with AI feels more like leadership than coding](https://allen.bargi.org/notes/working-with-ai-feels-like-leadership/) ⭐️ 8.0/10

A blog post argues that using AI coding assistants transforms the developer&\#x27;s role from coding to a leadership-like task, sparking a lively debate on Hacker News with 169 comments. This shift highlights the evolving skillset required for software engineers, potentially reducing the need for junior developers and altering hiring practices across the industry. Community members point out that managing AI is distinct from managing humans, requiring new skills to avoid pitfalls like blindly trusting AI-generated code, which can lead to project failures and technical debt.

hackernews · allenb · Aug 15, 10:39 · [Discussion](https://news.ycombinator.com/item?id=49309451)

**Background**: AI coding assistants \(e.g., GitHub Copilot, Claude\) are tools that generate code from natural language prompts. They are increasingly used by developers to accelerate coding tasks, but their output often requires careful review and guidance.

**Discussion**: The discussion is divided. Some experienced developers find AI amplifies their productivity, while others caution that treating AI as a human subordinate leads to technical bankruptcy. Many emphasize that this requires a distinct skill set, not just people management, and worry about the impact on junior developers entering the field.

**Tags**: `#AI`, `#software engineering`, `#management`, `#leadership`, `#coding assistants`

---

<a id="item-5"></a>
## [BDH-CQ: 150M-Parameter Model Breaks Cost-Accuracy Pareto Frontier on ARC-AGI-1](https://www.reddit.com/r/MachineLearning/comments/1vov5r5/bdhcq_incontext_learning_with_recurrent_latent/) ⭐️ 8.0/10

A 150M-parameter model called BDH-CQ uses recurrent latent reasoning to achieve 29.5% pass@2 on the ARC-AGI-1 benchmark at a cost of only $0.00070 per task, breaking the previously reported cost-accuracy Pareto frontier. This demonstrates that small models can perform complex reasoning tasks at extremely low cost by using iterative latent-space computation instead of generating verbose chain-of-thought tokens, potentially enabling efficient reasoning in resource-constrained applications. The model&\#x27;s recurrent memory is updated continuously during inference using task demonstrations, and the query is solved through iterative computation in a high-dimensional latent space without verbalizing intermediate steps. No task identifiers or evaluation-task demonstration pairs are used in training, and no parameters are updated at inference time.

reddit · r/MachineLearning · /u/moschles · Aug 15, 06:18

**Background**: ARC-AGI-1 is a reasoning benchmark that measures a model&\#x27;s ability to solve abstract visual puzzles. The Pareto frontier represents the trade-off between two objectives—here, cost and accuracy—where a solution is Pareto-optimal if no other solution achieves better accuracy at equal or lower cost. BDH-CQ&\#x27;s approach of recurrent latent reasoning allows the model to adapt to new tasks via in-context learning without gradient updates, iterating in a continuous latent space rather than generating discrete tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.09888v1">BDH-CQ: In-Context Learning with Recurrent Latent Reasoning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pareto_frontier">Pareto frontier</a></li>

</ul>
</details>

**Tags**: `#in-context learning`, `#latent reasoning`, `#ARC-AGI`, `#recurrent neural networks`, `#cost-efficiency`

---

<a id="item-6"></a>
## [Doom Renderer Compiled into a 21B-Parameter Transformer with No Training](https://www.reddit.com/r/MachineLearning/comments/1voazhm/i_compiled_dooms_renderer_into_a_21bparameter/) ⭐️ 8.0/10

A developer ported Doom&\#x27;s rendering algorithm into a 21B-parameter transformer by compiling the computation graph directly into model weights, eliminating the need for any training. The model receives a scene description as a prompt and autoregressively generates tokens representing pixel-drawing commands that produce a rendered frame. This project showcases how deterministic algorithms can be embedded directly into transformer weights, enabling the model to execute precise computations like rendering without training. It hints at a future where AI models combine probabilistic inference with exact program execution internally, potentially reducing reliance on external tools. The 21B-parameter transformer is a standard Hugging Face checkpoint, requiring no custom code. Rendering a single E1M1 frame involves a 3,614-token prompt and 53,747 output tokens, taking 40 minutes on an NVIDIA B200 GPU \(35 frames per day vs. original 35 FPS on a 486\). The entire inference host code is just 43 lines of Python.

reddit · r/MachineLearning · /u/notforrob · Aug 14, 15:50

**Background**: The Doom rendering engine is a classic software renderer that uses Binary Space Partitioning \(BSP\) to draw walls, floors, and sprites from a 2D map, achieving 3D-like visuals. A computation graph represents a mathematical expression as a directed graph of operations, which is the foundation of deep learning frameworks like PyTorch. The idea of compiling programs into transformer weights has been explored in recent projects, where a computation graph is translated into fixed attention and feedforward layers, allowing the model to execute a specific algorithm step-by-step during autoregressive generation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/deep-learning/computational-graphs-in-deep-learning/">Computational Graphs in Deep Learning - GeeksforGeeks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Doom_engine">Doom engine - Wikipedia</a></li>
<li><a href="https://towardsdatascience.com/i-built-a-tiny-computer-inside-a-transformer/">I Built a Tiny Computer Inside a Transformer | Towards Data ...</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#compilation`, `#graphics`, `#machine-learning`, `#novelty`

---

<a id="item-7"></a>
## [Oncothresh: Open-Source Library and Dashboard for Evaluating Oncology AI at Clinical Decision Thresholds](https://www.reddit.com/r/MachineLearning/comments/1vod2c8/opensource_python_library_nocode_web_dashboard/) ⭐️ 8.0/10

A new open-source Python library, oncothresh, and a companion no-code web dashboard have been released. They evaluate oncology AI models at specific clinical decision thresholds, providing sensitivity, specificity, PPV, NPV, bootstrap confidence intervals, and decision-curve net benefit at the chosen cutoff. Most oncology AI models are evaluated with global metrics like AUC, which ignore performance at the exact clinical cutoff where a patient is flagged for biopsy or treatment. This tool fills a critical gap by enabling clinicians and researchers to assess model reliability at the decision point, improving real-world clinical decision-making. The library is dependency-light \(numpy, scipy, scikit-learn, pydantic\) and includes boundary-weighted calibration and threshold-sensitivity curves. The dashboard allows uploading a CSV of predictions and labels, selecting a threshold, and generating charts with a downloadable PDF report, all running locally via Docker.

reddit · r/MachineLearning · /u/adom2989 · Aug 14, 17:06

**Background**: In oncology, AI models often output continuous scores \(e.g., tumor cellularity, Ki-67 index, TMB, PD-L1 expression\) that are dichotomized at a predefined clinical cutoff to decide on biopsy, treatment, or flagging. Traditional metrics like AUC measure overall ranking ability but not performance at that critical threshold. Decision curve analysis quantifies net benefit across threshold probabilities, and benchmarks like PathBench evaluate pathology foundation models globally, but do not provide threshold-specific uncertainty quantification.

<details><summary>References</summary>
<ul>
<li><a href="https://atm.amegroups.org/article/view/20389/html">Decision curve analysis: a technical note - Zhang - Annals of...</a></li>
<li><a href="https://github.com/scikit-learn/scikit-learn/issues/22136">Net benefit curve and decision curve analysis · Issue #22136...</a></li>
<li><a href="http://birkhoffkiki.github.io/PathBench/">PathBench : A compensive benchmark for pathology foundation...</a></li>

</ul>
</details>

**Tags**: `#oncology`, `#machine learning`, `#model evaluation`, `#clinical decision thresholds`, `#open-source`

---

<a id="item-8"></a>
## [AI has access to a vastly larger working memory than the human brain](https://davidepiffer.com/p/ai-isnt-outthinking-mathematicians) ⭐️ 7.0/10

The article argues that AI&\#x27;s advantage in mathematics comes not from superior reasoning but from its vastly larger working memory and relentless persistence, enabling brute-force exploration that human mathematicians cannot sustain. Community comments further emphasize that AI can publish and reuse negative results, a practice humans find difficult. This perspective challenges the common belief that AI surpasses humans through raw intelligence, reframing success as a combination of memory and stamina. It has implications for how we design AI systems and collaborate with them in research. The discussion highlights that human mathematicians are incentivized to publish only positive results, while AI agents can systematically explore and document negative findings. AI&\#x27;s unlimited &\#x27;mental energy&\#x27; allows it to tackle problems without fatigue or discouragement.

hackernews · rzk · Aug 15, 18:13 · [Discussion](https://news.ycombinator.com/item?id=49312845)

**Background**: Human working memory has a limited capacity, typically holding only a few items at once, while large language models can process context windows of hundreds of thousands of tokens, effectively acting as a massive working memory. This cognitive science concept is central to understanding why AI can brute-force through many research paths that a human would find exhausting.

**Discussion**: Commenters broadly agree that AI&\#x27;s edge is akin to tireless memory retrieval and brute-force search. Some note that human high performance often boils down to superior memory, while others highlight AI&\#x27;s ability to publish negative results as a game-changer. A reference to Michael Nielsen&\#x27;s essay on memory augmentation reinforces the idea that memory is a foundational component of intelligence.

**Tags**: `#artificial-intelligence`, `#working-memory`, `#cognitive-science`, `#mathematics`, `#hackernews-discussion`

---

<a id="item-9"></a>
## [LLM Hallucination Leveraged for Content Tagging via Vector Embeddings](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 7.0/10

Simon Willison highlights a technique from Doug Turnbull that instructs an LLM to generate novel, never-before-seen tag suggestions without seeing the existing tag vocabulary, then uses vector embeddings to find the closest matching existing tags. This approach elegantly solves the content tagging problem for large, dynamic tag sets, avoiding the need to feed all tags to an LLM and leveraging the creative, generative strengths of LLMs combined with the semantic matching of vector embeddings. The prompt asks the LLM to create novel, never-before-seen classifications, with examples of the tag shape to guide the generation; then vector similarity search matches the imagined tags to the real tag corpus.

rss · Simon Willison · Aug 14, 21:54

**Background**: LLM hallucination is usually considered a problem where models generate false information, but here it is deliberately used to invent novel tags. Vector embeddings are dense numerical representations of text that capture semantic meaning, enabling similarity search to find the most relevant existing tags.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vector_embedding">Vector embedding</a></li>
<li><a href="https://en.wikipedia.org/wiki/LLM_hallucination">LLM hallucination</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#embeddings`, `#tagging`, `#vector search`, `#content classification`

---

<a id="item-10"></a>
## [Survival of the Fitted: Qwen3.6-27B’s Jacobian lens reads and steers Qwen3.8-27B with zero refitting \[R\]](https://www.reddit.com/r/MachineLearning/comments/1vpa5cv/survival_of_the_fitted_qwen3627bs_jacobian_lens/) ⭐️ 7.0/10

A Jacobian lens trained on Qwen3.6-27B is shown to effectively read and steer the later Qwen3.8-27B without any refitting, indicating that such interpretability instruments can survive minor architectural updates.

reddit · r/MachineLearning · /u/imstilllearningthis · Aug 15, 18:24

**Tags**: `#interpretability`, `#Jacobian lens`, `#model steering`, `#Qwen`, `#transfer learning`

---

<a id="item-11"></a>
## [Semaglutide Linked to Lower Predicted Dementia Risk, but Doubts Remain](https://alz-journals.onlinelibrary.wiley.com/doi/10.1002/dad2.70432) ⭐️ 6.0/10

A study funded by Novo Nordisk reports that semaglutide use is associated with a lower predicted dementia risk based on a biomarker, rather than actual dementia diagnoses. Previous dedicated clinical trials for Alzheimer&\#x27;s disease failed to show cognitive benefits. If semaglutide genuinely reduces dementia risk, it could offer a new preventive strategy for a devastating condition with no cure. However, the reliance on a predictive biomarker and industry funding raises concerns about the validity of the findings. The study used a predictive biomarker—similar to a &\#x27;check engine&\#x27; light—not actual dementia outcomes. Critics note that Novo Nordisk&\#x27;s dedicated Alzheimer&\#x27;s trials failed, and the observed association may be confounded by weight loss or other factors.

hackernews · randycupertino · Aug 15, 15:58 · [Discussion](https://news.ycombinator.com/item?id=49311651)

**Background**: Semaglutide is a GLP-1 receptor agonist approved for type 2 diabetes and weight management. Predictive biomarkers measure biological signals that indicate future risk but do not confirm disease. Confounding variables, such as weight loss improving metabolic health, can distort associations in observational studies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Semaglutide">Semaglutide</a></li>
<li><a href="https://en.wikipedia.org/wiki/Predictive_biomarker">Predictive biomarker</a></li>
<li><a href="https://en.wikipedia.org/wiki/Confounding_variable">Confounding variable</a></li>

</ul>
</details>

**Discussion**: Commenters express skepticism, highlighting the study&\#x27;s industry funding and reliance on a biomarker instead of real-world dementia cases. They question whether the effect is due to weight loss rather than the drug itself, and some share personal experiences of side effects from semaglutide.

**Tags**: `#semaglutide`, `#dementia`, `#clinical-trials`, `#pharma-funding`, `#predictive-biomarkers`

---

<a id="item-12"></a>
## [At-Home Lateral Flow Test for Ticks Aims to Improve Lyme Disease Diagnosis](https://www.smithsonianmag.com/innovation/the-first-at-home-test-for-infected-ticks-could-improve-lyme-disease-diagnosis-180989235/) ⭐️ 6.0/10

A new at-home lateral flow test, LymeAlert, allows individuals to check a tick for the Borrelia burgdorferi pathogen after a bite, claiming lab-level accuracy without requiring specialized equipment. This could enable faster decision-making about whether to seek antibiotic treatment after a tick bite, potentially reducing unnecessary antibiotic use and improving early Lyme disease management, especially in areas with rising tick populations. The test uses lateral flow technology, which generally has a lower limit of detection than PCR-based lab tests, and it has not been cleared by the FDA; its accuracy claims remain unverified by public health authorities.

hackernews · gmays · Aug 15, 14:04 · [Discussion](https://news.ycombinator.com/item?id=49310682)

**Background**: Lateral flow tests are simple, paper-based devices that detect target substances using antibody-antigen reactions, commonly used for home pregnancy tests and rapid COVID-19 tests. Lyme disease is a tick-borne illness caused by the bacterium Borrelia burgdorferi, which can lead to serious neurological and joint complications if untreated. Current lab-based tick testing relies on PCR to amplify pathogen DNA, offering high sensitivity. Home tick tests are not subject to FDA medical device regulations, so manufacturers can market them without premarket review.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lateral_flow_test">Lateral flow test</a></li>

</ul>
</details>

**Discussion**: Community members expressed skepticism about the test&\#x27;s accuracy, noting that lateral flow tests have much lower sensitivity than PCR, and that the lack of FDA clearance raises concerns about unverified claims. Some highlighted the overdiagnosis of Lyme disease in online patient communities, while others saw potential value in raising awareness, especially in emerging risk zones like the UK.

**Tags**: `#Lyme disease`, `#at-home testing`, `#lateral flow`, `#public health`, `#tick-borne illness`

---

<a id="item-13"></a>
## [Abdominal Visceral Fat Better Predicts Heart Disease Risk Than BMI](https://www.acc.org/about-acc/press-releases/2026/08/11/14/59/abdominal-fat-predicts-heart-disease-risk-better-than-bmi) ⭐️ 6.0/10

A new study confirms that visceral abdominal fat, the fat surrounding internal organs, is a stronger predictor of heart disease risk than body mass index \(BMI\). This finding could prompt a shift in cardiovascular risk assessment toward more precise body composition metrics, potentially improving early detection and prevention strategies. The research distinguishes between visceral fat and subcutaneous fat; only visceral fat is strongly linked to adverse heart outcomes. However, measuring visceral fat typically requires CT scans or MRI, which are less accessible than BMI.

hackernews · theanonymousone · Aug 15, 21:14 · [Discussion](https://news.ycombinator.com/item?id=49314403)

**Background**: BMI is a widely used measure of body fat based on height and weight, but it does not reflect fat distribution. Visceral fat, located deep in the abdomen, secretes inflammatory substances and contributes to insulin resistance and atherosclerosis. Previous studies have already suggested its greater role in metabolic disease, but this research reinforces its predictive power for heart disease specifically.

**Discussion**: Community comments largely agreed that the finding isn&\#x27;t new, noting that visceral fat has long been recognized as more harmful. Several users pointed out that BMI is still used because it&\#x27;s easy to measure, while visceral fat assessment requires expensive imaging. Others highlighted alternative prediction methods like ECG and dietary interventions such as resistant starch, and criticized professional associations for not adopting more accurate risk models.

**Tags**: `#health`, `#medical research`, `#heart disease`, `#BMI`, `#abdominal fat`

---