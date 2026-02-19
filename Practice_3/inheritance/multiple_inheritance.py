class University:
    def university_name(self):
        return "KazNU"

class City:
    def city_name(self):
        return "Astana"

class Student(University, City):
    pass

student = Student()

print(student.university_name())
print(student.city_name())
