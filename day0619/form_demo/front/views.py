from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm,RegisterForm
from django.http import HttpResponse
from .models import User
from django.forms.utils import ErrorDict
# Create your views here.
class IndexView(View):
    def get(self,request,*args,**kwargs):
        form=MessageBoardForm()
        return render(request,'index.html',context={"form":form})
    def post(self,request):
        form=MessageBoardForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            content=form.cleaned_data.get('content')
            email=form.cleaned_data.get('email')
            reply=form.cleaned_data.get('reply')
            print("*"*80)
            print(title)
            print(content)
            print(email)
            print(reply)
            print("*" * 80)

            return HttpResponse("success")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("fail")

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            email = form.cleaned_data.get('email')
            User.objects.create(username=username,telephone=telephone,email=email)
            return HttpResponse("注册成功")
        else:
            # print(form.errors.get_json_data())
            print(form.get_errors())
            return HttpResponse("注册失败")