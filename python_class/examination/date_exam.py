from datetime import datetime

# Display the current date and time
current_date = datetime.now()
print("Current Date and Time:", current_date)

# Display the current date in the format: Day-Month-Year
formatted_date = current_date.strftime("%d-%B-%Y")
print("Formatted Date:", formatted_date)

# Display the current time in Hour:Minute AM/PM format
formatted_time = current_date.strftime("%I:%M %p")
print("Formatted Time:", formatted_time)


# Ask the user for their date of birth
user_input = input("Enter your date of birth (DD-MM-YYYY): ")

# Parse the user's input into a date object
try:
    dob = datetime.strptime(user_input, "%d-%m-%Y")
    today = datetime.now()

    # Calculate age in years
    age = today.year - dob.year

    # Adjust for the birth date not yet occurring this year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    print(f"You are {age} years old.")
except ValueError:
    print("Invalid date format. Please enter in DD-MM-YYYY.")
    

# Target date for countdown (e.g., New Year 2025)
target_date = datetime.strptime("01-01-2025", "%d-%m-%Y")

# Calculate the difference between now and the target date
current_time = datetime.now()
time_left = target_date - current_time

# Extract days, hours, and minutes from the time left
days = time_left.days
hours, remainder = divmod(time_left.seconds, 3600)
minutes, _ = divmod(remainder, 60)

print(f"Time left until {target_date.strftime('%d-%B-%Y')}:")
print(f"{days} days, {hours} hours, and {minutes} minutes.")

