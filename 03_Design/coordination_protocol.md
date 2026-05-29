# 变更与冲突协调协议（D7 种子）

> **这是什么.** WikiGenius 的核心难题（Proposal「The Hard Problem」）= 多 Agent 协调协议：Team Agent 如何同时应对多个 User Agent 的请求、并在请求矛盾时协调。本文是 **D7 的设计种子**，不是完整协议——把变更/冲突生命周期落成一个 **Kanban 式状态机**。
>
> **借鉴来源.** 协调骨架借鉴 [Hermes Kanban](https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban)（Nous Research）的**协调模型**——借模型，不借依赖（它单机、偏实验）。评估见 [`../02_Research/tech_references.md`](../02_Research/tech_references.md) §1。
>
> **边界（关键）.** Kanban 管**流程**（谁的变更、走到哪一步、会不会撞车）；它**不**管**内容矛盾**——语义矛盾由一致性内核（Graphiti / RefChecker，见 tech_references §2/§3）判定。本协议是流程骨架，一致性引擎是它在 `evaluating` 态调用的"裁判"。

---

## 1. 核心模型：变更是一行，不是一次调用

借 Hermes 的核心论点：*delegate_task 是函数调用；Kanban 是工作队列，每次交接都是一行，任何相关方都能看和改*。

WikiGenius 的**每条变更提交 = 协调板上的一行（durable change-row）**，而不是一次同步 RPC。这正好落地 Proposal 的异步设计：成员提交完就离线，变更作为一行留在板上，Team Agent 后台推进，解决后再通知。**这张板在 Lark 上就是一张 Base 表**（见 [`lark_wiki_mvp.md`](lark_wiki_mvp.md) 的"变更/冲突工单"行）。

---

## 2. 状态机（板上的列）

```
 submitted ──▶ evaluating ──┬─(校验通过)────────▶ writing ──▶ done
   │            │           ├─(权限不足)────────▶ rejected
   │            │           └─(语义矛盾)──▶ conflict(section 冻结)
   │            │                              │
   │            │                              ▼
   │            │                          negotiating ──┬─(达成一致)─▶ resolved
   │            │                              │         └─(超时/分歧)─▶ escalated
   │            │                              ▼                          │
   │            │                          (相关方在 comment/IM 线程协商)   ▼
   │            ▼                                              Owner→Admin 裁决
   └──── 同一节点已被认领 → 作为依赖排队（见 §4）                          │
                                                  resolved ◀──────────────┘
                                                      │
                                          重新评估队列 → writing → done
```

| 列 | 含义 | 谁推进 |
|----|------|--------|
| `submitted` | User Agent 提交的变更集（来自 ingest 的 Merge），待处理 | User Agent |
| `evaluating` | Team Agent 三维校验中（一致性/权限/影响）；**已原子认领受影响节点** | Team Agent |
| `writing` | 校验通过，落库中（写图谱 + Lark Doc） | Team Agent |
| `done` | 已写入；`+sync` 刷新；IM 回执 | Team Agent |
| `conflict` | 一致性内核报矛盾 → 受影响 **section 冻结** | Team Agent |
| `negotiating` | 相关方在 comment/IM 线程协商 | User Agents |
| `escalated` | 协商超时/分歧 → 沿权限链升级 | Team Agent → Owner/Admin |
| `rejected` | 权限不足 / 裁决不采纳 | — |
| `archived` | 归档（含被取代的历史变更） | Team Agent |

> 规则**显式且版本化**（呼应 C8 可靠性）：两个结构相似的冲突必须走出结构相似的状态轨迹。

---

## 3. 并发：原子认领 = "section 冻结"的并发原语

Team Agent 同时收到多个 User Agent 请求时，借 Hermes 的**原子认领**（Hermes 用 SQLite `BEGIN IMMEDIATE`；WikiGenius 用承载板的存储的等价原子事务）：

- 变更进入 `evaluating` 时，Team Agent **原子认领它要动的节点/section**。
- 认领成功 → 独占评估该处；其他想动**同一节点**的变更**认领失败 → 转为依赖排队**（§4）。
- 这给了 Proposal 里"section 冻结"一个**具体的并发实现**：冻结 = 对该节点的认领锁；文档其余部分无锁、照常读写。

