from abc import ABC, abstractmethod
from typing import Dict, Any


class Person(ABC):
    """Abstract base class representing a person.

    Demonstrates use of abstract classes and inheritance.
    """

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def display_details(self) -> None:
        """Display details about the person (implemented by subclasses)."""
        raise NotImplementedError


class Student(Person):
    """Student model that extends Person.

    Includes convenience methods to convert to/from dictionaries for CSV I/O.
    """

    def __init__(
        self,
        student_id: str,
        name: str,
        age: int,
        gender: str,
        course: str,
        email: str,
        phone: str,
        marks: float,
    ) -> None:
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.course = course
        self.email = email
        self.phone = phone
        self.marks = marks

    def display_details(self) -> None:
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Course: {self.course}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Marks: {self.marks}")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": str(self.age),
            "gender": self.gender,
            "course": self.course,
            "email": self.email,
            "phone": self.phone,
            "marks": str(self.marks),
        }

    @classmethod
    def from_dict(cls, d: Dict[str, str]) -> "Student":
        return cls(
            student_id=d.get("student_id", ""),
            name=d.get("name", ""),
            age=int(d.get("age", 0)),
            gender=d.get("gender", ""),
            course=d.get("course", ""),
            email=d.get("email", ""),
            phone=d.get("phone", ""),
            marks=float(d.get("marks", 0)),
        )


class GraduateStudent(Student):
    """Example subclass to demonstrate deeper inheritance.

    Could add graduate-specific fields (e.g., supervisor, thesis_title).
    """

    def __init__(self, *args, supervisor: str = "", **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.supervisor = supervisor

    def display_details(self) -> None:
        super().display_details()
        if getattr(self, "supervisor", None):
            print(f"Supervisor: {self.supervisor}")
