class PrintMixin:
    """Класс-миксин, который печатает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект."""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.name}, {self.description}, "
            f"{self.price}, {self.quantity})"
        )
