from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from fresh_shop_back.settings import PAGE_NUMBER
from goods.forms import GoodsForm
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


def goods_desc(request, goods_id):
    if request.method == 'GET':
        good = Goods.objects.get(pk=goods_id)

        return render(request, 'goods_desc.html', {'good': good})
    if request.method == 'POST':
        # good = Goods.objects.get(pk=goods_id)
        # goods_brief = request.POST.get('content')
        # if goods_brief:
        #     good.goods_brief = goods_brief
        #     good.save()
        content = request.POST.get('content')
        Goods.objects.filter(pk=goods_id).update(goods_desc=content)

        return HttpResponseRedirect(reverse('goods:goods_list'))


def goods_detail(request, goods_id):
    if request.method == 'GET':
        good = Goods.objects.get(pk=goods_id)
        category_tpye = GoodsCategory.CATEGORY_TYPE

        return render(request, 'goods_detail.html', {'good': good,
                                                     'category_type': category_tpye})
    if request.method == 'POST':
        # name = request.POST.get('name')
        # goods_sn = request.POST.get('goods_sn')
        # category_id = request.POST.get('category')
        # goods_nums = request.POST.get('goods_nums')
        # market_price = request.POST.get('market_price')
        # shop_price = request.POST.get('shop_price')
        # goods_brief = request.POST.get('goods_brief')
        # goods_front_image = request.FILES.get('goods_front_image')
        #
        # good = Goods.objects.get(pk=goods_id)
        # if name:
        #     good.name = name
        # if goods_sn:
        #     good.goods_sn = goods_sn
        # if category_id:
        #     good.category_id = category_id
        # if goods_nums:
        #     good.goods_nums = goods_nums
        # if market_price:
        #     good.market_price = market_price
        # if shop_price:
        #     good.shop_price = shop_price
        # if goods_brief:
        #     good.goods_brief = goods_brief
        # if goods_front_image:
        #     good.goods_front_image = goods_front_image
        #
        # good.save()
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            # good = Goods.objects.get(pk=goods_id)
            # good.name = form.cleaned_data['name']
            # good.category = form.cleaned_data['category']
            # good.goods_sn = form.cleaned_data['goods_sn']
            # good.goods_nums = form.cleaned_data['goods_nums']
            # good.market_price = form.cleaned_data['market_price']
            # good.shop_price = form.cleaned_data['shop_price']
            # good.goods_brief = form.cleaned_data['goods_brief']
            # if form.cleaned_data['goods_front_image']:
            #     good.goods_front_image = form.cleaned_data['goods_front_image']
            # good.save()

            # 获取表单验证中的参数，其中包含了封面图的键值对
            data = form.cleaned_data
            # 取出封面图
            goods_front_image = data.pop('goods_front_image')
            # 判断封面图是否存在
            # 存在
            if goods_front_image:
                # 图片保存不能使用update方法
                good = Goods.objects.get(pk=goods_id)
                good.goods_front_image = goods_front_image
                good.save()

            Goods.objects.filter(pk=goods_id).update(**data)

            return HttpResponseRedirect(reverse('goods:goods_list'))
        else:
            good = Goods.objects.get(pk=goods_id)
            category_type = GoodsCategory.CATEGORY_TYPE
            return render(request, 'goods_detail.html', {
                'good': good,
                'category_type': category_type,
                'form': form
            })


def goods_list(request):
    if request.method == 'GET':
        try:
            page_number = int(request.GET.get('page', 1))
        except:
            page_number = 1

        goods = Goods.objects.all()
        category_type = GoodsCategory.CATEGORY_TYPE

        paginator = Paginator(goods, PAGE_NUMBER)
        page = paginator.page(page_number)

        return render(request, 'goods_list.html', {'goods': page,
                                                   'category_type': category_type})


def goods_add(request):
    if request.method == 'GET':
        category_type = GoodsCategory.CATEGORY_TYPE

        return render(request, 'goods_add.html', {'category_type': category_type})
    if request.method == 'POST':
        # name = request.POST.get('name')
        # goods_sn = request.POST.get('goods_sn')
        # category_id = request.POST.get('category')
        # goods_nums = request.POST.get('goods_nums')
        # market_price = request.POST.get('market_price')
        # shop_price = request.POST.get('shop_price')
        # goods_brief = request.POST.get('goods_brief')
        # goods_front_image = request.FILES.get('goods_front_image')
        #
        # Goods.objects.create(
        #     name=name,
        #     goods_sn=goods_sn,
        #     category_id=category_id,
        #     goods_nums=goods_nums,
        #     market_price=market_price,
        #     shop_price=shop_price,
        #     goods_brief=goods_brief,
        #     goods_front_image=goods_front_image
        # )
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            # Goods.objects.create(
            #     name=form.cleaned_data['name'],
            #     goods_sn=form.cleaned_data['goods_sn'],
            #     goods_nums=form.cleaned_data['goods_nums'],
            #     market_price=form.cleaned_data['market_price'],
            #     shop_price=form.cleaned_data['shop_price'],
            #     goods_brief=form.cleaned_data['goods_brief'],
            #     goods_front_image=form.cleaned_data['goods_front_image']
            # )

            # 保存， *arg  **kwargs
            data = form.cleaned_data
            Goods.objects.create(**data)

            return HttpResponseRedirect(reverse('goods:goods_list'))
        else:
            return render(request, 'goods_add.html', {'form': form})


# def goods_delete(request, goods_id):
#     if request.method == 'GET':
#         good = Goods.objects.get(pk=goods_id)
#         good.delete()
#
#         return HttpResponseRedirect(reverse('goods:goods_list'))


def goods_delete(request, goods_id):
    if request.method == 'POST':
        Goods.objects.get(pk=goods_id).delete()
        return JsonResponse({'code': 200, 'msg': '请求成功'})
