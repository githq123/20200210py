import os
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app
from app.models import posts, Posts, Users
from app.exts import db

#创建app参数 为环境名称，在config中已经配置
app=create_app(os.environ.get('FLASK_CONFIG')or 'default')
manager=Manager(app)
manager.add_command('db',MigrateCommand)
# @manager.command
# def create_test_posts():
#     for x in range(1,255):
#         title='标题：%s'%x
#         content='内容：%s'%x
#         posts=Posts(title=title,content=content)
#         # users=Users.query.first()
#         # posts.uid=users
#         posts.uid=1
#         db.session.add(posts)
#         db.session.commit()
#     print("恭喜插入成功")

if __name__=="__main__":
    manager.run()