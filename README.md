# Campus Command-Line Toolkit

A small Python toolkit for useful campus and study utilities. This repository is used in SWE 325 to practice GitHub, VS Code, branching, staging, commits, publishing branches, pull requests, and review.

## Repository structure

```text
campus-command-line-toolkit/
├── main.py
├── README.md
├── CONTRIBUTING.md
├── requirements.txt
├── tools/
│   ├── __init__.py
│   └── example_tool.py
├── tests/
│   └── test_smoke.py
└── docs/
    └── contribution-evidence.md
```

## Run the toolkit

```bash
python main.py
```

Select a tool from the menu. The launcher discovers Python modules in `tools/` that expose the required plugin contract.

## Tool contract

A contributed tool should normally be a single module inside `tools/` and define:

```python
AUTHOR = "Your Name"
APP_NAME = "A clear tool name"


def run():
    """Run the tool from the launcher."""
    print("Tool output")
```

Use a feature branch, make a focused change, test it, and open a pull request. Read [CONTRIBUTING.md](CONTRIBUTING.md) before starting.

## Tools

| Tool | Module | Author | Description |
| --- | --- | --- | --- |
| Example Tool | `tools/example_tool.py` | SWE 325 Starter Team | Starter example showing the required contract. |
| _Your tool name_ | `tools/<your_module>.py` | _Your name_ | _One-sentence description of what the tool does._ |

### Adding your tool to this table

1. Add **one new row** for your tool directly below the last real entry, above the `_Your tool name_` template row.
2. Fill in the four columns: **Tool** (your tool's `APP_NAME`), **Module** (path inside `tools/`), **Author** (your tool's `AUTHOR`), and **Description** (one sentence).
3. Keep each row on a single line and use the same `|` format as the rows above.
4. Do not edit or reorder other contributors' rows.
5. In your pull request, record how you tested the tool (for example, `python main.py` and the input you used).

### If two pull requests add rows at the same place

Adding rows in the same spot of this table is expected to cause a merge conflict. When resolving it, keep **both** contributors' rows, place them one after another, delete every conflict marker (`<<<<<<<`, `=======`, `>>>>>>>`), and preview the README to confirm the table still renders.