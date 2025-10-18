from django.contrib import admin
from django.urls import path
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-view'),
]