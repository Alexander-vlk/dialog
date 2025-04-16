from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title='DiaLog API reference',
        default_version='v1',
        description='API for DiaLog application',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/auth_service/', include('auth_service.urls')),
    path('api/data-tracking/', include('data_tracking.urls')),

    path('', include('cabinet.templateurls')),
    path('', include('auth_service.templateurls')),

    path('data_tracking/', include('data_tracking.templateurls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
