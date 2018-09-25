from django.shortcuts import render


def goods_category_detail(request):
    if request.method == 'GET':

        return render(request, 'goods_category_detail.html')


def goods_category_list(request):
    if request.method == 'GET':

        return render(request, 'goods_category_list.html')


def goods_desc(request):
    if request.method == 'GET':

        return render(request, 'goods_desc.html')


def goods_detail(request):
    if request.method == 'GET':

        return render(request, 'goods_detail.html')


def goods_list(request):
    if request.method == 'GET':

        return render(request, 'goods_list.html')
