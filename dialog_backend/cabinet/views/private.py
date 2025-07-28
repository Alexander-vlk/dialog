from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser

from auth_service.models import AppUser
from auth_service.serializers import UserResponseSerializer
from cabinet.constants import USER_SWAGGER_TAG
from constants import SWAGGER_ERROR_MESSAGES


@extend_schema(
    tags=[USER_SWAGGER_TAG],
    responses={
        status.HTTP_200_OK: UserResponseSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class UserViewSet(viewsets.ModelViewSet):
    """GenericAPIView для модели User"""

    model = AppUser
    queryset = AppUser.objects.all()
    serializer_class = UserResponseSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]
