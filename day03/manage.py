#encoding:utf-8
from flask import Flask,render_template
from flask_script import  Manager
from flask_bootstrap import Bootstrap
ligong=Flask(__name__)
manager=Manager(ligong)
bootstrap=Bootstrap(ligong)

@ligong.route('/')
def index():
    return render_template('index.html')

@ligong.errorhandler(404)
def page_not_found(e):
    return render_template('error.html')

@ligong.route('/statics/')
def statics():
    return render_template('statics.html')

if __name__=='__main__':
    ligong.run(debug=True, port=5054, threaded=True, host='192.168.56.1')
    # manager.run()