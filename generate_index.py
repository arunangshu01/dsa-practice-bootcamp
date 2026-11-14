"""Generate a table of contents for the README by scanning the repo.

Walks the category directories, collects all .py solution files, and
injects a nested index between the INDEX_START and INDEX_END markers
in README.md. Run this after adding new code samples:

    python generate_index.py
"""

from pathlib import Path

REPO_ROOT = Path(__file__).parent
README = REPO_ROOT / "README.md"

# Top-level directories that contain code samples (in display order).
CATEGORIES = [
    "practice_codes",
    "common_questions_asked",
    "online_coding_portals",
]

START_MARKER = "<!-- INDEX_START -->"
END_MARKER = "<!-- INDEX_END -->"


def titleize(name: str) -> str:
    return name.replace("_", " ").title()


def build_index() -> str:
    lines = []
    for category in CATEGORIES:
        cat_path = REPO_ROOT / category
        if not cat_path.is_dir():
            continue
        lines.append(f"### {titleize(category)}\n")
        for topic_dir in sorted(p for p in cat_path.iterdir() if p.is_dir()):
            files = sorted(
                f for f in topic_dir.glob("*.py") if f.name != "__init__.py"
            )
            if not files:
                continue
            lines.append(f"#### {titleize(topic_dir.name)}")
            for f in files:
                rel = f.relative_to(REPO_ROOT).as_posix()
                label = f.stem.replace("_", " ").title()
                lines.append(f"- [{label}]({rel})")
            lines.append("")
    return "\n".join(lines).rstrip()


def main() -> None:
    readme = README.read_text()
    index = f"{START_MARKER}\n\n{build_index()}\n\n{END_MARKER}"
    if START_MARKER in readme and END_MARKER in readme:
        before = readme.split(START_MARKER)[0]
        after = readme.split(END_MARKER)[1]
        readme = before + index + after
    else:
        readme = readme.rstrip() + "\n\n## Index\n\n" + index + "\n"
    README.write_text(readme)
    print(f"Index updated in {README.name}")


if __name__ == "__main__":
    main()
