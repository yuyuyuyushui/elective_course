import pickle, uuid
from conf import settings

class Save:
    dir = settings.DIR_PATH
    dir_path = '%s\db'%dir

    def save_obj(self):
        with open(self.dir_path, 'wb', encode='utf-8') as f:
            pickle.dump(self, f)

class School(Save):
    def __init__(self,addree):
        self.addree = addree
        self.course = []  # 学校创建课程
        self.classes = []  # 学校创建班级

    def create_course(self, courese_obj):
        self.course.append(courese_obj)

    def create_classes(self, courese_obj):
        self.classes.append(courese_obj)
class Course(Save):
    def __init__(self, name, cycle, price):
        self.name = name
        self.cycle = cycle
        self.price = price
class Classes(Save):
    def __init__(self, name):
        self.name = name
        self.course = Course  # 班级关联课程
        self.teacher = Teacher  # 班级关联讲师
class Teacher(Save):
    def __init__(self,name):
        self.name = name
        self.school = School # 讲师关联学校
class Student(Save):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.classes = Classes # 学生关联班级
    def chioce_school(self, school_obj):
        self.school = school_obj


if __name__ == "__main__":
    print(uuid.uuid4())