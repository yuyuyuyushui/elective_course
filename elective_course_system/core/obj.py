import pickle, uuid, os
from conf import settings
def uuids():
    return uuid.uuid4()
class Save:
    dir = settings.DIR_PATH
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
    @staticmethod
    def get_all(type):
        obj_list = []
        dir_path = r"%s\db\%s"%(settings.DIR_PATH, type)

        if os.path.exists(dir_path):
            for i in os.listdir(dir_path):
                dir_paths = "%s\%s"%(dir_path, i)
                with open(dir_paths, 'rb') as f:
                    obj_list.append(pickle.load(f))
            return obj_list
        else:
            return False
    def __str__(self):
        return self.name
class School(Save):
    def __init__(self,addree, name):
        self.path = 'school'
        self.addree = addree
        self.name = name
        self.course = []  # 学校创建课程
        self.classes = []  # 学校创建班级
        self.uuid = uuids()

    def create_course(self, courseName, courseCycle, coursePrice ):
        courese_obj = Course(courseName, courseCycle, coursePrice)
        courese_obj.save_obj()
        self.course.append(courese_obj.uuid)

    def create_classes(self, name,course_uid,teacher_uid):
        courese_obj = Classes(name,course_uid,teacher_uid)
        courese_obj.save_obj()
        self.classes.append(courese_obj.uuid)
class Course(Save):
    def __init__(self, name, cycle, price):
        self.path = 'course'
        self.uuid = uuids()
        self.name = name
        self.cycle = cycle
        self.price = price
class Classes(Save):
    def __init__(self, name,course_uid,teacher_uid):
        self.path = 'classes'
        self.name = name
        self.uuid = uuids()
        self.classesCourse = course_uid  # 班级关联课程
        self.classesTeacher = teacher_uid  # 班级关联讲师
class Teacher(Save):
    def __init__(self, name, salary, school_uid):
        self.path = 'teacher'
        self.name = name
        self.uuid = uuids()
        self.salary = salary
        self.teacherSchool = school_uid  # 讲师关联学校
        self.schoolObject = self.load_schoolObject()
    def load_schoolObject(self):
        for school_obj in School.get_all('school'):
            if self.teacherSchool == school_obj.uuid:
                return school_obj
            else:
                pass
class Student(Save):
    def __init__(self, name, age, sex, class_uid):
        self.path = 'student'
        self.name = name
        self.age = age
        self.sex = sex
        self.uuid = uuids()
        self.studentClasses = class_uid  # 学生关联班级



if __name__ == "__main__":
    print(uuid.uuid4())