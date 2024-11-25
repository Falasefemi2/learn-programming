import sys

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print(f"Error occurred: {e}", file=sys.stderr)
#     sys.exit(1)


# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     with open("error_log.txt", "w") as file:
#         print(f"Error occurred: {e}", file=file)
#     sys.exit(1)



try:
    user1 = int(input("ENTER FIRST NUMBER: "))
    user2 = int(input("ENTER SECOND NUMBER: "))
    result = user1 / user2
    print(f"The result is: {result}")
except ZeroDivisionError as e:
    with open("error_log.txt", "w") as file:
        print(f"Error occurred: {e}", file=file)
    sys.exit(1)
except ValueError as e:
    with open("error_log.txt", "w") as file:
        print(f"Invalid input: {e}", file=file)
    sys.exit(1)
