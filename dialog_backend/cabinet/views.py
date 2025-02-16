from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from auth_service.serializers import UserSerializer
from cabinet.models import Allergy
from cabinet.serializers import AllergySerializer, DiseaseSerializer


class UserViewSet(viewsets.ModelViewSet):
    """GenericAPIView для модели User"""

    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAdminUser,)


class AllergyViewSet(viewsets.ModelViewSet):
    """ViewSet для Allergy"""

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = AllergySerializer
    queryset = Allergy.objects.all()
