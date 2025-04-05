from django.contrib import admin

from cabinet.models import Advantage, Allergy, Disease, UserProfile, Rate


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    """Админ для модели Advantage"""

    list_display = ['order_num', 'title', 'description']
    list_display_links = ['title']



@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    """Админ для модели Allergy"""

    list_display = ['name', 'updated_at', 'created_at']


@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    """Админ для модели Disease"""

    list_display = ['name', 'updated_at', 'created_at']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Админ для модели UserProfile"""
    
    list_display = ['user__username', 'gender', 'diabetes_type', 'updated_at']
    raw_id_fields = ['user']


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_info', 'text', 'is_visible']
    list_display_links = ['id', 'user_info']

    @admin.display(description='Пользователь')
    def user_info(self, obj):
        return obj.user_info
