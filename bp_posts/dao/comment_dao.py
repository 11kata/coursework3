from json import JSONDecodeError

import json

from bp_posts.dao.comment import Comment
from exceptions.data_exceptions import DataSourceError


class CommentDAO:

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

    def load_comments(self):
        """Возвращает список Comment"""

        comments_data = self.load_data()
        list_of_comments = [Comment(**comment_data) for comment_data in comments_data]
        comments = [Comment(**comment_data) for comment_data in comments_data]
        return list_of_comments

    def get_comments_by_post_pk(self, post_pk: int) -> list[Comment]:
        """Получает все комментарии к определенному посту"""
        comments: list[Comment] = self.load_comments()
        comments_match: list[Comment] = [c for c in comments if c.post_pk == post_pk]
        return comments_match
