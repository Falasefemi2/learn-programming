with open("user.txt", "w") as file:
    user_input = input("Enter your username: ")  # Added colon for clarity
    file.write(user_input)
    print("Username saved successfully!")


user_ans = input("What is the file name: ")
with open("new.txt", "w") as file:  # Changed mode to "w"
    file.write(f"{user_ans}\n")

    
with open("new.txt", "a") as file:
    file.write("Adding more to it \n")
    

try:
    file_name = input("Enter file name: ")
    with open(file_name, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("File read successfully!")
finally:
    print("Execution completed.")
