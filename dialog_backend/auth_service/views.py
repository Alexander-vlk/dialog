from django.conf import settings
from django.shortcuts import reverse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework.response import Response
from rest_framework import status

from constants import ONE_DAY, TWO_MONTHS


class CustomTokenObtainPairView(TokenObtainPairView):
    """APIView для установки токенов пользователю"""

    serializer_class = TokenObtainPairSerializer

    permission_classes: list = []
    authentication_classes: list = []

    def post(self, request, *args, **kwargs):
        """POST-запрос"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        access_token = serializer.validated_data.get('access')
        refresh_token = serializer.validated_data.get('refresh')

        response = Response({'access': access_token}, status=status.HTTP_200_OK)

        response.set_cookie(
            key='refresh_token',
            value=refresh_token,
            httponly=True,
            secure=not settings.DEBUG,
            samesite='Lax',
            path=reverse('token_refresh'),
            expires=TWO_MONTHS if request.data.get('remember') else ONE_DAY,
        )

        return response


class CustomTokenRefreshView(TokenRefreshView):
    """APIView для обновления токенов"""

    serializer_class = TokenRefreshSerializer

    permission_classes: list = []
    authentication_classes: list = []

    def post(self, request, *args, **kwargs):
        """POST-запрос"""
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(data={'refresh': refresh_token})
        serializer.is_valid(raise_exception=True)

        return Response({'access': serializer.validated_data.get('access')}, status=status.HTTP_200_OK)
