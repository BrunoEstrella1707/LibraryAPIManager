from django.db import models
from books.models import Book
from users.models import CustomUser


class WishReadList(models.Model):

    WISH = 'WISH'
    READ = 'READ'

    LISTS = (
        (WISH, 'wishlist'),
        (READ, 'readlist'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_list')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_list')
    list_type = models.CharField(max_length=10, choices=LISTS)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}-{self.book}'

