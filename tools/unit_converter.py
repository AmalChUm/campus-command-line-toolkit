"""Campus unit converter: miles/kilometers and pounds/kilograms."""

import math

AUTHOR = "Sravya Sambaturu"
APP_NAME = "Campus Unit Converter"

KILOMETERS_PER_MILE = 1.609344
KILOGRAMS_PER_POUND = 0.45359237

# Menu choice -> (from unit, to unit, multiplier applied to the input value)
CONVERSIONS = {
    "1": ("miles", "kilometers", KILOMETERS_PER_MILE),
    "2": ("kilometers", "miles", 1 / KILOMETERS_PER_MILE),
    "3": ("pounds", "kilograms", KILOGRAMS_PER_POUND),
    "4": ("kilograms", "pounds", 1 / KILOGRAMS_PER_POUND),
}


def convert(value, factor):
    """Return value multiplied by the conversion factor."""
    return value * factor


def read_amount(from_unit):
    """Ask for a number and return it, or None if the input is not valid."""
    text = input(f"Enter the number of {from_unit}: ").strip()
    try:
        amount = float(text)
    except ValueError:
        print("Invalid number. Please enter digits such as 12 or 3.5.")
        return None
    if not math.isfinite(amount) or amount < 0:
        print("Invalid number. Please enter a value of 0 or more.")
        return None
    return amount


def run():
    print("Choose a conversion:")
    for key, (from_unit, to_unit, _) in CONVERSIONS.items():
        print(f"{key}. {from_unit} to {to_unit}")

    choice = input("Selection: ").strip()
    if choice not in CONVERSIONS:
        print("Invalid selection. Please choose 1, 2, 3, or 4.")
        return

    from_unit, to_unit, factor = CONVERSIONS[choice]
    amount = read_amount(from_unit)
    if amount is None:
        return

    result = convert(amount, factor)
    print(f"{amount:g} {from_unit} = {result:.4f} {to_unit}")