import logging
import time

from django.utils.deprecation import MiddlewareMixin

from users.models import MyUser


class UserAuthMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):

        user = MyUser.objects.get(username='admin')
        request.user = user

        return None


class LogMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        # url到服务器的时候，经过中间件最先执行的方法
        request.init_time = time.time()
        request.init_body = request.body

    @staticmethod
    def process_response(request, response):
        # 经过中间件最后执行的方法
        count_time = (time.time() - request.init_time) / 1000
        code = response.status_code
        req_body = request.init_body
        res_body = response.content

        logger = logging.getLogger(__name__)
        msg = '%s %s %s %s' % (count_time, code, req_body, res_body)
        logger.info(msg)

        return response
