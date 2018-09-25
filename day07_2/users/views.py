from datetime import timedelta

from django.contrib.auth.hashers import check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import Users
from utils.functions import is_login


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 使用cookie加session形式实现登录
        username = request.POST.get('username')
        password = request.POST.get('password')
        # all()校验参数，如果列表中元素存在空，返回false
        if not all([username, password]):
            msg = '请填写完整！'
            return render(request, 'login.html', {'msg': msg})
        # 校验是否能够通过username和password找到user对象
        user = Users.objects.filter(username=username).first()
        if user:
            # 校验密码
            if not check_password(password, user.password):
                msg = '密码错误！'
                return render(request, 'login.html', {'msg': msg})
            else:
                # 向cookie中设值，向user_ticket表中设值
                request.session['user_id'] = user.id

                #  设置session过期时间
                request.session.set_expiry(timedelta(days=2))

                return HttpResponseRedirect(reverse('users:index'))
        else:
            msg = '用户名错误！'
            return render(request, 'login.html', {'msg': msg})


@is_login
def index(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = Users.objects.filter(id=user_id).first()
        return render(request, 'index.html', {'user': user})


@is_login
def logout(request):
    if request.method == 'GET':
        # 注销，删除session和cookie
        # request.session.flush()
        # 获取session_key并实现删除
        session_key = request.session.session_key
        request.session.delete(session_key)

        return HttpResponseRedirect(reverse('users:login'))
