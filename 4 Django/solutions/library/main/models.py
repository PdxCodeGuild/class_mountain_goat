from django.db import models





class Book(models.Model):
    title = models.CharField(max_length=200)
    year_published = models.IntegerField()
    # authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return f'{self.year_published} {self.title}'

class Author(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return self.name

