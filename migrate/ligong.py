from flask import Flask
import config
from exts import db

ligong=Flask(__name__)

ligong.config.from_object(config)#导入配置文件，需要from_object()方法
db.init_app(ligong)#将db与ligong进行绑定

@ligong.route('/')
def index():
    return '迁移脚本测试'

if __name__=="__main__":
    ligong.run()