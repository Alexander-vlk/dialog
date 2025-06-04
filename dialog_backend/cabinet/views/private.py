from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser

from auth_service.serializers import UserSerializer
from cabinet.constants import USER_SWAGGER_TAG
from constants import SWAGGER_ERROR_MESSAGES


@extend_schema(
    tags=[USER_SWAGGER_TAG],
    responses={
        status.HTTP_200_OK: UserSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class UserViewSet(viewsets.ModelViewSet):
    """GenericAPIView для модели User"""

    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
