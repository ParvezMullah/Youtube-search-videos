# -*- coding: utf-8 -*-

import os
from datetime import datetime, timedelta
import time
import googleapiclient.discovery
from youtube_search_videos.search_videos.models import (
    YoutubeVideoDetail)


class FetchYoutubeVideoList:
    def __init__(self, developer_key, search_query, fetch_per_request=40, max_records_to_process=300):
        self.developer_key = developer_key
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"
        self.search_query = search_query
        self.processed_counts = 0
        self.fetch_per_request = fetch_per_request
        self.max_records_to_process = max_records_to_process
        self.videos_list = []

        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=self.developer_key.key)

    def fetch_youtube_video_details(self):
        self.fetch_youtube_video_details_helper()

    def fetch_youtube_video_details_helper(self, token=None):
        request = None
        if token:
            request = self.youtube.search().list(
                part="snippet",
                pageToken=token,
                maxResults=self.fetch_per_request
            )
        else:
            past_look_up_time = (datetime.now() - timedelta(minutes=2)).strftime(
                '%Y-%m-%dT%H:%M:%SZ')
            request = self.youtube.search().list(
                part="snippet",
                maxResults=self.fetch_per_request,
                order="date",
                publishedAfter=past_look_up_time,
                q=self.search_query,
                type="video"
            )
        try:
            try:
                response = request.execute()
            except Exception as ex:
                self.developer_key.deactivate_key()
                print(ex)
            items = response.get("items")
            save_videos_obj = SaveVideoDetails(items)
            save_videos_obj.save_all_items()
            self.processed_counts += len(items)
            nextPageToken = response.get('nextPageToken')
            if self.processed_counts >= self.max_records_to_process or not nextPageToken:
                return
            time.sleep(1)
            self.fetch_youtube_video_details_helper(nextPageToken)
        except Exception as e:
            print(e)


class SaveVideoDetails:
    def __init__(self, items):
        self.items = items

    def save_all_items(self):
        youtube_video_details = []
        for item in self.items:
            youtube_vidoe_detail_obj = YoutubeObjToDbObject(item).get_db_obj()
            youtube_video_details.append(youtube_vidoe_detail_obj)
        YoutubeVideoDetail.objects.bulk_create(youtube_video_details)


class YoutubeObjToDbObject:
    def __init__(self, item):
        self.item = item

    def get_db_obj(self):
        video_id = self.item["id"].get("videoId")
        snippet = self.item.get("snippet", {})
        published_at = snippet.get("publishedAt")
        channel_id = snippet.get("channelId")
        title = snippet.get("title")
        description = snippet.get("description")
        thumbnails = snippet.get("thumbnails")
        channel_title = snippet.get("channelTitle")
        return YoutubeVideoDetail(
            video_id=video_id, title=title,
            description=description, thumbnails=thumbnails,
            channel_title=channel_title, channel_id=channel_id,
            published_at=published_at
        )
