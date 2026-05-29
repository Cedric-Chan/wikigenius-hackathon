# Graphiti Spike — 半天验证清单

> **目的.** 在投入 D1/D5 细节设计前，用约半天验证 [Graphiti](https://github.com/getzep/graphiti) 能不能当 WikiGenius 的真值/图引擎。产出一个 **go / no-go + 后备路线**，而不是一个原型。
>
> 对应决策见 [`../../02_Research/tech_references.md`](../../02_Research/tech_references.md) §6 第 1 项（Graphiti 待 spike）。
>
> ⚠️ **API 版本提醒.** 下方代码按 `graphiti-core` ~0.3.x 量级写，到 2026 可能已变。**第一步先 `pip show graphiti-core` 核对版本，再对照当前官方 README 调整 API**。命令是"照着改"的脚手架，不保证逐行可跑。

---

## 0. 成功判据（一句话 go/no-go）

| 结果 | 决策 |
|------|------|
| T1–T4 全绿 | ✅ 定 Graphiti 为核心引擎，进 D1/D5 细节设计 |
| 仅 T2（嵌入式后端）挂 | ⚠️ 退 **Neo4j** 后端（仍用 Graphiti），demo 多一个服务 |
| 仅 T3（矛盾检测）弱 | ⚠️ Graphiti 存图 + 时间，**RefChecker 做矛盾主判**（已在 tech_references 预案） |
| T1（provenance）或 T4（时间旅行）做不到 | 🔴 红灯，重新评估引擎选型 |

**时间盒：每个任务到点即止，不纠缠。** 目标是判断，不是打磨。

---

## 1. 前置（~30 min）

```bash
# 独立环境
python -m venv .venv && source .venv/bin/activate
pip install graphiti-core
pip show graphiti-core          # ← 记下版本，对照官方 README 校准下面的 API

# 后端二选一（T2 验证嵌入式；先备好 Neo4j 兜底）
# 兜底 Neo4j（docker）：
docker run -d --name neo4j-spike -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/spikepass neo4j:5
```

**LLM / embedder（模型无关）.** Graphiti 的抽取/矛盾判定需要一个 LLM + embedder，client 可配（OpenAI / Anthropic / Gemini / 本地 等）。按手上可用的配：

```python
# 例：用 Anthropic（或换成你们可用的 provider）。具体 client 名以当前版本为准。
from graphiti_core import Graphiti
# from graphiti_core.llm_client import AnthropicClient  # 名称按版本核对
# graphiti = Graphiti(llm_client=AnthropicClient(...), embedder=...)
```

> 这一步顺带覆盖原 T5（模型无关）：能用非 OpenAI provider 起来就算过。

---

## 2. 测试数据（~15 min）—— 复用 rate-limit 矛盾剧本

三条 episode，带 provenance（来源 Lark 节点 id + 人/agent），时间上制造一次"被取代"：

| # | 时间 | 内容 | 来源（provenance） |
|---|------|------|--------------------|
| E1 | 2025-09-01 | "API rate limit 上限为 500；超过会违反 SLA 承诺。" | Lark 节点 `wiki_node_archive_decision_001`；human:alice |
| E2 | 2025-09-02 | "Gateway runbook 按 rate limit = 500 配置告警阈值。" | Lark 节点 `wiki_node_runbook_gw`；human:bob |
| E3 | 2026-05-29 | "把 API rate limit 提到 1000。" | Lark 节点 `wiki_node_pr_4821`；agent-assisted:carol |

E3 应当与 E1 矛盾 → 这是 T3/T4 的考点。

---

## 3. 任务 T1–T4

### T1 — Provenance 能否进图并查回？（~45 min）
**问题**：能否把「Lark 节点 id + 人/agent 来源」随事实写入，并在查询结果里取回？（gate C4 溯源）

```python
import asyncio
from datetime import datetime
# add_episode 签名按当前版本核对：name / episode_body / source / source_description / reference_time / group_id
await graphiti.add_episode(
    name="E1",
    episode_body="API rate limit 上限为 500；超过会违反 SLA 承诺。",
    source_description="lark:wiki_node_archive_decision_001|by:human:alice",
    reference_time=datetime(2025, 9, 1),
    group_id="team_demo",          # 用 group_id 做空间/租户隔离
)
# …E2、E3 同理
results = await graphiti.search("API rate limit 上限")
for r in results:
    print(r.fact, getattr(r, "valid_at", None), getattr(r, "invalid_at", None))
    # 检查能否从 episode/source_description 取回 lark 节点 id 与 human/agent
```

**通过标准**：检索某条事实时，能拿到它来自哪个 Lark 节点、是 human 还是 agent。
**若不行**：看能否用**自定义实体属性（Pydantic 本体）**承载 provenance；仍不行 → provenance 走 WikiGenius 应用层旁挂（红灯转黄灯）。

---

### T2 — 能否用嵌入式 Kùzu 后端？（~45 min）
**问题**：Graphiti 能否跑在嵌入式 **Kùzu**（零运维），还是必须 Neo4j？

```bash
pip install kuzu     # 以及 graphiti 对应的 driver 包（按版本核对是否支持 Kùzu/FalkorDB）
```
```python
# 按当前版本看 Graphiti 是否暴露 graph driver 参数（Neo4jDriver / KuzuDriver / FalkorDriver）
# graphiti = Graphiti(graph_driver=KuzuDriver(db_path="./spike.kuzu"), llm_client=..., embedder=...)
```

**通过标准**：用 Kùzu 跑通 §2 三条 episode 的写入 + 一次 search。
**若不行（时间到）**：直接用前置里的 Neo4j 兜底，记一条"demo 需带 Neo4j 服务"，继续 T3。**不在这纠缠**。

---

### T3 — 自动被取代 / 矛盾检测质量如何？（~60 min）
**问题**：写入 E3（rate limit=1000）后，旧的 E1（=500）事实是否被**自动 invalidate**（而非删除/并存矛盾）？质量够不够，还是要 RefChecker 兜底？

```python
await graphiti.add_episode(name="E3",
    episode_body="把 API rate limit 提到 1000。",
    source_description="lark:wiki_node_pr_4821|by:agent:carol",
    reference_time=datetime(2026,5,29), group_id="team_demo")

res = await graphiti.search("API rate limit 当前值")
# 期望：500 那条 edge 现在带 invalid_at（约 2026-05-29），1000 那条为当前有效
for r in res:
    print(r.fact, getattr(r,"valid_at",None), getattr(r,"invalid_at",None))
```

**通过标准（分级）**：
- 🟢 强：500 被自动标记 invalid_at、1000 成为当前真值，且**不误伤** E2 runbook 那条仍有效的引用。
- 🟡 中：能检出矛盾但边界不准（漏标或误标）→ 记"主判用 RefChecker，Graphiti 做候选召回"。
- 🔴 弱：完全没识别 → 矛盾检测整体交给 RefChecker（Graphiti 仅存图+时间）。

> 这是最关键、也最该多给时间的一项——它直接决定 D5 的架构（Graphiti 自带 vs RefChecker 主判）。

---

### T4 — 真值时间旅行（~45 min）
**问题**：能否查"**某时刻**团队对 rate limit 的公认真值"？（gate 决策②：真值只用 Graphiti 双时态）

```python
# 期望：以 2025-10-01 视角查 → 500；以 now 视角查 → 1000
# 看当前版本 search 是否支持按时间点过滤（valid_at <= T < invalid_at），
# 或用 search 结果里的 valid_at/invalid_at 自行过滤重建。
```

**通过标准**：能稳定重建"2025-Q4 时 rate limit 的公认真值 = 500"且"现在 = 1000"。
**若只能拿到带时间戳的边、需自己过滤**：也算过（应用层薄封装即可），记一条"point-in-time 需自建查询封装"。
**若完全没有时态可查**：红灯（直接动摇决策②）。

---

## 4. 决策矩阵（填完即出结论）

| 任务 | 结果(🟢/🟡/🔴) | 观察到的关键事实 | 引出的决策 |
|------|----------------|------------------|------------|
| T1 provenance | | | |
| T2 Kùzu 后端 | | | Kùzu / 退 Neo4j |
| T3 矛盾检测 | | | Graphiti 自判 / +RefChecker 主判 |
| T4 时间旅行 | | | 满足决策② / 需封装 / 红灯 |
| LLM 模型无关 | | | provider = ? |

---

## 5. 产出（spike 结束后必做）

1. 把上面矩阵填好，连同关键命令输出，回填到本文件「结果」区。
2. 更新 [`../../02_Research/tech_references.md`](../../02_Research/tech_references.md) §6 第 1 项：把 🔬 待 spike → ✅/⚠️/🔴 + 一句结论。
3. 若结论影响 D1/D5，在 [`../../03_Design/design_readiness.md`](../../03_Design/design_readiness.md) 标注。

---

## 6. 已知坑 / 注意

- **API 漂移**：先核对 `graphiti-core` 版本，`add_episode` / 驱动参数 / search 时态过滤的签名按当前 README 校准。
- **LLM 抽取不确定**：同样输入两次结果可能不同；T3 多跑两遍看稳定性（呼应学术约束 C8 可靠性）。
- **group_id 做隔离**：用它当 WikiGenius 的 space/租户边界，避免 demo 数据互相污染。
- **embedder 成本**：spike 数据量小，忽略；但记一笔生产期的调用成本（关联 D11 成本模型）。
- **时间盒纪律**：任何一项卡到点 → 记 🟡/🔴 走人，别把半天 spike 拖成两天。

---

*Last updated: 2026-05-29*
