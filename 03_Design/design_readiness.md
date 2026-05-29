# Design Readiness — 进入 Design 阶段前要补齐的信息

> **用途.** Design 阶段要产出 product spec / UX flows / system architecture / agent protocol / data model（见本目录 [`README.md`](README.md)）。但要把这些做对，目前缺一批**决策和输入**。本文按"是否阻塞设计开始"分级罗列。🔴 需要你拍板，🟡 给方向后我们来设计。

> **进度更新（2026-05-29）.** ✅ **B2** 已定（原型+演示+HTML，模板参考 beautiful-html-templates）。✅ **B3** 已定（Lark Wiki 为载体）——设计见 [`lark_wiki_mvp.md`](lark_wiki_mvp.md)。✅ **D2 入图 pipeline** 已落（Decompose-Match-Merge）——见 [`ingest_pipeline.md`](ingest_pipeline.md)，并部分回答 D1/D4/D12。⏳ **B1**（demo 楔子场景）仍待定。下一步阻塞项 = B1 + D7（协商协议）。

---

## 🔴 Blocking — 需要你先拍板（缺这些 design 无法真正开始）

### B1. Demo 楔子：一个具体场景 ⏳ 待定
Proposal 是抽象的产品愿景，但设计必须锚定**一个**最能体现"WikiGenius 明显更好"的工作流（[`../02_Research/km_trends.md`](../02_Research/km_trends.md) 自己提的 open question）。需要你定：
- 目标团队画像：团队规模？什么职能（工程 / 风控 / 跨职能）？
- 一个具体冲突故事：谁改了什么、和什么已有知识矛盾、Agent 如何介入（参考 Proposal 里 API rate limit 那个例子，但要落到你们真实的场景）。

### B2. Hackathon 交付形态与约束 ✅ 已定
- 交付物 = **可运行原型 + 现场演示 + HTML**（不再是 slides）；演示面模板参考 [`zarazhangrui/beautiful-html-templates`](https://github.com/zarazhangrui/beautiful-html-templates)（34 套、浏览器直开、无 build）。落地见 [`lark_wiki_mvp.md`](lark_wiki_mvp.md) §5。
- 仍可补充：时间预算、人手、评审标准权重（用于排优先级）。

### B3. 载体选型 ✅ 已定：Lark Wiki
押 **Lark Wiki** 作为载体，按 [`larksuite/cli`](https://github.com/larksuite/cli) 设计结构/权限/功能，目标是可运行 MVP 而非 PPT。完整载体映射、权限映射、Agent 链路、MVP 形态见 [`lark_wiki_mvp.md`](lark_wiki_mvp.md)。

---

## 🟡 Core Design Inputs — 有方向后我们设计，但需要你定方向

### 数据模型 / 知识图谱
- **D1. 节点粒度与边类型.** 一个"节点"是什么——事实 / 文档 / section / 实体？边有哪几类（引用 / 依赖 / 矛盾 / 取代）？这是整个系统的地基，目前完全未定义。
- **D2. 知识入图 pipeline.** ✅ 已定：**Decompose → Match → Merge**（消化而非堆砌，克制膨胀）——见 [`ingest_pipeline.md`](ingest_pipeline.md)。剩 Match 的具体实现（LLM/向量/混合）待定。
- **D3. 真值快照 + 时间旅行的数据结构.** Proposal 承诺"能重建 2025 Q4 的真值状态"，但这个快照怎么存、怎么回放，目前只有概念没有结构。
- **D4. Provenance schema（C4）.** "人类撰写 / User Agent 辅助 / 生成"的具体字段设计。

### 一致性 / 冲突引擎（这是 The Hard Problem）
- **D5. 语义矛盾检测的具体机制.** 纯 LLM 判断 / 规则引擎 / 混合？研究说"需要推理层"，但没有设计。
- **D6. 冲突 vs 兼容更新的判定 + impact-scope 阈值.** "局部更新 vs 结构性变更"要操作化成可执行的判定。
- **D7. 多 Agent 协商协议.** 状态机（proposed → negotiating → frozen → escalated → resolved）、消息格式、超时行为、升级链——Proposal 把它点名为核心难题，但还没有设计。
- **D8. 仲裁规则的显式化 + 版本化（C8 可靠性）.** 规则不能藏在 prompt 里，要显式、可版本控制。

### Agent 设计
- **D9. User Agent 的上下文/记忆模型.** 它持久化哪些上下文、怎么获知用户角色与历史。
- **D10. Team Agent 行动分类表（C9）.** 把每一类 Agent 行动映射到 a) 直接执行 / b) 建议+路由 / c) 拒绝+升级。
- **D11. 模型选型与成本模型.** 用哪个/哪些 LLM，调用成本与频次。

### UX / 信任界面（C6–C9）
- **D12. 关键 UX flows 的屏幕.** 提交变更、看到冲突、协商、看 provenance、"Agent 为什么这么裁决"（C7 透明）、"Team Agent 在做什么"（C6 可见）——目前都没有界面设计。
- **D13. 投递/通知 UX.** Agent 的主动推送落在哪里（与 B3 载体选型强相关）。

### 评估
- **D14. Demo 的可测成功指标.** 研究里有 TMS 衍生指标（differentiation / credibility / coordination，见 [`../02_Research/academic_takeaways_zh.md`](../02_Research/academic_takeaways_zh.md)）——需要从中挑出 demo 要证明的那一两个可量化指标。

---

## 建议的补齐顺序

1. 先答 **B1 / B2 / B3**（三个拍板）——它们决定后面所有设计的范围和形态。
2. 再定 **D1（节点/边）+ D7（协商协议）**——这两个是地基和核心难题，其余设计依赖它们。
3. 其余 🟡 项在 design 阶段迭代中补齐即可。

---

*Last updated: 2026-05-29*
