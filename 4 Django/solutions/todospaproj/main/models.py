from django.db import models


class Priority(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todo_items')
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text

