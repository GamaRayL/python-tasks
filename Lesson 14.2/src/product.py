class Product:
    def __init__(self, name: str, price: int or float, count: int):
        self.name = name
        self.price = price
        self.__count = count

    @property
    def count(self):
        return self.__count

    def sale(self, sale_count):
        self.__count -= sale_count

    def fill(self, fill_count):
        self.__count += fill_count
