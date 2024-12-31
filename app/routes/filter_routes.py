from flask import Blueprint, jsonify, request
from app.models import Product

filter_bp = Blueprint('filter', __name__, url_prefix='/filters')


@filter_bp.route('/')
def filter_products():
    """Маршрут для фильтрации товаров."""
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    query = Product.query
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    filtered_products = query.all()
    product_list = [
        {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "image_url": product.image_url
        }
        for product in filtered_products
    ]
    return jsonify(product_list)
