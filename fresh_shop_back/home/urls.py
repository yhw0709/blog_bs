from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from home import views

urlpatterns = [
    # 登录页面
    url(r'^login/', views.login, name='login'),
    # index页面
    url(r'^index/', login_required(views.index), name='index'),
    # 登出页面
    url(r'^logout/', login_required(views.logout), name='logout'),
]
