students = [
    {"name": "Aruzhan", "grade": 85},
    {"name": "Dias", "grade": 92},
    {"name": "Aigerim", "grade": 78}
]

sorted_students = sorted(students, key=lambda student: student["grade"])

print(sorted_students)
