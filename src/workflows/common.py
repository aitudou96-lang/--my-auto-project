from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any


BASE_DIR = Path(r"E:\Codex位置\New project 2")
TODAY = str(date.today())


@dataclass
class TopicCandidate:
    topic_name: str
    platform: str
    source_type: str
    audience: str
    content_class: str
    pillar: str
    heat_score: int
    account_fit_score: int
    monetization_fit_score: int
    explainability_score: int
    production_difficulty_score: int
    conversion_potential_score: int
    urgency_score: int
    recommended_action: str
    why_now: str
    monetization_link: str
    notes: str

    def final_score(self) -> int:
        return round(
            self.heat_score * 0.20
            + self.account_fit_score * 0.20
            + self.monetization_fit_score * 0.20
            + self.explainability_score * 0.10
            + self.production_difficulty_score * 0.10
            + self.conversion_potential_score * 0.15
            + self.urgency_score * 0.05
        )


def ensure_dirs() -> None:
    for path in [
        BASE_DIR / "config",
        BASE_DIR / "data",
        BASE_DIR / "data" / "raw",
        BASE_DIR / "data" / "processed",
        BASE_DIR / "data" / "knowledge",
        BASE_DIR / "docs",
        BASE_DIR / "outputs" / TODAY,
        BASE_DIR / "src",
        BASE_DIR / "src" / "workflows",
    ]:
        path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def serialize_candidates(items: list[TopicCandidate]) -> list[dict[str, Any]]:
    serialized: list[dict[str, Any]] = []
    for item in items:
        row = asdict(item)
        row["final_score"] = item.final_score()
        serialized.append(row)
    return serialized


def simple_yaml_list_map(path: Path) -> dict[str, list[dict[str, str]]]:
    result: dict[str, list[dict[str, str]]] = {}
    current_section: str | None = None
    current_item: dict[str, str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if not line.startswith(" ") and stripped.endswith(":"):
            continue
        if line.startswith("  ") and stripped.endswith(":") and not stripped.startswith("-"):
            current_section = stripped[:-1]
            result.setdefault(current_section, [])
            current_item = None
            continue
        if stripped.startswith("- "):
            current_item = {}
            if current_section is None:
                continue
            result[current_section].append(current_item)
            payload = stripped[2:]
            if ":" in payload:
                key, value = payload.split(":", 1)
                current_item[key.strip()] = value.strip()
            continue
        if current_item is not None and ":" in stripped:
            key, value = stripped.split(":", 1)
            current_item[key.strip()] = value.strip()
    return result
