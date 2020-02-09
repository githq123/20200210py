from flask import Blueprint
#创建蓝本对象
book=Blueprint('book',__name__)

#添加视图函数

@book.route('/mingzhu/')
def mingzhu():
    return 'booktest'

@book.route('/classes/')
def register():
    return 'test'