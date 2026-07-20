---
title: "The Devil is in Temporal Token: High Quality Video Reasoning Segmentation"
title_zh: 魔鬼在时序标记中：高质量视频推理分割
authors: "Gong, Sitong, Zhuge, Yunzhi, Zhang, Lu, Yang, Zongxin, Zhang, Pingping, Lu, Huchuan"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Gong_The_Devil_is_in_Temporal_Token_High_Quality_Video_Reasoning_CVPR_2025_paper.pdf"
tags: ["query:seg-llm"]
score: 8.0
evidence: 基于MLLM的视频推理分割，结合语义分割与大模型推理
tldr: "现有视频推理分割方法依赖单个特殊标记，难以捕捉空间复杂性和帧间运动。本文提出VRS-HQ，利用多模态大语言模型（MLLM）将丰富时空特征注入分层标记中，包括帧级<SEG>和时序级<TAK>标记。通过时序动态聚合和关键帧选择，显著提升了分割质量。实验表明该方法在多个数据集上达到最优性能，推动了基于推理的语义分割发展。"
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1804, \"height\": 583, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1707, \"height\": 771, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1702, \"height\": 700, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 817, \"height\": 502, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1513, \"height\": 616, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1591, \"height\": 578, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 1673, \"height\": 435, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 466, \"height\": 167, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 566, \"height\": 170, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-006.webp\", \"caption\": \"\", \"page\": 0, \"index\": 6, \"width\": 563, \"height\": 193, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-007.webp\", \"caption\": \"\", \"page\": 0, \"index\": 7, \"width\": 512, \"height\": 218, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-008.webp\", \"caption\": \"\", \"page\": 0, \"index\": 8, \"width\": 541, \"height\": 170, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-gong-the-devil-is-in-temporal-token-high-quality-video-reasoning-cvpr-2025-paper/table-009.webp\", \"caption\": \"\", \"page\": 0, \"index\": 9, \"width\": 559, \"height\": 144, \"label\": \"Table\"}]"
motivation: 现有视频推理分割方法使用单个标记，未能充分捕捉空间复杂性和时间动态。
method: "提出VRS-HQ方法，利用MLLM设计分层标记（帧级<SEG>和时序级<TAK>），并创新时序动态聚合和关键帧选择机制。"
result: 在多个基准上取得高质量视频推理分割结果，显著优于现有方法。
conclusion: 本研究展示了利用分层标记和MLLM进行精细化视频分割的潜力，为推理引导分割提供了新方向。
---

## Abstract
Existing methods for Video Reasoning Segmentation rely heavily on a single special token to represent the object in the keyframe or the entire video, inadequately capturing spatial complexity and inter-frame motion. To overcome these challenges, we propose VRS-HQ, an end-to-end video reasoning segmentation approach that leverages Multimodal Large Language Models (MLLMs) to inject rich spatiotemporal features into hierarchical tokens. Our key innovations include a Temporal Dynamic Aggregation (TDA) and a Token-driven Keyframe Selection (TKS). Specifically, we design frame-level <SEG> and temporal-level <TAK> tokens that utilize MLLM's autoregressive learning to effectively capture both local and global information. Subsequently, we apply a similarity-based weighted fusion and frame selection strategy, then utilize SAM2 to perform keyframe segmentation and propagation. To enhance keyframe localization accuracy, the TKS filters keyframes based on SAM2's occlusion scores during inference. VRS-HQ achieves state-of-the-art performance on ReVOS, surpassing VISA by 5.9%/12.5%/9.1% in J&F scores across the three subsets. These results highlight the strong temporal reasoning and segmentation capabilities of our method.

---

## 论文详细总结（自动生成）

