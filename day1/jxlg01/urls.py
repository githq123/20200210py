from django.urls import path
from . import views
urlpatterns=[
    path('',views.book),# http://127.0.0.1:8000/book/
    path('detail/<book_id>/<category_id>/',views.books_detail())
    # http://127.0.0.1:8000/book/detail/2/3/
]