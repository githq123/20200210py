import os

from flask import Flask, render_template, flash, get_flashed_messages, url_for, request, redirect, Blueprint,current_app
from sqlalchemy import or_

from app.exts import db,photos
from app.forms import RegisterForm,UploadedForm,LoginForm,ChangePasswordForm,PostForm
from app.email import send_mail
from app.models import Users,Posts
from flask_login import login_user,logout_user,login_required,current_user
from PIL import Image
from flask_paginate import Pagination, get_page_parameter

users=Blueprint("users",__name__)

@users.route('/register/',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
       u=Users(
           username=form.username.data,
           password=form.password.data,
           email=form.email.data )
       db.session.add(u)
       db.session.commit()
       token=u.generate_active_token()
       send_mail(u.email,"激活用户",'mail/activate',username=u.username,token=token)
       flash("账户注册成功")
       return redirect(url_for('main.index'))
    return  render_template('user/register.html',form=form)

@users.route('/activate/<token>/')
def activate(token):
    if Users.check_active_token(token):
        flash('该账户已经激活')
        return redirect(url_for('users.login'))
    else:
        flash('账户激活失败')
        return redirect(url_for('main.index'))

@users.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = Users.query.filter_by(username=form.username.data).first()
        if not u:
            flash("无效的用户名")
        elif not u.confirmed:
            flash("用户尚未激活,请激活以后再登录")
        elif u.verify_password(form.password.data):
            login_user(u, remember=form.remember.data)
            flash("登录成功")
            return redirect(request.args.get('next') or url_for("main.index"))
        else:
            flash("无效密码")
    return render_template('user/login.html',form=form)


## 退出登录
@users.route('/logout/')
def logout():
    logout_user() #重点
    flash("您已退出登录")
    return redirect(url_for("main.index"))

@users.route('/change_icon/',methods=['GET','POST'])
@login_required
def change_icon():
    form = UploadedForm()
    img_url=''
    if form.validate_on_submit():
        suffix=os.path.splitext(form.icon.data.filename)[1]
        filename=random_string()+suffix
        photos.save(form.icon.data,name=filename)
        #生成缩略图
        pathname=os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],filename)
        img=Image.open(pathname)
        img.thumbnail((128,128))
        img.save(pathname)
        if current_user.icon !='default.jpg':
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon))
        current_user.icon=filename
        db.session.add(current_user)
        db.session.commit()
        flash("头像已经保存")
        return redirect(url_for('users.change_icon'))
    img_url=photos.url(current_user.icon)
    return render_template('user/change_icon.html',form=form,img_url=img_url)

def random_string(length=16):
    import random
    base_str='qwertyuioplkjhgfdsazxcvbnm0987654321'
    return ''.join(random.choice(base_str) for i in range(length))


@users.route('/change_pwd/',methods=['GET','POST'])
@login_required
def change_pwd():
    form=ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password=form.new_password.data
            db.session.add(current_user)
            db.session.commit()
            flash("修改密码成功")
            return redirect(url_for('main.index'))
        else:
            flash("修改失败")
    return render_template('user/change_pwd.html',form=form)

@users.route('/blog1',methods=['GET','POST'])
@login_required
def blog1():
    form = PostForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            # 获取当前登录的用户
            u = current_user._get_current_object()
            p = Posts(title=form.title.data, content=form.content.data, user=u)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('users.blog1'))
        else:
            flash("请先登录")
            print(form.errors)
            return redirect(url_for('users.login'))
    page = request.args.get('page', 1, type=int)
    pagination = Posts.query.filter_by(rid=0).order_by(Posts.timestamp.desc()).paginate(page, per_page=5,error_out=False)
    posts = pagination.items
    return  render_template('user/blog1.html', form=form, posts=posts,pagination=pagination)


@users.route('/user1',methods=['GET','POST'])
@login_required
def user1():
        posts = Users.query.all()
        return  render_template('user/user1.html',posts=posts)

@users.route('/blog2',methods=['GET','POST'])
@login_required
def blog2():
    qu = request.args.get('q')
    page = request.args.get('page', 1, type=int)
    pagination = Posts.query.filter(or_( Posts.title==qu, Posts.content==qu)).paginate(page, per_page=5,error_out=False)
    posts=pagination.items
    return render_template('user/blog2.html', posts=posts,pagination=pagination)

