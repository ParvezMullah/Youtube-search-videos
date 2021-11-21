from django.core.management.base import BaseCommand
from youtube_search_videos.search_videos.utils.fetch_youtube_video_details import FetchYoutubeVideoList
from youtube_search_videos.search_videos.models import (
    DeveloperKey)
from datetime import datetime


class Command(BaseCommand):
    help = 'Fetch the vidoes from youtube.'

    def handle(self, *args, **options):
        print(f"fetching at {datetime.now()}")
        self.developer_key = DeveloperKey.get_activate_key()
        search_query = "cricket|politics|movie|india|share|official|football|news|music|funny|vlog|food|mobile"
        fetch_youtube_videos_obj = FetchYoutubeVideoList(
            self.developer_key, search_query)
        fetch_youtube_videos_obj.fetch_youtube_video_details()
