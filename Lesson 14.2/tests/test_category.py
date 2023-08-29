import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("Ноутбук", 99999, 40)


@pytest.fixture
def category():
    return Category("Компьютерная техника", [product])


def test_init(category):
    assert category.name == "Компьютерная техника"
    assert category.products == [product]


def test_remove_item(category):
    category.remove(0)
    assert category.products == []


def test_add_item(category):
    category + product
    assert category.products == [product, product]
