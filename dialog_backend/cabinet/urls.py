from django.urls import path, include
from rest_framework.routers import SimpleRouter

from cabinet.views import DiseaseViewSet, AppUserViewSet, UpdateAppUser

cabinet_router = SimpleRouter()
cabinet_router.register('disease', DiseaseViewSet)

cabinet_router.register('update_users', UpdateAppUser)

cabinet_router.register('users', AppUserViewSet, basename='user')

urlpatterns = [
    path('', include(cabinet_router.urls)),
]
