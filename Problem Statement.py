Student_marks = [35, 78, 42, 90, 25, 60, 55]
def get_passed_students(Student_marks):
    return [mark for mark in Student_marks if mark >= 40]
grace_marks = list(map(lambda x: x + 5, Student_marks))
def calculate_average(Student_marks):
    return sum(Student_marks) / len(Student_marks)
passed_students = get_passed_students(Student_marks)
class_average = calculate_average(Student_marks)
print("Passed Students:", passed_students)
print("Grace Marks:", grace_marks)
print("Class Average:", class_average)