from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.
def index(request):
    username=request.GET.get('username')
    if username:
       return HttpResponse("前台首页")
    else:
       # login_url=reverse('front:login')+"?next=/"
       login_url=reverse('front:detail',kwargs={"article_id":1,"p":6})
       print("="*50)
       print(login_url)
       print("="*50)
       return redirect(login_url)
       # return redirect(reverse('front:login'))
def login(request):
    return HttpResponse("登录首页")

def article_detail(request,article_id,p):
    text="您要查看的文章详情id是：%s,第%s页"%(article_id,p)
    return HttpResponse(text)