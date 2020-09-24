from django.db import models
from django.utils import timezone
from datetime import datetime

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    birthday = models.DateField()

    def name(self):
        return self.first_name + ' ' + self.last_name

    def age(self):
        # today = datetime.now()
        # this_year_birthday = datetime(today.year, self.birthday.month, self.birthday.day)
        # return today.year - self.birthday.year - (this_year_birthday >= today)

        today = datetime.now()
        return (today - datetime(self.birthday.year, self.birthday.month, self.birthday.day)).days // 365 
    

    
    def __str__(self):
        return self.name()


