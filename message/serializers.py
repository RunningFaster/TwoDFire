
from rest_framework import serializers

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

class OrderdatalistSerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="查询店铺订单列表（按天）")

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday

class OrderdetailslistSerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="查询店铺订单列表（按天）")
    orderIds = serializers.CharField(write_only=True, help_text='["10001","10002"]')

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday


class StorepaymentreceiptSerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="查询店铺支付流水")

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday

class RetailordersSerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="零售订单列表")

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday

class RetailreturnorderSerializer(serializers.Serializer):
    # 指定rest表单信息
    databyday = serializers.CharField(write_only=True, help_text="零售退货订单列表")

    def create(self, validated_data):
        databyday = validated_data['databyday']
        return databyday