from flask import current_app,flash
from flask_login import UserMixin
from app.exts import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .posts import Posts
#判断用户是否登录 以及匿名用户  用户模型要继承于它

class Users(UserMixin,db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(20),unique=True)
    password_hash=db.Column(db.String(128))
    email=db.Column(db.String(64),unique=True)
    confirmed=db.Column(db.Boolean,default=False)
    icon=db.Column(db.String(64),default='default.jpg')

    #通过backref反向访问posts属性
    posts=db.relationship('Posts',backref="user",lazy='dynamic')

    #添加收藏功能
    favorites=db.relationship('Posts',secondary='collections',backref=db.backref('useres',lazy='dynamic'),lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('密码不可读')

    @password.setter
    def password(self,password):
        self.password_hash=generate_password_hash(password)

    # 密码校验
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

     #生成token
    def generate_active_token(self,expires_in=3600):
        s=Serializer(current_app.config['SECRET_KEY'],expires_in=expires_in)
        return s.dumps({'id':self.id})
    #检测token
    @staticmethod
    def check_active_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        u = Users.query.get(data['id'])

        if not u:
            return False
        if not u.confirmed:
            u.confirmed = True
            db.session.add(u)
            db.session.commit()
        return True
    # 登录成功以后执行的回调函数
    @login_manager.user_loader
    def load_user(uid):
        return Users.query.get(int(uid))


     #判断用户是否收藏了
    def is_favorite(self,pid):
        #先获取所有收藏的博
          favorites=self.favorites.all()
          post=list(filter(lambda p:p.id==pid,favorites))
          if len(post)>0:
              return True
          return False


    #添加收藏
    def add_favorite(self,pid):
        p=Posts.query.get(pid)#先根据id查出来
        self.favorites.append(p)#然后追加到第三张表中

    def del_favorite(self,pid):
        p=Posts.query.get(pid)#先根据id查出来
        self.favorites.remove(p)#从第三张表中移除





