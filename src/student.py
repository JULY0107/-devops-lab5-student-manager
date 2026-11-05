"""Student model for DevOps Lab 5."""


class Student:
    """Represent a student."""

    def __init__(self, student_id: str, name: str, age: int, grade: str):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self) -> str:
        return f"Student(id={self.student_id}, name='{self.name}', age={self.age}, grade='{self.grade}')"

    def to_dict(self) -> dict:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
        }


if __name__ == "__main__":
    student = Student("SV001", "Nguyen Van A", 20, "K20")
    print(student)
    print(student.to_dict())
