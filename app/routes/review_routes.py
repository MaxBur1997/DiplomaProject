from flask import Blueprint, request, jsonify

# Создаем Blueprint для маршрутов отзывов
review_bp = Blueprint('review', __name__, url_prefix='/reviews')

# Временные данные для тестирования
reviews = [
    {"id": 1, "product_id": 1, "user_name": "Иван", "rating": 5, "comment": "Очень вкусно!",
     "created_at": "2023-12-01T10:00:00"},
    {"id": 2, "product_id": 2, "user_name": "Мария", "rating": 4, "comment": "Хороший шоколадный пончик.",
     "created_at": "2023-12-02T14:30:00"}
]


@review_bp.route('/')
def get_reviews():
    """Маршрут для получения всех отзывов."""
    return jsonify(reviews)


@review_bp.route('/<int:product_id>')
def get_reviews_for_product(product_id):
    """Маршрут для получения отзывов к конкретному товару."""
    product_reviews = [r for r in reviews if r["product_id"] == product_id]
    return jsonify(product_reviews)


@review_bp.route('/', methods=['POST'])
def add_review():
    """Маршрут для добавления нового отзыва."""
    data = request.get_json()
    if not all(key in data for key in ("product_id", "user_name", "rating")):
        return jsonify({"error": "Некорректные данные"}), 400

    new_review = {
        "id": len(reviews) + 1,
        "product_id": data["product_id"],
        "user_name": data["user_name"],
        "rating": data["rating"],
        "comment": data.get("comment", ""),
        "created_at": "2023-12-31T12:00:00"
    }
    reviews.append(new_review)
    return jsonify(new_review), 201
