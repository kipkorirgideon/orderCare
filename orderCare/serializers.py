from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['customer_code', ]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['uuid', 'customer', 'item', 'amount']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['id', 'uuid', 'item_name', 'item_amount']
