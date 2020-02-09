from django.shortcuts import render
from .models import Article,Category,Tag
from django.http import HttpResponse
from frontuser.models import FrontUser
# Create your views here.
def index(request):
    # category=Category(name="test目录1")
    # category.save()
    # article=Article(title="title1",content="content1")
    # article.category=category
    # article.save()
    article=Article.objects.first()
    print(article.category.name)
    return HttpResponse("SUCCESS")

def one_to_many(request):
    users=FrontUser(username="zhangsan")
    users.save()
    article=Article(title="title2",content="content2")
    category =Category.objects.first()
    article.category=category
    article.author=users
    article.save()
    return HttpResponse("SUCCESS")