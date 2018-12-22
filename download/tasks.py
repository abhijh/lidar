from celery.decorators import task
from celery import group
from celery.utils.log import get_task_logger
from .downloader import Downloader
from django.conf import settings

logger = get_task_logger(__name__)

downloader = Downloader(settings.BASE_DOWNLOAD_DIR)

@task(name="download_single_track")
def download_single_track_task(track_name, album_name, url):
    """downloads a single track from the url provided"""
    downloader.download_single_track(track_name, album_name, url, download_single_track_task)
