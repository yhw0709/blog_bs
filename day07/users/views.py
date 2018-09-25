from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserForm
from users.models import Users, UserTicket
from utils.functions import get_ticket


def register(request):
    if request.method == 'GET':

        return render(request, 'register.html')

    if request.method == 'POST':
        # 校验参数
        form = UserForm(request.POST, request.FILES)
        # 判断是否成功
        if form.is_valid():
            # registration
            # password = make_password(form.cleaned_data['password'])
            Users.objects.create(username=form.cleaned_data['username'],
                                 password=make_password(form.cleaned_data['password']),
                                 icon=request.FILES.get('icon'))
            return HttpResponseRedirect(reverse('users:login'))
        else:
            # stay
            return render(request, 'register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # check values
        form = UserForm(request.POST)
        if form.is_valid():
            # login settings
            # 1.get user  -----auth.authenticate
            user = Users.objects.filter(username=form.cleaned_data['username']).first()
            if user:
                # get user by username successfully
                # check password
                if check_password(form.cleaned_data['password'], user.password):
                    # 1.set ticket in cookie
                    res = HttpResponseRedirect(reverse('users:index'))
                    # set_cookie
                    ticket = get_ticket()
                    res.set_cookie('ticket', ticket, max_age=1000)
                    # 2.build up relationship between user and ticket in user_ticket
                    UserTicket.objects.create(user=user, ticket=ticket)
                    return res
                else:
                    return render(request, 'login.html')
            else:
                # failed, direct to login.html
                return render(request, 'login.html')
            # 2.set cookie  ------auth.login()
            # 3.set user_ticket
            pass
        else:
            # fail,back to login
            return render(request, 'login.html')


# @is_login
def index(request):
    if request.method == 'GET':
        # # get ticket from cookie
        # ticket = request.COOKIES.get('ticket')
        # # get values from UserTicket by ticket
        # user_ticket = UserTicket.objects.filter(ticket=ticket).first()
        # if user_ticket:
        #     # get user who login
        #     user = user_ticket
        #     return render(request, 'index.html', {'user': user})
        # else:
        #     return HttpResponseRedirect(reverse('users:login'))
        return render(request, 'index.html')


def logout(request):
    if request.method == 'GET':
        response = HttpResponse()
        response.delete_cookie('ticket')
        return render(request, 'login.html')


def users(request):
    if request.method == 'GET':
        # 使用切片完成分页功能
        # sql: select * from uses offset 0 limit 3
        page_number = int(request.GET.get('page', 1))
        # users = Users.objects.all()[3*(page_number-1): 3*page_number]
        users = Users.objects.all()

        paginator = Paginator(users, 3)
        page = paginator.page(page_number)

        # return render(request, 'users.html', {'users': users})
        return render(request, 'users.html', {'page': page})
