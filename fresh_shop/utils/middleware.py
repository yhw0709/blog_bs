import re

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from users.models import User
from shopping.models import ShoppingCart


class UserAuthMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        # 登录验证中间件
        not_need_check = [
            '/home/index/',
            '/users/login/',
            '/users/is_login/',
            '/users/logout/',
	    '/users/register/',
            '/shopping/cart/',
            '/shopping/show_cart/',
            '/shopping/f_price/',
            '/shopping/add_cart/',
            '/goods/goods_detail/(\d+)/',
            '/media/(.*)/',
            '/static/(.*)/'
        ]

        path = request.path
        for not_path in not_need_check:
            # 匹配当前url地址是否需要验证
            if re.match(not_path, path):
                return None

        user_id = request.session.get('user_id')
        # 没有登录，获取不到user_id参数，跳转到login页面
        if not user_id:
            return HttpResponseRedirect(reverse('users:login'))

        # 给request.user赋值，赋值为当前用户
        user = User.objects.get(pk=user_id)
        request.user = user

        return None


class UserSessionMiddleware(MiddlewareMixin):
    # 同步session数据到shopping_cart表
    @staticmethod
    def process_request(request):
        # 判断用户是否登录
        user_id = request.session.get('user_id')
        if user_id:
            # 同步
            # 获取到session中的数据
            session_goods = request.session.get('goods')
            if session_goods:
                # 1. 如果购物车中没有session中的商品数据，则创建
                # 2. 如果购物车中有session种的商品数据，则更新
                # session中商品信息的结构：[[id, num, is_select],[]]
                # goods_ids = [goods[0] for goods in session_goods]
                for goods in session_goods:
                    # 查询购物车中是否存在商品
                    cart = ShoppingCart.objects.filter(goods_id=goods[0], user_id=user_id).first()

                    if cart:
                        # 如果购物车中存在session中保存的商品信息，则修改选择状态和数量
                        if cart.nums != goods[1]:
                            cart.nums = goods[1]
                        cart.is_select = int(goods[2])
                        cart.save()
                    else:
                        # session中的商品数据不存在购物车中
                        ShoppingCart.objects.create(
                            user_id=user_id,
                            goods_id=goods[0],
                            nums=int(goods[1]),
                            is_select=int(goods[2])
                        )

                return None
