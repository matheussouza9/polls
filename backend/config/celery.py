import os
import logging

from celery import Celery
from django.conf import settings

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# Start celery app

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_default_queue = "default"

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
