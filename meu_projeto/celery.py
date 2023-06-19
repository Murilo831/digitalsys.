
from celery import Celery
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meu_projeto.settings')

app = Celery('meu_projeto')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


