from twilio.rest import Client
import smtplib
account_sid = 'AC759fe92fa01dad49f602eff2663d0549'
auth_token = 'c1e8a136af715d14a724f3c87c9fa977'

# ----------------SMTP----------------- #
email = "throwawaytestemail2@gmail.com"
password = "5Tlny6lL45+tj)Nt"

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

    def send_emails(self, data, text):
        for row in data:
            receiver = row["email"]
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email, to_addrs=receiver, msg=text)

