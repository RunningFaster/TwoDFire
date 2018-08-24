
from rest_framework import serializers

class PlaceanhoderSerializer(serializers.Serializer):
    # 指定rest表单信息
    sessionToken = serializers.CharField(write_only=True, help_text="权限验证")
    thirdpartWMOrderBo = serializers.CharField(write_only=True, help_text="下单对象")

    # orderId = serializers.CharField(write_only=True, help_text="第三方外卖平台的外卖编号")
    # orderFrom = serializers.IntegerField(write_only=True, help_text="118：未知", default=118)
    # address = serializers.CharField(write_only=True, help_text="配送地址(配送方式为自取时，可不填)")
    # viewId = serializers.CharField(write_only=True, help_text="第三方外卖平台的外卖编号,orderId")
    # phoneNo = serializers.CharField(write_only=True, help_text="收件人号码")
    # name = serializers.CharField(write_only=True, help_text="收件人姓名")
    # # outFee = serializers.FloatField(write_only=True, help_text="配送费，单位元")
    # realPrice = serializers.FloatField(write_only=True, help_text="消费者实际支付，单位元")
    # totalPrice = serializers.FloatField(write_only=True, help_text="原价，单位元")
    # memo = serializers.CharField(write_only=True, help_text="备注")
    # # courierName = serializers.CharField(write_only=True, help_text="配送员姓名")
    # # courierPhone = serializers.CharField(write_only=True, help_text="配送员号码")
    # hasInvoiced = serializers.BooleanField(write_only=True, help_text="是否支持开发票")
    # invoiceTitle = serializers.CharField(write_only=True, help_text="发票抬头")
    # reserveDate = serializers.IntegerField(write_only=True, help_text="配送时间，下单是可以选择立即送：reserveDate = 0。单位为毫秒。默认为立即送")
    # book = serializers.BooleanField(write_only=True, help_text="是否是预订单（待定）")
    # isThirdShipping = serializers.IntegerField(write_only=True, help_text="配送方式(0 表示自配送 1 表示三方配送 2 表示自取)")
    # daySeq = serializers.CharField(write_only=True, help_text="流水号")
    # extras = serializers.CharField(write_only=True, help_text="活动信息")
    # peopleCount = serializers.IntegerField(write_only=True, help_text="订单人数")
    # income = serializers.FloatField(write_only=True, help_text="商家实收")
    # payType = serializers.IntegerField(write_only=True, help_text="付款方式。1：货到付款 2：在线支付。")
    # payFrom = serializers.IntegerField(write_only=True, help_text="支付来源")
    #
    # # cartBoList = serializers.FloatField(write_only=True, help_text="菜品列表")
    # menuId = serializers.CharField(write_only=True, help_text="菜品ID")
    # vname = serializers.CharField(write_only=True, help_text="菜品名称")
    # price = serializers.FloatField(write_only=True, help_text="菜品价格，单位元")
    # num = serializers.IntegerField(write_only=True, help_text="菜品数量")
    # fee = serializers.FloatField(write_only=True, help_text="菜品总价，单位元")
    # # memo = serializers.CharField(write_only=True, help_text="备注")
    # taste = serializers.CharField(write_only=True, help_text="菜品口味、做法")
    # boxPrice = serializers.FloatField(write_only=True, help_text="打包盒费用，单位元(一道菜)")
    # boxNum = serializers.IntegerField(write_only=True, help_text="打包盒个数(一道菜)")
    # unit = serializers.CharField(write_only=True, help_text="菜品单位")

    def create(self, validated_data):
        sessionToken = validated_data['sessionToken']
        return sessionToken

class BusinessdatabydaySerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="订单数据统计报表（按天或按月）")

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday

class OrdersourcebydaySerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="订单来源统计报表（按天或按月）")

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday

class PaymentorderdatebydaySerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="订单支付统计报表（按天或按月）")

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday

class OrderdatabydaySerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="点菜数据统计报表（按天或按月）")

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday