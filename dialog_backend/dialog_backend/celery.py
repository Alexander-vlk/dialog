import os
from celery import Celery

from dialog_backend.settings import CELERY_BROKER_URL


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dialog_backend.settings")

app = Celery(
    "dialog_backend", broker=CELERY_BROKER_URL, include=["dialog_backend.tasks"]
)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
