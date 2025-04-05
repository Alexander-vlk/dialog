from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth_service/', include('auth_service.urls')),
    path('api/cabinet/', include('cabinet.urls')),

    path('', include('cabinet.templateurls')),
    path('', include('auth_service.templateurls')),

    path('data_tracking/', include('data_tracking.templateurls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
