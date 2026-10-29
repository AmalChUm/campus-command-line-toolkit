
AUTHOR = "Madelyn Moore"
APP_NAME = "Percentage Calculator"


def run():
    print("\nThis is a percentage Calculator!")
    print("\nChoose what you would like to calculate:")
    print("1. Calculate percentage of a number")
    print("2. Calculate percentage change")
    print("3. Calculate part from whole")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ").strip()

    if choice == "1":
        try:
            number = float(input("Enter the number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return
        try:
            percentage = float(input("Enter the percentage: "))
        except ValueError:
            print("Invalid input. Please enter a valid percentage.")
            return
        result = (percentage / 100) * number
        print(f"{percentage}% of {number} is {result}")
    elif choice == "2":
        try:
            initial_value = float(input("Enter the initial value: "))
        except ValueError:
            print("Invalid input. Please enter a valid initial value.")
            return
        try:
            final_value = float(input("Enter the final value: "))
        except ValueError:
            print("Invalid input. Please enter a valid final value.")
            return
        if initial_value == 0:
            print("Initial value cannot be zero for percentage change calculation.")
            return
        else:
            percentage_change = ((final_value - initial_value) / initial_value) * 100
            print(f"The percentage change from {initial_value} to {final_value} is {percentage_change}%")
    elif choice == "3":
        try:
            part = float(input("Enter the part value: "))
        except ValueError:
            print("Invalid input. Please enter a valid part value.")
            return
        try:
            whole = float(input("Enter the whole value: "))
        except ValueError:
            print("Invalid input. Please enter a valid whole value.")
            return
        if whole == 0:
            print("Whole value cannot be zero for percentage calculation.")
            return
        else:
            percentage = (part / whole) * 100
            print(f"{part} is {percentage}% of {whole}")
    elif choice == "4":
        print("Exiting the Percentage Calculator.")
    else:
        print("Invalid choice. Please select a valid option (1-4).")