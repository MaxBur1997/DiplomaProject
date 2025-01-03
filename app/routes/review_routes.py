from flask import Blueprint, jsonify, request, redirect, url_for, flash
from app.models import Review, Product
from app import db

review_bp = Blueprint('review', __name__, url_prefix='/reviews')

@review_bp.route('/add', methods=['POST'])
def add_review():
    """Маршрут для добавления нового отзыва."""
    product_id = request.form.get('product_id')
    user_name = request.form.get('user_name')
    rating = request.form.get('rating')
    comment = request.form.get('comment')

    if not all([product_id, user_name, rating]):
        flash("Please fill in all required fields.", "error")
        return redirect(request.referrer)

    # Проверяем, существует ли товар
    product = Product.query.get(product_id)
    if not product:
        flash("Product not found.", "error")
        return redirect(request.referrer)

    new_review = Review(
        product_id=product_id,
        user_name=user_name,
        rating=int(rating),
        comment=comment
    )
    db.session.add(new_review)
    db.session.commit()

    flash("Your review has been added successfully!", "success")
    return redirect(url_for('product.product_detail', product_id=product_id))
