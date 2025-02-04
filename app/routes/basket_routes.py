from flask import Blueprint, session, redirect, url_for, render_template, request, flash
from app.models import Product

basket_bp = Blueprint('basket', __name__, url_prefix='/basket')


def get_basket():
    """Получить корзину в правильном формате."""
    basket = session.get('basket', [])
    # Убедимся, что каждая запись в корзине имеет правильный формат
    return [
        {
            "product_id": int(item.get("product_id", 0)),
            "quantity": int(item.get("quantity", 0)),
        }
        for item in basket if isinstance(item, dict)
    ]


@basket_bp.route('/', methods=['GET', 'POST'])
def view_basket():
    """Отображение корзины и обработка заказа."""
    basket = get_basket()
    total_price = 0
    basket_details = []

    for item in basket:
        product = Product.query.get(item['product_id'])
        if product:
            item_total = product.price * item['quantity']
            basket_details.append({
                'product': product,
                'quantity': item['quantity'],
                'total': item_total
            })
            total_price += item_total

    if request.method == 'POST':
        if not basket:
            flash('To place an order, add items to the basket.', 'error')
            return redirect(url_for('basket.view_basket'))
        return redirect(url_for('basket.place_order'))

    return render_template('basket.html', basket_details=basket_details, total_price=total_price)


@basket_bp.route('/add/<int:product_id>', methods=['POST'])
def add_to_basket(product_id):
    """Добавление товара в корзину."""
    quantity = int(request.form.get('quantity', 1))
    basket = get_basket()

    for item in basket:
        if item['product_id'] == product_id:
            item['quantity'] += quantity
            session['basket'] = basket
            session.modified = True
            flash("Product added to the basket.")
            return redirect(url_for('product.product_detail', product_id=product_id))

    basket.append({"product_id": product_id, "quantity": quantity})
    session['basket'] = basket
    session.modified = True
    flash("Product added to the basket.")
    return redirect(url_for('product.product_detail', product_id=product_id))


@basket_bp.route('/remove/<int:product_id>', methods=['POST'])
def remove_from_basket(product_id):
    """Удаление товара из корзины."""
    basket = get_basket()
    basket = [item for item in basket if item['product_id'] != product_id]
    session['basket'] = basket
    session.modified = True
    flash("Product removed from the basket.")
    return redirect(url_for('basket.view_basket'))


@basket_bp.route('/clear', methods=['POST'])
def clear_basket():
    """Очистить корзину."""
    session['basket'] = []
    session.modified = True
    flash("Basket cleared.")
    return redirect(url_for('basket.view_basket'))


@basket_bp.route('/place_order', methods=['GET', 'POST'])
def place_order():
    """Форма оформления заказа."""
    basket = get_basket()
    basket_details = []
    total_price = 0

    for item in basket:
        product = Product.query.get(item['product_id'])
        if product:
            item_total = product.price * item['quantity']
            basket_details.append({
                'product': product,
                'quantity': item['quantity'],
                'total': item_total
            })
            total_price += item_total

    if request.method == 'POST':
        # Обработка данных формы (имя, контакты и т.д.)
        flash('Order placed successfully!', 'success')
        session['basket'] = []  # Очистить корзину после оформления заказа
        return redirect(url_for('basket.payment_system'))

    return render_template('place_order.html', basket_details=basket_details, total_price=total_price)



@basket_bp.route('/payment', methods=['GET', 'POST'])
def payment_system():
    """Страница платежной системы."""
    return render_template('payment_system.html')

