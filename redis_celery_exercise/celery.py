from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<redis_celery_exercise>.settings')

app = Celery('<redis_celery_exercise>')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'add-every-2-seconds': {  #name of the scheduler
        'task': 'add_2_numbers',  # task name which we have created in tasks.py
        'schedule': 2.0,   # set the period of running
        'args': (16, 16)  # set the args
    },
    'print-name-every-5-seconds': {  #name of the scheduler
        'task': 'print_msg_with_name',  # task name which we have created in tasks.py
        'schedule': 5.0,  # set the period of running
         'args': ("DjangoPY", )  # set the args
    },
}