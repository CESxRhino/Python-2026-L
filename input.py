import math
from domains.Student import Student
from domains.Courses import Courses
def input_stu():
    students = []
    cnt = int(input("The Number of Students: "))
    print("Please enter the information of the students:")
    for _ in range(cnt):
        stu_id = input("\tStudent's ID is: ")
        stu_name = input("\tStudent's Name is: ")
        dob = input("\tStudent's DOB is: ")
        students.append(Student(stu_id, stu_name, dob))
    return students
def input_cou():
    courses = []
    cnt = int(input("The Number of Courses: "))
    print("Please enter the information of the Courses:")
    for _ in range(cnt):
        cou_id = input("\tCourse ID: ")
        cou_name = input("\tCourse Name: ")
        credits = int(input("\tCourse Credits: "))
        courses.append(Courses(cou_id, cou_name, credits))
    return courses
def input_marks(courses, students, marks):
    courses_id = input("\nSelect a course ID: ")
    selected_course = next((c for c in courses if c.get_cou_id() == courses_id), None)
    print(f"Course name: {selected_course.get_name()}\n")
    if courses_id not in marks:
        marks[courses_id] = {}
    for stu in students:
        mark = float(input(f"\tEnter {stu.get_stu_name()}'s mark: "))
        rounded_mark = math.floor(mark * 10) / 10
        marks[courses_id][stu.get_stu_id()] = rounded_mark