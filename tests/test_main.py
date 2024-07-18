# library_management/tests/test_main.py

import unittest
from unittest.mock import patch, MagicMock
import sys
import io
from src.library import Library
from src.main import main


class TestMain(unittest.TestCase):
    def setUp(self):
        # Создание временной библиотеки для тестов
        self.library = Library(data_file='test_books.json')
        self.library.books = []

    @patch('builtins.input', side_effect=['1', 'Test Title', 'Test Author', '2020', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_book(self, mock_stdout, mock_input):
        with patch('src.library.Library', return_value=self.library):
            main()
        output = mock_stdout.getvalue()
        self.assertIn("Книга добавлена.", output)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, 'Test Title')

    @patch('builtins.input', side_effect=['2', '1', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_book(self, mock_stdout, mock_input):
        self.library.add_book("Test Title", "Test Author", 2020)
        with patch('src.library.Library', return_value=self.library):
            main()
        output = mock_stdout.getvalue()
        self.assertIn("Книга удалена.", output)
        self.assertEqual(len(self.library.books), 0)

    @patch('builtins.input', side_effect=['3', 'title', 'Test Title', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_book(self, mock_stdout, mock_input):
        self.library.add_book("Test Title", "Test Author", 2020)
        with patch('src.library.Library', return_value=self.library):
            main()
        output = mock_stdout.getvalue()
        self.assertIn("Test Title", output)
        self.assertIn("Test Author", output)
        self.assertIn("2020", output)

    @patch('builtins.input', side_effect=['4', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_books(self, mock_stdout, mock_input):
        self.library.add_book("Test Title", "Test Author", 2020)
        with patch('src.library.Library', return_value=self.library):
            main()
        output = mock_stdout.getvalue()
        self.assertIn("Test Title", output)
        self.assertIn("Test Author", output)
        self.assertIn("2020", output)

    @patch('builtins.input', side_effect=['5', '1', 'выдана', '6'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_book_status(self, mock_stdout, mock_input):
        self.library.add_book("Test Title", "Test Author", 2020)
        with patch('src.library.Library', return_value=self.library):
            main()
        output = mock_stdout.getvalue()
        self.assertIn("Статус книги обновлен.", output)
        self.assertEqual(self.library.books[0].status, "выдана")


if __name__ == '__main__':
    unittest.main()
