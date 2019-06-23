from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from shopping.views import add_goods_to_session
from users.forms import UserLoginForm, UserRegisterForm
from users.models import User


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            if user:
                if not check_password(form.cleaned_data['password'], user.password):
                    msg = '密码错误！'
                    return render(request, 'login.html', {'msg': msg})
                else:
                    request.session['user_id'] = user.id
                    add_goods_to_session(request)

                    return HttpResponseRedirect(reverse('home:index'))
            else:
                msg = '用户不存在'
                return render(request, 'login.html', {'msg': msg})
        else:
            return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            User.objects.create(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['password']),
                email=form.cleaned_data['email']
            )

            return HttpResponseRedirect(reverse('users:login'))
        else:
            return render(request, 'register.html', {'form': form})


def is_login(request):
    if request.method == 'GET':
        if request.session.get('user_id'):
            user_id = request.session['user_id']
            user = User.objects.filter(id=user_id).first()
            username = user.username

            return JsonResponse({'code': 200, 'user': username})
        else:
            return JsonResponse({'code': 500})


def logout(request):
    if request.method == 'GET':
        session_key = request.session.session_key
        request.session.delete(session_key)

        return HttpResponseRedirect(reverse('home:index'))


def user_center_info(request):
    if request.method == 'GET':
        return render(request, 'user_center_info.html')


def user_center_order(request):
    if request.method == 'GET':
        return render(request, 'user_center_order.html')


def user_center_site(request):
    if request.method == 'GET':
        return render(request, 'user_center_site.html')
