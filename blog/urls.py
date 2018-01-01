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
from django.views.static import serve
from DjangoUeditor import urls as DjangoUeditor_urls

from index.views import IndexView
from .settings import MEDIA_ROOT, STATIC_ROOT


urlpatterns = [
    url(r'^woshinibaba/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^article/', include('index.urls', namespace='article')),
    url(r'^comment/', include('operation.urls', namespace='operation')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {"document_root":STATIC_ROOT}),
]