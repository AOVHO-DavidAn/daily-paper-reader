---
title: "Not Only Text: Exploring Compositionality of Visual Representations in Vision-Language Models"
title_zh: 不仅仅是文本：探索视觉-语言模型中视觉表示的组合性
authors: "Berasi, Davide, Farina, Matteo, Mancini, Massimiliano, Ricci, Elisa, Strisciuglio, Nicola"
date: 2025-06-01
pdf: "https://openaccess.thecvf.com/content/CVPR2025/papers/Berasi_Not_Only_Text_Exploring_Compositionality_of_Visual_Representations_in_Vision-Language_CVPR_2025_paper.pdf"
tags: ["query:lr"]
score: 7.0
evidence: 通过GDE框架探索视觉-语言模型潜空间中的组合性
tldr: 本文研究视觉-语言模型中视觉嵌入空间的组合性结构，提出测地线可分解嵌入（GDE）框架，通过几何感知的组合结构逼近图像表示，揭示视觉表示在潜空间中的组合模式。该方法为多模态隐空间推理提供了重要基础。
source: CVPR-2025-Accepted
selection_source: conference_retrieval
figures_json: "[{\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-berasi-not-only-text-exploring-compositionality-of-visual-representations-in-vision-language-cvpr-2025-paper/fig-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 848, \"height\": 573, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-berasi-not-only-text-exploring-compositionality-of-visual-representations-in-vision-language-cvpr-2025-paper/fig-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 852, \"height\": 803, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-berasi-not-only-text-exploring-compositionality-of-visual-representations-in-vision-language-cvpr-2025-paper/fig-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 844, \"height\": 533, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-berasi-not-only-text-exploring-compositionality-of-visual-representations-in-vision-language-cvpr-2025-paper/fig-004.webp\", \"caption\": \"\", \"page\": 0, \"index\": 4, \"width\": 810, \"height\": 330, \"label\": \"Figure\"}, {\"url\": \"assets/figures/cvpr-2025-accepted/cvpr-2025-berasi-not-only-text-exploring-compositionality-of-visual-representations-in-vision-language-cvpr-2025-paper/fig-005.webp\", \"caption\": \"\", \"page\": 0, \"index\": 5, \"width\": 813, \"height\": 756, \"label\": \"Figure\"}]"
tables_json: "[{\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-berasi-not-only-text-exploring-compositionality-of-visual-representations-in-vision-language-cvpr-2025-paper/table-001.webp\", \"caption\": \"\", \"page\": 0, \"index\": 1, \"width\": 1804, \"height\": 235, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-berasi-not-only-text-exploring-compositionality-of-visual-representations-in-vision-language-cvpr-2025-paper/table-002.webp\", \"caption\": \"\", \"page\": 0, \"index\": 2, \"width\": 1799, \"height\": 435, \"label\": \"Table\"}, {\"url\": \"assets/tables/cvpr-2025-accepted/cvpr-2025-berasi-not-only-text-exploring-compositionality-of-visual-representations-in-vision-language-cvpr-2025-paper/table-003.webp\", \"caption\": \"\", \"page\": 0, \"index\": 3, \"width\": 856, \"height\": 442, \"label\": \"Table\"}]"
motivation: 现有研究未能充分探索视觉嵌入空间的组合性结构，限制了多模态模型的理解能力。
method: 提出GDE框架，利用测地线距离在潜空间中构建几何感知的组合表示。
result: 实验证明GDE有效捕获了视觉表示的组合模式，提升了多模态理解性能。
conclusion: 该工作揭示了视觉潜空间的组合性，为多模态推理提供了新视角。
---

