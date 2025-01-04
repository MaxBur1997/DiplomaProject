from flask import Blueprint, request, render_template, redirect, url_for
from app.models import Product
from sqlalchemy import func



product_bp = Blueprint('product', __name__)


@product_bp.route('/products/list', methods=['GET', 'POST'])
def list_products():
    """Отображение списка продуктов с фильтрацией."""
    query = Product.query

    # Получение параметров фильтрации из GET-запроса
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    name = request.args.get('name', '').strip()

    # Применение фильтров
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)
    if name:
        # Фильтрация имени независимо от регистра
        query = query.filter(func.lower(Product.name).like(f"%{name.lower()}%"))

    products = query.all()

    return render_template(
        'product_list.html',
        products=products,
        min_price=min_price,
        max_price=max_price,
        name=name
    )


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
