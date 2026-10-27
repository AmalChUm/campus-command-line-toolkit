import re

AUTHOR = "Ibrahim Atatri"
APP_NAME = "Duplicate Word Detector"


def run():
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Please enter a sentence.")
        return

    words = re.findall(r"\b\w+\b", sentence.lower())

    seen = set()
    duplicates = []

    for word in words:
        if word in seen and word not in duplicates:
            duplicates.append(word)
        seen.add(word)

    if duplicates:
        print("Repeated words:", ", ".join(duplicates))
    else:
        print("No repeated words found.")