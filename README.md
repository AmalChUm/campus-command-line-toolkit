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
│   └── random_study_tip.py
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

- **Example Tool** — Starter example showing the required contract.
- **Word Counter** — Created by Matthew Sabadac. Counts the number of words, characters, and lines in user-entered text.
- **Random Study-Tip Tool** — Created by Matthew Sabadac. Randomly selects and displays one of 10 helpful study tips.

### Random Study-Tip Tool Testing

The Random Study-Tip Tool was tested using the following steps:

1. Ran `py tools/random_study_tip.py` and confirmed that a random study tip was displayed.
2. Ran `py main.py` and verified that the Random Study-Tip Tool appeared in the main menu.
3. Selected option 2 and confirmed that the tool displayed a study tip successfully.
4. Verified that the program ran without errors.

Example output:

    Random Study Tip:
    Practice explaining what you learned in your own words.
