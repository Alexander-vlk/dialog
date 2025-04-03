from django.urls import path

from cabinet.templateviews import index, cabinet


urlpatterns = [
    path('', index, name='index'),
    path('cabinet/', cabinet, name='cabinet'),
]