from django.shortcuts import render


def order_list(request):
    if request.method == 'GET':

        return render(request, 'order_list.html')
