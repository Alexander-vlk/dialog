from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser

from auth_service.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """GenericAPIView для модели User"""

    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication | SessionAuthentication]
    permission_classes = [IsAdminUser]
