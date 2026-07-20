---
title: "SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model"
title_zh: SeqAfford：基于多模态大模型的顺序3D可供性推理
authors: "Yu, Chunlin, Wang, Hanqing, Shi, Ye, Luo, Haoyang, Yang, Sibei, Yu, Jingyi, Wang, Jingya"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Yu_SeqAfford_Sequential_3D_Affordance_Reasoning_via_Multimodal_Large_Language_Model_CVPR_2025_paper.pdf"
tags: ["query:seg-llm"]
score: 8.0
evidence: 提出基于多模态大模型的顺序3D可供性分割推理任务
tldr: 本文提出顺序3D可供性推理任务，突破单对象单可供性范式。构建首个基于指令的可供性分割数据集，使多模态大模型能够推理复杂用户意图并分解为一系列分割图，显著提升了机器人操作中的可解释性和灵活性。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1731, \"height\": 796, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1692, \"height\": 713, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1720, \"height\": 608, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 1376, \"height\": 767, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 1475, \"height\": 1245, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1769, \"height\": 368, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 910, \"height\": 937, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 886, \"height\": 254, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-yu-seqafford-sequential-3d-affordance-reasoning-via-multimodal-large-language-model-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 840, \"height\": 256, \"label\": \"Table\"}]"
motivation: 现有3D可供性分割无法处理长期任务和复杂用户意图。
method: 构建顺序3D可供性推理任务，利用多模态大模型将复杂意图分解为分割序列。
result: 在构建的数据集上取得了优异性能，支持更复杂的机器人操作指令。
conclusion: 该方法为机器人操作中的长时推理提供了新方案。
---

## Abstract
3D affordance segmentation aims to link human instructions to touchable regions of 3D objects for embodied manipulations. Existing efforts typically adhere to single-object, single-affordance paradigms, where each affordance type or explicit instruction strictly corresponds to a specific affordance region and are unable to handle long-horizon tasks. Such a paradigm cannot actively reason about complex user intentions that often imply sequential affordances. In this paper, we introduce the Sequential 3D Affordance Reasoning task, which extends the traditional paradigm by reasoning from cumbersome user intentions and then decomposing them into a series of segmentation maps. Toward this, we construct the first instruction-based affordance segmentation benchmark that includes reasoning over both single and sequential affordances, comprising 180K instruction-point cloud pairs. Based on the benchmark, we propose our model, SeqAfford, to unlock the 3D multi-modal large language model with additional affordance segmentation abilities, which ensures reasoning with world knowledge and fine-grained affordance grounding in a cohesive framework. We further introduce a multi-granular language-point integration module to endow 3D dense prediction. Extensive experimental evaluations show that our model excels over well-established methods and exhibits open-world generalization with sequential reasoning abilities.

---

## 论文详细总结（自动生成）

# SeqAfford：基于多模态大模型的顺序3D可供性推理 —— 论文总结

## 1. 核心问题与整体含义（研究动机和背景）

- **现有范式局限**：传统3D可供性分割（Affordance Segmentation）遵循单对象、单可供性（single-object, single-affordance）范式，每个可供性类型或显式指令严格对应一个区域，无法处理隐含多个顺序步骤的复杂用户意图（例如“用微波炉加热碗中的食物”需要先抓碗、开门、放入）。
- **研究空白**：缺乏能够主动推理复杂意图、分解为动作原语并生成顺序可供性地图的系统。
- **本文贡献**：
  - 提出 **顺序3D可供性推理（Sequential 3D Affordance Reasoning）** 任务，要求模型从复杂人类指令中推理并分割一系列可供性区域。
  - 构建首个大规模指令驱动的可供性分割基准，含 **180K 指令-点云对**（162K 单步 + 20K 顺序），覆盖23类物体。
  - 提出 **SeqAfford** 模型，利用多模态大语言模型（MLLM）的内在世界知识，实现顺序推理与细粒度可供性分割的统一框架。

## 2. 方法论

### 核心思想
- 基于预训练的3D MLLM（ShapeLLM），将其扩展出可供性分割能力：在词汇表中加入特殊标记 `<SEG>`，模型输出文本中包含 `<SEG>` token，每个 token 对应一个顺序步骤的分割结果。
- 设计多粒度语言-点云融合模块，将MLLM提出的分割 token 与点云特征深度融合，生成高质量可供性掩码。

### 关键技术细节
1. **3D MLLM 骨干**：采用 ShapeLLM-7B，其3D编码器 ReCon++ 通过多视角蒸馏预训练，LLM 为 LLaMA。冻结3D编码器，使用 LoRA（rank=8）进行高效微调。
2. **顺序可供性推理**：
   - 输入点云 `X_point` 和指令 `X_txt`，MLLM 生成包含多个 `<SEG>` 的文本 `~y_txt`。
   - 提取最后一层每个 `<SEG>` 对应的 embedding `h_seg^{(i)}`，经MLP投影为 `H_seg^{(i)}`。
