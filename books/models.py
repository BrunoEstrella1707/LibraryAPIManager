from django.db import models
from authors.models import Author
from publishers.models import Publisher


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    synopsis = models.CharField(max_length=500, blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='book_publisher')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='book_author')

    def __str__(self):
        return self.title
