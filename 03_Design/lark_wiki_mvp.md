# Lark Wiki MVP — 把 WikiGenius 骑在 Lark 上

> **目标（B3）.** Hackathon 演示要有一个**基于 Lark Wiki 的可运行 MVP**，不是只讲 PPT。本文按 [`larksuite/cli`](https://github.com/larksuite/cli) 设计 WikiGenius 的载体映射。命令均对 **lark-cli v1.0.43 实测确认**（本机已 `npx @larksuite/cli@latest install`）。
>
> 落地 [`design_readiness.md`](design_readiness.md) 的 **B3**，推进 D13（投递）、部分 D1/D10。承接 [`../02_Research/carrier_vs_competitor.md`](../02_Research/carrier_vs_competitor.md)，ingest 链路见 [`ingest_pipeline.md`](ingest_pipeline.md)。

---

## 一、为什么 lark-cli 是天作之合

lark-cli 自我定位 **"built for humans and AI Agents"**，覆盖 18 个业务域（Wiki / Docs / Drive / Base / IM / Contact / Approval / Task …），三层命令：

| 层 | 形态 | 实测例子 |
|----|------|---------|
| **Shortcuts**（`+` 前缀，人/AI 友好） | 高层意图 | `lark-cli docs +create --api-version v2`<br>`lark-cli im +messages-send --chat-id "oc_xxx" --text "Hello"` |
| **API Commands**（按域自动生成，含 `+shortcut`） | 结构化 | `lark-cli wiki +space-list` / `lark-cli wiki +node-list` |
| **Raw API**（直连端点） | 兜底 | `lark-cli api GET /open-apis/wiki/v2/spaces` |

**关键巧合**：lark-cli 用 `+shortcut` 约定，WikiGenius 的 ingest/promote/audit 也用 `+`（见 [`ingest_pipeline.md`](ingest_pipeline.md)）——后者落地时就是**对一组 lark-cli `+shortcut` 的编排**。

**认证**：`lark-cli config init`（一次性配 app 凭证）→ `lark-cli auth login`（scope 交互登录）→ 命令用 `--as user | bot` 切身份，凭证存 OS keychain。Team Agent 用 `--as bot`，User Agent 代表人时用 `--as user`。

---

## 二、载体映射：WikiGenius 概念 → Lark 原语 → lark-cli（实测命令）

| WikiGenius 概念 | Lark 原语 | lark-cli（v1.0.43） |
|-----------------|-----------|---------------------|
| 团队知识空间 | 一个 **Knowledge Space** | `wiki +space-create` / `wiki +space-list` |
| PARA 四层 | 空间下四个**顶层节点** Projects/Areas/Resources/Archives | `wiki +node-create`（建节点树） |
| 一个 Project（Overview/README/Requirements/Decisions/Issues/Resources） | Projects 下的**子节点树**，叶子 wrap 一个 Lark **Doc** | `wiki +node-create` + `docs +create --api-version v2` |
| 知识容器（文档，读写） | Lark **Doc**（markdown 友好） | `docs +create` / `docs +fetch` / `docs +update` |
| **Match 检索**（ingest 第 2 步） | **图本身是索引**；候选召回用全文搜索 | `docs +search`（跨 Docs/Wiki/表格）→ WikiGenius 图层判归属/矛盾 |
| **冲突投递通道**（决定性优势） | **IM 消息**（套件原生） | `im +messages-send --chat-id … --text …` / `im +messages-reply`（线程内协商） |
| 变更/冲突工单 | **Base 表** 或 **Task** | `base records …` / `task …` |
| 溯源 / 元数据（C4） | Doc 内 provenance 区块 或 Base 字段 | `docs +update` / `base records` |
| Match 派生缓存（**可选**，非源） | 一张 **Base 表**（图的投影，可随时重建） | `base records`（可选；真值在 WikiGenius 图层） |

> **图层是 WikiGenius 自建的那一层.** Lark Wiki 是 doc 树不是图（[`carrier_vs_competitor.md`](../02_Research/carrier_vs_competitor.md) 已标注）。节点间的引用/依赖/矛盾/取代边，以及 Match/一致性推理，都在 WikiGenius 侧。Lark 提供文档、节点树、搜索、IM、权限；**跨文档的图与真值维护是护城河**。这也是为什么不需要借来范式里的 `knowledge-map.md`——图就是索引（见 [`ingest_pipeline.md`](ingest_pipeline.md) §二）。

---

## 三、权限映射（C10 accountability）

| WikiGenius 三级 | Lark 落点 | lark-cli |
|-----------------|-----------|----------|
| **Space Admin** | 知识空间 `admin` 角色 | `wiki +member-add --member-role admin` |
| **Project Owner** | 空间 `member` + 其 Project 子树/Doc 的 Drive 所有者权限 | `wiki +member-add --member-role member` + `drive` 文档权限 |
| **Member** | 空间 `member` + Doc 可编辑/评论，经 User Agent 提交 | 同上 + `--as user` |

**实测确认**：Lark Wiki 空间角色**只有 `admin | member` 两级**（`wiki +member-add --member-role admin|member`，成员管理还有 `+member-list` / `+member-remove`）。所以：

- WikiGenius 的 **Project Owner vs Member** 之分、以及 **section 级冻结**，都在**应用层 + Drive 文档级权限**上实现——空间层只区分管理员与协作者，更细的内容级权限载体不原生提供。
- section 冻结的 MVP 近似：在冲突 section 插入冻结标记块 + Team Agent 拦截该区写入。

---

## 四、双层 Agent 怎么动起来（一次 ingest 的真实链路）

```
用户在 IM 里 @User Agent 提交一段内容 / 上传文件
        │
        ▼  User Agent（--as user，Assistive AI）
  1. Decompose：LLM 拆成原子 claim（顺手丢弃一次性细节）
  2. Match：docs +search 召回候选 + 查图定位归属/矛盾邻域
        │   lark-cli docs +search / wiki +node-list / wiki +node-get
  3. Merge：提议并入匹配节点（无匹配才 wiki +node-create 新建）
        │   → 产出"待评估变更集"（带 C4 溯源标记）
        ▼  Team Agent（--as bot，Coach + Diagnostic AI）
  4. 三维校验：一致性 / 权限 / 影响范围（Match 已交出邻域 → 一致性几乎免费）
        │
        ├─ 无冲突 → docs +update 写入 + 图谱更新 + 压缩 housekeeping + IM 回执
        │
        └─ 检测到矛盾（撞上已归档 decision）
                │   im +messages-send 推给双方/Owner（线程里 im +messages-reply 协商）
                ▼
           协商 → 同意则 docs +update；不同意则 base records 建工单沿权限链升级
                ▼
           解决后 section 解冻，队列里的写入重新评估
```

"**Agent 不请自来地推送冲突**"这一步是选 Lark 的**决定性理由**——`im +messages-send` 是套件原生通道，人不在产品里也收得到（Notion/Confluence 的站内通知做不到）。注意第 2 步 Match 与第 4 步一致性校验是**同一条流水线的两端**（详见 [`ingest_pipeline.md`](ingest_pipeline.md)）。

---

## 五、Hackathon MVP 的最小可演示形态

**后端（真跑）：**
1. 一个 Lark 租户 + 一个自建应用（app id/secret），`lark-cli config init` + `auth login` 配好；开通 Wiki/Docs/IM/Drive/Base 的权限 scope。
2. 预置一个知识空间，`wiki +node-create` 建好 PARA 节点树，种入几篇 Doc，其中**埋 1–2 个矛盾**（如 Archives 里一条"rate limit ≤ 500 否则违反 SLA"的归档决策）。
3. WikiGenius Agent 编排进程（双层 Agent）通过 lark-cli 驱动上面的链路。

**前端 / 演示面（B2：HTML，不是 PPT）：**
- 用 [`zarazhangrui/beautiful-html-templates`](https://github.com/zarazhangrui/beautiful-html-templates)（34 套模板，浏览器直开、无 build；按其 `AGENTS.md` 选型）做 demo 仪表盘 + pitch deck。
- 仪表盘体现信任面（C6/C7）：
  - **"Team Agent 在做什么"** 实时视图（C6 可见性）
  - **冲突时间线** + 每个裁决 **"为什么这么判"** 展开（C7 透明）
  - **PARA 各层节点数 + 膨胀趋势**（ingest 的 `status` 操作，呼应 D14 指标）
  - 知识图谱可视化（WikiGenius 自建的边）
- 数据来源：HTML 面板读 lark-cli / Lark API 实时数据，或读 Agent 进程导出的状态。

**演示脚本（B1 待定具体台词）**：提交一个看似无害的变更 → User Agent 拆解归并 → 撞上埋好的矛盾 → IM 弹冲突 → 一键看"为什么" → 协商/升级 → 解决。一条龙证明那个楔子。

---

## 六、诚实的待确认项与风险

- **section 级冻结**与 **Project Owner/Member 细分**是应用层 + Drive 权限实现，非 Lark 空间原生（空间只有 admin|member）。
- **图层自建**：跨文档一致性图是护城河，也是工作量大头，载体不提供。
- **`docs` API 版本**：用 `--api-version v2`（v1 已废弃；安装时已装 lark-doc v2 skill）。
- **租户与 app 审批**：自建应用要开通多域 scope，demo 前预留申请时间。
- **Base 派生缓存**是否需要，取决于图层实现（见 [`ingest_pipeline.md`](ingest_pipeline.md) §二），非必需。

---

*Last updated: 2026-05-29*
