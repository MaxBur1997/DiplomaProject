from app.routes.product_routes import product_bp
from app.routes.review_routes import review_bp
from app.routes.home_routes import home_bp
from app.routes.basket_routes import basket_bp
from app.routes.contact_routes import contact_bp

def register_routes(app):
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(review_bp, url_prefix='/reviews')
    app.register_blueprint(home_bp)
    app.register_blueprint(basket_bp)
    app.register_blueprint(contact_bp)
