import os
from googleapiclient.discovery import build

API_KEY = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=API_KEY)

channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)

