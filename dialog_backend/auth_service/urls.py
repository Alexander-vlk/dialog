from django.urls import path

from auth_service.views import RegistrationAPIView, LoginAPIView, LogoutAPIView


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
]
