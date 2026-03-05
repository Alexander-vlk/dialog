from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth_service.permissions import HasNoRefreshToken, HasRefreshToken
from auth_service.serializers import (
    AccessTokenResponseSerializer,
)

from auth_service.services import get_authenticated_response
from common_utils.constants import APISchemaTags


@extend_schema_view(
    post=extend_schema(
        tags=[APISchemaTags.AUTH_SERVICE],
        summary='Обновить access токен с использованием refresh токена',
        operation_id='Обновить access токен с использованием refresh токена',
        request={},
        responses={
            status.HTTP_200_OK: AccessTokenResponseSerializer,
        },
    ),
)
class CustomTokenRefreshView(TokenRefreshView):
    """Обновить access токен с использованием refresh токена"""

    permission_classes: list = [HasRefreshToken]
    authentication_classes: list = []

    serializer_class = TokenRefreshSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        """POST-запрос"""
        refresh_token = request.COOKIES.get('refresh_token')
        request_serializer = self.serializer_class(
            data={
                'refresh': refresh_token,
            },
        )
        request_serializer.is_valid(raise_exception=True)

        response_serializer = AccessTokenResponseSerializer(
            {
                'access_token': request_serializer.validated_data['access'],
            },
        )
        return Response(response_serializer.data, status=status.HTTP_200_OK)


@extend_schema_view(
    get=extend_schema(
        tags=[APISchemaTags.AUTH_SERVICE],
        summary='Проверка доступности сервиса',
        operation_id='Проверка доступности сервиса',
        responses={
            status.HTTP_202_ACCEPTED: {},
        },
    ),
)
class HealthCheckAPIView(APIView):
    """Проверка доступности сервиса"""

    authentication_classes: list = []
    permission_classes: list = []

    @staticmethod
    def get(request):
        """GET-запрос"""
        return Response(status=status.HTTP_202_ACCEPTED)


@extend_schema_view(
    get=extend_schema(
        tags=[APISchemaTags.AUTH_SERVICE],
        summary='Проверка доступности сервиса',
        operation_id='Проверка доступности сервиса',
        responses={
            status.HTTP_200_OK: {},
        },
    ),
)
class HealthCheck(APIView):
    """Проверка доступности сервиса"""

    authentication_classes: list = []
    permission_classes: list = []

    @staticmethod
    def get(request):
        """GET-запрос"""
        return Response(status=status.HTTP_202_ACCEPTED)


# @extend_schema_view(
#     post=extend_schema(
#         tags=[APISchemaTags.AUTH_SERVICE],
#         summary='Регистрация',
#         operation_id='Регистрация',
#         request=RegisterEmployeeRequestSerializer,
#         responses={
#             **DefaultAPIResponses.RESPONSES,
#             status.HTTP_200_OK: AccessTokenResponseSerializer,
#         },
#     ),
# )
# class RegisterEmployee(APIView):
#     """Регистрация работника"""
#
#     permission_classes: list = [HasNoRefreshToken]
#     authentication_classes: list = []
#
#     def post(self, request, *args, **kwargs):
#         """POST-запрос"""
#
#
#         token_serializer = TokenObtainPairSerializer(
#             data={
#                 'username': request_serializer.validated_data['username'],
#                 'password': request_serializer.validated_data['password'],
#             },
#         )
#         token_serializer.is_valid(raise_exception=True)
#
#         response = get_authenticated_response(
#             request,
#             token_serializer.validated_data['access'],
#             token_serializer.validated_data['refresh'],
#         )
#         return response


@extend_schema_view(
    post=extend_schema(
        tags=[APISchemaTags.AUTH_SERVICE],
        summary='Получить пару access и refresh токенов',
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
