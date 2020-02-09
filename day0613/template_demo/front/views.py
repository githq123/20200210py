from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        "username":"123"
    }
    return render(request,'index.html',context=context)

def company(request):
    return render(request, 'company.html')

def school(request):
    return render(request, 'school.html')