from django.http import JsonResponse
from django.shortcuts import render

from shopping.models import ShoppingCart
from order.models import OrderGoods, OrderInfo
from utils.functions import get_order_sn


def place_order(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        # user = request.user
        # 获取当前勾选的商品用于下单
        cart_goods = ShoppingCart.objects.filter(user_id=user_id, is_select=True)
        for cart in cart_goods:
            cart.total_price = cart.nums * cart.goods.shop_price
        return render(request, 'place_order.html', {'cart_goods': cart_goods})

    if request.method == 'POST':
        """
        接收ajax请求，创建订单
        """
        # 1. 选择购物车中is_select为True的商品
        # 2. 创建订单
        # 3. 创建订单和商品之间的关联关系表，order_goods表
        # 4. 删除购物车中已经下单的商品
        user_id = request.session['user_id']
        # 获取购物车中当前登录用户勾选的商品
        carts = ShoppingCart.objects.filter(user_id=user_id, is_select=True)
        order_sn = get_order_sn()
        # 订单金额
        order_mount = 0
        for cart in carts:
            order_mount += cart.nums * cart.goods.shop_price
        # 创建订单
        order = OrderInfo.objects.create(
            user_id=user_id,
            order_sn=order_sn,
            order_mount=order_mount,
        )

        for cart in carts:
            OrderGoods.objects.create(
                order_id=order.id,
                goods_id=cart.goods_id,
                goods_nums=cart.nums
            )
        carts.delete()
        # 删除session中的商品信息
        if request.session.get('goods'):
            request.session.pop('goods')
        return JsonResponse({'code': 200, 'msg': '请求成功'})
