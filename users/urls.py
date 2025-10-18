from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserCRUDView


router = DefaultRouter()
router.register(r'users', UserCRUDView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
# http://localhost:8000/api/v1/users/
# http://localhost:8000/api/v1/users/1/