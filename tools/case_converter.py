"""Case converter tool: convert text to uppercase, lowercase, or title case."""

AUTHOR = "Arian Nunez Alonso"
APP_NAME = "Case Converter"


def run():
    """Run the tool from the launcher."""
    text = input("Enter text to convert: ")

    if not text.strip():
        print("No text was entered. Nothing to convert.")
        return

    print("1. UPPERCASE")
    print("2. lowercase")
    print("3. Title Case")
    choice = input("Choose a conversion: ").strip()

    if choice == "1":
        print(text.upper())
    elif choice == "2":
        print(text.lower())
    elif choice == "3":
        print(text.title())
    else:
        print("Invalid selection.")