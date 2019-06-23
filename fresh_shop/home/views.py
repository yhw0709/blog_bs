from django.shortcuts import render

from goods.models import Goods, GoodsCategory


def index(request):
    if request.method == 'GET':
        # user_id = request.session['user_id']
        # user = User.objects.filter(id=user_id).first()

        kinds = ['fruit', 'seafood', 'meet', 'egg', 'vegetables', 'ice']

        # 获取分类
        category_type = GoodsCategory.CATEGORY_TYPE
        # 按照id降序排列
        goods = Goods.objects.all().order_by('-id')
        # 循环商品分类，并且组装结果
        data_all = {}
        for c_type in category_type:
            data = []
            count = 0
            for good in goods:
                # 限制每个分类的个数为4
                if count < 4:
                    if c_type[0] == good.category.category_type:
                        data.append(good)
                        count += 1
            data_all['goods_'+str(c_type[0])] = data

        return render(request, 'index.html', {'kinds': kinds,
                                              'goods': data_all,
                                              'category_type': category_type})
