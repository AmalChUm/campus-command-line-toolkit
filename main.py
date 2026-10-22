"""Launcher for the Campus Command-Line Toolkit."""

from importlib import import_module
from pkgutil import iter_modules
from tools import __path__ as tools_path


def discover_tools():
    discovered = []
    for module_info in iter_modules(tools_path):
        if module_info.name.startswith("_"):
            continue
        module = import_module(f"tools.{module_info.name}")
        if all(hasattr(module, attribute) for attribute in ("AUTHOR", "APP_NAME", "run")):
            discovered.append(module)
    return sorted(discovered, key=lambda module: module.APP_NAME.lower())


def main():
    tools = discover_tools()
    if not tools:
        print("No tools are available yet.")
        return

    print("Campus Command-Line Toolkit")
    for index, module in enumerate(tools, start=1):
        print(f"{index}. {module.APP_NAME} — {module.AUTHOR}")
    print("0. Exit")

    choice = input("Choose a tool: ").strip()
    if choice == "0":
        return
    try:
        selected = tools[int(choice) - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return
    selected.run()


if __name__ == "__main__":
    main()
