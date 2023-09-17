from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from orderCare.models import Order, Customer, Item
from orderCare.serializers import OrderSerializer, CustomerSerializer, ItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = 'uuid'

    def create(self, request, *args, **kwargs):
        order_amount = Item.objects.filter(id__in=request.data['item']).aggregate(Sum('item_amount'))
        request.data['amount'] = order_amount['item_amount__sum']
        return super(OrderViewSet, self).create(request, *args, **kwargs)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = 'customer_code'


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    lookup_field = 'uuid'
