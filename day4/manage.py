#encoding:utf-8
from flask import Flask, render_template, request,session,flash,get_flashed_messages
from flask_script import  Manager
from flask_bootstrap import Bootstrap
#导入flask表单类
from flask_wtf import FlaskForm
#导入表单类型
from wtforms import StringField,PasswordField,SubmitField
#导入表单验证
from wtforms.validators import DataRequired,length,email,EqualTo
from flask_moment import  Moment
from datetime import datetime,timedelta


class NameForm(FlaskForm):
    name=StringField('用户名',validators=[DataRequired(),length(min=6,max=16)])
    email=StringField('Email',validators=[email()])
    password=PasswordField('密码',validators=[DataRequired(),length(min=6,max=16),EqualTo('confirm')])
    confirm=StringField('确认密码')
    submit=SubmitField('提交')

ligong=Flask(__name__)
manager=Manager(ligong)
bootstrap=Bootstrap(ligong)
ligong.config['SECRET_KEY']='day4abc'
#配置 bootstrap使用本地css、js
ligong.config['BOOTSTRAP_SERVE_LOCAL']=True
moment=Moment(ligong)
#定义表单类

@ligong.route('/registers/',methods=['GET','POST'])
def registers():
    # form = NameForm()  # 实例化表单对象
    # if request.method == 'GET':
    #     return render_template('index.html', form=form)
    # else:
    #     return "Hello %s,您的邮箱是：%s,您的密码是：%s" % (request.form['name'],request.form['email'],request.form['password'])
    form=NameForm()
    #表单校验
    if form.validate_on_submit():
        last_name=session.get('name')
        if last_name and last_name!=form.name.data:
            flash('名称不能经常换')
            flash('签名要常换')
        session['name']=form.name.data
    name=session.get('name')
    return  render_template('index.html',form=form,name=name)
@ligong.route('/moments/')
def moments():
    #current_time = datetime.utcnow() + timedelta(seconds=-3600)  # 这是显示当前的时间
    current_time=datetime.utcnow()+timedelta(seconds=-100)#这是显示当前的时间
    return render_template('moments.html',current_time=current_time)

if __name__=='__main__':
    ligong.run(debug=True, port=5058, threaded=True, host='192.168.56.1')
    # manager.run()