from app import db
from datetime import datetime

class Product(db.Model):
    """Модель для представления товаров (пончиков)."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)  # Ссылка на изображение
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Связь с отзывами (один ко многим)
    reviews = db.relationship('Review', backref='product', lazy=True)

    def __repr__(self):
        return f'<Product {self.name}>'


class Review(db.Model):
    """Модель для представления отзывов пользователей."""
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Оценка от 1 до 5
    comment = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Review {self.id} - Product {self.product_id}>'
