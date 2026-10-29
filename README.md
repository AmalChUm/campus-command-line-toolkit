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
- Weekly Study Schedule Formatter (`tools/study_schedule.py`) - Organizes course names and study blocks into Monday-Sunday order. Run `python main.py` and select the tool. Example: enter `Math`, `Monday`, and `3 PM - 4 PM`, then leave the next course name blank to display the schedule. Leave the first course name blank to exit without adding blocks.

Verification: Ran `py main.py` on Windows and selected the Weekly Study Schedule Formatter. Math on Monday from 3 PM - 4 PM displayed correctly. A blank first course displayed "No study blocks entered." An invalid day (Funday) and an empty study block were rejected; corrected input displayed English on Tuesday from 5 PM - 6 PM.

New tools should add one row to this section and explain how the tool was tested.
