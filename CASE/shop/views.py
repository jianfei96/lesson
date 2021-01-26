from django.shortcuts import render


# Create your views here.


# 定义跳转方法
def index(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')
