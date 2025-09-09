class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price  # приватный атрибут
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        result = ((self.__price * self.quantity)
                  + (other.__price * other.quantity))
        return result

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        old_price = self.__price

        if value < old_price:
            user_input = input(
                f"Старая цена: {old_price}. "
                f"Вы хотите понизить цену до {value}? (y/n): "
            )
            if user_input.lower() == "y":
                self.__price = value
            else:
                print("Действие отменено. Цена не изменилась.")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, data: dict):
        """Создает новый объект Product из словаря"""
        return cls(data["name"],
                   data["description"],
                   data["price"],
                   data["quantity"])

    # Доп.метод для проверки дубликатов - Дополнительное задание (к заданию 3)
    @classmethod
    def new_or_update_product(cls, data: dict,
                              products: list["Product"]) -> "Product":
        """Создает новый объект или обновляет существующий
        при совпадении имени."""
        # ищем дубликат по имени
        for product in products:
            if product.name == data["name"]:
                # обновляем количество
                product.quantity += data["quantity"]
                # оставляем более высокую цену
                product.price = max(product.price, data["price"])
                return product

        # если дубликата нет — создаём новый товар
        new = cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )
        products.append(new)
        return new
