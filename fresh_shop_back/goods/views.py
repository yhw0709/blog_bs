from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from goods.models import GoodsCategory, Goods


def goods_category_detail(request, category_id):
    if request.method == 'GET':
        category = GoodsCategory.objects.get(id=category_id)
        # 返回类型
        category_tpye = GoodsCategory.CATEGORY_TYPE

        return render(request, 'goods_category_detail.html', {'category': category,
                                                              'category_type': category_tpye})
    if request.method == 'POST':
        category_front_image = request.FILES.get('category_front_image')
        if category_front_image:
            category = GoodsCategory.objects.get(pk=category_id)
            category.category_front_image = category_front_image
            category.save()

        return HttpResponseRedirect(reverse('goods:goods_category_list'))


def goods_category_list(request):
    if request.method == 'GET':
        # 获取分类信息
        categorys = GoodsCategory.objects.all()
        # 返回类型
        category_tpye = GoodsCategory.CATEGORY_TYPE

        return render(request, 'goods_category_list.html', {'categorys': categorys,
                                                            'category_type': category_tpye})


def goods_desc(request):
    if request.method == 'GET':

        return render(request, 'goods_desc.html')


def goods_detail(request, goods_id):
    if request.method == 'GET':
        good = Goods.objects.get(pk=goods_id)
        category_tpye = GoodsCategory.CATEGORY_TYPE

        return render(request, 'goods_detail.html', {'good': good,
                                                     'category_type': category_tpye})
    if request.method == 'POST':
        name = request.POST.get('name')
        goods_sn = request.POST.get('goods_sn')
        category_id = request.POST.get('category')
        goods_nums = request.POST.get('goods_nums')
        market_price = request.POST.get('market_price')
        shop_price = request.POST.get('shop_price')
        goods_brief = request.POST.get('goods_brief')
        goods_front_image = request.FILES.get('goods_front_image')

        good = Goods.objects.get(pk=goods_id)
        if name:
            good.name = name
        if goods_sn:
            good.goods_sn = goods_sn
        if category_id:
            good.category_id = category_id
        if goods_nums:
            good.goods_nums = goods_nums
        if market_price:
            good.market_price = market_price
        if shop_price:
            good.shop_price = shop_price
        if goods_brief:
            good.goods_brief = goods_brief
        if goods_front_image:
            good.goods_front_image = goods_front_image

        good.save()

        return HttpResponseRedirect(reverse('goods:goods_list'))


def goods_list(request):
    if request.method == 'GET':
        goods = Goods.objects.all()
        category_tpye = GoodsCategory.CATEGORY_TYPE

        return render(request, 'goods_list.html', {'goods': goods,
                                                   'category_type': category_tpye})


def goods_add(request):
    if request.method == 'GET':

        return render(request, 'goods_add.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        goods_sn = request.POST.get('goods_sn')
        category_id = request.POST.get('category')
        goods_nums = request.POST.get('goods_nums')
        market_price = request.POST.get('market_price')
        shop_price = request.POST.get('shop_price')
        goods_brief = request.POST.get('goods_brief')
        goods_front_image = request.FILES.get('goods_front_image')

        Goods.objects.create(
            name=name,
            goods_sn=goods_sn,
            category_id=category_id,
            goods_nums=goods_nums,
            market_price=market_price,
            shop_price=shop_price,
            goods_brief=goods_brief,
            goods_front_image=goods_front_image
        )

        return HttpResponseRedirect(reverse('goods:goods_list'))


def goods_delete(request, goods_id):
    if request.method == 'GET':
        good = Goods.objects.get(pk=goods_id)
        good.delete()

        return HttpResponseRedirect(reverse('goods:goods_list'))
