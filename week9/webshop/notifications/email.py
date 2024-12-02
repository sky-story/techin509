from notifications import NotificationMethod


class EmailNotification(NotificationMethod):
    def send(self, message):
        # use Gmail API
        # Create email message object
        # send GMail API
        print(f"Sending email: {message}")
