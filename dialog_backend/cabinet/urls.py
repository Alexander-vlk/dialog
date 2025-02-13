from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cabinet.views import UserListAPIView, AllergyViewSet


cabinet_router = DefaultRouter()
cabinet_router.register(r'users', UserListAPIView, basename='users')
cabinet_router.register(r'allergies', AllergyViewSet, basename='allergies')

urlpatterns = [
    path('', include(cabinet_router.urls)),
]
