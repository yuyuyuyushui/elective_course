import pickle
from conf import settigns
class School:
    def __init__(self,addree):
        self.addree = addree
        self.course = []
        self.classes = []
        self.teacher = []

    def creat_class(self, classes_obj): # 学校创建班级
        self.classes.append(classes_obj)

    def creat_coures(self,course_obj): # 学校创建课程
        self.classes.append(course_obj)
    def save(self,school):
        dir = "%s\db\school"%settigns.DIR_PATH
        with open(dir,'w',encoding='utf-8') as f:
            pass

class Course:
    def __init___(self,name, cycle, price):
        self.name = name
        self.cycle = cycle
        self.price = price
class Classes:
    def __init__(self, name):
        self.name = name
        self.course = Course  # 班级关联课程
        self.teacher = Teacher # 班级关联讲师
class Teacher:
    def __init__(self,name):
        self.name = name
        self.school = School # 讲师关联学校
class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.classes = Classes # 学生关联班级
    def chioce_class(self):
        pass


