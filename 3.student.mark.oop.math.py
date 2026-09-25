import math
import numpy as np
class Student:
    def __init__(self,stu_id = "",stu_name = "",dob = ""):
        self.__stu_id = stu_id
        self.__stu_name = stu_name
        self.__dob = dob
        self.__gpa = 0.0
    def get_stu_id(self):
        return self.__stu_id
    def get_stu_name(self):
        return self.__stu_name
    def get_dob(self):
        return self.__dob
    def get_stu_gpa(self):
        return self.get_stu_gpa
    def set_stu_gpa(self,gpa):
        self.__gpa = gpa
    def input_stu_inf(self):
        self.__stu_id = input("\tStudent's ID is: ")
        self.__stu_name = input("\tStudent's Name is: ")
        self.__dob = input("\tStudent's DOB is: ")
    def display_stu_inf(self):
        print(f"ID: {self.__stu_id} | Name: {self.__stu_name} | DoB: {self.__dob}|GPA: {self.__gpa:.2f}")
    
class Courses:
    def __init__(self,cou_id = "",cou_name = "",credits = 0):
        self.__cou_id = cou_id
        self.__cou_name = cou_name
        self.__credits = credits
    def get_cou_id(self):
        return self.__cou_id
    def get_name(self):
        return self.__cou_name
    def get_credits(self):
        return self.__credits;
    def input_cou_inf(self):
        self.__cou_id = input("\tCourse ID: ")
        self.__cou_name = input("\tCourse Name: ")
        self.__credits = int(input("\tCourse Credits: "))
    def display_cou_inf(self):
        print(f"Course ID: {self.__cou_id} | Course Name: {self.__cou_name} | Credits: {self.__credits}")

class SchoolMa:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}
    def input_stu(self):
        cnt = int(input("The Number of Students: "))
        print("Please enter the information of the students:")
        for _ in range(cnt):
            s = Student()
            s.input_stu_inf()
            self.__students.append(s)
    def input_cou(self):
        cnt = int(input("The Number of Courses: "))
        print("Please enter the information of the Courses:")
        for _ in range(cnt):
            s = Courses()
            s.input_cou_inf()
            self.__courses.append(s)
    def list_stu(self):
        print("\n" + "=" * 60)
        print("\nThe list of all students is:")
        print("=" * 60)
        for i in self.__students:
            i.display_stu_inf()
    def list_cou(self):
        print("\n" + "=" * 60)
        print("\nThe list of all courses is:")
        print("=" * 60)
        for i in self.__courses:
            i.display_cou_inf()
    def input_marks(self):
        course_id = input("\nSelect a course ID: ") 
        selected_course = next((c for c in self.__courses if c.get_cou_id() == course_id), None)
        print(f"Course name: {selected_course.get_name()}\n")
        if course_id not in self.__marks:
            self.__marks[course_id] = {}
        for stu in self.__students:
            mark = float(input(f"\tEnter {stu.get_stu_name()}'s mark: "))
            rounded_mark = math.floor(mark * 10)/10;
            self.__marks[course_id][stu.get_stu_id()] = rounded_mark
    def display_marks(self):
        course_id = input("\nThe course to be selected (ID): ")
        # course_name = selected_course.get_name() if selected_course else course_id
        selected_course = next((c for c in self.__courses if c.get_cou_id() == course_id), None)
        course_name = selected_course.get_name() if selected_course else course_id
        print(f"\n--- Marks for Course: {course_name} ({course_id}) ---")
        for stu in self.__students:
            mark = self.__marks[course_id].get(stu.get_stu_id())
            print(f"ID: {stu.get_stu_id()} | Name: {stu.get_stu_name()} | Mark: {mark}")
    def cal_gpa(self):
        for stu in self.__students:
            marks_list = []
            credits_list = []
            for course in self.__courses:
                c_id = course.get_cou_id()
                if c_id in self.__marks and stu.get_stu_id() in self.__marks[c_id]:
                    marks_list.append(self.__marks[c_id][stu.get_stu_id()])
                    credits_list.append(course.get_credits())
            if credits_list and sum(credits_list) > 0:
                np_marks = np.array(marks_list)
                np_credits = np.array(credits_list)
                gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
                stu.set_stu_gpa(gpa)
            else:
                stu.set_stu_gpa(0.0)
    def sort_stu_by_gpa(self):
        self.cal_gpa()
        self.__students.sort(reverse = 0,key = lambda s:s.get_stu_gpa())
        print("\n=== Students sorted by GPA (Descending) ===")
        self.list_stu()
mana = SchoolMa()
mana.input_stu()
mana.list_stu()
mana.input_cou()
mana.list_cou()
print("\nPlease enter the marks of the course: ")
while True:
    mana.input_marks()
    choice = input("\n another? (yes/no) *** ")
    if choice == 'no':
        break
while True:
    mana.display_marks()
    choice = input("\n another? (yes/no) *** ")
    if choice == 'no':
        break
mana.sort_stu_by_gpa()