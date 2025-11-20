from src.product import LawnGrass, Product, Smartphone


def test_print_mixin(capsys):
    """Проверка корректного вывода в консоль информации
    при создании экземпляров классов"""

    Product("Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет, 200MP камера",
            180000.0,
            5)

    message = capsys.readouterr()
    assert (
        message.out
        == "Product(Samsung Galaxy S23 Ultra, 256GB, "
           "Серый цвет, 200MP камера, 180000.0, 5)\n"
    )

    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )

    message = capsys.readouterr()
    assert (
        message.out
        == "LawnGrass(Газонная трава, Элитная трава для газона, 500.0, 20)\n"
    )

    Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )

    message = capsys.readouterr()
    assert message.out == (
        "Smartphone(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, "
        "200MP камера, 180000.0, 5)\n"
    )
