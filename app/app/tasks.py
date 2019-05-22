import os
from background_task import background

from app import settings


@background(queue='delete_file')
def delete_file_schedule(doc_name):
    """
    schedule delete file from server
    """
    os.remove(os.path.join(settings.MEDIA_ROOT, doc_name))