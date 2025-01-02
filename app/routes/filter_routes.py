from flask import Blueprint, render_template, request
from app.models import Product

filter_bp = Blueprint('filter', __name__)


@filter_bp.route('/filter_page')
def filter_page():
    """Страница для ввода параметров фильтрации."""
    return render_template('home.html')  # Используем существующий шаблон для фильтрации


@filter_bp.route('/results')
def filter_results():
    """Отображение результатов фильтрации."""
    # Получаем параметры из URL
    name = request.args.get('name', '').strip()
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    # Создаём базовый запрос
    query = Product.query

    # Фильтруем по имени, если задано
    if name:
        query = query.filter(Product.name.ilike(f'%{name}%'))

    # Фильтруем по диапазону цен, если указаны
    if min_price is not None:
        query = query.filter(Product.price >= min_price)
    if max_price is not None:
        query = query.filter(Product.price <= max_price)

    # Выполняем запрос
    filtered_products = query.all()

    return render_template('filter_results.html', products=filtered_products)
