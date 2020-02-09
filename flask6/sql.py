from sqlalchemy import create_engine,Column,Integer,FLOAT,BOOLEAN,DECIMAL,String,ForeignKey,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import  sessionmaker,relationship

HOSTNAME='127.0.0.1'
PORT='3306'
DATABASE='jiangxiligong'
USERNAME='root'
PASSWORD='123456'
DB_URI='mysql+pymysql://{username}:{password}@{host}: {port}/{db}'.format(
    username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

engine=create_engine(DB_URI)
Base=declarative_base(engine)

session=sessionmaker(engine)()#实例化类

#一对一，一对多，多对多
#用户表--父表（主表），文章表（从表）
class User(Base):#继承Base类
    __tablename__='user'
    id=Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    username=Column(String(20),nullable=False)
    def __repr__(self):
        return "User:(username:%s)"%(self.username)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content=Column(Text,nullable=False)
    uid=Column(Integer,ForeignKey("user.id"))

    author=relationship("User",backref="users")
    def __repr__(self):
        return "Article:(title:%s,content:%s)"%(self.title,self.content)

Base.metadata.drop_all()
Base.metadata.create_all()

user1=User(username="day6abc")
session.add(user1)
session.commit()

article1=Article(title="javaday6",content="mysqlday6",uid=1)
session.add(article1)
session.commit()

article=session.query(Article).first()
uid=article.uid
print(article)

user=session.query(User).get(uid)
print(user)