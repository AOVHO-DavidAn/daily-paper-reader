---
title: Latent Collaboration in Multi-Agent Systems
title_zh: 多智能体系统中的隐式协作
authors: "Jiaru Zou, Ruizhong Qiu, Gaotang Li, Xiyuan Yang, Katherine Tieu, Pan Lu, Ke Shen, Hanghang Tong, Yejin Choi, Jingrui He, James Zou, Mengdi Wang, Ling Yang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/15bee174811cf963d2bb355c7908653b26d4a7ff.pdf"
tags: ["query:lr"]
score: 8.0
evidence: 多智能体在连续隐空间中协作
tldr: 针对现有LLM智能体依赖文本推理通信效率低的问题，提出LatentMAS框架，让智能体在连续隐空间中通过自回归隐式思考直接协作，无需文本解码。共享隐工作记忆实现无损信息交换。实验表明该方法在保持性能的同时显著提升通信效率，为多智能体系统提供了新的隐空间交互范式。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有LLM智能体依赖文本中介进行推理和通信，效率低且信息有损。
method: 提出LatentMAS，智能体生成隐式思考嵌入，通过共享隐工作记忆协作，无需训练。
result: 在多个推理任务上实现高效通信，性能与文本基线相当。
conclusion: 隐空间协作是可行且高效的多智能体交互方式。
---

## Abstract
Multi-agent systems (MAS) extend large language models (LLMs) from independent single-model reasoning to coordinative system-level intelligence. While existing LLM agents depend on text-based mediation for reasoning and communication, we take a step forward by enabling models to collaborate directly within the continuous latent space. We introduce LatentMAS, an end-to-end training-free framework that enables pure latent collaboration among LLM agents. In LatentMAS, each agent first performs auto-regressive latent thoughts generation through last-layer hidden embeddings instead of text. Then, a shared latent working memory preserves and transfers each agent's internal representations and latent thoughts, ensuring lossless information exchange without re-encoding. We provide detailed theoretical analyses showing that LatentMAS achieves higher expressiveness and lossless information preservation with lower overall complexity than standard text-based MAS. In addition, empirical evaluations across 9 comprehensive benchmarks spanning math and science reasoning, commonsense understanding, and code generation show that LatentMAS outperforms advanced single agents and text-based MAS baselines, achieving up to 14.6\% higher accuracy, reducing output token usage by 70.8\%-83.7\%, and providing 4$\times$-4.3$\times$ faster end-to-end inference.

---

## 论文详细总结（自动生成）

# 论文《Latent Collaboration in Multi-Agent Systems》详细中文总结

## 1. 论文的核心问题与整体含义（研究动机和背景）
- **研究动机**：现有基于大语言模型（LLM）的多智能体系统（MAS）依赖文本中介进行推理和通信，即智能体之间通过生成自然语言文本来交换信息。这种方式存在两大缺陷：① 文本解码过程导致通信效率低下，增加推理延迟和 token 消耗；② 文本编码会丢失原始隐层表示中的细粒度信息，造成信息有损。
- **整体含义**：论文旨在突破文本中介的限制，让 LLM 智能体直接在连续隐空间（latent space）中进行协作，实现无损、高效的信息交换，从而提升多智能体系统的整体性能和推理速度。

## 2. 论文提出的方法论：核心思想、关键技术细节、算法流程
- **核心思想**：提出 **LatentMAS** 框架，是一种端到端、无需训练的纯隐空间协作方法。智能体之间通过共享的“隐工作记忆”（shared latent working memory）传递自回归生成的“隐式思考”（latent thoughts），而无需将中间推理过程解码为文本。
- **关键技术细节**：
  - 每个智能体首先基于自身输入生成自回归隐式思考——不输出文本 token，而是直接输出最后一层隐藏层的嵌入向量。
  - 所有智能体的隐式思考被存入共享的隐工作记忆中，该工作记忆保留了智能体的内部表示和隐思考，实现了无损信息交换（无需重新编码）。
  - 框架是 **training-free** 的，即不需要额外训练或微调 LLM，直接利用预训练模型的前向传播能力。
