import re

text = "Welcome to Python class!"
pattern = "Python"

match = re.search(pattern, text)
if match:
    print(f"Found {pattern} in the text at position {match.start()}")
else:
    print(f"{pattern} not found in text")


email = input("Enter your email: ")
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(email_pattern, email):
    print("Valid email!")
else:
    print("Invalid email!")


numbers = re.findall(r"\d+", "Order number 12345 was shipped on 2024-11-25.")
print(f"Found numbers: {numbers}")


# Example 1: Check if the string starts with "Python"
input1 = "Python is fun"
pattern1 = "^Python"  # `^` ensures the pattern matches the start of the string.

match1 = re.search(pattern1, input1)
if match1:
    print(f"Starts with {pattern1.replace('^', '')}.")
else:
    print(f"Does not start with {pattern1.replace('^', '')}.")

    
    
# Example 2: Validate phone number
phone = input("Enter your phone number (e.g., +123-456-7890): ")
phone_pattern = r"^\+\d{1,3}-\d{3}-\d{4}$"

if re.match(phone_pattern, phone):
    print("Valid phone number!")
else:
    print("Invalid phone number! Make sure to follow the format +123-456-7890.")


# Example 3: Extract all email addresses from a string
email_str = "Contact us at info@python.org or support@openai.com."
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", email_str)
print(f"Found email addresses: {emails}")


# Ask the user to input a string containing email addresses
user_input = input("Enter a string containing email addresses: ")

# Find all email addresses in the input
emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", user_input)

if emails:
    print(f"Found email addresses: {emails}")
else:
    print("No email addresses found.")
