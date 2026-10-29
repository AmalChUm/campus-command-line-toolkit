from datetime import datetime

AUTHOR = "Tyler Guest"
APP_NAME = "Weekday Calculator"

def run():
  date_input = input("Enter a date (YYYY-MM-DD): ").strip()
  try:
    date = datetime.strptime(date_input, "%Y-%m-%d").date()
  except ValueError:
    print("Invalid data. Enter in YYYY-MM-DD format.")
    return
  print(f"{date.isoformat()} is a {date.strftime('%A')}.")
