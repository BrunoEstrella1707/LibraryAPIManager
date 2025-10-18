from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'synopsis', 'pages', 'author', )


admin.site.register(Book, BookAdmin)
