import os

# Class to represent a student with a name and course
class Students:
    def __init__(self, name, course):
        self.name = name
        self.course = course

# Lists to store students and courses
student_list = []
course_list = []

# Function to add a student and their course
def add_student_course():
    print("\n--- Add a New Student ---")
    name = input("Enter student name: ").strip()
    course = input("Enter course name: ").strip()

    # Add student to the student list
    student = Students(name, course)
    student_list.append(student)

    # Add course to course list if it's not already present
    if course not in course_list:
        course_list.append(course)

    print(f"Student '{name}' enrolled in course '{course}' added successfully!")

# Function to save student data to a file
def save_student_data():
    if not student_list:
        print("No student data to save.")
        return

    with open("students.txt", "w") as file:
        for s in student_list:
            file.write(f"{s.name}, {s.course}\n")
    print("Student data saved to 'students.txt'.")

# Function to save course data to a file
def save_course_data():
    if not course_list:
        print("No course data to save.")
        return

    with open("courses.txt", "w") as file:
        for course in course_list:
            file.write(f"{course}\n")
    print("Course data saved to 'courses.txt'.")

# Function to load and display student data from the file
def load_student_data():
    if not os.path.exists("students.txt"):
        print("No student data found.")
        return

    print("\n--- Loaded Student Data ---")
    with open("students.txt", "r") as file:
        for line in file:
            print(line.strip())

# Main function to run the program
def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add a Student and Course")
        print("2. Save Student Data")
        print("3. Save Course Data")
        print("4. Load Student Data")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student_course()
        elif choice == "2":
            save_student_data()
        elif choice == "3":
            save_course_data()
        elif choice == "4":
            load_student_data()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
