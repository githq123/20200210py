from django.shortcuts import render
from .models import Article,Category,Tag
from frontuser.models import FrontUser,UserExtension
from django.http import HttpResponse
# Create your views here.
def index(request):
    # category=Category(name="最火文章")
    # category.save()
    # article=Article(title="text文本1",content="hhhhhhh1")
    # article.category=category
    # article.save()

    article=Article.objects.first()
    print(article.category.name)

    return HttpResponse("SUCCESS")

def one_to_many_view(request):
    # article=Article(title="text文本2",content="hhhhhhh2")
    # category=Category.objects.first()
    # author=FrontUser(username="zhangsan")
    # author.save()
    # article.category=category
    # article.author=author
    # article.save()

    # category = Category.objects.first()
    # articles=category.article_set.all()#使用时删去related_name
    # for article in articles:
    #     print(article)

    # category=Category.objects.first()
    # articles=category.articles.all()
    # for article in articles:
    #     print(article)

    category=Category.objects.first()
    article=Article(title="text文本3",content="hhhhhh3")
    article.author=FrontUser.objects.first()#不需要额外保存
    category.articles.add(article,bulk=False)

    return HttpResponse("一对多SUCCESS")
def one_to_one_view(request):
    # user =FrontUser.objects.first()
    # extension=UserExtension(school="textschool")
    # extension.user=user
    # extension.save()

    # extension=UserExtension.objects.first()
    # print(extension.user)

    user=FrontUser.objects.first()
    print(user.extensions)

    return HttpResponse("一对一成功")

def many_to_many_view(request):
   # article=Article.objects.first()
   # tag=Tag(name="testname")
   # tag.save()
   # article.tag_set.add(tag)

   # article=Article.objects.first()
   # tag=Tag(name="testname1")
   # tag.save()
   # article.tags.add(tag)

   # tag=Tag.objects.get(pk=2)
   # article=Article.objects.get(pk=3)
   # tag.articles.add(article)

   article=Article.objects.get(pk=1)
   tags=article.tags.all()
   for tag in tags:
       print(tag)

   return HttpResponse("多对多成功")