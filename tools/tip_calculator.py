"""Tip calculator: shows 10%, 15%, and 20% tips for a valid bill amount."""

AUTHOR = "Matthew Maslowski - mjmaslow-UMich"
APP_NAME = "Tip Calculator"
 
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
 
TIP_RATES = (10, 15, 20)
CENT = Decimal("0.01")
 
 
def parse_amount(raw: str) -> Decimal:
    """Convert user input to a positive monetary Decimal.
 
    Accepts an optional leading $ and thousands commas (e.g. "$1,234.50").
    Raises ValueError for non-numeric, zero, negative, or non-finite values,
    and for more than two decimal places.
    """
    cleaned = raw.strip().replace("$", "").replace(",", "")
    try:
        amount = Decimal(cleaned)
    except InvalidOperation:
        raise ValueError("Invalid input: please enter a numeric value.")
 
    if not amount.is_finite():
        raise ValueError("Invalid input: please enter a numeric value.")
    if amount <= 0:
        raise ValueError("Invalid input: amount must be greater than 0.")
    if amount != amount.quantize(CENT):
        raise ValueError("Invalid input: use at most two decimal places.")
 
    return amount
 
 
def calculate_tips(amount: Decimal) -> dict:
    """Return {rate: (tip, total)} for each tip rate, rounded to cents."""
    results = {}
    for rate in TIP_RATES:
        tip = (amount * rate / 100).quantize(CENT, rounding=ROUND_HALF_UP)
        results[rate] = (tip, amount + tip)
    return results
 
 
def run() -> None:
    """Plugin entry point. Prompts repeatedly; press Enter on a blank line to exit."""
    while True:
        raw = input("Enter the bill amount (or press Enter to exit): ")
        if raw.strip() == "":
            print("Goodbye!")
            return
 
        try:
            amount = parse_amount(raw)
        except ValueError as err:
            print(err)
            continue
 
        print(f"\nBill: ${amount:,.2f}")
        print(f"{'Tip %':<8}{'Tip':>12}{'Total':>14}")
        for rate, (tip, total) in calculate_tips(amount).items():
            print(f"{rate:<8}{'$' + format(tip, ',.2f'):>12}{'$' + format(total, ',.2f'):>14}")
        print()