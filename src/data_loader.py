from pathlib import Path
import json
from src.product import Product
from src.category import Category

def load_data_from_json(filename: str) -> list[Category]:
    """Загружает данные из JSON-файла и возвращает список объектов Category."""
    file_path = Path(filename)  # теперь можно подавать и абсолютный, и относительный путь

    if not file_path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    categories = []

    for cat in data:
        products = []
        for p in cat.get("products", []):
            try:
                product = Product(
                    name=p["name"],
                    description=p["description"],
                    price=p["price"],  # это может вызвать KeyError
                    quantity=p["quantity"]
                )
                products.append(product)
            except KeyError as e:
                print(f"Продукт пропущен из-за отсутствия ключа: {e}")
                continue

        category = Category(cat["name"], cat["description"], products)
        categories.append(category)

    return categories


if __name__ == "__main__":
    categories = load_data_from_json( r"C:\Users\Irina Litvinchuk\PycharmProjects\PythonProject5_oop\data\products.json")

    for category in categories:
        print(f"{category.name}: {len(category.products)} товаров")