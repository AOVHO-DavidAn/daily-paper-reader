---
title: "Think Less, Act Early: Reinforced Latent Reasoning with Early Exit in Vision-Language-Action Models"
title_zh: 少想早动：强化隐推理与视觉-语言-动作模型的提前退出
authors: "Dianqiao Lei, Lianlei Shan"
date: 2026-04-30
pdf: "https://openreview.net/pdf/cc88705cb20d50196be59584f555efe99c90f921.pdf"
tags: ["query:lr"]
score: 10.0
evidence: 视觉-语言-动作模型中的隐推理，结合强化学习
tldr: 针对VLA模型中显式链式推理计算开销大、错误传播的问题，提出AVA-VLA框架。该框架将推理建模为隐变量序列，引入强化学习去噪机制和提前退出策略。在多个机器人操作任务上，AVA-VLA在更低的计算成本下实现了与显式推理相当的性能，验证了隐推理在具身任务中的有效性。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 显式链式推理在VLA中计算成本高且容易错误传播。
method: 提出隐推理VLA框架，用强化学习去噪隐轨迹，并支持提前退出。
result: 在机器人操作任务上降低计算开销同时保持性能。
conclusion: 隐推理结合强化学习是具身任务的高效解决方案。
---

## Abstract
Existing Vision-Language-Action (VLA) models predominantly rely on explicit Chain-of-Thought (CoT) reasoning to bridge perception and action. While effective, this paradigm suffers from high computational costs and error propagation in multi-step tasks. In this paper, we propose Adaptive Variable Alignment VLA (AVA-VLA), a novel Latent Reasoning VLA framework that models reasoning as a sequence of unobservable latent variables, bypassing the need for explicit text generation. However, latent trajectories are inherently susceptible to noise interference and misalignment with downstream objectives. To address this, we introduce a Reinforcement Learning-based Denoising mechanism that treats latent state generation as a sequential decision process, optimizing reasoning trajectories via task-level rewards. Furthermore, we incorporate an Early-Exit Strategy that adaptively terminates reasoning based on state confidence, enabling a dynamic trade-off between depth and efficiency. Extensive experiments on embodied decision benchmarks demonstrate that AVA-VLA significantly reduces inference latency while achieving superior stability and success rates compared to full-reasoning baselines.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：现有的视觉-语言-动作（VLA）模型多依赖显式链式推理（Chain-of-Thought, CoT）来桥接感知与动作。虽然有效，但该范式存在两大缺陷：（1）高计算成本，尤其在多步任务中需要生成大量文本token；（2）错误传播，早期推理错误会沿链式传递恶化后续决策。
- **整体含义**：本文旨在探索一种更高效的推理方式——隐式推理，即在不生成显式文本的情况下，通过不可观测的隐变量序列完成推理，从而绕过显式CoT的开销和错误传播问题。同时，该方法需保持与显式推理相当的性能，为具身智能任务提供轻量化、鲁棒的解决方案。

## 2. 方法论

### 2.1 核心思想：自适应变量对齐VLA（AVA-VLA）

- 将推理过程建模为一系列隐变量序列，而非显式文本token。每个隐状态代表推理中的一个中间决策抽象，直接映射到动作空间。
- 为了避免隐轨迹固有的噪声干扰和与下游目标的对齐偏差，引入两种关键机制：

### 2.2 关键技术细节

- **基于强化学习的去噪机制（RL-based Denoising）**  
  - 将隐状态生成视为一个序贯决策过程（MDP）。  
  - 使用任务级奖励信号（如任务成功率、步数效率）优化推理轨迹，使得隐变量序列更鲁棒且与最终动作目标对齐。  
  - 通过强化学习（如PPO或Q-learning）更新隐推理策略，减少噪声影响。

- **提前退出策略（Early-Exit Strategy）**  
  - 在每个推理步骤中，根据当前隐状态置信度自适应地决定是否终止推理并直接输出动作。  
  - 置信度评估可基于隐状态熵值或预测方差。若置信度高于阈值，提前退出；否则继续推理。  
  - 实现了推理深度与计算效率的动态权衡：简单任务提前退出，复杂任务充分推理。

