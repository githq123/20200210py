from django.urls import path
from . import  views
app_name='article'
urlpatterns=[
    path('',views.index,name='index'),
    path('one_many/',views.one_to_many_view,name='one_many'),
    path('one_one/',views.one_to_one_view,name='one_one'),
    path('many_many/',views.many_to_many_view,name='many_many'),
]