from __future__ import annotations

from pathlib import Path

from common import BASE_DIR, TODAY, ensure_dirs, read_json


def run() -> Path:
    ensure_dirs()
    path = BASE_DIR / "data" / "knowledge" / "title_hooks_library.md"
    viral_items = read_json(BASE_DIR / "data" / "processed" / f"viral_analysis_{TODAY}.json")
    existing = path.read_text(encoding="utf-8") if path.exists() else "# 标题库与钩子库\n"

    marker = f"## 自动回写 - {TODAY}"
    if marker in existing:
        return path

    lines = ["", marker, "", "### 新增标题机制", ""]
    for item in viral_items[:5]:
        category = item.get("category", "待分类")
        audience = item.get("audience", "待确认")
        lines.append(f"- {category} / {audience}：痛点或误区 + 具体结果 + 行动场景")

    lines.extend(["", "### 新增开头机制", ""])
    for item in viral_items[:5]:
        hook = str(item.get("hook_3s", "")).strip()
        if hook:
            lines.append(f"- {hook}")

    lines.extend(["", "### 转化提醒", ""])
    lines.append("- C 类内容优先把 CTA 指向业务场景诊断、智能体方案咨询、现成工作流购买。")

    path.write_text(existing.rstrip() + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    return path


if __name__ == "__main__":
    print(run())