- **理论分析**：论文提供了详细的理论证明，表明 LatentMAS 在表达能力（expressiveness）上高于标准文本 MAS，且能够实现无损信息保持，同时整体复杂度更低。

## 3. 实验设计：数据集、场景、基准、对比方法
- **数据集与场景**：涵盖 9 个综合性基准测试，涉及：
  - 数学与科学推理（如数学题）
  - 常识理解（如常识问答）
  - 代码生成（如程序合成）
- **对比方法**：
  - 先进单智能体方法（single agent baselines）
  - 基于文本的多智能体系统（text-based MAS baselines）
- **评估指标**：准确性（accuracy）、输出 token 使用量、端到端推理速度（inference latency）。

## 4. 资源与算力
- **论文未明确说明**：摘要及元数据中未提及具体使用的 GPU 型号、数量、训练时长或推理硬件配置。但鉴于框架是 training-free 的，主要消耗在推理阶段，可能采用主流 GPU（如 A100 或 V100）进行实验，但具体细节缺失。

## 5. 实验数量与充分性
- **实验数量**：共在 9 个不同数据集上进行了评估，涵盖了多个推理领域。
- **充分性评估**：
  - 数据集覆盖较为全面，包括数学、常识和代码，能体现方法的通用性。
  - 对比了单智能体和文本 MAS 基线，但未提及是否进行消融实验（如隐空间维度的影响、工作记忆大小等），也未报告多次运行的标准差或统计显著性检验。
  - 总体实验数量尚可，但缺少消融和超参数敏感性分析，可能不够充分。实验设计相对公平（对比了同类方法），但缺乏与更多近期 MAS 方法的比较（例如基于工具或结构化消息的 MAS）。

## 6. 论文的主要结论与发现
- LatentMAS 在 9 个基准上超过先进的单智能体和文本 MAS 基线，准确率提升最高达 **14.6%**。
- 输出 token 使用量减少 **70.8%–83.7%**，端到端推理速度提升 **4×–4.3×**。
- 理论分析证实：隐空间协作具有更高的表达力和无损信息保持能力，且复杂度更低。
- 结论：隐空间协作是一种可行且高效的多智能体交互方式，未来可替代传统文本中介范式。

## 7. 优点：方法或实验设计上的亮点
- **方法创新性**：首次提出纯隐空间多智能体协作框架，无需训练，直接利用预训练 LLM 的隐层表示，避免了文本解码瓶颈。
- **共享隐工作记忆**：实现无损信息交换，显著减少 token 消耗和推理延迟。
- **理论支撑**：提供了形式化的理论分析，证明了方法的优势（如表达能力、复杂度）。
- **实验全面性**：覆盖 9 个不同推理任务，且结果相比基线有明显优势，说明方法通用性强。
- **高效率**：在提升或保持性能的同时，大幅降低计算开销，具有实际部署价值。

## 8. 不足与局限
- **实验细节缺失**：未报告硬件配置、重复实验的统计量、消融实验（例如隐工作记忆大小的影响、不同 LLM 的选择等），限制了结果的可重复性和深度理解。
- **对比基线有限**：仅对比了单智能体和文本 MAS，未与其他先进的隐空间方法（如其他表示学习或多模态 MAS）或基于检索的 MAS 进行对比。
- **应用限制**：假设所有智能体共享同一个隐工作记忆，这可能在异构模型或分布式场景中不可行；当前仅适用于可访问中间隐层表示的 LLM（如 GPT-2/3 类），对于仅提供 API 访问的封闭模型不适用。
- **潜在偏差风险**：未讨论隐空间表示可能引入的语义漂移或模型内部偏差，以及是否对所有任务类型（尤其是需要精确文本输出如代码生成）鲁棒。
- **未说明推理代价**：虽然 token 数减少，但隐空间通信可能增加内存占用（存储连续向量），论文未比较总体计算量（FLOPs）。

（完）
