# library_management/src/library.py

import json
from typing import List, Optional

from src.book import Book


class Library:
    def __init__(self, data_file: str = 'data/books.json') -> None:
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
            return [Book.from_dict(book) for book in books_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self) -> None:
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()

    def delete_book(self, book_id: int) -> bool:
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, query: str, field: str) -> List[Book]:
        return [book for book in self.books if query.lower() in getattr(book, field).lower()]

    def list_books(self) -> List[Book]:
        return self.books

    def update_book_status(self, book_id: int, status: str) -> bool:
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            self.save_books()
            return True
        return False
