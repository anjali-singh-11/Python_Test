import json

students = [
    {"name": "Rahul", "age": 20, "city": "Delhi", "marks": 85},
    {"name": "Priya", "age": 21, "city": "Mumbai", "marks": 90},
    {"name": "Amit", "age": 22, "city": "Pune", "marks": 70}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

try:
    with open("students.json", "r") as file:
        data = json.load(file)

    print("Students with marks > 75")

    for student in data:
        if student["marks"] > 75:
            print(student)

except FileNotFoundError:
    print("JSON File Not Found")