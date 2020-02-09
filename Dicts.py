student = {
    "name": "Kishore",
    "id": 101,
    "feedback": 'None'
}

student_keys = student.keys()
print(student["name"].capitalize())
print(student.get("feedback"))
print(student.get("chumma", 'Not found'))
print(student_keys)


