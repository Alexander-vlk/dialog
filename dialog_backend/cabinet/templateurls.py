from django.urls import path

from cabinet.templateviews import index, cabinet, edit_profile


urlpatterns = [
    path('', index, name='index'),
    path('cabinet/', cabinet, name='cabinet'),

    path('cabinet/update', edit_profile, name='cabinet_update'),
]