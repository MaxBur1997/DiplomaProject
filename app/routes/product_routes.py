from flask import Blueprint, jsonify

# Создаем Blueprint для маршрутов товаров
product_bp = Blueprint('product', __name__, url_prefix='/products')

# Временные данные для тестирования
products = [
    {"id": 1, "name": "Классический пончик", "price": 50.0, "description": "Классический вкус.", "image_url": "/static/images/classic.png"},
    {"id": 2, "name": "Шоколадный пончик", "price": 60.0, "description": "С шоколадной глазурью.", "image_url": "/static/images/chocolate.png"}
]

@product_bp.route('/')
def get_products():
    """Маршрут для получения списка товаров."""
    return jsonify(products)

@product_bp.route('/<int:product_id>')
def get_product(product_id):
    """Маршрут для получения информации о конкретном товаре."""
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Товар не найден"}), 404
    return jsonify(product)
