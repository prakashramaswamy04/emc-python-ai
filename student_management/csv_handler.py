import csv
import os
from typing import List, Dict

FIELDNAMES = [
    "student_id",
    "name",
    "age",
    "gender",
    "course",
    "email",
    "phone",
    "marks",
]


def ensure_csv(path: str) -> None:
    """Ensure the CSV exists and has a header."""
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    if not os.path.exists(path):
        with open(path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def read_students(path: str) -> List[Dict[str, str]]:
    """Read all student rows from CSV and return list of dicts."""
    ensure_csv(path)
    rows = []
    with open(path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip empty rows that might appear
            if not any(row.values()):
                continue
            rows.append(row)
    return rows


def write_student(path: str, student_dict: Dict[str, str]) -> None:
    """Append a single student record to CSV."""
    ensure_csv(path)
    with open(path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(student_dict)


def overwrite_students(path: str, students: List[Dict[str, str]]) -> None:
    """Overwrite the CSV with the given list of student dicts."""
    ensure_csv(path)
    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        for s in students:
            writer.writerow(s)
