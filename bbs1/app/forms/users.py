from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,Email,ValidationError
from flask_wtf.file import FileField,FileAllowed,FileRequired
from app.exts import photos
from app.models import Users

#用户注册表单
class RegisterForm(FlaskForm):
    username=StringField('用户名',validators=[DataRequired(),Length(3,10,message="用户名必须在6-20之间")])
    email=StringField('Email',validators=[Email(message="请写正确的邮箱")])
    password=StringField('密码',validators=[DataRequired(),Length(6,20,message="密码必须在6-20之间")])
    confirm=StringField('确认密码',validators=[EqualTo('password',message="两次密码必须一致")])
    submit=SubmitField('立即注册')

     #自定义验证函数
    def validate_username(self,filed):
        if Users.query.filter_by(username=filed.data).first():
            raise ValidationError("该用户名已经注册")
    def validate_email(self,filed):
        if Users.query.filter_by(email=filed.data).first():
            raise ValidationError("该用户名已经注册")


class LoginForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired()])
    password = PasswordField('密码',validators=[DataRequired()])
    remember = BooleanField('记住我')
    submit =  SubmitField("立即登录")

class UploadedForm(FlaskForm):
   icon=FileField('头像',validators=[FileRequired('请选择文件'),FileAllowed(photos,message="只能选择图片")])
   submit=SubmitField("上传图片")

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('原密码', validators=[DataRequired()])
    new_password = StringField('密码', validators=[DataRequired(), Length(6, 20, message="密码必须在6-20之间")])
    confirm_new = StringField('确认密码', validators=[EqualTo('new_password', message="两次密码必须一致")])
    submit = SubmitField('修改密码')
