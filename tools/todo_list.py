AUTHOR = "Braeden Burger"
APP_NAME = "To-Do List"

HELP_TEXT = """Commands:
  add <task>     Add a task
  list           Show all tasks
  remove <n>     Remove task number n
  help           Show this help
  quit           Exit the tool"""

def add_task(tasks, text):
    text = text.strip()
    if not text:
        return "Task cannot be empty. Usage: add <task>"
    tasks.append(text)
    return f"Added task {len(tasks)}: {text}"


def list_tasks(tasks):
    if not tasks:
        return "No tasks yet."
    return "\n".join(f"{i}. {task}" for i, task in enumerate(tasks, start=1))


def remove_task(tasks, arg):
    if not tasks:
        return "No tasks to remove."
    arg = arg.strip()
    if not arg.isdigit():
        return "Please give a task number. Usage: remove <n>"
    index = int(arg)
    if not 1 <= index <= len(tasks):
        return f"No task {index}. Choose a number from 1 to {len(tasks)}."
    removed = tasks.pop(index - 1)
    return f"Removed: {removed}"


def run():
    tasks = []
    print("To-Do List")
    print(HELP_TEXT)

    while True:
        try:
            line = input("todo> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not line:
            continue

        command, _, arg = line.partition(" ")
        command = command.lower()

        if command == "add":
            print(add_task(tasks, arg))
        elif command == "list":
            print(list_tasks(tasks))
        elif command == "remove":
            print(remove_task(tasks, arg))
        elif command == "help":
            print(HELP_TEXT)
        elif command in ("quit", "exit", "q"):
            break
        else:
            print(f"Unknown command '{command}'. Type 'help' for options.")

    print("Goodbye! Your tasks were not saved.")