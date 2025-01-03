from flask import Blueprint, render_template

basket_bp = Blueprint('basket', __name__, url_prefix='/basket')

@basket_bp.route('/')
def view_basket():
    """Страница корзины."""
    return render_template('basket.html')
