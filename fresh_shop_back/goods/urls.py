from django.conf.urls import url

from goods import views

urlpatterns = [
    url(r'^goods_category_detail/', views.goods_category_detail, name='goods_category_detail'),
    url(r'^goods_category_list/', views.goods_category_list, name='goods_category_list'),
    url(r'^goods_desc/', views.goods_desc, name='goods_desc'),
    url(r'^goods_detail/', views.goods_detail, name='goods_detail'),
    url(r'^goods_list/', views.goods_list, name='goods_list'),
]
