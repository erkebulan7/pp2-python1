class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, city):
        super().__init__(name)
        self.city = city

student = Student("Dias", "Almaty")

print(student.name)
print(student.city)
