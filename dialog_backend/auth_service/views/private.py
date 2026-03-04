from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from auth_service.permissions import HasRefreshToken, HasNoRefreshToken
from auth_service.serializers import (
    ChangePasswordRequestSerializer,
    AccessTokenResponseSerializer,
)
from auth_service.services import get_authenticated_response
from common_utils.constants import APISchemaTags


@extend_schema_view(
    post=extend_schema(
        tags=[APISchemaTags.AUTH_SERVICE],
        summary='Получить пару access и refresh токенов (авторизоваться)',
        operation_id='Получение пары токенов',
        responses={
            status.HTTP_200_OK: AccessTokenResponseSerializer,
        },
    ),
)
class CustomTokenObtainPairView(TokenObtainPairView):
    """Получить пару access и refresh токенов"""

    permission_classes: list = [HasNoRefreshToken]
    authentication_classes: list = []

    def post(self, request, *args, **kwargs):
        """POST-запрос"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        access_token = serializer.validated_data['access']
        refresh_token = serializer.validated_data['refresh']
        response = get_authenticated_response(request, access_token, refresh_token)
        return response


@extend_schema_view(
    post=extend_schema(
        tags=[APISchemaTags.AUTH_SERVICE],
        summary='Сменить пароль',
        operation_id='Сменить пароль',
        request=ChangePasswordRequestSerializer,
        responses={
            status.HTTP_200_OK: {},
        },
    ),
)
class ChangePassword(APIView):
    """Сменить пароль"""

    permission_classes: list = [IsAuthenticated]
    authentication_classes: list = [JWTAuthentication]

    def post(self, reqeust: Request, *args, **kwargs) -> Response:
        """POST-запрос"""
        request_serializer = ChangePasswordRequestSerializer(
            data=reqeust.data,
            context={
                'user': reqeust.user,
            },
        )
        request_serializer.is_valid(raise_exception=True)
        reqeust.user.set_password(request_serializer.validated_data['new_password'])
        return Response(status=status.HTTP_200_OK)


@extend_schema_view(
    post=extend_schema(
        tags=[APISchemaTags.AUTH_SERVICE],
        summary='Выйти из профиля',
        operation_id='Выйти из профиля',
        responses={
            status.HTTP_205_RESET_CONTENT: {},
        },
    ),
)
class LogoutAPIView(APIView):
    """Выйти из профиля"""

    permission_classes: list = [IsAuthenticated, HasRefreshToken]
    authentication_classes: list = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        """POST-запрос"""
        refresh_token = request.COOKIES.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        response = Response(status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie('refresh_token')
        return response
