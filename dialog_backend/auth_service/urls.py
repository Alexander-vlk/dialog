from django.urls import path

from auth_service.views import CustomTokenObtainPairView, CustomTokenRefreshView


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
