from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Создаем экземпляры расширений
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class='config.Config'):
    """Фабрика приложения Flask."""
    app = Flask(__name__)

    # Загружаем конфигурацию
    app.config.from_object(config_class)

    # Инициализация расширений
    db.init_app(app)
    migrate.init_app(app, db)

    # Регистрация маршрутов
    from app.routes.product_routes import product_bp
    from app.routes.review_routes import review_bp
    from app.routes.filter_routes import filter_bp

    app.register_blueprint(product_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(filter_bp)

    return app
