from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View

from meiduo_mall.utils.response_code import RETCODE
from users.models import User


class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """
        提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """
        return render(request, 'register.html')

class UsernameCountView(View):
    # 判断用户名是否重复注册
    def get(self,request,username):
        '''

        :param request: 请求对象
        :param username: 用户名
        :return: JSON
        '''
        # 获取数据库中用户名的个数
        count = User.objects.filter(username=username).count()
        return http.JsonResponse({'code':RETCODE.OK,'errmsg':'ok','count':count })

class MobileCountView(View):
    # 判断手机号是否重复注册
    def get(self,ruquest,mobile):
        '''

        :param ruquest: 请求对象
        :param mobile: 手机号
        :return: JSON
        '''
        count = User.objects.filter(mobile=mobile).count()
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'count': count})