### 1. 论文的核心问题与整体含义（研究动机和背景）
视频推理分割（Video Reasoning Segmentation, VRS）要求模型根据蕴含常识推理或时序逻辑的文本指令，在视频中分割出目标物体。现有方法（如VISA、VideoLISA）通常仅依赖单个特殊标记（如 `<SEG>` ）来表示关键帧或整段视频中的物体，这导致两个主要问题：  
- **空间复杂性与帧间运动欠捕获**：单个标记难以同时编码帧内的精细空间细节和跨帧的时间动态。  
- **关键帧检测不准确**：关键帧选择依赖外部模型（如LLaMA-VID），易出错且无法端到端训练。  
- **分割与传播解耦**：使用独立的SAM和外部跟踪器（如XMem），无法统一优化。  

本文提出 **VRS-HQ**，通过多模态大语言模型（MLLM）生成**层级式特殊标记**（帧级 `<SEG>` 和时序级 `<TAK>` ），并设计时序动态聚合（TDA）与标记驱动的关键帧选择（TKS）机制，实现高质量、端到端的视频推理分割。

### 2. 论文提出的方法论
#### 核心思想
将MLLM（选用Chat-UniVi）的强时序推理能力与SAM2的统一分割‑传播能力结合，通过层级标记分别编码帧级空间信息与视频级时序信息，再以相似度加权融合，并利用遮挡分数进行智能关键帧选择。

#### 关键技术细节
- **时序标记编码（§3.1）**：在MLLM词表中新增 `<SEG>`（帧级）和 `<TAK>`（时序级）特殊标记。设计对话模板：“USER: Please find {expression} in the Reference Video and segment it in each frame and the entire video respectively.” MLLM自回归生成包含多个 `<SEG>` 和一个 `<TAK>` 的响应。提取最后一层的嵌入 `h_seg ∈ R^{T'×d'}` 和 `h_tak ∈ R^{1×d'}`，经MLP投影到SAM2特征空间得到 `h_seg, h_tak`。
- **时序动态聚合（TDA, §3.2）**：计算各帧 `<SEG>` 与 `<TAK>` 的余弦相似度 `λ_i`，归一化后加权融合：  
  `h'_tak = h_tak + α * Σ(λ_i * h_seg[i])`  
  其中α为融合系数（设为0.1），使时序标记吸收帧级空间细节，同时保持时序一致性。
- **标记驱动的关键帧选择（TKS, §3.3）**：
  - **训练时**：选择与 `h_tak` 相似度最高的帧作为关键帧。
  - **推理时**：先使用CLIP选取与文本最匹配的锚帧进行全局采样（`T̂` 帧）；对每帧，将其特征与融合后的 `h'_tak` 输入SAM2的掩码解码器，得到**遮挡分数** `S_o ∈ R^{T̂×1}`（反映目标是否存在）；最后结合软最大归一化的遮挡分数与标记相似度分数，确定最佳关键帧。
- **掩码解码与传播（MDP, §3.4）**：将关键帧特征和 `h'_tak` 输入SAM2掩码解码器生成关键帧掩码，随后利用SAM2的记忆机制将掩码传播至相邻帧及整段视频，实现单阶段端到端流程。
- **训练目标（§3.5）**：含文本生成损失（交叉熵）和掩码损失（BCE + DICE），权重分别为1、1、2、0.5。

### 3. 实验设计
#### 数据集与基准
- **视频推理分割（VRS）**：ReVOS（含 `referring`、`reasoning`、`overall` 三个子集）。
- **视频指代分割（RVOS）**：Ref‑YouTube‑VOS、Ref‑DAVIS17、MeViS。
- **图像指代与推理分割**：refCOCO/+/g、ReasonSeg（val/test）。
- **训练数据**：LLaVA‑Instruct‑150k、Video‑ChatGPT的QA数据、多个语义/指代/推理分割数据集（ADE20K、COCO‑Stuff、PACO‑LVIS、PASCALPart、Ref‑YouTube‑VOS、Ref‑DAVIS17等）。

#### 对比方法
包括MTTR、LMPM、ReferFormer、LISA、TrackGPT、VISA（7B/13B）、VideoLISA等。

#### 评估指标
视频： **J**（区域相似度）、**F**（轮廓准确率）、**J&F**（平均）；图像：**gIoU**、**cIoU**；额外：**R**（鲁棒性分数，处理负样本能力）。

