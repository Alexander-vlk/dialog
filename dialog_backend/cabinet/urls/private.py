from django.urls import path
from rest_framework.routers import SimpleRouter

from cabinet.views.private import UserViewSet, UserDataAPIView


router = SimpleRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('users/me/', UserDataAPIView.as_view(), name='current_user_data'),
]

urlpatterns.extend(router.urls)
