from django.db import models
from books.models import Book
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviewer', blank=True, null=True)
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Rate the book from 0 to 5 stars!'),
            MaxValueValidator(5, 'Rate the book from 0 to 5 stars')
        ]
    )
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.book}'
