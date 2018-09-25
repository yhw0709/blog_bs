from django.conf.urls import url

from users import views

urlpatterns = [
    # url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^index/', views.index, name='index'),
    url(r'^logout/', views.logout, name='logout'),
    # url(r'^users/', views.users, name='users'),
]
