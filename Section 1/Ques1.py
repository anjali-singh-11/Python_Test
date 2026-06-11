class Employee:
    def __init__(self):
        self.__salary = 50000

    def increment(self):
        self.__salary += 10000

    def deduct(self):
        self.__salary -= 5000

    def get_salary(self):
        print(f"Current Salary: {self.__salary}")
    
emp1 = Employee()
emp2 = Employee()

print("For Employee 1")
emp1.increment()
emp1.deduct()
emp1.get_salary()

print("\nFor Employee 2")
emp2.increment()
emp2.deduct()
emp2.get_salary()