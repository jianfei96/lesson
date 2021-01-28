from django.shortcuts import render,redirect
import datetime
from django.db import connection


# Create your views here.


# 定义跳转方法
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
         values('%s','%s','%s','%s');" %(username,password,phone,time)
        cursor .execute(sql)
        return redirect('login')

    return render(request, 'register.html')


# def register_action(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         print(username)
#         return username

def login(request):
    return render(request, 'login.html')
