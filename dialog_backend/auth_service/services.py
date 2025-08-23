from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

from auth_service.constants import REFRESH_TOKEN_COOKIE_NAME
from auth_service.serializers import AccessTokenResponseSerializer
from constants import TWO_MONTHS, ONE_DAY


def authenticate_user(request, access_token, refresh_token) -> Response:
    """Аутентифицировать пользователя"""
    response_serializer = AccessTokenResponseSerializer(instance={'access': access_token})
    response = Response(response_serializer.data, status.HTTP_201_CREATED)

    response.set_cookie(
        key=REFRESH_TOKEN_COOKIE_NAME,
        value=refresh_token,
        httponly=True,
        secure=not settings.DEBUG,
        samesite='Lax',
        expires=TWO_MONTHS if request.data.get('remember') else ONE_DAY,
    )

    return response
