from rest_framework import generics, views, response, status
from django.db.models import Avg, Count
from books.serializers import BookSerializer, BookListDetailSerializer, BookReviewListSerializer, BookStatsSerializer
from books.models import Book
from reviews.models import Review
from rest_framework.permissions import IsAuthenticated, AllowAny


class BookCreateListView(generics.ListCreateAPIView):

    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListDetailSerializer
        return BookSerializer


    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
        

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookListDetailSerializer
        return BookSerializer
        

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
        

class BooksByAuthor(generics.ListAPIView):
    
    serializer_class = BookListDetailSerializer
    
    def get_queryset(self):
        author_id = self.kwargs["author_id"]
        return Book.objects.filter(author_id=author_id)


class BooksByPubliser(generics.ListAPIView):

    serializer_class = BookListDetailSerializer

    def get_queryset(self):
        publisher_id = self.kwargs["publisher_id"]
        return Book.objects.filter(publisher_id=publisher_id)
    

class BookReviewsView(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookReviewListSerializer
        return BookSerializer
        
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class BookStatsView(views.APIView):
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()

    def get(self, request):
        total = self.queryset.count()
        books_by_author = self.queryset.values('author__name').annotate(count=Count("id"))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data={
            'total_books': total,
            'books_by_author': books_by_author,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0}
        
        serializer = BookStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)


        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK
        )
    

    





