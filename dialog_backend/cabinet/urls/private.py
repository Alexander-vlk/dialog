from django.urls import path
from rest_framework.routers import SimpleRouter

from cabinet.views import AppUserAPIView

router = SimpleRouter()


urlpatterns = [
    path('api/users/', AppUserAPIView.as_view(), name='user_me'),
]

urlpatterns.extend(router.urls)
