from src.product import Product


class Category:
    name: str
    description: str
    products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str,
                 products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products  # приватный атрибут
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Строковое отображение в следующем виде:
        Название категории, количество продуктов: Х шт."""
        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, new_product: Product) -> None:
        """Добавляет товар в категорию, таким образом,
        чтобы не было возможности добавить вместо продукта или его наследников
        любой другой объект."""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        else:
            raise (TypeError
                   ("Возникла ошибка TypeError при добавлении не продукта"))

    @property
    def products(self) -> str:
        """Возвращает список товаров в виде строк."""
        lines = []
        for product in self.__products:
            lines.append(
                f"{product.name}, {product.price} руб. "
                f"Остаток: {product.quantity} шт."
            )
        return "\n".join(lines)

    def get_products(self) -> list[Product]:
        """Возвращает список объектов Product
        (для тестов и внутренней логики)"""
        return self.__products

    def middle_price(self):
        all_prices = 0
        try:
            for product in self.__products:
                all_prices += product.price
            middle_price = all_prices / len(self.__products)
            return round(middle_price, 2)
        except ZeroDivisionError:
            return 0.0

