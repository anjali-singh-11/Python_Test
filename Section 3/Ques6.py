students_data = [
    "Rahul-85",
    "Priya-90",
    "Rohan-78",
    "Sneha-92",
    "Amit-65"
]

with open("report.txt", "w") as file:
    for student in students_data:
        file.write(student + "\n")

print("Data successfully written to report.txt.\n")
try:
    print("Students scoring more than 80:")
    with open("report.txt", "r") as file:
        pass

except FileNotFoundError:
    print("Error: 'report.txt' does not exist. Please create the file first.")

finally:
    print("\nExecution complete. The finally block has run.")