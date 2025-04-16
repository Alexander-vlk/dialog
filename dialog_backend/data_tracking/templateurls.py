from django.urls import path

from data_tracking.templateviews import (
    daily_log,
    DailyLogListView,
)

urlpatterns = [

    path('daily_log', daily_log, name='daily_log'),
    path('daily_log_list', DailyLogListView.as_view(), name='daily_log_list'),
]
