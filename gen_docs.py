"""Generate the docs site pages and the README index from the code samples.

Walks the category directories, turns every .py solution into a rendered
markdown page under docs/, writes a homepage with stats, and refreshes
the README index. Run after adding new samples (CI also runs this):

    python gen_docs.py

Docstring convention (all fields optional - first line is the title):

    \"\"\"Two Sum

    Difficulty: Easy
    Source: LeetCode
    Link: https://leetcode.com/problems/two-sum/

    Problem statement goes here...
    \"\"\"
"""

import ast
import functools
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent
DOCS_DIR = REPO_ROOT / "docs"
README = REPO_ROOT / "README.md"

CATEGORIES = [
    "practice_codes",
    "common_questions_asked",
    "online_coding_portals",
]

SITE_URL = "https://arunangshu01.github.io/dsa-practice-bootcamp"

START_MARKER = "<!-- INDEX_START -->"
END_MARKER = "<!-- INDEX_END -->"

MKDOCS_YML = REPO_ROOT / "mkdocs.yml"
NAV_START = "## NAV_START"
NAV_END = "## NAV_END"
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
        if w.lower() == "and":
            out.append("&")
            continue
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


EXEC_TIMEOUT = 5  # seconds per file
MAX_OUTPUT = 3000


@functools.lru_cache(maxsize=1)
def last_commit_date_map() -> dict:
    """Map repo-relative file paths to their last commit dates (one git call)."""
    out = subprocess.run(
        ["git", "log", "--format=__C__%cs", "--name-only", "--diff-filter=MAR"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=30,
    )
    dates = {}
    current = ""
    for line in out.stdout.splitlines():
        if line.startswith("__C__"):
            current = line[5:]
        elif line.endswith(".py") and line not in dates:
            dates[line] = current
    return dates


def execute_solution(f: Path) -> str:
    """Run a solution file and capture its stdout/stderr (None if skipped)."""
    if os.environ.get("GEN_NO_EXEC"):
        return ""
    try:
        result = subprocess.run(
            [sys.executable, f.name],
            cwd=f.parent,
            capture_output=True,
            text=True,
            timeout=EXEC_TIMEOUT,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )
    except subprocess.TimeoutExpired:
        return "(execution timed out)"
    output = (result.stdout + result.stderr).strip()
    if not output:
        return ""  # nothing worth showing (e.g. class-only solutions)
    if len(output) > MAX_OUTPUT:
        output = output[:MAX_OUTPUT] + "\n... (truncated)"
    return output


def write_page(category: str, topic_dir: Path, f: Path) -> Path:
    """Emit a markdown page for one solution file; returns the page path."""
    source = f.read_text(encoding="utf-8")
    info = parse_docstring(source)
    title = clean_title(info["title"], f.stem)

    out = [f"# {title}\n"]
    rev = last_commit_date_map().get(f.relative_to(REPO_ROOT).as_posix())
    if rev:
        out.append(f'<span class="last-updated">Last updated: {rev}</span>\n')
    meta = info["meta"]
    if meta:
        badges = []
        if "difficulty" in meta:
            cls = f"badge-{meta['difficulty'].lower()}"
            badges.append(
                f'<span class="badge {cls}">{meta["difficulty"]}</span>'
            )
        if "source" in meta:
            badges.append(f'<span class="badge badge-src">{meta["source"]}</span>')
        if "link" in meta:
            badges.append(
                f"[Problem link]({meta['link']}){{:target=\"_blank\"}}"
            )
        out.append(" ".join(badges) + "\n")
    if info["statement"]:
        out.append("!!! abstract \"Problem\"\n")
        out.extend(f"    {line}".rstrip() for line in info["statement"].splitlines())
        out.append("")
    out.append(f"## Solution\n\n```python\n{source.rstrip()}\n```\n")
    run_output = execute_solution(f)
    if run_output:
        out.append('??? terminal "Output"\n')
        out.append("    ```text")
        out.extend(f"    {line}" for line in run_output.splitlines())
        out.append("    ```\n")
    rel_src = f.relative_to(REPO_ROOT).as_posix()
    out.append(
        "---\n\n[:material-pencil: Edit this solution on GitHub]"
        f"(https://github.com/arunangshu01/dsa-practice-bootcamp/blob/master/{rel_src})"
        '{:target="_blank"}\n'
    )

    page_dir = DOCS_DIR / category / topic_dir.name
    page_dir.mkdir(parents=True, exist_ok=True)
    page = page_dir / f"{f.stem}.md"
    page.write_text("\n".join(out), encoding="utf-8")
    return {
        "category": category,
        "topic": topic_dir.name,
        "stem": f.stem,
        "title": title,
        "meta": info["meta"],
        "page": page.relative_to(DOCS_DIR).as_posix(),
    }


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
                f" - {len(files)} solutions"
            )
            topic_lines = [f"# {titleize(topic_dir.name)}\n"]
            for f in files:
                info = parse_docstring(f.read_text(encoding="utf-8"))
                title = clean_title(info["title"], f.stem)
                diff = info["meta"].get("difficulty")
                suffix = f" - *{diff}*" if diff else ""
                topic_lines.append(f"- **[{title}]({f.stem}.md)**{suffix}")
            (cat_docs / topic_dir.name / "index.md").write_text(
                "\n".join(topic_lines) + "\n"
            )
        (cat_docs / "index.md").write_text("\n".join(cat_lines) + "\n")


