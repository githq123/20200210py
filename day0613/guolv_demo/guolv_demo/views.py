from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
def greet(word):
    return "hello world %s"%word

def index(request):
    context={
        'greet':greet
    }
    return render(request,'index.html',context=context)

def add_view(request):
    context={
        'v1':['1','2','3'],
        'v2':['4','5','6']
    }
    return render(request,'add.html',context=context)
def cut_view(request):
    return render(request,'cut.html')

def date_view(request):
    context={
        'today':datetime.now(),

    }
    return render(request,'date.html',context=context)