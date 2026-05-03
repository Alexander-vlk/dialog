from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from auth_service.permissions import HasRefreshToken, HasNoRefreshToken
from auth_service.serializers import (
    ChangePasswordRequestSerializer,
)
from common_utils.constants import APISchemaTags


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

    serializer_class = None

    def post(self, request, *args, **kwargs):
        """POST-запрос"""
        refresh_token = request.COOKIES.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()
        response = Response(status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie('refresh_token')
        return response
