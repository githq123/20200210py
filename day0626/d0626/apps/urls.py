from django.conf.urls import url

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet)
# router.register(r'movie', views.MovieViewSet)
router.register(r'game', views.GameViewSet)
# urlpatterns = [
#     url(r'movie/',views.MovieViewSet.as_view()),
#     url(r'^games/',views.GameViewSet.as_view(
#         actions={
#             "get":"list",#这个是查看所有的列表
#             "post":"create", #这是进行创建
#         }
#     )),
# url(r'^game/(?P<pk>\d+)/',views.GameViewSet.as_view(
#         actions={
#             "get":"retrieve", #根据id 获取相信信息
#             "put":"update" #更新
#         }
#     )),
# ]
