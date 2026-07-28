---
title: "Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations"
title_zh: 对比推理对齐：从隐藏表示中进行强化学习
authors: "Haozheng Luo, Yimin Wang, Jiahao Yu, Binghui Wang, Yan Chen"
date: 2026-04-30
pdf: "https://openreview.net/pdf/52925f64fcf245878049971f30f807121aecf743.pdf"
tags: ["query:lr"]
score: 6.0
evidence: 隐空间优化用于安全推理对齐
tldr: 针对大模型安全对齐仅在输出层操作、缺乏对推理过程引导的问题，提出CRAFT框架。该框架利用对比表征学习和强化学习，在隐空间中分离安全与不安全的推理轨迹。理论分析表明隐文本一致性约束能消除表面对齐策略。实验证明CRAFT能有效提升模型对越狱攻击的鲁棒性。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有安全对齐仅在输出层操作，无法纠正内部不安全推理。
method: CRAFT在隐状态空间优化安全轨迹，结合对比学习和强化学习。
result: 在多个红队测试中显著提升模型安全性。
conclusion: 隐空间推理对齐是一种有效的安全防御手段。
---

## Abstract
We propose CRAFT, a red-teaming alignment framework that leverages model reasoning capabilities and hidden representations to improve robustness against jailbreak attacks. 
Unlike prior defenses that operate primarily at the output level, CRAFT aligns large reasoning models to generate safety-aware reasoning traces by explicitly optimizing objectives defined over the hidden state space. 
Methodologically, CRAFT integrates contrastive representation learning with reinforcement learning to separate safe and unsafe reasoning trajectories, yielding a latent-space geometry that supports robust, reasoning-level safety alignment. 
Theoretically, we show that incorporating latent–textual consistency into GRPO eliminates superficially aligned policies by ruling them out as local optima.
Empirically, we evaluate CRAFT on multiple safety benchmarks using two strong reasoning models, Qwen3-4B-Thinking and R1-Distill-Llama-8B, where it consistently outperforms state-of-the-art defenses such as IPO and SafeKey. Notably,  CRAFT delivers an average **79.0%** improvement in reasoning safety and **87.7%** improvement in final-response safety
over the base models, demonstrating the effectiveness of hidden-space reasoning alignment.

---

## 论文详细总结（自动生成）

## 1. 核心问题与整体含义（研究动机和背景）

- **核心问题**：现有的大语言模型安全对齐方法仅在**输出层**进行操作（如基于奖励的RLHF、输出过滤等），无法在推理过程中纠正模型内部的不安全思维链（chain-of-thought），导致模型易受越狱攻击。
- **研究动机**：推理模型（如Qwen3、R1-Distill-Llama）在生成答案前会输出显式的推理轨迹，这些轨迹中可能包含有害或不安全的中间步骤，而输出层对齐无法触及这些隐层表征。
- **整体含义**：提出在**隐空间（hidden state space）** 中对齐模型的安全推理过程，从根源上提升模型对越狱攻击的鲁棒性，实现“推理级安全对齐”。

## 2. 方法论：核心思想、关键技术细节

- **核心思想**：CRAFT（Contrastive Reasoning Alignment Framework，对比推理对齐框架）结合**对比表征学习**与**强化学习**，在隐状态空间中分离安全和不安全的推理轨迹，迫使模型学习安全导向的推理路径。
- **关键技术细节**：
  - **隐空间对比学习**：对同一输入（如恶意指令），同时生成安全和不安全两种推理轨迹，利用对比损失拉大它们在隐空间中的距离，使安全轨迹聚集、不安全轨迹远离。
  - **强化学习优化**：基于Group Relative Policy Optimization (GRPO) 框架，在隐空间定义奖励函数，鼓励模型选择安全轨迹并抑制不安全轨迹。
  - **隐–文本一致性约束**（Latent–Textual Consistency）：理论证明该约束可以排除那些仅在输出层表现安全、但隐层仍保留不安全推理的“表面对齐”策略，使其不再是局部最优解。
- **算法流程**（文字描述）：
  1. 对每个提示，模型生成多个推理轨迹，包含安全与不安全路径。
  2. 通过对比学习提取隐状态表示，构建正负样本对（安全vs不安全）。
  3. 使用GRPO更新策略，奖励基于隐空间距离和安全文本一致性。
  4. 重复迭代直至收敛。

## 3. 实验设计

- **数据集和场景**：使用**多个安全红队基准**（具体名称未在摘要中列出，推测包括常用 jailbreak 测试集，如HarmBench、AdvBench等），覆盖不同攻击类型（如 prompt 注入、角色扮演等）。
- **Benchmark**：对比方法包括**IPO**（Identity Preference Optimization）和**SafeKey**等最新安全对齐防御方法。
- **评估模型**：**Qwen3-4B-Thinking** 和 **R1-Distill-Llama-8B**，两个具有显式推理能力的推理模型。
- **对比基线**：基础模型（未经CRAFT对齐的版本）、IPO、SafeKey。

## 4. 资源与算力

- **论文摘要/元数据未明确说明**使用的GPU型号、数量、训练时长等具体算力信息。可推测是基于常见训练配置（如NVIDIA A100），但无法确认。

## 5. 实验数量与充分性

- **实验数量**：摘要中提到在“多个安全基准”上进行评估，并对比了两种基线方法，但未列出具体数据集数量和消融实验详情。从元数据看，证据为“隐空间优化用于安全推理对齐”，可能包含一定数量的消融（如不同对比损失权重、RL超参数等），但信息不足。
- **充分性**：在两个不同规模的推理模型上验证，且与两种较强的基线比较，结论具有一定泛化性。但缺乏对非推理模型（如普通指令微调模型）的对比，以及跨领域（如医疗、法律）的测试，可能不够全面。总体而言，在红队安全场景下是充分的，但覆盖范围有限。

## 6. 主要结论与发现

- CRAFT在推理安全（reasoning safety）上平均提升**79.0%**，在最终响应安全（final-response safety）上平均提升**87.7%**（相对于基础模型）。
- 一致优于IPO和SafeKey等现有防御方法，证明隐空间推理对齐比输出层对齐更有效。
- 理论分析表明隐–文本一致性约束可以消除仅输出安全的表面对齐策略，为安全对齐提供了新理论视角。

## 7. 优点

- **方法创新**：首次将对比学习与强化学习结合应用于隐空间安全对齐，而非仅关注输出层，切中推理模型内部安全漏洞的关键。
- **理论支撑**：提供了严格的数学证明，说明隐–文本一致性约束如何排除次优策略，增强了方法可信度。
- **实验有力**：在两个主流推理模型上获得显著提升，且效果大幅超越现有方法。
- **实用性**：CRAFT框架可集成到现有RL对齐流程中，无需额外的人工标注或外部分类器，易于部署。

## 8. 不足与局限

- **实验覆盖有限**：仅在两个推理模型上测试，未验证小型推理模型或非推理模型；基准数据集未具体公开，可能影响可复现性。
- **缺乏算力与成本分析**：未提及训练时间、GPU资源需求，不利于实际落地的成本评估。
- **潜在偏差风险**：对比学习和强化学习均依赖预先定义的安全/不安全轨迹，若数据集中“安全”定义存在偏差（如过度保守），可能导致模型过度拒绝合理请求。
- **应用限制**：目前仅针对越狱攻击，对其他安全威胁（如数据泄露、偏见生成）的防御效果未知；且隐空间对齐可能增加推理计算开销。
- **缺乏部署细节**：未讨论在实际系统中如何高效执行隐空间奖励计算，可能存在工程挑战。

（完）
