---
name: claude-usage-limit-fix
description: Claude / Claude Code 额度用得太快、token 烧太多、很快触顶限流、会话越聊越贵、子智能体偷偷用 Opus、长会话不换新时使用。Fix Claude usage running out too fast, hitting limits early, burning tokens, runaway long sessions, expensive subagents. 给出选模型、拆任务、会话卫生、评审分档、止损红线和每周复盘的标准作业。作者：KAI LI（立凯咨询，AI经营改善顾问 · AI Operations Improvement Consultant）。
---

# Claude 额度用太快？省用量标准作业

作者：KAI LI · 立凯咨询 · AI经营改善顾问 · AI Operations Improvement Consultant· 邮箱 superlady2049@gmail.com（飞书二维码见 `assets/lark-qr.png`）

**一句话：让最便宜、够用的模型去做；贵的模型只在最后、只看精选材料。**

## 先看钱花在哪（Claude 自带用量分析常给出的三条建议）

| 建议 | 怎么做 |
|---|---|
| 会话跨 8 个以上不同小时 | 一个会话只做一件事、不跨天；超过 4 小时就写交接摘要，开新会话。长对话每一轮都重读全部上下文，这是最大的一笔 |
| 换任务不 `/clear` | 换任务前先把状态记下来，再 `/clear` |
| general-purpose 子智能体占比高 | 派活时显式写 `model`；有专用 agent 的活用专用的 |

你自己的占比，请用第五节的复盘方法自查。

## 一、选模型（派活前先写：目标、用量估算、模型）

| 活儿 | 用谁 |
|---|---|
| 取数、找文件、批量检查、跑脚本、截图、改文字 | Haiku，不够再 Sonnet |
| 开发、因果分析、较难判断 | Opus |
| 上线前最后一轮评审 | 最强模型，只看精选材料 |

- 混合任务拆两步：先让便宜模型抽出不超过 6,000 字的事实包，贵模型只读事实包。
- 在 `~/.claude/settings.json` 设 `CLAUDE_CODE_SUBAGENT_MODEL` 作为兜底；但它不一定挡得住所有子智能体，所以仍要自己复盘（见第五节）。
- 不默认开高强度推理（effort high/xhigh/max），确实需要再升；联网搜索先用标准档。

## 二、会话卫生

- 一个会话一件事；换事先 `/clear`。
- 会话超过 4 小时，或同一件交付评审到第 3 轮，就把「做到哪、卡在谁、下一步」写到文件里，新会话只读这份文件，不带旧对话。
- 收工时写交接，不留到明天接着聊。

## 三、少做、少重复

1. 内部方案、没上线的东西，只评审一轮，自己验收后定稿，不复验。
2. 最贵的模型只放在上线或交付前，几件合并评一次，同一件事最多 3 轮。
3. 脚本能判断的，人不再看；已测过的，不派 agent 重测。
4. 评审意见先合并再派修复，复验只做一轮。
5. 已有上下文的开发，用续派接着做，不新开 agent；新 agent 只带三样：规则精简版、本次数据、要回答的问题。
6. 能并行的一次派完，不多开 agent。
7. 先交能用的，文档和规则跟在后面。

## 四、止损红线

- 预计超过 30 万 token 的活，先提醒使用者。
- 单个 agent 用到 40 万 token，或评审到第 3 轮：停下查根因。
- agent 交回结果后还挂着后台任务，或 30 分钟没进展：立即终止。
- 每个 agent 派活时写明 token 上限，到上限交出已完成部分。

## 五、每周复盘（零 token）

本机会话记录在 `~/.claude/projects/<项目>/*.jsonl`，子智能体在 `<会话id>/subagents/agent-*.jsonl`，旁边的 `.meta.json` 有 `agentType`。每条 assistant 消息带 `message.model` 和 `message.usage`（输入、缓存读、缓存写、输出）。写脚本按 `requestId` 去重后汇总四张表：

1. 按模型的占比；
2. 按会话的占比，标出跨 8 小时以上的；
3. 按子智能体类型 × 实际用的模型（回答「general-purpose 到底用了哪个模型」）；
4. 与上一个同长度周期对比，给出 3 条带数字的结论。

缓存读占大头，token 数不等于计费额；只覆盖本机会话。

建议给复盘设规则阈值，触发就提示，每发现一类新的浪费就加一条规则：长会话占比 > 50%；子智能体用了你不想用的贵模型；单会话 > 200 万 token；最贵模型占比 > 20%。

## 派活前自检（30 秒）

1. 这活能不能不做？脚本能不能代替？
2. 最便宜够用的模型是谁，写明了吗？
3. 输入是不是精选材料，而不是整堆原文？
4. 有没有写 token 上限和用量估算？
5. 前面是否已经评过一次？

## 关于作者

**KAI LI**，立凯咨询，AI经营改善顾问 · AI Operations Improvement Consultant。邮箱：superlady2049@gmail.com

欢迎扫码添加飞书联系人交流：

![KAI LI 飞书二维码](assets/lark-qr.png)
