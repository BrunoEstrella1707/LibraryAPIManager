from rest_framework import serializers
from authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta():
        model = Author
        fields = '__all__'


class AuthorNameSerializer(serializers.ModelSerializer):

    class Meta():
        model = Author
        fields = ['id', 'name']


