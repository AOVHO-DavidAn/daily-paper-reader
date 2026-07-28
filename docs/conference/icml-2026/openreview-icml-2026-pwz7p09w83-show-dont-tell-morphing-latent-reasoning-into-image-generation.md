---
title: "Show, Don't Tell: Morphing Latent Reasoning into Image Generation"
title_zh: 别说出来：将隐式推理融入图像生成
authors: "Harold Haodong Chen, Xinxiang Yin, Wen-Jie Shu, Hongfei Zhang, Zixin Zhang, Chenfei Liao, Litao Guo, Qifeng Chen, Ying-Cong Chen"
date: 2026-04-30
pdf: "https://openreview.net/pdf/73e157bb6458e94aa149380b05b0aa3be43609c6.pdf"
tags: ["query:lr"]
score: 9.0
evidence: 将隐式隐推理集成到文本到图像生成中
tldr: 针对现有文本到图像生成缺乏动态推理能力、中间过程需频繁解码编码导致效率低的问题，提出LatentMorph框架。该框架将隐式隐推理无缝融入生成过程，通过冷凝器等组件在隐空间中迭代优化视觉表示。实验表明，相比传统方法，LatentMorph在生成质量和推理效率上均有显著提升，实现了更自然的生成式推理。
source: ICML-2026-Accepted
selection_source: conference_retrieval
motivation: 现有文本到图像生成缺乏动态推理能力，中间解码编码导致信息丢失和效率低下。
method: 提出LatentMorph，在隐空间中进行迭代推理，通过冷凝器组件汇总中间状态。
result: 在多个文本到图像基准上取得更优的生成质量和推理速度。
conclusion: 隐式隐推理能有效提升图像生成的动态性和效率。
---

## Abstract
Text-to-image (T2I) generation has achieved remarkable progress, yet existing methods often lack the ability to dynamically reason and refine during generation--a hallmark of human creativity. Current reasoning-augmented paradigms mostly rely on explicit thought processes, where intermediate reasoning is decoded into discrete text at fixed steps with frequent image decoding and re-encoding, leading to inefficiencies, information loss, and cognitive mismatches. To bridge this gap, we introduce **LatentMorph**, a novel framework that seamlessly integrates implicit latent reasoning into the T2I generation process. At its core, LatentMorph introduces four lightweight components: (***i***) a **condenser** for summarizing intermediate generation states into compact visual memory, (***ii***) a **translator** for converting latent thoughts into actionable guidance, (***iii***) a **shaper** for dynamically steering next image token predictions, and (***iv***) an RL-trained **invoker** for adaptively determining when to invoke reasoning. By performing reasoning entirely in continuous latent spaces, LatentMorph avoids the bottlenecks of explicit reasoning and enables more adaptive self-refinement. Extensive experiments demonstrate that LatentMorph **(I)** enhances the base model Janus-Pro by 16% on GenEval and 25% on T2I-CompBench; **(II)** outperforms explicit paradigms (*e.g.*, TwiG) by 15% and 11% on abstract reasoning tasks like WISE and IPV-Txt, **(III)** while reducing inference time by 44% and token consumption by 51%; and **(IV)** exhibits 71% cognitive alignment with human intuition on reasoning invocation.

---

## 论文详细总结（自动生成）

# 论文详细中文总结

## 1. 论文的核心问题与整体含义

- **研究背景**：文本到图像（T2I）生成领域虽取得显著进展，但现有方法缺乏生成过程中的动态推理与自我修正能力——这是人类创作过程的标志性特征。
- **核心问题**：当前主流的推理增强范式（如显式思维链）依赖将中间推理结果解码为离散文本，在固定步骤进行频繁的图像解码与重新编码，导致效率低下、信息丢失以及认知不匹配（cognitive mismatch）。
- **整体含义**：本文提出一种全新的隐式隐推理（implicit latent reasoning）框架，将推理过程无缝融入连续隐空间，避免显式推理的瓶颈，实现更自适应、更高效的生成式推理。

## 2. 论文提出的方法论

- **核心思想**：设计名为 **LatentMorph** 的框架，在连续隐空间中执行完整的推理过程，通过四个轻量级组件实现中间状态的迭代优化与下一步生成引导。
- **关键技术细节**：
  - **冷凝器（Condenser）**：将中间生成状态总结为紧凑的视觉记忆（visual memory），压缩信息并保持关键上下文。
  - **翻译器（Translator）**：将隐空间中的“思想”（latent thoughts）转换为可操作的引导信号（actionable guidance）。
  - **塑造器（Shaper）**：动态引导下一个图像令牌（token）的预测，实现逐令牌的精细化调控。
  - **调用器（Invoker）**：基于强化学习（RL）训练，自适应判断何时需要触发推理，避免不必要的计算开销。
