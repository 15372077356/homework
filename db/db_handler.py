import os
import pickle
from conf import settings

def save_file(obj):

    classify = obj.__class__.__name__.lower()
    dir = os.path.join(settings.DB_PATH,classify)
    if not os.path.exists(dir):
        os.mkdir(dir)

    filename = os.path.join(dir,obj.name)

    with open(filename,'wb') as fw:
        pickle.dump(obj,fw)

def read_file(classify,name):

    filename = os.path.join(settings.DB_PATH,classify,name)
    if not os.path.exists(filename):
        return False

    with open(filename,'rb') as fr:
        obj =pickle.load(fr)
    return obj