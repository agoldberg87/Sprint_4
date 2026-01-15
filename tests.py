import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # ТЕСТ 1: присваивание жанра
    # покрывает методы add_new_book, set_book_genre, get_books_genre
    @pytest.mark.parametrize('name, genre', 
    [
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Что делать, если ваш кот хочет вас убить', 'Детективы'),
        ('Дюna', 'Фантастика'),
        ('Кладбище домашних животных', 'Ужасы'),
        ('Кошечки-собачки', 'Мультфильмы'),
        ('Шум за сценой', 'Комедии')
    ])
    
    
    def test_set_book_genre_returns_genre(self, collector, name, genre):
        collector.add_new_book(name)
        
        # Назначаем книге жанр
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre()[name] == genre

    
    # ТЕСТ 2: фильтр по жанру
    # покрывает методы add_new_book, set_book_genre, get_books_with_specific_genre
    def test_get_books_with_specific_genre_returns_two_books(self, collector, add_base_books):
        
        # Устанавливаем жанр
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        
        # Проверяем, что фильтр работает
        assert collector.get_books_with_specific_genre('Ужасы') == ['Кладбище домашних животных', 'Гордость и предубеждение и зомби']

    # ТЕСТ 3: текущие жанры
    # покрывает методы add_new_book, set_book_genre, get_books_genre
    @pytest.mark.parametrize('name, genre', 
    [
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Что делать, если ваш кот хочет вас убить', 'Детективы'),
        ('Шум за сценой', 'Комедии'),
        ('Дюна', 'Фантастика'),
        ('Кошечки-собачки', 'Мультфильмы')
    ])
    def test_get_books_genres_returns_name_genre(self, collector, name, genre):
        
        # Устанавливаем жанр
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {(name):(genre)}
    
    # ТЕСТ 4: фильтр по возрастной категории
    # покрывает методы add_new_book, set_book_genre, get_books_for_children

    def test_get_books_for_children_returns_two_books(self, collector, add_base_books):
        
        # Затем устанавливаем жанр
        collector.set_book_genre('Дюна', 'Фантастика') 
        collector.set_book_genre('Кошечки-собачки', 'Мультфильмы')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        # Проверяем, что фильтр работает
        assert collector.get_books_for_children() == ['Дюна', 'Кошечки-собачки']

    # ТЕСТ 5: добавление в избранное
    # покрывает методы add_new_book, add_book_in_favorites, get_list_of_favorites_books
    def test_add_book_in_favorites_returns_two_books(self, collector, add_base_books):

        # Затем добавляем в избранное
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Кошечки-собачки')

        # Проверяем, что фильтр работает
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Кошечки-собачки']

    # ТЕСТ 6: удаление из избранного
    # покрывает методы add_new_book, add_book_in_favorites, delete_book_from_favorites, get_list_of_favorites_books
    def test_delete_book_from_favorites_returns_one_book(self, collector, add_base_books):

        # Затем добавляем в избранное две книги
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Кошечки-собачки')

        # Затем удаляем из избранного одну книгу
        collector.delete_book_from_favorites('Дюна')

        # Проверяем, что фильтр работает
        assert collector.get_list_of_favorites_books() == ['Кошечки-собачки']

    # ТЕСТ 7: валидация названия книги
    # покрывает метод add_new_book
    @pytest.mark.parametrize('name', ['', 'Тестовое название книги больше сорока символов'])
    def test_add_new_book_invalid_name_returns_empty(self, collector, name):
        collector.add_new_book(name)
        assert collector.get_books_genre() == {}

    # ТЕСТ 8: валидация жанра книги
    # покрывает методы add_new_book, set_book_genre, get_books_genre
    def test_set_book_genre_invalid_genre_returns_empty(self, collector):
        collector.add_new_book('Тестовая книга')

        # Устанавливаем невалидный жанр
        collector.set_book_genre('Тестовая книга', 'Тестовый жанр')
        assert collector.get_books_genre()['Тестовая книга'] == ''

    # ТЕСТ 9: валидация сортировки по возврастному рейтингу
    # покрывает методы add_new_book, set_book_genre, get_books_for_children
    @pytest.mark.parametrize('name, genre', [
        ('Гордость и предубеждение и зомби', 'Ужасы'),
        ('Что делать, если ваш кот хочет вас убить', 'Детективы')
    ])
    def test_get_books_for_children_invalid_genre_returns_empty(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == []

    # ТЕСТ 10: валидация сортировки по жанру
    def test_get_books_with_specific_genre_invalid_genre_returns_empty(self, collector, add_base_books):
    
        # Устанавливаем жанр
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
    
        # Проверяем, что фильтр работает
        assert collector.get_books_with_specific_genre('Комедии') == []


    # ТЕСТ 11: валидация добавления книги в избранное
    def test_add_book_in_favorites_invalid_book_returns_empty(self, collector, add_base_books):

        # Затем добавляем в избранное
        collector.add_book_in_favorites('Идиот')
        collector.add_book_in_favorites('Как тестируют в Google')

        # Проверяем, что фильтр работает
        assert collector.get_list_of_favorites_books() == []

    # ТЕСТ 12: валидация удаления книги из избранного
    def test_delete_book_from_favorites_invalid_book_returns_two_books(self, collector, add_base_books):

        # Затем добавляем в избранное две книги
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Кошечки-собачки')

        # Затем удаляем из избранного одну книгу
        collector.delete_book_from_favorites('Кладбище домашних животных')

        # Проверяем, что фильтр работает
        assert collector.get_list_of_favorites_books() == ['Дюна', 'Кошечки-собачки']