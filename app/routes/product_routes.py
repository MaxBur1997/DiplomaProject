from flask import Blueprint, render_template
from app.models import Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/list')
def list_products():
    """Страница со списком товаров."""
    products = Product.query.all()
    return render_template('filter_results.html', products=products)  # Используем filter_results.html

@product_bp.route('/detail/<int:product_id>')
def product_detail(product_id):
    """Детальная информация о товаре."""
    product = Product.query.get(product_id)
    if not product:
        return render_template('error.html', message="Product not found"), 404
    return render_template('product_detail.html', product=product)
