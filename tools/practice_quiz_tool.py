
import random

AUTHOR = "Moesha Woods"
APP_NAME = "Quiz Tool"






# Group 1: Questions about Git branching
BRANCHING_QUESTIONS = [
    {
        "question": "What is a branch in Git?",
        "options": [
            "A separate line of development",
            "A type of computer",
            "A file backup",
            "A programming language",
        ],
        "answer": "A separate line of development",
        "comment": "Correct! A branch lets you develop changes independently.",
        "wrong_comment": "A branch is a separate line of development, not a computer or programming language.",
    },
    {
        "question": "Which command creates and switches to a new branch?",
        "options": [
            "git merge",
            "git switch -c feature/login",
            "git push",
            "git status",
        ],
        "answer": "git switch -c feature/login",
        "comment": "Correct! The -c option creates a new branch and switches to it.",
        "wrong_comment": "Use git switch -c followed by a branch name to create and switch to a branch.",
    },
    {
        "question": "Which command shows your current branch?",
        "options": [
            "git merge",
            "git push",
            "git branch --show-current",
            "git commit",
        ],
        "answer": "git branch --show-current",
        "comment": "Correct! This command displays the name of your current branch.",
        "wrong_comment": "git branch --show-current prints the name of the active branch.",
    },
    {
        "question": "Why use a feature branch for a campus project?",
        "options": [
            "To avoid writing tests",
            "To delete main",
            "To skip code reviews",
            "To develop a feature separately from main",
        ],
        "answer": "To develop a feature separately from main",
        "comment": "Correct! A feature branch keeps your work separate from main.",
        "wrong_comment": "Feature branches let you develop changes without directly changing main.",
    },
    {
        "question": "What does git switch main do?",
        "options": [
            "Switches to the main branch",
            "Creates a new repository",
            "Uploads all files",
            "Deletes the current branch",
        ],
        "answer": "Switches to the main branch",
        "comment": "Correct! The command switches your active branch to main.",
        "wrong_comment": "git switch main changes your active branch. It does not upload or delete files.",
    },
    {
        "question": "What does git branch show by default?",
        "options": [
            "All GitHub users",
            "Files in the project",
            "Local branches",
            "All remote repositories",
        ],
        "answer": "Local branches",
        "comment": "Correct! git branch lists your local branches by default.",
        "wrong_comment": "The git branch command lists local branches by default.",
    },
]


# Group 2: Questions about Git merging
MERGING_QUESTIONS = [
    {
        "question": "What does git merge do?",
        "options": [
            "Deletes all branches",
            "Combines changes from another branch",
            "Creates a new repository",
            "Installs Git",
        ],
        "answer": "Combines changes from another branch",
        "comment": "Correct! Merging integrates changes from another branch into your current branch.",
        "wrong_comment": "Git merge integrates branch changes. It does not automatically delete branches or create repositories.",
    },
    {
        "question": "What is a merge conflict?",
        "options": [
            "A deleted repository",
            "A successful commit",
            "A situation where Git cannot automatically reconcile changes",
            "A GitHub login error",
        ],
        "answer": "A situation where Git cannot automatically reconcile changes",
        "comment": "Correct! Git needs help deciding how to combine conflicting changes.",
        "wrong_comment": "A merge conflict occurs when Git cannot automatically reconcile certain changes.",
    },
    {
        "question": "Two students edit the same line differently. What might happen during a merge?",
        "options": [
            "Git may report a merge conflict",
            "Git deletes the repository",
            "Both branches disappear",
            "Git automatically opens VS Code",
        ],
        "answer": "Git may report a merge conflict",
        "comment": "Correct! Git may require you to resolve the conflicting edits manually.",
        "wrong_comment": "When overlapping changes cannot be combined automatically, Git may report a merge conflict.",
    },
    {
        "question": "What should you do when resolving a merge conflict?",
        "options": [
            "Delete the entire project",
            "Accept both changes without checking",
            "Delete main",
            "Review the changes and choose an intentional result",
        ],
        "answer": "Review the changes and choose an intentional result",
        "comment": "Correct! Review both versions and create a final result that makes sense.",
        "wrong_comment": "Inspect the conflicting changes and decide what the final file should contain.",
    },
    {
        "question": "Which command stages a file after resolving its conflict?",
        "options": [
            "git merge",
            "git switch",
            "git add docs/conflict-practice.md",
            "git branch",
        ],
        "answer": "git add docs/conflict-practice.md",
        "comment": "Correct! git add stages the resolved file for the merge commit.",
        "wrong_comment": "Use git add with the resolved file's path to stage the resolution.",
    },
    {
        "question": "What should you check after resolving a merge conflict?",
        "options": [
            "That all branches are deleted",
            "That Git is reinstalled",
            "That every file is staged",
            "That conflict markers are gone and the final file is correct",
        ],
        "answer": "That conflict markers are gone and the final file is correct",
        "comment": "Correct! Check the final file and make sure no conflict markers remain.",
        "wrong_comment": "Review the final file, remove conflict markers, and verify that the result is correct.",
    },
]


