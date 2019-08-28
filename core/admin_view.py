from  interface import admin_interface,common_interface

user_info = {'username':None}

def login():
    print('欢迎登录')
    username =input('请输入你的用户名>>>')
    pwd =input('请输入你的密码>>>')

    flag,msg = common_interface.login_interface(username,pwd,'admin')
    print(msg)

    if flag:
        user_info['username'] = username
        return True

def register():
    print('欢迎注册')
    username = input('请输入你的用户名>>>')
    pwd = input('请输入你的密码>>>')

    msg = admin_interface.register_interface(username, pwd)
    print(msg)

def run():
    func_dic= {
        '1':login,
        '2':register,
    }
    while True:
        print('''
        1:登录
        2:注册
        ''')
        choice = input('请选择你需要的功能,输入q退出>>>').strip()
        if choice == 'q':
            break
        if choice not  in func_dic:
            print('请重新输入')
            continue
        func_dic[choice]()

