"""Student Manager command-line example for DevOps Lab 5."""

from student import Student


def add_student(students: list, student_id: str, name: str, age: int, grade: str) -> list:
    """Add a student unless the ID is already present."""
    if any(student.student_id == student_id for student in students):
        print(f"Mã sinh viên {student_id} đã tồn tại!")
        return students

    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print(f"Đã thêm sinh viên: {new_student}")
    return students


def main():
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    add_student(students, "SV004", "Pham Thi D", 22, "K19")

    for student in students:
        print(f"  {student}")
    print(f"\nTotal: {len(students)} students")


if __name__ == "__main__":
    main()
