from flask import Flask, render_template, flash, get_flashed_messages, url_for, request, Blueprint, current_app,redirect
from app.exts import db
from app.models import Posts
from app.forms import PostForm
from flask_login import current_user

main=Blueprint("main",__name__)

@main.route('/',methods=['GET','POST'])
def index():
    return render_template('main/index.html')

