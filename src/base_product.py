from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный базовый класс - родительский для класса продуктов"""

    @abstractmethod
    def __str__(self):
        """Строковое отображение в следующем виде:
        Название продукта, Х руб. Остаток: Х шт."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Получение суммы всех товаров на складе"""
        pass

    @abstractmethod
    def price(self, value):
        """Метод для установки цены с проверкой корректности значения"""
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, data: dict):
        """Создает новый объект продукта из словаря"""
        pass

    @classmethod
    @abstractmethod
    def new_or_update_product(cls, data: dict, products: list["Product"]):
        """Создает новый объект или обновляет существующий
        при совпадении имени"""
        pass
