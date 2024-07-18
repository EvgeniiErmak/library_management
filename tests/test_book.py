# library_management/tests/test_book.py

import unittest
from src.book import Book


class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book("Title", "Author", 2020)
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.year, 2020)
        self.assertEqual(book.status, "в наличии")

    def test_book_to_dict(self):
        book = Book("Title", "Author", 2020)
        book_dict = book.to_dict()
        self.assertEqual(book_dict['title'], "Title")
        self.assertEqual(book_dict['author'], "Author")
        self.assertEqual(book_dict['year'], 2020)
        self.assertEqual(book_dict['status'], "в наличии")

    def test_book_from_dict(self):
        book_data = {
            'id': 1,
            'title': "Title",
            'author': "Author",
            'year': 2020,
            'status': "в наличии"
        }
        book = Book.from_dict(book_data)
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.year, 2020)
        self.assertEqual(book.status, "в наличии")


if __name__ == '__main__':
    unittest.main()
