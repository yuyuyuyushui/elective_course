import pickle, uuid, os
from conf import settings
def uuids():
    return uuid.uuid4()
class Save:
    dir = settings.DIR_PATH
    obj_num = uuid.uuid4()

    def save_obj(self):
        dir_path = '%s\db\%s' % (self.dir, self.path)
        if os.path.exists(dir_path):
            dir_path = '%s\%s' % (dir_path, self.uuid)
            with open(dir_path, 'wb') as f:
                pickle.dump(self, f)
        else:
            os.mkdir(dir_path)
            dir_path = '%s\%s'%(dir_path,self.uuid)
            with open(dir_path, 'wb') as f:
                pickle.dump(self, f)
    def load_obj(self,):
        dir_path = '%s\db\%s\%s' % (dir, self.path, self.uuid)
        with open(dir_path,'rb') as f:
            date = pickle.load(f)
        return date
class School(Save):
    def __init__(self,addree, name):
        self.path = 'school'
        self.addree = addree
        self.name = name
        self.course = []  # 学校创建课程
        self.classes = []  # 学校创建班级
        self.uuid = uuids()

    def create_course(self, courese_obj):
        self.course.append(courese_obj)

    def create_classes(self, courese_obj):
        self.classes.append(courese_obj)
class Course(Save):
    def __init__(self, name, cycle, price):
        self.path = 'course'
        self.uuid = uuids()
        self.name = name
        self.cycle = cycle
        self.price = price
class Classes(Save):
    def __init__(self, name):
        self.name = name
        self.course = Course  # 班级关联课程
        self.teacher = Teacher  # 班级关联讲师
class Teacher(Save):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.school = School # 讲师关联学校
class Student(Save):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.classes = Classes # 学生关联班级
    def chioce_school(self, school_obj):
        self.school = school_obj


if __name__ == "__main__":
    print(uuid.uuid4())