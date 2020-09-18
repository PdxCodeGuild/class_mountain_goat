from django.db import models


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.text











