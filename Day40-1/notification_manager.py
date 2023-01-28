from twilio.rest import Client

TWILIO_SID = "AC106296c97ef6fdd940deb0aeec3dbd2c"
TWILIO_AUTH_TOKEN = "22a448add80422df33e8d23de45903aa"
TWILIO_VIRTUAL_NUMBER = '+19387777541'
TWILIO_VERIFIED_NUMBER = '+526643676744'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
