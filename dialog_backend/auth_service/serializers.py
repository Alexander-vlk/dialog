from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """Сериализатор для модели User"""
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'last_name', 'first_name')