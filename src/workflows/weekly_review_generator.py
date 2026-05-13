from __future__ import annotations

from pathlib import Path

from common import BASE_DIR, TODAY, ensure_dirs, read_json


def run() -> Path:
    ensure_dirs()
    output_path = BASE_DIR / "outputs" / TODAY / f"weekly_review_{TODAY}.md"
    hot_topics = read_json(BASE_DIR / "data" / "raw" / f"hot_topics_{TODAY}.json")
    viral_items = read_json(BASE_DIR / "data" / "processed" / f"viral_analysis_{TODAY}.json")
    high_conversion = [item for item in hot_topics if item.get("content_class") == "C"]

    lines = [
        f"# 周复盘 - {TODAY}",
        "",
        "## 本周爆款共性",
        "",
        "- 强结果导向比纯工具介绍更适合当前账号定位。",
        "- 能把 AI 讲成业务动作的内容，更容易连接创业者需求。",
        "- 小白内容要先降低门槛，再引出工作流或智能体。",
        "",
        "## 本周失败共性",
        "",
        "- 纯模型更新、纯参数对比、炫技型演示暂不适合作为主线。",
        "- 缺少真实场景的工具推荐容易吸粉弱、转化弱。",
        "",
        "## 本周新增有效标题模板",
        "",
        "- 创业者做 AI，最贵的不是工具费，是试错时间",
        "- AI 小白别乱学，先做出这 3 个结果",
        "- 哪些业务最适合先上 XX 智能体",
        "",
        "## 本周新增有效开头模板",
        "",
        "- 如果你是创业者，还在自己低效折腾，这条更值得看。",
        "- 如果你的业务每天都有大量重复咨询，这个场景最适合先上智能体。",
        "",
        "## 本周新增高转化内容模型",
        "",
        "- 业务痛点 -> 试错成本 -> 现成智能体结果 -> 私信诊断 CTA",
        "- 重复工作 -> 标准化判断 -> 智能体承接 -> 人工只处理复杂问题",
        "",
        "## 哪类内容适合卖智能体",
        "",
    ]

    if high_conversion:
        for item in high_conversion[:5]:
            lines.append(f"- {item.get('topic_name')}：{item.get('monetization_link')}")
    else:
        lines.append("- 客服、销售跟进、线索整理、内容生产这类场景更适合产品化。")

    lines.extend(
        [
            "",
            "## 哪类内容只能吸粉不适合成交",
            "",
            "- 泛新闻、泛模型更新、泛工具榜单，除非能落到明确业务场景。",
            "",
            "## 下周优先测试方向",
            "",
            "- 客服智能体场景短视频",
            "- 创业者 AI 试错成本观点口播",
            "- AI 小白 7 天入门路径",
            "",
            "## 该淘汰什么内容形式",
            "",
            "- 没有案例、没有场景、没有 CTA 的工具罗列。",
            "",
            "## 样本数量",
            "",
            f"- 热点样本：{len(hot_topics)}",
            f"- 拆解样本：{len(viral_items)}",
        ]
    )

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


if __name__ == "__main__":
    print(run())
