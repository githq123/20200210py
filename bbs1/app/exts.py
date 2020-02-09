from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_migrate import Migrate
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class
from flask_login import LoginManager

bootstrap=Bootstrap()
db=SQLAlchemy()
mail=Mail()
migrate=Migrate(db=db)
moment=Moment()
photos=UploadSet('photos',IMAGES)

login_manager = LoginManager()


#将扩展库对象跟app进行绑定
def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app)
    moment.init_app(app)

    configure_uploads(app,photos)
    patch_request_class(app,size=None)

    # 登录管理初始化
    login_manager.init_app(app)

    # 登录站点设置
    login_manager.login_view = 'users.login'
    # 指定登录的提示信息
    login_manager.login_message = 'you must login before '
    # 设置session保护级别  none 不保护 basic基本的  strong强保护
    login_manager.session_protection = 'strong'