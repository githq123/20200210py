from django.conf.urls import url
from rest_framework import routers

from . import views

app_name="cms"
# router = routers.DefaultRouter()
# router.register(r'blog', views.ArticleViewSet)

urlpatterns = [
    url(r'list/',views.ArticleList.as_view(),name='blog'),
    url(r'detail/(?P<pk>[0-9]+)$',views.ArticleDetail.as_view(),name='operate_blog'),
]