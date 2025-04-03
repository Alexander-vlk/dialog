from django.urls import path

from cabinet.templateviews import index, cabinet


urlpatterns = [
    path('', index, name='index'),
    path('cabinet/<int:cabinet_id>', cabinet, name='cabinet'),
]