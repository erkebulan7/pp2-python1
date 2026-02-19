class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        return f"My name is {self.name} and I live in {self.city}"

student = Student("Nurlan", "Aktobe")

print(student.introduce())
