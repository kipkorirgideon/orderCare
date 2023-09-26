import africastalking
import django
from twilio.rest import Client


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


class TwilioClient:
    def __init__(self):
        self.twilio_sender_id = django.conf.settings.TWILIO_ACCOUNT_SID
        self.twilio_auth_token = django.conf.settings.TWILIO_AUTH_TOKEN
        self.twilio_from_number = django.conf.settings.TWILIO_FROM_NUMBER
        self.client = Client(self.twilio_sender_id, self.twilio_auth_token)

    def send_message(self, body, to):
        try:
            self.client.messages.create(
                body=body,
                from_=self.twilio_from_number,
                to=to
            )
        except Exception as e:
            print(f'Failed sending sms message using twilio {e}')

        return body


africastalking_client = AfricasTalkingClient()
twilio_client = TwilioClient()
