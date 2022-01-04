from twilio.rest import Client
import smtplib
account_sid = 'AC759fe92fa01dad49f602eff2663d0549'
auth_token = 'c1e8a136af715d14a724f3c87c9fa977'


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_notification(self, text):
        message = self.client.messages.create(
            body=text,
            from_='+14159157364',
            to='+61459619924'
        )

    def send_emails(self, data):
        print(data)