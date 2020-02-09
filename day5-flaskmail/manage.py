from flask import Flask,render_template,current_app
from flask_mail import Mail,Message
import os
from  threading import Thread
ligong=Flask(__name__)


#配置邮箱服务器
ligong.config['MAIL_SERVER']=os.environ.get('MAIL_SERVER','smtp.126.com')
ligong.config['MAIL_USERNAME']=os.environ.get('MAIL_USERNAME','gaohj66666@126.com')
ligong.config['MAIL_PASSWORD']=os.environ.get('MAIL_PASSWORD','zxasqw12')


#创建邮箱对象
mail=Mail(ligong)


def async_send_mail(app,msg):
    #发送邮件需要程序上下文  新线程没有，需手动创建
     with app.app_context():
         #发送文件
          mail.send(message=msg)


def send_mail(to,subject,template,**kwargs):
    #根据current_app获取当前实例
    app=current_app._get_current_object()
    #创建邮件发送对象
    msg=Message(subject=subject,recipients=to,sender=app.config['MAIL_USERNAME'])
    #浏览器查看邮件
    msg.html = render_template(template + '.html', **kwargs)
    #终端看到的内容
    msg.body=render_template(template+'.txt',**kwargs)
    #创建线程
    thr=Thread(target=async_send_mail,args=[app,msg])
    #启动线程
    thr.start()
    return thr

#封装邮件发送函数
#发送对象 主题 发送账户 用户查看时客户端or网页
# def send_mail(subject,to,template,**kwargs):
#     #创建邮件对象
#     msg=Message(subject=subject,recipients=[to],sender=ligong.config['MAIL_USERNAME'])
# #视图函数发送文件
#     msg.html=render_template(template+'.html',**kwargs)
#     msg.body=render_template(template+'.txt',**kwargs)
#     mail.send(message=msg)


@ligong.route('/')
def index():
    # msg=Message(subject='账户激活',recipients=['1424127615@qq.com'],sender=ligong.config['MAIL_USERNAME'])
    # #网页的结果
    # msg.html=render_template('activate.html',username='day5abc') #'<h1>你好,点击链接激活</h1>'
    # #客户端结果
    # msg.body=render_template('activate.txt',username='day5abc')#'你好,点击链接激活'
    # mail.send(message=msg)
    # send_mail('账户激活','1424127615@qq.com','activate',username='day5abc')
    # return '邮件发送成功'
     send_mail(['1424127615@qq.com'],'找回密码','activate',username="day5abc")
     return '邮件发送成功'

if __name__=="__main__":
    ligong.run(debug=True, port=5062, threaded=True, host='192.168.56.1')