from datetime import datetime

AUTHOR = "SWE 525 Drew Giffin"
APP_NAME = "Semester Countdown"
SEMESTER_END = datetime(2026, 12, 16)


def time_until(target_date: datetime, from_date: datetime) -> dict:
    delta = target_date - from_date
    total_seconds = int(delta.total_seconds())
    return {
        "days": delta.days,
        "hours": total_seconds // 3600 % 24,
        "minutes": total_seconds // 60 % 60,
        "seconds": total_seconds % 60,
        "total_seconds": total_seconds,
    }


def run():
    result = time_until(SEMESTER_END, datetime.now())
    print(result)
