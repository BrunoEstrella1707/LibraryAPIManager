from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from reviews.models import Review
from reviews.serializers import ReviewSerializer, ReviewListDetailSerializer


class ReviewPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class ReviewListCreateView(generics.ListCreateAPIView):

    queryset = Review.objects.all()
    pagination_class = ReviewPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListDetailSerializer
        else:
            return ReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
           

class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReviewListDetailSerializer
        else:
            return ReviewSerializer
