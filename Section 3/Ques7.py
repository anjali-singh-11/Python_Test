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

print("Deleting file and verifying")
if os.path.exists("employees.txt"):
    os.remove("employees.txt")
    print("File deleted.")

if os.path.exists("employees.txt"):
    print("Verification Failed: File still exists.")
else:
    print("Verification Success: File no longer exists.")