def display_question(question):
    """Display a question with randomly ordered options."""

    # Copy the options so the original question data stays unchanged.
    options = question["options"].copy()

    # Shuffle the answer choices to make each quiz less predictable.
    random.shuffle(options)

    print(f"\n{question['question']}")

    # Display each option with a letter from A to D.
    for index, option in enumerate(options):
        letter = ["A", "B", "C", "D"][index]
        print(f"{letter}. {option}")

    # Return the shuffled options so we can check the selected answer.
    return options


def check_answer(question, options):
    """Get the player's answer, grade it, and display feedback."""

    # Match each answer letter to its position in the options list.
    # Python list indexes start at 0: A = 0, B = 1, C = 2, D = 3.
    answer_indexes = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
    }

    # Keep asking until the player enters a valid answer or quits.
    while True:
        user_answer = input(
            "Your answer (A-D, or Q to quit): "
        ).strip().upper()

        # Let the player exit the quiz at any question.
        if user_answer == "Q":
            print("\nThanks for playing!")
            return None

        # Accept only A, B, C, or D as answers.
        if user_answer in answer_indexes:
            break

        print("Invalid choice. Enter A, B, C, D, or Q.")

    # Find the selected option using its letter-to-index mapping.
    # For example, "B" maps to index 1, so we select options[1].
    selected_answer = options[answer_indexes[user_answer]]

    # Compare the player's selected option with the correct answer.
    if selected_answer == question["answer"]:
        print("Correct!")
        print(question["comment"])
        return 1

    # If the answer is incorrect, explain the correct concept.
    print("Incorrect!")
    print(f"Correct answer: {question['answer']}")
    print(question["wrong_comment"])

    return 0


def take_quiz(questions, amount=5):
    """Run a random selection of questions and return the score."""

    # Randomly select questions without repeating any in this quiz.
    selected_questions = random.sample(questions, amount)

    score = 0

    print(f"\n===== {APP_NAME} =====")
    print(f"You will answer {amount} random questions.")
    print("Type Q at any time to quit.")

    # Display and grade each selected question.
    for number, question in enumerate(selected_questions, start=1):
        print(f"\nQuestion {number} of {amount}")

        options = display_question(question)
        result = check_answer(question, options)

        # Stop immediately if the player chooses to quit.
        if result is None:
            return None

        # Add the points earned for this question.
        score += result

    # Show the score after all questions are completed.
    print(f"\nFinal score: {score}/{amount}")
    print(f"Percentage: {score / amount * 100:.0f}%")

    return score


def run():
    """Combine both question categories and start the quiz."""

    # Combine branching and merging into one question bank.
    all_questions = BRANCHING_QUESTIONS + MERGING_QUESTIONS

    # Ensure enough questions exist before selecting five.
    if len(all_questions) < 5:
        print("Not enough questions available to start the quiz.")
        return

    # Start the quiz with five randomly selected questions.
    score = take_quiz(all_questions, 5)

    # Do not display a final result if the player quit early.
    if score is None:
        return

    # Display a message based on the final score.
    if score == 5:
        print("Excellent! You're a Git Branching Boss!")
    elif score >= 3:
        print("Good job! Keep practicing your Git skills.")
    else:
        print("Keep learning! Practice makes progress.")


# No direct-launch block is necessary for the toolkit launcher.
# main.py discovers this module and calls run() when selected.
