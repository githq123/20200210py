from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    context={
        # 'mytime':datetime(year=2019,month=6,day=12,hour=12,minute=55,second=20)
        'mytime':datetime(year=2019,month=6,day=13,hour=8,minute=55,second=20)
    }
    return render(request,'index.html',context=context)