# Student Management System (Python OOP)

A simple, modular, console-based Student Management System implemented in Python to demonstrate and practice object-oriented programming (OOP) concepts, CSV persistence, input validation, and a small CLI.

Features
- Add, view, search, update, and delete student records
- Student records persisted in CSV: [students.csv](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/students.csv)
- Modular design: models, CSV handler, business logic (service), and CLI separated into files

Quick start
1. Requirements: Python 3.7+ installed
2. From the repository root (/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai) run:
   - python3 -m student_management.main
3. Follow the interactive menu to add/view/search/update/delete students.

Files and structure
- [main.py](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/main.py) — CLI entry point and menu
- [models.py](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/models.py) — Person, Student, GraduateStudent classes
- [csv_handler.py](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/csv_handler.py) — CSV read/write helpers
- [student_service.py](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/student_service.py) — validation, ID generation, and CRUD operations
- [students.csv](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/students.csv) — persistent data store (created automatically)
- [README.md](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/README.md) — this file
- [GUIDE.md](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/GUIDE.md) — usage + developer guide
- [PROJECT_SUMMARY.md](/Users/prakash.ramaswamy/Documents/EMC/emc-python-ai/student_management/PROJECT_SUMMARY.md) — learning outcomes and concept mapping

Notes & improvements
- Email and phone validation are intentionally simple for learning; stricter regex or libraries may be used if needed.
- The CSV is suitable for small datasets. For larger data or concurrent access use a database.

License & credits
- Educational project — feel free to adapt for learning and teaching purposes.

If you'd like, next steps can include: adding unit tests, stricter validation, a TUI or web interface, or import/export features.