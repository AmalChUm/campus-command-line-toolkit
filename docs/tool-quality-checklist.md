# Tool Quality Checklist

Use this checklist before opening a pull request.
Review CONTRIBUTING.md for the full contribution rules.

## Functional Behavior

- [ ] The tool meets the selected issue's requirements.
- [ ] The tool runs through `python main.py`.
- [ ] Normal input produces the expected result.
- [ ] Reasonable invalid or blank input is handled without crashing, when applicable.

## Structure

- [ ] The tool's Python module is inside `tools/`.
- [ ] The module defines `AUTHOR`, `APP_NAME`, and `run()`.
- [ ] Changes stay focused on the selected issue.
- [ ] Only files related to the issue are included.
- [ ] No passwords, tokens, or private information are included.

## Readability

- [ ] Variable and function names describe their purpose.
- [ ] The code is organized and easy to follow.
- [ ] Comments explain anything that may be confusing.
- [ ] Prompts, results, and error messages are clear.

## Documentation and Evidence

- [ ] The README tool list includes the new tool and describes its behavior.
- [ ] Examples use synthetic data without private information.
- [ ] Testing evidence records the command, input, and observed result.
- [ ] The pull request explains the changes and links the correct issue.
- [ ] The pull request discloses AI assistance when used.