3. **多粒度语言-点云融合模块**：
   - **多粒度特征传播**：对3D编码器中间特征进行分层上采样和FPS传播，生成密集特征 `f_dense`、稀疏特征 `f_sparse`。
   - **点-语言集成**：以 `H_seg^{(i)}` 为 query，`f_dense` 为 key/value 进行交叉注意力，结果与 `f_sparse` 融合，经解码器得到最终 mask `~y_mask`。
4. **训练损失**：联合优化 `L = λ_c L_c(文本生成) + λ_b L_b(BCE) + λ_d L_d(Dice)`，权重平衡。

## 3. 实验设计

### 数据集
- **来源**：基于 3D AffordanceNet（点云+标注）和 PartNet（网格渲染图）。
- **指令生成**：使用 GPT-4o 通过四种策略（仅文本、文本+网格渲染、文本+网格+HOI图像、文本+网格+场景描述）生成多样指令。
- **设置**：
  - **Seen**：训练/测试对象-可供性分布相似。
  - **Unseen**：测试时出现训练未见的对象-可供性组合（例如训练见过“抓杯子”，测试要求“抓耳机”）。
- **规模**：18K+ 点云实例，23个物体类别。

### 对比方法
- ReferTrans、ReLA、3D-SPS、IAGNet、PointRefer（LASO）。对于顺序任务，基线方法使用GPT将原指令拆分为单步指令后分别输入。

### 评估指标
- mIoU、AUC、SIM、MAE。

### 实验充分性
- **主实验**：在单任务（Seen/Unseen）和顺序任务上均报告结果，SeqAfford 在所有指标上超越基线。
- **消融实验**：
  - 移除多粒度语言-点融合模块（w/o MGLP），性能显著下降（单任务 mIoU 从19.5降至12.1，顺序任务从14.6降至11.7）。
  - 比较不同3D视觉编码器（ULIP、OpenShape、Recon++、Uni3D），Uni3D效果最佳。
- 实验公平客观：基线方法使用官方实现，顺序任务中统一提供真实顺序信息。

## 4. 资源与算力

- **GPU**：1张 NVIDIA A100 (40GB)。
- **训练 epoch**：10个 epoch（主实验），使用余弦学习率调度，warm-up 比例为0.03。
- **优化器**：AdamW，学习率 2e-4，权重衰减 0。
- **LoRA 配置**：rank=8，冻结3D编码器。
- **注意**：论文明确说明了单卡A100训练10个 epoch。

## 5. 实验数量与充分性

- **实验数量**：主实验（3个设置：Seen单任务、Unseen单任务、顺序任务）×多个指标 + 两组消融实验。
- **充分性**：
  - 全面对比了该任务上的主流方法（5种），包括专门的语言引导可供性模型 LASO。
  - 消融实验既验证了核心模块（MGLP）的有效性，也探索了编码器选择的影响。
  - 在 Unseen 设置下验证了开放世界泛化能力。
  - 提供定量和定性结果（图5展示了不同指令下的分割实例）。
- **公平性**：基线方法在顺序任务中使用真实顺序信息，避免了不公平比较。

## 6. 主要结论与发现

- SeqAfford 在单步和顺序可供性推理任务上均取得最佳结果，尤其在顺序任务中 mIoU 14.6% vs 次优14.3%（PointRefer*），AUC 84.2% vs 80.7%。
- 多粒度语言-点融合模块显著提升性能（+7.4 mIoU in single, +2.9 in sequential）。
- Uni3D 作为3D视觉编码器性能最优（mIoU 19.5%）。
- 定性结果显示模型能正确推理并分割复杂顺序操作（如“抓取耳机→佩戴”、“打开洗碗机→放入碗碟”）。

## 7. 优点

- **任务创新**：首次定义顺序3D可供性推理，填补了从简单指令到复杂多步操作之间的空白。
- **数据多样性**：通过四种GPT-4o提示策略生成指令，融合文本、2D图像、3D渲染等多模态信息，增强指令真实性和多样性。
- **模型设计**：将MLLM的分割 token 与点云特征进行多粒度交互，既保留MLLM的推理能力，又实现精细的3D密集预测。
- **泛化能力**：在 Unseen 设置下表现良好，表明模型学习了可供性概念而非过拟合特定对象。
- **高效率**：仅用1张A100训练10个 epoch，资源消耗可控。

## 8. 不足与局限

- **场景限制**：当前工作仅处理单个或多个独立物体点云，未涉及完整3D场景（如桌面、房间），缺乏对遮挡、空间关系的处理。
- **顺序依赖**：在顺序推理中，模型假设每步独立执行，未显式建模步骤间的状态变化（如物体被移动后点云变化）。
- **评估覆盖**：虽然对比了5种基线，但均为基于3D点云的方法，未与最新的2D/3D MLLM（如GPT-4V+3D投影）进行比较。
- **指令生成偏差**：GPT-4o生成的指令可能带有特定语言风格，真实用户指令可能更口语化或模糊。
- **可扩展性**：训练数据仅含23类物体，对于未见物体类别或完全不同的可供性类型（如“旋转”），泛化能力未充分验证。
- **计算资源报告较简**：仅提及单卡A100，未说明训练总时长或推理速度。

（完）
