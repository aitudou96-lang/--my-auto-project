# 知识库自动回写模块

## 目标

把每日爆款拆解和文案包中的有效标题机制、开头机制、转化提醒沉淀到知识库。

## 输入

- `data/processed/viral_analysis_YYYY-MM-DD.json`
- `outputs/YYYY-MM-DD/daily_scripts_YYYY-MM-DD.md`

## 输出

- `data/knowledge/title_hooks_library.md`

## 当前策略

- 每天按日期追加一个自动回写区块
- 不复刻原作者表达，只沉淀结构机制
- 优先保留能服务智能体成交的标题、钩子和 CTA 机制
