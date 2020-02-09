from django.http import HttpResponse
# Create your views here.

def book(request):
    return HttpResponse('江西理工test文本')

def book_detail(request):
    book_id=request.GET['id']
    text="您要找的图书id是 %s" % book_id
    return HttpResponse(text)
def books_detail(request,book_id,category_id):
    text = "您要找的图书id是 %s 图书的分类是 %s" %(book_id,category_id)
    return HttpResponse(text)