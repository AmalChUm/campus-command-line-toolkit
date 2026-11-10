"""Summarize a list of student expenses."""

from decimal import Decimal, InvalidOperation


AUTHOR = "Eliad Spraggins"
APP_NAME = "Student Budget Summary"


def _parse_amount(entry):
    """Return a nonnegative expense amount, or None when the entry is invalid."""
    try:
        amount = Decimal(entry.strip())
    except (InvalidOperation, AttributeError):
        return None

    if not amount.is_finite() or amount < 0:
        return None
    return amount


def run():
    """Read expenses until a blank line, then print their total and average."""
    print("Enter expense amounts one at a time. Press Enter on a blank line to finish.")
    expenses = []

    while True:
        entry = input("Expense amount: ").strip()
        if not entry:
            break

        amount = _parse_amount(entry)
        if amount is None:
            print("Invalid amount. Enter a nonnegative number, such as 12.50.")
            continue
        expenses.append(amount)

    if not expenses:
        print("No expenses entered; nothing to summarize.")
        return

    total = sum(expenses, Decimal("0"))
    average = total / len(expenses)
    print(f"Total expense: {total:.2f}")
    print(f"Average expense: {average:.2f}")
