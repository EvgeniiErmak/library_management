# library_management/tests/test_library.py

import unittest
from src.library import Library


class TestLibrary(unittest.TestCase):
    """
    Тесты для класса Library.
    """
    def setUp(self):
        """
        Подготовка временной библиотеки для тестов.
        """
        self.library = Library(data_file='../test_books.json')
        self.library.books = []

    def test_add_book(self):
        """
        Тест добавления новой книги.
        """
        self.library.add_book("Title", "Author", 2020)
        self.assertEqual(len(self.library.books), 1)

    def test_delete_book(self):
        """
        Тест удаления книги по ID.
        """
        self.library.add_book("Title", "Author", 2020)
        book_id = self.library.books[0].id
        self.assertTrue(self.library.delete_book(book_id))
        self.assertEqual(len(self.library.books), 0)

    def test_find_book_by_id(self):
        """
        Тест поиска книги по ID.
        """
        self.library.add_book("Title", "Author", 2020)
        book_id = self.library.books[0].id
        book = self.library.find_book_by_id(book_id)
        self.assertIsNotNone(book)
        self.assertEqual(book.title, "Title")

    def test_search_books(self):
        """
        Тест поиска книг по заданному полю.
        """
        self.library.add_book("Title1", "Author1", 2020)
        self.library.add_book("Title2", "Author2", 2021)
        books = self.library.search_books("Title1", "title")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Title1")

    def test_update_book_status(self):
        """
        Тест обновления статуса книги.
        """
        self.library.add_book("Title", "Author", 2020)
        book_id = self.library.books[0].id
        self.assertTrue(self.library.update_book_status(book_id, "выдана"))
        self.assertEqual(self.library.books[0].status, "выдана")


if __name__ == '__main__':
    unittest.main()
