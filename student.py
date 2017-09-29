class Student:
    #students = []

    school_name = "Springfield Elementary"

    def __init__(self, first_name, last_name, student_id=332):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        #self.students.append(self)

    def __str__(self):
        return "Student " + self.last_name

    def get_firstname_capitalized(self):
        return self.first_name.capitalize()

    def get_lastname_capitalized(self):
        return self.first_name.capitalize()

    def get_school_name(self):
        return self.school_name