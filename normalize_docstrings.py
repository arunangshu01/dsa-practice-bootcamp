"""One-off migration: normalize module docstrings across all solution files.

Ensures every .py solution has a docstring whose first non-empty line is a
title, followed by a `Source:` metadata line (inferred from the folder) so
gen_docs.py renders a consistent header on every page. Existing problem
statements are preserved. Idempotent — files already normalized are skipped.
"""

import ast
from pathlib import Path

REPO_ROOT = Path(__file__).parent

CATEGORIES = {
    "practice_codes": "Practice",
    "common_questions_asked": "Common Interview Question",
    "online_coding_portals/leetcode": "LeetCode",
}


def titleize(name: str) -> str:
    return name.replace("_", " ").title().replace("'S", "'s")


def source_for(path: Path) -> str:
    rel = path.relative_to(REPO_ROOT).as_posix()
    for prefix, source in CATEGORIES.items():
        if rel.startswith(prefix + "/"):
            return source
    return "Practice"


def normalize(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text)
    except SyntaxError:
        print(f"  ! skipped (syntax error): {path.name}")
        return False

    doc = ast.get_docstring(tree)
    source = source_for(path)
    title = None
    body_lines = []
    has_source = False

    if doc:
        lines = doc.splitlines()
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines:
            title = lines[0].strip()
            body_lines = lines[1:]
            has_source = any(
                l.strip().lower().startswith("source:") for l in body_lines
            )

    if title is None:
        title = titleize(path.stem)
    if has_source:
        return False  # already normalized

    new_doc_lines = ["", title, "", f"Source: {source}"]
    # keep the rest of the original docstring body
    new_doc_lines.extend(body_lines)
    new_doc = '"""' + "\n".join(new_doc_lines).rstrip() + '\n"""'

    if doc is None:
        # insert docstring at top of file
        new_text = new_doc + "\n\n" + text
    else:
        # replace the existing docstring node
        node = tree.body[0]
        start, end = node.lineno - 1, node.end_lineno
        src_lines = text.splitlines(keepends=True)
        new_text = "".join(src_lines[:start]) + new_doc + "\n" + "".join(
            src_lines[end:]
        )

    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> None:
    changed = 0
    for category in CATEGORIES:
        cat_path = REPO_ROOT / category
        if not cat_path.is_dir():
            continue
        for f in sorted(cat_path.rglob("*.py")):
            if f.name == "__init__.py":
                continue
            if normalize(f):
                changed += 1
    print(f"Normalized {changed} files")


if __name__ == "__main__":
    main()
