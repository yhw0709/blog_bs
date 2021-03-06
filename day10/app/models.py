from django.db import models
# from datetime import datetime


class Course(models.Model):
    c_name = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'course'


class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True, verbose_name='班级名称')

    class Meta:
        db_table = 'grade'


class StudentInfo(models.Model):
    tel = models.CharField(max_length=11, null=True, unique=True, verbose_name='手机号')
    address = models.CharField(max_length=50, null=True, verbose_name='住址')

    class Meta:
        db_table = 'student_info'


class Student2(models.Model):
    s_name = models.CharField(max_length=10, unique=True, verbose_name='姓名')
    s_age = models.IntegerField(default=19, verbose_name='年龄')
    s_sex = models.BooleanField(default=1, verbose_name='性别')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='操作时间')
    math = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    chinese = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    is_delete = models.BooleanField(default=0)

    # 一对一关系
    stu_info = models.OneToOneField(StudentInfo, null=True, related_name='stu')

    # 多对一关系
    g = models.ForeignKey(Grade, null=True, related_name='stu')

    # 多对多关系
    c = models.ManyToManyField(Course, null=True)

    # def __init__(self):
    #     super().__init__()
    #     self.s_name = 'jerry'
    #     self.s_age = 18
    #     self.s_sex = 1
    #     self.create_time = datetime.now()
    #     self.operate_time = datetime.now()
