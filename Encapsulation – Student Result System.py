class Student:

    def __init__(self):
        self.__marks = 0   

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks

    def get_result(self):
        if self.__marks >= 40:
            return "Pass"
        else:
            return "Fail"


s = Student()
s.set_marks(85)
print(s.get_marks())
print(s.get_result())


