from src.product import Product


def test_init(product1: Product) -> None:
    """Проверяет корректность инициализации объектов класса Product"""
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5
