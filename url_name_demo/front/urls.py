from django.urls import path
from . import views
app_name='front'
urlpatterns=[
    path('',views.index,name='index'),
    # path('login/', views.login,name='signin')
    path('fronttestname/', views.login,name='signin')

]