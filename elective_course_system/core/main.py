import os, sys, pickle,json

from conf import settings
from core import obj

class Manage_role():  #  管理对象
    def __init__(self):
        self.route = [('创建课程', self.create_course),
                      ('创建班级', self.create_classes),
                      ("查询讲师", self.query_teacher),
                      ('查询班级', self.query_classes),
                      ("查询课程", self.query_course)]
        self.school_uuid = {}
        self.dir_path = settings.DIR_PATH
        self.initialize()
        self.run()
        # self.run(self.schoolObjList)


    def initialize(self):
        dir_path = '%s\db\school' % self.dir_path
        # print(dir_path)
        # print(os.path.exists(dir_path)) #E:\py_study\elective_course\elective_course_system\db\school
        if os.path.exists(dir_path): # E:\py_study\elective_course\elective_course_system\school
            obj_schooles = obj.School.get_all('school')
            self.run()

        else:
            school_body = [("上海", '老男孩'),('北京', '老男孩')]
            return self.instantiation(school_body)
    def instantiation(self, school_bodys_list):
        school_objs = []
        for school_body in school_bodys_list:
            school_obj = obj.School(school_body[0], school_body[1])
            school_objs.append(school_obj)
            school_obj.save_obj()
        return school_objs

    def run(self):
        schoolObejects = obj.School.get_all('school')
        for index, value in enumerate(schoolObejects):
            print(index, value.addree)
        schoolNum = input("请输入你选择的学校>>")
        schoolObeject = schoolObejects[int(schoolNum)]
        print(hasattr(Manage_role, 'route'))
        flag = False
        while not flag:
            for inx, view in enumerate(self.route):
                print(inx, view[0])
            view_index = input('请输入你想执行的操作>>')
            if view_index == 'b':
                flag = True
            elif view_index.isdigit() and int(view_index)>=0 and int(view_index)<len(self.route):
                self.route[int(view_index)][1](schoolObeject)

    def create_course(self,schoolObeject):
        course,price,cycle = input('请输入创建的课程名，价格，周期》》').strip().split(',')
        schoolObeject.create_course(course,price,cycle)
        print(schoolObeject.course)

    def create_classes(self):
        # obj.Teacher().get_all('teacher')
        pass
    def query_teacher(self):
        pass
    def query_classes(self):
        pass
    def query_course(self):
        pass
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
