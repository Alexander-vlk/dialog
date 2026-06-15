from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from auth_service.models import AppUser
from auth_service.permissions import HasRefreshToken
from auth_service.serializers import RegisterUserSerializer
from cabinet.selectors import get_streak_data_from_redis
from cabinet.serializers import UserStreakResponseSerializer
from common_utils.constants import APISchemaTags


@extend_schema_view(
    retrieve=extend_schema(
        'Получить данные пользователя',
        tags=[APISchemaTags.USERS],
        request=RegisterUserSerializer,
        responses={
            status.HTTP_200_OK: RegisterUserSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить данные пользователя',
        tags=[APISchemaTags.USERS],
        request=RegisterUserSerializer,
        responses={
            status.HTTP_200_OK: RegisterUserSerializer,
        },
    ),
    update=extend_schema(
        'Обновить данные пользователя',
        tags=[APISchemaTags.USERS],
        request=RegisterUserSerializer,
        responses={
            status.HTTP_200_OK: RegisterUserSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить пользователя',
        tags=[APISchemaTags.USERS],
        request=RegisterUserSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
        },
    ),
    streak=extend_schema(
        'Получить данные об ударном режиме пользвоателя',
        tags=[APISchemaTags.USERS],
        responses={
            status.HTTP_200_OK: UserStreakResponseSerializer,
        },
    ),
)
class AppUserViewSet(
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    """ViewSet для работы с пользователями"""

    queryset = AppUser.objects.all()
    serializer_class = RegisterUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasRefreshToken]

    def get_object(self):
        return AppUser.objects.get(pk=self.request.user.pk)

    def has_permissions(self):
        """Проверка наличия доступов по разным actions"""
        permission_classes =  [IsAuthenticated(), HasRefreshToken()]
        if self.request.method != 'retrieve':
            permission_classes.append(IsAdminUser())

        return permission_classes

    @action(methods=['get'], detail=False, url_path='streak', url_name='streak')
    def streak(self, request):
        """Получить статус ударного режима для пользователя"""
        user_streak_data = get_streak_data_from_redis(request.user)
        response_serializer = UserStreakResponseSerializer(user_streak_data)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
