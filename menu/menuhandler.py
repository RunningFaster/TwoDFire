
# Create your views here.
from rest_framework import response, status
from rest_framework.views import APIView
from menu import serializers
import json, time, hashlib, requests
from utils import Myredis
from utils import support
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

'''下单'''
class placeanhoderView(APIView):
    """
    下单
    """

    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.PlaceanhoderSerializer()

    def post(self, request, format=None):
        serializer = serializers.PlaceanhoderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            # sessionToken = request.data['sessionToken']
            thirdpartWMOrderBo = request.data['thirdpartWMOrderBo']
            try:
                '''下单'''
                post_dict = {}
                APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
                now_time = int(time.time())
                # 这三项数据为固定数据，无需修改
                post_dict['timestamp'] = now_time
                post_dict['v'] = 1.0
                post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

                '''请求的方法'''
                post_dict['method'] = 'dfire.thirdpart.wm.order.submit'

                post_msg = dict(
                    address='测试数据',
                    orderId='ylkjrjbm04',  # 自己想的
                    # ylkjrjbm00001
                    # ylkj0001
                    orderFrom=118,
                    viewId='ylkjrjbm04',  # 自己想的
                    phoneNo='13273028239',
                    name='测试数据',
                    outFee=0.0,
                    realPrice=0.1,
                    totalPrice=0.1,
                    memo='餐具',
                    hasInvoiced=True,
                    reserveDate=0,
                    book=True,
                    isThirdShipping=0,
                    daySeq='11',
                    extras='不要辣',
                    peopleCount=2,
                    income=0.1,
                    payType=2,
                    invoiceTitle='haojiujia',
                    cartBoList=[
                        {
                            'menuId': "00134699657bc7d901657e648f9413c3",
                            'name': "测试",
                            'price': 0.01,
                            'num': 10,
                            'fee': 0.1,
                            'boxPrice': 0,
                            'boxNum': 1,
                            'unit': '份',
                            'taste': '不要辣',
                            'memo': '不要辣',
                        },

                    ],
                )
                post_dict['entityId'] = '00134699'
                post_dict['thirdpartWMOrderBo'] = json.dumps(post_msg)

                sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
                res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
                res = hashlib.sha1(res.encode("utf-8")).hexdigest()

                '''签名'''
                post_dict['sign'] = res.upper()
                me = requests.post(url='http://open.2dfire.com/router',
                                   data={'method': post_dict['method'],
                                         'v': post_dict['v'],
                                         'timestamp': post_dict['timestamp'],
                                         'appKey': post_dict['appKey'],
                                         'sign': post_dict['sign'],
                                         'entityId': post_dict['entityId'],
                                         'thirdpartWMOrderBo': post_dict['thirdpartWMOrderBo'],
                                         })

                return response.Response(me.text, status=status.HTTP_202_ACCEPTED)
            except:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''查看订单是否下单成功'''
class checkhodersuccessView(APIView):
    """
    查看订单是否下单成功
    """

    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.checkhodersuccessSerializer()

    def post(self, request, format=None):
        serializer = serializers.checkhodersuccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            outOrderId = request.data['outOrderId']
            # orderFrom = request.data['orderFrom']

            # 固定数据，无需修改
            post_dict, APP_SECRET = support.post_fixed()
            '''请求的方法'''
            post_dict['method'] = "dfire.thirdpart.wm.order.confirm"
            del post_dict['entityId']
            post_dict['outOrderId'] = outOrderId
            post_dict['orderFrom'] = 118

            sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
            res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
            res = hashlib.sha1(res.encode("utf-8")).hexdigest()

            '''签名'''
            post_dict['sign'] = res.upper()
            print(post_dict)
            model = requests.post(url='http://open.2dfire.com/router',
                                  data={'method': post_dict['method'],
                                        'v': post_dict['v'],
                                        'timestamp': post_dict['timestamp'],
                                        'appKey': post_dict['appKey'],
                                        'sign': post_dict['sign'],
                                        'outOrderId': post_dict['outOrderId'],
                                        'orderFrom': post_dict['orderFrom'],
                                        }).text
            return HttpResponse(model)


'''取消订单'''
class cancelorderView(APIView):
    """
    取消订单
    """

    def get_serializer(self):
        # 将rest表单信息展示
        return serializers.cancelorderSerializer()

    def post(self, request, format=None):
        serializer = serializers.cancelorderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            outOrderId = request.data['outOrderId']
            reason = request.data['reason']

            # 固定数据，无需修改
            post_dict, APP_SECRET = support.post_fixed()
            '''请求的方法'''
            post_dict['method'] = "dfire.thirdpart.wm.order.cancel"
            del post_dict['entityId']
            post_dict['outOrderId'] = outOrderId
            post_dict['orderFrom'] = 118
            post_dict['reason'] = reason

            sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
            res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
            res = hashlib.sha1(res.encode("utf-8")).hexdigest()

            '''签名'''
            post_dict['sign'] = res.upper()
            print(post_dict)
            model = requests.post(url='http://open.2dfire.com/router',
                                  data={'method': post_dict['method'],
                                        'v': post_dict['v'],
                                        'timestamp': post_dict['timestamp'],
                                        'appKey': post_dict['appKey'],
                                        'sign': post_dict['sign'],
                                        'outOrderId': post_dict['outOrderId'],
                                        'orderFrom': post_dict['orderFrom'],
                                        'reason': post_dict['reason'],
                                        }).text
            return HttpResponse(model)


'''查询所有的菜品信息'''
def selectmenu(request):
    aglio = request.GET.get('aglio')
    print(aglio)
    '''查询所有菜类信息'''
    result_aglio = Myredis.getAllMenu('AllMenu', 'allagliolist')

    '''查询所有菜品信息'''
    result = Myredis.getAllMenu('AllMenu', 'allmenulist')
    if result == None:
        # import pdb;pdb.set_trace()
        post_dict = {}
        APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
        now_time = int(time.time())
        # 这三项数据为固定数据，无需修改
        post_dict['timestamp'] = now_time
        post_dict['v'] = 1.0
        post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

        '''请求的方法'''
        post_dict['method'] = 'dfire.total.menu.query'
        post_dict['entityId'] = '00134699'

        sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
        res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
        res = hashlib.sha1(res.encode("utf-8")).hexdigest()

        '''签名'''
        post_dict['sign'] = res.upper()

        allmenu = requests.post(url='http://open.2dfire.com/router',

                                data={'method': post_dict['method'],
                                      'v': post_dict['v'],
                                      'timestamp': post_dict['timestamp'],
                                      'appKey': post_dict['appKey'],
                                      'sign': post_dict['sign'],
                                      'entityId': post_dict['entityId'],
                                      }).text
        allmenu = json.loads(allmenu)
        # 说明查询成功
        result = {}
        if allmenu['success'] == True:
            result['success'] = True
            result['message'] = '操作成功'
            result['model'] = allmenu['model']
            Myredis.my_redis.hmset('AllMenu', {'allmenulist': json.dumps(result)})
    # print(result['model'])
    if aglio != None:
        result['model'] = [menu for menu in result['model'] if menu['kindId'] == aglio]
    else:
        result['model'] = [menu for menu in result['model'] if menu['kindId'] == '001346995f2e3416015f4c0537fe4345']
    return render(request, 'market.html', {'result': result, 'result_aglio': result_aglio})
