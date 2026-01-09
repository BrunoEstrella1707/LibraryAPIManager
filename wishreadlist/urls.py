from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WishReadListViewSet


router = DefaultRouter()
router.register(r'userbooks', WishReadListViewSet, basename='userbooks')


urlpatterns = [
    path('', include(router.urls)),
]

# http://localhost:8000/api/v1/userbooks/add_to_wishlist/
# http://localhost:8000/api/v1/userbooks/add_to_readlist/