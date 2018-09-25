from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from app import views

router = SimpleRouter()

router.register(r'^student', views.StudentView)

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^add/', views.add, name='add'),

]
urlpatterns += router.urls