## Abstract
Vision-Language Models (VLMs) learn a shared feature space for text and images, enabling the comparison of inputs of different modalities. While prior works demonstrated that VLMs organize natural language representations into regular structures encoding composite meanings, it remains unclear if compositional patterns also emerge in the visual embedding space. In this work, we investigate compositionality in the image domain, where the analysis of compositional properties is challenged by noise and sparsity of visual data. We address these problems and propose a framework, called Geodesically Decomposable Embeddings (GDE), that approximates image representations with geometry-aware compositional structures in the latent space. We demonstrate that visual embeddings of pre-trained VLMs exhibit a compositional arrangement, and evaluate the effectiveness of this property in the tasks of compositional classification and group robustness. GDE achieves stronger performance in compositional classification compared to its counterpart method that assumes linear geometry of the latent space. Notably, it is particularly effective for group robustness, where we achieve higher results than task-specific solutions. Our results indicate that VLMs can automatically develop a human-like form of compositional reasoning in the visual domain, making their underlying processes more interpretable. Code is available at https://github.com/BerasiDavide/vlm_image_compositionality.

---

## 论文详细总结（自动生成）

好的，作为一名资深学术论文分析助手，以下是对给定论文的结构化、深入、客观的中文总结。

# 论文深度总结：不仅仅是文本：探索视觉-语言模型中视觉表示的组合性

## 1. 论文的核心问题与整体含义（研究动机和背景）

*   **核心问题**：大规模视觉-语言模型（VLM，如 CLIP）在共享的文本-图像嵌入空间中学习。先前的研究已经证明，文本嵌入空间存在组合性结构（即复杂概念可以由更简单的“原初”概念向量线性组合而成）。然而，视觉嵌入空间是否也存在类似的组合性模式，目前尚不清楚。
*   **研究动机**：
    *   人类视觉感知具有组合性，人类通过组合简单的视觉元件来理解复杂场景。如果 VLM 的视觉嵌入也具备这种特性，将极大地增强模型的可解释性和推理能力。
    *   文本组合性分析面临的主要挑战（如通过文本字符串轻松生成任何概念组合）在视觉领域变得更为严峻。
    *   **两大核心技术挑战**：
        1.  **噪声**：图像包含大量与目标概念无关的背景、纹理等额外信息，导致嵌入向量含有噪声。
        2.  **稀疏性**：并非所有原初概念的组合（例如，“蓝色 狗”）在现实图像数据集中都存在，导致训练数据覆盖不全。
*   **整体含义**：本文旨在**首次系统地探索** VLM 视觉嵌入空间的组合性，并提出一种旨在克服上述挑战的有效方法。

## 2. 论文提出的方法论：核心思想、关键技术细节

*   **核心思想**：视觉嵌入空间是一个**黎曼流形**（特别是球面，因为 CLIP 嵌入被归一化到单位球面），欧氏空间中的线性组合无法准确描述其上的组合性。因此，本文提出 **测地线可分解嵌入（GDE）** 框架，在流形的**切空间**上进行概念的分解与组合，再通过指数映射将结果映射回流形。
*   **关键概念定义**：
    *   **测地线可分解性**：一个嵌入集合是“测地线可分解”的，如果其中的每个复合概念 `z = (z1, ..., zs)` 的嵌入 `uz` 可以由其原初概念 `zi` 在切空间的向量 `v_zi` 之和，通过指数映射 `Exp_μ` 得到：`uz = Exp_μ(v_z1 + ... + v_zs)`。其中 `μ` 是这些嵌入的**内在均值**。
