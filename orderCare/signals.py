from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .sms import africastalking_client as sms
import django


@receiver(post_save, sender=Order)
def send_order_sms(sender, instance, created, **kwargs):
    sms.send_message(
        f'Hi {instance.customer.customer_name}, thank you for your order. Your order number is {instance.uuid}. '
        f'We will contact you shortly to confirm your order.',
        django.conf.settings.CUSTOMER_SERVICE_NUMBER,
    )
