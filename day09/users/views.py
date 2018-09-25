import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.decorators import permission_required

from users.models import MyUser


logger = logging.getLogger(__name__)


def create_user(request):
    if request.method == 'GET':
        MyUser.objects.create_user(username='admin',
                                   password='123')
        return HttpResponse('创建用户成功')


def add_user_permission(request):
    if request.method == 'GET':
        # 给用户名叫admin的用户添加修改用户名的权限
        user = MyUser.objects.filter(username='admin').first()
        per = Permission.objects.filter(codename='change_myuser_username').first()
        # 添加
        user.user_permissions.add(per)
        return HttpResponse('添加权限成功')

        # 删除
        # user.user_permissions.remove(per)
        # return HttpResponse('删除权限成功')

        # 清空权限
        # user.user_permissions.clear()
        # return HttpResponse('清空权限成功')


def add_group_permission(request):
    if request.method == 'GET':
        # 创建审核组，并分配查看和编辑
        group = Group.objects.filter(name='审核组').first()
        if group:
            per_list = ['change_myuser', 'delete_myuser', 'change_myuser_username', 'change_myuser_password']
            # 获取编辑的四个权限
            perms = Permission.objects.filter(codename__in=per_list)

            for per in perms:
                # 添加组和权限之间的关系
                group.permissions.add(per)
                # 删除组和权限之间的关系
                # group.permissions.remove(per)
            return HttpResponse('添加组和权限的关系')

        else:
            Group.objects.create(name='审核组')
            return HttpResponse('审核组未创建')


def add_user_group(request):
    if request.method == 'GET':
        # 给admin用户分配审核组
        user = MyUser.objects.filter(username='admin').first()
        group = Group.objects.filter(name='审核组').first()

        # 给admin用户分配组
        user.groups.add(group)

        return HttpResponse('分配组成功')


def user_permission(request):
    if request.method == 'GET':
        user = MyUser.objects.filter(username='admin').first()
        # 查询user的权限
        # 1.从用户和权限的关联表中查询
        perms = user.user_permissions.all().values('codename')
        print(perms)

        # 2.从用户查询组，从组查询权限
        perms = user.groups.first().permissions.all().values('codename')
        print(perms)

        # 通过用户获取组权限
        user.get_group_permissions()

        # 通过用户查询所有权限
        user.get_all_permission()

        return HttpResponse('查询用户对应的权限')


@permission_required('users.change_myuser_username')
def index(request):
    if request.method == 'GET':
        logger.info('index方法')
        # change_myuser_username

        # return HttpResponse('首页，需要国庆套才能登陆')
        return render(request, 'index.html')
