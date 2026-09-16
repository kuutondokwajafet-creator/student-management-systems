import sqlite3


# Connect to the database
connection = sqlite3.connect("students.db")
cursor = connection.cursor()


# Create the students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    student_number TEXT NOT NULL UNIQUE,
    programme TEXT NOT NULL
)
""")

connection.commit()


def add_student():
    name = input("Enter student name: ")
    student_number = input("Enter student number: ")
    programme = input("Enter programme: ")

    try:
        cursor.execute(
            "INSERT INTO students (name, student_number, programme) VALUES (?, ?, ?)",
            (name, student_number, programme)
        )
        connection.commit()
        print("Student added successfully.")
    except sqlite3.IntegrityError:
        print("Student number already exists.")


def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\nStudent Records")
    print("-" * 60)

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Student Number: {student[2]} | "
            f"Programme: {student[3]}"
        )


def search_student():
    student_number = input("Enter student number to search: ")

    cursor.execute(
        "SELECT * FROM students WHERE student_number = ?",
        (student_number,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent found:")
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Student Number: {student[2]}")
        print(f"Programme: {student[3]}")
    else:
        print("Student not found.")


def delete_student():
    student_number = input("Enter student number to delete: ")

    cursor.execute(
        "DELETE FROM students WHERE student_number = ?",
        (student_number,)
    )

    connection.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student not found.")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

connection.close()
