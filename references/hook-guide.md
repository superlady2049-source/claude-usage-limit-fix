## 六、防错钩子（让错误做不出来）

文字规则靠自觉，会被违反。把关键规则做成钩子，见 [hooks/agent_model_gate.py](../hooks/agent_model_gate.py)：

- 派 general-purpose（或未指定类型）不写 `model`：拦截。
- 指定 opus/fable 却没在派活说明里写「【理由】…」：拦截。
- 同时把每次派活记到日志，供复盘对照「派出数 vs 交回数」。

安装：把脚本放到 `~/.claude/hooks/`，在 `~/.claude/settings.json` 的 `hooks.PreToolUse` 里加：

```json
{"matcher": "Agent", "hooks": [{"type": "command", "command": "python3 ~/.claude/hooks/agent_model_gate.py", "timeout": 10}]}
```

改 settings.json 后一般会被自动识别；若没生效，再开新会话。

**覆盖范围（别过度相信）：** 钩子只管派 general-purpose（或未指定类型）。你自己的自定义 agent 若在定义文件里写了 `model: opus`，不受它管，需要在定义里改。

完整的 `~/.claude/settings.json` 示例（合并到你现有的 `hooks` 里，已有 `PreToolUse` 就把数组项并进去）：

```json
{
  "hooks": {
    "PreToolUse": [
      {"matcher": "Agent", "hooks": [{"type": "command", "command": "python3 ~/.claude/hooks/agent_model_gate.py", "timeout": 10}]}
    ],
    "SessionStart": [
      {"hooks": [{"type": "command", "command": "python3 ~/.claude/hooks/session_start_reminder.py", "timeout": 5}]}
    ]
  }
}
```
