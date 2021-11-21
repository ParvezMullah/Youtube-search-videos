from django.db.models import Q
from django.http import HttpResponseBadRequest
from youtube_search_videos.search_videos.models import (
    YoutubeVideoDetail)
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from youtube_search_videos.search_videos.serializer import YoutubeVideoDetailSerializer
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank


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
        vector = SearchVector('title', 'description')
        search_query = SearchQuery(query)
        self.queryset = self.queryset.annotate(rank=SearchRank(
            vector, search_query)).filter(rank__gte=0.001)
        page = self.paginate_queryset(self.queryset)
        serializer = YoutubeVideoDetailSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
