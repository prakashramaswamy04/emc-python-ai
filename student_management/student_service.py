import random
import re
from typing import List, Optional, Dict

from .csv_handler import FIELDNAMES, read_students, write_student, overwrite_students
from .models import Student


def generate_student_id(csv_path: str, prefix: str = "STU", digits: int = 5) -> str:
    """Generate a unique student ID by checking existing CSV records."""
    existing = {r.get("student_id") for r in read_students(csv_path)}
    while True:
        num = random.randint(0, 10 ** digits - 1)
        sid = f"{prefix}{num:0{digits}d}"
        if sid not in existing:
            return sid


def validate_student_data(
    name: str,
    age: str,
    gender: str,
    course: str,
    email: str,
    phone: str,
    marks: str,
) -> Dict[str, object]:
    """Validate inputs and return a dict with parsed/validated values or raise ValueError."""
    errors = []
    if not name.strip():
        errors.append("Name cannot be empty.")

    try:
        age_val = int(age)
        if age_val <= 0:
            errors.append("Age must be a positive integer.")
    except ValueError:
        errors.append("Age must be an integer.")
        age_val = None

    gender_val = gender.strip() or "Unspecified"

    if not course.strip():
        errors.append("Course cannot be empty.")

    if not email.strip() or "@" not in email:
        errors.append("Email must be a valid email address.")

    phone_val = phone.strip()
    if not re.fullmatch(r"[0-9+\-() ]{7,20}", phone_val):
        errors.append("Phone must contain 7-20 digits or common phone characters.")

    try:
        marks_val = float(marks)
        if not (0 <= marks_val <= 100):
            errors.append("Marks must be between 0 and 100.")
    except ValueError:
        errors.append("Marks must be a number.")
        marks_val = None

    if errors:
        raise ValueError("; ".join(errors))

    return {
        "name": name.strip(),
        "age": age_val,
        "gender": gender_val,
        "course": course.strip(),
        "email": email.strip(),
        "phone": phone_val,
        "marks": marks_val,
    }


def add_student(csv_path: str, **kwargs) -> Student:
    """Validate input, generate ID, create Student, and persist to CSV."""
    validated = validate_student_data(
        kwargs.get("name", ""),
        kwargs.get("age", ""),
        kwargs.get("gender", ""),
        kwargs.get("course", ""),
        kwargs.get("email", ""),
        kwargs.get("phone", ""),
        kwargs.get("marks", ""),
    )

    student_id = generate_student_id(csv_path)
    student = Student(
        student_id=student_id,
        name=validated["name"],
        age=validated["age"],
        gender=validated["gender"],
        course=validated["course"],
        email=validated["email"],
        phone=validated["phone"],
        marks=validated["marks"],
    )

    write_student(csv_path, student.to_dict())
    return student


def get_all_students(csv_path: str) -> List[Student]:
    rows = read_students(csv_path)
    return [Student.from_dict(r) for r in rows]


def find_student_by_id(csv_path: str, student_id: str) -> Optional[Student]:
    rows = read_students(csv_path)
    for r in rows:
        if r.get("student_id") == student_id:
            return Student.from_dict(r)
    return None


def search_students(csv_path: str, query: str) -> List[Student]:
    q = query.strip().lower()
    results = []
    for r in read_students(csv_path):
        if q in (r.get("name", "").lower() or "") or q in (r.get("student_id", "").lower() or ""):
            results.append(Student.from_dict(r))
    return results


def update_student(csv_path: str, student_id: str, updates: Dict[str, str]) -> Optional[Student]:
    """Update a student's fields. Returns updated Student or None if not found."""
    rows = read_students(csv_path)
    updated = None
    for i, r in enumerate(rows):
        if r.get("student_id") == student_id:
            # Prepare merged data for validation: use existing values if not provided in updates
            merged = {
                "name": updates.get("name", r.get("name", "")),
                "age": updates.get("age", r.get("age", "")),
                "gender": updates.get("gender", r.get("gender", "")),
                "course": updates.get("course", r.get("course", "")),
                "email": updates.get("email", r.get("email", "")),
                "phone": updates.get("phone", r.get("phone", "")),
                "marks": updates.get("marks", r.get("marks", "")),
            }
            # Validate merged data
            validated = validate_student_data(
                merged["name"],
                str(merged["age"]),
                merged["gender"],
                merged["course"],
                merged["email"],
                merged["phone"],
                str(merged["marks"]),
            )
            # Update row
            new_row = {
                "student_id": student_id,
                "name": validated["name"],
                "age": str(validated["age"]),
                "gender": validated["gender"],
                "course": validated["course"],
                "email": validated["email"],
                "phone": validated["phone"],
                "marks": str(validated["marks"]),
            }
            rows[i] = new_row
            updated = Student.from_dict(new_row)
            break

    if updated:
        overwrite_students(csv_path, rows)
    return updated


def delete_student(csv_path: str, student_id: str) -> bool:
    rows = read_students(csv_path)
    new_rows = [r for r in rows if r.get("student_id") != student_id]
    if len(new_rows) == len(rows):
        return False
    overwrite_students(csv_path, new_rows)
    return True
