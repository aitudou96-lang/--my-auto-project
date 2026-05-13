# 每日选题评分模块

## 目标

把热点采集、竞品采集、爆款拆解的结果统一收口，输出当天的：

- 今日优先选题
- 今日可观察选题
- 今日不建议做的选题

## 输入

- `data/raw/hot_topics_YYYY-MM-DD.json`
- `data/raw/competitors_YYYY-MM-DD.json`
- `data/processed/viral_analysis_YYYY-MM-DD.json`

## 输出

- `outputs/YYYY-MM-DD/daily_plan_YYYY-MM-DD.md`
- `outputs/YYYY-MM-DD/daily_materials_YYYY-MM-DD.csv`

## 当前策略

- 优先保留与 AI 小白、创业者、智能体变现强相关内容
- 优先保留 A/B/C 三类内容都能覆盖的选题组合
- 降低纯新闻、纯模型参数、炫技型内容优先级
