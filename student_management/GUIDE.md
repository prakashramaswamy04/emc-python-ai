Developer & User Guide — Student Management System

Purpose
- This guide explains how to use the CLI and how to work with and extend the code.

Running the application
- From project root (/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai):
  - python3 -m student_management.main
- The program will create [students.csv](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/students.csv) automatically if it doesn't exist.

Interactive menu options
1. Add Student
   - Prompts for name, age, gender, course, email, phone, marks
   - Input validation applied (age integer, marks between 0-100, non-empty name/email/course)
   - Student ID is auto-generated (format STUxxxxx)
2. View Students
   - Shows all students saved in the CSV
3. Search Student
   - Enter a full/partial name or student ID to find matches
4. Update Student
   - Enter Student ID. Then supply new values or leave blank to keep existing
   - Updated values are validated before persisting
5. Delete Student
   - Enter Student ID and type DELETE to confirm
6. Exit

CSV format
- The CSV header and columns are defined in [csv_handler.py](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/csv_handler.py):
  student_id,name,age,gender,course,email,phone,marks
- Keep the header intact if editing the CSV manually.

Key modules and how they connect
- models.py: defines Person (abstract), Student, GraduateStudent and conversions to/from dict for CSV I/O
- csv_handler.py: low-level CSV utilities (read, append, overwrite) and ensures the CSV file exists
- student_service.py: business logic — validation, ID generation, and CRUD that operate on CSV data
- main.py: ties everything into an interactive menu and handles user I/O

Extending the project
- Add unit tests
  - Create tests for validate_student_data, generate_student_id, and CRUD ops using temporary CSV files
- Add stricter validation
  - Replace the simple email check with a regex or use email-validator
- Add import/export
  - Add JSON export and an import command to batch-create students
- Add a small web UI
  - Build a simple Flask or FastAPI wrapper that calls student_service functions

Development tips
- Keep business logic in student_service; keep CLI code in main.py so automated tests can import the service functions directly
- When changing CSV schema, update FIELDNAMES in csv_handler.py and mapping logic in models.py

Common commands (examples)
- Run CLI: python3 -m student_management.main
- Run a scripted demo (example on macOS/Linux):
  printf "1\nAlice\n21\nFemale\nCS\nalice@example.com\n+12345\n90\n2\n6\n" | python3 -m student_management.main

If anything in the guide should be more detailed or you'd like a CONTRIBUTING.md or tests scaffold, say which and it will be added.