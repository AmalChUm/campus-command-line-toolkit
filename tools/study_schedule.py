"""Format course study blocks into a weekly schedule."""

AUTHOR = "Deandre Skelton"
APP_NAME = "Weekly Study Schedule Formatter"

DAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"
)


def run():
    schedule = {day: [] for day in DAYS}

    print("\nWeekly Study Schedule Formatter")
    print("Enter study blocks. Leave the course blank to finish.")

    while True:
        course = input("\nCourse name: ").strip()
        if not course:
            break

        day = input("Day (Monday-Sunday): ").strip().capitalize()
        while day not in DAYS:
            print("Please enter a full day name, such as Monday.")
            day = input("Day (Monday-Sunday): ").strip().capitalize()

        block = input("Study block (example: 3 PM - 4 PM): ").strip()
        while not block:
            print("The study block cannot be empty.")
            block = input("Study block: ").strip()

        schedule[day].append((course, block))

    if not any(schedule.values()):
        print("\nNo study blocks entered.")
        return

    print("\nYOUR WEEKLY STUDY SCHEDULE")
    print("=" * 32)

    for day in DAYS:
        print(f"\n{day}")
        if schedule[day]:
            for course, block in schedule[day]:
                print(f"  {block} | {course}")
        else:
            print("  No study blocks scheduled.")