from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth_service/', include('auth_service.urls')),
    path('api/cabinet/', include('cabinet.urls')),
]
