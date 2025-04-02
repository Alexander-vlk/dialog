from django.urls import path

from cabinet.templateviews import index


urlpatterns = [
    path('', index, name='index'),
]