from rest_framework import mixins, viewsets


from app.models import Student2
from app.serializers import StudentSerializer


class StudentView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    # 返回数据
    queryset = Student2.objects.all()
    # 序列化
    serializer_class = StudentSerializer
