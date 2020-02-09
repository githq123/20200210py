#encoding:utf-8
from flask import Flask,render_template
from flask_script import  Manager
ligong=Flask(__name__)
manager=Manager(ligong)




@ligong.route('/')
def index():
    return render_template('test.html',username='abc')


@ligong.route('/course/')
def course():
    return render_template('course_detail.html',username='abc')

if __name__=='__main__':
    ligong.run(debug=True, port=5054, threaded=True, host='192.168.56.1')
    # manager.run()




#宏：将页面上重复的单独分离，和函数一样，但无返回值
#定义宏
#使用宏
#模板继承:一小部分不相同