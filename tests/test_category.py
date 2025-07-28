from src.category import Category

def test_init(category1, products):
    assert category1.name == "Смартфоны"
    assert category1.description == (
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category1.products == products


def test_category_and_product_count_reset(products, product4):
    # Сбросим счётчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Смартфоны", "desc", products)
    category2 = Category("Телевизоры", "desc", [product4])

    assert Category.category_count == 2
    assert Category.product_count == 4
