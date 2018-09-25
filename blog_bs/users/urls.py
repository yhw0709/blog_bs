from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^article/', views.article, name='article'),
    url(r'^notice/', views.notice, name='notice'),
    url(r'^comment/', views.comment, name='comment'),
    url(r'^category/', views.category, name='category'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^update_article/(?P<article_id>\d+)/', views.update_article, name='update_article'),
    url(r'^delete_article/(?P<article_id>\d+)/', views.delete_article, name='delete_article'),
]