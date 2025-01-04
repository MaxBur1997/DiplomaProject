import os

class Config:
    """Базовая конфигурация приложения."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a3f1e2c8d6b4f0a3c9e8f7a1c3d2e6f5')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
