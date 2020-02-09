from .models import User
# from django.contrib.auth.models import User
# get_response是个方法
def front_user_middleware(get_response):
    def middleware(request):
        # print("这里是request到达view之前的代码")
        user_id=request.session.get('user_id')
        if user_id:
            try:
                user=User.objects.get(pk=user_id)
                request.front_user=user
            except:
                request.front_user =None
        else:
            request.front_user = None

        response=get_response(request)#这是一个界限

        #之后是response对象到达浏览器
        # print("这里是response到达浏览器执行的代码")
        return response
    return middleware
