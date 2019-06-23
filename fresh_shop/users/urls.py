from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^is_login/', views.is_login, name='is_login'),
    url(r'^register/', views.register, name='register'),
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    url(r'^user_center_order/', views.user_center_order, name='user_center_order'),
    url(r'^user_center_site/', views.user_center_site, name='user_center_site'),
]