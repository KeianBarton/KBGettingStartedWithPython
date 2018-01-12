students = []

class Student1:
    def add_student(self, name, student_id):
        student = {"name": name, "student_id":student_id}
        students.append(student)

class Student2:
    def __init__(self, name, student_id):
        student = {"name": name, "student_id":student_id}
        students.append(student)

    def __str__(self):
        return "Student"

class Student3:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def change_school_name(self):
        self.school_name = "Foo"


student = Student3("Mark", 1)
student.change_school_name()
print(student.school_name)


class HighSchoolStudent(Student3):
    school_name = "Springfield High School"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

