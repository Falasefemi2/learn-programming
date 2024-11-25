from datetime import datetime, date, time, timedelta

current_time = datetime.now()

print("Current date and time:", current_time)

print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)
print("Hour:", current_time.hour)
print("Minute:", current_time.minute)
print("Second:", current_time.second)

formatted_date = current_time.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted date and time:", formatted_date)

date_string = "25-11-2024 15:30:00"
parsed_date = datetime.strptime(date_string, "%d-%m-%Y %H:%M:%S")
print("Parsed date:", parsed_date)


# Current date
today = date.today()
print("Today's date:", today)

# Custom time
specific_time = time(14, 30, 0)  # 2:30 PM
print("Custom time:", specific_time)

# Add 5 days to the current time
future_date = current_time + timedelta(days=5)
print("Future date:", future_date)

# Subtract 2 hours
past_time = current_time - timedelta(hours=2)
print("Past time:", past_time)



