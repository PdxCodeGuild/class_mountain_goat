from django.db import models

# Create your models here.
class AddressContact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=40)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name