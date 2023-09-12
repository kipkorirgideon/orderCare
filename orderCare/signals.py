from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .sms import africastalking_client as sms
import django


# @receiver(post_save, sender=Order)
# def aggregate_order(sender, instance, created, **kwargs):
#     if created:
#         # Get all items in the order
#         items = instance.customer_set.all()
#         print(items)
#         # # Sum all item_amounts
#         # total_amount = sum(items_amounts)
#         # # Save the total_amount to the order's total_amount field
#         # instance.amount = total_amount
#         # instance.save()
#
#         # send sms to the customer
#         sms.send_message(
#             f'Hi {instance.customer.customer_name}, thank you for your order. Your order number is {instance.uuid}. '
#             f'We will contact you shortly to confirm your order.',
#             django.conf.settings.CUSTOMER_SERVICE_NUMBER,
#         )
