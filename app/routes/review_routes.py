from flask import Blueprint, jsonify, request
from app.models import Review, Product
from app import db

review_bp = Blueprint('review', __name__, url_prefix='/reviews')


@review_bp.route('/')
def get_reviews():
    """Маршрут для получения всех отзывов."""
    reviews = Review.query.all()
    review_list = [
        {
            "id": review.id,
            "product_id": review.product_id,
            "user_name": review.user_name,
            "rating": review.rating,
            "comment": review.comment,
            "created_at": review.created_at.isoformat()
        }
        for review in reviews
    ]
    return jsonify(review_list)


@review_bp.route('/<int:product_id>')
def get_reviews_for_product(product_id):
    """Маршрут для получения отзывов к конкретному товару."""
    reviews = Review.query.filter_by(product_id=product_id).all()
    review_list = [
        {
            "id": review.id,
            "product_id": review.product_id,
            "user_name": review.user_name,
            "rating": review.rating,
            "comment": review.comment,
            "created_at": review.created_at.isoformat()
        }
        for review in reviews
    ]
    return jsonify(review_list)


@review_bp.route('/', methods=['POST'])
def add_review():
    """Маршрут для добавления нового отзыва."""
    data = request.get_json()
    if not all(key in data for key in ("product_id", "user_name", "rating")):
        return jsonify({"error": "Некорректные данные"}), 400

    # Проверяем, существует ли товар
    product = Product.query.get(data["product_id"])
    if not product:
        return jsonify({"error": "Товар не найден"}), 404

    new_review = Review(
        product_id=data["product_id"],
        user_name=data["user_name"],
        rating=data["rating"],
        comment=data.get("comment", "")
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify({
        "id": new_review.id,
        "product_id": new_review.product_id,
        "user_name": new_review.user_name,
        "rating": new_review.rating,
        "comment": new_review.comment,
        "created_at": new_review.created_at.isoformat()
    }), 201
