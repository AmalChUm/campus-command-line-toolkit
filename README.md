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

## Current tools

The table lists tools currently included in this repository. Start the launcher
from the repository root and select the tool by its displayed menu name.

| Tool | Author | Purpose | Example command and selection |
| --- | --- | --- | --- |
| [Example Tool](tools/example_tool.py) | SWE 325 Starter Team | Demonstrates the required `AUTHOR`, `APP_NAME`, and `run()` interface and prints a starter message. | Run `python main.py`, then select `Example Tool` from the menu. |

### Example Tool output

Selecting Example Tool prints:

```text
This is the starter tool. Choose an issue and add your own tool!
```

### Updating the catalog

When adding a tool:

- Add one row using the tool's `APP_NAME` and `AUTHOR` values.
- Link the tool name to its Python module inside `tools/`.
- Describe its purpose and how to launch it.
- Refer to the displayed tool name rather than a fixed menu number, because
  the launcher sorts tools by application name.
- Include the verification command, input, and observed result in the pull
  request.
- List tools included in the repository, not proposed tools from unmerged
  pull requests.