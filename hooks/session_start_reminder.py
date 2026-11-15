#!/usr/bin/env python3
"""会话开始时注入一句提醒：已安装 claude-usage-limit-fix 技能，派活、开长会话前先调用。"""
print("【省用量提醒】派 agent、选模型、开长会话、评审测试前，先调用 claude-usage-limit-fix 技能；"
      "general-purpose 必须写 model；预计超 30 万 token 先问使用者；会话超 4 小时交接。")
