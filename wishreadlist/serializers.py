from datetime import datetime, date
from rest_framework import serializers
from .models import WishReadList
from users.models import CustomUser
from books.models import Book


class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishReadList
        fields = ['book', 'date']
        read_only_fields = ['date']
    

    def validate(self, attrs):
        user = self.context["request"].user
        book = attrs["book"]

        if WishReadList.objects.filter(
            user=user,
            book=book,
            list_type=WishReadList.WISH
        ).exists():
            raise serializers.ValidationError("Book is alredy on the wishlist.")
        
        return attrs
    

class ReadListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishReadList
        fields = ['book', 'date']

    
    def validate(self, attrs):
        user = self.context["request"].user
        book = attrs["book"]

        if WishReadList.objects.filter(
            user=user, 
            book=book, 
            list_type=WishReadList.READ
        ).exists():
            raise serializers.ValidationError("Book is alredy on the readlist.")
    
        return attrs

    def validate_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Invalid read date.")
        return value
