from db import db_handler

class BaseClass():

    def save(self):
        db_handler.save_file(self)

    @classmethod
    def read(cls, name):
        obj = db_handler.read_file(cls.__name__.lower(), name)  #cls表示类本身
        return obj

class Admin(BaseClass):
    def __init__(self,name,pwd):
        self.name=name
        self.pwd =pwd
        self.save()