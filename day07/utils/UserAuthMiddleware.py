from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from users.models import UserTicket


class UserMiddleware(MiddlewareMixin):
    # rebuild process_request
    @staticmethod
    def process_request(request):
        # get ticket
        ticket = request.COOKIES.get('ticket')
        # set urls which need no middleware
        not_login_path = ['/users/login/', '/users/register/']
        path = request.path
        # check url
        for n_path in not_login_path:
            # which need no middleware
            if path == n_path:
                return
        # no ticket,go to login.html
        if not ticket:
            return HttpResponseRedirect(reverse('users:login'))
        # get user by ticket
        user_ticket = UserTicket.objects.filter(ticket=ticket).first()
        # check user
        if not user_ticket:
            # no such user,go to login.html
            return HttpResponseRedirect(reverse('users:login'))
        # set global user
        request.user = user_ticket.user
        # middleware ends,return
        return None
