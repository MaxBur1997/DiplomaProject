from flask import Blueprint, render_template, request
from app.models import Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/list')
def list_products():
    """Страница со списком товаров."""
    products = Product.query.all()
    return render_template('filter_results.html', products=products)  # Используем filter_results.html

@product_bp.route('/detail/<int:product_id>')
def product_detail(product_id):
    """Детальная информация о товаре с сортировкой отзывов."""
    product = Product.query.get(product_id)
    if not product:
        return render_template('error.html', message="Product not found"), 404

    # Получаем параметры сортировки из URL
    sort_by = request.args.get('sort_by', 'date')  # По умолчанию сортируем по дате
    order = request.args.get('order', 'desc')  # По умолчанию убывание

    # Сортируем отзывы
    reviews_query = product.reviews
    if sort_by == 'rating':
        reviews_query = sorted(reviews_query, key=lambda r: r.rating, reverse=(order == 'desc'))
    elif sort_by == 'date':
        reviews_query = sorted(reviews_query, key=lambda r: r.created_at, reverse=(order == 'desc'))

    return render_template('product_detail.html', product=product, reviews=reviews_query, sort_by=sort_by, order=order)
