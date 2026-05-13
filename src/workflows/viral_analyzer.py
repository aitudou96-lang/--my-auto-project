from __future__ import annotations

import json
from pathlib import Path

from common import BASE_DIR, TODAY, ensure_dirs, write_json


def load_json(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def infer_hook(topic_name: str, audience: str) -> str:
    if audience == "AI小白":
        return f"如果你刚开始学 AI，还在乱学工具，这条你先看：{topic_name}"
    return f"如果你是创业者，还在自己低效折腾，这条更值得看：{topic_name}"


def infer_cta(content_class: str) -> str:
    if content_class == "C":
        return "如果你有明确业务场景，欢迎私信我判断适不适合直接上智能体。"
    if content_class == "B":
        return "如果你想看完整流程，我可以继续拆成可直接照着做的版本。"
    return "想少走弯路，先把这类基础场景做起来。"


def analyze_topic(item: dict[str, object]) -> dict[str, object]:
    topic_name = str(item.get("topic_name", item.get("latest_topic_guess", "")))
    audience = str(item.get("audience", item.get("audience_hint", "AI小白")))
    content_class = str(item.get("content_class", "B"))
    platform = str(item.get("platform", ""))
    pillar = str(item.get("pillar", item.get("focus", "待分类")))
    return {
        "platform": platform,
        "link": "internal_seed_sample",
        "category": pillar,
        "audience": audience,
        "title_structure": "痛点/误区 + 结果承诺 + 场景结论",
        "hook_3s": infer_hook(topic_name, audience),
        "conflict_point": "用户当前的低效路径与更短结果路径之间的冲突",
        "emotion_point": "怕落后、怕浪费时间、想快速看见结果",
        "core_promise": f"通过“{topic_name}”让用户更快看见 AI 的实际价值",
        "narrative_rhythm": "先打误区，再给结论，再给场景，再收行动",
        "information_density": "中高",
        "ending_cta": infer_cta(content_class),
        "comments_focus": "是不是小白也能做、适合什么行业、有没有现成方案",
        "reusable_mechanism": "用具体业务结果解释 AI，而不是只讲工具和概念",
        "cannot_copy": "不能照搬原句式、不能复刻原作者表达、不能伪造真实案例",
    }


def run() -> Path:
    ensure_dirs()
    hot_topics = load_json(BASE_DIR / "data" / "raw" / f"hot_topics_{TODAY}.json")
    competitors = load_json(BASE_DIR / "data" / "raw" / f"competitors_{TODAY}.json")
    payload = [analyze_topic(item) for item in hot_topics[:5]]
    payload.extend(analyze_topic(item) for item in competitors[:3])
    output_path = BASE_DIR / "data" / "processed" / f"viral_analysis_{TODAY}.json"
    write_json(output_path, payload)
    return output_path


if __name__ == "__main__":
    saved = run()
    print(saved)
