from __future__ import absolute_import, unicode_literals
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PriceTracker.settings')
app = Celery('PriceTracker')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace = 'CELERY')

#Celery Beat Settings
app.conf.beat_schedule = {
    'FetchPrice': {
        'task': 'Tracker.tasks.FetchPrice',
        'schedule': crontab(minute='30'),
    }
}

app.autodiscover_tasks()
@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')