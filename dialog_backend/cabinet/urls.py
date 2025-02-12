from django.urls import path
from cabinet.views import UserListAPIView

urlpatterns = [
    path('/users/', UserListAPIView.as_view(), name='users'),
]