# AI 自媒体增长操作系统

本项目服务于一个明确目标：通过 AI 内容增长，最终推动智能体、AI 工作流、AI 自动化方案和定制服务成交。

## 核心定位

- 赛道：AI
- 目标用户：AI 小白、创业者、个体经营者、副业人群
- 核心变现：售卖智能体、工作流、自动化方案、咨询陪跑、定制交付
- 内容原则：讲人话、强实操、强结果、强案例、低术语、可转化

## 目录说明

- `config/`：配置文件
- `data/`：素材、样本、知识库数据
- `docs/`：方法论、流程和规则文档
- `outputs/YYYY-MM-DD/`：每日导出结果
- `src/`：流程脚本、模板、数据结构

## 当前阶段

第一阶段已完成：

- 项目目录搭建
- 配置文件模板
- 数据结构设计
- 每日执行主流程设计
- 每日导出模板
- 示例文案包初始化
- 待用户协助机制设计
- 内容知识库文件初始化
## 一键运行

本项目固定根目录：

`E:\Codex位置\New project 2\`

本项目固定使用已验证可用的 Python 解释器：

`E:\Codex位置\New project 2\.venv\Scripts\python.exe`

以后日更运行方式：

- 双击 `run_daily.bat`
- 或在 PowerShell 中执行：`.\run_daily.ps1`

周复盘运行方式：

- 双击 `run_weekly.bat`
- 或在 PowerShell 中执行：`.\run_weekly.ps1`

说明：

- `run_daily` 会执行 `src\workflows\daily_run.py`
- `run_weekly` 会执行 `src\workflows\weekly_review_generator.py`
- 默认输出到 `outputs\当天日期\`
- 如需指定日期，可先设置环境变量 `CONTENT_DATE`


