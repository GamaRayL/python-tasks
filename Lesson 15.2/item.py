class Item:
    def __init__(self, name: str, price: int | float, quantity: int = 0) -> None:

        self.__check(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    @staticmethod
    def __check(name, price, quantity):
        if not isinstance(name, str):
            raise TypeError('Название товара должно быть строкой.')

        if not isinstance(price, int | float):
            raise TypeError('Цена товара должна быть числом.')

        if not isinstance(quantity, int):
            raise TypeError('Количество товара должно быть целым числом.')


print(Item('phone', 18000, 5))
Item(1, 18000, 5)
Item('phone', '18000', 5)
Item('phone', 18000, 5.5)
