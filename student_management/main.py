"""CLI entry point for the Student Management System.

This module ties together models, CSV handler, and service functions and provides
an interactive menu-driven console interface.
"""

import os
import sys

from .student_service import (
    add_student,
    get_all_students,
    find_student_by_id,
    search_students,
    update_student,
    delete_student,
)

CSV_PATH = os.path.join(os.path.dirname(__file__), "students.csv")


def display_menu() -> None:
    print("""
================================
     STUDENT MANAGEMENT SYSTEM
================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
""")


def prompt_add_student() -> None:
    print("\nAdd a new student (leave blank to cancel):")
    try:
        name = input("Name: ").strip()
        if not name:
            print("Cancelled.")
            return
        age = input("Age: ").strip()
        gender = input("Gender: ").strip()
        course = input("Course: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone: ").strip()
        marks = input("Marks (0-100): ").strip()

        student = add_student(
            CSV_PATH,
            name=name,
            age=age,
            gender=gender,
            course=course,
            email=email,
            phone=phone,
            marks=marks,
        )
        print("\nStudent added successfully:")
        student.display_details()
    except Exception as e:
        print(f"Error adding student: {e}")


def prompt_view_students() -> None:
    students = get_all_students(CSV_PATH)
    if not students:
        print("No students found.")
        return
    print(f"\nTotal students: {len(students)}\n")
    for s in students:
        print("----------------------------")
        s.display_details()
    print("----------------------------")


def prompt_search_student() -> None:
    q = input("Enter student name or ID to search: ").strip()
    if not q:
        print("Cancelled.")
        return
    results = search_students(CSV_PATH, q)
    if not results:
        print("No matching students found.")
        return
    for s in results:
        print("----------------------------")
        s.display_details()
    print("----------------------------")


def prompt_update_student() -> None:
    sid = input("Enter Student ID to update: ").strip()
    if not sid:
        print("Cancelled.")
        return
    existing = find_student_by_id(CSV_PATH, sid)
    if not existing:
        print("Student not found.")
        return
    print("Enter new values (leave blank to keep existing):")
    name = input(f"Name [{existing.name}]: ").strip() or existing.name
    age = input(f"Age [{existing.age}]: ").strip() or str(existing.age)
    gender = input(f"Gender [{existing.gender}]: ").strip() or existing.gender
    course = input(f"Course [{existing.course}]: ").strip() or existing.course
    email = input(f"Email [{existing.email}]: ").strip() or existing.email
    phone = input(f"Phone [{existing.phone}]: ").strip() or existing.phone
    marks = input(f"Marks [{existing.marks}]: ").strip() or str(existing.marks)

    try:
        updated = update_student(
            CSV_PATH,
            sid,
            {
                "name": name,
                "age": age,
                "gender": gender,
                "course": course,
                "email": email,
                "phone": phone,
                "marks": marks,
            },
        )
        if updated:
            print("Student updated successfully:")
            updated.display_details()
        else:
            print("Update failed.")
    except Exception as e:
        print(f"Error updating student: {e}")


def prompt_delete_student() -> None:
    sid = input("Enter Student ID to delete: ").strip()
    if not sid:
        print("Cancelled.")
        return
    confirm = input(f"Type DELETE to confirm deletion of {sid}: ")
    if confirm != "DELETE":
        print("Deletion cancelled.")
        return
    ok = delete_student(CSV_PATH, sid)
    if ok:
        print("Student deleted.")
    else:
        print("Student not found.")


def main() -> None:
    print("Starting Student Management System. CSV:", CSV_PATH)
    # Ensure the CSV file exists by importing the csv handler indirectly
    from .csv_handler import ensure_csv

    ensure_csv(CSV_PATH)

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            prompt_add_student()
        elif choice == "2":
            prompt_view_students()
        elif choice == "3":
            prompt_search_student()
        elif choice == "4":
            prompt_update_student()
        elif choice == "5":
            prompt_delete_student()
        elif choice == "6":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
