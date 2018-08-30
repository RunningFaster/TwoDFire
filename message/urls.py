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
    # 营业数据统计接口
    url(r'^businessdatabyday/$', messagedatahandler.businessdatabydayView.as_view(), name="businessdatabyday"),
    url(r'^ordersourcebyday/$', messagedatahandler.ordersourcebydayView.as_view(), name="ordersourcebyday"),
    url(r'^paymentorderdatebyday/$', messagedatahandler.paymentorderdatebydayView.as_view(), name="paymentorderdatebyday"),
    url(r'^orderdatabyday/$', messagedatahandler.orderdatabydayView.as_view(), name="orderdatabyday"),
    # 订单数据接口
    url(r'^orderdatalist/$', messagedatahandler.orderdatalistView.as_view(), name="orderdatalist"),
    url(r'^orderdetailslist/$', messagedatahandler.orderdetailslistView.as_view(), name="orderdetailslist"),
    url(r'^storepaymentreceipt/$', messagedatahandler.storepaymentreceiptView.as_view(), name="storepaymentreceipt"),
    url(r'^retailorders/$', messagedatahandler.retailordersView.as_view(), name="retailorders"),
    url(r'^retailreturnorder/$', messagedatahandler.retailreturnorderView.as_view(), name="retailreturnorder"),

]
