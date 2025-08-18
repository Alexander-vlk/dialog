from django.urls import path

from auth_service.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    HealthCheckAPIView,
    LogoutAPIView,
    UserRegistrationAPIView,
)

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('healthcheck/', HealthCheckAPIView.as_view(), name='healthcheck'),
]
