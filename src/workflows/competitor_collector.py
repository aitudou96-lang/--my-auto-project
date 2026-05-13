from __future__ import annotations

import csv
from pathlib import Path

from common import BASE_DIR, TODAY, ensure_dirs, simple_yaml_list_map, write_json


def build_config_posts() -> list[dict[str, str]]:
    config = simple_yaml_list_map(BASE_DIR / "config" / "competitors.yaml")
    rows: list[dict[str, str]] = []
    for platform, accounts in config.items():
        for account in accounts:
            rows.append(
                {
                    "platform": platform,
                    "account_name": account.get("name", "未命名竞品"),
                    "handle": account.get("handle", ""),
                    "focus": account.get("focus", ""),
                    "audience": account.get("audience", ""),
                    "priority": account.get("priority", ""),
                    "sample_status": "pending_login",
                    "latest_topic_guess": f"{account.get('focus', 'AI内容')}相关选题待采集",
                    "content_goal_guess": "待登录平台后判断是拉新、信任还是转化",
                    "note": "当前为结构化占位记录，待登录平台后补真实内容。",
                }
            )
    return rows


def load_manual_samples() -> list[dict[str, str]]:
    path = BASE_DIR / "data" / "raw" / "manual_inputs" / "competitor_manual_input.csv"
    if not path.exists():
        return []
    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row.get("account_name"):
                rows.append(dict(row))
    return rows


def run() -> Path:
    ensure_dirs()
    output_path = BASE_DIR / "data" / "raw" / f"competitors_{TODAY}.json"
    write_json(output_path, build_config_posts() + load_manual_samples())
    return output_path


if __name__ == "__main__":
    saved = run()
    print(saved)
