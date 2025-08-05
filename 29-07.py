import datetime
from datetime import timedelta

# 1. Current Date and Time
now = datetime.datetime.now()
print("1. Current Date and Time:", now)

# 2. Today's Date
today = datetime.date.today()
print("2. Today's Date:", today)

# 3. Create Custom Date and Time
custom_date = datetime.date(2025, 8, 5)
print("3. Custom Date:", custom_date)

custom_time = datetime.time(14, 30, 15)
print("4. Custom Time:", custom_time)

# 4. Extracting Parts of Date/Time
print("5. Year:", now.year)
print("6. Month:", now.month)
print("7. Day:", now.day)
print("8. Hour:", now.hour)
print("9. Minute:", now.minute)
print("10. Second:", now.second)

# 5. Formatting Date/Time using strftime()
formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("11. Formatted Date-Time:", formatted)

# 6. Parsing Date String using strptime()
date_str = "05-08-2025 14:45:30"
parsed_date = datetime.datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
print("12. Parsed Date-Time:", parsed_date)

# 7. Date Arithmetic using timedelta
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print("13. Tomorrow:", tomorrow)
print("14. Yesterday:", yesterday)

# 8. Difference Between Two Dates
d1 = datetime.date(2025, 8, 1)
d2 = datetime.date(2025, 8, 5)
diff = d2 - d1
print("15. Difference in days:", diff.days)

# 9. Current Timestamp
timestamp = datetime.datetime.now().timestamp()
print("16. Current Timestamp:", timestamp)