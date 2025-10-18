from django.urls import path
from publishers.views import PublisherListCreateView, PublisherRetrieveUpdateDestroyView


urlpatterns = [
    path('publishers/', PublisherListCreateView.as_view(), name='publisher-list-create'),
    path('publishers/<int:pk>/', PublisherRetrieveUpdateDestroyView.as_view(), name='publisher-detail-view'),
]