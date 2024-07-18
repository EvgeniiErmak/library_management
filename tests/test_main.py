# library_management/tests/test_main.py

import os
import unittest
from unittest.mock import patch, MagicMock
import sys
import io
from src.library import Library
from src.main import main


class TestMain(unittest.TestCase):
    """
    Тесты для проверки основного функционала приложения управления библиотекой.
    """

    def setUp(self):
        """
        Подготовка временной библиотеки для тестов.
        """
        self.test_file = os.path.join(os.path.dirname(__file__), '..', 'test_books.json')
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.library = Library(data_file=self.test_file)

    @patch('builtins.input', side_effect=['1', 'Test Title', 'Test Author', '2020', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_book(self, mock_stdout, mock_input):
        """
        Тест добавления книги.
        """
        library = main(self.library)
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0].title, 'Test Title')

    @patch('builtins.input', side_effect=['2', '1', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_book(self, mock_stdout, mock_input):
        """
        Тест удаления книги.
        """
        self.library.add_book("Test Title", "Test Author", 2020)
        library = main(self.library)
        self.assertEqual(len(library.books), 0)

    @patch('builtins.input', side_effect=['3', '1', 'Test Title', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_book(self, mock_stdout, mock_input):
        """
        Тест поиска книги.
        """
        self.library.add_book("Test Title", "Test Author", 2020)
        main(self.library)
        output = mock_stdout.getvalue()
        self.assertIn("Test Title", output)
        self.assertIn("Test Author", output)
        self.assertIn("2020", output)

    @patch('builtins.input', side_effect=['4', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_books_with_books(self, mock_stdout, mock_input):
        """
        Тест отображения списка книг при наличии книг.
        """
        self.library.add_book("Test Title", "Test Author", 2020)
        main(self.library)
        output = mock_stdout.getvalue()
        self.assertIn("Test Title", output)
        self.assertIn("Test Author", output)
        self.assertIn("2020", output)

    @patch('builtins.input', side_effect=['4', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_books_without_books(self, mock_stdout, mock_input):
        """
        Тест отображения списка книг при отсутствии книг.
        """
        main(self.library)
        output = mock_stdout.getvalue()
        self.assertIn("В библиотеке нет книг.", output)

    @patch('builtins.input', side_effect=['5', '1', '2', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_book_status(self, mock_stdout, mock_input):
        """
        Тест обновления статуса книги.
        """
        self.library.add_book("Test Title", "Test Author", 2020)
        library = main(self.library)
        self.assertEqual(library.books[0].status, "выдана")


if __name__ == '__main__':
    unittest.main()
