from flask import Blueprint, render_template

contact_bp = Blueprint('contact', __name__, url_prefix='/contacts')

@contact_bp.route('/')
def show_contacts():
    """Страница с контактной информацией."""
    return render_template('contacts.html')
