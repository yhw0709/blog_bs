"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static

from blog import settings
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^index/', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^gbook/', views.gbook, name='gbook'),
    url(r'^info/', views.info, name='info'),
    url(r'^infopic/', views.infopic, name='infopic'),
    url(r'^list/', views.lists, name='list'),
    url(r'^share/', views.share, name='share'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
