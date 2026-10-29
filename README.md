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

- Example Tool — starter example showing the required contract.

New tools should add one row to this section and explain how the tool was tested.

- Percentage calculator - A tool module made to calculate the percentage, percentage change, or part from whole. Testing each option using valid and invalid inputs to make sure the calculations were working and errors were handled. Example, select the Part from whole option enter 10 for part and 50 for whole and the result will be 20%.