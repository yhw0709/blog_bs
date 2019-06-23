import random
from datetime import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse


def is_login(func):

    def check(request):
        try:
            # 获取session中已经保存的user_id值
            request.session['user_id']
        except:
            # 跳转到登录
            return HttpResponseRedirect(reverse('users:login'))

        return func(request)

    return check


def get_order_sn():
    """
    生成随机的订单号
    :return:
    """
    sn = ''
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(10):
        sn += random.choice(s)
    sn += datetime.now().strftime('%Y%m%d%H%M%S')
    return sn
