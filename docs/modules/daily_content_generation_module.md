# 今日文案包自动生成模块

## 目标

把每日评分后的重点选题转成可直接进入创作流程的文案包。

## 输入

- `outputs/YYYY-MM-DD/daily_plan_YYYY-MM-DD.md`
- `data/processed/viral_analysis_YYYY-MM-DD.json`
- 标题库、钩子库、内容模型库

## 输出

- `outputs/YYYY-MM-DD/daily_scripts_YYYY-MM-DD.md`
- `outputs/YYYY-MM-DD/daily_todo_for_user_YYYY-MM-DD.md`

## 当前策略

- 默认优先生成 3 个重点选题
- 同时覆盖 A/B/C 三类内容
- 默认先适配抖音，再给小红书、视频号、B站建议
