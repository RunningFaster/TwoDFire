from django.shortcuts import render
import json, time, hashlib, requests
from utils import Myredis
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


'''下单'''
class placeanhoderView(APIView):
    """
    下单
    """
    def get_serializer(self):
        # 将rest表单信息展示
        return PlaceanhoderSerializer()

    def post(self, request, format=None):
        serializer = PlaceanhoderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 获取到传递的参数,房间信息
            sessionToken = request.data['sessionToken']
            thirdpartWMOrderBo = request.data['thirdpartWMOrderBo']
            try:
                '''下单'''
                result = None
                if result == None:
                    post_dict = {}
                    APP_SECRET = "d67ee437b292c992b8c34b5ea984139cABC"
                    now_time = int(time.time())
                    # 这三项数据为固定数据，无需修改
                    post_dict['timestamp'] = now_time
                    post_dict['v'] = 1.0
                    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

                    '''请求的方法'''
                    post_dict['method'] = 'dfire.thirdpart.wm.order.submit'
                    #
                    # post_msg = dict(
                    #     address='教工222552号',
                    #     orderId='0001',  # 自己想的
                    #     orderFrom=118,
                    #
                    #     viewId='0001',  # 自己想的
                    #     phoneNo='13273028239',
                    #     name='网二',
                    #     outFee=0.0,
                    #     realPrice=7800.0,
                    #     totalPrice=7800.0,
                    #     memo='两份餐具',
                    #     hasInvoiced=True,
                    #     reserveDate=0,
                    #     book=True,
                    #     isThirdShipping=0,
                    #     daySeq='2',
                    #     extras='不要辣',
                    #     peopleCount=2,
                    #     income=0.0,
                    #     payType=1,
                    #     cartBoList=[
                    #         {
                    #             'menuId': "001346995f2e335f015f4c4636ad4747",
                    #             'name': "水煮鱼片",
                    #             'price': 7800.0,
                    #             'num': 1,
                    #             'fee': 7800.0,
                    #             'boxPrice': 2.0,
                    #             'boxNum': 1,
                    #             'unit': '份',
                    #             'taste': '不要辣',
                    #             'memo': '不要辣',
                    #         }
                    #     ],
                    #     invoiceTitle='haojiujia',
                    # )
                    post_msg = {}
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

                    Myredis.my_redis.hmset('AllMenu', {'allagliolist': json.dumps(result)})
                # return response.Response(json.dumps(result), status=status.HTTP_202_ACCEPTED)
                return response.Response(result, status=status.HTTP_202_ACCEPTED)
            except:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''查询所有的菜品信息'''
def selectmenu(request):
    try:
        aglio = request.GET.get('aglio')
    except:
        aglio = 0
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
            # menu_msg = []
            # for menu in allmenu['model']:
            #     try:
            #         pic = menu['pic']
            #     except:
            #         pic = ''
            #     newmenu = dict(
            #         menuId=menu['id'],
            #         menuName=menu['name'],
            #         price=menu['price'],
            #         unit=menu['unit'],
            #         # 父类
            #         kindId=menu['kindId'],
            #         kindNm=menu['kindName'],
            #         # 最小起订份数，默认且最小为1
            #         startNum=menu['startNum'],
            #         # 顺序码
            #         sort=menu['sort'],
            #         # 是否估清
            #         isSoldOut=menu['soldOut'],
            #         # 辛辣指数，默认为0：不辣
            #         acridLevel=menu['acridLevel'],
            #         pic=pic,
            #     )
            #     menu_msg.append(newmenu)
            result['success'] = True
            result['message'] = '操作成功'
            result['model'] = allmenu['model']
            Myredis.my_redis.hmset('AllMenu', {'allmenulist': json.dumps(result)})
    if aglio != 0:
        result['model'] = [menu for menu in result['model'] if menu['kindId']==aglio]
    print(result['model'])
    return render(request, 'market.html', {'result': result, 'result_aglio': result_aglio})
