from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .sms import africastalking_client as sms, twilio_client as twilio_sms
import django


@receiver(post_save, sender=Order)
def send_order_sms(sender, instance, created, **kwargs):
    if django.conf.settings.USE_TWILIO_SMS:
        twilio_sms.send_message(
            f'Hi {instance.customer.customer_name}, thank you for your order. Your order number is {instance.uuid}. '
            f'Your order will be delivered in 2 business days.',
            django.conf.settings.TWILIO_CUSTOMER_SERVICE_NUMBER
        )
    else:
        sms.send_message(
            f'Hi {instance.customer.customer_name}, thank you for your order. Your order number is {instance.uuid}. '
            f'We will contact you shortly to confirm your order. Your order will be delivered in 2 business days.',
            django.conf.settings.CUSTOMER_SERVICE_NUMBER,
        )

