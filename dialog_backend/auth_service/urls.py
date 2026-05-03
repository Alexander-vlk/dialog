from django.urls import path

from auth_service.views import (
    HealthCheckAPIView,
    AuthorizationAPIView,
    CustomTokenRefreshView,
    ChangePassword,
    LogoutAPIView,
    NewAppUserRegisterAPIView,
)

urlpatterns = [
    path('healthcheck/', HealthCheckAPIView.as_view(), name='health_check'),
    path('token/obtain/', AuthorizationAPIView.as_view(), name='token_obtain'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('password/change/', ChangePassword.as_view(), name='password_change'),
    path('users/register', NewAppUserRegisterAPIView.as_view(), name='new_app_user_register'),
    path('logout/', LogoutAPIView.as_view(), name='log_out'),
]
