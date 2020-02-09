from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError


class PostForm(FlaskForm):
    title=StringField('标题',validators=[DataRequired(),Length(6,30,message="6-30")])
    content=TextAreaField("内容",render_kw={'placeholder':'此时此刻...'},validators=[DataRequired(),Length(3,140,message="3-140")])
    submit=SubmitField("发表")
