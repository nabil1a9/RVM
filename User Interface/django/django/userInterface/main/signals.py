from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.http import  HttpResponseRedirect
import os
import time

def has_file_been_modified(filepath, recorded_timestamp):
    current_timestamp = os.stat(filepath).st_mtime
    return current_timestamp != recorded_timestamp


@receiver(post_save)
def check_file_modification(sender, instance, **kwargs):
    file_path = 'C:/Users/Public/yolov71/data.xlsx'
    recorded_timestamp = getattr(settings, 'RECORDED_TIMESTAMP', None)

    if has_file_been_modified(file_path, recorded_timestamp):
        # File has been modified, execute your desired method here


        # Update the recorded timestamp
        setattr(settings, 'RECORDED_TIMESTAMP', os.stat(file_path).st_mtime)
        return HttpResponseRedirect("/ajouter")