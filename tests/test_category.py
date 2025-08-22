from src.category import Category
from src.product import Product


def test_init_Category(category1: Category, products: list[Product]) -> None:
    """Проверяет корректность инициализации объектов класса Category"""
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )

    # Проверяем список объектов
    assert category1.get_products() == products

    # Проверяем строковое представление
    output = category1.products
    for product in products:
        assert product.name in output
        assert str(product.price) in output
        assert str(product.quantity) in output


def test_category_and_product_count_reset(
    products: list[Product], product4: Product
) -> None:
    """Проверяет подсчет количества продуктов и категорий"""
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Смартфоны", "desc", products)
    category2 = Category("Телевизоры", "desc", [product4])

    assert category1.name == "Смартфоны"
    assert category2.name == "Телевизоры"
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_multiple_category_counts(products: list[Product],
                                  product4: Product) -> None:
    """Проверка, как счётчики работают при добавлении
    нескольких категорий подряд"""
    Category.category_count = 0
    Category.product_count = 0

    Category("Смартфоны", "desc", products)
    Category("Телевизоры", "desc", [product4])
    Category("Пустая", "desc", [])

    assert Category.category_count == 3
    assert Category.product_count == 4  # 3+1+0


def test_category_with_no_products() -> None:
    """Проверяет создание категории, если список продуктов пустой"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Пустая категория", "Нет товаров", [])

    assert category.name == "Пустая категория"
    assert category.get_products() == []  # список объектов пустой
    assert category.products == ""  # строка пустая
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_with_duplicate_products(product1: Product) -> None:
    """Тест с дубликатами продуктов"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Повторы", "одинаковые", [product1, product1])

    # Проверяем список объектов
    products = category.get_products()
    assert len(products) == 2
    assert all(p is product1 for p in products)

    # Проверяем строковое представление
    lines = category.products.splitlines()
    assert len(lines) == 2
    assert all(product1.name in line for line in lines)

    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_add_product_and_getter(category1: Category,
                                         products: list[Product]):
    """Проверяет добавление товара и работу геттера products"""
    Category.category_count = 0
    Category.product_count = 0

    p1, p2 = products[0], products[1]

    # Создаём категорию с первым продуктом
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        [p1],
    )

    # Проверка начального списка объектов
    assert category.get_products() == [p1]

    # Проверка строкового представления
    output = category.products
    assert f"{p1.name}, {p1.price} руб. Остаток: {p1.quantity} шт." in output

    # Добавление нового продукта
    category.add_product(p2)

    # Список объектов
    assert category.get_products() == [p1, p2]

    # Строковое представление
    output = category.products
    assert f"{p2.name}, {p2.price} руб. Остаток: {p2.quantity} шт." in output

    assert Category.product_count == 2
