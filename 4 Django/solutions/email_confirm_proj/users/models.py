from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email_address_confirmed = models.BooleanField(default=False)


class EmailConfirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='email_confirmations')
    code = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)
    date_confirmed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username + ' ' + self.code

    



