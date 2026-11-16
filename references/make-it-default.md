## 让它默认生效（技能不会自己每次触发）

技能是「软触发」：只有模型判断任务匹配时才会读它，不保证每次都用。想让它成为默认动作，做两件事：

1. **在你的全局规则 `~/.claude/CLAUDE.md` 加一句：** 「派 agent、选模型、开长会话、评审测试前，先调用 `claude-usage-limit-fix` 技能。」每个新会话开头都会读到。
2. **加会话开始钩子**（`hooks/session_start_reminder.py`），每次新会话自动注入一句提醒。在 `~/.claude/settings.json` 的 `hooks` 里加：

```json
"SessionStart": [{"hooks": [{"type": "command", "command": "python3 ~/.claude/hooks/session_start_reminder.py", "timeout": 5}]}]
```

仍然要靠钩子兜底：第六节的派活钩子是唯一不依赖模型自觉的硬约束。
