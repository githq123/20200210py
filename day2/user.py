from flask import Blueprint
#创建蓝本对象
user=Blueprint('user',__name__)

#添加视图函数

@user.route('/login/')
def login():
    return '欢迎光临'

@user.route('/register/')
def register():
    return '欢迎光临'