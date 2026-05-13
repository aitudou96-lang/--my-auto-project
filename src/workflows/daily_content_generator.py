from __future__ import annotations

from pathlib import Path

from common import BASE_DIR, TODAY, ensure_dirs, read_json


def _titles(topic: str, content_class: str) -> list[str]:
    if content_class == "C":
        return [
            topic,
            "创业者做 AI，最贵的不是工具费，是试错时间",
            "为什么我不建议老板自己从头搭 AI",
            "会算账的创业者，先买结果，不买折腾",
            "你以为自己搭更省钱，其实更贵",
            "现成智能体，可能比你自己研究 30 天更划算",
            "别让学 AI 变成拖慢业务的借口",
            "什么业务最适合先上智能体",
            "一个智能体，先帮你省掉重复工作",
            "真正值得买的 AI，不是工具，是结果",
        ]
    return [
        topic,
        "AI 小白别乱学，先做出这 3 个结果",
        "普通人学 AI，最先见效的不是写代码",
        "很多人学 AI 没结果，是第一步就错了",
        "别再收藏工具了，先把这个场景跑通",
        "不懂代码，也能先用 AI 做出结果",
        "AI 入门最短路径，我建议你这样开始",
        "新手学 AI，不要贪多，先拿下这个用途",
        "你不是不会用 AI，是不知道先解决什么问题",
        "AI 对普通人最有用的地方，其实很简单",
    ]


def _hooks(topic: str, audience: str) -> list[str]:
    if audience == "创业者":
        return [
            "如果你是创业者，还在自己低效折腾 AI，这条更值得看。",
            "很多老板以为自己搭更省钱，结果最贵的是时间。",
            "你不是缺更多教程，你是缺一套能跑起来的结果。",
            "会算账的创业者，先看 AI 能不能帮业务省人省时间。",
            "别把学 AI 这件事，变成拖慢业务的借口。",
        ]
    return [
        "AI 小白最容易犯的错，就是一上来学太多。",
        "很多人不是不会用 AI，而是第一步就选错了。",
        "先别管模型多厉害，普通人先看能不能帮你省时间。",
        "如果你现在还在到处找 AI 神器，你大概率学不明白。",
        f"你要是刚接触 AI，就先看这个场景：{topic}",
    ]