def build_nav() -> list:
    """Build the mkdocs nav tree so sidebar labels use our titles."""
    nav = [{"Home": "index.md"}, {"Tags": "tags.md"}]
    for category in CATEGORIES:
        cat_docs = DOCS_DIR / category
        if not cat_docs.is_dir():
            continue
        section = [{"Overview": f"{category}/index.md"}]
        for topic_dir in sorted(p for p in cat_docs.iterdir() if p.is_dir()):
            pages = []
            for page in sorted(topic_dir.glob("*.md")):
                rel = page.relative_to(DOCS_DIR).as_posix()
                if page.stem == "index":
                    pages.insert(0, {"Overview": rel})
                    continue
                info = parse_docstring(
                    (REPO_ROOT / category / topic_dir.name / f"{page.stem}.py")
                    .read_text(encoding="utf-8")
                )
                pages.append({clean_title(info["title"], page.stem): rel})
            section.append({titleize(topic_dir.name): pages})
        nav.append({titleize(category): section})
    nav.append({"Contributing": "contributing.md"})
    return nav


def _nav_yaml(items: list, indent: int) -> list:
    lines = []
    pad = " " * indent
    for item in items:
        for title, value in item.items():
            if isinstance(value, str):
                lines.append(f'{pad}- "{title}": {value}')
            else:
                lines.append(f"{pad}- {title}:")
                lines.extend(_nav_yaml(value, indent + 4))
    return lines


def update_mkdocs_nav() -> None:
    nav_yaml = "\n".join(_nav_yaml(build_nav(), 2))
    block = f"{NAV_START}\nnav:\n{nav_yaml}\n{NAV_END}"
    yml = MKDOCS_YML.read_text()
    if NAV_START in yml and NAV_END in yml:
        yml = yml.split(NAV_START)[0] + block + yml.split(NAV_END)[1]
    else:
        yml = yml.rstrip() + "\n\n" + block + "\n"
    MKDOCS_YML.write_text(yml)


def write_homepage(entries: list) -> None:
    counts = {}
    diff_counts = {}
    for e in entries:
        counts[e["category"]] = counts.get(e["category"], 0) + 1
        d = e["meta"].get("difficulty")
        if d:
            diff_counts[d] = diff_counts.get(d, 0) + 1
    lines = [
        "# DSA Practice Bootcamp\n",
        "Data structures and algorithms implemented in Python - "
        "browsable by category, topic, and difficulty.\n",
        "## Stats\n",
        "| Metric | Count |",
        "| --- | ---: |",
        f"| Total solutions | {len(entries)} |",
    ]
    for category in CATEGORIES:
        if counts.get(category):
            lines.append(
                f"| {titleize(category)} | {counts[category]} |"
            )
    for diff in ("Easy", "Medium", "Hard"):
        if diff_counts.get(diff):
            lines.append(f"| {diff} problems | {diff_counts[diff]} |")
    lines.append("\n## Contents\n")
    for category in CATEGORIES:
        n = counts.get(category, 0)
        if n:
            lines.append(
                f"- **[{titleize(category)}]({category}/index.md)**"
                f" - {n} solutions"
            )
    lines.append("\n---\n\nBrowse via the sidebar, the "
                 "[Tags](tags.md) page, or the search bar above.\n")
    lines.append("\n---\n\n*Arunangshu Pramanik*\n")
    (DOCS_DIR / "index.md").write_text("\n".join(lines))


def write_tags_page(entries: list) -> None:
    """Generate a tags.md grouping solutions by difficulty and topic."""
    by_diff = {}
    by_topic = {}
    for e in entries:
        link = f"- [{e['title']}]({e['page']})"
        d = e["meta"].get("difficulty")
        if d:
            by_diff.setdefault(d, []).append(link)
        topic = f"{titleize(e['topic'])} ({titleize(e['category'])})"
        by_topic.setdefault(topic, []).append(link)

    lines = ["# Tags\n", "## By Difficulty\n"]
    for diff in ("Easy", "Medium", "Hard"):
        if by_diff.get(diff):
            lines.append(f"### {diff}\n")
            lines.extend(sorted(by_diff[diff]))
            lines.append("")
    lines.append("\n## By Topic\n")
    for topic in sorted(by_topic):
        lines.append(f"### {topic}\n")
        lines.extend(sorted(by_topic[topic]))
        lines.append("")
    (DOCS_DIR / "tags.md").write_text("\n".join(lines))


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
                site_page = (
                    f"{SITE_URL}/{category}/{topic_dir.name}/{f.stem}/"
                )
                lines.append(f"- [{titleize(f.stem)}]({site_page})")
            lines.append("")
    body = "\n".join(lines).rstrip()
    index = f"{START_MARKER}\n\n{body}\n\n{END_MARKER}"
    readme = README.read_text()
    if START_MARKER in readme and END_MARKER in readme:
        readme = readme.split(START_MARKER)[0] + index + readme.split(END_MARKER)[1]
        README.write_text(readme)


def copy_static_assets() -> None:
    """Copy hand-maintained assets (CSS, images) into the generated docs."""
    assets = REPO_ROOT / "docs_assets"
    if assets.is_dir():
        shutil.copytree(assets, DOCS_DIR, dirs_exist_ok=True)


def main() -> None:
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    copy_static_assets()
    entries = []
    for category, topic_dir, f in py_files():
        entries.append(write_page(category, topic_dir, f))
    write_section_indexes()
    write_homepage(entries)
    write_tags_page(entries)
    update_mkdocs_nav()
    update_readme_index()
    print(f"Generated docs for {len(entries)} files")


if __name__ == "__main__":
    main()
