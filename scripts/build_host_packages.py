"""Build coaster's committed Claude Code package, `hosts/claude`.

Source is host-neutral Markdown: skills name packaged files by relative path.
The installed plugin cannot read those paths without a permission grant, so
each rendered SKILL.md carries the full text of its files under `## Packaged:`
headings. `--check` rebuilds into a scratch folder and compares it with the
committed tree, naming each file that drifted.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGEN = "python3 scripts/build_host_packages.py"
SKIP = {"__pycache__", ".DS_Store"}

# file -> (heading title, fenced). Templates are fenced so their own code
# fences cannot break out; shared rules are pasted as text.
FILES = {
    "templates/dossier.md": ("dossier template", True),
    "templates/research-brief.md": ("research brief template", True),
    "templates/challenge-round.md": ("challenge round template", True),
    "templates/naming.md": ("naming template", True),
    "templates/handoff.md": ("handoff template", True),
    "skills/_shared/evidence.md": ("evidence rules", False),
    "skills/_shared/lenses.md": ("lenses", False),
    "skills/_shared/hats.md": ("hats", False),
}
# Which packaged files each skill carries.
SKILL_FILES = {
    "capture": ["templates/dossier.md", "skills/_shared/evidence.md"],
    "scout": ["templates/research-brief.md", "skills/_shared/evidence.md"],
    "frame": ["skills/_shared/lenses.md"],
    "challenge": ["skills/_shared/hats.md", "skills/_shared/evidence.md",
                  "templates/challenge-round.md"],
    "name": ["templates/naming.md"],
    "handoff": ["templates/handoff.md"],
}
HELPERS = {  # source form -> skill that owns the helper
    "`python3 scripts/link_check.py": "scout",
    "`python3 scripts/name_check.py": "name",
}
FORBIDDEN = ("`templates/", "`../_shared/", "`evidence.md`", "`scripts/",
             "python3 scripts/", "allowed-tools")
INTRO = ("Each `## Packaged:` section below runs to the next `## Packaged:` heading "
         "or the end of this file.")


def _skipped(rel: Path) -> bool:
    return any(part in SKIP or part.endswith(".pyc") for part in rel.parts)


def _ref(rel: str) -> str:
    """How source names a packaged file."""
    return f"`{rel}`" if rel.startswith("templates/") else f"`../_shared/{Path(rel).name}`"


def _section(rel: str, root: Path) -> str:
    title, fenced = FILES[rel]
    body = (root / rel).read_text(encoding="utf-8").rstrip("\n")
    if fenced:
        runs = [len(w) for w in body.split() if set(w) == {"`"}]
        fence = "`" * max(4, max(runs, default=0) + 1)
        body = f"{fence}markdown\n{body}\n{fence}"
    return f"## Packaged: {title}\n\n{body}\n"


def render_skill(skill: str, root: Path) -> str:
    text = (root / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
    for rel in SKILL_FILES[skill]:
        text = text.replace(_ref(rel), f"the `## Packaged: {FILES[rel][0]}` section")
    for old, owner in HELPERS.items():
        if owner == skill:
            if old not in text:
                raise SystemExit(f"ERROR: {skill}: helper reference not found: {old}")
            # jig's form: python3 "${CLAUDE_PLUGIN_ROOT}/skills/<skill>/scripts/<file>"
            new = old.replace("`python3 scripts/",
                              f'`python3 "${{CLAUDE_PLUGIN_ROOT}}/skills/{skill}/scripts/') + '"'
            text = text.replace(old, new)
    sections = "\n".join(_section(rel, root) for rel in SKILL_FILES[skill])
    text = text.rstrip("\n") + "\n\n" + INTRO + "\n\n" + sections
    for bad in FORBIDDEN:
        if bad in text:
            raise SystemExit(f"ERROR: {skill}: unmapped reference {bad}")
    return text


def build(root: Path, out: Path) -> None:
    """Render into a scratch folder, and replace `out` only on success."""
    found = {p.parent.name for p in (root / "skills").glob("*/SKILL.md")}
    if found != set(SKILL_FILES):
        raise SystemExit(f"ERROR: skills and map differ: {sorted(found ^ set(SKILL_FILES))}")
    tmp = Path(tempfile.mkdtemp(prefix="coaster-build-"))
    try:
        tmp.chmod(0o755)
        (tmp / ".claude-plugin").mkdir()
        shutil.copy(root / ".claude-plugin" / "plugin.json", tmp / ".claude-plugin")
        for name in ("README.md", "LICENSE"):
            if (root / name).is_file():
                shutil.copy(root / name, tmp / name)
        for skill in SKILL_FILES:
            src, dst = root / "skills" / skill, tmp / "skills" / skill
            dst.mkdir(parents=True)
            (dst / "SKILL.md").write_text(render_skill(skill, root), encoding="utf-8")
            for helper in sorted((src / "scripts").glob("*")):
                if not _skipped(helper.relative_to(root)):
                    (dst / "scripts").mkdir(exist_ok=True)
                    shutil.copy(helper, dst / "scripts" / helper.name)
        if out.exists():
            shutil.rmtree(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(tmp), str(out))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def _files(root: Path) -> dict[str, bytes]:
    if not root.is_dir():
        return {}
    return {p.relative_to(root).as_posix(): p.read_bytes() for p in sorted(root.rglob("*"))
            if p.is_file() and not _skipped(p.relative_to(root))}


def check(root: Path, out: Path) -> int:
    scratch = Path(tempfile.mkdtemp(prefix="coaster-drift-"))
    try:
        build(root, scratch / "claude")
        want, have = _files(scratch / "claude"), _files(out)
        drift = sorted(r for r in set(want) | set(have) if want.get(r) != have.get(r))
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    if not drift:
        print("OK: hosts/claude is in sync with source.")
        return 0
    print("ERROR: hosts/claude is stale relative to source.")
    for rel in drift:
        print(f"  - hosts/claude/{rel}")
    print(f"Regenerate and commit:\n    {REGEN}")
    return 1


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="build or check hosts/claude")
    parser.add_argument("--check", action="store_true",
                        help="rebuild in a scratch folder and diff against hosts/claude")
    ns = parser.parse_args(argv[1:])
    out = ROOT / "hosts" / "claude"
    if ns.check:
        return check(ROOT, out)
    build(ROOT, out)
    print(f"OK: built Claude package at {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
