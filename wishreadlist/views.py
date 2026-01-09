from datetime import datetime
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import WishReadList
from .serializers import WishListSerializer, ReadListSerializer


class WishReadListViewSet(viewsets.GenericViewSet):

    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'wishlist':
            return WishListSerializer
        elif self.action == 'readlist':
            return ReadListSerializer
        return None
    

    @action(detail=False, methods=["post"])
    def add_to_wishlist(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        WishReadList.objects.create(
            user=request.user,
            book=serializer.validated_data["book"],
            list_type=WishReadList.WISH,
            date=datetime.now(),
        )

        return Response(
            {"detail": "Book added to the wishlist."},
            status=status.HTTP_201_CREATED
        )
    

    @action(detail=False, methods=["post"])
    def add_to_readlist(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        read_date = serializer.validated_data.get("date", datetime.now())

        WishReadList.objects.create(
            user=request.user,
            book=serializer.validated_data["book"],
            list_type=WishReadList.READ,
            date=read_date
        )

        return Response(
            {"detail": "Book marked as read."},
            status=status.HTTP_201_CREATED
        )
    