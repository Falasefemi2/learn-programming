import os

class Student:
    def __init__(self, name, age, school, grade):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
        
    def __str__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, School: {self.school}, Grade: {self.grade}"
    
students = []

def add_students():
    while True:
        name = input("Enter student's name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        school = input("Enter student's school: ")
        age = input("Enter student's age: ")
        grade = input("Enter student's grade: ")
        student = Student(name.strip(), age.strip(), school.strip(), grade.strip())
        students.append(student)
        print(f"Student {name} added successfully!")
    
def display_students():
    if not students:
        print("No students to display.")
        return
    for student in students:
        print(student)

def search_student():
    name = input("Enter the name of the student to search: ")
    found = False  # Flag to track if a student is found
    for student in students:
        if student.name.lower() == name.lower():
            print("Student Found:")
            print(student)
            found = True  # Set flag to True if student is found
            break  # Exit loop after finding the student
    if not found:
        print("Student not found.")

def save_student_data():
    with open('student.txt', "w") as file:
        for student in students:
            file.write(f"{student.name}, {student.age}, {student.school}, {student.grade}\n")
    print("Student data saved to 'student.txt'.")

def load_student_data():
    if not os.path.exists("student.txt"):
        print("No saved data found.")
        return
    with open("student.txt", "r") as file:
        for line in file:
            # Strip whitespace and split by comma
            name, age, school, grade = map(str.strip, line.strip().split(","))
            students.append(Student(name, age, school, grade))
    print("Student data loaded successfully.")
         

# Menu System
def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student(s)")
        print("2. Display All Students")
        print("3. Search Student")
        print('4. Save Students to File') 
        print('5. Load Students from File') 
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_students()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            save_student_data()
        elif choice == "5":
            load_student_data()
        elif choice == "6":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

# Run the system
if __name__ == "__main__":
    main()
