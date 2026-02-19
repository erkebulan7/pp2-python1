class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

class Student(Person):
    pass

student = Student("Aruzhan")

print(student.greet())
