from __future__ import annotations

import csv
from pathlib import Path

from common import BASE_DIR, TODAY, TopicCandidate, ensure_dirs, serialize_candidates, write_json


def build_seed_topics() -> list[TopicCandidate]:
    return [
        TopicCandidate(
            topic_name="AI 小白别乱学，先学哪 3 个最容易出结果",
            platform="douyin",
            source_type="seed_hot_topic",
            audience="AI小白",
            content_class="A",
            pillar="AI小白入门",
            heat_score=84,
            account_fit_score=92,
            monetization_fit_score=78,
            explainability_score=93,
            production_difficulty_score=88,
            conversion_potential_score=72,
            urgency_score=75,
            recommended_action="do_now",
            why_now="持续有新手入场，且最容易形成拉新内容。",
            monetization_link="可衔接入门型智能体、陪跑和训练营。",
            notes="优先做强钩子口播版。",
        ),
        TopicCandidate(
            topic_name="创业者为什么别自己瞎折腾 AI，直接买现成智能体更省时间",
            platform="video_channel",
            source_type="seed_hot_topic",
            audience="创业者",
            content_class="C",
            pillar="创业者提效与变现",
            heat_score=80,
            account_fit_score=95,
            monetization_fit_score=96,
            explainability_score=90,
            production_difficulty_score=86,
            conversion_potential_score=94,
            urgency_score=72,
            recommended_action="do_now",
            why_now="创业者最关心结果，不关心复杂技术细节。",
            monetization_link="直接承接智能体产品、定制服务和咨询。",
            notes="适合视频号和抖音双版本测试。",
        ),
    ]


def load_manual_topics() -> list[TopicCandidate]:
    path = BASE_DIR / "data" / "raw" / "manual_inputs" / "hot_topics_manual_input.csv"
    if not path.exists():
        return []
    rows: list[TopicCandidate] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if not row.get("topic_name"):
                continue
            rows.append(
                TopicCandidate(
                    topic_name=row["topic_name"],
                    platform=row.get("platform", "manual"),
                    source_type=row.get("source_name", "manual_input"),
                    audience=row.get("audience_hint", "AI小白"),
                    content_class=row.get("content_class", "A"),
                    pillar=row.get("pillar", "AI小白入门"),
                    heat_score=70,
                    account_fit_score=85,
                    monetization_fit_score=80,
                    explainability_score=85,
                    production_difficulty_score=80,
                    conversion_potential_score=78,
                    urgency_score=65,
                    recommended_action="watch",
                    why_now=row.get("why_now", "手动补录待验证"),
                    monetization_link=row.get("monetization_link", "待补充"),
                    notes=row.get("notes", ""),
                )
            )
    return rows


def run() -> Path:
    ensure_dirs()
    output_path = BASE_DIR / "data" / "raw" / f"hot_topics_{TODAY}.json"
    payload = serialize_candidates(build_seed_topics() + load_manual_topics())
    write_json(output_path, payload)
    return output_path


if __name__ == "__main__":
    saved = run()
    print(saved)
