"""Generate the docs site pages and the README index from the code samples.

Walks the category directories, turns every .py solution into a rendered
markdown page under docs/, writes a homepage with stats, and refreshes
the README index. Run after adding new samples (CI also runs this):

    python gen_docs.py

Docstring convention (all fields optional — first line is the title):

    \"\"\"Two Sum

    Difficulty: Easy
    Source: LeetCode
    Link: https://leetcode.com/problems/two-sum/

    Problem statement goes here...
    \"\"\"
"""

import ast
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).parent
DOCS_DIR = REPO_ROOT / "docs"
README = REPO_ROOT / "README.md"

CATEGORIES = [
    "practice_codes",
    "common_questions_asked",
    "online_coding_portals",
]

START_MARKER = "<!-- INDEX_START -->"
END_MARKER = "<!-- INDEX_END -->"
METADATA_KEYS = ("difficulty", "source", "link")


SPECIAL_CASES = {
    "leetcode": "LeetCode",
    "hackerrank": "HackerRank",
    "codesignal": "CodeSignal",
    "codeforces": "CodeForces",
    "avl": "AVL",
    "bst": "BST",
    "dfs": "DFS",
    "bfs": "BFS",
    "qno": "Q.No.",
    "fizzbuzz": "FizzBuzz",
    "ds": "DS",
    "ii": "II",
    "iii": "III",
    "iv": "IV",
}


def titleize(name: str) -> str:
    words = name.replace("_", " ").title().replace("'S", "'s").split()
    out = []
    for w in words:
        key = w.lower().rstrip("0123456789")
        suffix = w[len(key):] if w.lower().startswith(key) else ""
        out.append(SPECIAL_CASES.get(key, w) + suffix)
    return " ".join(out)


LEETCODE_PREFIX = re.compile(r"(?i)^leetcode question:?\s*(\d+)[\.:]?\s*(.*)$")


def clean_title(raw: str, fallback: str) -> str:
    """Normalize a docstring title into a consistent display title."""
    title = " ".join(raw.split()).rstrip(" -")
    m = LEETCODE_PREFIX.match(title)
    if m:
        return f"{m.group(1)}. {titleize(m.group(2))}"
    return titleize(title) if title else titleize(fallback)


def py_files():
    """Yield (category, topic_dir, file) for every solution file."""
    for category in CATEGORIES:
        cat_path = REPO_ROOT / category
        if not cat_path.is_dir():
            continue
        for topic_dir in sorted(p for p in cat_path.iterdir() if p.is_dir()):
            for f in sorted(topic_dir.glob("*.py")):
                if f.name != "__init__.py":
                    yield category, topic_dir, f


def parse_docstring(source: str) -> dict:
    """Extract title, metadata, and problem statement from a module docstring."""
    doc = ast.get_docstring(ast.parse(source))
    info = {"title": None, "statement": "", "meta": {}}
    if not doc:
        return info
    lines = doc.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    info["title"] = lines[0].strip() or None
    body = []
    for line in lines[1:]:
        stripped = line.strip()
        key = stripped.split(":", 1)
        if len(key) == 2 and key[0].strip().lower() in METADATA_KEYS:
            info["meta"][key[0].strip().lower()] = key[1].strip()
        else:
            body.append(line)
    info["statement"] = "\n".join(body).strip()
    return info


def write_page(category: str, topic_dir: Path, f: Path) -> Path:
    """Emit a markdown page for one solution file; returns the page path."""
    source = f.read_text(encoding="utf-8")
    info = parse_docstring(source)
    title = clean_title(info["title"], f.stem)

    out = [f"# {title}\n"]
    meta = info["meta"]
    if meta:
        badges = []
        if "difficulty" in meta:
            badges.append(f"**Difficulty:** {meta['difficulty']}")
        if "source" in meta:
            badges.append(f"**Source:** {meta['source']}")
        if "link" in meta:
            badges.append(f"[Problem link]({meta['link']}){{:target=\"_blank\"}}")
        out.append(" | ".join(badges) + "\n")
    if info["statement"]:
        out.append("!!! abstract \"Problem\"\n")
        out.extend(f"    {line}".rstrip() for line in info["statement"].splitlines())
        out.append("")
    out.append(f"## Solution\n\n```python\n{source.rstrip()}\n```\n")

    page_dir = DOCS_DIR / category / topic_dir.name
    page_dir.mkdir(parents=True, exist_ok=True)
    page = page_dir / f"{f.stem}.md"
    page.write_text("\n".join(out), encoding="utf-8")
    return page


def write_section_indexes() -> None:
    """Write index.md pages that list each section's contents."""
    for category in CATEGORIES:
        cat_docs = DOCS_DIR / category
        cat_src = REPO_ROOT / category
        if not cat_docs.is_dir():
            continue
        cat_lines = [f"# {titleize(category)}\n"]
        for topic_dir in sorted(p for p in cat_src.iterdir() if p.is_dir()):
            files = sorted(
                f for f in topic_dir.glob("*.py") if f.name != "__init__.py"
            )
            if not files:
                continue
            cat_lines.append(
                f"- **[{titleize(topic_dir.name)}]({topic_dir.name}/index.md)**"
                f" — {len(files)} solutions"
            )
            topic_lines = [f"# {titleize(topic_dir.name)}\n"]
            for f in files:
                info = parse_docstring(f.read_text(encoding="utf-8"))
                title = clean_title(info["title"], f.stem)
                diff = info["meta"].get("difficulty")
                suffix = f" — *{diff}*" if diff else ""
                topic_lines.append(f"- **[{title}]({f.stem}.md)**{suffix}")
            (cat_docs / topic_dir.name / "index.md").write_text(
                "\n".join(topic_lines) + "\n"
            )
        (cat_docs / "index.md").write_text("\n".join(cat_lines) + "\n")


def write_homepage(counts: dict) -> None:
    lines = [
        "# DSA Practice Bootcamp\n",
        "Data structures and algorithms implemented in Python, "
        "browsable by category and topic.\n",
        "## Contents\n",
    ]
    for category in CATEGORIES:
        n = counts.get(category, 0)
        if n:
            slug = category
            lines.append(f"- **[{titleize(category)}]({slug}/index.md)** — {n} solutions")
    lines.append("\n---\n\nBrowse via the sidebar or use the search bar above.\n")
    (DOCS_DIR / "index.md").write_text("\n".join(lines))


def update_readme_index() -> None:
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
                lines.append(f"- [{titleize(f.stem)}]({rel})")
            lines.append("")
    body = "\n".join(lines).rstrip()
    index = f"{START_MARKER}\n\n{body}\n\n{END_MARKER}"
    readme = README.read_text()
    if START_MARKER in readme and END_MARKER in readme:
        readme = readme.split(START_MARKER)[0] + index + readme.split(END_MARKER)[1]
        README.write_text(readme)


def main() -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    counts = {}
    for category, topic_dir, f in py_files():
        write_page(category, topic_dir, f)
        counts[category] = counts.get(category, 0) + 1
    write_section_indexes()
    write_homepage(counts)
    update_readme_index()
    print(f"Generated docs for {sum(counts.values())} files")


if __name__ == "__main__":
    main()
