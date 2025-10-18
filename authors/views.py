from rest_framework import generics
from authors.serializers import AuthorSerializer
from authors.models import Author
from rest_framework.permissions import IsAuthenticated, AllowAny


class AuthorListCreateView(generics.ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
        

class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


