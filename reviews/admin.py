from django.contrib import admin
from .models import Review

# Register your models here.
class ReviewAdimin(admin.ModelAdmin):
    list = ('book', 'stars', 'comment', )


admin.site.register(Review, ReviewAdimin)