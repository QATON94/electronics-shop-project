import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate: float = 0.9
    all: list = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value) -> None:
        try:
            if len(value) < 10:
                self.__name = value
            else:
                raise Exception('Длина наименования товара превышает 10 символов.')
        except:
            print('Exception: Длина наименования товара превышает 10 символов.')
            self.__name = value[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path: str) -> list:
        """
        Создание экземпляра класса item из данных файла.

        :param path: Путь к файлу с данными по товарам.
        """
        with open(path, 'r') as f:
            reader = csv.DictReader(f)
            for read in reader:
                name = read['name']
                price = float(read['price'])
                quantity = int(read['quantity'])
                cls(name, price, quantity)
            return cls.all

    @staticmethod
    def string_to_number(string: str) -> float:
        """
        Преобразование строки в число.

        :param string: Преобразованная строка.
        :return: Преобразованное число.
        """
        return int(float(string))
