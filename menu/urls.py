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
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
from menu import menuhandler
from message import messagedatahandler

urlpatterns = [
    # 查询菜，下单
    url(r'^placeanhoder/$', menuhandler.placeanhoderView.as_view(), name="placeanhoder"),
    url(r'^checkhodersuccess/$', menuhandler.checkhodersuccessView.as_view(), name="checkhodersuccess"),
    url(r'^getAllmenu/$', menuhandler.selectmenu, name="getAllmenu"),
    url(r'^cancelorder/$', menuhandler.cancelorderView.as_view(), name="cancelorder"),

]
