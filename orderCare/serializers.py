from rest_framework import serializers

from . import models


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Customer
        fields = ['customer_code', 'customer_name']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['uuid', 'customer', 'item', 'amount']


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        fields = ['uuid', 'item_name', 'item_amount']
