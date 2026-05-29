# 工程实现参考：适合 WikiGenius 的开源仓库调研

> **用途.** 为 Design 阶段的引擎设计（D1 图模型 / D2 入图 / D5 矛盾检测 / D7 协商协议 + 真值压缩）提供工程先验：哪些开源仓库能直接用、能借鉴、或定义了正确的范式。
>
> **范围（按你确认的口径）.** Python 优先；**模型无关**；每个领域给一个 **demo 快选（fast pick）** + 一个 **面向未来的方案（future-grade）**；四大引擎支柱全覆盖。
>
> **核验时间 2026-05.** 仓库 star/活跃度/license 会变，demo 前需复核（见末尾「待确认」）。

---

## 0. 头号结论 + 边界

**头号推荐：[Graphiti](https://github.com/getzep/graphiti)（getzep/graphiti）** 一个仓库就吃掉 WikiGenius 三块最难的东西：

- **双时态知识图谱**：每条边带 `valid_at` / `invalid_at`，区分"何时为真"与"何时被记录"——直接支持"回问 Q4 2025 的真值"。
- **事实失效而非删除**：信息变化时旧事实被 *invalidate* 而非丢弃——这就是 WikiGenius 的「被取代检测 + 真值无损」。
- **LLM 矛盾检测**：用 LLM 比对新边与语义相关的旧边，发现冲突时用时态元数据更新/失效而非覆盖。

换句话说，Graphiti 几乎是 WikiGenius「真值压缩」那一章的参考实现。它会在下面第 2、3、4 节反复出现。

**边界：载体 Lark 已经覆盖的，不要重造。** Lark Docs 自带多人实时协同、文档版本历史。所以**字符级 CRDT 协同**这块大体委托给载体；WikiGenius 真正要自建的是**语义层**——语义真值版本、跨文档矛盾检测、双层 Agent 协商。下面按这个判断排优先级。

---

## 1. 多 Agent 框架 + 协商（D7 / D10）

**WikiGenius 要什么**：双层 Agent；本地处理 vs 升级的决策；跨 Agent 后台协商/仲裁；变更状态机（proposed → frozen → escalated → resolved）。

| 角色 | 仓库 | 为什么 |
|------|------|--------|
| **Fast pick** | [CrewAI](https://github.com/crewAIInc/crewAI) | 角色制 agent 团队 + 任务委派，上手成本最低，最快搭出"User Agent / Team Agent / Owner 升级链"的可演示骨架；已加 A2A 支持。 |
| **Future-grade** | [LangGraph](https://github.com/langchain-ai/langgraph)（v1.0） | 图式 agent：节点 + 共享状态天然映射 WikiGenius 的**变更状态机、审计轨迹、回滚点**——正好对应冻结/解冻/重评估。企业向，生产就绪。 |
| 工具层（MVP 用） | **MCP**（Model Context Protocol） | agent↔工具：把 `lark-cli` 包成 agent 可调的工具层。全内部场景也照用。 |
| 内部 agent 协调（MVP 用） | **框架原生**（LangGraph 边 / CrewAI / 共享状态） | User↔Team↔Owner 的协商升级在所选框架内实现。这些都是你自己造、互为白盒的内部 agent，不需要跨黑盒协议。 |
| A2A（**未来可选，不进 MVP**） | A2A（Agent2Agent） | A2A 解决的是"互为黑盒的 agent 跨边界互操作"。WikiGenius 全内部时用不到——仅当**跨组织 / 跨厂商**协作时才有意义，放未来展望（成熟度调研见 §6）。 |
| 也看 | [AutoGen](https://github.com/microsoft/autogen)（对话式多 agent 辩论，贴合"协商"语义）；OpenAI Agents SDK / [Pydantic-AI](https://github.com/pydantic/pydantic-ai)（类型安全、模型无关） | |

**注意（诚实）**：没有现成的"知识仲裁"框架。上述框架解决的是 agent 编排与通信，**协商/仲裁协议本身仍要自建在它们之上**——这正是 Proposal 的 The Hard Problem，框架只是地基。

**协调模型参考（借模型，非依赖）：[Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)（Nous Research）.** 一个 SQLite 持久化的共享任务板，用"durable 行 + 原子认领 + 父子依赖放行 + heartbeat/TTL/熔断"协调多 agent 并发——正好映射 Team Agent 同时应对多个 User Agent 请求、冲突排队与升级。**只借协调骨架**：它管*流程*不管*内容矛盾*（一致性仍靠 §2/§3），且单机、偏实验，不作为 MVP 依赖。已据此起 D7 种子 → [`../03_Design/coordination_protocol.md`](../03_Design/coordination_protocol.md)。

---

## 2. 知识图谱存储 + 入图（D1 / D2 + 真值压缩）

**WikiGenius 要什么**：存事实节点 + 关系边；随时间演化；把文档/claim 结构化入图。

| 角色 | 仓库 | 为什么 |
|------|------|--------|
| **头号 / Fast pick（逻辑层）** | [Graphiti](https://github.com/getzep/graphiti) | 见第 0 节。时序图 + 失效 + 矛盾检测三合一，省掉 WikiGenius 自己造一半的真值机制。 |
| **存储后端** | [Kùzu](https://github.com/kuzudb/kuzu)（嵌入式，"图界 SQLite"，demo 零运维）<br>[FalkorDB](https://github.com/FalkorDB/FalkorDB)（Redis 系，主打 GraphRAG 低延迟）<br>[Neo4j](https://github.com/neo4j/neo4j) / [Memgraph](https://github.com/memgraph/memgraph)（服务级，**future-grade**；Graphiti 默认后端即 Neo4j） | 按运维成本选：demo 用 Kùzu，规模化用 Neo4j。 |
| 入图 / GraphRAG | [microsoft/graphrag](https://github.com/microsoft/graphrag)（社区检测式）<br>[LightRAG](https://github.com/HKUDS/LightRAG)（轻量、快）<br>[Cognee](https://github.com/topoteretes/cognee)、nano-graphrag | 把原始文档转成图。注意 WikiGenius 的入图是 **Decompose→Match→Merge**（见 [`../03_Design/ingest_pipeline.md`](../03_Design/ingest_pipeline.md)），可借这些做 Decompose/抽取那一步。 |

**推荐组合**：`Graphiti（时序图 + 矛盾逻辑）` on `Kùzu（demo）/ Neo4j（未来）`。claim 抽取复用第 3 节 RefChecker 的 triplet。

---

## 3. 语义矛盾检测（D5）

**WikiGenius 要什么**：判断新 claim 是否与已有事实**逻辑矛盾**——不是相似度，是 entailment / contradiction 级推理。

| 角色 | 仓库 | 为什么 |
|------|------|--------|
| **头号 / Future-grade** | [RefChecker](https://github.com/amazon-science/RefChecker)（amazon-science） | 把内容表示成 **claim-triplet**（subject-relation-object，与知识图谱同构），再判 **Entailment / Contradiction / Neutral**；checker 可换 LLM 或小 NLI 模型。和 WikiGenius 的 Decompose(→triplet) + 一致性校验(→entailment) **一一对应**。论文报告比旧法高 6.8~26.1 分。 |
| **Fast pick** | sentence-transformers 的 **cross-encoder NLI**（如 `nli-deberta-v3`）；AlignScore | 对一对 claim 直接判蕴含/矛盾，本地、轻、快，适合 demo 内联校验。 |
| 也看 | SummaC（摘要一致性）、各 NLI 模型（RoBERTa/DeBERTa-NLI）；**Graphiti 内置矛盾检测**（图原生方案） | |

**与 D2 的协同**：先用 Match 在图里召回邻域（候选相关/可能矛盾的节点），再只对邻域跑 triplet/NLI 校验——把"全库两两比对"降成"邻域内校验"，这就是 ingest 前半段为后半段省成本的地方。

**注意**：纯向量相似度**不够**（相似 ≠ 一致，见 [`rag_vs_kag.md`](rag_vs_kag.md)）；triplet 化能显著提精度。

---

## 4. 并发编辑 / CRDT / 版本化（Core Flow + 真值压缩）

**先划边界**：Lark Docs 自带多人实时协同 + 文档版本历史，**字符级 CRDT 大体委托载体**。WikiGenius 真正缺的是**语义级真值版本**（时间旅行到"某时刻的公认真值"）和 **section 冻结**。

| 角色 | 仓库 | 为什么 |
|------|------|--------|
| **真值时间旅行 / Future-grade** | [Dolt](https://github.com/dolthub/dolt)（"Git for data"） | SQL + 版本 + point-in-time 查询，适合真值快照与回放、双时态建模。**但**：若用 Graphiti，其双时态已在图层提供 point-in-time——**Dolt 与 Graphiti 二选一**，别叠床架屋。 |
| CRDT（若要自建协同/离线） | **Fast pick** [pycrdt](https://github.com/y-crdt/pycrdt)（Yrs/Rust 的 Python 绑定）<br>**Future** [Loro](https://github.com/loro-dev/loro)（新一代 CRDT，含版本/时间旅行） | 仅当不完全依赖 Lark 协同时才需要。 |
| section 冻结 | 应用层（CRDT 子文档 / 标记块 + Agent 拦截） | 非载体原生，见 [`../03_Design/lark_wiki_mvp.md`](../03_Design/lark_wiki_mvp.md) §三。 |

---

## 5. 综合：WikiGenius 引擎的最小栈

```
        ┌──────────────────────────────────────────────┐
        │  Agent 层：CrewAI(快) 或 LangGraph(未来)        │
        │   内部协调走框架原生 + MCP(包 lark-cli 工具)     │  ← D7 自建协商协议在此之上
        │   (A2A 仅未来跨组织/跨厂商时可选)               │
        ├──────────────────────────────────────────────┤
        │  真值/图引擎：Graphiti                          │
        │   双时态图 + 失效(=被取代) + 矛盾检测            │  ← D1/D2/D5 + 真值压缩 大半在此
        │   存储后端：Kùzu(demo) / Neo4j(未来)            │
        ├──────────────────────────────────────────────┤
        │  矛盾增强：RefChecker(triplet) / NLI cross-enc │  ← D5 提精度
        ├──────────────────────────────────────────────┤
        │  载体：Lark Wiki（文档/协同/版本/IM/权限）       │  ← 已有，不重造
        └──────────────────────────────────────────────┘
```

**一句话**：`Graphiti + 一个 agent 框架 + RefChecker 思路` ≈ WikiGenius 引擎的约 70%；剩下的护城河——**双层 Agent 协商协议 + 权限-知识耦合**——没有现成轮子，是必须自建的部分（也正是评审会看的技术硬核）。

---

## 6. 选型决策（2026-05-29 已定）

| # | 决策 | 状态 |
|---|------|------|
| 1 | **Graphiti**：先做半天 spike 验证（能否接 Lark 作 provenance 源、能否用嵌入式 Kùzu 后端、内置矛盾检测够不够）再拍板，不盲投 → 清单见 [`../04_Build/experiments/graphiti_spike.md`](../04_Build/experiments/graphiti_spike.md) | 🔬 **待 spike** |
| 2 | **真值时间旅行**：**只用 Graphiti 双时态**，不引入 Dolt（少维护一套系统） | ✅ 已定 |
| 3 | **A2A 协议**：**不进 MVP**。内部 User↔Team 协调走**框架原生** + MCP 包 lark-cli；A2A 降为**未来可选**（仅跨组织/跨厂商互操作时才需要）。理由见下 | ✅ 已定（未来可选） |
| 4 | **License**：纯比赛/内部 demo，不作选型约束 | ✅ 已定（不顾虑） |

### A2A 调研结论（第 3 项）：成熟，但 WikiGenius 内部用不到
- **成熟度没问题**：A2A v1.0（首个生产就绪）→ 现 **v1.2 稳定**（2026-03）；**Linux Foundation 托管**（Google 捐赠），150+ 组织、22k+ stars，SDK 覆盖 **Python**/JS/Java/Go/.NET；gRPC + 签名 Agent Card + 多租户。所以"不用"不是因为它不成熟。
- **关键：A2A 的本质是"互为黑盒的 agent 跨边界互操作"**（官方定义即 *opaque agentic applications*），不是"远端通信"。WikiGenius 的 User Agent / Team Agent 都是**你自己造、互为白盒的内部 agent**——它们的协调用所选框架的原生机制（共享状态 / 图的边）就够，不需要跨黑盒协议。"分布式"本身不要求 A2A，"异构 + 跨边界"才要求。
- **MCP 仍然用**：MCP 连「agent↔工具」（包 lark-cli），这层和 A2A 无关，MVP 照用；A2A 连「agent↔agent」，是被降级的那层。
- **A2A 的未来位置**：仅当 WikiGenius 跨**组织**（两家公司的知识空间协商）或要与**别家厂商**的 agent 互操作时才有意义——届时"讲一个标准"省去逐家定制。**放未来展望，不进 MVP。**

> **下一步行动**：第 1 项的 Graphiti spike 是进入 D1/D5 细节设计前的唯一前置；第 2、3、4 项已定。

---

## Sources

- Graphiti — [github.com/getzep/graphiti](https://github.com/getzep/graphiti) ；[Neo4j 介绍](https://neo4j.com/blog/developer/graphiti-knowledge-graph-memory/) ；Zep 论文 [arxiv 2501.13956](https://arxiv.org/html/2501.13956v1)
- 多 Agent 框架对比（2026） — [OpenAgents blog](https://openagents.org/blog/posts/2026-02-23-open-source-ai-agent-frameworks-compared) ；LangGraph / CrewAI / AutoGen
- RefChecker — [github.com/amazon-science/RefChecker](https://github.com/amazon-science/RefChecker) ；论文 [arxiv 2405.14486](https://arxiv.org/pdf/2405.14486)
- pycrdt — [github.com/y-crdt/pycrdt](https://github.com/y-crdt/pycrdt) ；Loro — [loro.dev](https://loro.dev/docs/concepts/crdt) ；Dolt — [dolthub time-travel](https://www.dolthub.com/blog/2023-01-18-unlocking-time-travel/)
- A2A — [github.com/a2aproject/A2A](https://github.com/a2aproject/A2A) ；[v1.0 公告](https://a2a-protocol.org/latest/announcing-1.0/) ；[LF 一周年/150+ 组织](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year) ；[A2A vs MCP](https://apigene.ai/blog/mcp-vs-a2a-when-to-use-each-protocol)

---

*Last updated: 2026-05-29*
