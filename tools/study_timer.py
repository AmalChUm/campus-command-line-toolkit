import time

AUTHOR = "Destiny Jordan"
APP_NAME = "Study Timer"


def run():
    while True:
        timer = input("Enter the number of minutes for your study session: ")
        try:
            minutes = int(timer)
            if minutes <= 0:
                print("Please enter a number greater than 0.")
                continue
        except ValueError:
            print("Please enter a valid number of minutes.")
            continue
        break

    print(f"Starting a {minutes}-minute study session...")

    try:
        for i in range(minutes, 0, -1):
            print(f"{i} minute(s) remaining...")
            time.sleep(60)
        print("Time's up! Take a break.")
    except KeyboardInterrupt:
        print("\nStudy session interrupted. Take a break and try again later.")

 
