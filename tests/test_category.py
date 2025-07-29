from src.category import Category


def test_init_Category(category1, products):
    """Проверяет корректность инициализации объектов класса Category"""
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category1.products == products


def test_category_and_product_count_reset(products, product4):
    """Проверяет подсчет количества продуктов и категорий"""
    # Сбросим счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Смартфоны", "desc", products)
    category2 = Category("Телевизоры", "desc", [product4])

    assert category1.name == "Смартфоны"
    assert category2.name == "Телевизоры"
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_multiple_category_counts(products, product4):
    """Проверка, как счётчики работают при добавлении нескольких категорий подряд."""
    Category.category_count = 0
    Category.product_count = 0

    Category("Смартфоны", "desc", products)
    Category("Телевизоры", "desc", [product4])
    Category("Пустая", "desc", [])

    assert Category.category_count == 3
    assert Category.product_count == 4  # 3+1+0

def test_category_with_no_products():
    """Проверяет создание категории, если список продуктов пустой"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Пустая категория",
                        "Нет товаров",
                        [])

    assert category.name == "Пустая категория"
    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_with_duplicate_products(product1):
    """Тест с нестандартными данными (например, дубликаты продуктов)"""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Повторы", "одинаковые", [product1, product1])

    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


