class Student:
    def __init__(self, name, city):
        self.name = name
        self.city = city

student1 = Student("Dias", "Astana")
student2 = Student("Aigerim", "Shymkent")

print(student1.name, student1.city)
print(student2.name, student2.city)
