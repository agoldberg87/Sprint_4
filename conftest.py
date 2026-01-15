import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def add_base_books(collector):
    collector.add_new_book('Шум за сценой')
    collector.add_new_book('Дюна')
    collector.add_new_book('Кошечки-собачки')
    collector.add_new_book('Кладбище домашних животных')
    collector.add_new_book('Гордость и предубеждение и зомби')
    collector.add_new_book('Что делать, если ваш кот хочет вас убить')
    
    return collector