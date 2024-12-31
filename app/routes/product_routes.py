from flask import Blueprint, jsonify, request
from app.models import Product
from app import db

product_bp = Blueprint('product', __name__, url_prefix='/products')


@product_bp.route('/')
def get_products():
    """Маршрут для получения списка товаров."""
    products = Product.query.all()
    product_list = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "image_url": product.image_url
        }
        for product in products
    ]
    return jsonify(product_list)


@product_bp.route('/<int:product_id>')
def get_product(product_id):
    """Маршрут для получения информации о конкретном товаре."""
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Товар не найден"}), 404
    return jsonify({
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": product.price,
        "image_url": product.image_url
    })


@product_bp.route('/', methods=['POST'])
def add_product():
    """Маршрут для добавления нового товара."""
    data = request.get_json()
    if not all(key in data for key in ("name", "description", "price")):
        return jsonify({"error": "Некорректные данные"}), 400

    new_product = Product(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        image_url=data.get("image_url")
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({
        "id": new_product.id,
        "name": new_product.name,
        "description": new_product.description,
        "price": new_product.price,
        "image_url": new_product.image_url
    }), 201
