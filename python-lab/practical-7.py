student = {"name": "Nihar", "age": 25, "course": "Python"}
print("Dictionary:", student)
print("Name:", student["name"])

student["age"] = 26
student["city"] = "Nagpur"
print("After updating:", student)

del student["course"]
print("After deleting course:", student)

print("Dictionary items:")
for key, value in student.items():
    print(key, ":", value)
