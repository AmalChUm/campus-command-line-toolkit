
import random

AUTHOR = "Matthew Sabadac"
APP_NAME = "Random Study-Tip Tool"


def run():
    study_tips = [
        "Take short breaks while studying to stay focused.",
        "Review your notes every day to remember information better.",
        "Study in a quiet place without distractions.",
        "Break large assignments into smaller tasks.",
        "Use flashcards to help memorize important information.",
        "Get enough sleep before an exam.",
        "Practice explaining what you learned in your own words.",
        "Create a study schedule and stick to it.",
        "Test yourself instead of just rereading your notes.",
        "Start studying early instead of waiting until the last minute."
    ]

    print("\nRandom Study Tip:")
    print(random.choice(study_tips))


if __name__ == "__main__":
    run()
