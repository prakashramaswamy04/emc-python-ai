with open("./basics/test.txt", "r") as file:
    content = file.read()
    print(content)

with open("./basics/test.txt", "a") as file:
    file.write("\nThis is a new line added to the file.")


import os
import csv
folder = os.listdir("./basics")

for file in folder:
    print(file)

os.rename("./basics/test.txt", "./basics/renamed_test.txt")

students = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, "A"],
    ["Bob", 21, "B"],
    ["Charlie", 19, "A"],
    ["David", 22, "C"]
]

with open("./basics/students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

with open("./basics/students.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)