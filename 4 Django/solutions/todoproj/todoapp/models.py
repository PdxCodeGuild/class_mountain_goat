from django.db import models




class Priority(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField()
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.text











