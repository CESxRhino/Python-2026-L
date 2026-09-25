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