from django.http import HttpResponse
from datetime import datetime,timedelta
from django.utils.timezone import make_aware

def index(request):
    #key_cookie的key
    #value_cookie的值
    #max_age 最长的生命周期，单位是秒
    #expires 过期时间，同时设置max_length，以expires为准
    #path 对域名下那个路径有效
    #domain对那个域名有效
    #secure是否是安全的，如果是true,只能是https协议的
    #httponly  如果为true 只能通过页面访问，不能通过ajax
    response=HttpResponse('index')
    expires=datetime(year=2019,month=6,day=22,hour=20,minute=30,second=40)
    expires=make_aware(expires)
    # response.set_cookie('user_id','zhangshan',expires=expires,max_age=180)
    response.set_cookie('user_id','zhangshan',expires=expires,max_age=180,path='/cms/')
    return response

def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('user_id')
    return response
def cms_cookie(request):
    cookies=request.COOKIES
    username=cookies.get('user_id')
    return HttpResponse(username)
def my_cookie(request):
    cookies=request.COOKIES
    username=cookies.get('user_id')
    return HttpResponse(username)
def session_view(request):

    # expires = datetime(year=2019, month=6, day=22, hour=20, minute=30, second=40)
    # expires = make_aware(expires)
    # expiry=timedelta(days=2)
    # request.session.set_expiry(0)0 none int -1

    request.session['username']='zhangsan'
    request.session.pop()
    request.session['age'] = '18'

    return HttpResponse("session view")
def get_session(request):
    username=request.session.get('username')
    print(username)
    return HttpResponse("get session view")
def log_out(request):
    request.session.clear_expired()
    return HttpResponse("clear")