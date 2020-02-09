from django.conf.urls import url
from django.urls import include

from apps.blogs import views

app_name='blogs'

urlpatterns=[
url(r'^articles', views.articles, name='articles'),
url(r'^blog1', views.blog1, name='blog1'),
url(r'^new', views.new_article, name='new'),
url(r'^edit/(?P<id>[0-9]+)$', views.edit_article, name='edit'),
url(r'^delete/(?P<article_id>[0-9]+)$', views.del_article, name='delete'),
url(r'^search', views.search, name='search'),
url(r'^detail/(?P<id>[0-9]+)$', views.article_page, name='detail')
]