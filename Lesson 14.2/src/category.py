from typing import List


class Category:
    def __init__(self, name: str, products: List):
        self.name = name
        self.__products = products
        self.__is_active = True

    @property
    def is_active(self):
        return self.__is_active

    @property
    def products(self):
        return self.__products

    def remove(self, index):
        del self.__products[index]

    def __add__(self, product):
        self.__products.append(product)
