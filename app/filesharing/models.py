from datetime import datetime

from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # delete_at = models.DateTimeField(default=datetime.now, blank=True)
    file_live_time = models.IntegerField(blank=True, default=0)