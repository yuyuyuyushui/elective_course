import os, sys, pickle,json

from conf import settings
from core import obj
class Load_object:
    def load_obj(self,type, uuid):
        dir_path = '%s\db\%s\%s' % (self.dir_path, type, uuid)
        with open(dir_path,'rb') as f:
            date = pickle.load(f)
        return date
class Manage_role(Load_object):  #  管理对象
    def __init__(self):
        self.school_uuid = {}
        self.dir_path = settings.DIR_PATH
        self.school_objs = self.initialize()
        self.test()
    def test(self):
        print(self.school_objs[0].name)
        input("请输入你想关联的学校")
    def initialize(self):
        dir_path = '%s\db\school' % self.dir_path
        print(dir_path)
        print(os.path.exists(dir_path)) #E:\py_study\elective_course\elective_course_system\db\school
        if os.path.exists(dir_path): # E:\py_study\elective_course\elective_course_system\school

            school_obj = []
            for i in self.school_uuid:
                dir_path = '%s\%s' % (dir_path,i)
                obj_school = self.load_obj('school',i)
                school_obj.append(obj_school)
            return school_obj
        else:
            school_body = [("上海", '老男孩'),('北京', '老男孩')]
            return self.instantiation(school_body)
    def instantiation(self, school_bodys_list):
        school_objs = []
        for school_body in school_bodys_list:
            school_obj = obj.School(school_body[0], school_body[1])
            school_objs.append(school_obj)
            school_obj.save_obj()
            self.school_uuid[school_body[0]] = school_obj.uuid
        print(self.school_uuid)
        dir_uerpath = r"%s\userdb\userdate"%settings.DIR_PATH
        with open(dir_uerpath,'wb',encoding='utf-8') as f:
            f.write(pickle.dumps(self.school_uuid))
        return school_objs
def Teacher_role():
    pass
def Student_role():
    input("请输入你的用户名》》")
    input("请输入的登陆密码》》")

def run():
    three_view_list = [
        ('管理视图', Manage_role),
        ('讲师视图', Teacher_role),
        ('学生视图', Student_role)
    ]

    while True:
        for index, value in enumerate(three_view_list):
            print(index, value[0])
        role = input('请选择你的角色>>')
        if int(role) < len(three_view_list) and int(role) >= 0 :
            three_view_list[int(role)][1]()
