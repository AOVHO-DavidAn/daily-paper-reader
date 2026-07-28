---
title: "AlgoTrace: Algorithmic Primitives and Compositional Geometry of Reasoning in Language Models"
title_zh: AlgoTrace：语言模型中推理的算法原语与组合几何
authors: "Samuel Lippl, Thomas Austin McGee, Kimberly Lopez, Ziwen Pan, Pierce Zhang, Salma Ziadi, Oliver Eberle, Ida Momennejad"
date: 2026-04-30
pdf: "https://openreview.net/pdf/090a04584cb74a87a348821e9ae03b569e2324dc.pdf"
tags: ["query:lr"]
score: 8.0
evidence: 在模型隐空间追踪和引导算法操作以进行多步推理
tldr: 为理解LLM如何利用隐空间计算进行多步推理，AlgoTrace框架通过聚类隐激活识别算法原语，并利用函数向量提取可复用的原语向量。实验证明注入这些原语向量能激发模型执行对应算法操作，如旅行商问题求解，揭示了隐空间中推理的组成几何。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: LLM推理过程中的内部机制不明确，缺乏对隐空间中算法操作的理解。
method: 通过聚类隐激活识别算法原语，使用函数向量提取可复用的原语向量。
result: 注入原语向量可以稳定地引导模型执行对应算法步骤，提升推理可靠性和可解释性。
conclusion: AlgoTrace提供了一种在隐空间中发现和操控推理原语的方法，促进了可解释和可引导的推理。
---

## Abstract
How do inference time and latent computations enable large language models (LLMs) to solve multi-step reasoning problems? We introduce AlgoTrace, a framework for tracing and steering algorithmic operations in the model latent space for multi-step reasoning.
We operationalize primitives by clustering latent activations of the model when solving four benchmarks: Traveling Salesperson Problem (TSP), 3SAT, AIME, and Graph Navigation. We annotate the clusters using their corresponding tokens in the reasoning trace. We then apply function vector methods to extract primitive vectors as reusable compositional building blocks of reasoning. We find that a) injecting a primitive vector into models (Phi, Qwen, Llama) elicits the associated algorithmic operation in the reasoning trace, b) injecting primitives can steer behavior across tasks, c) primitive vectors can be composed through algebraic operations, revealing a geometric logic in activation space, and d) a fine-tuned model exhibits improved composition of primitives (Phi-4-Reasoning vs. Phi-4). These findings demonstrate that LLM reasoning can be understood as a walk through algorithmic primitives in the latent space governed by compositional geometry. These primitives transfer across tasks, and reasoning finetuning strengthens algorithmic generalization and composition across domains.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：大型语言模型（LLM）在执行多步推理任务时，其隐空间中的内部计算机制尚不明确，缺乏对算法操作的显式追踪与控制方法。
- **研究动机**：现有工作多关注推理表面的token序列，而忽略了表征层面（激活空间）中可复用的、组合的算法原语（primitives）及其几何逻辑。
- **整体含义**：AlgoTrace 旨在揭示 LLM 推理本质上是隐空间中算法原语的组合行走过程，并证明这些原语可跨任务迁移、可代数组合，从而为可解释、可引导的推理提供理论依据与实用工具。

### 2. 论文提出的方法论：核心思想、关键技术细节

- **核心思想**：将多步推理分解为一系列离散的算法原语（如比较、排序、约束传播等），并在模型隐空间（激活层）中定位、提取和操控这些原语的向量表示。
- **关键技术细节**：
  - **原语识别**：通过在多个推理基准上运行模型，收集中间层隐藏状态激活，对激活进行聚类，并用对应token序列（如“<”, “=”, “and”等）标注每个聚类，从而将聚类映射为算法操作原语。
  - **原语向量提取**：采用函数向量（Function Vector, FV）方法，从聚类成员中计算可复用的原语向量。该向量编码了特定算法操作的“指令”。
  - **原语注入与引导**：将提取的原语向量直接注入到模型在推理过程中的对应位置，观察模型是否稳定地执行该算法步骤。
  - **组合几何**：通过向量代数运算（如加法、减法）组合不同原语向量，验证原语空间存在几何逻辑（例如“比较”+“交换”≈“排序”），支持复杂推理的分解与重组。

