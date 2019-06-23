from django.http import JsonResponse
from django.shortcuts import render

from goods.models import Goods
from shopping.models import ShoppingCart


def cart(request):
    # if request.method == 'GET':
    #     user_id = request.session['user_id']
    #     if user_id:
    #         pass
    #     else:
    #         if request.session.get('goods'):
    #             global session_goods
    #             global goods
    #             global cart_count
    #             session_goods = request.session['goods']
    #             cart_count = len(session_goods)
    #             goods = list()
    #             for session_good in session_goods:
    #                 good = Goods.objects.filter(id=session_good[0]).first()
    #                 goods.append(good)
    #
    #             return render(request, 'cart.html', {'cart_count': cart_count,
    #                                                  'goods': goods})
    # return render(request, 'cart.html')
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        if user_id:
            # 登录系统用户，获取购物车中的商品信息
            shop_cart = ShoppingCart.objects.filter(user_id=user_id)
            goods_all = [(cart.goods, cart.is_select, cart.nums) for cart in shop_cart]

            cart_count = len(shop_cart)
            return render(request, 'cart.html', {'goods_all': goods_all, 'cart_count': cart_count})

        else:
            # 没有登录
            if request.session.get('goods'):
                goods = request.session['goods']
                cart_count = len(goods)
                # 拿到session中所有的商品id
                # goods_ids = [good.id for good in goods]
                # 获取商品信息
                # [[goods object, is_selected, nums],[goods object, is_selected, nums]]
                goods_all = [(Goods.objects.filter(pk=good[0]).first(), good[1], good[2]) for good in goods]
                # data = list()
                # for goods in goods_all:
                #     data.append(goods)
            else:
                goods_all = []
                cart_count = 0

            return render(request, 'cart.html', {'goods_all': goods_all,
                                                 'cart_count': cart_count})


def add_cart(request):
    if request.method == 'POST':
        # 添加到购物车，分登录和未登录
        # 判断用户是否登录，session['user_id']
        # 添加到session中的数据格式为：
        # key:goods
        # value:[[id1, num], [id2, num], [id3, num]]

        # 1.1添加到购物车的数据，就是添加到session中
        # 1.2 如果商品已经加入到session中，则修改session中商品的个数
        # 1.3 如果商品没有添加到session中，则添加

        # 获取从ajax中传递的商品的id和商品的个数
        goods_id = request.POST.get('goods_id')
        goods_num = request.POST.get('goods_num')

        goods_list = [goods_id, goods_num, 1]

        # user_id = request.session.get('user_id')
        # is_goods = request.session.get('goods')
        #
        # if user_id and not is_goods:
        #     shopping_carts = ShoppingCart.objects.filter(user_id=user_id)
        #     goods_carts = list()
        #     if shopping_carts:
        #         for cart in shopping_carts:
        #             goods_cart = [int(cart.goods_id), int(cart.nums), int(cart.is_select)]
        #             goods_carts.append(goods_cart)
        #         request.session['goods'] = goods_carts

            # cart_count = len(shopping_carts)

        if request.session.get('goods'):
            flag = 0
            # 说明购物车中还没有商品
            session_goods = request.session['goods']
            for goods in session_goods:
                if goods_id == goods[0]:
                    goods[1] = int(goods[1]) + int(goods_num)
                    flag = 1

            if not flag:
                session_goods.append(goods_list)
            # 修改sess中的商品信息
            request.session['goods'] = session_goods
            cart_count = len(session_goods)

        else:
            data = list()
            data.append(goods_list)
            request.session['goods'] = data
            cart_count = 1

        # if user_id:
        #     shopping_carts = ShoppingCart.objects.filter(user_id=user_id)
        #     cart_count += len(shopping_carts)

        return JsonResponse({'code': 200, 'cart_count': cart_count})


def show_cart(request):
    if request.method == 'GET':

        cart_count = 0

        # if request.session.get('goods'):
        #     session_goods = request.session['goods']
        #     cart_count += len(session_goods)

        #     return JsonResponse({'code': 200, 'cart_count': cart_count})
        # else:
        #     return JsonResponse({'code': 200, 'cart_count': 0})

        user_id = request.session.get('user_id')
        if user_id:
            shopping_carts = ShoppingCart.objects.filter(user_id=user_id)
            cart_count += len(shopping_carts)
        else:
            if request.session.get('goods'):
                session_goods = request.session['goods']
                cart_count += len(session_goods)
            else:
                cart_count = 0

        return JsonResponse({'code': 200, 'cart_count': cart_count})


def f_price(request):
    if request.method == 'GET':
        """
        返回物品的价格，总价
        {key:[[id1, price], [id2, price]], key: [[],[]]}
        """
        user_id = request.session.get('user_id')
        if user_id:
            # 获取当前用户的购物车中的商品
            carts = ShoppingCart.objects.filter(user_id=user_id)
            cart_data = dict()
            all_price = 0
            if carts:
                cart_data['goods_price'] = [(cart.goods_id, cart.nums * cart.goods.shop_price) for cart in carts]

                for cart in carts:
                    if cart.is_select:
                        all_price += cart.nums * cart.goods.shop_price

            cart_data['all_price'] = all_price
            final_price = int(all_price) + 10
            cart_data['final_price'] = final_price

        else:
            session_goods = request.session.get('goods')
            cart_data = dict()
            data_all = []
            all_price = 0
            if session_goods:
                for goods in session_goods:
                    data = list()
                    data.append(goods[0])
                    g = Goods.objects.get(pk=goods[0])
                    data.append(int(goods[1]) * g.shop_price)
                    data_all.append(data)
                    if goods[2]:
                        all_price += int(goods[1]) * g.shop_price
                cart_data['goods_price'] = data_all
                cart_data['all_price'] = all_price
                final_price = int(all_price) + 10
                cart_data['final_price'] = final_price

        return JsonResponse({'code': 200, 'cart_data': cart_data})


def add_goods_to_session(request):
    # 获取user_id
    user_id = request.session['user_id']
    # 获取session中的商品
    session_goods = request.session.get('goods')
    # 获取用户的购物车中的商品
    shopping_carts = ShoppingCart.objects.filter(user_id=user_id)
    goods_carts = list()
    # 购物车中有商品
    if shopping_carts:
        for carts in shopping_carts:
            # 组装商品
            goods_cart = [int(carts.goods_id), int(carts.nums), int(carts.is_select)]
            goods_carts.append(goods_cart)
        if session_goods:
            for good_carts in goods_carts:
                flag = 0
                for goods in session_goods:
                    if good_carts[0] == goods[0]:
                        goods[1] = int(goods[1]) + int(good_carts[1])
                        flag = 1

                if not flag:
                    session_goods.append(good_carts)
                # 修改sess中的商品信息
                request.session['goods'] = session_goods
        else:
            request.session['goods'] = goods_carts

    return
