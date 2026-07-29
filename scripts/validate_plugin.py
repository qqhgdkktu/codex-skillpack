#!/usr/bin/env python3
"""Validate codex-skillpack structure and bundled skills."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
SKILLS_DIR = ROOT / "skills"
SOURCES_JSON = ROOT / "SKILL_SOURCES.json"
EXPECTED_SKILL_COUNT = 32
EXPECTED_VERSION = "0.4.0"
MAX_DESCRIPTION_CHARS = 220
MAX_CATALOG_CHARS = 6000
MAX_SKILL_LINES = 500
ALLOWED_FRONTMATTER_KEYS = {"name", "description"}
REQUIRED_DOCS = [
    "README.md",
    "LICENSE.md",
    "NOTICE.md",
    "THIRD_PARTY_NOTICES.md",
    "PRIVACY.md",
    "TERMS.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "docs/index.html",
]


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


def frontmatter_keys(text: str) -> set[str]:
    if not text.startswith("---\n"):
        return set()
    parts = text.split("---", 2)
    if len(parts) < 3:
        return set()
    keys: set[str] = set()
    for line in parts[1].splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):", line)
        if match:
            keys.add(match.group(1))
    return keys


def validate_relative_links(markdown_path: Path, text: str) -> None:
    for raw_target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = raw_target.strip().strip("<>").split("#", 1)[0]
        if not target or target.startswith(("#", "/", "mailto:")) or "://" in target:
            continue
        if not (markdown_path.parent / target).resolve().exists():
            fail(f"{markdown_path.relative_to(ROOT)} has broken relative link: {raw_target}")


def validate_skill_path_references(skill_md: Path, text: str) -> None:
    for skill_name in re.findall(r"skills/([a-z0-9]+(?:-[a-z0-9]+)*)/SKILL\.md", text):
        if not (SKILLS_DIR / skill_name / "SKILL.md").exists():
            fail(
                f"{skill_md.relative_to(ROOT)} references missing bundled skill: "
                f"skills/{skill_name}/SKILL.md"
            )


def main() -> int:
    manifest = load_json(PLUGIN_JSON)
    if manifest.get("name") != "codex-skillpack":
        fail("plugin.json name must be codex-skillpack")
    if manifest.get("version") != EXPECTED_VERSION:
        fail(f"plugin.json version must be {EXPECTED_VERSION}")
    if not re.fullmatch(r"(?:0|[1-9]\d*)(?:\.(?:0|[1-9]\d*)){2}", EXPECTED_VERSION):
        fail(f"expected version is not strict semver: {EXPECTED_VERSION}")
    if manifest.get("skills") != "./skills/":
        fail("plugin.json skills must be ./skills/")
    if manifest.get("license") != "SEE LICENSE.md AND NOTICE.md":
        fail("plugin.json license must point to LICENSE.md and NOTICE.md")
    default_prompts = manifest.get("interface", {}).get("defaultPrompt", [])
    if len(default_prompts) > 3:
        fail("plugin.json interface.defaultPrompt supports at most 3 entries")
    if any(not isinstance(prompt, str) or len(prompt) > 128 for prompt in default_prompts):
        fail("plugin.json interface.defaultPrompt entries must be strings up to 128 chars")

    for rel_path in REQUIRED_DOCS:
        path = ROOT / rel_path
        if not path.exists():
            fail(f"required documentation file is missing: {rel_path}")
        if not path.read_text(encoding="utf-8", errors="replace").strip():
            fail(f"required documentation file is empty: {rel_path}")

    source_manifest = load_json(SOURCES_JSON)
    source_entries = source_manifest.get("sources", [])
    imported = {entry["skill"] for entry in source_entries}
    if len(imported) != len(source_entries):
        fail("SKILL_SOURCES.json contains duplicate skill entries")
    for entry in source_entries:
        if not re.fullmatch(r"[0-9a-f]{40}", str(entry.get("commit", ""))):
            fail(f"SKILL_SOURCES.json has invalid commit for {entry.get('skill')}")
        if not isinstance(entry.get("stars"), int) or entry["stars"] < 0:
            fail(f"SKILL_SOURCES.json has invalid star count for {entry.get('skill')}")
        if not entry.get("source") or not entry.get("license"):
            fail(f"SKILL_SOURCES.json has incomplete provenance for {entry.get('skill')}")
    expected_imported = EXPECTED_SKILL_COUNT - 1  # plugin-check is local to this bundle.
    if len(imported) != expected_imported:
        fail(
            f"expected {expected_imported} imported skills in SKILL_SOURCES.json, "
            f"found {len(imported)}"
        )

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if len(skill_dirs) != EXPECTED_SKILL_COUNT:
        fail(f"expected {EXPECTED_SKILL_COUNT} skill dirs, found {len(skill_dirs)}")

    names: list[str] = []
    missing_license: list[str] = []
    catalog_chars = 0
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
        keys = frontmatter_keys(text)
        if keys != ALLOWED_FRONTMATTER_KEYS:
            fail(
                f"{skill_dir.name}/SKILL.md frontmatter keys must be "
                f"{sorted(ALLOWED_FRONTMATTER_KEYS)}, found {sorted(keys)}"
            )
        if name != skill_dir.name:
            fail(f"{skill_dir.name}/SKILL.md name must match its directory")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail(f"{skill_dir.name}/SKILL.md has invalid skill name: {name}")
        if not description.startswith(("Use when", "Use only when")):
            fail(f"{skill_dir.name}/SKILL.md description must start with a trigger")
        if len(description) > MAX_DESCRIPTION_CHARS:
            fail(
                f"{skill_dir.name}/SKILL.md description is {len(description)} chars; "
                f"maximum is {MAX_DESCRIPTION_CHARS}"
            )
        if len(text.splitlines()) > MAX_SKILL_LINES:
            fail(
                f"{skill_dir.name}/SKILL.md is {len(text.splitlines())} lines; "
                f"maximum is {MAX_SKILL_LINES}"
            )
        if any(pattern in text for pattern in ("subagent_type=", "read_url_content(")):
            fail(f"{skill_dir.name}/SKILL.md contains a non-portable tool assumption")
        for markdown_path in skill_dir.rglob("*.md"):
            markdown_text = markdown_path.read_text(encoding="utf-8", errors="replace")
            validate_relative_links(markdown_path, markdown_text)
        validate_skill_path_references(skill_md, text)
        names.append(name)
        catalog_chars += len(name) + len(description)
        if skill_dir.name != "plugin-check" and not (skill_dir / "LICENSE.txt").exists():
            missing_license.append(skill_dir.name)

    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        fail(f"duplicate skill names: {duplicates}")
    if missing_license:
        fail(f"imported skills missing LICENSE.txt: {missing_license}")

    expected_imported_names = {path.name for path in skill_dirs if path.name != "plugin-check"}
    if imported != expected_imported_names:
        missing = sorted(expected_imported_names - imported)
        extra = sorted(imported - expected_imported_names)
        fail(f"SKILL_SOURCES.json mismatch; missing={missing}, extra={extra}")
    if catalog_chars > MAX_CATALOG_CHARS:
        fail(
            f"skill name+description catalog is {catalog_chars} chars; "
            f"maximum is {MAX_CATALOG_CHARS}"
        )

    print(
        f"ok: {len(skill_dirs)} skills, {len(imported)} imported, "
        f"version {EXPECTED_VERSION}, catalog {catalog_chars} chars, "
        "docs present, no duplicate names"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
