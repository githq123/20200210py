from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')
    def post(self,request):
        form=ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("成功")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("失败")

