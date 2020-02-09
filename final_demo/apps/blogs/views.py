from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from apps.users.models import User
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator
from django.contrib.auth.models import ContentType,Permission
from django.db.models import Q
#主页
# def articles(request):
#     # 查询列表页面，获取Article的所有信息
#     articles = Article.objects.all()
#     # 这里是取所有，如果取某一个article = models.Article.objects.get(pk=1)
#     paginator = Paginator(articles, 5)
#     # 获取 url 中的页码
#     page = request.GET.get('page')
#     # 将导航对象相应的页码内容返回给 articles
#     articles = paginator.get_page(page)
#     return render(request, 'blogs/articles.html', {'articles': articles})

def articles(request):
    # 根据GET请求中查询条件
    # 返回不同排序的对象数组
    if request.GET.get('order') == 'total_views':
        articles = Article.objects.all().order_by('-total_views')
        order = 'total_views'
    else:
        articles = Article.objects.all()
        order = 'normal'

    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    print(page)
    articles = paginator.get_page(page)

    # 修改此行
    context = {'articles': articles, 'order': order}

    return render(request, 'blogs/articles.html', context)


def blog1(request):
    # 查询列表页面，获取Article的所有信息
    articles = Article.objects.all()
    # 这里是取所有，如果取某一个article = models.Article.objects.get(pk=1)
    paginator = Paginator(articles, 5)
    # 获取 url 中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 articles
    articles = paginator.get_page(page)
    return render(request, 'blogs/blog1.html', {'articles': articles})



#展示页面
def article_page(request, id):
    # 取出相应的文章
    article = Article.objects.get(id=id)
    # 需要传递给模板的对象
    article.total_views += 1
    article.save(update_fields=['total_views'])
    context = {'article': article}
    # 载入模板，并返回context对象
    return render(request, 'blogs/article_page.html', context)

# 添加页面
def new_article(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存数据，但暂时不提交到数据库中
            new_article = article_post_form.save()
            new_article.save()
            # 完成后返回到文章列表
            return redirect(reverse('blogs:articles'))
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticleForm()
        # 赋值上下文
        context = { 'article_post_form': article_post_form }
        # 返回模板
        return render(request, 'blogs/new_article.html', context)

# # 编辑修改页面
def edit_article(request, id):
    # 获取需要修改的具体文章对象
    article = Article.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、text数据并保存
            article.title = request.POST['title']
            article.text = request.POST['text']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            return redirect(reverse('blogs:articles'), id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")

    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticleForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        # 将响应返回到模板中
        return render(request, 'blogs/edit_article.html', context)

#删除页面
def del_article(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect(reverse('blogs:articles'))
    return render(request, 'blogs/del_article.html', {'article_id': article_id})

def search(request): #article_date_added):
    search = request.GET.get('search')
    order = request.GET.get('order')
    # 用户搜索逻辑
    if search:
        if order == 'total_views':
            # 用 Q对象 进行联合搜索
            article_list = Article.objects.filter(
                Q(title__icontains=search) |
                Q(text__icontains=search)
            ).order_by('-total_views')
        else:
            article_list = Article.objects.filter(
                Q(title__icontains=search) |
                Q(text__icontains=search)
            )
    else:
        # 将 search 参数重置为空
        search = ''
        if order == 'total_views':
            article_list = Article.objects.all().order_by('-total_views')
        else:
            article_list = Article.objects.all()

    paginator = Paginator(article_list, 3)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    # 增加 search 到 context
    context = {'articles': articles, 'order': order, 'search': search}

    return render(request, 'blogs/search.html', context)
