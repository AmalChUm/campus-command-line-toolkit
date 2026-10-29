"""Shopping-list tool: add items, display the list, and mark items as purchased."""

AUTHOR = "Justin Mehl"  # TODO: replace with your real name before committing
APP_NAME = "Shopping List"


def add_item(items, name):
    """Add an item to the list. Return (ok, message)."""
    name = name.strip()
    if not name:
        return False, "Item name cannot be empty."
    for item in items:
        if item["name"].lower() == name.lower():
            return False, f"'{name}' is already on the list."
    items.append({"name": name, "purchased": False})
    return True, f"Added '{name}'."


def format_list(items):
    """Return the list as a printable string."""
    if not items:
        return "The shopping list is empty."
    lines = []
    for number, item in enumerate(items, start=1):
        mark = "x" if item["purchased"] else " "
        lines.append(f"{number}. [{mark}] {item['name']}")
    return "\n".join(lines)


def mark_purchased(items, choice):
    """Mark the item at the 1-based position `choice` as purchased."""
    if not items:
        return False, "The list is empty. Add an item first."
    try:
        index = int(choice.strip())
    except ValueError:
        return False, "Please enter the item number, for example: 2"
    if index < 1 or index > len(items):
        return False, f"Choose a number between 1 and {len(items)}."
    item = items[index - 1]
    if item["purchased"]:
        return False, f"'{item['name']}' is already marked as purchased."
    item["purchased"] = True
    return True, f"Marked '{item['name']}' as purchased."


def run():
    """Run the tool from the launcher."""
    items = []  # kept in memory only, so no personal data is written to disk
    print(f"\n=== {APP_NAME} ===")
    while True:
        print("\n1) Add item")
        print("2) Show list")
        print("3) Mark item as purchased")
        print("4) Back to main menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            _, message = add_item(items, input("Item to add: "))
            print(message)
        elif choice == "2":
            print(format_list(items))
        elif choice == "3":
            print(format_list(items))
            if items:
                _, message = mark_purchased(items, input("Item number: "))
                print(message)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Enter 1, 2, 3, or 4.")