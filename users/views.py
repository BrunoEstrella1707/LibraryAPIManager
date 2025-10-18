from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.db.utils import IntegrityError
from rest_framework import status, viewsets, serializers
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import CustomUser
from users.serializers import UserCreateSerializer, UserUpdateListDetailSerializer


class UserCRUDView(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateListDetailSerializer
    permission_classes = [AllowAny]


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateSerializer
        return UserUpdateListDetailSerializer
    

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
        

    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save()

            headers = self.get_success_headers(data=serializer.data)

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers
            )
        
        except IntegrityError:
            raise serializers.ValidationError({"detail": "Error creating the user. Check the fields!"})
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserUpdateListDetailSerializer(user)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
        
        


