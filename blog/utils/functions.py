from django.http import HttpResponseRedirect
from django.urls import reverse


def is_login(func):

    def check(request):
        try:
            request.session['user_id']
        except:
            return HttpResponseRedirect(reverse('users:login'))

        return func(request)

    return check
