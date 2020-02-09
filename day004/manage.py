import os
from flask import Flask, render_template, request
from flask_script import Manager
from flask_uploads import UploadSet,IMAGES,configure_uploads,patch_request_class

app=Flask(__name__)
#设置上传文件大小
app.config['MAX_CONTENT_LENGTH']=1024*1024*8
#设置上传位置
app.config['UPLOADED_PHOTOS_DEST']=os.getcwd()
#创建上传对象，制定过滤的文件后缀
photos=UploadSet('photos',IMAGES)
#跟应用实例绑定
configure_uploads(app,photos)
#设置文件上传大小，默认64M，如果为none说明设置为自己设置的大小
patch_request_class(app,size=None)
@app.route('/uploads/',methods=['GET','POST'])
def uploads():
    img_url=''
    #如果请求方法是post而且文件已经选中
    if request.method=='POST' and 'photo' in request.files:
        filename=photos.save(request.files['photo'])

        #获取图片url
        img_url=photos.url(filename)
    return render_template('index.html',img_url=img_url)

manager=Manager(app)
if __name__=="__main__":
    app.run(debug=True, port=5060, threaded=True, host='192.168.56.1')
    #manager.run()