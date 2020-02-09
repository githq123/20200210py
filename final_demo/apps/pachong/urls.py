from django.conf.urls import url
from . import views

app_name = 'pachong'

urlpatterns = [
    url('^index/', views.detail, name='pachong_index'),
    # path('show_detail/', views.detail, name='show_detail'),
    url('^spider/', views.position_spider, name='position_spider'),
]