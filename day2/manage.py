from flask import  Flask,request,redirect,url_for,render_template
from flask_script import Manager
#导入其他蓝本
from user import user
from book import book


#ligong=Flask(__name__,template_folder='C:/Users/admin/PycharmProjects/day2/templates')
ligong=Flask(__name__)
#实例化Manage对象
manager=Manager(ligong)

#注册蓝本
ligong.register_blueprint(user,url_prefix='/user/')
ligong.register_blueprint(book,url_prefix='/book/')


#自动加载模板文件
#ligong.config['TEMPLATES_AUTO_RELOAD']=True


@ligong.route('/')
def index():
    #return 'hello world'
    #return render_template('hello.html')
    #return  render_template('test.html',name='abc',honey='123')
    # context={
    #     'username':'ABC',
    #     'age':19,
    #     'country':'China',
    #     'children':{
    #     'name':'abc',
    #     'age':4,
    #     'height':'100cm'
    # }
    # }
    context={
        'users':['A','B','C'],
        'person': {
                'name':'abc',
                'age':4,
                'height':'100cm'
            },
        'books':[
            {
                'name':'三国演义',
                'author':'罗贯中',
                'price':'110'
            },{
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': '110'
            },{
                'name': '水浒传',
                'author': '施耐庵',
                'price': '20'
            }
        ]
    }
    #return render_template('test.html',**context)
    return render_template('hello.html', **context)
@ligong.route('/welcome/<name>/')
def welcome(name):
    return 'hello%s'%name

@ligong.route('/index1/<int:uid>/')
def index1(uid):
    return 'hello%d号'%uid

# @ligong.route('/path/<path:p>/')
# def path(p):
#     return p

@ligong.route('/request1/',methods=['GET','POST'])
def request1():
    #返回完整url地址
    #return request.url
    #返回
    #return request.base_url
    # return request.host_url
    #return request.path
    #return request.remote_addr
    #return request.method
    #return request.args['name']
    #获取请求头信息
    return request.headers['User-Agent']


@ligong.route('/redirect/')
def old():
     #return redirect('/new/')
     # return url_for('welcome',name='xiaoming')#返回指定路径
     return redirect(url_for('welcome', name='xiaoming'))


@ligong.route('/new/')#变动
def new():#不变
    return '这是新的内容'



# @ligong.route('/response/')
# def response():
#     return 'ok'


#2成功3跳转4客户端错误（未找到）5服务器错误（代码、请求）

if  __name__=='__main__':
    ligong.run(debug=True,port=5067,threaded=True,host='192.168.56.1')
    #manager.run()#cmd运行