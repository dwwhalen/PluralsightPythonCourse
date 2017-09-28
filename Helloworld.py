students = []


def get_students_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase.append(student["name"].title())
    return student_titlecase


def print_student_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)


def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not save file")


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("could not read file")


read_file()
print_student_titlecase()

enter_a_student = input("Want to enter a new student? (y/n): ")

while enter_a_student == 'y':
    student_name = input("Enter student name: ")
    student_id = input("Enter student id: ")
    add_student(student_name, student_id)
    save_file(student_name)
    enter_a_student = input("Student added.  Want to enter another new student? (y/n): ")