*   **技术细节（算法流程）**：
    1.  **输入**：一组带有标签（如“红色 汽车”）的图像嵌入 `{u_(z,e)}`，其中 `z` 是复合概念，`e` 是代表噪声的索引（假设每个 `z` 有 `k` 个含噪不同版本）。
    2.  **噪声处理**：对于每个复合概念 `z`，其 `k` 个含噪嵌入被不同权重 `p_(z,e)`（由 CLIP 文本-图像匹配概率决定）加权。在切空间中对这些加权嵌入取平均，得到一个去噪的、代表该复合概念的单一嵌入 `v_z`。这一步解决了“噪声”问题。
    3.  **稀疏性处理**：当只有部分复合概念（子集 `Z'`）有图像时，通过计算有数据的原初概念 `zi` 在切空间中的平均向量 `v_zi` 来估计所有原初概念的方向。这样，即使没见过的组合（如 `Z \ Z'`）也能被表示出来。这一步解决了“稀疏性”问题。
    4.  **获取原初方向**：对于每个原初概念 `zi`（如“红色”或“汽车”），其切向量 `v_zi` 由所有包含该原初概念的已知复合概念的切向量 `v_z` 的平均值得到。
    5.  **构建任意组合**：对于任意目标组合 `(a, o)`，其“可分解近似”嵌入 `ũ_(a,o)` 通过组合对应的原初方向并映射回流形得到：`ũ_(a,o) = Exp_μ(v_a + v_o)`。

    这整个过程框架性地解决了视觉数据固有的**噪声**和**稀疏性**难题。

## 3. 实验设计

*   **使用数据集**：
    *   **组合分类**：UT-Zappos（鞋类图像，12 种对象，16 种材质属性）、MIT-States（自然图像，115 种状态/属性，245 种对象）。
    *   **群体鲁棒性**：Waterbirds（水鸟/陆鸟 + 水/陆地背景，存在虚假相关）、CelebA（头发颜色 + 性别，存在虚假相关）。
*   **Benchmark 与评价指标**：
    *   **组合分类**：采用广义零样本学习（GZSL）的封闭世界（Closed-world）和开放世界（Open-world）两种场景。评价指标包括属性/对象准确率（ATTR/OBJ）、已见/未见类别的联合调和均值（HM）和曲线下面积（AUC）。
    *   **群体鲁棒性**：采用最差组准确率（WG）和平均准确率（AVG），以及两者之间的差距（GAP）。目标是在保持平均准确率的同时，显著提升最差组的准确率。
*   **对比方法**：
    *   **组合分类**：零样本 CLIP 基线、线性可分解嵌入（LDE，旨在验证流形几何的重要性）、以及它们在文本模态上的对应版本。
    *   **群体鲁棒性**：CLIP 基线、LDE、以及多种专门用于去偏或提升鲁棒性的方法，包括 ERM（经验风险最小化，使用线性探针或适配器）、DFR（深度特征重加权）、CA（对比适配器）和 FairerCLIP。

## 4. 资源与算力

*   文中**未明确说明**训练模型或运行主要实验所消耗的具体算力（如 GPU 型号、数量、训练时长）。作者仅提到“在 ISCRA 倡议下使用 CINECA 的高性能计算资源和支持” 以及在致谢部分感谢了支持。

## 5. 实验数量与充分性

*   **实验数量**：论文报告了多个维度的实验，数量较为充分。
    *   **核心实验 1**：在两个数据集（UT-Zappos, MIT-States）、两个场景（封闭、开放世界）、多种 backbone（CLIP ViT-L/14, RN50, SigLIP）下进行组合分类实验。
    *   **核心实验 2**：在两个数据集（Waterbirds, CelebA）上进行群体鲁棒性实验。
    *   **消融/分析实验**：进行了 backbone 的消融实验（Tab. 2）、数据效率实验（Fig. 4）、不同 `k` 值的可视化实验（Fig. 3）。
    *   **可视化实验**：使用扩散模型生成图像，直观展示分解后嵌入的语义质量（Fig. 5）。
*   **充分性与公平性评估**：
    *   **实验充分**：实验覆盖了分割、分类、鲁棒性、生成等多种任务，并考虑了多个主流 backbone 和对比方法，结论具有较好的泛化性。
    *   **实验公平**：对比方法均为公开的标准或最新方法，且在同一 backbone 下公平比较。对于 LDE 方法，作者进行了复现；对提出的 GDE 框架，设置了文本（TEXT）和图像（IMAGE）两种模态的对比，隔离了模态差异的影响。群体鲁棒性实验使用了标准的数据划分（来自 [58]）。
    *   **结论客观**：实验结果清晰展示了 GDE 相比 LDE 和 CLIP 基线的优势，尤其是在处理视觉数据的噪声和稀疏性方面。结果符合论文的理论预期。

