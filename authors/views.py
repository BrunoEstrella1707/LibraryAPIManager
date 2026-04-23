from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from authors.filters import AuthorFilterSet
from authors.serializers import AuthorSerializer
from authors.models import Author
from rest_framework.permissions import IsAuthenticated, AllowAny


class AuthorPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class AuthorListCreateView(generics.ListCreateAPIView):

    queryset = Author.objects.all().order_by('-id')
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilterSet
    pagination_class = AuthorPagination

    
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


