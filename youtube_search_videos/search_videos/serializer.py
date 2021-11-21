from youtube_search_videos.search_videos.models import (
    YoutubeVideoDetail)
from rest_framework import serializers


class YoutubeVideoDetailSerializer(serializers.ModelSerializer):
    video_url = serializers.SerializerMethodField("get_video_url")

    def get_video_url(self, obj):
        return f'https://www.youtube.com/watch?v={obj.video_id}'

    class Meta:
        model = YoutubeVideoDetail
        exclude = ('id', 'is_active')
