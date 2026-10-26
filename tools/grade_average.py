AUTHOR = "Nolan Hughes"
APP_NAME = "Grade Average Tool"


def run():
    print(f"{APP_NAME} by {AUTHOR}")

    total = 0
    count = 0
    highest = 0
    lowest = 100

    while True:
        user_input = input("Enter score (leave blank to finish): ")
        if user_input:
            try:
                score = float(user_input)
                if 0 <= score <= 100:
                    total += score
                    count += 1

                    if score > highest:
                        highest = score
                    if score < lowest:
                        lowest = score
                else:
                    print("Error: Entered score is not between 0 and 100 inclusive.")
            except ValueError:
                print("Error: Entered score is not a valid number.")
        else:
            break

    if count > 0:
        average = total / count
        print(f"Average: {average:.2f}")
        print(f"Highest: {highest:.2f}")
        print(f"Lowest: {lowest:.2f}")
    else:
        print("No scores were entered.")
