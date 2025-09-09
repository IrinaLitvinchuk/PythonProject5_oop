from src.product import Product


def test_init(product1: Product) -> None:
    """Проверяет корректность инициализации объектов класса Product"""
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_price_setter_positive():
    p = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    p.price = 35000.0
    assert p.price == 35000.0


def test_price_setter_zero_or_negative(capsys):
    p = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    p.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 31000.0

    p.price = -10
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 31000.0


def test_price_setter_decrease(monkeypatch):
    p = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # согласие на понижение
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 25000.0
    assert p.price == 25000.0

    # отмена понижения
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 20000.0
    assert p.price == 25000.0


def test_new_product_creation():
    """Проверяет создание нового объекта Product из словаря"""
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    p = Product.new_product(data)
    assert p.name == "Samsung Galaxy S23 Ultra"
    assert p.description == "256GB, Серый цвет, 200MP камера"
    assert p.price == 180000.0
    assert p.quantity == 5


def test_new_or_update_product_duplicate():
    """Проверка обновления объекта при совпадении имени"""
    products = [Product("A", "desc", 100, 5), Product("B", "desc", 200, 2)]
    data = {"name": "A", "description": "desc", "price": 120, "quantity": 3}
    p = Product.new_or_update_product(data, products)
    assert p.quantity == 8  # 5+3
    assert p.price == 120  # максимальная цена
    assert len(products) == 2  # новый объект не добавился


def test_new_or_update_product_new():
    """Проверка создания нового объекта при несовпадении имен"""
    products = [Product("A", "desc", 100, 5), Product("B", "desc", 200, 2)]
    data = {"name": "C", "description": "desc", "price": 50, "quantity": 4}
    p = Product.new_or_update_product(data, products)
    assert p.name == "C"
    assert len(products) == 3


def test_str(product1):
    """Проверка корректности строкового представления"""
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add(product1, product2):
    """Тестирование метода сложения для получения
    суммы произведений цены на количество у двух объектов."""
    assert product1 + product2 == 2580000.0
