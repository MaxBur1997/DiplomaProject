from flask import Blueprint


def register_routes(app):
    """Регистрирует маршруты для приложения."""
    from app.routes.product_routes import product_bp
    from app.routes.review_routes import review_bp
    from app.routes.filter_routes import filter_bp

    app.register_blueprint(product_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(filter_bp)
