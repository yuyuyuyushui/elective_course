from core import obj

def create_course(name,time,price):
    couse_obj = obj.Course(name, time, price)
    print(couse_obj.name)
def create_classes():
    pass
def manage_role():
    name, time, price =input("请输入课程名，周期，价格").strip().split(',')
    print(name,time,price)
    create_course(name, time, price)

def teacher_role():
    pass
def student_role():
    input("请输入你的用户名》》")
    input("请输入的登陆密码》》")

def run():
    three_view_list = [
        ('管理视图', manage_role),
        ('讲师视图', teacher_role),
        ('学生视图', student_role)
    ]

    while True:
        for index, value in enumerate(three_view_list):
            print(index, value[0])
        role = input('请选择你的角色>>')
        if int(role) < len(three_view_list) and int(role) >= 0 :
            three_view_list[int(role)][1]()
