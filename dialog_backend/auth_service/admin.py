from django.contrib import admin


from auth_service.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    """Админ для модели AppUser"""

    list_display = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('password', 'last_login', 'date_joined')

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
                    'birth_date',
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
                    'email',
                    'phone_number',
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
