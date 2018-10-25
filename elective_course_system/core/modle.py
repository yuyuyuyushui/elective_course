<<<<<<< HEAD
import uuid, pickle
from conf import settings
class Nid:
    def __init__(self):
        self.nid = uuid.uuid4()
    def get_file(self):
        path = '%s\db\%s'%(settings.DIR_PATH, self.path)
        with open(path, 'rb') as f:
            return pickle.load(f)
class SchoolNid:
    def __init__(self):
        super(SchoolNid,self).__init__()
        self.path = 'school'
class CourseNid:
    def __init__(self):
        super(CourseNid,self).__init__()
        self.path = 'course'
class ClassesNid:
    def __init__(self):
        super(ClassesNid,self).__init__()
        self.path = 'classes'
=======
import uuid,os,pickle
from conf import settings
class Nid:
    def __init__(self):
        self.uid = uuid.uuid4()
    def find_obj(self):
        db_path = '%s\db'%(settings.DIR_PATH)
        for obj_path in os.path.exists(db_path):
            if self.uid == obj_path:
                path = '%s\%s'%(db_path,self.uid)
                return pickle.load(open(path,'rb'))
class ClassesNid(Nid):
    def __init__(self):
        super(Nid,self).__init__()
        self.path = 'classes'
class SchoolNid(Nid):
    def __init__(self):
        super(Nid,self).__init__()
        self.path = 'school'
class Teacher(Nid):
    def __init__(self):
        super(Nid,self).__init__()
        self.path = 'teacher'
class CourseNid(Nid):
    def __init__(self):
        super(Nid,self).__init__()
        self.path = 'course'
>>>>>>> 578f8a003368e03ef93a6070ae1feb9a1d9e9047
