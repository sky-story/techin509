from notifications import NotificationMethod


class SMSNotification(NotificationMethod):
    def send(self, message):
        # use Twilio API
        # Twilio API to send SMS to a phone number
        print(f"Sending SMS: {message}")
