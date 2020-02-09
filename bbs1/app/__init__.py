from flask import Flask,render_template
from app.config import config
from app.exts import config_extensions
from app.views import config_blueprint

#封装一个函数，专门用来创建app
def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name]
    config_extensions(app)
    #完成蓝本配置
    config_blueprint(app)
    return app

def config_errorhandler(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html')