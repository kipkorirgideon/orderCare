import model_utils.models
import uuid
from django.db import models
from native_shortuuid import NativeShortUUIDField


# Create your models here.
class Customer(model_utils.models.TimeStampedModel):
    user_ptr = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='customer')
    customer_code = NativeShortUUIDField(unique=True, default=uuid.uuid4)
    customer_name = models.CharField(max_length=200)

    def __str__(self):
        return self.customer_name


class Item(model_utils.models.TimeStampedModel):
    uuid = NativeShortUUIDField(unique=True, default=uuid.uuid4)
    item_name = models.CharField(max_length=200, blank=False)
    item_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name


class Order(model_utils.models.TimeStampedModel):
    uuid = NativeShortUUIDField(unique=True, default=uuid.uuid4)
    customer = models.ForeignKey('orderCare.Customer', on_delete=models.CASCADE, related_name='customer_orders', null=True)
    item = models.ManyToManyField('orderCare.Item', related_name='ordered_items', blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
