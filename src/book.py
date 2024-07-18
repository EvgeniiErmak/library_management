# library_management/src/book.py

import json
from typing import Any, Dict


class Book:
    """
    Класс для представления книги.
    """
    def __init__(self, title: str, author: str, year: int) -> None:
        """
        Инициализация экземпляра книги.

        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        """
        self.id = self.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def generate_id(self) -> int:
        """
        Генерация уникального идентификатора для книги.

        :return: Уникальный идентификатор книги
        """
        try:
            with open('src/data/books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
            return max(book['id'] for book in books) + 1
        except (FileNotFoundError, ValueError):
            return 1

    def to_dict(self) -> Dict[str, Any]:
        """
        Преобразование экземпляра книги в словарь.

        :return: Словарь с данными книги
        """
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Book':
        """
        Создание экземпляра книги из словаря.

        :param data: Словарь с данными книги
        :return: Экземпляр книги
        """
        book = Book(data['title'], data['author'], data['year'])
        book.id = data['id']
        book.status = data['status']
        return book
