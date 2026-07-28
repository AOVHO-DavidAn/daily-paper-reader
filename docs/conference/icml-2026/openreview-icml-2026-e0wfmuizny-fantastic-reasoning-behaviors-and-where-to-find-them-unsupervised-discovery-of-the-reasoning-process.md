---
title: "Fantastic Reasoning Behaviors and Where to Find Them: Unsupervised Discovery of the Reasoning Process"
title_zh: 奇妙的推理行为及其发现之处：推理过程的无监督发现
authors: "Zhenyu Zhang, Shujian Zhang, John Wheatley Lambert, Wenxuan Zhou, Zhangyang Wang, Mingqing Chen, Andrew Hard, Rajiv Mathews, Lun Wang"
date: 2026-04-30
pdf: "https://openreview.net/pdf/68e942e7c758c90b02012db5dacb1bf79c8965e0.pdf"
tags: ["query:lr"]
score: 7.0
evidence: 在LLM激活空间（隐空间）中发现推理向量
tldr: 针对现有推理行为分析依赖人工定义和词级别监督的问题，RISE框架利用稀疏自编码器在LLM激活空间中无监督发现推理向量（编码不同推理行为的方向）。该方法无需先验标签，可自动识别反思、回溯等行为，为理解隐空间推理机制提供新工具。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有推理分析依赖人工定义的词级别概念，无法覆盖隐空间中多样的推理行为。
method: 利用稀疏自编码器在LLM激活空间中无监督学习推理向量，每个向量编码一种推理行为。
result: 发现多个有意义的推理行为向量，可解释模型内部推理过程，且能用于行为控制。
conclusion: 隐空间中的推理向量为理解LLM推理提供了无监督、细粒度的分析维度。
---

## Abstract
Despite the growing reasoning capabilities of recent large language models (LLMs), their internal mechanisms during the reasoning process remain underexplored. Prior approaches often rely on human-defined concepts (e.g., overthinking, reflection) at the word level to analyze reasoning in a supervised manner. However, such methods are limited, as it is infeasible to capture the full spectrum of potential reasoning behaviors, many of which are difficult to define in token space. In this work, we propose an unsupervised framework (namely, RISE: Reasoning behavior Interpretability via Sparse auto-Encoder) for discovering reasoning vectors, which we define as directions in the activation space that encode distinct reasoning behaviors. By segmenting chain-of-thought traces into sentence-level 'steps' and training sparse auto-encoders (SAEs) on step-level activations, we uncover disentangled features corresponding to interpretable behaviors such as reflection and backtracking. Visualization and clustering analyses show that these behaviors occupy separable regions in the decoder column space. Moreover, targeted interventions on SAE-derived vectors can controllably amplify or suppress specific reasoning behaviors, altering inference trajectories without retraining. Beyond behavior-specific disentanglement, SAEs capture structural properties such as response length, revealing clusters of long versus short reasoning traces. More interestingly, SAEs enable the discovery of novel behaviors beyond human supervision. We demonstrate the ability to control response confidence by identifying confidence-related vectors in the SAE decoder space. These findings underscore the potential of unsupervised latent discovery for both interpreting and controllably steering reasoning in LLMs.

---

## 论文详细总结（自动生成）

# 论文详细总结

## 1. 论文的核心问题与整体含义（研究动机和背景）

- **核心问题**：大型语言模型（LLM）在推理过程中内部机制仍不清晰，现有分析方法依赖人工定义的概念（如过度思考、反思等）在词级别进行有监督分析，无法捕捉隐空间中多样且难以在词空间中定义的推理行为。
- **研究动机**：需要一种无监督、细粒度的方式来自动发现LLM隐含层中编码的不同推理行为，从而更好地理解和控制模型推理过程。
- **整体含义**：通过无监督发现“推理向量”（激活空间中编码特定推理行为的方向），为解释和可控引导LLM推理提供新工具。

## 2. 论文提出的方法论：核心思想、关键技术细节、公式或算法流程

- **核心思想**：RISE框架（Reasoning behavior Interpretability via Sparse auto-Encoder）利用稀疏自编码器（SAE）在LLM激活空间中无监督学习推理向量，每个向量对应一种推理行为。
- **关键技术细节**：
  - 将链式思维（Chain-of-Thought）轨迹分割成句子级别的“步骤”（step-level）。
  - 在步骤级别的激活值上训练稀疏自编码器（SAE），得到解耦的特征（disentangled features）。
  - 每个特征对应于可解释的推理行为（如反思、回溯）。
