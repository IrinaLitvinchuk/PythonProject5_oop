import unittest
from typing import List
from src.base_product import BaseProduct
from src.product import Product


# Создаем специальный тестовый класс для проверок
class TestProduct(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self._price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, BaseProduct):
            return self._price * self.quantity + other._price * other.quantity
        raise TypeError("Ошибка добавления")

    def price(self, value):
        if value > 0:
            self._price = value
        else:
            raise ValueError("Недопустимая цена")

    @classmethod
    def new_product(cls, data: dict):
        return cls(**data)

    @classmethod
    def new_or_update_product(cls, data: dict, products: List['TestProduct']):
        matching_products = [product for product in products if product.name == data.get('name')]
        if matching_products:
            matching_product = matching_products[0]
            matching_product.quantity += data.get('quantity', 0)
            matching_product.price(data.get('price'))
            return matching_product
        else:
            return cls.new_product(data)

class TestAbstractClass(unittest.TestCase):
    def test_str_representation(self):
        test_product = TestProduct(name="Тестовый продукт", description="Простое описание",
                                      price=100.0, quantity=5)
        expected_output = "Тестовый продукт, 100.0 руб. Остаток: 5 шт."
        assert str(test_product) == expected_output

    def test_addition(self):
        first_product = TestProduct(name="Продукт А", description="", price=10.0, quantity=10)
        second_product = TestProduct(name="Продукт Б", description="", price=20.0, quantity=5)
        assert first_product + second_product == 200.0

    def test_set_price_valid(self):
        test_product = TestProduct(name="Тестовый продукт", description="", price=100.0, quantity=5)
        test_product.price = 150.0
        assert test_product.price == 150.0

    def test_set_price_invalid(self):
        test_product = TestProduct(name="Тестовый продукт", description="", price=100.0, quantity=5)
        with self.assertRaises(ValueError):
            test_product.price(-50.0)

if __name__ == '__main__':
    unittest.main()