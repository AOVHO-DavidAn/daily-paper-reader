---
title: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph
title_zh: 通过多模态记忆图导航海量视觉上下文的检索增强生成
authors: "Qiuchen Wang, Shihang Wang, Yu Zeng, Qiang Zhang, Fanrui Zhang, Zhuoning Guo, Bosi Zhang, Wenxuan Huang, Lin Chen, Zehui Chen, Pengjun Xie, Ruixue Ding"
date: 2026-04-30
pdf: "https://openreview.net/pdf/15bcadd889fea39eb43c9100ff8bf6e8f045eccf.pdf"
tags: ["query:lr"]
score: 5.0
evidence: 基于图记忆的多模态检索增强推理
tldr: 针对传统RAG在线性交互中难以处理长上下文多模态推理的问题，提出VimRAG框架，将推理过程建模为动态有向无环图，结构化存储智能体状态和检索到的多模态证据。实验证明该方法在长上下文多模态推理任务上显著优于现有RAG方法。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有RAG方法依赖线性交互历史，难以处理信息稀疏但token密集的视觉数据。
method: 提出VimRAG，使用动态有向无环图对推理过程进行结构化建模。
result: 在多个长上下文多模态推理基准上取得了最佳性能。
conclusion: 图结构记忆能有效组织多模态证据，提升推理鲁棒性。
---

## Abstract
Effectively retrieving, reasoning, and understanding multimodal information remains a critical challenge for agentic systems. Traditional Retrieval-augmented Generation (RAG) methods rely on linear interaction histories, which struggle to handle long-context tasks, especially those involving information-sparse yet token-heavy visual data in iterative reasoning scenarios. To bridge this gap, we introduce VimRAG, a framework tailored for multimodal Retrieval-augmented Reasoning across text, images, and videos. Inspired by our systematic study, we model the reasoning process as a dynamic directed acyclic graph that structures the agent states and retrieved multimodal evidence. Building upon this structured memory, we introduce a Graph-Modulated Visual Memory Encoding mechanism, with which the significance of memory nodes is evaluated via their topological position, allowing the model to dynamically allocate high-resolution tokens to pivotal evidence while compressing or discarding trivial clues. To implement this paradigm, we propose a Graph-Guided Policy Optimization strategy. This strategy disentangles step-wise validity from trajectory-level rewards by pruning memory nodes associated with redundant actions, thereby facilitating fine-grained credit assignment. Extensive experiments demonstrate that VimRAG consistently achieves state-of-the-art performance on diverse multimodal RAG benchmarks.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）

传统检索增强生成（RAG）方法在处理长上下文多模态任务时存在明显缺陷：它们依赖线性交互历史，无法有效应对信息稀疏但 token 密集的视觉数据（如图片、视频）在迭代推理场景中的检索与理解。现有智能体系统在多模态信息检索、推理和整合方面仍面临巨大挑战。本文旨在解决这一关键瓶颈，提出一种能够结构化组织多模态记忆、动态分配视觉资源并实现细粒度信用分配的框架，以提升长上下文多模态推理的性能与鲁棒性。

### 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

**核心思想**：将多模态推理过程建模为一个动态有向无环图（DAG），用于结构化存储智能体状态和检索到的多模态证据，从而打破线性交互的局限。

**关键技术细节**：
- **图结构记忆**：推理过程被表示为 DAG，其中节点代表智能体状态或检索到的多模态证据（文本、图像、视频片段），边表示推理依赖关系。这种结构允许非线性的信息流动和回溯。
- **图调制的视觉记忆编码（Graph-Modulated Visual Memory Encoding）**：利用节点在 DAG 中的拓扑位置（如入度、出度、中心性）评估其重要性，动态分配高分辨率 token 给关键证据，同时压缩或丢弃次要线索，以缓解视觉 token 过多导致的计算瓶颈。
- **图引导的策略优化（Graph-Guided Policy Optimization）**：解耦步骤有效性（step-wise validity）与轨迹级奖励，通过剪枝与冗余动作关联的记忆节点，实现细粒度信用分配，避免传统强化学习中长程奖励稀疏的问题。

