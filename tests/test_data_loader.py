import json
from pathlib import Path

import pytest

from src.category import Category
from src.data_loader import load_data_from_json
from src.product import Product


def test_load_data_from_json_success(tmp_path: Path) -> None:
    """Тест корректной загрузки json-файла"""
    test_data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                }
            ],
        }
    ]

    file_path = tmp_path / "test_data.json"
    file_path.write_text(json.dumps(test_data, ensure_ascii=False),
                         encoding="utf-8")

    categories = load_data_from_json(str(file_path))

    assert isinstance(categories, list)
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert len(categories[0].products) == 1
    assert isinstance(categories[0].products[0], Product)
    assert categories[0].name == "Смартфоны"
    assert categories[0].products[0].name == "Iphone 15"


def test_load_data_from_json_file_not_found() -> None:
    """Тест на FileNotFoundError, если файл не найден"""
    with pytest.raises(FileNotFoundError):
        load_data_from_json("data/nonexistent_file.json")


def test_load_data_from_json_empty_file(tmp_path: Path) -> None:
    """Тест с пустым JSON-файлом"""
    file_path = tmp_path / "empty.json"
    file_path.write_text("[]", encoding="utf-8")

    categories = load_data_from_json(str(file_path))

    assert isinstance(categories, list)
    assert categories == []


def test_load_data_from_json_missing_price(tmp_path: Path) -> None:
    """Тестирование обработки ошибки, когда данные неполные,
    например, у продукта нет цены"""

    test_data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "quantity": 8,  # нет price
                },
                {
                    "name": "Xiaomi",
                    "description": "128GB",
                    "price": 31000.0,
                    "quantity": 10,
                },
            ],
        }
    ]

    file_path = tmp_path / "incomplete_data.json"
    file_path.write_text(json.dumps(test_data, ensure_ascii=False),
                         encoding="utf-8")

    categories = load_data_from_json(file_path)

    assert len(categories) == 1
    assert len(categories[0].products) == 1  # только Xiaomi загружен
    assert categories[0].products[0].name == "Xiaomi"
