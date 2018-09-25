from datetime import timedelta

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserForm, ArticleForm
from users.models import Users, Articles
from utils.functions import is_login


@is_login
def index(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = Users.objects.filter(id=user_id).first()

        return render(request, 'index.html', {'user': user})


def article(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = Users.objects.filter(id=user_id).first()
        articles = user.articles.all()

        return render(request, 'article.html', {'user': user, 'articles': articles})


def notice(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = Users.objects.filter(id=user_id).first()

        return render(request, 'notice.html', {'user': user})


def comment(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = Users.objects.filter(id=user_id).first()

        return render(request, 'comment.html', {'user': user})


def category(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = Users.objects.filter(id=user_id).first()

        return render(request, 'category.html', {'user': user})


def login(request):
    if request.method == 'GET':

        return render(request, 'login.html')

    if request.method == 'POST':
        # 使用cookie加session形式实现登录
        username = request.POST.get('username')
        password = request.POST.get('userpwd')
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


def register(request):
    if request.method == 'GET':

        return render(request, 'register.html')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            Users.objects.create(
                username=form.cleaned_data['username'],
                password=make_password(form.cleaned_data['userpwd'])
            )

            return HttpResponseRedirect(reverse('users:login'))
        else:

            return render(request, 'register.html')


def logout(request):
    if request.method == 'GET':
        session_key = request.session.session_key
        request.session.delete(session_key)

        return HttpResponseRedirect(reverse('users:login'))


def add_article(request):
    if request.method == 'GET':
        user_id = request.session['user_id']
        user = Users.objects.filter(id=user_id).first()

        return render(request, 'add-article.html', {'user': user})

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        user_id = request.session['user_id']
        if form.is_valid():
            Articles.objects.create(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['describe'],
                u_id=user_id
            )

            return HttpResponseRedirect(reverse('users:article'))
        else:
            return render(request, 'add-article.html')


def update_article(request, article_id):
    if request.method == 'GET':
        article_update = Articles.objects.get(id=article_id)

        return render(request, 'update-article.html', {'article': article_update})

    if request.method == 'POST':
        article_update = Articles.objects.get(id=article_id)
        form = ArticleForm(request.POST)
        # user_id = request.session['user_id']
        if form.is_valid():
            article_update.title = form.cleaned_data['title']
            article_update.content = form.cleaned_data['content']
            article_update.save()
            return HttpResponseRedirect(reverse('users:article'))
        else:
            return render(request, 'update-article.html', {'article': article_update})


def delete_article(request, article_id):
    if request.method == 'GET':
        article_del = Articles.objects.get(id=article_id)
        article_del.is_delete = 1
        article_del.save()

        return HttpResponseRedirect(reverse('users:article'))
