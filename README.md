# claude-usage-limit-fix

Claude / Claude Code 额度用得太快？这是一个可直接放进 `~/.claude/skills/` 的技能：选模型、会话卫生、预测大用量任务、主动终止空跑、防错钩子、每周零 token 复盘与自我迭代。

Claude usage running out too fast? A drop-in Claude Code skill: model routing, session hygiene, stop-loss rules, and a zero-token weekly usage review.

## 安装

```bash
mkdir -p ~/.claude/skills/claude-usage-limit-fix ~/.claude/hooks
B=https://raw.githubusercontent.com/superlady2049-source/claude-usage-limit-fix/main
curl -L $B/SKILL.md -o ~/.claude/skills/claude-usage-limit-fix/SKILL.md
# 可选：防错钩子（派 general-purpose 不写模型就拦截），配置方法见 SKILL.md 第六节
curl -L $B/hooks/agent_model_gate.py -o ~/.claude/hooks/agent_model_gate.py
curl -L $B/hooks/session_start_reminder.py -o ~/.claude/hooks/session_start_reminder.py
```

## 作者

**KAI LI** · 立凯咨询 · AI经营改善顾问 · AI Operations Improvement Consultant

邮箱：superlady2049@gmail.com

扫码添加飞书联系人：

<img src="assets/lark-qr.png" width="220" alt="KAI LI 飞书二维码">

MIT License

## English summary

A Claude Code skill to cut usage burn: model routing for subagents, session hygiene (one task per session, hand off after ~4h, `/clear` when switching), forecasting big jobs before dispatch, killing idle agents, a PreToolUse hook that blocks `general-purpose` subagents launched without an explicit `model` (and requires a stated reason for opus/fable), and a zero-token weekly review script design reading `~/.claude/projects/**/*.jsonl`. Docs are in Chinese; the hook scripts work as-is.
