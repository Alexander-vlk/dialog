from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from auth_service.serializers.response_serializers import AppUserResponseSerializer
from cabinet.constants import USER_SWAGGER_TAG
from constants import SWAGGER_ERROR_MESSAGES


@extend_schema(
    tags=[USER_SWAGGER_TAG],
    responses={
        status.HTTP_200_OK: AppUserResponseSerializer,
        **SWAGGER_ERROR_MESSAGES,
    }
)
class AppUserAPIView(APIView):
    """APIViwe для данных о пользователе"""

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AppUserResponseSerializer

    def convert_user_data_to_dict(self):
        """Конвертировать request.user в словарь"""
        return {
            'id': self.request.user.id,
            'username': self.request.user.username,
            'email': self.request.user.email,
            'last_name': self.request.user.last_name,
            'first_name': self.request.user.first_name,
            'patronymic_name': self.request.user.patronymic_name,
            'image_url': self.request.user.image.url,
            'gender': self.request.user.gender,
            'birth_date': self.request.user.birth_date,
            'diabetes_type': self.request.user.diabetes_type,
            'diagnosis_date': self.request.user.diagnosis_date,
            'treatment_type': self.request.user.treatment_type,
            'phone_number': self.request.user.phone_number,
        }

    def get(self, request):
        """GET-запрос"""
        serializer = self.serializer_class(data=self.convert_user_data_to_dict())
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
