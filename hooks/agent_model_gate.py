#!/usr/bin/env python3
"""防错：派 general-purpose（或未指定类型）子智能体必须显式写 model，否则拦截。
同时把每次派活记到 agent_dispatch.log，供用量复盘对照。"""
import json, sys, time, os
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
if d.get("tool_name") not in ("Agent", "Task"):
    sys.exit(0)
i = d.get("tool_input") or {}
t = i.get("subagent_type") or "general-purpose"
m = i.get("model")
try:
    with open(os.path.expanduser("~/.claude/hooks/agent_dispatch.log"), "a", encoding="utf-8") as f:
        f.write(f"{time.strftime('%F %T')}\t{t}\t{m or '-'}\t{i.get('description','')}\n")
except Exception:
    pass
if t in ("general-purpose", "claude") and not m:
    sys.stderr.write("拦截：派 general-purpose 必须显式写 model（取数/检查/截图用 haiku 或 sonnet，开发/因果分析才用 opus）。"
                     "有专用 agent 的活（ad-data-fetcher、kb-checker、report-developer、Explore）请用专用的。")
    sys.exit(2)
if t in ("general-purpose", "claude") and m in ("opus", "fable"):
    if "【理由】" not in (i.get("prompt") or ""):
        sys.stderr.write("拦截：general-purpose 指定 %s 必须在派活说明里写「【理由】…」（只有开发、因果分析、上线前终审才可用；取数/检查/截图改用 haiku 或 sonnet）。" % m)
        sys.exit(2)
sys.exit(0)
