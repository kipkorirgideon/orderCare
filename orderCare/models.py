import model_utils.models
import uuid
from django.db import models
from native_shortuuid import NativeShortUUIDField


# Create your models here.
class Customer(model_utils.models.TimeStampedModel):
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
    customer = models.ForeignKey('orderCare.Customer', on_delete=models.CASCADE, related_name='customer_orders', null=False)
    item = models.ManyToManyField('orderCare.Item', related_name='ordered_items', blank=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    # def __str__(self):
    #     return self.uuid

    # def save(self, *args, **kwargs):
    #     self.amount = self.item.ordered_items.all().aggregate(models.Sum('item_amount'))['item_amount__sum']
    #     return super(Order, self).save(*args, **kwargs)

