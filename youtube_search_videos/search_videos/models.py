from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
# Create your models here.


class YoutubeVideoDetail(models.Model):
    video_id = models.CharField(max_length=12, blank=True, null=True)
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    channel_id = models.CharField(max_length=32)
    channel_title = models.CharField(max_length=64)
    thumbnails = models.JSONField()
    published_at = models.DateTimeField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        indexes = (GinIndex(fields=["title"]),
                   GinIndex(fields=["description"]))


class DeveloperKey(models.Model):
    key = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def deactivate_key(self):
        self.is_active = False
        self.save()

    @classmethod
    def get_activate_key(self):
        activate_keys = self.objects.filter(is_active=True)
        if activate_keys:
            return activate_keys[0]
        raise Exception('No active key.')
