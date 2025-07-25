from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from cabinet.models import Advantage, Allergy, Disease, Rate, UserProfile


class AllergySerializer(serializers.ModelSerializer):
    """Сериализатор для модели Allergy"""

    class Meta:
        model = Allergy
        fields = ('name',)

    def create(self, validated_data):
        allergy = super().create(validated_data)
        user = self.context['request'].user
        if user.is_authenticated:
            allergy.users.add(user)
        allergy.save()
        return allergy


class DiseaseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Disease"""

    class Meta:
        model = Disease
        fields = ('name',)

    def create(self, validated_data):
        disease = super().create(validated_data)
        user = self.context['request'].user
        if user.is_authenticated:
            disease.users.add(user)
        disease.save()
        return disease


class UserProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для модели UserProfile"""

    class Meta:
        model = UserProfile
        fields = (
            'patronymic_name',
            'gender',
            'birth_date',
            'diabetes_type',
            'diabetes_type',
            'diagnosis_date',
            'treatment_type',
            'phone_number',
        )

    def create(self, validated_data):
        user_profile = super().create(validated_data)
        user = self.context['request'].user
        if user.is_authenticated:
            user_profile.user = user
        user_profile.save()
        return user_profile


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'title': 'Преимущество 1',
                    'description': 'Описание преимущества',
                    'image_url': 'https://dialog.com/media/advantages/advantage1.png',
                    'order_num': 1,
                },
            ],
        ),
    ],
)
class AdvantageSerializer(serializers.ModelSerializer):
    """Сериализатор модели Advantage"""

    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Advantage
        fields = ('title', 'description', 'image_url', 'order_num')

    def get_image_url(self, obj):
        """Получить url изображения"""
        return obj.image.url if obj.image else ''


@extend_schema_serializer(
    many=True,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value=[
                {
                    'user_info': 'Тестина Тестова',
                    'text': 'Текст отзыва',
                },
                {
                    'user_info': 'Тестина',
                    'text': 'Текст отзыва',
                },
            ],
        ),
        OpenApiExample(
            'Анонимный отзыв',
            description='Пример ответа от сервера, если отзыв оставлен анонимным пользователем',
            value=[
                {
                    'user_info': 'Аноним',
                    'text': 'Текст отзыва',
                },
            ],
        ),
    ],
)
class RateSerializer(serializers.ModelSerializer):
    """Сериализатор модели Rate"""

    class Meta:
        model = Rate
        fields = ('user_info', 'text')


@extend_schema_serializer(
    many=False,
    examples=[
        OpenApiExample(
            'Пример ответа от сервера',
            description='Базовый ответ',
            value={
                'id': 1,
                'username': 'testov',
                'email': 'testov@testov.com',
                'first_name': 'Тест',
                'last_name': 'Тестов',
                'patronymic_name': 'Тестович',
                'is_superuser': True,
                'date_joined': '2025-10-10 13:04:00',
                'image_url': '/media/profile_images/user_image.png',
                'gender': 'Мужской',
                'birth_date': '2025-10-10 13:04:00',
                'diabetes_type': '1-го типа',
                'diagnosis_date': '2025-10-10 13:04:00',
                'treatment_type': 'Инсулинотерапия',
                'phone_number': '79990001122',
            },
        ),
    ],
)
class UserDataSerializer(serializers.ModelSerializer):
    """Сериализатор всех пользовательских данных (базовая модель пользователя User + UserProfile"""

    username = serializers.CharField(read_only=True)
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'patronymic_name',
            'is_superuser',
            'date_joined',
            'image_url',
            'gender',
            'birth_date',
            'diabetes_type',
            'diagnosis_date',
            'treatment_type',
            'phone_number',
        )

    def to_representation(self, instance):
        """Расширение метода преобразования объекта модели"""
        representation = super().to_representation(instance)

        if instance.user:
            representation['username'] = instance.user.username
            representation['first_name'] = instance.user.first_name
            representation['last_name'] = instance.user.last_name
            representation['email'] = instance.user.email
            representation['is_superuser'] = instance.user.is_superuser
            representation['date_joined'] = instance.user.date_joined

        return representation

    def get_image_url(self, obj):
        """Получить URL аватарки пользователя"""
        return obj.image.url if obj.image else ''
