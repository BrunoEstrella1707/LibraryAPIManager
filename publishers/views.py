from rest_framework import generics
from publishers.models import Publisher
from publishers.serializers import PublisherSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class PublisherListCreateView(generics.ListCreateAPIView):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]


class PublisherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