### 4. 资源与算力
- **GPU**：4块NVIDIA A800（80GB）。
- **优化器**：AdamW（lr=0.0003，无权重衰减），WarmupDecayLR调度（100步预热）。
- **训练配置**：DeepSpeed ZeRO？未具体说明；每GPU batch size=1，梯度累积32，总batch size=128；训练 **7500次迭代**。
- **微调方式**：Chat‑UniVi通过LoRA（rank=8）微调，SAM2部分参数冻结；掩码解码器与MLP投影层全参优化。  
文中未报告具体训练时长（小时数）。

### 5. 实验数量与充分性
**实验数量**非常丰富，包括：
- **主要对比**：在ReVOS三个子集（表1）、三个RVOS数据集（表2）、图像分割三个基准（表3）上全面对比。
- **消融实验**：
  - 组件消融（表4）：移除TDA、TKS等。
  - 融合系数α（表5）：0、0.1、0.25、0.5。
  - 关键帧选择策略（表6）：仅用CLIP分数、仅用标记相似度、仅用遮挡分数、联合使用。
  - 推理抽样帧数（表7）：1～12帧与非固定帧数。
  - 掩码解码与传播策略（表8）：SAM+单帧、SAM2+单帧、多帧训练/推理组合。
  - 采样策略（表9）：随机、均匀、CLIP引导。
- **可视化**：分割图对比（图3）、特征图对比（图4）印证TDA有效性。

**充分性与公平性**：
- 所有实验使用相同MLLM骨干（Chat‑UniVi 7B/13B）与最先进方法对比。
- 消融实验控制变量，指标全面（J、F、J&F）。
- 在多数据集、多任务上验证，结论具有鲁棒性。

### 6. 论文的主要结论与发现
- VRS‑HQ在ReVOS上大幅超越此前最佳VISA‑13B：**J&F分别提升5.9%（referring）、12.5%（reasoning）、9.1%（overall）**，鲁棒性R提升4.4%。
- 在RVOS基准上，J&F提升7.3%（Ref‑YouTube‑VOS）和5.6%（Ref‑DAVIS17），在运动密集的MeViS上提升6.4%。
- 在图像分割任务中，性能与LISA/VideoLISA相当（略低），说明模型更擅长视频场景。
- **层级标记与TDA**有效聚合帧级空间细节与时序语义，**TKS**利用遮挡分数显著提升关键帧定位。
- 使用SAM2统一分割与传播实现端到端，优于分离的SAM+XMem方案。

### 7. 优点
- **创新性**：提出帧级与视频级分层标记，突破单标记瓶颈；TDA与TKS设计巧妙，将标记相似度与SAM2遮挡分数结合。
- **性能卓越**：在多个视频基准上创下新SOTA，差距显著。
- **端到端**：无需外部关键帧检测器与跟踪器，训练和推理流程统一。
- **消融充分**：深入分析了融合系数、关键帧选择、采样策略等超参数影响，设计严谨。
- **可复现**：开源代码与模型权重（文中提及）。
- **鲁棒性**：负样本处理能力（R分数）明显优于以往方法。

### 8. 不足与局限
- **图像任务性能偏低**：在refCOCO、ReasonSeg上略低于VideoLISA，作者指出原因是训练偏重视频数据以及依赖SAM2记忆机制对单帧不友好。
- **计算资源要求高**：4×A80 GPU训练，且需同时运行MLLM与SAM2，部署成本较高；未报告推理速度或FLOPs。
- **依赖预训练模型**：MLLM（Chat‑UniVi）和SAM2均为预训练，微调后泛化能力可能受限于预训练数据分布。
- **可扩展性未验证**：实验视频长度未见详细说明，极端长视频或复杂多目标场景下的传播稳定性有待测试。
- **未讨论失败案例**：可视化仅展示成功案例，缺乏对错误模式的分析（如遮挡严重、目标消失等）。
- **消融实验较少在图像任务上验证**：图像分割仅展示单项结果，缺内部组件消融。

（完）
