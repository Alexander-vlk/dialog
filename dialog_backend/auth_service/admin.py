from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from auth_service.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(UserAdmin):
    """Админ для модели AppUser"""

    model = AppUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name')
    raw_id_fields = ('town', 'diabetes_type', 'treatment_type')
    readonly_fields = (
        'last_login',
        'date_joined',
        'created_at',
        'updated_at',
    )
    list_filter = ('is_active', 'is_superuser', 'is_staff')
    fieldsets = [
        (
            'Сведения о пользователе',
            {
                'fields': [
                    'last_name',
                    'first_name',
                    'patronymic_name',
                    'gender',
                    'height',
                    'birth_date',
                    'phone_number',
                    'diabetes_type',
                    'treatment_type',
                    'diagnosis_date',
                    'image',
                ],
            },
        ),
        (
            'Система',
            {
                'fields': [
                    'username',
                    'password',
                    'email',
                    'is_superuser',
                    'is_staff',
                    'is_active',
                    'date_joined',
                    'last_login',
                    'user_permissions',
                    'groups',
                ],
            },
        ),
    ]
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
    )
