from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=14, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=200, verbose_name='密码')
    icon = models.ImageField(upload_to='upload', null=True, verbose_name='头像')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='最后操作时间')
    is_delete = models.IntegerField(default=0)

    class Meta:
        db_table = 'users'


class Articles(models.Model):
    title = models.CharField(max_length=30, verbose_name='标题')
    content = models.TextField(verbose_name='内容')
    picture = models.ImageField(upload_to='upload', null=True, verbose_name='图片')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='最后操作时间')
    is_delete = models.IntegerField(default=0)

    u = models.ForeignKey(Users, related_name='articles')

    class Meta:
        db_table = 'articles'
