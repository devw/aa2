class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def get_info(self):
        return super().get_info() + f", Student's score: {self.score}"


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_info(self):
        return super().get_info() + f", Teacher's subject: {self.subject}"


student_1 = Student('Bob', 20, 18)
teacher_1 = Teacher('Alice', 40, 'Math')
print(student_1.get_info())
print(teacher_1.get_info())
