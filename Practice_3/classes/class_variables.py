class Student:
    university = "ENU"

    def __init__(self, name):
        self.name = name

student1 = Student("Madina")
student2 = Student("Sanzhar")

print(student1.university)
print(student2.university)
