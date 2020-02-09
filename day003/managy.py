#encoding:utf-8
from flask import Flask, render_template, request
from flask_script import  Manager
from flask_bootstrap import Bootstrap
#导入类库
from flask_wtf import FlaskForm
#导入字段类型
from wtforms import StringField,PasswordField,SubmitField
#导入验证器类，保证合法数据
from wtforms.validators import DataRequired

ligong=Flask(__name__)
manager=Manager(ligong)
bootstrap=Bootstrap(ligong)
ligong.config['SECRET_KEY']='day3abc'


#定义表单类
class NameForm(FlaskForm):
    name=StringField('用户名',validators=[DataRequired()])
    password=PasswordField('密码')
    submit=SubmitField('提交')
@ligong.route('/login/',methods=['GET','POST'])
def index():
    form=NameForm()#实例化表单对象
    if request.method=='GET':
       return render_template('form.html',form=form)
    else:
        return "Hello%s"%request.form['name']



if __name__=='__main__':
    ligong.run(debug=True, port=5058, threaded=True, host='192.168.56.1')
    # manager.run()