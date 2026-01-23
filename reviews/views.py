from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from reviews.models import Review
from reviews.serializers import ReviewSerializer, ReviewListDetailSerializer

# Create your views here.
class ReviewListCreateView(generics.ListCreateAPIView):

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
