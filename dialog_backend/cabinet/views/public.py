from rest_framework import viewsets
from cabinet.models import Allergy
from cabinet.serializers import AllergySerializer


class AllergyViewSet(viewsets.ModelViewSet):
    """ViewSet для Allergy"""

    permission_classes: list = []
    authentication_classes: list = []

    serializer_class = AllergySerializer
    queryset = Allergy.objects.all()
