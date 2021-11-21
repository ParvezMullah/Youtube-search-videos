from django.urls import path, include
from rest_framework.routers import DefaultRouter

from youtube_search_videos.search_videos.views import (
    YoutubeVideoDetailViewSet, YoutubeVideoDetailSearchViewSet)

router = DefaultRouter()
router.register(r'search', YoutubeVideoDetailSearchViewSet)
router.register(r'', YoutubeVideoDetailViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
