"""TwoDFire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    # Restframework branch routing
    url(r'^docs/', include_docs_urls('酒店自助机后台')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    # 添加了api-key的权限验证，在请求头上带上api-key信息到数据库进行验证之后才能正确访问路由地址
    # 请求头信息有api-key参数，参数的值为UUID，根据名字自动生成的
    path('order/', include('menu.urls')),
    path('message/', include('message.urls')),
]
