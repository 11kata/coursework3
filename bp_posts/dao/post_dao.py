import json
from json import JSONDecodeError

from bp_posts.dao.post import Post
from exceptions.data_exceptions import DataSourceError


class PostDAO:
    """Менеджер постов"""

    def __init__(self, path):
        self.path = path

    def load_data(self):
        """Загружает данные из JSON и возвращает"""

        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                posts_data = json.load(file)
        except(FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f'Не удается получит данные из файла {self.path}')

        return posts_data

    def load_posts(self):
        """Возвращает список Post"""

        posts_data = self.load_data()
        list_of_posts = [Post(**post_data) for post_data in posts_data]

        return list_of_posts

    def get_all(self):
        """Получает все посты"""

        posts = self.load_posts()
        return posts

    def get_pk(self, pk):
        """Получает пост по Pk"""
        if type(pk) != int:
            raise TypeError('pk must be an int')

        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):
        """Ищет посты где встречается substring """
        substring = str(substring)
        posts = self.load_posts()
        matching_posts = [post for post in posts if substring in post.content.lower()]
        return matching_posts

    def get_poster(self, user_name):
        """Ищет посты по имени"""
        user_name = str(user_name).lower()
        posts = self.load_posts()
        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]
        return matching_posts



