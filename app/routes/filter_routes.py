from flask import Blueprint, request, jsonify

# Создаем Blueprint для маршрутов фильтрации
filter_bp = Blueprint('filter', __name__, url_prefix='/filters')

# Временные данные для тестирования
products = [
    {"id": 1, "name": "Классический пончик", "price": 50.0, "description": "Классический вкус.",
     "image_url": "/static/images/classic.png"},
    {"id": 2, "name": "Шоколадный пончик", "price": 60.0, "description": "С шоколадной глазурью.",
     "image_url": "/static/images/chocolate.png"}
]


@filter_bp.route('/')
def filter_products():
    """Маршрут для фильтрации товаров."""
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    filtered_products = products
    if min_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] >= min_price]
    if max_price is not None:
        filtered_products = [p for p in filtered_products if p["price"] <= max_price]

    return jsonify(filtered_products)