> Lark 原生只到文档级权限，section 级冻结本就是应用层（见 `lark_wiki_mvp.md` §三）——原子认领就是这个应用层锁的机制。

---

## 4. 依赖与解冻：排队写入 = 冲突 ticket 的子项

借 Hermes 的 **parent→child（父完成才放行子）**，逐字命中 Proposal 的"解决后队列里的写入重新评估、section 解冻"：

- 当一个 section 因冲突冻结，后续想改它的变更**挂为该冲突 ticket 的子项**，停在 `submitted`（被 parent 阻塞）。
- 冲突 ticket → `resolved` 后，子项**自动 promote 回 `evaluating`** 重新评估（因为真值可能已变），section 解冻。
- 跨 Project 的冲突 = 多个 parent；全部 `resolved` 才放行子（借 Hermes "all parents done"）。

---

## 5. 协商线程：change-row 的 comments → Lark IM

借 Hermes 的 **comments = inter-agent 协议线程**：

- `negotiating` 期间，User↔Team↔相关 User 的往来记录在 change-row 的**评论线程**上——可追溯、可解释（C7 透明）。
- 在 Lark 上，这条线程直接落到 **IM 线程**：`im +messages-send` 起头、`im +messages-reply` 往来。"Agent 不请自来推冲突"的投递就是这一步。

---

## 6. 超时与升级：heartbeat / TTL / 熔断

借 Hermes 的 **TTL + 僵死回收 + 熔断（连续失败 N 次自动 block）**，落地 Proposal 的"协商失败沿权限链升级"：

- 每个 `negotiating` ticket 带 **TTL**；超时未达成 → 自动 `escalated`，升级给 Project Owner（再无果 → Space Admin）。
- **熔断**：同一冲突反复协商失败到阈值 → 自动升级，不无限重试。
- 升级**路由给具体的人**（C2 人保留决策、C10 问责到具体角色），不是 Agent 自裁。

---

## 7. Lark 落地：板 = 一张 Base 表

change-row 的建议字段（D1 待最终定）：

| 字段 | 含义 |
|------|------|
| `change_id` | 变更唯一 id |
| `node_id` | 受影响的知识节点/section（认领锁的对象） |
| `status` | §2 状态列 |
| `submitter` | 提交人（C4 溯源、C10 问责） |
| `assignee` | 当前负责推进的角色（Team Agent / Owner / Admin） |
| `parent_id` | 依赖的冲突 ticket（§4） |
| `claim_ttl` | 认领/协商超时（§6） |
| `priority` | 优先级（Team Agent 限流，呼应负载分流） |
| `thread_ref` | 关联的 Lark IM 协商线程（§5） |
| `created_at` / `updated_at` | 时间 |

---

## 8. 与一致性内核的接口

状态机在 `evaluating` 态**调用**一致性内核，不自己判内容：

```
evaluating ──▶ 一致性内核（Graphiti 邻域召回 + RefChecker/NLI 矛盾判定）
                   ├─ 无矛盾 + 有权限 ──▶ writing
                   └─ 有矛盾 ──▶ conflict（内核给出矛盾的边界 = 要冻结的 section）
```

Kanban 是骨架，Graphiti/RefChecker 是裁判——两层互补（见 tech_references §0 边界）。

---

## 9. 与学术约束对齐

| 约束 | 本协议如何满足 |
|------|----------------|
| **C2** 人保留决策 | `escalated` 路由给人；Agent 不自裁结构性冲突 |
| **C8** 可靠性 | 状态机显式、规则版本化；相似冲突走相似轨迹 |
| **C10** 问责 | `submitter`/`assignee` 指向具体人/角色，非"系统" |
| **C6/C7** 可见/透明 | 板本身可见（Team Agent 在做什么）；comment 线程 = "为什么这么判"可查 |

---

## 10. 仍待定（D7 未尽）

- **认领粒度**：锁到 node 还是更细的 section？粒度太粗误伤并发，太细难界定边界。
- **多方并行协商**：跨 Project 冲突涉及多个 Owner 时，协商是串行升级还是并行征询？
- **优先级策略**：什么变更插队（如安全/合规）？
- **超时阈值**：TTL 具体多久；与 C1（不打扰过度）平衡。
- **认领锁的存储**：Lark Base 是否够做原子事务，还是要旁挂一个状态存储。

---

*Last updated: 2026-05-29*
