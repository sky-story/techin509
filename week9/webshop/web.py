# Services
from notifications.notification_service import NotificationService
# from account_service import AccountService

# Notifications
from notifications.sms import SMSNotification
from notifications.email import EmailNotification

# Logins
# from accounts.google import GoogleLogin
# from accounts.twitter import TwitterLogin


sms_notifier = SMSNotification()
email_notifier = EmailNotification()

notification_service = NotificationService([sms_notifier, email_notifier])

print("Welcome to my shop")
notification_service.send_notification("hello, this is a notification")
