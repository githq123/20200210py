from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import make_aware

from  .models import Book,Article,Category
from django import urls
# Create your views here.
def index(request):
    print(type(Book.objects))
    return HttpResponse("index")
def index1(request):
    # book=Book.objects.filter(name__exact="发展史1")
    book=Book.objects.filter(name__iexact="发展史1")#不区分大小写
    print(book.query)
    print(book)
    return HttpResponse("index1")
def index2(request):
    book=Book.objects.filter(name__contains="史1")
    print(book.query)
    print(book)
    return HttpResponse("index2")

def index3(request):
    articles=Article.objects.filter(id__in=[1,2,3,4])
    for article in articles:
        print(article)
    categories=Category.objects.filter(articles__in=[1,2,3,4])
    for category in categories:
        print(category)
    print(categories.query)

    return HttpResponse("index3")
def index4(request):
    articles=Article.objects.filter(id__gte=2)
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse("index4")

def index5(request):
    start_time=make_aware(datetime(year=2019,month=1,day=23,hour=12,minute=35,second=33))
    end_time=make_aware(datetime(year=2059,month=1,day=23,hour=12,minute=35,second=33))
    articles=Article.objects.filter(create_time__range=(start_time,end_time))
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse("index5")
def index6(request):
    categories=Category.objects.filter(articles__title__contains="发展")#related_name
    for category in categories:
        print(category)
    print(categories.query)
    return HttpResponse("index6")
def index7(request):
    # article=Article.objects.filter(create_time__isnull=False)#时间不为空
    articles=Article.objects.filter(title__iregex=r"^hello")#正则表达式
    for article in articles:
        print(article)
    print(articles.query)
    return HttpResponse("index7")















