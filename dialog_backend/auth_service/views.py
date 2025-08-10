from django.conf import settings
from jwt import InvalidTokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.response import Response
from rest_framework import status

from auth_service.models import AppUser
from constants import ONE_DAY, TWO_MONTHS


class CustomTokenObtainPairView(TokenObtainPairView):
    """APIView для установки токенов пользователю"""

    serializer_class = TokenObtainPairSerializer  # type: ignore

    permission_classes: list = []  # type: ignore
    authentication_classes: list = []  # type: ignore

    refresh_token_cookie_name = 'refresh_token'

    def post(self, request, *args, **kwargs):
        """POST-запрос"""
        if self.refresh_token_cookie_name in request.COOKIES:
            return Response({'detail': 'already_authenticated'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        access_token = serializer.validated_data.get('access')
        refresh_token = serializer.validated_data.get('refresh')

        response = Response({'access': access_token}, status=status.HTTP_200_OK)

        response.set_cookie(
            key=self.refresh_token_cookie_name,
            value=refresh_token,
            httponly=True,
            secure=not settings.DEBUG,
            samesite='Lax',
            expires=TWO_MONTHS if request.data.get('remember') else ONE_DAY,
        )

        return response


class CustomTokenRefreshView(TokenRefreshView):
    """APIView для обновления токенов"""

    serializer_class = TokenRefreshSerializer  # type: ignore

    permission_classes: list = []  # type: ignore
    authentication_classes: list = []  # type: ignore

    def post(self, request, *args, **kwargs):
        """POST-запрос"""
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(data={'refresh': refresh_token})
        serializer.is_valid(raise_exception=True)

        return Response({'access': serializer.validated_data.get('access')}, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    """APIView для выхода пользователя из профиля"""

    authentication_classes: list = [JWTAuthentication]
    permission_classes: list = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """POST-запрос"""
        refresh_token = request.COOKIES.get('refresh_token')
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except InvalidTokenError:
            return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        response = Response(status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie('refresh_token')
        return response


class HealthCheckAPIView(APIView):
    """APIView для проверки, что аутентификация работает, и пользователь есть в request.user"""

    authentication_classes: list = [JWTAuthentication]
    permission_classes: list = [IsAuthenticated]

    def get(self, request):
        """GET-запрос"""
        return Response(status=status.HTTP_200_OK)
