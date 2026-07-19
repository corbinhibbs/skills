#!/usr/bin/env python3
"""Regenerate the skills table in README.md from .claude-plugin/plugin.json.

Runs on every upstream sync (see .github/workflows/sync-upstream.yml) so the
README always lists the skills the plugin currently ships. The table lives
between the SKILLS-TABLE markers; everything outside them is left untouched.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- SKILLS-TABLE:START -->"
END = "<!-- SKILLS-TABLE:END -->"


def frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.S)
    return m.group(1) if m else ""


def field(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip().strip("\"'") if m else ""


def main():
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    rows = []
    for raw in plugin.get("skills", []):
        rel = raw[2:] if raw.startswith("./") else raw
        name = Path(rel).name
        desc = ""
        md = ROOT / rel / "SKILL.md"
        if md.exists():
            fm = frontmatter(md.read_text())
            name = field(fm, "name") or name
            desc = field(fm, "description")
        parts = Path(rel).parts
        category = parts[1] if len(parts) > 2 else ""
        desc = desc.replace("|", "\\|")
        rows.append(f"| [`{name}`]({raw}/SKILL.md) | {category} | {desc} |")

    block = "\n".join(
        [
            START,
            "",
            f"_{len(rows)} skills, as listed in"
            " [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json)"
            " — this table regenerates automatically on every sync._",
            "",
            "| Skill | Category | What it does |",
            "|---|---|---|",
            *rows,
            "",
            END,
        ]
    )

    readme = ROOT / "README.md"
    text = readme.read_text()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(text):
        sys.exit("README.md is missing the SKILLS-TABLE markers")
    readme.write_text(pattern.sub(lambda _: block, text))
    print(f"Updated README skills table with {len(rows)} skills")


if __name__ == "__main__":
    main()
