from django.contrib import admin

from cabinet.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Админ для модели UserProfile"""
    
    list_display = ['user__username', 'gender', 'diabetes_type', 'updated_at']
    raw_id_fields = ['user']
    