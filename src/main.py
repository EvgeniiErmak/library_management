# library_management/src/main.py

import sys
from src.library import Library


def main() -> None:
    """
    Основная функция для запуска приложения управления библиотекой.
    """
    library = Library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания книги: ")
            library.add_book(title, author, int(year))
            print("Книга добавлена.")
        elif choice == '2':
            book_id = int(input("Введите ID книги для удаления: "))
            if library.delete_book(book_id):
                print("Книга удалена.")
            else:
                print("Книга не найдена.")
        elif choice == '3':
            print("Выберите параметр для поиска:")
            print("1. Title / Название")
            print("2. Author / Автор")
            print("3. Year / Год издания")
            param_choice = input("Введите номер параметра: ")

            if param_choice == '1':
                field = 'title'
            elif param_choice == '2':
                field = 'author'
            elif param_choice == '3':
                field = 'year'
            else:
                print("Неверный выбор, попробуйте снова.")
                continue

            query = input(f"Введите значение для поиска по {field}: ")
            books = library.search_books(query, field)
            if books:
                for book in books:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("Книги не найдены.")
        elif choice == '4':
            books = library.list_books()
            if books:
                for book in books:
                    print(f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
            else:
                print("В библиотеке нет книг.")
        elif choice == '5':
            book_id = int(input("Введите ID книги для изменения статуса: "))
            if not library.find_book_by_id(book_id):
                print("Книга не найдена.")
                continue

            print("Выберите новый статус:")
            print("1. В наличии")
            print("2. Выдана")
            status_choice = input("Введите номер нового статуса: ")

            if status_choice == '1':
                status = "в наличии"
            elif status_choice == '2':
                status = "выдана"
            else:
                print("Неверный выбор, попробуйте снова.")
                continue

            if library.update_book_status(book_id, status):
                print("Статус книги обновлен.")
            else:
                print("Книга не найдена.")
        elif choice == '6':
            print("Выход из программы.")
            sys.exit()
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == '__main__':
    main()
