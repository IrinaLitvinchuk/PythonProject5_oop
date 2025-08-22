from src.product import Product


class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self,
                 name: str,
                 description: str,
                 products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products # приватный атрибут
        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, new_product: Product) -> None:
        "Добавляет товар в категорию"
        self.__products.append(new_product)
        Category.product_count += 1


    @property
    def products(self) -> str:
        """Возвращает список товаров в виде строк."""
        lines = []
        for product in self.__products:
            lines.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(lines)


