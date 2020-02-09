# from django.shortcuts import render
# from .models import Book,BookOrder,Publisher,Author
# from django.http import HttpResponse
# from django.db.models import Avg,Count,Max,Min,Sum,F,Q
# from django.db import connection
# # Create your views here.
# def index():
#     result=Book.objects.aggregate(avg=Avg("price"))
#     print(result)
#     # print(result,query)#只有filter才能使用query查看orm
#     print(connection.queries)
#     return HttpResponse("获取所有图书平均价")
# def index1():
#     # 每本书销售的平均价格
#     result=Book.objects.aggregate(avg=Avg("bookorder__price"))
#     print(result)
#     print(connection.queries)
#     print("=="*50)
#
#     books  = Book.objects.annotate(avg=Avg("bookorder__price"))
#     for book in books:
#         print("%s:%s"%(book.name,book.price))
#     print(connection.queries)
#
#
#     return HttpResponse("获取每本图书平均价")
# def index3():
#     # result = Author.objects.aggregate(booknums=Count("id"))
#     # print(result)
#     # result1 = Author.objects.aggregate(email=Count("email",distinct=True))
#     # print(result1)
#     # print(connection.queries)
#     books=Book.objects.annotate(booknums=Count("bookorder"))
#     for book in books:
#         print("%s:%s"%(book.name,book.booknums))
#     print(connection.queries)
#     return HttpResponse("book表中一共多少本书")
# def index4(request):
#     # result=Author.objects.aggregate(max=Max('age'),min=Min('age'))
#     # print(result)
#     # print(connection.queries)
#     # return HttpResponse("最大值，最小值")
#
#     #获取每一本书售卖时价格最大值，最小值
#     books = Book.objects.annotate(max=Max('bookorder__price'), min=Min('bookorder__price'))
#     for book in books:
#       print("%s:%s:%s"%(book.name,book.max,book.min))
#     print(connection.queries)
#     return HttpResponse("最大值，最小值")
# def index5():
#     #数据库book_order新增create_time字段
#
#     # result=BookOrder.objects.aggregate(total=Sum('price'))
#
#     #所有图书销售总额
#
#     #每本书销售总额
#
#
#    #18年图书销售总额
#    # result1 = BookOrder.objects.filter(create_time__year=2018).aggregate(total=Sum('price'))
#
#    #每本书在2018销售总额
#    # result2 = BookOrder.objects.filter(bookorder__create_time__year=2018).annotate(total=Sum('price'))
#
#    return HttpResponse()
#
#
# def index6():
#     # 每个价格增加10元
#     Book.objects.update(price=F("price")+10)
#     return HttpResponse()
#
#
#
# def index7(request):
#     #获取价格大于100元 并且评分大于4.9
#     # books = Book.objects.filter(price__gte=100,rating__gte=100)
#    #  books=Book.objects.filter(Q(price__gte=100)&Q(rating__gte=100))
#    # for book in books:
#    #     print("%s:%s:%s"%(book.name,book.price,book.rating))
#    #
#    #  # books=Book.objects.filter(Q(price__gte=100)|Q(rating__gte=100))
#    #  # books=Book.objects.filter(Q(price__gte=100)&~Q(rating__gte=100))
#    #
#     return HttpResponse()


from django.shortcuts import render
from .models import Book, BookOrder, Publisher, Author
from django.http import HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum, F, Q
from django.db import connection


# Create your views here.
def index(request):
    # 获取所有图书定价的平均价
    # select price as avg
    result = Book.objects.aggregate(avg=Avg("price"))
    print(result)
    # print(result.query) #只有filter 才可以使用 query来查看orm最终执行的sql语句
    print(connection.queries)
    return HttpResponse("获取所有图书定价的平均价")


def index1(request):
    # 每一本书销售的平均价格
    # select price as avg
    result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    print(result)
    print(connection.queries)
    print("==" * 50)
    books = Book.objects.annotate(avg=Avg("bookorder__price"))
    for book in books:
        print("%s:%s" % (book.name, book.avg))
    print(connection.queries)
    return HttpResponse("每一本书销售的平均价格")


def index3(request):
    # book表中总共多少本书  作者表中总共多少不同的邮箱
    # books = Book.objects.aggregate(booknums=Count("id"))
    # print(books)
    # author = Author.objects.aggregate(email_nums=Count('email',distinct=True))
    # print(author)
    # print(connection.queries)

    books = Book.objects.annotate(book_numbers=Count("bookorder"))
    for book in books:
        print("%s:%s" % (book.name, book.book_numbers))
    print(connection.queries)
    return HttpResponse("book表中总共多少本书")


def index4(request):
    # result = Author.objects.aggregate(max=Max("age"),min=Min("age"))
    # print(result)
    # print(connection.queries)
    # 获取没一本书 售卖的时候 最大值 和最小值
    books = Book.objects.annotate(max=Max("bookorder__price"), min=Min("bookorder__price"))
    for book in books:
        print("%s:%s:%s" % (book.name, book.max, book.min))
    print(connection.queries)
    return HttpResponse("最大值最小值")


def index5(request):
    # 所有图书的销售总额
    result = BookOrder.objects.aggregate(total=Sum('price'))
    print(result)
    print(connection.queries)
    print("*" * 100)
    # 每一本书的销售总额
    books = Book.objects.annotate(total=Sum('bookorder__price'))
    for book in books:
        print("%s:%s" % (book.name, book.total))
    print(connection.queries)
    print("*" * 100)
    # 2018年度图书销售总额
    result = BookOrder.objects.filter(create_time__year=2018).aggregate(total=Sum('price'))
    print(result)
    print(connection.queries)
    print("*" * 100)
    # 每一本图书在2018年销售总额
    books = Book.objects.filter(bookorder__create_time__year=2018).annotate(total=Sum('bookorder__price'))
    for book in books:
        print("%s:%s" % (book.name, book.total))
    print(connection.queries)

    return HttpResponse("总额")


def index6(request):
    # 每一本书的售价增加10元钱
    Book.objects.update(price=F("price") + 10)
    print(connection.queries[-1])
    return HttpResponse("index6")


def index7(request):
    # 获取价格 大于100块钱 并且评分 大于4.9
    # books =Book.objects.filter(price__gte=100,rating__gte=4.9)
    # books =Book.objects.filter(Q(price__gte=100)&Q(rating__gte=4.9))
    # books =Book.objects.filter(Q(price__gte=100)|Q(rating__gte=4.9))
    books = Book.objects.filter(Q(price__gte=100) & ~Q(name__icontains='传'))
    for book in books:
        print("%s:%s:%s" % (book.name, book.price, book.rating))
    print(connection.queries[-1])
    return HttpResponse("qf")