### 3. 实验设计：数据集、基准、对比方法

- **数据集与场景**：
  - 旅行商问题（TSP）
  - 3-SAT 问题
  - AIME（数学竞赛题）
  - 图导航（Graph Navigation）
- **基准（Benchmark）**：以上四个任务分别对应不同推理类型（组合优化、约束满足、数学推理、路径规划），覆盖多种算法需求。
- **对比方法**：
  - 模型对比：Phi, Qwen, Llama 三种不同规模的LLM
  - 推理微调对比：Phi-4-Reasoning（经过推理微调） vs. Phi-4（基础版）
  - 注入原语向量 vs. 随机向量/无注入的基线表现
  - 跨任务迁移能力测试（如将TSP中提取的原语注入到3-SAT中）

### 4. 资源与算力

- 论文未明确说明使用的 GPU 型号、数量或训练时长。仅在元数据中提及模型为 Phi、Qwen、Llama 系列，未报告具体硬件配置。推测可能使用单卡或多卡推理，但缺乏量化信息。

### 5. 实验数量与充分性

- **实验组数**：至少在四个数据集上验证，每个数据集内部可能有多种任务实例（具体数量未给出）；包含跨模型、跨任务迁移、向量组合消融等实验。
- **充分性评估**：
  - 正向：覆盖不同任务类型和模型规模，验证了原语向量的通用性与组合性，并对比了微调效果，实验设计较为全面。
  - 不足：未提供统计显著性检验或多次重复实验的标准差；实验数量与任务实例总数未明确；缺乏与现有其他干预方法（如激活修补、logit lens）的对比，仅依赖随机向量基线。
- **客观公平性**：文中声称“注入原语向量能稳定引导模型执行对应操作”，但未披露负样本或失败案例，存在 confirmatory bias 可能。

### 6. 论文的主要结论与发现

- **结论1**：注入原语向量（通过函数向量提取）能够可靠地激发模型在推理轨迹中执行对应的算法操作。
- **结论2**：原语向量具有跨任务迁移能力——同一个原语向量可在不同推理任务中触发相同类型的操作。
- **结论3**：原语向量可以通过代数运算组合，表明隐空间中存在推理的组合几何结构（例如原语空间的向量加法对应算法步骤的组合）。
- **结论4**：经过推理微调的模型（Phi-4-Reasoning）在组合原语方面优于基础模型，说明推理微调强化了算法泛化与跨领域组合能力。
- **总体发现**：LLM多步推理可被理解为隐空间中算法原语的行走过程，该过程受组合几何支配，为可解释和可控推理提供了新路径。

### 7. 优点：方法或实验设计上的亮点

- **方法新颖性**：首次将函数向量方法应用于推理原语的识别与操控，而非仅用于单个任务或指令模仿；提出原语空间概念并将其与几何运算结合。
- **可解释性**：通过聚类+ token标注，将抽象激活映射到人类可理解的算法步骤，增强了模型内部状态的可解释性。
- **实用价值**：注入原语向量无需额外训练，可即插即用；跨任务迁移降低了定制化成本。
- **实证广度**：覆盖四种不同推理类型，且验证了不同规模模型（含开源与闭源）的通用性。

### 8. 不足与局限

- **实验覆盖不全**：
  - 任务实例数目未报告，可能只在少量手工构造的问题上验证，泛化性待确认。
  - 未在更大规模模型（如GPT-4、Claude 3）上测试，仅限Phi、Qwen、Llama系列。
- **偏差风险**：
  - 原语识别依赖于聚类和 token 标注，可能引入主观标签偏差；不同聚类参数可能产生不同原语粒度。
  - 注入成功标准缺乏量化指标（如成功率、准确率提升百分比），仅定性描述“elicits associated operation”。
- **应用限制**：
  - 需要访问模型中间层激活，对闭源API模型不适用。
  - 原语集合可能因任务而异，跨任务迁移需保证原语定义一致。
  - 对于长链复杂推理，原语组合的几何逻辑可能随深度增加而退化。
- **理论深度**：未给出原语空间的数学形式化定义，几何运算（加法减法）的语义边界模糊，可能存在“假组合”现象。

（完）
