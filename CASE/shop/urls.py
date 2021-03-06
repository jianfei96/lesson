"""CASE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path,re_path

from shop import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),  # name 用于html页面中{% url %}匹配。缺少会报错
    # 设置没有匹配路径，跳转主页
    # path('', views.index),
    # url(r'^$',views.index)
    # path(r'^$',views.index)
    re_path(r'^$',views.index),
    path('login/', views.login, name='login'),
    # 127.0.0.1:8000/username/sssss/count/
    # as_view()将请求
    re_path(r'^username/(?P<username>[a-zA-Z0-9-_]{5,12})/count/$', views.UsernameCountView.as_view()),
]
