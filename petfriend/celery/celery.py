from __future__ import absolute_import, unicode_literals

from decouple import config
from celery import Celery

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", config("DJANGO_SETTINGS_MODULE"))


app = Celery('settings', broker="amqp://guest@rabbitmq//")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')