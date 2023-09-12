from django.apps import AppConfig


class OrdercareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orderCare'

    def ready(self):
        import orderCare.signals
