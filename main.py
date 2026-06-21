students = []


def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    roll_no = input("Enter roll number: ")

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)

    print("\nStudent added successfully!\n")


def view_students():
    if len(students) == 0:
        print("\nNo students found.\n")
        return

    print("\n===== Student List =====")

    for student in students:
        print(f"Name: {student['name']} | Roll No: {student['roll_no']}")

    print()


while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("\nInvalid choice. Please try again.\n")