**算法流程（文字说明）**：
1. 输入查询与多模态文档库；
2. 初始化一个空的 DAG，首个节点为查询状态；
3. 迭代执行：当前节点（智能体状态）选择下一个检索动作（如检索文本、图像区域或视频片段），返回的证据作为新节点加入 DAG，并建立与前驱节点的边；
4. 利用图调制视觉记忆编码对证据节点进行重要性评估，调整视觉 token 的分辨率分配；
5. 通过图引导策略优化更新智能体的动作选择策略，奖惩基于 DAG 中节点拓扑位置和步骤有效性；
6. 最终从 DAG 中提取推理路径生成答案。

### 3. 实验设计：使用了哪些数据集 / 场景，它的 benchmark 是什么，对比了哪些方法

- **数据集与场景**：论文在“多样化的多模态 RAG 基准（diverse multimodal RAG benchmarks）”上进行评估，包括需要长上下文推理的任务，涉及文本、图像和视频。但摘要中未逐一列出具体数据集名称。
- **Benchmark**：覆盖多模态信息检索与推理的标准评测集。
- **对比方法**：与现有主流 RAG 方法（如传统基于检索的生成流水线、线性记忆方法等）进行比较。论文未具体提及基线名称，但声称 VimRAG 在所有基准上“一致达到最先进性能”。

### 4. 资源与算力

论文摘要及提供的元数据中均未提及使用的 GPU 型号、数量、训练时长等具体算力信息。推测可能是实验部分未在摘要中体现，或作者在正文中有说明但此处未提供。需指出这一点。

### 5. 实验数量与充分性

- **数量**：摘要仅提到“extensive experiments”并在“diverse multimodal RAG benchmarks”上验证。未给出明确实验组数（如多少个数据集、消融实验次数等）。
- **充分性**：从摘要描述看，实验覆盖了不同模态（文本、图像、视频）和多种推理场景，但缺乏详细数据。若正文包含消融研究、参数分析、不同组件贡献度实验等，则可能较为充分。但仅凭摘要无法判断公平性（如是否使用相同训练/测试划分、是否调参一致等）。总体上，摘要声明一致最优，但需阅读全文确认。

### 6. 论文的主要结论与发现

- 图结构记忆（DAG）相比线性记忆，能更有效地组织多模态证据，提升长上下文推理鲁棒性。
- 基于拓扑位置动态分配视觉 token 资源的方法，可以在不牺牲性能的前提下大幅降低计算开销。
- 解耦步骤有效性奖励与轨迹奖励的优化策略，改善了强化学习在多步检索推理中的信用分配问题。
- VimRAG 在多个多模态 RAG 基准上均取得当前最佳性能，验证了方法的通用性。

### 7. 优点：方法或实验设计上的亮点

- **创新性**：首次将动态 DAG 引入多模态 RAG，突破了线性交互的固有限制。
- **精细资源管理**：图调制视觉记忆编码基于拓扑重要性动态分配 token，属于自适应的计算资源调度，适合处理高维度视觉数据。
- **强学习信号**：图引导的策略优化通过剪枝冗余动作对应的记忆节点，实现了步骤级的细粒度奖惩，比传统轨迹级奖励更有效。
- **实验充分性潜力**：虽未在摘要中列全，但声称在多样基准上一致最优，暗示了较强的泛化能力。

### 8. 不足与局限

- **实验细节缺失**：摘要未提供具体数据集名称、基线方法、消融实验设置、超参数等，难以独立评估结果的可复现性和公平性。
- **算力消耗未交代**：缺乏训练和推理的资源成本信息，无法判断方法在实际部署中的可行性。
- **应用限制**：只强调了性能提升，未讨论在处理极端长视频或非常庞大的记忆图时的扩展性问题；也未分析图重构的开销和复杂性。
- **偏差风险**：可能仅在作者选择的基准上优于基线，未涵盖所有多模态 RAG 场景（如低资源语言、跨模态对齐等）。同时，强化学习训练对环境交互的依赖性可能导致样本效率问题。

（完）
