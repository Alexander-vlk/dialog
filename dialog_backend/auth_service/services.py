from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

from auth_service.constants import REFRESH_TOKEN_COOKIE_NAME, ONE_DAY, TWO_MONTHS
from auth_service.serializers import AccessTokenResponseSerializer


def get_authenticated_response(request, access_token, refresh_token) -> Response:
    """Сгенерировать ответ при аутентификации"""
    serializer = AccessTokenResponseSerializer(
        {
            'access_token': access_token,
        },
    )

    response = Response(serializer.data, status=status.HTTP_200_OK)
    response.set_cookie(
        key=REFRESH_TOKEN_COOKIE_NAME,
        value=refresh_token,
        httponly=True,
        secure=not settings.DEBUG,
        samesite='Lax',
        max_age=TWO_MONTHS if request.data.get('remember') else ONE_DAY,
    )
    return response
