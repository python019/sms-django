import os
from django.db import models
from twilio.rest import Client

class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = os.environ['TWILIO_ACCOUNT_SID']
            auth_token = os.environ['TWILIO_AUTH_TOKEN']
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                                        body="SUSYSda korsatgan natijangiz yomon {self.result}",
                                        from_='+998991234567',
                                        to='+998991234567'
                                    )

            print(message.sid)
        return super().save(*args, **kwargs)