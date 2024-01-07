from src.item import Item

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.
    assert item.name == 'СуперСмарт'
    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла

    assert len(Item.all) == 6  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'СуперСмарт'

    item1 = Item.all[1]

    assert item1.name == 'Смартфон'
    assert item1.price == 100.0

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