## 6. 论文的主要结论与发现

1.  **视觉嵌入具有组合性**：预训练 VLM 的视觉嵌入空间**确实存在**类似文本嵌入的组合性结构。
2.  **流形几何至关重要**：与文本不同，视觉嵌入的组合性**不能用简单的线性模型有效捕获**。考虑流形内在几何的 GDE 框架（基于测地线距离）明显优于忽视几何的线性可分解嵌入（LDE）。
3.  **GDE 框架有效**：GDE 能有效提取解耦的原初概念向量（如“属性”和“对象”），并通过组合这些向量来近似未见过的复合概念。
4.  **应用效果显著**：
    *   在**组合分类**任务中，GDE 显著优于 CLIP 和 LDE，尤其在对象-属性组合多样、视觉区分度高的 UT-Zappos 数据集上。
    *   在**群体鲁棒性**任务中，GDE 直接使用解耦的对象嵌入进行分类，取得了与或优于许多专门训练的去偏方法（如 FairerCLIP）的效果，展示了强大的消除虚假相关能力。
    *   **数据效率高**：只需少量数据（约 25%）就能获得非常高的 WG 准确率。
5.  **可解释性与可控性**：GDE 分解出的向量可以用于控制图像生成（如生成特定属性-对象组合，甚至混合动物物种），增强了模型的可解释性与可控性。

## 7. 优点（亮点）

*   **方法的开创性**：首次系统性地研究并实现了 VLM 视觉嵌入空间的组合性，填补了该领域空白。
*   **问题建模的精确性**：准确识别并形式化了视觉分析中的两个核心难题——噪声和稀疏性，并提出了针对性的解决方案（加权平均及部分数据估计）。
*   **几何直觉的正确性**：基于黎曼流形切空间的分解，是对 CLIP 球面嵌入空间的最佳近似，这种“几何感知”的方法比传统的线性方法更符合数据分布的内在规律。
*   **无需重新训练的实用价值**：GDE 是一种**训练即用（training-free）** 的方法，无需微调 VLMs，直接利用预训练模型的输出，计算成本低且易于部署。
*   **广泛的应用潜力**：实验证明了 GDE 在组合分类、群体鲁棒性、生成等多个任务上的有效性，展示了其作为基础工具的潜力。

## 8. 不足与局限

*   **原初概念集合的限制**：GDE 要求预定义原初概念的集合（`Z_i`），这是一种**格子（lattice）结构**，即假设概念只能由固定的、离散的原初概念组合而成。这限制了模型处理更开放、不存在明确标签组合的场景。
*   **噪声处理的局限性**：对图像噪声（即额外信息）的处理依赖于 CLIP 文本-图像匹配概率，假设该模型能有效识别主要概念，这可能对图像内容高度复杂的场景效果不佳。
*   **计算与理论上的近似**：方法本身是一个近似优化（利用切空间线性近似代替流形上的精确优化），并且需要计算所有图像嵌入的加权内在均值和对数映射，对于具有大量概念的超大型数据集，计算量可能较大。
*   **未覆盖所有范式**：论文主要聚焦于“对象-属性”这种二元组合范式，未探索更复杂的组合（如关系、空间布局、动作）或更细粒度的概念分解。
*   **实验公平性（细微局限）**：在 MIT-States 上的绝对性能（AUC）与 CLIP 相比存在差距（尽管 GDE 相对性能提升更高），这可能源于该数据集的标注噪声和标签定义的模糊性，GDE 对这种复杂自然图像的建模能力仍有待提升。

（完）
