from django.shortcuts import render

# Create your views here.
# 编写web应用视图

from django.http import HttpResponse


def index(request):
    # 当用户访问子项目
    # return HttpResponse('ok')
    context = {'title': 'views'}
    #render跳转页面 1:requst 2,页面 3，发送的数据
    return render(request, 'index.html', context)
