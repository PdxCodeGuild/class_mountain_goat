from django.db import models

class ToDoItem(models.Model):
    description = models.CharField(max_length=200)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description + ' ' + self.created_date.strftime('%Y-%m-%d')

