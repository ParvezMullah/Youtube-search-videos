from django.contrib import admin
from youtube_search_videos.search_videos.models import (
    YoutubeVideoDetail, DeveloperKey)


class YoutubeVideoDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'published_at']


admin.site.register(YoutubeVideoDetail, YoutubeVideoDetailAdmin)


class DeveloperKeyAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'is_active', 'created_at', 'updated_at']


admin.site.register(DeveloperKey, DeveloperKeyAdmin)