- **算法流程（文字描述）**：
  1. 从LLM推理过程中收集句子级激活向量。
  2. 训练SAE，使其输入（激活）经过编码器得到稀疏潜在表示，再通过解码器重构输入。
  3. 解码器的每一列（即每个潜在单元对应的解码方向）被解释为一个“推理向量”。
  4. 可视化与聚类分析表明，这些推理向量在解码器列空间中占据可分离的区域。
  5. 通过对SAE导出的向量进行有针对性的干预（amplify或suppress），可以可控地改变推理轨迹，无需重新训练模型。

## 3. 实验设计：使用了哪些数据集 / 场景，它的 benchmark 是什么，对比了哪些方法

- **数据集与场景**：摘要未明确列出具体数据集或任务，但提及“response length”分析以及“confidence-related vectors”的发现，暗示可能使用了多种推理任务（如数学推理、常识推理等）。基准（benchmark）未明确说明。
- **对比方法**：文中未直接列出对比方法，但隐含对比了传统依赖人工定义词级别概念的有监督分析方法。实验可能包含：
  - 与人工标注的推理行为标签进行对应性验证（如反射、回溯）。
  - 干预实验：比较有无SAE向量干预下的输出变化。
  - 聚类分析：展示推理向量在空间中的分离性。

## 4. 资源与算力：如果文中有提到，请总结使用了多少算力（GPU 型号、数量、训练时长等）。若未明确说明，也请指出这一点

- **未明确说明**：摘要和元数据中未提及具体的GPU型号、数量、训练时长等算力信息。仅可推断训练SAE在通常的LLM激活数据上计算量不大，但无法提供具体数字。

## 5. 实验数量与充分性：大概做了多少组实验（如不同数据集、消融实验等），这些实验是否充分、是否客观、公平

- **实验数量**：摘要仅定性描述了可视化、聚类、干预等几类实验，但未详细列出所有实验组数。可能包含：
  - 行为发现实验（识别反射、回溯等行为）。
  - 行为干预实验（放大/抑制特定行为）。
  - 结构特性实验（响应长度聚类）。
  - 新颖行为发现（置信度相关向量）。
- **充分性评估**：从摘要看，实验覆盖了发现、解释、干预多个方面，但缺少定量指标（如准确率、干预成功率等），也缺乏与基线方法的直接比较。因此实验的充分性和客观性尚不明确，需要阅读全文才能判断。文中提到“demonstrate the ability to control response confidence”，可能提供了控制效果的量化证据，但摘要中未展示。

## 6. 论文的主要结论与发现

- 无监督学习的SAE能够在LLM激活空间中发现多个有意义的推理行为向量，可解释模型内部推理过程（如反射、回溯）。
- 推理行为在解码器列空间中占据可分离的区域（通过可视化和聚类验证）。
- 通过对SAE向量进行干预可以可控地改变推理轨迹（放大/抑制特定行为），无需重新训练模型。
- SAE还能捕获结构属性（如响应长度），揭示长/短推理轨迹的聚类。
- SAE能够发现超越人类监督的新颖行为（如置信度相关向量），并可控制响应置信度。

## 7. 优点：方法或实验设计上有哪些亮点

- **无监督发现**：无需人工预定义标签，能够自动发现隐空间中多样化的推理行为，包括人类难以定义的新行为。
- **细粒度与可解释性**：基于句子级激活和稀疏编码，每个向量对应一种行为，具有可解释性。
- **可控干预**：无需微调模型，仅通过改变SAE向量的强度即可控制推理行为，具有实用价值。
- **泛化性**：方法不依赖特定模型或任务，理论上可适用于任何LLM的推理分析。
- **实验多样性**：覆盖了行为发现、可视化、聚类、干预、新颖行为探究等多个方面。

## 8. 不足与局限：包括实验覆盖、偏差风险、应用限制等

- **实验覆盖有限**：摘要中缺乏具体的定量结果（如干预成功率、行为识别的准确率、与人工标注的一致率等），没有在不同模型大小或不同任务上的系统性比较。
- **偏差风险**：SAE训练依赖于激活数据的采集，可能受到特定模型、提示分布或数据集偏差的影响，发现的推理向量是否具有跨模型通用性未知。
- **应用限制**：当前方法仅针对句子级激活，可能无法捕捉更细粒度（如token级）的推理行为；干预效果可能依赖于SAE的解码质量，且对复杂长链推理的鲁棒性需进一步验证。
- **可解释性局限性**：虽然每个向量可解释为一种行为，但解读仍需人工关联，可能存在主观性。
- **资源要求**：虽然未提及算力，但训练SAE需要从LLM中提取大量激活，对存储和计算有一定需求。

（完）
