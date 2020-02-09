from django.shortcuts import render, reverse, redirect
from django.http import JsonResponse
from .models import User
from django.views.generic import View
from .forms import LoginForm, RegisterForm, ImgForm
from django.contrib import messages
import random
import requests

# Create your views here.
def index(request):
    return render(request, 'users/index.html')
def admin(request):
    return render(request, 'cms/admin.html')
class RegisterView(View):
    def get(self, request):
        return render(request, 'users/Register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')
            is_superuser = form.cleaned_data.get('is_superuser')
            code = form.cleaned_data.get('code')
            if code == request.session['captcha']:
                if is_superuser:
                    user = User.objects.create_superuser(telephone=telephone, username=username, email=email,
                                                         password=password)
                    user.save()
                else:
                    user = User.objects.create_user(telephone=telephone, username=username, email=email,
                                                    password=password)
                    user.save()
                return redirect(reverse('users:login'))
            else:
                print(form.errors.get_json_data())
                return redirect(reverse('users:register'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('users:register'))


def my_authenticate(telephone, password):
    user = User.objects.filter(telephone=telephone).first()
    if user:
        is_correct = user.check_password(password)  # 方法自带
        if is_correct:
            return user
        else:
            return None
    else:
        return None
def my_authenticate1(telephone, password):
    user = User.objects.filter(telephone=telephone).first()
    if user:
        if user.is_superuser:
            is_correct = user.check_password(password)  # 方法自带
            if is_correct:
               return user
            else:
               return None
        else:
           return None
    else:return None
class LoginView(View):
    def get(self, request):
        return render(request, 'users/Login.html')
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            is_superuser = form.cleaned_data.get('is_superuser')
            if is_superuser:
               user = my_authenticate1(telephone=telephone, password=password)
               if user:
                   request.session['user_id'] = user.uid
                   return redirect(reverse('admin'))
               else:
                   messages.info(request, '手机号或密码或用户类型错误')
                   return redirect(reverse('users:login'))
            else:
               user=my_authenticate(telephone=telephone, password=password)
               if user:
                   request.session['user_id'] = user.uid
                   return redirect(reverse('index'))
               else:
                   messages.info(request, '手机号或密码或用户类型错误')
                   return redirect(reverse('users:login'))
        else:
            errors = form.get_errors()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('users:login'))

class ImgView(View):
    def get(self, request):
        return render(request, 'users/Img.html')

    def post(self, request):
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        request.front_user = user
        form = ImgForm(request.POST, request.FILES)

        if form.is_valid():
            img = form.cleaned_data["img"]
            request.front_user.img = img
            request.front_user.save()
            return redirect(reverse('index'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('users:img'))

def send(telephone, captcha):
    url = 'http://v.juhe.cn/sms/send'
    params = {
        "mobile": telephone,  # 手机号
        "tpl_id": "167859",  # 模板id
        "tpl_value": "#code#=" + captcha,
        "key": "5f087912e36560739c20cd5e95f08b3b"  # AppKey
    }
    response = requests.get(url, params=params)
    result = response.json()
    print(result)
    if result['error_code'] == 0:
        return True
    else:
        return False


def send_message(request):
    telephone = request.GET.get('telephone')
    print(telephone)
    if telephone:
        captcha = ''
        for i in range(6):
            i = random.randint(0, 9)
            captcha += str(i)
        print(captcha)
        rs = send(telephone, captcha)
        if rs:
            request.session['captcha'] = captcha
            return JsonResponse({'ok': 1, 'code': 200})
        else:
            return JsonResponse({'ok': 0, 'code': 500, 'msg': '短信验证码发送失败'})
    else:
        return JsonResponse({'ok': 0, 'code': 500, 'msg': '请输入正确格式手机号'})


def reset_passwords(request):
    request.session.flush()
    return render(request, 'users/reset_passwords.html')


def logout(request):
    request.session.flush()
    return redirect(reverse('users:login'))
