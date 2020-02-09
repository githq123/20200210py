from django.conf.urls import url
from django.urls import include

from apps.users import views

app_name='users'

urlpatterns = [
    url(r'^register', views.RegisterView.as_view(), name='register'),
    # 发送短信验证
    url(r'^send_message$', views.send_message, name='send_message'),
    url(r'^login', views.LoginView.as_view(),name='login'),
    url(r'^logout', views.logout,name='logout'),
    url(r'^img', views.ImgView.as_view(),name='img'),
    url(r'^reset_passwords', views.reset_passwords,name='reset_passwords'),

]

