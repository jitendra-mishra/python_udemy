class Employee:
    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary


class Programmer(Employee):
    def __init__(self, full_name, salary, programming_language):
        Employee.__init__(self, full_name, salary)
        self.programming_language = programming_language


jitu = Programmer("Jitendra Mishra", 15000, "Python")

print(f"Name={jitu.full_name} Salary={jitu.salary}")