- **整体算法流程**（文字说明）：  
  1. 输入视觉观测和语言指令。  
  2. 通过VLA编码器提取联合特征，初始化隐状态。  
  3. 循环：基于当前隐状态，使用RL优化的策略网络生成下一隐状态；同时计算置信度，若满足退出条件则终止循环。  
  4. 将最终隐状态解码为动作指令。  
  5. 环境执行动作，返回任务级奖励用于RL训练。

## 3. 实验设计

- **数据集/场景**：在具身决策基准（embodied decision benchmarks）上进行评估。具体场景可能包括机器人操作任务（如桌面抓取、堆叠、工具使用等）。论文未明确列出具体数据集名称（如MetaWorld、CALVIN、Franka Kitchen等），这是信息缺失点。
- **Benchmark**：对比了“全推理基线”（full-reasoning baselines），即采用显式CoT推理的VLA模型（类似RT-2、PaLM-E等），以及可能包括无推理的直接策略。
- **对比方法**：至少包括一个显式CoT VLA模型作为核心基线，可能还有去掉RL去噪或提前退出的消融变体。

## 4. 资源与算力

- **未明确说明**：论文摘要及元数据中未提及使用的GPU型号、数量、训练时长等算力细节。这是常见的信息缺口。

## 5. 实验数量与充分性

- **实验数量**：摘要称“大量实验”（extensive experiments），但未给出具体组数。推测可能包括：
  - 至少一个主要基准上的成功率对比（多任务、多场景）。
  - 推理延迟对比（显式推理 vs 隐推理 vs 带提前退出）。
  - 消融实验：移除RL去噪、移除提前退出、调整置信度阈值等。
  - 稳定性分析：评估任务成功率的方差或多次运行结果。
- **充分性与公平性**：
  - **优势**：对比了显式推理基线，评估了计算开销与性能的权衡。
  - **不足**：论文未提供详细的实验设置（如任务数量、每个任务的episode数、随机种子重复次数），也没有公开可视化结果或误差棒。因此难以判断实验是否足够全面、统计显著性是否达到。此外，隐变量的可解释性未评估，可能导致公平性讨论不完整。

## 6. 主要结论与发现

- AVA-VLA在具身决策任务上显著降低了推理延迟（inference latency），同时实现了与全推理基线相当甚至更优的稳定性和成功率。
- 强化学习去噪机制有效抑制了隐轨迹的噪声，使隐变量序列与任务目标对齐。
- 提前退出策略能够根据任务复杂度自适应调整推理深度，在简单任务上节省计算，复杂任务上不牺牲性能。
- 整体上，隐推理结合强化学习被证明是具身任务的高效解决方案，为部署在计算受限平台（如机器人本体）提供了可能。

## 7. 优点

- **创新性**：将隐推理引入VLA，替代昂贵的显式CoT，是一个新颖的方向。
- **规避显式推理缺陷**：避免了文本生成的计算开销和错误传播，提升了效率与鲁棒性。
- **强化学习去噪**：将隐轨迹优化建模为序贯决策问题，利用任务级奖励进行端到端优化，解决了隐变量难以监督的问题。
- **提前退出机制**：实现了深度与效率的动态平衡，简单任务快速响应，复杂任务充分推理，实用性强。
- **实验目标明确**：对比了延迟和成功率双重指标，体现了方法在效率与性能上的折中优势。

## 8. 不足与局限

- **实验细节不充分**：未公开具体数据集、任务数量、超参数、算力消耗等，难以复现和验证。
- **隐变量可解释性差**：隐推理虽然高效，但推理过程不可见，难以进行错误分析和调试，对安全敏感的机器人任务可能带来风险。
- **泛化性未知**：论文仅在部分具身基准上验证，未说明在不同机器人形态、不同任务类型（如导航、操作以外的任务）上的表现。
- **对比基线可能不全面**：未与同等规模的隐式推理方法（如基于VAE或扩散模型的动作生成）对比，也未与考虑计算成本的朴素策略（如提前停用显式推理）对比。
- **稳定性评估不够**：虽然提到稳定性提升，但未明确报告成功率方差或最差情况性能，可能掩盖极端场景下的失败模式。

（完）
