from django.shortcuts import render

# Create your views here.
from rest_framework import response, status
from rest_framework.views import APIView
from message import serializers
import json, time, hashlib, requests
from utils import Myredis
from utils import support
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


'''订单数据统计报表'''
class businessdatabydayView(APIView):
    """
    订单数据统计报表
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.BusinessdatabydaySerializer()

    def post(self, request, format=None):
        serializer = serializers.BusinessdatabydaySerializer(data=request.data)
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
                # print(json.dumps(json.loads(model)))
            return HttpResponse(model)


'''订单来源统计报表'''
class ordersourcebydayView(APIView):
    """
    订单来源统计报表
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.OrdersourcebydaySerializer()

    def post(self, request, format=None):
        serializer = serializers.OrdersourcebydaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Ordersource', databyday)
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
                Myredis.my_redis.hmset('Ordersource', {'databyday': model})
            return HttpResponse(model)


'''订单支付统计报表'''
class paymentorderdatebydayView(APIView):
    """
    订单支付统计报表
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.PaymentorderdatebydaySerializer()

    def post(self, request, format=None):
        serializer = serializers.PaymentorderdatebydaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Paymentorderdate', databyday)
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
                Myredis.my_redis.hmset('Paymentorderdate', {'databyday': model})
            return HttpResponse(model)


'''点菜数据统计报表'''
class orderdatabydayView(APIView):
    """
    点菜数据统计报表
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.OrderdatabydaySerializer()

    def post(self, request, format=None):
        serializer = serializers.OrderdatabydaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            # databyday = databyday.replace('-','')
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Orderdata', databyday)
            # print(model)
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
                Myredis.my_redis.hmset('Orderdata', {'databyday': model})
            return HttpResponse(model)


'''查询店铺订单列表'''
class orderdatalistView(APIView):
    """
    查询店铺订单列表（按天）
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.OrderdatalistSerializer()

    def post(self, request, format=None):
        serializer = serializers.OrderdatalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            # model = Myredis.getAllMenu('Orderdatalist', databyday)
            model = None
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.shop.order.list"
                post_dict['currDate'] = databyday
                curr_x = 'currDate'

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
                Myredis.my_redis.hmset('Orderdatalist', {'databyday': model})
                print(model)
            return HttpResponse(model)


'''查询店铺订单详情列表'''
class orderdetailslistView(APIView):
    """
    查询店铺订单列表（按天）
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.OrderdetailslistSerializer()

    def post(self, request, format=None):
        serializer = serializers.OrderdetailslistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            orderIds = request.data['orderIds']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Orderdetailslist', databyday)
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.shop.order.instance.list"
                post_dict['currDate'] = databyday
                post_dict['orderIds'] = orderIds
                curr_x = 'currDate'

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
                                         'orderIds': post_dict['orderIds'],
                                         curr_x: databyday,
                                         }).text
                Myredis.my_redis.hmset('Orderdetailslist', {'databyday': model})
            return HttpResponse(model)


'''查询店铺支付流水'''
class storepaymentreceiptView(APIView):
    """
    查询店铺订单列表（按天）
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.StorepaymentreceiptSerializer()

    def post(self, request, format=None):
        serializer = serializers.StorepaymentreceiptSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Storepaymentreceipt', databyday)
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.shop.paymentflow.query"
                post_dict['currDate'] = databyday
                curr_x = 'currDate'

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
                Myredis.my_redis.hmset('Storepaymentreceipt', {'databyday': model})
            return HttpResponse(model)


'''查询店铺支付流水'''
class retailordersView(APIView):
    """
    零售订单列表
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.RetailordersSerializer()

    def post(self, request, format=None):
        serializer = serializers.RetailordersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Storepaymentreceipt', databyday)
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.retail.shop.order.list"
                post_dict['currDate'] = databyday
                curr_x = 'currDate'

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
                Myredis.my_redis.hmset('Storepaymentreceipt', {'databyday': model})
            return HttpResponse(model)


'''零售退货订单列表'''
class retailreturnorderView(APIView):
    """
    零售退货订单列表
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.RetailreturnorderSerializer()

    def post(self, request, format=None):
        serializer = serializers.RetailreturnorderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            databyday = request.data['databyday']
            '''查询cache中当天订单数据'''
            model = Myredis.getAllMenu('Storepaymentreceipt', databyday)
            if model == None:
                # 固定数据，无需修改
                post_dict, APP_SECRET = support.post_fixed()
                '''请求的方法'''
                post_dict['method'] = "dfire.retail.shop.order.return.list"
                post_dict['currDate'] = databyday
                curr_x = 'currDate'

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
                Myredis.my_redis.hmset('Storepaymentreceipt', {'databyday': model})
            return HttpResponse(model)