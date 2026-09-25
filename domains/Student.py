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
        return self.__gpa
    def set_stu_gpa(self,gpa):
        self.__gpa = gpa