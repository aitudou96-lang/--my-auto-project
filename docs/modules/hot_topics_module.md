# 热点采集模块

## 目标

优先抓与 AI 赛道、AI 小白、创业者、智能体变现相关的热点，而不是泛流量新闻。

## 当前输入来源

- 内置种子样本
- 手动补录 CSV
- 后续可接入平台或网页采集

## 当前输出

- `data/raw/hot_topics_YYYY-MM-DD.json`

## 手动补录入口

- `src/templates/hot_topics_manual_input.csv`
- 可复制到 `data/raw/manual_inputs/` 后再由后续流程读取
