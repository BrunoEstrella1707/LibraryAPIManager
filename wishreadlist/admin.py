from django.contrib import admin
from .models import WishReadList


class WishReadListAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'list_type', 'date', )


admin.site.register(WishReadList, WishReadListAdmin)