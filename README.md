# claude-usage-limit-fix

Claude / Claude Code 额度用得太快？这是一个可直接放进 `~/.claude/skills/` 的技能：选模型、会话卫生、预测大用量任务、主动终止空跑、防错钩子、每周零 token 复盘与自我迭代。

Claude usage running out too fast? A drop-in Claude Code skill: model routing, session hygiene, stop-loss rules, and a zero-token weekly usage review.

## 安装

```bash
mkdir -p ~/.claude/skills/claude-usage-limit-fix ~/.claude/hooks
B=https://raw.githubusercontent.com/superlady2049-source/claude-usage-limit-fix/main
curl -L $B/SKILL.md -o ~/.claude/skills/claude-usage-limit-fix/SKILL.md
# 可选：防错钩子（派 general-purpose 不写模型就拦截），配置方法见 references/hook-guide.md
curl -L $B/hooks/agent_model_gate.py -o ~/.claude/hooks/agent_model_gate.py
curl -L $B/hooks/session_start_reminder.py -o ~/.claude/hooks/session_start_reminder.py
```

## 交接模板

长会话交接用 `templates/handoff.md`（目标、已完成、已确认事实、卡在哪、下一步、不要重做的事）。

## 版本历史
- v1.0：初版（选模型、会话卫生、大用量预测、终止空跑、防错钩子、复盘）。
- v1.1：新增触发/不触发条件、4 行默认输出、证据分级、FAQ、示例。效果尚未被证明，仅有初步实测（单一环境、样本小）。
- v1.3.1：取消单个 agent 的硬停线（半路强停会交回半成品），改为「提醒线只告知、确认线先交方案」；新增「评审少走弯路」：先写 90 分评分表、自报结果用真实数据复核、规则冲突即 bug、测试脚本防误判。
- v1.3.0：测试和检查交给脚本；长命令不放进子智能体里跑；用量上限改为预估、不强停，新增修复类任务估算法。
- v1.2.0：七类浪费表重排为八类，新增「怎么发现」列和第八类「经验没用起来」，对策改为可直接照说的话。核心 SKILL.md 未改结构。

## 作者

**KAI LI** · 立凯咨询 · AI经营改善顾问 · AI Operations Improvement Consultant

邮箱：superlady2049@gmail.com

扫码添加飞书联系人：

<img src="assets/lark-qr.png" width="220" alt="KAI LI 飞书二维码">

MIT License

## English summary

A Claude Code skill to cut usage burn: model routing for subagents, session hygiene (one task per session, hand off after ~4h, `/clear` when switching), forecasting big jobs before dispatch, killing idle agents, a PreToolUse hook that blocks `general-purpose` subagents launched without an explicit `model` (and requires a stated reason for opus/fable), and a zero-token weekly review script design reading `~/.claude/projects/**/*.jsonl`. Docs are in Chinese; the hook scripts work as-is.
