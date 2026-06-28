students = []
MENU = """
===== Student Management System =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
"""

def validate_name(name):
    """Validate student name."""

    if not name:
        print("Error: Name cannot be empty.\n")
        return False

    if not name.replace(" ", "").isalpha():
        print("Error: Name should contain only letters.\n")
        return False

    return True



def validate_student_id(student_id):
    """Validate student ID."""

    if not student_id:
        print("Error: Student ID cannot be empty.\n")
        return False

    if not student_id.isdigit():
        print("Error: Student ID must contain only numbers.\n")
        return False

    return True


def validate_roll_no(roll_no):
    """Validate roll number."""

    if not roll_no:
        print("Error: Roll number cannot be empty.\n")
        return False

    return True


def display_student(student):
    """Display student information."""

    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Roll No: {student['roll_no']}")


def get_student_id(prompt):
    """Get and validate student ID."""

    student_id = input(prompt).strip()

    if not validate_student_id(student_id):
        return None

    return int(student_id)


def print_header(title):
    """Display section header."""

    print(f"\n===== {title} =====")



def add_student():
    """Add a new student to the system."""

    name = input("Enter student name: ").strip()

    if not validate_name(name):
        return

    student_id = get_student_id("Enter student ID: ")

    if student_id is None:
        return

    if find_student_by_id(student_id):
        print("Error: Student ID already exists.\n")
        return

    roll_no = input("Enter roll number: ").strip()

    if not validate_roll_no(roll_no):
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

    print_header("Student List")

    for student in students:
        display_student(student)
        print("-" * 25)

    print()


def find_student_by_id(student_id):
    """Return student dictionary if found, otherwise None."""

    return next(
        (student for student in students if student["id"] == student_id),
        None
    )

def search_student():
    """Search for a student by ID."""

    search_id = get_student_id("Enter student ID to search: ")

    if search_id is None:
        return

    student = find_student_by_id(search_id)

    if student:
        print_header("Student Found")
        display_student(student)
        print()
    else:
        print("Student not found.\n")


def update_student():
    """Update student information."""

    student_id = get_student_id("Enter student ID to update: ")

    if student_id is None:
        return

    student = find_student_by_id(student_id)

    if not student:
        print("Student not found.\n")
        return

    print_header("Current Student Information")
    display_student(student)
    print("\n1. Update Name")
    print("2. Update Roll Number")
    print("3. Update Both")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").strip()

        if not validate_name(new_name):
            return

        student["name"] = new_name

        print("Student name updated successfully.\n")

    elif choice == "2":
        new_roll_no = input("Enter new roll number: ").strip()

        if not validate_roll_no(new_roll_no):
            return

        student["roll_no"] = new_roll_no

        print("Roll number updated successfully.\n")

    elif choice == "3":
        new_name = input("Enter new name: ").strip()
        new_roll_no = input("Enter new roll number: ").strip()

        if not validate_name(new_name):
            return

        if not validate_roll_no(new_roll_no):
            return

        student["name"] = new_name
        student["roll_no"] = new_roll_no

        print("Student updated successfully.\n")

    else:
        print("Error: Invalid choice.\n")


def delete_student():
    """Delete a student from the system."""

    student_id = get_student_id("Enter student ID to delete: ")

    if student_id is None:
        return

    student = find_student_by_id(student_id)

    if not student:
        print("Student not found.\n")
        return

    print_header("Student Found")
    display_student(student)
    confirm = input(
        "\nAre you sure you want to delete this student? (yes/no): "
    ).strip().lower()

    if confirm in ["yes", "y"]:
        students.remove(student)
        print("Student deleted successfully.\n")

    elif confirm in ["no", "n"]:
        print("Deletion cancelled.\n")

    else:
        print("Invalid choice. Deletion cancelled.\n")


def display_menu():
    """Display the main menu."""

    print(MENU)


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
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using the Student Management System. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
