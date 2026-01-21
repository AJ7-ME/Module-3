from datetime import date, time, datetime
today = date.today()
now = datetime.now()
print("Today's date:", today)
print("\nCurrent date and time:", now)
print("\nDate components", today.day, today.month, today.year)
while True:
    now = datetime.now()
    print("THE time is :", now.time())