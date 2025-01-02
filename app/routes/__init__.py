from app.routes.product_routes import product_bp
from app.routes.review_routes import review_bp
from app.routes.filter_routes import filter_bp
from app.routes.home_routes import home_bp

def register_routes(app):
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    app.register_blueprint(filter_bp, url_prefix='/filters')
    app.register_blueprint(home_bp)
