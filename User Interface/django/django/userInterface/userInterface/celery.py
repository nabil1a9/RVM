import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")

app = Celery("your_project")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()