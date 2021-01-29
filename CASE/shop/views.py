from django.shortcuts import render, redirect
import datetime
from django.db import connection
from django import http

# Create your views here.


# 定义跳转方法
from django.views import View


def index(request):
    return render(request, 'index.html')


def register(request):
    username = request.POST.get("username")
    password = request.POST.get('password')
    phone = request.POST.get('phone')
    time = datetime.datetime.now()

    # 获取数据库链接对象
    cursor = connection.cursor()
    sql = "select * from shop_customer where username='%s'" % (username)
    count = cursor.execute(sql)
    # print(count)
    if count == 0:
        sql = "insert into shop_customer(username,password,phone,time_created)\
         values('%s','%s','%s','%s');" % (username, password, phone, time)
        cursor.execute(sql)
        return redirect('login')

    return render(request, 'register.html')


# def register_action(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         print(username)
#         return username

def login(request):
    # 页面默认跳转是get方式
    if request.method == 'POST':
        # 获取用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        cursor = connection.cursor()
        sql = """select * from shop_customer where(username = %s) and (password = %s)"""
        count = cursor.execute(sql, [username, password])
        if count == 1:
            print(username)
            return render(request, 'index.html', {'username': username})
    return render(request, 'login.html')


# 类视图
class UsernameCountView(View):
    def get(self, request, username):
        # 接受 处理用户是否存在
        print(username)
        cursor = connection.cursor()
        sql = '''select * from shop_customer where (username = %s)'''
        # username 执行时替换%s
        count = cursor.execute(sql, [username])
        print(count)
        # 发送给前端响应，返回json数据格式
        return http.JsonResponse({
            'count': count,
        })
