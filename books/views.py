from rest_framework import generics
from books.serializers import BookSerializer, BookListDetailSerializer
from books.models import Book
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




