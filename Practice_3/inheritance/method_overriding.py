class Person:
    def speak(self):
        return "I am a person"

class Student(Person):
    def speak(self):
        return "I am a student"

person = Person()
student = Student()

print(person.speak())
print(student.speak())