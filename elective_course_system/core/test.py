import pickle,os,uuid
uui = uuid.uuid4()
dir_path = os.path.dirname(os.path.abspath(__file__))
dir_path = '%s\%s\%s'%(dir_path,'db',uui)
with open(dir_path,'wb') as f:
    pickle.dump('sss', f)