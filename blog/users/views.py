# from datetime import timedelta

# from django.contrib.auth.hashers import check_password, make_password
# from django.http import HttpResponseRedirect
from django.shortcuts import render
# from django.urls import reverse

# from users.forms import UserForm
# from users.models import Users
# from utils.functions import is_login


# index索引
# def index(request):
#     if request.method == 'GET':
#         # 通过user_id是否存在session中来判断用户是否登入
#         # 用户存在
#         try:
#             user_id = request.session['user_id']
#             # 通过id找到用户对象，并且把用户对象传到index页面
#             user = Users.objects.filter(id=user_id).first()
#             return render(request, 'index.html', {'user': user})
#         except:
#             # 用户不存在
#             return render(request, 'index.html')
from users.models import Users


def index(request):
    if request.method == 'GET':
        user = Users.objects.filter(id=1).first()
        articles = user.articles.all()

        return render(request, 'index.html', {'user': user, 'articles': articles})


def about(request):
    if request.method == 'GET':

        return render(request, 'about.html')


def gbook(request):
    if request.method == 'GET':

        return render(request, 'gbook.html')


def info(request):
    if request.method == 'GET':

        return render(request, 'info.html')


def infopic(request):
    if request.method == 'GET':

        return render(request, 'infopic.html')


def lists(request):
    if request.method == 'GET':

        return render(request, 'list.html')


def share(request):
    if request.method == 'GET':

        return render(request, 'share.html')


'''
# 登录
def login(request):
    # 响应跳转到login页面的请求
    if request.method == 'GET':

        return render(request, 'login.html')
    # 响应登录请求，完成登录后跳转至index页面
    if request.method == 'POST':
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


# 登出
@is_login
def logout(request):
    # 登出后跳转到index界面
    if request.method == 'GET':
        session_key = request.session.session_key
        request.session.delete(session_key)

        return HttpResponseRedirect(reverse('users:index'))


# 注册，仅私用
def register(request):
    if request.method == 'GET':

        return render(request, 'register.html')
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            Users.objects.create(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['password']),
                icon=request.FILES.get('icon')
            )
        else:
            return render(request, 'register.html')
'''
