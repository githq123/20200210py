from django.shortcuts import render,redirect,reverse
from .models import Article
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods,require_GET,require_POST
# Create your views here.
# 查  select  get
# 增  insert  post
# 删  delete  delete
# 改  update  put、patch


#返回所有的文章
#这个方法只是用来看 也就是只能允许你get 请求过来

# @require_http_methods(['GET','POST','PUT','DELETE'])
#@require_http_methods(['GET']) = @require_GET
@require_GET
def index(request):
    return HttpResponse("首页")

#添加文章
#1.先让用户看到文章添加页面    get
#2.用户通过表单将数据提交到 视图函数   post
@require_http_methods(['GET','POST'])
# @require_POST
def add_article(request):
    if request.method == 'GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        Article.objects.create(title=title,content=content,price=price)
        return redirect(reverse('index'))