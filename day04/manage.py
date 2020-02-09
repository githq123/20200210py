#encoding:utf-8
from flask import Flask, render_template, request, send_from_directory, url_for
from flask_script import  Manager
from flask_bootstrap import Bootstrap
#导入flask表单类
from flask_wtf import FlaskForm
#导入表单类型
from wtforms import StringField,PasswordField,SubmitField
#导入表单验证
from wtforms.validators import DataRequired,length,email,EqualTo
from datetime import datetime,timedelta
import os
from PIL import Image#PIL不支持Python.x需要使用pillow

ligong=Flask(__name__)
manager=Manager(ligong)
bootstrap=Bootstrap(ligong)
ligong.config['SECRET_KEY']='day4abc'
#配置 bootstrap使用本地css、js
ligong.config['BOOTSTRAP_SERVE_LOCAL']=True
#指定文件的上传位置
ALLOWED_EXTENSIONS=set(['jpg','png','gif','jpeg'])
#指定上传文件的大小
ligong.config['MAX_CONTENT_LENGTH']=1024*1024*8
ligong.config['UPLOAD_FOLDER']=os.getcwd()#获取当前目录


#定义表单类
@ligong.route('/uploads/',methods=['GET','POST'])
def uploads():
    img_url=''
    if request.method=='POST':
        file=request.files.get('photo')#获取文件
        if file and allow__file(file.filename):
            #获取文件后缀名
            suffix=os.path.splitext(file.filename)[1]
            print(suffix)
            filename=random_string()+suffix#获取文件名
            pathname=os.path.join(ligong.config['UPLOAD_FOLDER'],filename)
            file.save(pathname)
            #生成缩略图
           #打开文件
            img=Image.open(pathname)
        #重新设置尺寸
            img.thumbnail((128,128))
        #保存修改
            img.save(pathname)
            img_url=url_for('show_file',filename=filename)
    return  render_template('index.html',img_url=img_url)

#判断是否是允许的后缀名
def allow__file(filename):
    return  '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS
#生成随机字符串
def random_string(length=16):
    import random
    base_str='abcdefghijklmnopqrstuvwxyz1234567890'
    return  ''.join(random.choice(base_str) for i in range(length))

@ligong.route('/show_file/<filename>')
def show_file(filename):
    #send_from_directory表示安全发送文件
    return  send_from_directory(ligong.config['UPLOAD_FOLDER'],filename)


if __name__=='__main__':
    ligong.run(debug=True, port=5059, threaded=True, host='192.168.56.1')
    # manager.run()