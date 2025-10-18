from rest_framework import serializers
from django.db.models import Avg
from books.models import Book
from authors.serializers import AuthorNameSerializer
from publishers.serializers import PublisherSerializer
from reviews.serializers import ReviewSerializer


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
        
    
class BookListDetailSerializer(serializers.ModelSerializer):
    author = AuthorNameSerializer()
    publisher = PublisherSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'rate', 'release_date', 'synopsis', 'pages', 'publisher', 'author']
    

    def get_rate(self, object):
        rate = object.reviews.aggregate(Avg('stars'))['stars__avg']
    
        if rate:
            return round(rate, 2)
        
        return None


class BookReviewListSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'reviews']
    
    def get_reviews(self, obj):
        # Ordena as reviews do livro antes de serializar
        reviews = obj.reviews.all().order_by('-stars')  # '-stars' = da maior para a menor nota
        return ReviewSerializer(reviews, many=True).data


class BookStatsSerializer(serializers.Serializer):

    total_books = serializers.IntegerField()
    books_by_author = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()

