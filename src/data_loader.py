from pathlib import Path
import json
from src.product import Product
from src.category import Category


def load_data_from_json(filename: str) -> list[Category]:
    """Загружает данные из JSON-файла и возвращает список объектов Category."""
    # Определим абсолютный путь к файлу, независимо от того, откуда запускается скрипт
    base_dir = Path(__file__).resolve().parent.parent  # поднимаемся на уровень выше, из src/
    file_path = base_dir / filename

    if not file_path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден.")

    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for cat in data:
        products = [
            Product(p["name"], p["description"], p["price"], p["quantity"])
            for p in cat.get("products", [])
        ]
        category = Category(cat["name"], cat["description"], products)
        categories.append(category)

    return categories


if __name__ == "__main__":
    categories = load_data_from_json("data/products.json")

    for category in categories:
        print(f"{category.name}: {len(category.products)} товаров")