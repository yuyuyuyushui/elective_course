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