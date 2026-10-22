# Contributing to Campus Command-Line Toolkit

## Workflow

1. Choose one open GitHub issue. Do not begin an issue already claimed by another student.
2. Fork this repository to your GitHub account.
3. Clone your fork and open the repository root in VS Code.
4. Create a branch with this pattern:

   ```text
   feature/issue-<number>-<short-name>
   ```

5. Make a focused change related to the selected issue.
6. Inspect the diff before staging.
7. Stage only files that belong to the issue.
8. Commit with a meaningful message.
9. Publish the branch to your fork.
10. Open a pull request to `mkaouer/campus-command-line-toolkit`.
11. Link the issue with wording such as `Closes #12`.
12. Include testing evidence and disclose AI assistance when applicable.

## Requirements for tool contributions

- Put the module inside `tools/`.
- Define `AUTHOR`, `APP_NAME`, and `run()`.
- Keep the tool focused on the selected issue.
- Handle reasonable invalid input when the tool accepts input.
- Avoid passwords, tokens, or private information.
- Update the README tool list when adding a tool.
- Run `python main.py` and record the result.

## Pull-request checklist

- [ ] The base repository is `mkaouer/campus-command-line-toolkit`.
- [ ] The base branch is `main`.
- [ ] The PR links the correct issue.
- [ ] The changed files match the issue.
- [ ] The tool was tested through `python main.py` when applicable.
- [ ] The description explains what changed and what was tested.
- [ ] AI assistance is disclosed when used.
