# Git vs WikiGenius — 异同分析

## 相同点

| 维度 | 共同特征 |
|------|---------|
| **版本追踪** | 两者都记录"谁改了什么"——Git 通过 commit 链追溯变更，WikiGenius 通过 Team Agent 持续评估变更历史 |
| **冲突检测** | Git 检测文本级合并冲突（同一行被两人改了），WikiGenius 检测语义级冲突（新内容是否与已有知识矛盾） |
| **异步协作** | Git 分布式仓库支持离线提交后推送，WikiGenius 的 User Agent 本地处理查询、异步提交变更给 Team Agent |
| **权限控制** | Git 有 repo owner / collaborator / read-only，WikiGenius 有 Space Admin / Project Owner / Member 三级权限 |
| **本地优先** | Git 允许 commit 在本地，WikiGenius 允许 User Agent 在本地处理查询 |
| **冻结机制** | Git 冲突时整个文件无法合并，WikiGenius 冲突时仅冻结受影响的知识 section，其余部分正常读写 |

---

## 关键差异

### 1. 追踪的粒度：文本行 vs 语义知识

- **Git** 追踪的是**代码/文本行**的增删改，完全不理解内容含义
- **WikiGenius** 追踪的是**知识的语义一致性**——它需要理解"这段描述是否与项目需求文档矛盾"

### 2. 冲突解决的智能程度

- **Git** 是"哑"工具：只要不是同一行被同时改动，它就认为没问题——哪怕两段逻辑上完全矛盾的代码同时合入
- **WikiGenius** 通过 **AI Agent** 做三维度评估：一致性（语义/逻辑冲突检查）、权限（提交者角色是否有写入权限）、影响范围（局部更新 vs 结构性变更）

### 3. 冲突恢复的工作流

- **Git**：`merge conflict` → 人工手动解决 → `git add` → `git commit`
- **WikiGenius**：Team Agent 检测冲突 → 通知双方协商 → 达成一致则自动更新 → 不同意则生成工单沿权限链升级（Project Owner → Space Admin）

### 4. 数据结构

- **Git**：有向无环图（DAG）的 commit 历史 + 文件树
- **WikiGenius**：三层知识图谱（Projects / Areas / Resources & Archives），具有角色关联、生命周期状态、跨文档交叉引用关系

### 5. 中心化 vs 去中心化

- **Git** 是**分布式**的：每个人有完整副本，`push`/`pull` 同步
- **WikiGenius** 是**中心化**的：Team Agent 是唯一真实来源（source of truth），User Agent 只是"代理"，不持有完整知识图谱

### 6. 同意的门槛

- **Git**：你能 push 就能改，合并策略是机械的（fast-forward / three-way merge）
- **WikiGenius**：每一条变更都要通过 **一致性 + 权限 + 影响范围** 三重校验，结构性变更的门槛高于局部更新

### 7. 变更感知的维度

- **Git** 只知道文本变了
- **WikiGenius** 需要知道：
  - 这个变更影响的是单个 Project 还是跨 Area？
  - 改的是事实陈述还是决策逻辑？
  - 和三个已归档文档有没有矛盾？

---

## 一句话总结

> Git 管理的是**代码的版本**——谁在什么时候改了什么行；  
> WikiGenius 想管理的是**知识的真值**——团队现在公认什么是真的、什么已经过时、谁说的一定是权威。Git 赢了版本控制，但它在"知识一致性"这件事上几乎完全无能为力——那正是 WikiGenius 要解决的问题。

---

## 对 WikiGenius 产品设计的启示

1. **不要重新发明 Git**：版本历史追踪应该用 Git 或类似机制，WikiGenius 的差异化价值在语义层而非文本层
2. **冻结粒度是核心竞争力**：Git 是整个文件冲突，WikiGenius 的 section 级冻结是更好的用户体验，但需要精确的 section 边界定义
3. **Git 的工作流已经深入人心**：PR → review → merge 的模式可以作为 WikiGenius 冲突解决工作流的设计参考
4. **权限模型可以借鉴但不照搬**：Git 的 CODEOWNERS 机制和 WikiGenius 的 Project Owner 概念有相似之处，但 WikiGenius 需要更细粒度的内容级权限