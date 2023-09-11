import africastalking
import django


class AfricasTalkingClient:
    def __init__(self):
        self.sender_id = django.conf.settings.AFRICAS_TALKING_SENDER_ID
        africastalking.initialize(
            django.conf.settings.AFRICAS_TALKING_USERNAME,
            django.conf.settings.AFRICAS_TALKING_API_KEY)
        self.africas_talking_client = africastalking.SMS

    def send_message(self, body, to):
        try:
            self.africas_talking_client.send(body, [to], self.sender_id)
        except Exception as e:
            print(f'Failed sending sms message using africas talking {e}')

        return body


africastalking_client = AfricasTalkingClient()
