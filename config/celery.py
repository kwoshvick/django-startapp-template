from __future__ import absolute_import, unicode_literals

import os
import environ

from django.conf import settings

from celery import Celery
# from decouple import config

env = environ.Env()

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", env("DJANGO_SETTINGS_MODULE", default="config.settings")
)
app = Celery("config")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
