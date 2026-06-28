students = []


def add_student():
    """Add a new student to the system."""

    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Name cannot be empty.\n")
        return

    if not name.replace(" ", "").isalpha():
        print("Error: Name should contain only letters.\n")
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

def find_student_by_id(student_id):
    """Return student if found, otherwise None."""

    for student in students:
        if student["id"] == student_id:
            return student

    return None


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

    student = find_student_by_id(search_id)

    if student:
        print("\n===== Student Found =====")
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Roll No: {student['roll_no']}\n")
    else:
        print("Student not found.\n")
def update_student():
    """Update student information."""

    student_id = input("Enter student ID to update: ").strip()

    if not student_id:
        print("Error: Student ID cannot be empty.\n")
        return

    if not student_id.isdigit():
        print("Error: Student ID must contain only numbers.\n")
        return

    student_id = int(student_id)

    student = find_student_by_id(student_id)

    if not student:
        print("Student not found.\n")
        return

    print("\n===== Current Student Information =====")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Roll No: {student['roll_no']}")

    print("\n1. Update Name")
    print("2. Update Roll Number")
    print("3. Update Both")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        new_name = input("Enter new name: ").strip()

        if not new_name:
            print("Error: Name cannot be empty.\n")
            return

        if not new_name.replace(" ", "").isalpha():
            print("Error: Name should contain only letters.\n")
            return

        student["name"] = new_name

        print("Student name updated successfully.\n")

    elif choice == "2":

        new_roll_no = input("Enter new roll number: ").strip()

        if not new_roll_no:
            print("Error: Roll number cannot be empty.\n")
            return

        student["roll_no"] = new_roll_no

        print("Roll number updated successfully.\n")

    elif choice == "3":

        new_name = input("Enter new name: ").strip()
        new_roll_no = input("Enter new roll number: ").strip()

        if not new_name:
            print("Error: Name cannot be empty.\n")
            return

        if not new_name.replace(" ", "").isalpha():
            print("Error: Name should contain only letters.\n")
            return

        if not new_roll_no:
            print("Error: Roll number cannot be empty.\n")
            return

        student["name"] = new_name
        student["roll_no"] = new_roll_no

        print("Student updated successfully.\n")

    else:
        print("Error: Invalid choice.\n")

def delete_student():
    """Delete a student from the system."""

    student_id = input("Enter student ID to delete: ").strip()

    if not student_id:
        print("Error: Student ID cannot be empty.\n")
        return

    if not student_id.isdigit():
        print("Error: Student ID must contain only numbers.\n")
        return

    student_id = int(student_id)

    student = find_student_by_id(student_id)

    if not student:
        print("Student not found.\n")
        return

    print("\n===== Student Found =====")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Roll No: {student['roll_no']}")

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

    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


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
