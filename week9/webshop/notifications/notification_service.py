class NotificationService:
    def __init__(self, methods):
        self.methods = methods

    def send_notification(self, message):
        for method in self.methods:
            method.send(message)
