from django.db.models import Q
from django.http import HttpResponseBadRequest
from youtube_search_videos.search_videos.models import (
    YoutubeVideoDetail)
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from youtube_search_videos.search_videos.serializer import YoutubeVideoDetailSerializer


class YoutubeVideoDetailViewSet(ModelViewSet):
    serializer_class = YoutubeVideoDetailSerializer
    queryset = YoutubeVideoDetail.objects.filter(
        is_active=True).order_by('-published_at')


class YoutubeVideoDetailSearchViewSet(GenericViewSet):
    serializer_class = YoutubeVideoDetailSerializer
    queryset = YoutubeVideoDetail.objects.filter(
        is_active=True).order_by('-published_at')

    def list(self, request):
        query = self.request.GET.get('q')
        if not query:
            return HttpResponseBadRequest("Please provide a search query.")
        self.queryset = self.queryset.filter(
            Q(title__icontains=query) or Q(description__icontains=query))
        page = self.paginate_queryset(self.queryset)
        serializer = YoutubeVideoDetailSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
