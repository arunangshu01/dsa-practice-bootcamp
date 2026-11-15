# Contributing

Adding a new solution is simple - this site regenerates itself on every push to `master`.

## Steps

1. Drop a `.py` file into the right folder:

    | Folder | Use for |
    | --- | --- |
    | `practice_codes/<topic>/` | Data structure implementations (stacks, trees, queues...) |
    | `common_questions_asked/<topic>/` | Common interview questions |
    | `online_coding_portals/<portal>/` | LeetCode, HackerRank, etc. |

2. Start the file with a docstring header:

    ```python
    """Two Sum

    Difficulty: Easy
    Source: LeetCode
    Link: https://leetcode.com/problems/two-sum/

    Given an array of integers, return indices of the two numbers
    that add up to the target.
    """
    ```

    - **First line** = the page title
    - `Difficulty:`, `Source:`, `Link:` = rendered as badges (all optional)
    - Everything else = shown in the "Problem" panel

3. Commit and push to `master`. The site rebuilds and your page appears in the sidebar, its topic index, the Tags page, and search - no other steps needed.

## Conventions

- Filenames: `snake_case.py` - they become page URLs.
- Include a `if __name__ == "__main__":` block that prints example output - it gets executed at build time and shown in the Output panel.
- `__init__.py` files are ignored.
