
import random

from django.http import HttpResponseRedirect
from django.urls import reverse

from users.models import UserTicket


def get_ticket():
    s = '1234567890abcdefghijklmnopqrstuvwxyz'
    ticket = ''
    for i in range(25):
        ticket += random.choice(s)
    return ticket


def is_login(func):

    def check(request):
        ticket = request.COOKIES.get('ticket')
        # if ticket existed
        if ticket:
            user_ticket = UserTicket.objects.filter(ticket=ticket).first()
            if user_ticket:
                return func(request)
            else:
                return HttpResponseRedirect(reverse('users:login'))
        # if not existed
        else:
            return HttpResponseRedirect(reverse('users:login'))

    return check
