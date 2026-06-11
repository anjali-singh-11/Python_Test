import json

Employees = [
    "id: 101, name: Aman\n",
    "id: 102, name: Jai\n",
    "id: 103, name: Riya\n"
]
with open('employees.txt', 'w') as file:
    file.writelines(Employees)
print("File Created successfully")

print("\nReading employee file")
with open('employees.txt', 'r') as file:
    print(file.read())


new_employees = [
    "id: 104, name: Mahi\n",
    "id: 105, name: Karan\n"
]
with open('empolyees.txt', 'r') as file:
    file.writelines(new_employees)
print("Employees appended successfully.\n")

print("Reading updated file")
with open("employees.txt", "r") as file:
    updated_content = file.read()
    print(updated_content)

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
