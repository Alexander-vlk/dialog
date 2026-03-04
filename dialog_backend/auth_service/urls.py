from django.urls import path

from auth_service.views import (
    HealthCheckAPIView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    ChangePassword,
    LogoutAPIView,
)

urlpatterns = [
    path('healthcheck/', HealthCheckAPIView.as_view(), name='health_check'),
    path('token/obtain/', CustomTokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('password/change/', ChangePassword.as_view(), name='password_change'),
    path('logout/', LogoutAPIView.as_view(), name='log_out'),
]
