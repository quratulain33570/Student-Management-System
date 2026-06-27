students = []


def add_student():
    """Add a new student to the system."""

    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Name cannot be empty.\n")
        return

    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Error: Student ID cannot be empty.\n")
        return

    if not student_id.isdigit():
        print("Error: Student ID must contain only numbers.\n")
        return

    student_id = int(student_id)

    for student in students:
        if student["id"] == student_id:
            print("Error: Student ID already exists.\n")
            return

    roll_no = input("Enter roll number: ").strip()

    if not roll_no:
        print("Error: Roll number cannot be empty.\n")
        return

    student = {
        "id": student_id,
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)

    print("\nStudent added successfully!\n")


def view_students():
    """Display all students."""

    if not students:
        print("No students found.\n")
        return

    print("\n===== Student List =====")

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Roll No: {student['roll_no']}"
        )

    print()


def search_student():
    """Search for a student by ID."""

    search_id = input("Enter student ID to search: ").strip()

    if not search_id:
        print("Error: Student ID cannot be empty.\n")
        return

    if not search_id.isdigit():
        print("Error: Student ID must contain only numbers.\n")
        return

    search_id = int(search_id)

    for student in students:
        if student["id"] == search_id:
            print("\n===== Student Found =====")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Roll No: {student['roll_no']}\n")
            return

    print("Student not found.\n")


def display_menu():
    """Display the main menu."""

    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")


def main():
    """Main program loop."""

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Error: Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()