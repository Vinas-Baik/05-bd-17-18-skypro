# в файле utils.py
from googleapiclient.discovery import build
from typing import Any
import psycopg2

def get_youtube_data(api_key: str, channel_ids: list[str]) -> list[dict[str, Any]]:
    """Получение данных о каналах и видео с помощью API YouTube."""

    youtube = build('youtube', 'v3', developerKey=api_key)

    for channel_id in channel_ids:
        data = []
        channel_data = youtube.channels().list(part='snippet, statistics', id=channel_id).execute()

        videos_data = []
        while True:
            response = youtube.search().list(part='id,snippet', channelId=channel_id, type='video',
                                             order='date', maxResults=50, pageToken=next_page_token).execute()
            videos_data.extend(response['items'])
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        data.append({
            'channel': channel_data['items'][0],
            'videos': videos_data
        })

    return data