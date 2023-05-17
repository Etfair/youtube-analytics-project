import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Video:
    """
    Класс для ютуб-канала
    """
    API_KEY: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, video_id: str):
        self.video_id = video_id

        try:
            self.video_link = f'https://www.youtube.com/watch?v={self.video_id}'

        except HttpError:
            self.video_info = None
            self.title = None
            self.video_link = None
            self.video_views = None
            self.like_count = None

        try:
            self.video_info = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
            self.title = self.video_info['items'][0]['snippet']['title']

        except IndexError:
            self.video_info = None
            self.title = None
            self.video_link = None
            self.video_views = None
            self.like_count = None

        else:
            self.video_info = self.youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
            self.title = self.video_info['items'][0]['snippet']['title']
            self.video_link = f'https://www.youtube.com/watch?v={self.video_id}'
            self.video_views = self.video_info["items"][0]["statistics"]["viewCount"]
            self.like_count = self.video_info["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return self.title

    def get_info(self):
        """
        Выводит в консоль информацию о канале
        """
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails', id=self.video_id).execute()
        return video_response


class PLVideo(Video):
    """
    Наследуемый класс от Video
    """
    def __init__(self, video_id: str, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
