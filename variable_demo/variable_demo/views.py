from django.shortcuts import render

class Person(object):
    def __init__(self,username):
        self.username=username


def index(request):
    p=Person('zhangsan')

    # context={
    #     'person':p
    # }

    # context={
    #     'person':{
    #         'username':'lisi'
    #     }
    # }

    # context={
    #     'person':(
    #         'zhangsan',
    #         'lisi'
    #     )
    # }

    # return render(request,'index.html',context)
    # return render(request, 'index.html', context={'username':'testname'})

    # context={'age':20}
    # return render(request,'index.html',context)

    # context={
    #     'heros':[
    #         '乔丹','科比'
    #     ]
    # }
    # return render(request,'index.html',context=context)

    # context={
    #     'persons':{
    #         'username':'123',
    #         'age':18,
    #         'height':'121cm',
    #     }
    # }
    # return render(request, 'index.html', context=context)

    # context={
    #     #     'persons':[
    #     #         '水浒传','红楼梦','三国'
    #     #     ]
    #     # }
    #     # return render(request, 'index.html', context=context)

    # context={
    #     'comments':['very good'],
    #     'books':[{
    #         'name':'python',
    #         'author':'zhangsan',
    #         'price':200
    #     },{
    #         'name':'mysql',
    #         'author':'lisi',
    #         'price':100
    #     },{
    #         'name':'linux',
    #         'author':'wangwu',
    #         'price':200
    #     },{
    #         'name':'离散数学',
    #         'author':'zhangsan',
    #         'price':300
    #     },{
    #         'name':'javascripts',
    #         'author':'testname',
    #         'price':130
    #     }
    #
    #     ]
    # }
    # return render(request, 'index.html', context=context)

    # context={
    #     'persons':[
    #         'zhangsan',
    #         'lisi',
    #         'wangwu'
    #     ]
    # }
    # return render(request, 'index.html', context=context)


    context={
        "info":"<a href='http://www.91.com/'>91</a>",
        # "info":"<script><alert></script>"
    }

    return render(request, 'index.html', context=context)