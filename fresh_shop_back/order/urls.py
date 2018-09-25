from django.conf.urls import url

from order import views

urlpatterns = [
    url(r'^order_list', views.order_list, name='order_list')
]
