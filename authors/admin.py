from django.contrib import admin
from authors.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'nationality', 'bio', )


admin.site.register(Author, AuthorAdmin)
