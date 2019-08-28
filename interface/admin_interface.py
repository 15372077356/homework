from db import model

def register_interface(username, pwd):
    obj = model.Admin.read(username)
    if obj:
        return '用户名已经被使用'

    model.Admin(username,pwd)
    return '注册成功'