from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    image = models.ImageField(upload_to='profile_images/', null=True)

    def name(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        return self.name()
