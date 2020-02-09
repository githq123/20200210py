from django.urls import re_path
from  . import views
app_name="retest"
urlpatterns=[

    re_path(r'^$',views.article),
    # re_path('list/<year>',views.article_list),
    # re_path('list/<month>',views.article_list)
    re_path(r'^list/(?P<year>\d{4})/',views.article_list),
    re_path(r'^list/(?P<month>\d{2})/',views.article_list_month)
]