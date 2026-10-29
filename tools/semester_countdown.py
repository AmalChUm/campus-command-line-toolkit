from datetime import datetime

AUTHOR = "SWE 525 Drew Giffin"
APP_NAME = "Semester Countdown"
SEMESTER_END = datetime(2026, 12, 16)


def time_until(target_date: datetime, from_date: datetime) -> dict:
    if not isinstance(target_date, datetime):
        raise TypeError(f"target_date must be datetime, got {type(target_date).__name__}")
    if not isinstance(from_date, datetime):
        raise TypeError(f"from_date must be datetime, got {type(from_date).__name__}")
    delta = target_date - from_date
    total_seconds = int(delta.total_seconds())
    return {
        "days": delta.days,
        "hours": total_seconds // 3600 % 24,
        "minutes": total_seconds // 60 % 60,
        "seconds": total_seconds % 60,
        "total_seconds": total_seconds,
    }


def print_result(target_date: datetime, result: dict):
    formatted_date = target_date.strftime('%B %d, %Y')
    if result['total_seconds'] < 0:
        print(f"End of semester ({formatted_date}) already passed:")
        print(f"  {abs(result['days'])} days ago")
        print(f"  {abs(result['hours'])} hours ago")
        print(f"  {abs(result['minutes'])} minutes ago")
        print(f"  {abs(result['seconds'])} seconds ago")
    else:
        print(f"Time until end of semester ({formatted_date}):")
        print(f"  {result['days']} days")
        print(f"  {result['hours']} hours")
        print(f"  {result['minutes']} minutes")
        print(f"  {result['seconds']} seconds")


def run():
    result = time_until(SEMESTER_END, datetime.now())
    print_result(SEMESTER_END, result)
