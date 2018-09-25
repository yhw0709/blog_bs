
from django.utils.deprecation import MiddlewareMixin

from users.models import MyUser


class UserAuthMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):

        user = MyUser.objects.get(username='admin')
        request.user = user

        return None
