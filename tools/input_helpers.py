"""Read validated console input for Campus Command-Line Toolkit tools.

Each helper displays the caller's prompt, reads input, and strips leading and
trailing whitespace. Invalid input produces a short error message and repeats
the prompt until a valid value is entered.

These helpers do not enforce tool-specific rules such as minimum or maximum
values. Callers should apply those rules to the returned value when needed.
KeyboardInterrupt and EOFError propagate to the caller rather than being
treated as invalid input.

Example usage inside a tool's run() function::

    from tools.input_helpers import read_integer, read_nonempty_text

    name = read_nonempty_text("Course name: ")
    credits = read_integer("Credit hours: ")
"""


def read_integer(prompt):
    """Prompt repeatedly until input can be converted to an integer.

    Accepts positive integers, negative integers, and zero using Python's
    int() conversion. Blank input, decimal notation such as "3.5", and
    nonnumeric text produce an error message followed by another prompt.

    Args:
        prompt (str): Message displayed before each input attempt. Include any
            desired trailing space or punctuation.

    Returns:
        int: The successfully converted value, with no range restriction.

    Raises:
        EOFError: If the input stream ends before a value is read.
        KeyboardInterrupt: If the user interrupts input, typically with Ctrl+C.
    """
    while True:
        value = input(prompt).strip()

        try:
            return int(value)
        except ValueError:
            print("Please enter a whole number.")


def read_nonempty_text(prompt):
    """Prompt repeatedly until input contains a non-whitespace character.

    Leading and trailing whitespace is removed; internal whitespace is
    preserved. Empty or whitespace-only input produces an error message
    followed by another prompt. Numeric text is accepted as a string.

    Args:
        prompt (str): Message displayed before each input attempt. Include any
            desired trailing space or punctuation.

    Returns:
        str: Nonempty text with leading and trailing whitespace removed.

    Raises:
        EOFError: If the input stream ends before a value is read.
        KeyboardInterrupt: If the user interrupts input, typically with Ctrl+C.
    """
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Please enter text; the input cannot be blank.")
