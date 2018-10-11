from core import obj
three_view_list = [
    ('学校视图',manage_role),
    ( '讲师视图',teacher_role),
    ('学生视图',student_role)
    ]
def school_role():
    obj.School('上海')
def teacher_role():
    pass
def student_role():
    pass
def run():
    while True:
        for index, value in three_view_list:
            print(index,value[0])
        role = input('请选择你的角色')
        if int(role) < len(three_view_list) and int(role) >= 0 :
            three_view_list[int(role)][1]()
