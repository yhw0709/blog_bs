from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserForm, CheckUserForm


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        # 校验页面中传递的参数是否填写完整
        # username = request.POST.get('username')
        form = UserForm(request.POST)
        # is_valid():判断表单是否验证通过
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password)
            # 实现跳转
            return HttpResponseRedirect(reverse('users:login'))
        else:
            return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 表单验证，用户名和密码是否填写，校验用户名是否注册
        form = CheckUserForm(request.POST)
        if form.is_valid():
            # 校验用户名和密码，判断返回的对象是否为空，如果不为空，则为user对象
            user = auth.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                # 校验成功 用户名和密码是正确的 加密方法是Django自带的，所以用Django自带的方法
                auth.login(request, user)
                return HttpResponseRedirect(reverse('users:index'))
            else:
                # 密码错误
                return render(request, 'login.html', {'error': '密码错误'})
        else:
            return render(request, 'login.html', {'form': form})


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def logout(request):
    if request.method == 'GET':
        # 注销
        auth.logout(request)
        return HttpResponseRedirect(reverse('users:login'))
