from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_service.serializers import UserSerializer
from cabinet.constants import USER_SWAGGER_TAG
from cabinet.serializers import UserDataSerializer
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


@extend_schema(
    tags=[USER_SWAGGER_TAG],
    responses={
        status.HTTP_200_OK: UserDataSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class UserDataAPIView(APIView):
    """APIView получения данных о пользователе"""

    permission_classes = [IsAuthenticated]
    serializer_class = UserDataSerializer

    def get(self, request):
        """GET-запрос"""
        if not hasattr(request.user, 'userprofile'):
            return Response(
                {
                    'error': 'У пользователя отсутствует UserProfile',
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.serializer_class(request.user.userprofile)
        return Response(serializer.data, status=status.HTTP_200_OK)
