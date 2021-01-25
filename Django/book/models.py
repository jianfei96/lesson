from django.db import models

# Create your models here.
# 用户数据模型类 class 执行命令会在数据库创建表

# 继承父类，模型类进行数据迁移


class BookInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    pub_date = models.DateField(verbose_name='发表日期', null=True)
    readcount = models.IntegerField(verbose_name='阅读量', default=0)
    commentcount = models.IntegerField(verbose_name='评论量', default=0)
    is_deleted = models.BooleanField(default=False, verbose_name='删除')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female'),
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(
        verbose_name='性别', choices=GENDER_CHOICES, default=0)
    description = models.CharField(
        verbose_name='描述', max_length=200, null=True)
    book = models.ForeignKey(
        BookInfo, on_delete=models.CASCADE, verbose_name='图书名称')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
