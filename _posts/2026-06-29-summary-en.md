---
layout: default
title: "Horizon Summary: 2026-06-29 (EN)"
date: 2026-06-29
lang: en
---

> From 26 items, 13 important content pieces were selected

---

1. [Brown University Professor Exposes Mass AI Cheating on Exam](#item-1) ⭐️ 8.0/10
2. [I used Claude Code to get a second opinion on my MRI](#item-2) ⭐️ 8.0/10
3. [GLM 5.2 Outperforms Claude on Semgrep’s Cybersecurity Benchmarks](#item-3) ⭐️ 7.0/10
4. [Librepods: Open-Source Project Unlocks Full AirPods Features on Non-Apple Devices](#item-4) ⭐️ 7.0/10
5. [Jon Udell Proposes 'Agent in the Loop' over 'Human in the Loop'](#item-5) ⭐️ 7.0/10
6. [Interactive Tiny Transformer with Editable Weights Demystifies LLM Internals](#item-6) ⭐️ 7.0/10
7. [MathFormer: 4M-Parameter Model Tests Symbolic Math Pattern Matching](#item-7) ⭐️ 7.0/10
8. [NagaTranslate: Translation and voice pipeline for low-resource Nagaland creoles](#item-8) ⭐️ 7.0/10
9. [Historical memory prices 1960-2026](#item-9) ⭐️ 6.0/10
10. [A curated exploration of 5,000 historical menus from NYPL’s Buttolph Collection (1880–1920)](#item-10) ⭐️ 6.0/10
11. [Hiding Messages in the Least Significant Mantissa Bits of Fine-Tuned ONNX Model Weights](#item-11) ⭐️ 6.0/10
12. [pybench: A pytest-style tool for statistical benchmark regression testing](#item-12) ⭐️ 6.0/10
13. [ML System Detects MMA Fight Events for Searchable Timeline](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Brown University Professor Exposes Mass AI Cheating on Exam](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html) ⭐️ 8.0/10

A professor at Brown University publicly denounced a mass AI fraud incident where students used AI tools to cheat on an exam, sparking a broad debate on academic integrity and assessment design. The incident underscores the urgent need for educational institutions to adapt assessment methods in the AI era, as traditional exams become vulnerable to AI-assisted cheating, threatening the value of academic credentials. The professor, whose research is in game theory, highlighted the incident at Brown University, with community responses noting that similar cheating problems are rampant in computer science departments and advocating for adversarial assignment design that raises the cognitive cost of using LLMs.

hackernews · geox · Jun 28, 16:41 · [Discussion](https://news.ycombinator.com/item?id=48708991)

**Background**: Adversarial assignment design is an approach that intentionally adds friction and cognitive overhead to assignments, making it harder for students to use AI tools like ChatGPT without genuine understanding. This concept has gained traction as educators seek to preserve academic integrity in the face of advanced language models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/adversarial-assignment-design-carl-james-grindley-rvupe">Adversarial Assignment Design - LinkedIn</a></li>

</ul>
</details>

**Discussion**: The discussion featured diverse perspectives: some advocated for in-person handwritten exams and 1-on-1 interviews to verify understanding, while others questioned the value of grading entirely, suggesting that credentials should be determined by employers. A game theory researcher noted the irony of the situation, and there was strong consensus on the need for adversarial course design.

**Tags**: `#AI`, `#education`, `#academic integrity`, `#cheating`, `#assessment`

---

<a id="item-2"></a>
## [I used Claude Code to get a second opinion on my MRI](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

A person used Claude Code, an AI model, to analyze their own MRI scan as a second opinion, leading to a detailed discussion about AI's potential and limitations in medical diagnosis. This experiment highlights the growing interest in using AI for medical second opinions, raising questions about trust, accuracy, and the relationship between patients and experts, and reflects broader trends of AI in healthcare. The experiment used Claude Code (likely Claude Opus, a multimodal large language model) to analyze MRI images, but was a personal anecdote rather than a clinical study. A radiologist in the comments noted that full 3D data is needed for proper assessment and that ultrasound is not ideal for detecting calcification.

hackernews · engmarketer · Jun 28, 16:35 · [Discussion](https://news.ycombinator.com/item?id=48708941)

**Background**: Claude is a series of large language models developed by Anthropic, with multimodal capabilities to process text and images. Opus is the most capable variant. Claude Code is a tool that allows interacting with the model via terminal, IDE, and other interfaces, and was used in this non-medical-grade experiment to obtain an AI-generated interpretation of medical imaging.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Discussion**: The discussion includes a radiologist emphasizing the need for 3D data, a user reflecting on the emotional comfort of trust in experts versus AI, a story of a misdiagnosis leading to forced hospitalization, and a debate on the deterministic expectations of diagnosis. Sentiment is mixed, with some seeing AI as a helpful second pair of eyes and others cautioning against over-reliance without expert oversight.

**Tags**: `#AI`, `#medical-imaging`, `#healthcare`, `#second-opinion`, `#claude`

---

<a id="item-3"></a>
## [GLM 5.2 Outperforms Claude on Semgrep’s Cybersecurity Benchmarks](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 7.0/10

Semgrep's cybersecurity benchmarks show that the open-source model GLM 5.2 outperforms Claude in finding security bugs. However, community comments reveal that other benchmarks yield mixed results, and the model is praised for its cost-effectiveness as a daily programming assistant. This marks a significant moment where an open-source Chinese LLM achieves competitive or superior performance in a specialized cybersecurity task against a leading proprietary model, potentially democratizing advanced security tooling. The cost advantage is especially impactful for heavy LLM users who can save hundreds of dollars per session. GLM 5.2 is a 753B-parameter model released under the MIT license with a 1M-token context window and effort level control, developed by the Chinese company Z.ai (formerly Zhipu AI). It is notably slower than some alternatives, and community benchmarks show that DeepSeek V4 Pro often performs better in security bug hunting, while MiMo 2.5 Pro's results were inconsistent.

hackernews · jms703 · Jun 28, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48709670)

**Background**: Semgrep is an open-source static analysis tool used for detecting security vulnerabilities and bugs in code through semantic pattern matching. GLM, or General Language Model, is a family of large language models from Z.ai, a Chinese AI company that was blacklisted by the U.S. in 2025. The benchmark tested models on their ability to find security issues, including those that Mythos, a prior system, had discovered. GLM 5.2 is designed for long-horizon coding tasks and is notable for being fully open-source under the MIT license.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Semgrep">Semgrep</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.2">GLM 5.2</a></li>
<li><a href="https://z.ai/blog/glm-5.2">GLM-5.2: Built for Long-Horizon Tasks</a></li>

</ul>
</details>

**Discussion**: Community members presented mixed results: some found GLM 5.2 slightly worse than Claude Opus 4.8 but 5x cheaper and 3x slower; others noted that DeepSeek V4 Pro consistently outperformed it in security bug hunting, while MiMo 2.5 Pro's performance was inconsistent. Many praised GLM 5.2 as a cost-effective 'workhorse' for daily programming, with one user spending only $20 over a weekend compared to $100+ with GPT-5.6. Some expressed optimism about Chinese models surpassing U.S. ones in cybersecurity, particularly due to lower training costs and self-training capabilities.

**Tags**: `#LLM`, `#benchmark`, `#cybersecurity`, `#open-source`, `#AI`

---

<a id="item-4"></a>
## [Librepods: Open-Source Project Unlocks Full AirPods Features on Non-Apple Devices](https://github.com/librepods-org/librepods) ⭐️ 7.0/10

Librepods is a new open-source project that reverse-engineers Apple's proprietary AirPods features, such as noise control modes and ear detection, enabling them to work fully on non-Apple devices like Android and Windows. This project allows users to access premium AirPods features without being locked into Apple's ecosystem, potentially increasing the value of AirPods for a wider audience and challenging Apple's hardware-software integration strategy. The project currently implements features like noise control modes, adaptive transparency, and ear detection via a companion app, but it may be vulnerable to future Apple firmware updates that could break compatibility.

hackernews · rbanffy · Jun 28, 18:48 · [Discussion](https://news.ycombinator.com/item?id=48710232)

**Background**: AirPods are Apple's wireless earbuds with proprietary features that only work seamlessly with Apple devices. While they can function as standard Bluetooth earbuds on other devices, advanced features like active noise cancellation switching and automatic ear detection are typically unavailable outside Apple's ecosystem. Reverse engineering involves analyzing the communication protocols to replicate these features on other platforms. This has been attempted before, as seen in projects like OpenDrop for AirDrop.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/librepods-org/librepods">GitHub - librepods -org/ librepods : AirPods liberated from...</a></li>
<li><a href="https://alternativeto.net/software/librepods/about/">LibrePods : Unlocks AirPods features on any device... | AlternativeTo</a></li>

</ul>
</details>

**Discussion**: Community members expressed cautious optimism, noting that while AirPods already function as standard Bluetooth earbuds, unlocking extra features is valuable. Some worry that Apple may patch the exploit, and hope for similar projects for other Apple-exclusive features like AirDrop.

**Tags**: `#open-source`, `#reverse-engineering`, `#airpods`, `#bluetooth`, `#apple`

---

<a id="item-5"></a>
## [Jon Udell Proposes 'Agent in the Loop' over 'Human in the Loop'](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 7.0/10

Jon Udell, in a blog post quoted by Simon Willison, criticizes the phrase 'human in the loop' for ceding authority to machines. He proposes flipping the narrative to 'agent in the loop,' where developers invite AI agents into their own workflow, maintaining control and transparency. This reframing shifts the power dynamic in AI-assisted development, emphasizing that developers retain authority and transparency. It could influence how teams adopt AI coding agents, encouraging them to treat these tools as controllable collaborators integrated into existing workflows rather than autonomous black boxes. Udell's original post addresses the problem of 'unreviewable PRs' generated by agents, advocating for transparent, reviewable processes. The 'agent in the loop' metaphor is a conceptual shift, not a technical fix, but it encourages developers to design workflows that avoid opaque agent outputs.

rss · Simon Willison · Jun 28, 21:57

**Background**: The phrase 'human in the loop' (HITL) is commonly used in AI to describe systems where humans provide oversight or intervention. 'Agentic coding' refers to autonomous AI agents that can plan, write, test, and modify code. Udell's proposal flips the narrative, suggesting that developers should invite AI agents into their own human-driven development loop, rather than inserting humans into an AI-centric loop.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/agent-loop-mona-borham-nze0e">Agent in the Loop</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-engineering">What is agentic engineering? - IBM</a></li>

</ul>
</details>

**Tags**: `#ai-agents`, `#software-development`, `#human-in-the-loop`, `#coding-agents`, `#best-practices`

---

<a id="item-6"></a>
## [Interactive Tiny Transformer with Editable Weights Demystifies LLM Internals](https://www.reddit.com/r/MachineLearning/comments/1uhw7fu/i_shrank_a_transformer_until_every_number_fitted/) ⭐️ 7.0/10

A software engineer built a self-contained HTML page that implements a complete forward pass of a minimal transformer (6-word vocabulary, 3-dimensional embeddings, single attention head) and allows users to edit weights live, seeing real-time prediction changes to demystify the internal mechanics. This tool makes the complex matrix operations of transformers tangible, lowering the learning barrier for students and practitioners and bridging the gap between abstract theory and hands-on understanding of how large language models actually work. The tool walks through the entire forward pass: word vectors, Q/K/V, attention scores, causal mask, softmax, feed-forward network, logits, and final probabilities. Randomizing weights immediately turns predictions to nonsense, highlighting the crucial role of training. It is a single dependency-free HTML file.

reddit · r/MachineLearning · /u/DanielMoGo · Jun 28, 12:35

**Background**: Transformers are a neural network architecture based on self-attention, widely used in modern large language models. The forward pass is the computation from input tokens to output predictions. The attention mechanism allows the model to weigh the importance of different tokens, and a causal mask ensures each prediction only depends on previous tokens, preventing information leakage from future tokens. Logits are raw scores output by the model, and softmax converts them into a probability distribution over the vocabulary. Editing weights live in this tool helps illustrate how training shapes the model's behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://machinelearningmastery.com/a-gentle-introduction-to-attention-masking-in-transformer-models/">A Gentle Introduction to Attention Masking in Transformer Models</a></li>
<li><a href="https://learn.deeplearning.ai/courses/attention-in-transformers-concepts-and-code-in-pytorch/lesson/h6tni/multi-head-attention">Attention in Transformers: Concepts and Code in... - DeepLearning.AI</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#transformers`, `#education`, `#visualization`, `#explainability`

---

<a id="item-7"></a>
## [MathFormer: 4M-Parameter Model Tests Symbolic Math Pattern Matching](https://www.reddit.com/r/MachineLearning/comments/1uhatw8/mathformer_testing_whether_symbolic_math_is/) ⭐️ 7.0/10

A tiny seq2seq model with 4 million parameters, trained without any mathematical knowledge, achieves 98.6% accuracy on expanding factorized symbolic expressions, indicating that it learns structural token transformations rather than mathematical reasoning. This finding supports the hypothesis that large language models’ apparent reasoning may be largely pattern matching, which could reshape how we evaluate and build AI systems for complex tasks. The model is a 4M-parameter seq2seq transformer trained on pairs like (7-3*z)*(-5*z-9) → 15*z^2-8*z-63. The near-perfect accuracy suggests it captures token-level structural transformations without any operator or variable semantics.

reddit · r/MachineLearning · /u/AlphaCode1 · Jun 27, 18:57

**Background**: Symbolic mathematics involves exact manipulation of expressions as symbols, unlike numerical computation. Computer algebra systems are designed for such tasks. The debate about whether neural networks can truly reason or just pattern-match is central to AI research. This experiment uses polynomial expansion, a basic symbolic operation, to probe whether a minimal model can succeed without inherent understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Symbolic_math">Symbolic math</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#reasoning`, `#transformers`, `#symbolic math`, `#pattern matching`

---

<a id="item-8"></a>
## [NagaTranslate: Translation and voice pipeline for low-resource Nagaland creoles](https://www.reddit.com/r/MachineLearning/comments/1uhlvjv/nagatranslate_building_a_translation_and_voice/) ⭐️ 7.0/10

A developer shared the architecture of NagaTranslate, a pipeline that uses a commercial LLM API for translation, fine-tuned Whisper for automatic speech recognition, and fine-tuned VITS for text-to-speech, targeting the low-resource Nagaland creoles Nagamese, Ao, and Sema. The project tackles low-resource NLP for predominantly oral languages with very little standardized parallel data, providing a practical blueprint for similar efforts to digitize underserved languages. The translation backend initially used a fine-tuned NLLB model but switched to a commercial LLM API for better colloquial flow; the long-term goal is to self-host lightweight open-weights models. Key challenges include non-standardized spelling, regional accent variations, and GPU hosting costs.

reddit · r/MachineLearning · /u/Material_Dinner_1924 · Jun 28, 03:05

**Background**: Whisper is an OpenAI open-source speech recognition model based on transformer architecture, known for robustness to accents and noise. VITS is an end-to-end text-to-speech model combining a variational autoencoder with adversarial training. NLLB (No Language Left Behind) is Meta's multilingual translation model that supports many underserved languages. Nagaland's creoles like Nagamese are primarily oral, with limited standardized text corpora, making low-resource NLP especially difficult.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system)">Whisper (speech recognition system)</a></li>
<li><a href="https://huggingface.co/docs/transformers/model_doc/vits">VITS · Hugging Face</a></li>
<li><a href="https://huggingface.co/facebook/nllb-200-3.3B">facebook/ nllb -200-3.3B · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#low-resource NLP`, `#machine translation`, `#speech synthesis`, `#language models`, `#project showcase`

---

<a id="item-9"></a>
## [Historical memory prices 1960-2026](https://dam.stanford.edu/memory-prices.html) ⭐️ 6.0/10

A visualization from Stanford's DAM project shows the price of memory per gigabyte from 1960 to 2026, accompanied by discussion on inflation, technological nostalgia, and AI's potential impact on future prices. The chart illustrates the dramatic long-term decline in memory costs, but also recent volatility and the potential for AI-driven demand spikes, which could affect hardware costs and industry planning. The prices are not adjusted for inflation, and per-GB pricing before 1990 is anachronistic. The curve flattens in the 2010s, coinciding with the end of Moore's law, and recent volatility is attributed to crypto and AI booms.

hackernews · vga1 · Jun 28, 18:32 · [Discussion](https://news.ycombinator.com/item?id=48710092)

**Background**: Memory prices historically fell exponentially due to Moore's law and manufacturing advances. Since the 2010s, the decline slowed as physical limits were reached. The chart visualizes this trend, while the discussion notes that inflation adjustment would make early prices appear even steeper, and that the shift to gigabyte-scale thinking is a modern lens. The recent AI boom has spiked demand for high-bandwidth memory (HBM), causing supply constraints and price increases, which could disrupt the long-term downward trend.

**Discussion**: Commenters shared nostalgic memories of expensive RAM in the past and debated the lack of inflation adjustment. Some noted that modern software is more memory-hungry, while others pointed to AI and crypto as causes of recent price volatility. The flattening curve in the 2010s was seen as evidence of Moore's law ending, and speculation arose that high AI demand might eventually justify increased production capacity, potentially lowering prices in the long term.

**Tags**: `#hardware`, `#memory`, `#history`, `#economics`, `#data-visualization`

---

<a id="item-10"></a>
## [A curated exploration of 5,000 historical menus from NYPL’s Buttolph Collection (1880–1920)](https://pudding.cool/2026/06/menu-story/) ⭐️ 6.0/10

The Pudding published an interactive visual essay that explores 5,000 digitized historical menus from the New York Public Library’s Buttolph Collection, spanning 1880 to 1920, revealing evolving culinary trends and design aesthetics. This project demonstrates how data visualization can make cultural heritage engaging and accessible, sparking public interest in food history, design evolution, and digital humanities. The visualization includes a curated narrative story and a browsable menu interface, allowing users to explore categories like 'Boiled' and observe design patterns; the menus were originally collected by Frank E. Buttolph and digitized by the NYPL.

hackernews · xbryanx · Jun 28, 14:44 · [Discussion](https://news.ycombinator.com/item?id=48707763)

**Background**: The Buttolph Collection is a renowned archive of over 25,000 historical menus at the New York Public Library, assembled by Frank E. Buttolph in the early 20th century. The Pudding is a digital publication that creates data-driven visual essays on culture and society.

**Discussion**: Comments were highly positive, with readers sharing personal anecdotes: one noted German beer mat tallying has legal weight, another praised the nostalgic aesthetics of NYC Chinese takeout menus, and a foodie observed the early prevalence of 'Boiled' dishes. A detailed comment highlighted celery’s historical status as a luxury item, explaining why it appeared prominently on these menus.

**Tags**: `#data visualization`, `#food history`, `#cultural history`, `#historical menus`, `#digital humanities`

---

<a id="item-11"></a>
## [Hiding Messages in the Least Significant Mantissa Bits of Fine-Tuned ONNX Model Weights](https://www.reddit.com/r/MachineLearning/comments/1uh61uw/hiding_messages_in_the_least_significant_mantissa/) ⭐️ 6.0/10

A Reddit user shared a project that embeds hidden messages into the least significant bits of the mantissa of floating-point weights in ONNX models, specifically targeting only those weights that are altered during fine-tuning to make the modifications appear natural. This technique could enable covert data embedding for watermarking or secret communication in ML models, while evading simple detection methods that compare a model against a reference. It highlights a potential security and privacy concern in model distribution. The approach capitalizes on the fact that fine-tuning already changes many weights, so modifying the least significant mantissa bits in those altered weights adds minimal detectable anomaly. However, the author notes that advanced statistical analysis could still reveal hidden data, and the data capacity is very limited. The project is a closed prototype, not a production tool, and the author acknowledges that similar concepts exist in academic literature.

reddit · r/MachineLearning · /u/Admin-ABC-XYZ · Jun 27, 15:45

**Background**: ONNX (Open Neural Network Exchange) is an open standard for representing machine learning models, enabling interoperability. Floating-point numbers are composed of a sign, exponent, and mantissa (significand); the least significant bits of the mantissa carry the smallest numerical weight. LSB steganography is a classic technique that hides data in the least significant bits of digital content (e.g., image pixels) because altering them causes minimal perceptual change. In this project, the same principle is applied to model weights: by modifying only the LSBs of the mantissa in weights that are already updated during fine-tuning, the hidden message blends into the normal noise of the training process.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open_Neural_Network_Exchange">Open Neural Network Exchange - Wikipedia</a></li>
<li><a href="https://medium.com/@renantkn/lsb-steganography-hiding-a-message-in-the-pixels-of-an-image-4722a8567046">LSB Steganography — Hiding a message in the pixels of an... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Floating-point_arithmetic">Floating-point arithmetic - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#steganography`, `#machine learning`, `#ONNX`, `#model security`, `#least significant bits`

---

<a id="item-12"></a>
## [pybench: A pytest-style tool for statistical benchmark regression testing](https://www.reddit.com/r/MachineLearning/comments/1ugv7u3/i_silently_break_training_codes_or_configs_so_i/) ⭐️ 6.0/10

A new Python tool called pybench has been released, which applies pytest-like testing to statistical benchmarks. It manages seeds and past results to detect regressions in training metrics at a statistical level. This tool fills a niche for machine learning practitioners who need to ensure that code changes do not inadvertently degrade model performance metrics. It provides a systematic way to catch statistical regressions, which are often subtle and hard to detect manually. pybench works like pytest: it uses a benchmarks/ directory, saves a baseline on first run, and on subsequent runs, marks results as PASS or FAIL based on statistical comparison. The CLI includes commands like pybench update to re-baseline after intentional changes and pybench show to view current stats.

reddit · r/MachineLearning · /u/SpecificPark2594 · Jun 27, 06:33

**Background**: In machine learning, training runs often involve randomness from seeds, and changes in code or configurations can silently affect performance metrics. Traditional unit tests check for correctness, but they do not detect statistical regressions in metrics like accuracy or loss. pybench addresses this gap by treating benchmarks as statistical tests, ensuring that the same random seeds are used across runs for fair comparison.

**Tags**: `#machine-learning`, `#testing`, `#benchmarking`, `#python`, `#tool`

---

<a id="item-13"></a>
## [ML System Detects MMA Fight Events for Searchable Timeline](https://www.reddit.com/r/MachineLearning/comments/1ugwrmz/showcase_building_ml_models_that_watch_mma_fights/) ⭐️ 6.0/10

A developer with a background in MMA and AI has built a system that uses machine learning to analyze MMA fight videos, detecting positions like standing, clinching, and ground, as well as key events such as knockdowns and takedowns. The system generates a timeline with markers for each moment, making the video content searchable and easy to navigate. This project applies video understanding to combat sports analytics, making complex fight footage more accessible for coaches, fighters, and fans. It demonstrates a practical use case at the intersection of AI and sports, highlighting the potential for automated sports content analysis. The system currently distinguishes standing, clinching, and ground positions, detects knockdowns and takedowns, and provides a timeline at the bottom of the video for navigation. The developer, a former amateur MMA fighter and Brazilian Jiu-Jitsu brown belt, plans to refine the detection granularity in the future.

reddit · r/MachineLearning · /u/UnholyCathedral · Jun 27, 08:01

**Background**: Mixed martial arts (MMA) is a full-contact combat sport combining techniques from various disciplines. Brazilian Jiu-Jitsu (BJJ) is a grappling martial art. Video action detection is a computer vision task that identifies and localizes specific actions within video streams, while temporal action localization determines the start and end times of actions. This project applies such techniques to MMA fight analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Chen_Watch_Only_Once_An_End-to-End_Video_Action_Detection_Framework_ICCV_2021_paper.pdf">Watch Only Once: An End-to-End Video Action Detection Framework Shoufa Chen1</a></li>
<li><a href="https://arxiv.org/abs/1710.03383">[1710.03383] Real-Time Action Detection in Video Surveillance using Sub-Action Descriptor with Multi-CNN</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#computer vision`, `#sports analytics`, `#video understanding`, `#action detection`

---