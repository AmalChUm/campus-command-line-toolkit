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
|   └── tip_calculator.py
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
- Tip Calculator - Shows 10%, 15%, and 20% tips for a valid bill amount. Asks for a new input on invalid values (v<0, Non-Number)
    - Sample Input: 10.00
        Sample Output: 
            Bill: $10.00
            Tip %            Tip         Total
            10             $1.00        $11.00
            15             $1.50        $11.50
            20             $2.00        $12.00
    - Validation:
        Enter the bill amount (or press Enter to exit): 0
        Invalid input: amount must be greater than 0.
        Enter the bill amount (or press Enter to exit): -1500000
        Invalid input: amount must be greater than 0.
        Enter the bill amount (or press Enter to exit): ten
        Invalid input: please enter a numeric value.
        Enter the bill amount (or press Enter to exit): 12.560

        Bill: $12.56
        Tip %            Tip         Total
        10             $1.26        $13.82
        15             $1.88        $14.44
        20             $2.51        $15.07
        Enter the bill amount (or press Enter to exit): 
        Goodbye!
New tools should add one row to this section and explain how the tool was tested.
