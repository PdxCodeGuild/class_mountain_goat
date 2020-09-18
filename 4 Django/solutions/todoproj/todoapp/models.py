from django.db import models


class TodoItem(models.Model):
    text = models.CharField(max_length=500)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.text
    