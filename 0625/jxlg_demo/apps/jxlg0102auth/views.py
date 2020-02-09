from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.core.cache import cache
from .forms import LoginForm
from django.views.decorators.http import require_POST
from utils import restful
# Create your views here.
# def img_captcha(request):
#     text,image='zhangsan'
#     cache.set(text.lower(),text.lower(),5*60)
#     pass

@require_POST
def login_view(request):
    form=LoginForm(request.POST)
    if form.is_valid():
        telephone=form.cleaned_data.get('telephone')
        password=form.cleaned_data.get('telephone')
        remember=form.cleaned_data.get('remember')
        user =authenticate(request,username=telephone,password=password)
        if user:
            if user.is_active:
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                return restful.ok()
            else:
                return restful.unauth(message="您的账户已经被冻结")
        else:
            return restful.params_error(message="手机号或密码错误")
    else:
        errors=form.get_errors()
        return restful.params_error(message=errors)