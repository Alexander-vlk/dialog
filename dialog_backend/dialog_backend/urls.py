from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    path('api/auth_service/', include('auth_service.urls')),
    path('api/data-tracking/', include('data_tracking.urls')),
    path('api/sitesettings/', include('sitesettings.urls')),
    path('api/cabinet/public/', include('cabinet.urls.public')),
    path('api/cabinet/private/', include('cabinet.urls.private')),
    path('', include('cabinet.templateurls')),
    path('', include('auth_service.templateurls')),
    path('data_tracking/', include('data_tracking.templateurls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
