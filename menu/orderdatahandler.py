from django.shortcuts import render

# Create your views here.
from rest_framework import response, status
from rest_framework.views import APIView
from menu.serializers import \
    PlaceanhoderSerializer, BusinessdatabydaySerializer, \
    OrdersourcebydaySerializer,PaymentorderdatebydaySerializer,OrderdatabydaySerializer
import json, time, hashlib, requests
from utils import Myredis
from utils import support
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


'''订单数据统计报表（按天或按月）'''
class businessdatabydayView(APIView):
    """
    订单数据统计报表（按天或按月）
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return BusinessdatabydaySerializer()

    def post(self, request, format=None):
        serializer = BusinessdatabydaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Businessdata', databyday)
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.shop.day.statistic.data"
                post_dict['currDate'] = databyday
                curr_x = 'currDate'
                if len(databyday) == 6:
                    post_dict['method'] = "dfire.shop.month.statistic.data"
                    post_dict['currMonth'] = databyday
                    del post_dict['currDate']
                    curr_x = 'currMonth'
                sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
                res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
                res = hashlib.sha1(res.encode("utf-8")).hexdigest()

                '''签名'''
                post_dict['sign'] = res.upper()
                model = requests.post(url='http://open.2dfire.com/router',
                                   data={'method': post_dict['method'],
                                         'v': post_dict['v'],
                                         'timestamp': post_dict['timestamp'],
                                         'appKey': post_dict['appKey'],
                                         'sign': post_dict['sign'],
                                         'entityId': post_dict['entityId'],
                                         curr_x: databyday,
                                         }).text
                Myredis.my_redis.hmset('Businessdata', {'databyday': model})
            return HttpResponse(model)


'''订单来源统计报表（按天或按月）'''
class ordersourcebydayView(APIView):
    """
    订单数据统计报表（按天或按月）
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return OrdersourcebydaySerializer()

    def post(self, request, format=None):
        serializer = OrdersourcebydaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Businessdata', databyday)
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.shop.day.platform.data"
                post_dict['currDate'] = databyday
                curr_x = 'currDate'
                if len(databyday) == 6:
                    post_dict['method'] = "dfire.shop.month.platform.data"
                    post_dict['currMonth'] = databyday
                    del post_dict['currDate']
                    curr_x = 'currMonth'
                sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
                res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
                res = hashlib.sha1(res.encode("utf-8")).hexdigest()

                '''签名'''
                post_dict['sign'] = res.upper()
                model = requests.post(url='http://open.2dfire.com/router',
                                   data={'method': post_dict['method'],
                                         'v': post_dict['v'],
                                         'timestamp': post_dict['timestamp'],
                                         'appKey': post_dict['appKey'],
                                         'sign': post_dict['sign'],
                                         'entityId': post_dict['entityId'],
                                         curr_x: databyday,
                                         }).text
                Myredis.my_redis.hmset('Businessdata', {'databyday': model})
            return HttpResponse(model)


'''订单支付统计报表（按天或按月）'''
class paymentorderdatebydayView(APIView):
    """
    订单数据统计报表（按天或按月）
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return PaymentorderdatebydaySerializer()

    def post(self, request, format=None):
        serializer = PaymentorderdatebydaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Businessdata', databyday)
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.shop.day.payment.data"
                post_dict['currDate'] = databyday
                curr_x = 'currDate'
                if len(databyday) == 6:
                    post_dict['method'] = "dfire.shop.month.payment.data"
                    post_dict['currMonth'] = databyday
                    del post_dict['currDate']
                    curr_x = 'currMonth'
                sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
                res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
                res = hashlib.sha1(res.encode("utf-8")).hexdigest()

                '''签名'''
                post_dict['sign'] = res.upper()
                model = requests.post(url='http://open.2dfire.com/router',
                                   data={'method': post_dict['method'],
                                         'v': post_dict['v'],
                                         'timestamp': post_dict['timestamp'],
                                         'appKey': post_dict['appKey'],
                                         'sign': post_dict['sign'],
                                         'entityId': post_dict['entityId'],
                                         curr_x: databyday,
                                         }).text
                Myredis.my_redis.hmset('Businessdata', {'databyday': model})
            return HttpResponse(model)


'''订单支付统计报表（按天或按月）'''
class orderdatabydayView(APIView):
    """
    订单数据统计报表（按天或按月）
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return OrderdatabydaySerializer()

    def post(self, request, format=None):
        serializer = OrderdatabydaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Businessdata', databyday)
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.shop.day.memu.data"
                post_dict['currDate'] = databyday
                curr_x = 'currDate'
                if len(databyday) == 6:
                    post_dict['method'] = "dfire.shop.month.memu.data"
                    post_dict['currMonth'] = databyday
                    del post_dict['currDate']
                    curr_x = 'currMonth'
                sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
                res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
                res = hashlib.sha1(res.encode("utf-8")).hexdigest()

                '''签名'''
                post_dict['sign'] = res.upper()
                model = requests.post(url='http://open.2dfire.com/router',
                                   data={'method': post_dict['method'],
                                         'v': post_dict['v'],
                                         'timestamp': post_dict['timestamp'],
                                         'appKey': post_dict['appKey'],
                                         'sign': post_dict['sign'],
                                         'entityId': post_dict['entityId'],
                                         curr_x: databyday,
                                         }).text
                Myredis.my_redis.hmset('Businessdata', {'databyday': model})
            return HttpResponse(model)