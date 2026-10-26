
AUTHOR = "Matthew Sabadac"
APP_NAME = "Word Counter"


def run():
    print("\nWelcome to the Word Counter!")
    print("Enter your text below.")
    print("Press Enter on an empty line to finish.\n")

    lines = []

    while True:
        text = input("Text: ")

        if text == "":
            break

        lines.append(text)

    if not lines or not any(line.strip() for line in lines):
        print("No text was entered. Please try again.")
        return

    full_text = "\n".join(lines)

    word_count = len(full_text.split())
    character_count = len(full_text)
    line_count = len(lines)

    print("\nWord Counter Results:")
    print(f"Words: {word_count}")
    print(f"Characters: {character_count}")
    print(f"Lines: {line_count}")


if __name__ == "__main__":
    run()
