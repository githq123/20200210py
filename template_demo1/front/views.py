from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    # html=render_to_string('index1.html')
    # return HttpResponse(html)
    return render(request,'index1.html')