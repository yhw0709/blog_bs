from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app.models import Student2


def index(request):
    if request.method == 'GET':
        stus = Student2.objects.all()

        # return render(request, 'index.html', {'students': stus})
        # return HttpResponse('hello')
        return render(request, 'stus.html', {'students': stus})


def del_stu(request, s_id):
    if request.method == 'GET':
        # 删除方法
        # 1.获取url中的id值
        # id = request.GET.get('id')
        # 2.获取id对应的学生对象
        stu = Student2.objects.get(pk=s_id)
        # 3.对象.delete()
        stu.delete()
        # 重定向
        return HttpResponseRedirect(reverse('app:index'))
        # return HttpResponseRedirect('/app/stu/')


def sel_stu(request, s_id):
    if request.method == 'GET':
        stu = Student2.objects.get(pk=s_id)

        return render(request, 'stu_info.html', {'student': stu})
