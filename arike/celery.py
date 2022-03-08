import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','arike.settings')

app = Celery('arike')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps
app.autodiscover_tasks()

# @app.task
# def myname(name):
#     print("My name is: " + name)

# app.conf.beat_schedule = {
#     'run every 3 sec': {
#         'task': 'tasks.myname',
#         'schedule': 3.0,
#         'args': ("ravinder")
#     },
# }
app.conf.timezone = 'UTC'