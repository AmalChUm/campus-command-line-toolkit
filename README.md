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
│   ├── example_tool.py
│   └── input_helpers.py
├── tests/
│   ├── test_smoke.py
│   └── test_input_helpers.py
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

- **Input Validation Example** by Andrew Haralambous:
  Demonstrates reusable helpers for nonblank text and integer input.
  Run `python main.py` and select **Input Validation Example**.

## Input-validation helpers

`tools/input_helpers.py` provides:

- `read_nonempty_text(prompt)`: Rejects empty or whitespace-only input.
  Returns text with leading and trailing whitespace removed.
- `read_integer(prompt)`: Rejects blank input, words, and decimal values.
  Returns an integer; positive numbers, negative numbers, and zero are accepted.

Both helpers display an error and repeat the prompt after invalid input.
The example tool in `tools/example_tool.py` demonstrates both helpers.

## Verification

Run from the repository root:

```text
python -m unittest discover -s tests -p test_input_helpers.py -v
```

Observed result: All 8 tests passed (`OK`).

Tests cover valid text, whitespace trimming, blank and whitespace-only
input, positive and negative integers, zero, nonnumeric input, decimal
input, and the complete launcher interaction.