def _script_block(item: dict[str, object], index: int) -> list[str]:
    topic = str(item.get("topic_name", "待定选题"))
    audience = str(item.get("audience", "AI小白"))
    content_class = str(item.get("content_class", "A"))
    pillar = str(item.get("pillar", "AI小白入门"))
    titles = _titles(topic, content_class)
    hooks = _hooks(topic, audience)
    cta = "如果你有明确业务场景，欢迎私信我判断适不适合直接上智能体。" if content_class == "C" else "想少走弯路，先从能立刻省时间的 AI 用法开始。"
    cover = "先买结果，少走弯路" if content_class == "C" else "AI 小白先做出结果"

    lines = [
        f"## 重点选题 {index}",
        "",
        "### 选题",
        topic,
        "",
        "### 分类",
        f"{content_class} 类内容 / {pillar}",
        "",
        "### 10 个标题",
        "",
    ]
    lines.extend(f"{i}. {title}" for i, title in enumerate(titles, start=1))
    lines.extend(["", "### 5 个开头钩子", ""])
    lines.extend(f"{i}. {hook}" for i, hook in enumerate(hooks, start=1))
    lines.extend(
        [
            "",
            "### 3 个脚本结构版本",
            "",
            "1. 痛点对比型：现状问题 -> 错误路径 -> 更短路径 -> CTA",
            "2. 案例拆解型：具体场景 -> 操作过程 -> 前后对比 -> CTA",
            "3. 清单判断型：适合谁 -> 先做什么 -> 不建议做什么 -> CTA",
            "",
            "### 短视频口播版",
            "",
            f"{hooks[0]}这件事的核心不是工具多不多，而是能不能帮你更快拿到结果。围绕“{topic}”，先把场景讲清楚，再给用户一个能马上理解的动作：哪些重复工作可以交给 AI，哪些部分仍然需要人工判断。这样用户不会觉得 AI 很虚，反而会觉得这个东西跟自己的生意或效率直接相关。",
            "",
            "### 混剪版",
            "",
            "开场用痛点画面建立冲突，中段用流程图或屏录展示 AI 承接动作，结尾用前后对比和 CTA 收口。",
            "",
            "### 强情绪版",
            "",
            "很多人不是不想用 AI，而是把时间浪费在了错误路径上。真正该做的是先找一个能省时间、能提效、能带来业务结果的场景跑通。",
            "",
            "### 创业者版",
            "",
            "如果你是老板，先别把 AI 当成新玩具。先看它能不能帮你省掉重复沟通、整理线索、跟进客户、生产内容这些真实成本。",
            "",
            "### AI 小白版",
            "",
            "你不需要一开始就懂复杂技术。先选一个具体场景，让 AI 帮你做出一个看得见的结果。",
            "",
            "### 封面文案",
            "",
            cover,
            "",
            "### 首评文案",
            "",
            "如果你想看我把这个场景拆成可直接照着做的流程，评论区打“流程”。",
            "",
            "### CTA",
            "",
            cta,
            "",
            "### 剪辑辅助",
            "",
            "- 分镜建议：痛点画面 -> 出镜结论 -> 流程展示 -> 前后对比 -> CTA",
            "- 字幕重点词：结果、提效、少走弯路、智能体、自动化",
            "- 镜头需求清单：出镜口播、电脑屏录、业务流程图、聊天或表格示意",
            "- 搜索素材关键词：AI workflow, business automation, customer support, productivity",
            "- 可替代镜头方案：白底大字卡+流程图动画",
            "- BGM 风格建议：清晰推进、偏商务效率感",
            "- 节奏建议：前 3 秒给结论，20 秒内讲完核心机制",
            "- 必须原创拍摄镜头：你本人出镜讲观点和 CTA",
            "- 可用合规素材镜头：办公环境、键盘操作、通用聊天界面示意",
            "",
        ]
    )
    return lines


def _load_priority_items() -> list[dict[str, object]]:
    hot_topics = read_json(BASE_DIR / "data" / "raw" / f"hot_topics_{TODAY}.json")
    return sorted(hot_topics, key=lambda item: int(item.get("final_score", 0)), reverse=True)[:3]


def write_daily_scripts(items: list[dict[str, object]]) -> Path:
    output_path = BASE_DIR / "outputs" / TODAY / f"daily_scripts_{TODAY}.md"
    lines = [f"# 每日脚本包 - {TODAY}", ""]
    for index, item in enumerate(items, start=1):
        lines.extend(_script_block(item, index))
    lines.extend(
        [
            "## 平台适配建议",
            "",
            "### 抖音",
            "",
            "- 开头先下结论，前 3 秒给强利益点。",
            "",
            "### 小红书",
            "",
            "- 写成经验笔记，多补过程感和踩坑感。",
            "",
            "### 视频号",
            "",
            "- 强调经营、成本、效率和可信案例。",
            "",
            "### B站",
            "",
            "- 扩成系统教程，增加完整操作流程和复盘。",
        ]
    )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def write_daily_todo() -> Path:
    output_path = BASE_DIR / "outputs" / TODAY / f"daily_todo_for_user_{TODAY}.md"
    output_path.write_text(
        "\n".join(
            [
                f"# 待用户协助事项 - {TODAY}",
                "",
                "当前无需人工协助。",
                "",
                "## 说明",
                "",
                "本次流程使用本地结构化样本完成采集、评分、拆解、文案包生成和知识库回写。",
                "",
                "后续接入真实平台采集时，需要你协助登录、扫码、验证码或授权。",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return output_path


def run() -> dict[str, Path]:
    ensure_dirs()
    items = _load_priority_items()
    return {
        "daily_scripts": write_daily_scripts(items),
        "daily_todo": write_daily_todo(),
    }


if __name__ == "__main__":
    print(run())
