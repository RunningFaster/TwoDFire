import time, hashlib
import requests, json

'''下单'''
def placeanhoder():
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
        address='教工222552号',
        orderId='0001',  # 自己想的
        orderFrom=118,

        viewId='0001',  # 自己想的
        phoneNo='13273028239',
        name='网二',
        outFee=0.0,
        realPrice=7800.0,
        totalPrice=7800.0,
        memo='两份餐具',
        hasInvoiced=True,
        reserveDate=0,
        book=True,
        isThirdShipping=0,
        daySeq='2',
        extras='不要辣',
        peopleCount=2,
        income=0.0,
        payType=1,
        cartBoList=[
            {
                'menuId': "001346995f2e335f015f4c4636ad4747",
                'name': "水煮鱼片",
                'price': 7800.0,
                'num': 1,
                'fee': 7800.0,
                'boxPrice': 2.0,
                'boxNum': 1,
                'unit': '份',
                'taste': '不要辣',
                'memo': '不要辣',
            }
        ],
        invoiceTitle='haojiujia',
    )

    post_dict['entityId'] = '00134699'
    post_dict['thirdpartWMOrderBo'] = json.dumps(post_msg)

    sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))

    res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET

    res = hashlib.sha1(res.encode("utf-8")).hexdigest()

    print(post_msg)
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
    print(me.text)
# placeanhoder()
'''查看订单是否下单成功'''
def Checkwhethertheorder():
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    '''这三项数据为固定数据，无需修改'''
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"
    '''请求的方法'''
    post_dict['method'] = 'dfire.thirdpart.wm.order.confirm'
    # post_dict['entityId'] = '00134699'

    post_dict['outOrderId'] = 'ylkj0001'
    post_dict['orderFrom'] = 118

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
                             # 'entityId': post_dict['entityId'],
                             'outOrderId': post_dict['outOrderId'],
                             'orderFrom': post_dict['orderFrom'],
                             })
    print(me.text)
# Checkwhethertheorder()
'''取消订单'''
def cancellationoforder():
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    '''这三项数据为固定数据，无需修改'''
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"
    '''请求的方法'''
    post_dict['method'] = 'dfire.thirdpart.wm.order.cancel'
    # post_dict['entityId'] = '00134699'

    post_dict['outOrderId'] = '0001'
    post_dict['orderFrom'] = 118
    post_dict['reason'] = '测试信息'

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
                             # 'entityId': post_dict['entityId'],
                             'outOrderId': post_dict['outOrderId'],
                             'orderFrom': post_dict['orderFrom'],
                             'reason': post_dict['reason'],
                             })
    print(me.text)
# cancellationoforder()
'''查询所有菜品信息'''
def searchHotelDishes():
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

    me = requests.post(url='http://open.2dfire.com/router',

                       data={'method': post_dict['method'],
                             'v': post_dict['v'],
                             'timestamp': post_dict['timestamp'],
                             'appKey': post_dict['appKey'],
                             'sign': post_dict['sign'],
                             'entityId': post_dict['entityId'],
                             }).text
    print(me)
# searchHotelDishes()
'''查询绑定店铺列表'''
def quertTheBindStoreList():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.shop.list"

    sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
    res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
    res = hashlib.sha1(res.encode("utf-8")).hexdigest()

    '''签名'''
    post_dict['sign'] = res.upper()

    me = requests.post(url='http://open.2dfire-daily.com/router',
                       data={'method': post_dict['method'],
                             'v': post_dict['v'],
                             'timestamp': post_dict['timestamp'],
                             'appKey': post_dict['appKey'],
                             'sign': post_dict['sign'],
                             }).text
    print(me)
# quertTheBindStoreList()
'''根据连锁店铺ID获取品牌信息'''
def obtainBrandById():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.shop.plate.data"
    post_dict['entityId'] = "00134699"

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
                             }).text
    print(me)
# obtainBrandById()
'''查询商铺的单个菜品信息'''
def queryIndividualmenuinformation():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.single.menu.query"
    post_dict['itemId'] = "00134699657bc7d901657e648f9413c3"
    post_dict['entityId'] = "00134699"

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
                             'itemId': post_dict['itemId'],
                             'entityId': post_dict['entityId'],
                             }).text
    print(me)
# queryIndividualmenuinformation()
'''查询店铺订单详情列表'''
def checkorderlist():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.shop.order.instance.list"
    # post_dict['itemId'] = "001346995f2e341a015f4c05f2dc660e"
    post_dict['entityId'] = "00134699"
    post_dict['orderIds'] = '["ylkjrjbm02"]'
    post_dict['currDate'] = "20180824"

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
                             # 'itemId': post_dict['itemId'],
                             'entityId': post_dict['entityId'],
                             'orderIds': post_dict['orderIds'],
                             'currDate': post_dict['currDate'],
                             }).text
    print(me)
