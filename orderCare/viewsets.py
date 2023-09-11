from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from orderCare.models import Order, Customer, Item
from orderCare.serializers import OrderSerializer, CustomerSerializer, ItemSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []
    lookup_field = 'uuid'

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super(OrderViewSet, self).create(request, *args, **kwargs)

    # @action(detail=False, methods=['get'])
    # def get_orders_by_customer(self, request):
    #     customer_id = request.query_params.get('customer_id')
    #     orders = Order.objects.filter(customer_id=customer_id)
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_orders_by_item_name(self, request):
    #     item_name = request.query_params.get('item_name')
    #     orders = Order.objects.filter(item_name=item_name)
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_orders_by_item_amount(self, request):
    #     item_amount = request.query_params.get('item_amount')
    #     orders = Order.objects.filter(item_amount=item_amount)
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_orders_by_customer_and_item_name(self, request):
    #     customer_id = request.query_params.get('customer_id')
    #     item_name = request.query_params.get('item_name')
    #     orders = Order.objects.filter(customer_id=customer_id, item_name=item_name)
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_orders_by_customer_and_item_amount(self, request):
    #     customer_id = request.query_params.get('customer_id')
    #     item_amount = request.query_params.get('item_amount')
    #     orders = Order.objects.filter(customer_id=customer_id, item_amount=item_amount)
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_orders_by_item_name_and_item_amount(self, request):
    #     item_name = request.query_params.get('item_name')
    #     item_amount = request.query_params.get('item_amount')
    #     orders = Order.objects.filter(item_name=item_name, item_amount=item_amount)
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_orders_by_customer_and_item_name_and_item_amount(self, request):
    #     customer_id = request.query_params.get('customer_id')
    #     item_name = request.query_params.get('item_name')
    #     item_amount = request.query_params.get('item_amount')
    #     orders = Order.objects.filter(customer_id=customer_id, item_name=item_name, item_amount=item_amount)
    #     serializer = OrderSerializer(orders, many=True)
    #     return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = []
    lookup_field = 'customer_code'

    # @action(detail=False, methods=['get'])
    # def get_customers_by_name(self, request):
    #     name = request.query_params.get('name')
    #     customers = Customer.objects.filter(name=name)
    #     serializer = CustomerSerializer(customers, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_customers_by_order(self, request):
    #     order_id = request.query_params.get('order_id')
    #     customers = Customer.objects.filter(order_id=order_id)
    #     serializer = CustomerSerializer(customers, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_customers_by_name_and_order(self, request):
    #     name = request.query_params.get('name')
    #     order_id = request.query_params.get('order_id')
    #     customers = Customer.objects.filter(name=name, order_id=order_id)
    #     serializer = CustomerSerializer(customers, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_customers_by_order_and_name(self, request):
    #     order_id = request.query_params.get('order_id')
    #     name = request.query_params.get('name')
    #     customers = Customer.objects.filter(order_id=order_id, name=name)
    #     serializer = CustomerSerializer(customers, many=True)
    #     return Response(serializer.data)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = []
    lookup_field = 'uuid'

    # @action(detail=False, methods=['get'])
    # def get_items_by_name(self, request):
    #     name = request.query_params.get('name')
    #     items = Item.objects.filter(name=name)
    #     serializer = ItemSerializer(items, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_items_by_order(self, request):
    #     order_id = request.query_params.get('order_id')
    #     items = Item.objects.filter(order_id=order_id)
    #     serializer = ItemSerializer(items, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_items_by_name_and_order(self, request):
    #     name = request.query_params.get('name')
    #     order_id = request.query_params.get('order_id')
    #     items = Item.objects.filter(name=name, order_id=order_id)
    #     serializer = ItemSerializer(items, many=True)
    #     return Response(serializer.data)
    #
    # @action(detail=False, methods=['get'])
    # def get_items_by_order_and_name(self, request):
    #     order_id = request.query_params.get('order_id')
    #     name = request.query_params.get('name')
    #     items = Item.objects.filter(order_id=order_id, name=name)
    #     serializer = ItemSerializer(items, many=True)
    #     return Response(serializer.data)
