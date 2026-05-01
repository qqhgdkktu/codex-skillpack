#!/usr/bin/env python3
"""Validate my-codex-plugin structure and bundled skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
SKILLS_DIR = ROOT / "skills"
SOURCES_JSON = ROOT / "SKILL_SOURCES.json"
EXPECTED_SKILL_COUNT = 41


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path} is invalid JSON: {exc}")


def frontmatter_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*[\"']?([^\"'\n]+)", text, re.M)
    return match.group(1).strip() if match else None


def main() -> int:
    manifest = load_json(PLUGIN_JSON)
    if manifest.get("name") != "my-codex-plugin":
        fail("plugin.json name must be my-codex-plugin")
    if manifest.get("skills") != "./skills/":
        fail("plugin.json skills must be ./skills/")

    source_manifest = load_json(SOURCES_JSON)
    imported = {entry["skill"] for entry in source_manifest.get("sources", [])}
    if len(imported) != 40:
        fail(f"expected 40 imported skills in SKILL_SOURCES.json, found {len(imported)}")

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if len(skill_dirs) != EXPECTED_SKILL_COUNT:
        fail(f"expected {EXPECTED_SKILL_COUNT} skill dirs, found {len(skill_dirs)}")

    names: list[str] = []
    missing_license: list[str] = []
    for skill_dir in skill_dirs:
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            fail(f"{skill_dir.name} is missing SKILL.md")
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        name = frontmatter_value(text, "name")
        description = frontmatter_value(text, "description")
        if not name:
            fail(f"{skill_dir.name}/SKILL.md is missing name frontmatter")
        if not description:
            fail(f"{skill_dir.name}/SKILL.md is missing description frontmatter")
        names.append(name)
        if skill_dir.name != "plugin-check" and not (skill_dir / "LICENSE.txt").exists():
            missing_license.append(skill_dir.name)

    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        fail(f"duplicate skill names: {duplicates}")
    if missing_license:
        fail(f"imported skills missing LICENSE.txt: {missing_license}")

    print(f"ok: {len(skill_dirs)} skills, {len(imported)} imported, no duplicate names")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
