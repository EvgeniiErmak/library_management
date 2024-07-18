# library_management/src/library.py

import json
from typing import List, Optional
from src.book import Book


class Library:
    """
    Класс для управления библиотекой.
    """
    def __init__(self, data_file: str = 'data/books.json') -> None:
        """
        Инициализация экземпляра библиотеки.

        :param data_file: Путь к файлу данных
        """
        self.data_file = data_file
        self.books = self.load_books()

    def load_books(self) -> List[Book]:
        """
        Загрузка книг из файла данных.

        :return: Список экземпляров книг
        """
        try:
            with open(self.data_file, 'r', encoding='utf-8') as file:
                books_data = json.load(file)
            return [Book.from_dict(book) for book in books_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self) -> None:
        """
        Сохранение книг в файл данных.
        """
        with open(self.data_file, 'w', encoding='utf-8') as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """
        Добавление новой книги в библиотеку.

        :param title: Название книги
        :param author: Автор книги
        :param year: Год издания книги
        """
        new_book = Book(title, author, year)
        self.books.append(new_book)
        self.save_books()

    def delete_book(self, book_id: int) -> bool:
        """
        Удаление книги из библиотеки по ID.

        :param book_id: Уникальный идентификатор книги
        :return: True, если книга успешно удалена, иначе False
        """
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            return True
        return False

    def find_book_by_id(self, book_id: int) -> Optional[Book]:
        """
        Поиск книги по ID.

        :param book_id: Уникальный идентификатор книги
        :return: Экземпляр книги, если найдена, иначе None
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, query: str, field: str) -> List[Book]:
        """
        Поиск книг по заданному полю.

        :param query: Строка поиска
        :param field: Поле для поиска (title, author, year)
        :return: Список найденных книг
        """
        return [book for book in self.books if query.lower() in getattr(book, field).lower()]

    def list_books(self) -> List[Book]:
        """
        Получение списка всех книг в библиотеке.

        :return: Список экземпляров книг
        """
        return self.books

    def update_book_status(self, book_id: int, status: str) -> bool:
        """
        Обновление статуса книги.

        :param book_id: Уникальный идентификатор книги
        :param status: Новый статус книги (в наличии, выдана)
        :return: True, если статус успешно обновлен, иначе False
        """
        book = self.find_book_by_id(book_id)
        if book:
            book.status = status
            self.save_books()
            return True
        return False
