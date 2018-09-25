from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from goods import views

urlpatterns = [
    # 商品详情
    url(r'^goods_category_detail/(?P<category_id>\d+)/', login_required(views.goods_category_detail), name='goods_category_detail'),
    # 商品分类列表
    url(r'^goods_category_list/', login_required(views.goods_category_list), name='goods_category_list'),
    # 排序
    url(r'^goods_desc/', login_required(views.goods_desc), name='goods_desc'),
    # 商品详情
    url(r'^goods_detail/(?P<goods_id>\d+)/', login_required(views.goods_detail), name='goods_detail'),
    # 商品列表
    url(r'^goods_list/', login_required(views.goods_list), name='goods_list'),
    # 添加商品
    url(r'^goods_add/', login_required(views.goods_add), name='goods_add'),
    # 删除商品
    url(r'^goods_delete/(?P<goods_id>\d+)/', login_required(views.goods_delete), name='goods_delete'),
]
