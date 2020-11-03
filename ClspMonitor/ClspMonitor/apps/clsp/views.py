from django.shortcuts import render
import os
from django.views.generic import View
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from clsp import models
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.


def index(request):
    # return  HttpResponse("ok")
    res = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    a = request.GET.get('a')
    print(a)
    return render(request, 'clsp/index.html', context={"name": res})


def user_count(request):

    return render(request, 'clsp/user_count.html')


def user_list(request):

    return render(request, 'clsp/user_list.html')


def news_review(request):
    return render(request, 'clsp/news_review.html')


class RegisterView(View):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return HttpResponse("我是get")

    def post(self, request):
        return HttpResponse("我是post")


def middleware(request):
    print('view 视图被调用')
    return HttpResponse('OK')


class AuthView(APIView):

    def post(self,request,*args,**kwargs):
        ret = {'code':1000,'msg':None}
        try:
            # 参数是datadict 形式
            usr = request.data.get('username')
            pas = request.data.get('password')

            # usr = request._request.POST.get('username')
            # pas = request._request.POST.get('password')

            # usr = request.POST.get('username')
            # pas = request.POST.get('password')

            print(usr)
            # obj = models.User.objects.filter(username='yang', password='123456').first()
            obj = models.User.objects.filter(username=usr,password=pas).first()
            print(obj)
            print(type(obj))
            print(obj.username)
            print(obj.password)
            if not obj:
                ret['code'] = '1001'
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
                # 里为了简单，应该是进行加密，再加上其他参数
            token = usr
            print(token)
            models.userToken.objects.update_or_create(username=obj, defaults={'token': token})
            ret['msg'] = '登录成功'
            #ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)