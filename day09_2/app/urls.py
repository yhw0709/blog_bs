from rest_framework.routers import SimpleRouter

from app import views

router = SimpleRouter()

router.register(r'^student', views.StudentView)

urlpatterns = [

]
urlpatterns += router.urls
