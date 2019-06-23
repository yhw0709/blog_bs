from django.shortcuts import render

from goods.models import Goods


def goods_detail(request, id):
    if request.method == 'GET':
        good = Goods.objects.filter(pk=id).first()

        return render(request, 'detail.html', {'good': good})


def lists(request):
    if request.method == 'GET':
        return render(request, 'list.html')
