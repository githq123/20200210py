from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import render,redirect,reverse
# from django.contrib.auth.models import User
from django.http import HttpResponse
# from .models import Person
# from .models import UserExtension
from .models import User,Article
from .forms import LoginForm
from django.contrib.auth.models import ContentType,Permission,Group
# Create your views here.
def index(request):
     # user=User.objects.create_user(username='jxlg2',email='jxlg2@163.com',password='hq123123')#objects是UserManager
    # user=User.objects.create_superuser(username='jxlg1',email='jxlg1@163.com',password='hq123123')#objects是UserManager
    #  user.save()

    # user=User.objects.get(pk=1)
    # user.set_password('123qwe123')

    # username = 'jxlg'
    # password = 'hq123123'
    # user = authenticate(request, username=username, password=password)
    # if user:
    #     print('登录成功', user.username)
    # else:
    #     print('用户名或密码错误')
    #  return HttpResponse("OK")
    return render(request,'index.html')
# def proxys(request):
#     blacklists=Person.get_black_list()
#     for  blacklist in blacklists:
#         print(blacklist)
#     return HttpResponse("blacklist")
#


#
# def my_authenticate(telephone,password):
#     user=User.objects.filter(extension__telephone=telephone).first()
#     if user:
#         is_correct=user.check_password(password)#方法自带
#         if is_correct:
#             return user
#         else:
#             return None
#     else:
#         return None

#
#
# def one_view(request):
#    # user=User.objects.create_user(username='zhangsan',email='zhangsan@qq.com',password='zhangsan123')
#    # user.extension.telephone='13911111111'
#    # user.save()
#
#    # user=User.objects.create_user(username='lisi',email='lisi@qq.com',password='lisi123')
#    # user.extension.telephone='13922222222'
#    # user.extension.school='清华大学'
#    # user.save()
#
#    telephone=request.GET.get('telephone')
#    password=request.GET.get('password')
#    user=my_authenticate(telephone,password)
#    if user:
#        print("%s:验证成功"%user.username)
#    else:
#        print("验证失败")
#    return HttpResponse("一对一扩展模型")

def inherit(request):
    # telephone='13933333333'
    # password='jxlg123'
    # username='jxlg'
    # school='江西理工大学'
    # email='jxlg@qq.com'
    # user=User.objects.create_user(telephone=telephone,username=username,email=email,password=password,school=school)
    # user.save()
    # # user=authenticate(request,telephone='13933333333',password='jxlg123')
    # # if user:
    # #     print('验证成功')
    # # else:
    # #     print('验证失败')


    # telephone='13933333333'
    # password='jxlg123'
    # username='jxlg'
    # email='jxlg@qq.com'
    # user=User.objects.create_user(telephone=telephone,username=username,email=email,password=password)
    # user.save()
    user = authenticate(request, username='13933333333', password='jxlg123')
    if user:
        print('验证成功')
    else:
        print('验证失败')
    return  HttpResponse("模型继承")
def my_login(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        form=LoginForm(request.POST)
        if form.is_valid():
            telephone=form.cleaned_data.get('telephone')
            password=form.cleaned_data.get('password')
            remember=form.cleaned_data.get('remember')
            user=authenticate(request,username=telephone,password=password)

            if user and user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_url=request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponse("登录成功")
            else:
                return HttpResponse("手机号或密码错误")
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('login'))
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))


@login_required(login_url='/login/')
def profiles(request):
    return HttpResponse("我是个人中心，登录以后才可以查看")
def add_permissions(request):
    #获取模型对应的ContentTypeId
    content_type=ContentType.objects.get_for_model(Article)
    permission=Permission.objects.create(codename='black_article',name='拉黑文章',content_type=content_type)
    permission.save()
    return HttpResponse("权限创建成功")
def  operate_permission(request):
    user=User.objects.first()
    content_type=ContentType.objects.get_for_model(Article)
    permissions=Permission.objects.filter(content_type=content_type)

    for permission in permissions:
        print(permission)

    user.user_permissions.set(permissions)
    user.save()

    # user.user_permissions.clear()
    # user.user_permissions.remove(*permission)

    if user.has_perm('front.view_article'):
        print('拥有查看文章的权限')
    else:print('没有查看文章的权限')
    print(user.get_all_permissions())

    return HttpResponse("操作权限成功")
@permission_required(['front.view_article','front.add_article'],login_url='/login/',raise_exception=True)
def add_article(request):
    if request.user.is_authenticated:
        print('已经登录了')
        if request.user.has_perm('front.add_article'):
            return HttpResponse("添加文章的页面")
        else:
            return HttpResponse('您没有访问该页面的权限',status=403)
    else:
        return redirect(reverse('login'))

def operate_group(request):
    # group=Group.objects.create(name="运营")
    # content_type = ContentType.objects.get_for_model(Article)
    # permissions=Permission.objects.filter(content_type=content_type)
    # group.permissions.from_queryset(permissions)
    # group.save()

    # user=User.objects.first()
    # group=Group.objects.filter(name='运营').first()
    # user.groups.add(group)
    # user.save()

    # user = User.objects.first()
    # permissions=user.get_group_permissions()
    # print(permissions)

    user = User.objects.first()
    if user.has_perms(['front.view_article','front.black_article']):#先看自己有没有，再看分组有没有
        print("有查看文章  拉黑文章权限")
    else:
        print("没有有查看文章  拉黑文章权限")
    return HttpResponse("操作分组")