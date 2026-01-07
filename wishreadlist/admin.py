from django.contrib import admin
from .models import WishReadList
# Register your models here.


class WishReadListAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'list_type', 'date', )


admin.register(WishReadList, WishReadListAdmin)