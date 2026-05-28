# Why Not Mega Agent + CLI

## 背景：什么是 Mega Agent + CLI 模式

CLI（命令行界面）本质是 API 上面的一层**人类适配器**——把 HTTP API 的 JSON 返回格式化成终端里的文本、表格和颜色，把参数抽象成 flag，让人类可以直接敲命令调用。以 [Lark CLI](https://github.com/larksuite/cli) 为例：

```bash
lark message send --receive-id ou_xxx --msg-type text --content "hello"
lark doc create --title "PRD" --folder-token "xxx"
```

它把飞书开放平台的 API 封装成命令，但**没有做任何超出"封装"的事情**——不自主规划、不维护状态、不替用户做决策。

Mega Agent + CLI 模式，就是把这个思路搬到 WikiGenius：用户通过终端命令直接和中央的 Team Agent 交互，没有 User Agent 这一层。

---

## CLI 本质：是交互式接口，不是 Subagent

| 维度 | CLI | Subagent (User Agent) |
|------|-----|----------------------|
| **自主性** | 零。用户敲什么命令，它就执行什么，多一步都不走 | 有。可以主动规划多步操作，根据上下文调整策略 |
| **状态** | 无状态。每次调用是独立事务，不记得上次聊了什么 | 有状态。维护对话历史和用户上下文 |
| **决策权** | 没有。连 `--msg-type` 都必须用户显式指定 | 有。可以推断意图、补全信息、甚至质疑用户的输入 |
| **协作能力** | 不能。不会去和另一个 CLI 实例协商任何事情 | 可以。能代表用户去和其他 Agent 谈判 |
| **类比** | 增强版 curl + jq | 数字员工 |

CLI 没有 API 做不到的事情——它只是让 API 对人类更友好。但一个 Subagent 能做的事情（自主决策、后台运行、代表用户协商），CLI 一件也做不了。

---

## 为什么 WikiGenius 不能走 Mega Agent + CLI

### 1. 异步协商不可能

Proposal 里定义的冲突解决流程：

```
User A ──change──▶ User Agent A ──submit──▶ Team Agent
                                              │
                                         检测到冲突
                                              │
                        User Agent A ◀──通知──┴──通知──▶ User Agent B
                             │                              │
                         后台协商                         后台协商
                             │                              │
                        ┌─同意─┐                      ┌─同意─┐
                        │      │                      │      │
                    Team Agent 更新文档           Team Agent 更新文档
```

这个流程的核心假设是：**两个 User Agent 可以在后台自主协商，用户不需要在线等待**。用户早上提交完变更就去开会了，她的 User Agent 继续代表她工作。

CLI 是同步调用-等待模型：

```bash
$ wiki submit-change --doc "PRD" --section "API Strategy" --content "..."
# 终端阻塞，等待响应
# 如果 Team Agent 检测到冲突需要和其他人协商：
# → 用户只能在线等，或者 Ctrl+C 放弃
```

一旦需要"人在回路之外"的处理，CLI 就断了——它没有"代表我在后台跑"的能力。

### 2. 丢失个人上下文和角色感知

User Agent 的核心价值之一是**持久化地理解用户**：

- 你是谁？Space Admin / Project Owner / Member？
- 你最近在改哪个 Project 的哪些文档？
- 你的历史查询和变更偏好是什么？
- 你和哪些人的变更最常发生冲突？

CLI 天然是 stateless 的。每次 `wiki query` 都是一张白纸——你需要重新声明身份、上下文、意图。权限校验退化成每次传 token，变更评估丢失了"提交者的工作习惯和历史"这一维度的信息。

### 3. 负载分流崩溃，单点瓶颈

双层架构的负载分流逻辑：

```
              ┌─────────────┐
              │  Team Agent │  ← 只处理：全局冲突仲裁、跨 Project 变更、权限边界决策
              └──────┬──────┘
        ┌────────────┼────────────┐
        │            │            │
  ┌─────┴─────┐ ┌───┴─────┐ ┌───┴─────┐
  │User Agent │ │User Agent│ │User Agent│  ← 处理：本地查询、意图澄清、上下文补全
  │   Alice   │ │  Bob     │ │  Carol   │
  └───────────┘ └──────────┘ └──────────┘
```

User Agent 承担了大量**不需要上升**的工作——"这个文档我上次看到哪了？""帮我搜一下我们 PRD 里关于 API 版本的描述。"这些查询如果全部打到 Team Agent，它就是单点瓶颈。

Mega Agent + CLI 模式把所有请求直接打到一个点上：

```
$ wiki query "API version strategy?"
$ wiki submit-change --doc "PRD" ...
$ wiki search "onboarding guide"
# 50 个用户的所有查询、变更、搜索 → 全部集中到 Team Agent
```

这不是架构优化问题，这是数学问题——N 个用户的全部交互 vs 只有需要全局协调的部分才升级。

---

## CLI 的正确角色

CLI 不是没有用，只是不应该替代 User Agent。正确的定位是：

### 作为 User Agent 的一个交互界面

```bash
# CLI 是 User Agent 的前端，不是 Team Agent 的前端
$ wiki-agent ask "我们的 API 版本策略是什么？"
$ wiki-agent submit-change --doc "PRD" --section "API Strategy" --content "..."
$ wiki-agent status  # 查看你提交的变更当前状态
```

和 Chat UI、IDE 插件、Web 面板并列——都是同一个 User Agent 的接入方式。

### Mega Agent 的运维接口

```bash
# Space Admin 直接操作 Team Agent 的管理面
$ wiki-admin list-projects
$ wiki-admin resolve-conflict --id 42 --decision "accept A's version"
$ wiki-admin update-permissions --user bob --role "Project Owner" --project "Backend"
```

这是运维层面，不是日常协作路径。

---

## 总结

> Mega Agent + CLI 把 WikiGenius 降级成"带 AI 回答功能的命令行 wiki"——抹掉了双层架构的三个核心差异：
>
> 1. **异步协商** → 退化成人必须在终端前等着
> 2. **个人上下文** → 退化成每次重新声明身份的 stateless 调用
> 3. **负载分流** → 退化成一个 Agent 单点扛所有请求
>
> CLI 应该做 User Agent 的**可选手柄**，不是替代它。