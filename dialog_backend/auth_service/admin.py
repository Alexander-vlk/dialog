from django.contrib import admin


from auth_service.models import AppUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    """Админ для модели AppUser"""

    list_display = ('username', 'email', 'first_name', 'last_name')
