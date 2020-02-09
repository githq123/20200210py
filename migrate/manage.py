#encoding:utf-8
from flask_script import Manager
from ligong import ligong
from exts import db
from flask_migrate import Migrate,MigrateCommand
from models import User#导入model模型

manager=Manager(ligong)
Migrate(ligong,db)
manager.add_command("db",MigrateCommand)
#python manage.py db migrate
if __name__=="__main__":
    manager.run()
#python manage.py runserver