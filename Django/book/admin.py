from django.contrib import admin
# 网站后台管理站点配置相关
# Register your models here.
from book.models import BookInfo
from book.models import PeopleInfo
admin.site.register(BookInfo)
admin.site.register(PeopleInfo)