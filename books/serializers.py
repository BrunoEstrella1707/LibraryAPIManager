from rest_framework import serializers
from books.models import Book
from authors.serializers import AuthorNameSerializer
from publishers.serializers import PublisherSerializer


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        
    
class BookListDetailSerializer(serializers.ModelSerializer):
    author = AuthorNameSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'release_date', 'synopsis', 'pages', 'publisher', 'author']


