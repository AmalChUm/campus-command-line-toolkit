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
Choose `H. Help / Instructions` (or type `help`) from the menu for launcher instructions; the menu reappears afterward and this option is available even when no tools have been added.
The menu starts with an expected-input hint: enter `H` for help, a tool number to run it, or `0` to exit.

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

- Example Tool — starter example showing the required contract.

New tools should add one row to this section and explain how the tool was tested.
