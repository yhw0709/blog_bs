from django.conf.urls import url

from shopping import views

urlpatterns = [
    url(r'^cart/', views.cart, name='cart'),
    url(r'^add_cart/', views.add_cart, name='add_cart'),
    url(r'^show_cart/', views.show_cart, name='show_cart'),
    url(r'^f_price/', views.f_price, name='f_price'),
]