# checkorderlist()
'''订单数据统计报表（按月）'''
def Orderstatisticsreportbymonth():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.shop.month.statistic.data"
    post_dict['entityId'] = "00134699"
    post_dict['currMonth'] = '201807'

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
                             'currMonth': post_dict['currMonth'],
                             }).text
    print(me)
# Orderstatisticsreportbymonth()
'''订单数据统计报表（按天）'''
def Orderstatisticsreportbyday():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.shop.day.statistic.data"
    post_dict['entityId'] = "00134699"
    post_dict['currDate'] = '20180823'

    sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
    res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
    res = hashlib.sha1(res.encode("utf-8")).hexdigest()

    '''签名'''
    post_dict['sign'] = res.upper()
    # print(post_dict)
    me = requests.post(url='http://open.2dfire.com/router',
                       data={'method': post_dict['method'],
                             'v': post_dict['v'],
                             'timestamp': post_dict['timestamp'],
                             'appKey': post_dict['appKey'],
                             'sign': post_dict['sign'],
                             'entityId': post_dict['entityId'],
                             'currDate': post_dict['currDate'],
                             }).text
    print(me)
# Orderstatisticsreportbyday()
'''查询店铺订单列表'''
def Querythestoreorderlist():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.shop.order.list"
    post_dict['entityId'] = "00134699"
    post_dict['currDate'] = '20180821'

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
                             'currDate': post_dict['currDate'],
                             }).text
    print(me)
# Querythestoreorderlist()
'''查询会员卡信息列表'''
def Querythemembershipcardinformationlist():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.shop.member.card.list"
    post_dict['entityId'] = "00134699"

    post_dict['locale'] = 'zh_CN'
    post_dict['mobile'] = '111'
    # post_dict['code'] = ''

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
                             'locale': post_dict['locale'],
                             'mobile': post_dict['mobile'],
                             # 'code': post_dict['code'],
                             }).text
    print(me)
# Querythemembershipcardinformationlist()
'''保存会员信息'''
def Savememerinformation():
    # 固定数据，无需修改
    post_dict = {}
    APP_SECRET = "d67ee437b292c992b8c34b5ea984139c"
    now_time = int(time.time())
    post_dict['timestamp'] = now_time
    post_dict['v'] = 1.0
    post_dict['appKey'] = "69966cafe1d22ebcf8c48907339d3e4d"

    '''请求的方法'''
    post_dict['method'] = "dfire.member.save"
    post_dict['locale'] = 'zh_CN'
    post_dict['entityId'] = "00134699"

    sorted_x = dict(sorted(post_dict.items(), key=lambda x: x[0]))
    res = APP_SECRET + ''.join([str(key) + str(sorted_x[key]) for key in sorted_x]) + APP_SECRET
    res = hashlib.sha1(res.encode("utf-8")).hexdigest()

    '''签名'''
    post_dict['sign'] = res.upper()

    '''
    [{“source”:3,”kindCardName”:”金卡”, ”code”:”1004”, ”innerCode”:”1003”, ”customerName”:”毛豆”, 
    ”mobile”:”15057162790”, ”countryCode”:”+86”, ”sex”:1,”birth”:”2017 / 07 / 21”, 
    ”balance”:0,”baseBalance”:0,”giveBalance”:0,”giftBalance”:0,”realBalance”:0,
    ”degree”:0,”payAmount”:0,”ratioAmount”:0,”status”:1,”pay”:0,”consumeAmount”:0,
    ”lastConsumeTime”:0,”consumeNum”:0,”kindCardType”:1,”pledge”:0,”refundAmount”:0,
    ”mode”:3,”ratio”:100,”applyShopEntityIdList”:[“99932176”]}],
    '''
    post_dict['cardList'] = list(dict(
        source=1,
        kindCardName='1卡',
        code='123421',
        mobile='15057162790',
        countryCode='+86',
    ))
    me = requests.post(url='http://open.2dfire.com/router',
                       data={'method': post_dict['method'],
                             'v': post_dict['v'],
                             'timestamp': post_dict['timestamp'],
                             'appKey': post_dict['appKey'],
                             'sign': post_dict['sign'],
                             'entityId': post_dict['entityId'],
                             'cardList': post_dict['cardList'],
                             'locale': post_dict['locale'],
                             }).text
    print(me)
# Savememerinformation()

url = 'http://127.0.0.1:8000/order/orderdatalist/'
header = {'API-KEY':'d36b7c12-8535-4940-963b-5cfead94d1bc'}

data = {'databyday': '20180706'}

res = requests.post(url=url, headers=header,data=data)
# res = requests.get(url=url)
print(res.text)