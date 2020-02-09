from  flask import Flask
from   flask_sqlalchemy import  SQLAlchemy

ligong=Flask(__name__)
HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='jiangxiligongdaxue'
USERNAME='root'
PASSWORD='123456'
DB_URI='mysql+pymysql://{username}:{password}@{host}: {port}/{db}'.format(
    username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

ligong.config['SQLALCHEMY_DATABASE_URI']=DB_URI
ligong.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True#False
db=SQLAlchemy(ligong)

#用户表--父表（主表），文章表（从表）
class User(db.Model):#继承Base类
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    username=db.Column(db.String(20),nullable=False)
    def __repr__(self):
        return "User:(username:%s)"%(self.username)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content=db.Column(db.Text,nullable=False)
    uid=db.Column(db.Integer,db.ForeignKey("user.id"))

    author=db.relationship("User",backref="articles")
    def __repr__(self):
        return "Article:(title:%s,content:%s)"%(self.title,self.content)

db.drop_all()
db.create_all()
user=User(username="qianfeng")
article=Article(title="phptest",content="开发")
article.author=user

db.session.add(article)
db.session.commit()

# users=User.query.order_by(User.id.desc()).all()
# print(users)
# users=User.query.order_by(User.id.desc()).first()
# print(users)
# users=User.query.order_by(User.id.desc()).first()
# users.username="day6abc"
#  db.session.commit()
users=User.query.order_by(User.id.desc()).first()
db.session.delete(users)
db.session.commit()

@ligong.route('/')
def index():
    return 'day6测试文本'


if __name__=="__main__":
    ligong.run(debug=True, port=5062, threaded=True, host='192.168.56.1')