"""Temperature Converter Tool for the Campus Command-Line Toolkit."""

# Toolkit Contract Attributes
AUTHOR = "Munjaap Uppal"
APP_NAME = "Temperature Converter"


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def prompt_temperature(prompt_text: str) -> float | None:
    """Prompt user for a numeric temperature value with validation.

    Allows user to type 'back' to cancel and return to the tool menu.
    """
    while True:
        raw_input = input(prompt_text).strip()
        if raw_input.lower() in ("back", "b", "cancel"):
            return None

        try:
            return float(raw_input)
        except ValueError:
            print("⚠️  Invalid input: Please enter a valid number (e.g., 25, -40, 98.6) or 'back'.")


def run():
    """Main execution loop for the Temperature Converter tool."""
    print("\n" + "=" * 48)
    print(f"🌡️  {APP_NAME} — {AUTHOR}")
    print("=" * 48)

    while True:
        print("\nChoose conversion direction:")
        print("  1. Celsius to Fahrenheit (°C ➔ °F)")
        print("  2. Fahrenheit to Celsius (°F ➔ °C)")
        print("  0. Return to Main Toolkit Menu")

        choice = input("\nEnter choice (0-2): ").strip()

        if choice == "1":
            print("\n[Celsius to Fahrenheit]")
            temp = prompt_temperature("Enter temperature in °C (or 'back'): ")
            if temp is not None:
                result = celsius_to_fahrenheit(temp)
                print(f"\n✅ Result: {temp:g}°C = {result:.2f}°F")

        elif choice == "2":
            print("\n[Fahrenheit to Celsius]")
            temp = prompt_temperature("Enter temperature in °F (or 'back'): ")
            if temp is not None:
                result = fahrenheit_to_celsius(temp)
                print(f"\n✅ Result: {temp:g}°F = {result:.2f}°C")

        elif choice in ("0", "exit", "quit", "q"):
            print("Returning to the Campus Command-Line Toolkit launcher...\n")
            break

        else:
            print("⚠️  Invalid option. Please enter 1, 2, or 0.")

