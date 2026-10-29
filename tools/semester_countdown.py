from datetime import datetime

AUTHOR = "SWE 525 Drew Giffin"
APP_NAME = "Semester Countdown"
SEMESTER_END = datetime(2026, 12, 16)


def days_until(target_date: datetime, from_date: datetime) -> int:
    delta = target_date - from_date
    return delta.days


def parse_date_input(raw: str) -> datetime:
    return datetime.strptime(raw.strip(), "%m %d %Y")


def run():
    print("Semester countdown placeholder!")
