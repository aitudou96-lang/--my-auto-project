from __future__ import annotations

from pathlib import Path

from common import BASE_DIR, TODAY, ensure_dirs, read_json


def score_items() -> list[dict[str, object]]:
    hot_topics = read_json(BASE_DIR / "data" / "raw" / f"hot_topics_{TODAY}.json")
    items: list[dict[str, object]] = []
    for item in hot_topics:
        final_score = int(item.get("final_score", 0))
        action = "watch"
        if final_score >= 85:
            action = "priority"
        elif final_score < 72:
            action = "skip"
        record = dict(item)
        record["score_action"] = action
        items.append(record)
    return items


def _priority_label(score: int) -> str:
    if score >= 85:
        return "高"
    if score >= 78:
        return "中高"
    return "中"


def _difficulty_label(score: int) -> str:
    if score >= 86:
        return "低"
    if score >= 78:
        return "中"
    return "中高"


def _conversion_label(score: int) -> str:
    if score >= 90:
        return "高"
    if score >= 78:
        return "中高"
    return "中"


def write_daily_materials(items: list[dict[str, object]]) -> Path:
    output_path = BASE_DIR / "outputs" / TODAY / f"daily_materials_{TODAY}.csv"
    lines = ["date,platform,topic_name,content_class,pillar,audience,source_type,status,score,notes"]
    for item in items:
        row = [
            TODAY,
            str(item.get("platform", "")),
            str(item.get("topic_name", "")).replace(",", "，"),
            str(item.get("content_class", "")),
            str(item.get("pillar", "")),
            str(item.get("audience", "")),
            str(item.get("source_type", "")),
            str(item.get("score_action", "watch")),
            str(item.get("final_score", "")),
            str(item.get("notes", "")).replace(",", "，"),
        ]
        lines.append(",".join(row))
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def write_daily_plan(items: list[dict[str, object]]) -> Path:
    output_path = BASE_DIR / "outputs" / TODAY / f"daily_plan_{TODAY}.md"
    priority = [item for item in items if item.get("score_action") == "priority"]
    watch = [item for item in items if item.get("score_action") == "watch"]

    lines = [
        f"# 每日选题总览 - {TODAY}",
        "",
        "## 今日优先选题",
        "",
        "| 类别 | 选题名称 | 为什么值得做 | 适合人群 | 与智能体变现关系 | 形式建议 | 优先级 | 制作难度 | 转化潜力 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for item in priority[:8]:
        score = int(item.get("final_score", 0))
        lines.append(
            "| {content_class} | {topic_name} | {why_now} | {audience} | {monetization_link} | 口播+案例/屏录 | {priority} | {difficulty} | {conversion} |".format(
                content_class=item.get("content_class", ""),
                topic_name=item.get("topic_name", ""),
                why_now=item.get("why_now", ""),
                audience=item.get("audience", ""),
                monetization_link=item.get("monetization_link", ""),
                priority=_priority_label(score),
                difficulty=_difficulty_label(int(item.get("production_difficulty_score", 0))),
                conversion=_conversion_label(int(item.get("conversion_potential_score", 0))),
            )
        )

    lines.extend(["", "## 今日可观察选题", "", "| 选题名称 | 观察原因 | 暂不立刻做的原因 |", "|---|---|---|"])
    for item in watch[:5]:
        lines.append(f"| {item.get('topic_name', '')} | {item.get('why_now', '')} | 需要更多真实样本或案例支撑 |")

    lines.extend(
        [
            "",
            "## 今日不建议做的选题",
            "",
            "| 选题名称 | 不建议原因 |",
            "|---|---|",
            "| 纯模型参数对比 | 与 AI 小白和创业者的真实购买动机弱相关 |",
            "| 只讲最新模型更新 | 热点短、信任弱、难转化 |",
            "| 炫技型自动化演示 | 容易吸引错流量，成交质量低 |",
        ]
    )
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def run() -> dict[str, object]:
    ensure_dirs()
    items = score_items()
    return {
        "items": items,
        "daily_plan": write_daily_plan(items),
        "daily_materials": write_daily_materials(items),
    }


if __name__ == "__main__":
    print(run())
