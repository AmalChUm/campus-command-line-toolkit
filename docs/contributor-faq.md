# Contributor FAQ

This FAQ explains the basic Git and GitHub workflow for contributing to the Campus Command-Line Toolkit.

## 1. What is a fork?
A fork is a personal copy of a GitHub repository. It allows contributors to make changes without directly modifying the original project.

## 2. What is a branch?
A branch is a separate line of development where you can work on changes without affecting the main branch.

## 3. What does staging mean?
Staging means selecting the changes you want to include in your next commit.

Example:
git add docs/contributor-faq.md

## 4. What is a commit?
A commit saves a snapshot of your staged changes in your local Git history.

Example:
git commit -m "Add contributor FAQ"

## 5. What does publishing a branch mean?
Publishing uploads your local branch to a remote repository on GitHub.

Example:
git push -u origin feature/issue-25-contributor-faq

## 6. What is a pull request?
A pull request proposes changes from your branch to another branch or repository. It allows others to review and discuss your changes before merging them.

## Basic Contribution Workflow

1. Fork the original repository.
2. Clone your fork.
3. Create a feature branch.
4. Make and test your changes.
5. Review and stage the intended files.
6. Commit your changes.
7. Push your branch to your fork.
8. Open a pull request to the original repository.
