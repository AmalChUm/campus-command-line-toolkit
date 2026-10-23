"""Demonstrate reusable input-validation helpers."""

from tools.input_helpers import read_integer, read_nonempty_text

AUTHOR = "Andrew Haralambous"
APP_NAME = "Input Validation Example"


def run():
    """Collect and display a nonblank name and a valid integer."""
    name = read_nonempty_text("Enter your name: ")
    number = read_integer("Enter a whole number: ")

    print(f"Hello, {name}!")
    print(f"You entered: {number}")
