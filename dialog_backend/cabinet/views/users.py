from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from auth_service.models import AppUser
from auth_service.permissions import HasRefreshToken
from auth_service.serializers import AppUserSerializer
from common_utils.constants import APISchemaTags


@extend_schema_view(
    retrieve=extend_schema(
        'Получить данные пользователя',
        tags=[APISchemaTags.USERS],
        request=AppUserSerializer,
        responses={
            status.HTTP_200_OK: AppUserSerializer,
        },
    ),
    partial_update=extend_schema(
        'Частично обновить данные пользователя',
        tags=[APISchemaTags.USERS],
        request=AppUserSerializer,
        responses={
            status.HTTP_200_OK: AppUserSerializer,
        },
    ),
    update=extend_schema(
        'Обновить данные пользователя',
        tags=[APISchemaTags.USERS],
        request=AppUserSerializer,
        responses={
            status.HTTP_200_OK: AppUserSerializer,
        },
    ),
    destroy=extend_schema(
        'Удалить пользователя',
        tags=[APISchemaTags.USERS],
        request=AppUserSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: {},
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
    serializer_class = AppUserSerializer
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
