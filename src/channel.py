import json
import os
from googleapiclient.discovery import build


API_KEY = os.getenv('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=API_KEY)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel[0]['snippet']['title']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel[0]['snippet']['title']
        self.description = self.channel[0]['snippet']['description']
        print(f'Информацию о канале {self.channel}')
        print(f'Информацию о канале {self.title}')
        print(f'Информацию о канале {self.description}')


    @classmethod
    def get_service(cls):
        """"""
        return
        pass

    def to_json(dict_to_print: dict):
        """"""
        print(json.dump(dict_to_print, indent=2, ensure_ascii=False))
        # state = {}
        # state['title'] = self.title
        # state['description'] = self.description
        # state['url'] = self.url
        # state['subscriber_count'] = self.subscriber_count
        # state['video_count'] = self.video_count
        # state['view_count'] = self.view_count

        # with open("file.json", "wb") as f:
        #   pickle.dump(self.state, f)

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self,chanell_id):
        pass

# print(f'Информацию о канале {self.channel}')
# print(f'Информацию о канале {self.title}')
# print(f'Информацию о канале {self.description}')
