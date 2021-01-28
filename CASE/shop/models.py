from django.db import models

# Create your models here.

# 传概念数据库表的模型类
class Customer(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=12)
    phone = models.CharField(max_length=11)
    time_created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.username
