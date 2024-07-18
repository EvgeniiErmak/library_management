# library_management/src/book.py

import json
from typing import Any, Dict


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.id = self.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"

    def generate_id(self) -> int:
        try:
            with open('data/books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
            return max(book['id'] for book in books) + 1
        except (FileNotFoundError, ValueError):
            return 1

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Book':
        book = Book(data['title'], data['author'], data['year'])
        book.id = data['id']
        book.status = data['status']
        return book
