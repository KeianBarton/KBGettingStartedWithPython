import pprint

students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    print(get_students_titlecase())


def add_student(name, student_id=1):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def main(args):
    while True:
        user_input = input("Would you like to add a student? (Y or N)\n")
        if user_input.upper() == 'N':
            pprint.pprint(students)
            break
        elif user_input.upper() != 'Y':
            break
        else:
            student_name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            add_student(student_name, int(student_id))
            print_students_titlecase()


main()
