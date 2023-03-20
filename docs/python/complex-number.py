class Employee:

    company_name = "ESME"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"


e1 = Employee("Bob", 33)
e2 = Employee("Alice", 34)

print(e1.description())
