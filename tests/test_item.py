"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    assert item1.calculate_total_price() == 200000
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    item1.name = 'СуперСмартфон'
    assert item1.name == 'СуперСмарт'


def test_instantiate_from_csv():
    Item.all = []
    items = Item.instantiate_from_csv('../src/items.csv')
    assert len(items) == 5
    assert items[0].name == 'Смартфон'
    assert items[1].name == 'Ноутбук'
    assert items[2].name == 'Кабель'
    assert items[3].price == 50.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('4.0') == 4
    assert Item.string_to_number('3.6') == 3
