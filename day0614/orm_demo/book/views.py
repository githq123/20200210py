from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.
# class Person(object):
#     username='ad'
#     age=18
#     height='181cm'
#
#
# p=Person()
def index(request):
    # # book=Book(name='test1',author="张三",price=100.1)
    # # book.save()
    # return HttpResponse("添加成功")

    # book=Book.objects.get(pk=1)
    # print(book)
    # return HttpResponse("查询成功")

    # book=Book.objects.filter(name="test1").first()
    # print(book)
    # return HttpResponse("查询成功")

    # book=Book.objects.get(pk=1)
    # book.delete()
    # return HttpResponse("删除成功")

    book=Book.objects.get(pk=1)
    book.price=200
    book.save()
    return HttpResponse("更新成功")