- **算法流程（文字描述）**：
  1. 输入文本提示，通过基础图像生成模型（如Janus-Pro）生成初始隐表示。
  2. 在生成过程中，调用器根据当前生成的视觉状态（由冷凝器总结）决定是否触发推理。
  3. 若需要推理，冷凝器生成紧凑视觉记忆，翻译器将其转化为引导信号，塑造器据此调整后续令牌预测概率。
  4. 所有推理步骤均在隐空间内完成，不涉及解码为图像或文本。
  5. 推理完成后继续生成，直至图像完成。整个流程形成闭环的自适应优化。

## 3. 实验设计

- **数据集/场景**：
  - 通用T2I生成：在 **GenEval** 和 **T2I-CompBench** 两个标准基准上评估生成质量。
  - 抽象推理任务：使用 **WISE**（推测为与视觉常识/抽象推理相关）和 **IPV-Txt**（图像-文本语义对齐）测试复杂推理能力。
- **基准方法**：
  - 基础模型：**Janus-Pro**（作为基线和改进对象）。
  - 显式推理范式：**TwiG**（Topic-wise Image Generation，显式中间解码）等。
- **对比方法**：与当前最先进的显式推理增强方法及无推理基线进行对比。

## 4. 资源与算力

- 论文摘要及元数据**未明确说明**训练所使用的具体GPU型号、数量、训练时长等算力资源。仅提到框架是轻量级的（四个组件较小），但未披露完整训练开销。需要查阅全文才可获知。

## 5. 实验数量与充分性

- **实验组数**：主要涉及四大类实验：
  1. 在GenEval和T2I-CompBench上对比LatentMorph与基础模型Janus-Pro的性能。
  2. 在抽象推理任务（WISE、IPV-Txt）上对比显式推理范式（TwiG）。
  3. 推理效率评估（推理时间减少44%，token消耗减少51%）。
  4. 认知对齐评估（人类直觉对齐度71%）。
- **充分性与公平性**：
  - 覆盖了通用生成质量、复杂推理、效率、人类认知对齐四个维度，较为全面。
  - 对比方法包括最相关的显式推理基线，且在同一基础模型上改进，公平性较好。
  - 但摘要中未提及消融实验（如移除某组件的效果）、超参数敏感性分析等，充分性有待全文确认。

## 6. 论文的主要结论与发现

1. **性能提升显著**：LatentMorph在GenEval上比基础模型Janus-Pro提升16%，在T2I-CompBench上提升25%。
2. **超越显式推理范式**：在抽象推理任务WISE上比TwiG高15%，在IPV-Txt上高11%。
3. **效率优势突出**：推理时间减少44%，token消耗减少51%，证明隐空间推理的高效性。
4. **认知对齐良好**：推理调用点与人类直觉的匹配度达71%，说明模型生成的推理时机符合人类认知模式。
5. **总体结论**：隐式隐推理（LatentMorph）能有效提升图像生成的动态性与效率，开创了一种新的生成式推理范式。

## 7. 优点

- **方法创新性**：首次将推理过程完全置于连续隐空间，避免了频繁编解码导致的效率损失和信息丢失，是T2I生成与推理结合的重要突破。
- **组件设计精巧**：冷凝器、翻译器、塑造器、调用器四个组件各司其职，且通过RL训练调用器实现自适应，体现端到端学习的灵活性。
- **实验全面且结果领先**：在多个基准和任务上取得一致优势，且效率指标显著优于显式方法。
- **轻量化**：四个组件均为轻量级，易集成到现有T2I模型（如Janus-Pro），具备良好扩展性。

## 8. 不足与局限

- **算力与复现成本未公开**：缺少训练所需GPU资源、时间等细节，不利于其他研究者复现与评估可复制性。
- **消融实验缺失**：未在摘要中报告各组件独立贡献的消融结果，无法判断每个改进点的实际效果。
- **任务覆盖有限**：仅测试了标准T2I基准和两个抽象推理任务，在更复杂场景（如多对象交互、风格迁移、长文本描述）下的表现未知。
- **认知对齐评估单一**：71%的人类对齐度仅基于推理调用判断，模型是否生成符合人类审美的图像仍需更全面的人因实验验证。
- **潜在偏差风险**：基础模型Janus-Pro的预训练数据分布可能引入社会偏见，LatentMorph本身未做去偏处理。
- **应用限制**：当前框架依赖特定基础模型（Janus-Pro），对其他T2I架构（如扩散模型）的通用性需进一步探索。

（完）
