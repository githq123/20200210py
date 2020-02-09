from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from .models import User
from django.views.generic import View
from .forms import SignUpForm,SignInForm
from django.contrib import messages
# Create your views here.
def index(request):
    # users=User.objects.all()
    # for user in users:
    #      print(user)

    # user_id=request.session.get('user_id')
    # context={}
    # try:
    #     user =User.objects.get(pk=user_id)
    #     context['front_user']=user
    # except:
    #     pass

    if request.front_user:
        print(request.front_user.username)

    return render(request,'index.html')
class SignUpView(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('signup'))
class SignInView(View):
    def get(self,request):
        return render(request,'signin.html')
    def post(self,request):
        form=SignInForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id']=user.id
                return redirect(reverse('index'))
            else:
                messages.info(request,'用户名或密码错误')
                return redirect(reverse('signin'))
        else:
            errors=form.get_errors()
            for error in errors:
                messages.info(request,error)
            return redirect(reverse('signin'))

def logout(request):
    request.session.flush()
    return redirect(reverse('index'))
def blog(request):
    return render(request,'blog.html')
def video(request):
    return render(request,'video.html')