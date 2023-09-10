import pytest

from src.product import Product


@pytest.fixture
def product():
    return Product("Ноутбук", 99999, 40)


def test_init(product):
    assert product.name == "Ноутбук"
    assert product.price == 99999
    assert product.count == 40


def test_sale(product):
    product.sale(1)
    assert product.count == 39


def test_fill(product):
    product.fill(10)
    assert product.count == 50
